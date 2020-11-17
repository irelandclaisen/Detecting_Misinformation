import streamlit as st
import pickle
from bs4 import BeautifulSoup
import requests
import re
import string

def app():
    st.title('Misinformation Classification')

    t = st.text_input("Please enter the URL of the article you are interest in")

    start = st.button("Start")

    if start:
        classify_news(t)

def classify_news(url):
    try:
        source_code = requests.get(url)
        soup = BeautifulSoup(source_code.text, 'html5lib')
        visible = soup.find_all(text=True)
        text = ''
        for tag in visible:
            if tag.parent.name in ['p', 'a']:
                text += ' ' + tag
        text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text.lower())
        lr = pickle.load(open('log_reg', 'rb'))
        tfidf1 = pickle.load(open('tfidf1.pickle', 'rb'))
        y = tfidf1.transform([text])
        prob_fake = lr.predict_proba(y)[0,0]*100
        if prob_fake < 50:
            st.write('Likely Reliable')
            st.write(int(prob_fake), '% chance that it is misinformation')
        if prob_fake > 50:
            st.write('Likely Misinformation')
            st.write(int(prob_fake), '% chance that it is misinformation')
    
    except:
        st.write('Not a valid URL')
