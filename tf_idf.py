import glob
import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

path = "/Users/anantaa/Desktop/python/keyword_search/stories"

# number of keywords to be extracted; initialised to 10
number_of_keywords = 10

# USE THIS TO CREATE YOUR CORPUS FROM .TXT FILES
def extract_corpus():
    corpus = []

    for file in glob.glob(os.path.join(path, '*.txt')):
        f = open(file, 'r', encoding='latin-1')
        text = f.read()
        f.close()

        # FORMATTING THE TEXT FOR PRETTY PRINT
        text = text.replace('.', ' ')
        text = re.sub(r'\s+', ' ', re.sub(r'[^\w \s]', '', text)).lower()
        corpus.append(text)

    return corpus


# TF_IDF MODULE; RETURNS KEYWORDS FOR EACH DOCUMENT
def tf_idf(corpus):
    # initializing vectorizer
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    names = vectorizer.get_feature_names()
    data = vectors.todense().tolist()

    # Create a dataframe with the results
    df = pd.DataFrame(data, columns=names)

    # filtering stopwords
    st = set(stopwords.words('english'))
    df = df[filter(lambda x: x not in list(st), df.columns)]

    # printing top 10 keywords
    N = number_of_keywords
    for i in df.iterrows():
        print(i[1].sort_values(ascending=False)[:N])

    return df

def test():
    corpus = extract_corpus()
    tf_idf(corpus)

test()