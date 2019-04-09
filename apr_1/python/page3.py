import urllib3

class Source:
    def __init__(self, url, fileName):
        self.__url = url
        self.__fileName = fileName

    def downloadContents(self):
        http = urllib3.PoolManager()
        request = http.request('GET', self.__url)
        data = request.data
        self.processContents(data)
        # file = open('./election/page.html', 'w')
        # file.write(str(data))
        # file.close()

    def processContents(self, data):
        from bs4 import BeautifulSoup
        # file = open('./election/page.html', 'r')
        # data = file.read()
        soup = BeautifulSoup(data, 'html.parser')

        # title
        # div = soup.find('div', { 'class': 'story-highlight' })
        # h1 = div.find('h1')
        # title = h1.text.replace('\n', '').replace('\t', '')
        # print(title)

        # content
        divContent = soup.find('div', {'class': 'story-details'})
        if divContent == None:
            divContent = soup.find('div', {'class': 'blogRight'})
        paras = divContent.findAll('p')
        content = ''
        for para in paras:
            content += para.text
        # print(content)

        file = open(self.__fileName, 'w')
        file.write(content)
        file.close()



def downloadContentsFromInternet(urls, category):
    count = 1
    for url in urls:
        fileName = './{}/{}.txt'.format(category, count)
        s = Source(url, fileName)
        s.downloadContents()
        count += 1


election = [
    'https://www.hindustantimes.com/constituency-watch/lok-sabha-elections-2019-will-union-minister-jual-oram-get-fifth-time-lucky-in-odisha-s-sundargarh-constituency/story-r1QG410WHi3pCq0qRl10jL.html',
    'https://www.hindustantimes.com/lok-sabha-elections/lok-sabha-elections-2019-priyanka-gandhi-urged-to-visit-temple-of-saint-who-blessed-indira-after-1977-rout/story-Sxl24agu2UQboaCbnIA6WO.html',
    'https://www.hindustantimes.com/lok-sabha-elections/lok-sabha-elections-2019-live-updates-pm-narendra-modi-rahul-gandhi-telangana-bjp-congress-ami-shah/story-zI1hPQygVJbdH0JpqxEyYK.html',
    'https://www.hindustantimes.com/lok-sabha-elections/lok-sabha-elections-2019-bjp-looks-to-retain-damoh-in-madhya-pradesh/story-r09lDNTnQM8h9EvH7WlClK.html'
]

# downloadContentsFromInternet(election, 'election')


ipl = [
    'https://www.hindustantimes.com/cricket/live-ipl-score-dc-vs-kkr-match-10-delhi-capitals-vs-kolkata-knight-riders-cricket-score-updates-at-feroz-shah-kotla/story-akCq0LKc4YdUb5bob15dAJ.html',
    'https://www.hindustantimes.com/cricket/kxip-vs-mi-another-umpiring-howler-in-ipl-as-r-ashwin-bowls-seven-ball-first-over-in-mohali/story-QldMNqXjOmE88oHKY5mYgI.html',
    'https://www.hindustantimes.com/cricket/ipl-2019-csk-vs-rr-statistical-highlights-ms-dhoni-sanju-samson-set-records/story-RheB2yTyTrmwaCi04FgocO.html',
    'https://www.hindustantimes.com/cricket/youngest-ipl-debutant-prayas-managing-rcb-and-cbse-tests-at-same-time/story-HQOi9Q6MCuSprgv0RSp5OM.html'
]

# downloadContentsFromInternet(ipl, 'ipl')

entertainment = [
    'https://www.hindustantimes.com/bollywood/parineeti-chopra-shares-pic-with-sania-mirza-s-son-says-she-wants-to-keep-him-forever/story-Poq9WosbB5NRRXa45qxoMJ.html',
    'https://www.hindustantimes.com/hollywood/avengers-endgame-director-joe-russo-says-sitcoms-influenced-which-characters-to-get-rid-of/story-jPFDZlV01YGkkanrIZsUGL.html',
    'https://www.hindustantimes.com/bollywood/happy-birthday-ajay-devgn-4-times-when-he-hilariously-roasted-wife-kajol-on-instagram/story-XuH9rWSf1eVHnmNZ8wuK1O.html',
    'https://www.hindustantimes.com/hollywood/ar-rahman-joe-russo-release-marvel-s-hindi-anthem-before-avengers-endgame-watch-video/story-91vcdvKYFFa1a45AzTXtsI.html'
]

# downloadContentsFromInternet(entertainment, 'entertainment')

# e1 = Source('https://www.hindustantimes.com/constituency-watch/lok-sabha-elections-2019-will-union-minister-jual-oram-get-fifth-time-lucky-in-odisha-s-sundargarh-constituency/story-r1QG410WHi3pCq0qRl10jL.html', './election/e1.txt')
# e1.downloadContents()

#
s = Source('https://www.hindustantimes.com/bollywood/sara-ali-khan-slays-on-mag-cover-says-she-is-thankful-to-kareena-kapoor-because-she-makes-my-father-happy/story-z8N2iUI3BlTRxFGXbIzX4L.html', 'test.txt')
s.downloadContents()

