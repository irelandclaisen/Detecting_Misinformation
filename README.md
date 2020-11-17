# Detecting_Misinformation

## Description
In this project, I scrape data from news sites to develop a logistic regression model that can classify news as misinformation or reliable.  I also found the topics that news clusters.

## Context

Misinformation is a major problem.  Before the 2016 election, fake articles were getting more interactions on Facebook than real articles [(Buzzfeed)](https://www.buzzfeednews.com/article/craigsilverman/viral-fake-election-news-outperformed-real-news-on-facebook#.dfDpPnYRD). By developing this model, I can classify news articles that are likely misinformation and find topics that misinformation clusters on so people can be more informed when consuming news and hopefully be less likely to be misled.


## Featured Techniques
 * Feature Engineering
 * Data Visualization
 * Balancing Classes
 * Logistic Regression
 * Unsupervised Learning
 * LDA
 

## Data
Data was taken from [kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset), [adfontesmedia.com](https://www.adfontesmedia.com) and this [dataset](https://github.com/KaiDMML/FakeNewsNet).  I also used the News API to get more recent news articles.


## Workflow
* Scrape data and ratings from adfontesmedia.com.  Also got data from kaggle and FakeNewsNet
* Cleaned text using regular expressions
* Vectorized text using CV and TFIDF
* Developed Logistic Regression model to predict whether articles are misinformation or reliable
* Collected more recent articles and classified the articles as misinformation or not
* Take the most recent fake news and older fake news and performed topic modeling using LDA
* Develop an app that can take a URL and identify articles as misinformation or reliable using my logisitic regression model.  The app also lists the topics that misinformation clusters on
