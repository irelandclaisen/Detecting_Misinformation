import streamlit as st
import pickle
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd



def app():
    st.title('Misinformation Clusters')
    st.write('Current Clusters')
    fake_news = pickle.load(open('fake_new', 'rb'))
    tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                stop_words = 'english')
    dtm_tf = tf_vectorizer.fit_transform(fake_news)
    lda_tf = LatentDirichletAllocation(n_components=8, random_state=0)
    lda_tf.fit(dtm_tf)
    df_topics = pd.DataFrame(get_topics(lda_tf, tf_vectorizer, 10))
    topic= st.selectbox("Select Topic", df_topics.columns)
    for item in df_topics[topic]:
        st.write(item)
    
def get_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    dict_words = dict()
    for topic_idx, topic in enumerate(model.components_):
        topic_name = ("Topic #%d" % (topic_idx+1))
        dict_words[topic_name] = []
        for i in topic.argsort()[:-n_top_words - 1:-1]:
            dict_words[topic_name].append(words[i])
    return dict_words