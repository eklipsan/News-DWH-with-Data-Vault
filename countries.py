from loadtran import load_json

# create country classes to download news by category
class Russia:
    def load_russian_top(self):
        return load_json(
        url='https://newsdata.io/api/1/news?country=ru&category=top&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
        name = 'russian top'
        )


    def load_russian_sports(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=ru&category=sports&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='russian sports'
        )


    def load_russian_technology(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=ru&category=technology&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='russian technology'
        )


    def load_russian_business(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=ru&category=business&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='russian business'
        )


class UnitedStates:
    def load_usa_top(self):
        return load_json(
        url='https://newsdata.io/api/1/news?country=us&category=top&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
        name = 'usa top'
        )


    def load_usa_sports(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=us&category=sports&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='usa sports'
        )


    def load_usa_technology(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=us&category=technology&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='usa technology'
        )


    def load_usa_business(self):
        return load_json(
            url=r'https://newsdata.io/api/1/news?country=us&category=business&apikey=pub_23940db00d0c79dab836398603f98450d0c07',
            name='usa business'
        )