import glob
import os
import re
from rake_nltk import Rake
from nltk.corpus import stopwords

path = "/Users/anantaa/Desktop/python/keyword_search/stories"

# number of keywords to be extracted; initialised to 10
number_of_keywords = 10

# USE THIS TO CREATE YOUR CORPUS FROM .TXT FILES
def extract_corpus():
    stop_dir = "SmartStoplist.txt"
    r = Rake(stopwords=stop_dir, min_length=1, max_length=4)

    for file in glob.glob(os.path.join(path, '*.txt')):
        f = open(file, 'r', encoding='latin-1')
        text = f.read()
        f.close()

        # FORMATTING THE TEXT FOR PRETTY PRINT
        text = text.replace('.', ' ')
        text = re.sub(r'\s+', ' ', re.sub(r'[^\w \s]', '', text)).lower()

        r.extract_keywords_from_text(text)

        a = r.get_ranked_phrases()
        print(a)


extract_corpus()