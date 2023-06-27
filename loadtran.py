import json
from datetime import datetime
import requests
import psycopg2


def load_json(url: str, name: str = '[language category]') -> list:
        """
        Downloads a JSON file through an API.
        The JSON file consists of three parts:
        - status: upload status (e.g. 'success')
        - totalResults: result
        - results: list with strings of words
        - nextPage: link to the next page
        Args:
        - url: str - URL of the JSON file to download
        - name: str - optional name of the file being downloaded
        Returns:
        - list: list of strings of words from the JSON file, if successful
        - str: error message, if unsuccessful
        """
        error_msg = f"ERROR: Could not load {name}."
        try:
            # Attempt to download the JSON file
            raw_data = json.loads(requests.get(url).text)
        except:
            # If unsuccessful, log the error message to a file and return the error message
            with open('report.log', 'a') as f:
                print(error_msg, 'Something happened with the URL (could not get JSON format or your URL is invalid)', datetime.today(), file=f)
            return error_msg
        if raw_data['status'] == 'success':
            # If successful, log a success message to a file and return the list of words
            with open('report.log', 'a') as f:
                print(f'SUCCESS: {name} has loaded successfully', datetime.today(), file=f)
            return raw_data['results']
        else:
            # If unsuccessful, log the error message to a file and return the error message
            with open('report.log', 'a') as f:
                print(error_msg, 'Something happened to the server (401 or your limit of API requests is exceeded)', datetime.today(), file=f)
            return error_msg


def clean(raw_data):
    """
    Returns a cleaned and converted set of dictionary data in a list.
    Each row is stored as a dictionary. All strings are in a list.
    The dictionary keys (attributes) which are given as input:
    title link keywords creator video_url description content pubDate image_url source_id category country language
    The keys (attributes) of the dictionary, which are returned:
    title link keywords description content pubDate pubTime source_id category country language
    Args:
    raw_data (list): A list of dictionaries containing raw data.
    Returns:
    list: A list of dictionaries containing cleaned data.
    """
    # Check if input is a list of dictionaries
    if isinstance(raw_data, list):
        # Loop through each dictionary in the list
        for row in raw_data:
            # Remove unnecessary keys
            del row['video_url']
            del row['image_url']
            del row['creator']
            del row['content']
            # Split pubDate into date and time and update dictionary
            dateandtime = row['pubDate'].split()
            del row['pubDate']
            row['pubDate'] = dateandtime[0]
            row['pubTime'] = dateandtime[1]
            # Check if category, country, and keywords are lists and update dictionary with first element if they are
            if row['category'] is not None and isinstance(row['category'], list):
                row['category'] = row['category'][0]
            if row['country'] is not None and isinstance(row['country'], list):
                row['country'] = row['country'][0]
            if row['keywords'] is not None and isinstance(row['keywords'], list):
                row['keywords'] = row['keywords'][0]

        return raw_data
    else:
        # Log error if input is not a list of dictionaries
        with open('report.log', 'a') as f:
            print('ERROR: Wrong type of data in function "clean"', datetime.today())     


def load_staging(cleaned_data, name_data):
    """
    This function loads cleaned data from different sources and loads it into the operational layer.
    The data to connect to the database is not encrypted for openness.
    """
    # Connect to the database
    con = psycopg2.connect(
            host = 'snuffleupagus.db.elephantsql.com',
            database = 'wpnpltzb',
            user = 'wpnpltzb',
            password = 'zkU2gefzyFyITIjarDapIqKsq99_aFp9'
        )
    # Create a cursor object
    cur = con.cursor()
    # Fetch all titles from the News table
    cur.execute("SELECT title from News")
    checking_list = [i[0] for i in cur.fetchall()]
    # Insert cleaned data into the News table
    for row in cleaned_data:
        if row['title'] not in checking_list:
            try:
                cur.execute(
            '''
            insert into News (title, link, keyword, description, source_id, country, language, pubDate, pubTime) values 
            (%(title)s, %(link)s, %(keywords)s, %(description)s, %(source_id)s, %(country)s, %(language)s, %(pubDate)s, %(pubTime)s)
            ''',
            row
            )
            except psycopg2.Error as e:
                # Log any errors to a file
                with open('report.log', 'a') as f:
                    print(f'ERROR: Something happened with loading staging {e} {datetime.today()}', file=f)
                return e
    # Log success to a file
    with open('report.log', 'a') as f:
        print(f'SUCCESS: staging loading is done {datetime.today()}', file=f)
    # Delete any rows with null keyword or description values
    cur.execute('''
    delete from News
    where keyword is null or description is null
    ''')
    # Commit changes and close the connection
    con.commit()
    con.close()
    # Log success to a file
    with open('report.log', 'a') as f:
        print(f'SUCCESS: {name_data} for staging layer has loaded successfully {datetime.today()}', file=f)
    
    return True