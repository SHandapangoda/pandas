import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split, KFold
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# import seaborn as sns


def showSales():

    data1 = pd.read_csv('Sales_January_2019.csv')
    data2 = pd.read_csv('Sales_February_2019.csv')
    data3 = pd.read_csv('Sales_March_2019.csv')

    saleCount1 = data1.count()
    saleCount2 = data2.count()
    saleCount3 = data3.count()

    plt.bar(10,saleCount1,3, label="Jan")
    plt.bar(20,saleCount2,3, label="Feb")
    plt.bar(30,saleCount3,3, label="Mar")
    plt.legend()
    plt.ylabel("Sales")
    plt.title("Monthly sales")
    plt.show()


showSales()




