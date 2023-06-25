import json
from datetime import datetime
import requests
import psycopg2


def load_json(url: str, name: str =  '[language category]'):
    """
    downloading the json file through the api.
    The json itself consists of three parts:
        status - upload status (e.g. 'success') 
        totalResults - result
        results - list with strings of words
        nextPage - link to the next page
    """
    error = f"ERROR: Could not load {name}."
    try:
        raw_data = json.loads(requests.get(url).text)
    except:
        with open('report.log', 'a') as f:
            print(error,'Something happened with the url(could not get json format or your url is invalid)', datetime.today(), file=f)
        return error
    
    if raw_data['status'] == 'success':
        with open('report.log', 'a') as f:
            print(f'SUCCESS: {name} has loaded successfully', datetime.today(), file=f)
        return raw_data['results']
    else:
        with open('report.log', 'a') as f:
            print(error, 'something happened to the server(401 or your limit of api-requests is exceeded)', datetime.today(), file=f)
        return f"ERROR: Could not load {name}"


def clean(raw_data):
    """
    Returns a cleaned and converted set of dictionary data in a list.
    Each row is stored as a dictionary. All strings are in a list.
    The dictionary keys (attributes) which are given as input:
    title link keywords creator video_url description content pubDate image_url source_id category country language
    The keys (attributes) of the dictionary, which are returned:
    title link keywords description content pubDate pubTime source_id category country language

    """
    if isinstance(raw_data, list):
        for row in raw_data:
            del row['video_url']
            del row['image_url']
            del row['creator']
            del row['content']
            dateandtime = row['pubDate'].split()
            del row['pubDate']
            row['pubDate'] = dateandtime[0]
            row['pubTime'] = dateandtime[1]
            if row['category'] is not None and isinstance(row['category'], list):
                row['category'] = row['category'][0]
            if row['country'] is not None and isinstance(row['country'], list):
                row['country'] = row['country'][0]
            if row['keywords'] is not None and isinstance(row['keywords'], list):
                row['keywords'] = row['keywords'][0]

        return raw_data
    else:
        with open('report.log', 'a') as f:
            print('ERROR: Wrong type of data in function "clean"', datetime.today())     


def load_staging(cleaned_data, name_data):
    """
    The function loads cleaned data from different sources and loads it into the operational layer.
    The data to connect to the database is not encrypted for openness.
    """
    con = psycopg2.connect(
            host = 'snuffleupagus.db.elephantsql.com',
            database = 'wpnpltzb',
            user = 'wpnpltzb',
            password = 'zkU2gefzyFyITIjarDapIqKsq99_aFp9'
        )

    cur = con.cursor()
    cur.execute("SELECT title from News")
    checking_list = [i[0] for i in cur.fetchall()]

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
                with open('report.log','a') as f:
                    print(f'ERROR: Something happened with loading staging {e} {datetime.today()}', file=f)
                return e
    with open('report.log','a') as f:
        print(f'SUCCESS: staging loading is done {datetime.today()}',file=f)
                    
    cur.execute('''
    delete from News
    where keyword is null or description is null
    ''')
                    
    con.commit()
    con.close()
    
    with open('report.log','a') as f:
        print(f'SUCCESS: {name_data} for staging layer has loaded successfully {datetime.today()}', file=f)
    
    return True