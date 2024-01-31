from nltk.corpus import stopwords
import operator
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
import argparse
import matplotlib.pyplot as plt
import math

wordsAndWeights = {}
ps = PorterStemmer()
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
parser = argparse.ArgumentParser(prog='nlphw0.py',description='A program that Normalizaes Text in a text file', epilog='By Joshua Pagonas')
parser.add_argument('filename', help='Text file to be read')
parser.add_argument('-l','--lower', help='Turns all words into lowercase present in the text file', action='store_true')
parser.add_argument('-s','--stem', help='Stems all words present in the text file', action='store_true')
parser.add_argument('-sw','--stopword', help='Removes all stopwords present in the text file', action='store_true')
parser.add_argument('-ran','--removenonalphnum', help='Removes all non-alphanumeric characters present in the text file', action='store_true')
args = parser.parse_args()

try:
    with open(args.filename, 'r', encoding="utf-8") as file:
        text = file.read()
        if args.lower:
            text = text.lower()
        if args.stem:
            text = ps.stem(text)
        if args.removenonalphnum:
            words = text.split()
        else:
            words = word_tokenize(text)

        for word in words:
            if args.stopword and word in stop_words:
                continue

            if args.removenonalphnum:
                if word=='-':
                    continue
                word = ''.join(s for s in word if s.isalnum() or s=='-')
                if not word:
                    continue

            if word not in wordsAndWeights:
                wordsAndWeights[word] = 1
            else:
                wordsAndWeights[word] += 1
            
    sortedWordsAndWeights = dict(sorted(wordsAndWeights.items(), key=operator.itemgetter(1), reverse=True))
    for word,weight in sortedWordsAndWeights.items():
        print(word,weight)

    x = list(range(len(sortedWordsAndWeights.keys())))
    y = list(sortedWordsAndWeights.values())
    y = [math.log10(i) for i in y]

    plt.plot(x, y, marker='o')

    plt.title("Sample Word and Weight Plot")
    plt.xlabel("Words")
    plt.ylabel("Weights")

    plt.grid(True)
    plt.show(block=True)
except KeyboardInterrupt:
    print('Program Closed By User')