from countries import Russia, UnitedStates
from loadtran import clean, load_staging
from datetime import datetime

usa = UnitedStates()
russia = Russia()
try:
    russian_sports = clean(russia.load_russian_sports())
    russian_business = clean(russia.load_russian_business())
    russian_technology = clean(russia.load_russian_technology())

    usa_sports = clean(usa.load_usa_sports())
    usa_business = clean(usa.load_usa_business())
    usa_technology = clean(usa.load_usa_technology())

    print(load_staging(russian_sports, 'russian_sports'))
    print(load_staging(russian_business, 'russian_business'))
    print(load_staging(russian_technology, 'russian_technology'))
    print()
    print(load_staging(usa_sports, 'usa_sports'))
    print(load_staging(usa_business, 'usa_business'))
    print(load_staging(usa_technology, 'usa_technology'))
    print("DONE")
    with open('report.log', 'a') as f:
        print(f"SUCCESS: Loading into the staging layer has done {datetime.today()}",file=f)
except:
    with open('report.log', 'a') as f:
        print(f"ERROR: Loading into the staging layer is not successful {datetime.today()}", file=f)
    print("Something happened to main file")