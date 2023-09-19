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
#2 subplots
f, (ax1,ax2) = plt.subplots(1,2)
ax1.bar(X, Y, color='g')
ax1.set_title("Bar graph Mountain Flowers vs Petal Length")
ax1.set_xlabel("Flowers",fontsize=8)
ax1.set_ylabel("Petal Length",fontsize=8)
ax2.set_ylabel("Petal Width",fontsize=8)
ax2.bar(X, Y1)
plt.tight_layout(pad=0.4)
st.pyplot(plt)
