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
plt.ylabel("Petal Length")
plt.bar(X, Y, color='g')
fig = plt.figure(figsize=(8,8))
st.pyplot(fig)
plt.title("Bar graph Mountain Flowers vs Petal Width")
plt.xlabel("Flowers")
plt.ylabel("Petal Width")
plt.bar(X,Y1, color='r')
fig = plt.figure(figsize=(8,8))
st.pyplot(fig)
