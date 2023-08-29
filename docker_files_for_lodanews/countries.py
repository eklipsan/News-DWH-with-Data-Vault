from loadtran import load_json
 # Create country classes to download news by category
 
class Russia:
    
    # Load top news from Russia
    def load_russian_top(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=ru&category=top&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='russian top'
        )
    
    # Load sports news from Russia
    def load_russian_sports(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=ru&category=sports&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='russian sports'
        )
    
    # Load technology news from Russia
    def load_russian_technology(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=ru&category=technology&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='russian technology'
        )
    
    # Load business news from Russia
    def load_russian_business(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=ru&category=business&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='russian business'
        )
    

class UnitedStates:
    
    # Load top news from the United States
    def load_usa_top(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=us&category=top&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='usa top'
        )
    
    # Load sports news from the United States
    def load_usa_sports(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=us&category=sports&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='usa sports'
        )
    
    # Load technology news from the United States
    def load_usa_technology(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=us&category=technology&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='usa technology'
        )
    
    # Load business news from the United States
    def load_usa_business(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=us&category=business&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='usa business'
        )