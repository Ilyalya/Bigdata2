from pyspark.sql import SparkSession
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

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Learning_Spark") \
    .getOrCreate()

data = spark.read.csv('questions1.csv', sep='\t', inferSchema=True, header=True)

languages = ["javascript", "python", "java", "php", "c#", "c++", "ruby", "css", "typescript", "c", "swift", "objective-c", "scala", "r",
             "go", "shell", "powershell", "perl", "kotlin", "haskell", "matlab", "sql", "rust", "typescript", "node.js", "pascal", "groovy", "d", "assembler", "pl/sql", "vue.js"]
platforms = ["windows", "macos", "linux", "ios", "chromeos", "ipados", "debian", "centos", "tizen", "freebsd", "bsd", "ubuntu", "windows server"]

print(data['tags'])

# data['tags'] = data['tags'].map(lambda x: x.replace("'", ''))
# data['tags'] = data['tags'].map(lambda x: x.replace("[", ''))
# data['tags'] = data['tags'].map(lambda x: x.replace(",", ''))
# data['tags'] = data['tags'].map(lambda x: x.replace("]", ''))
#
# list_tags = []
#
# for i in range(len(data['tags'])):
#     words = word_tokenize(data['tags'][i])
#     for j in range(len(words)):
#         list_tags.append(words[j])
#
# languages_tags = []
# for i in range(len(list_tags)):
#     for j in range(len(languages)):
#         if languages[j] == list_tags[i]:
#             languages_tags.append(list_tags[i])
#
# platforms_tags = []
# for i in range(len(list_tags)):
#     for j in range(len(platforms)):
#         if platforms[j] == list_tags[i]:
#             platforms_tags.append(list_tags[i])
#
# c = Counter(list_tags)
# print(c)
#
# spisok1 = ', '.join(list(list_tags))
# spisok2 = ', '.join(list(languages_tags))
# spisok3 = ', '.join(list(platforms_tags))
#
# def popular_tags(list_tags):
#     spam_wc = WordCloud(width = 512,height = 512).generate(spisok1)
#     plt.figure(figsize = (10, 8), facecolor = 'k')
#     plt.imshow(spam_wc)
#     plt.axis('off')
#     plt.tight_layout(pad = 0)
#     plt.show()
#
# popular_tags(spisok1)
#
# def show_langugaes_tags(languages_tags):
#     ham_wc = WordCloud(width = 512,height = 512).generate(spisok2)
#     plt.figure(figsize = (10, 8), facecolor = 'k')
#     plt.imshow(ham_wc)
#     plt.axis('off')
#     plt.tight_layout(pad = 0)
#     plt.show()
#
# show_langugaes_tags(spisok2)
#
# def show_platform_tags(languages_tags):
#     ham_wc = WordCloud(width = 512,height = 512).generate(spisok3)
#     plt.figure(figsize = (10, 8), facecolor = 'k')
#     plt.imshow(ham_wc)
#     plt.axis('off')
#     plt.tight_layout(pad = 0)
#     plt.show()
#
# show_platform_tags(spisok3)