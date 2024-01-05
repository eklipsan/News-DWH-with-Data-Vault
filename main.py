from countries import Russia, UnitedStates
from loadtran import clean, load_staging
from datetime import datetime

# create instances of Russia and UnitedStates classes
usa = UnitedStates()
russia = Russia()
try:
    # load and clean data from Russia
    russian_sports = clean(russia.load_russian_sports())
    russian_business = clean(russia.load_russian_business())
    russian_technology = clean(russia.load_russian_technology())

    # load and clean data from USA
    usa_sports = clean(usa.load_usa_sports())
    usa_business = clean(usa.load_usa_business())
    usa_technology = clean(usa.load_usa_technology())

    # load data into staging layer and print success message
    print(load_staging(russian_sports, 'russian_sports'))
    print(load_staging(russian_business, 'russian_business'))
    print(load_staging(russian_technology, 'russian_technology'))
    print()
    print(load_staging(usa_sports, 'usa_sports'))
    print(load_staging(usa_business, 'usa_business'))
    print(load_staging(usa_technology, 'usa_technology'))
    print("DONE")

    # write success message to log file
    with open('report.log', 'a') as f:
        print(f"SUCCESS: Loading into the staging layer has been completed"
              "{datetime.today()}", file=f)
except:
    # write error message to log file and print error message to console
    with open('report.log', 'a') as f:
        print(
            f"ERROR: Loading into the staging layer has not been successful {datetime.today()}", file=f)
    print("Something went wrong with the main file")
