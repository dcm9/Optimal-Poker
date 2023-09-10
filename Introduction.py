import streamlit as st

st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
)

st.write('# Exploiting Asymmetric Habits in No-Limit Poker')

st.sidebar.success('Navigate to the desired section')
st.write("")

st.markdown("""
## Personal Introduction 
Hello! My name is Aaron Zhang, and I’m currently a rising junior at the University of Chicago studying Economics and Data Science. This app is a culmination of a passion project regarding habits in Texas Hold’em poker.

## Sections 
* Background & Summary of Findings
* Literature Review
* Data Description & Preliminary Data Analysis
* Modelling Choice, Models and Results

""")

st.markdown("""
## Disclaimer
This project is purely for my personal enjoyment, but I do especially have to thank Allen Wang 
for his immense help in unwrapping the datamined files. I would also like to thank Jax Ma for his 
personal and computational support. Last of all, I would like to thank the University of Chicago, 
who provided me with the knowledge and computational resources that I could not have done without.

""")