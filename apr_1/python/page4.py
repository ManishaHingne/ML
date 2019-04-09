from nltk.corpus import stopwords
from heapq import nlargest
from nltk.stem import PorterStemmer

class Source:
    def __init__(self, fileName, category):
        self.__fileName = fileName
        self.__category = category
        self.__stopWords = stopwords.words('english')
        self.__finalWords = []
        self.__wordCount = {}
        self.__topWords = []

    def getTopWords(self):
        return self.__topWords

    def removeNumers(self, line):
        for number in range(10):
            line = line.replace(str(number), '')
        return line

    def removeStopwords(self, line):
        for word in self.__stopWords:
            line = line.replace(word, '')
        return line

    def removeSpecialCharacters(self, line):
        for ch in ["'", '"', ',', ':', '@', '#', '$', '%', '^', '&', '!', '~', '.']:
            line = line.replace(ch, '')
        return line

    def removeWhitespaces(self, line):
        line = line.replace('\t', '')
        line = line.replace('\n', '')
        line = line.replace('\r\n', '')
        return line

    def processContents(self):
        file = open(self.__fileName, 'r')

        stemmer = PorterStemmer()

        # get the  lines
        lines = file.readlines()
        for line in lines:

            # convert the line into lower case
            line = line.lower()

            # remove all the special characters
            line = self.removeSpecialCharacters(line)

            #  remove all the numbers
            line = self.removeNumers(line)

            # remove all the whitespaces
            line = self.removeWhitespaces(line)

            # break down the line into words
            words = line.split(' ')


            for word in words:

                # stem the word
                    # word = stemmer.stem(word)

                # consider the word if it is not a stop word and the  length is > 0
                if word not in self.__stopWords and len(word) > 0:
                    self.__finalWords.append(word)

                    # check if word is present in the dictionary
                    # yes: increment the count
                    # no: set the count = 1

                    if self.__wordCount.get(word) == None:
                        self.__wordCount[word] = 1
                    else:
                        self.__wordCount[word] += self.__wordCount[word]



        # print(self.__finalWords)
        # print(self.__wordCount)


        # find top 10 most repeated words
        self.__topWords = nlargest(40, self.__wordCount, key=self.__wordCount.get)
        # print(self.__topWords)



# s1 = Source('./election/1.txt', 'election')
# s1.processContents()

# steming the document
# play, playing, played => play

topWords = []
for category in ['election', 'ipl', 'entertainment']:
    # collection top words in a category
    words = []
    for index in range(1, 5):
        s = Source('./{}/{}.txt'.format(category, index), category)
        s.processContents()
        for word in s.getTopWords():
            if word not in words:
                words.append(word)

    topWords.append({'category': category, 'words': words})

print(topWords)

# get the new NEWS article and try to classify based on the top words
s = Source('test.txt', '')
s.processContents()
print(s.getTopWords())

# find the category based on the top words
finalResult = []
# finalResult {
#   'category': 'election',
#   'count': 10
# }

# finalResult {
#   'category': 'ipl',
#   'count': 20
# }

topCount, finalCategory = 0, ''
for mapping in topWords:
    dict = {}
    dict['category'] = mapping['category']
    dict['count'] = 0

    # get all the top words from the new article
    for word in s.getTopWords():
        # word = ipl,
        for categoryWord  in mapping['words']:
            if word == categoryWord:
                dict['count'] += 1
                break

    finalResult.append(dict)
    if dict['count'] > topCount:
        topCount = dict['count']
        finalCategory = dict['category']


print(finalResult)
print('the article belogs to {} category as {} words are repeated'.format(finalCategory, topCount))






















