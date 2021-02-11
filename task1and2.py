from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import StringIO
from itertools import chain
from nltk.tokenize import word_tokenize
import pandas as pd
from collections import Counter
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

languages = ["javascript", "python", "java", "php", "c#", "c++", "ruby", "css", "typescript", "c", "swift", "objective-c", "scala", "r",
             "go", "shell", "powershell", "perl", "kotlin", "haskell", "matlab", "sql", "rust", "typescript", "node.js", "pascal", "groovy", "d", "assembler", "pl/sql", "vue.js"]

platforms = ["windows", "macos", "linux", "ios", "chromeos", "ipados", "debian", "centos", "tizen", "freebsd", "bsd", "ubuntu", "windows server"]

data = pd.read_csv('questions.csv', sep='\t', encoding='utf-8', low_memory=False)

df = pd.DataFrame(data=data, dtype=str)
print(df['tags'])
df['tags'] = df['tags'].map(lambda x: x.replace(",", ''))

list_tags = []

for i in range(len(df['tags'])):
    words = word_tokenize(df['tags'][i])
    for j in range(len(words)):
        list_tags.append(words[j])
print(list_tags)

languages_tags = []
for i in range(len(list_tags)):
    for j in range(len(languages)):
        if languages[j] == list_tags[i]:
            languages_tags.append(list_tags[i])

platforms_tags = []
for i in range(len(list_tags)):
    for j in range(len(platforms)):
        if platforms[j] == list_tags[i]:
            platforms_tags.append(list_tags[i])

c = Counter(list_tags)
# print(c)
#
# print(platforms_tags)
#
spisok1 = ', '.join(list(list_tags))
print(spisok1)
spisok2 = ', '.join(list(languages_tags))
print(spisok2)
spisok3 = ', '.join(list(platforms_tags))
print(spisok3)

def popular_tags(list_tags):
    spam_wc = WordCloud(width = 512,height = 512).generate(spisok1)
    plt.figure(figsize = (10, 8), facecolor = 'k')
    plt.imshow(spam_wc)
    plt.axis('off')
    plt.tight_layout(pad = 0)
    plt.show()

popular_tags(spisok1)

def show_langugaes_tags(languages_tags):
    ham_wc = WordCloud(width = 512,height = 512).generate(spisok2)
    plt.figure(figsize = (10, 8), facecolor = 'k')
    plt.imshow(ham_wc)
    plt.axis('off')
    plt.tight_layout(pad = 0)
    plt.show()

show_langugaes_tags(spisok2)

def show_platform_tags(languages_tags):
    ham_wc = WordCloud(width = 512,height = 512).generate(spisok3)
    plt.figure(figsize = (10, 8), facecolor = 'k')
    plt.imshow(ham_wc)
    plt.axis('off')
    plt.tight_layout(pad = 0)
    plt.show()

show_platform_tags(spisok3)
# каво
# np.random.seed(123)
# groups = [f"P{i}" for i in range(7)]
# counts = np.random.randint(3, 10, len(groups))
# plt.bar(groups, counts)