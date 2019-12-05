from nltk.corpus import wordnet as wn
import json

#synonyms = wordnet.synset("saspense")
#print(synonyms.name())

syns = wn.synsets('saspense')

for ss in syns :
    print(ss.name(), ss.lemma_names())
print(f"{'-'*20}")


synonyms = []
antonyms = []
wordList = ["anxiety","apprehension","confusion","doubt","insecurity","tension","thriller","uncertainty","chiller","dilemma","eagerness","expectancy","expectation","grabber","hesitancy","hesitation","impatience","indecision","indecisiveness","irresolution","perplexity","potboiler","wavering","cliff-hanger","cloak and dagger","page-turner",

            ]

for word in wordList:
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    set(synonyms)
    set(antonyms)
    #print(set(synonyms))
    #print(set(antonyms))

# start = 0
# finish = len(synonyms)
# counter = 0
# thisIsAmasing = str
#
# for word in synonyms:
#     if counter == start:
#         thisIsAmasing += ('{'+ str(word) + ':saspense')
#     elif counter == finish:
#         thisIsAmasing += (str(word) + ':saspense}')
#     else:
#         thisIsAmasing += ( str(word) + ':saspense')
#     counter += 1
#
# print(thisIsAmasing)
with open('saspense.json', 'w') as file:
    file.write(json.dumps({word: 'saspense' for word in synonyms}, indent=4))
