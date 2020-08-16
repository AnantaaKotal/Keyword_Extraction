import glob
import os
import re
from rake_nltk import Rake

path = "INSERT PATH HERE"


# RAKE MODULE; RETURNS KEYWORDS FOR EACH DOCUMENT
def rake():
    # exhaustive list of stop words
    stop_dir = "SmartStoplist.txt"

    # initializing rake module
    # min_length = minimum number of words in keyword phrases
    # max_length = maximum number of words in keyword phrases
    # adjust min_length and max_length to your preference
    r = Rake(stopwords=stop_dir, min_length=1, max_length=4)

    # reading from file
    for file in glob.glob(os.path.join(path, '*.txt')):
        f = open(file, 'r', encoding='latin-1')
        text = f.read()
        f.close()

        # formatting text for pretty print
        text = text.replace('.', ' ')
        text = re.sub(r'\s+', ' ', re.sub(r'[^\w \s]', '', text)).lower()

        # extracting keywords
        r.extract_keywords_from_text(text)

        # printing ranked phrases
        ranked_phrases = r.get_ranked_phrases()
        print(ranked_phrases)


# calling rake module
rake()