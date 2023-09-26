"""
Program to display bar graph for mountain flowers
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('mountain_flowers.csv')
st.title("Hello! Here's the mountain flower table details")
st.write(data)
#creating two separate bar graphs for length and width of flower petals
X = list(data.iloc[:, 2])
Y = list(data.iloc[:,0])
Y1 = list(data.iloc[:,1])
#2 subplots
f, (ax1,ax2) = plt.subplots(1,2)
ax1.bar(X, Y, color='g')
ax1.set_title("Bar graph Flowers vs Petal Length")
ax1.set_ylabel("Petal Length",fontsize=8)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax2.boxplot(Y)
ax2.set_title("Box Plot Flowers vs Petal Length")
ax2.set_ylabel("Petal Length")
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.tight_layout(pad=0.4)
st.pyplot(plt)
