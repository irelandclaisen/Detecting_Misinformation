import os
import streamlit as st
import json
import yaml
import operator


import app1
import app2

PAGES = {
    "Misinformation Classification": app1,
    "Misinformation Clusters": app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
