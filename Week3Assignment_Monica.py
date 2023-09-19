"""
Program to display bar graph for mountain flowers
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('mountain_flowers.csv')
df = pd.DataFrame(data)
#creating two seperate bar graphs for length and width of flower petals
X = list(df.iloc[:, 2])
Y = list(df.iloc[:,0])
Y1 = list(df.iloc[:,1])
plt.title("Bar graph Mountain Flowers vs Petal Length")
plt.xlabel("Flowers")
plt.bar(X, Y, color='g')
plt.ylabel("Petal Length")
plt.show()
