import streamlit as st

st.set_page_config(page_title="Literature Review")
st.markdown('# Literature Review')
st.sidebar.header("Literature Review")

st.markdown("""

Academic research in poker has primarily split up into two schools of thought: 1. 
Modeling player behavior through bayesian models with rulesets, and 2. Building 
machine learning models with large quantities of data to predict player behavior. Player 
classification largely fell into the latter category. While classifying players into distinct 
categories had been done before (Teofilo and Reis 2013), and opponent modeling was 
widely researched (Billings et al. 1998), the anecdotal axes of “tightness” and 
“aggressiveness” had yet to be extensively delved into. In Teofilo and Reis’ paper, 7 
clusters were identified, but these clusters were unintuitive from a players’ perspective. 
One cluster of individuals appeared to be relatively passive on preflop and flop rounds, 
but were highly aggressive on the last card. One has to wonder if the paper truly found a 
group who systematically played aggressively on the last card, or merely found a group 
of players that had the last card complete a good hand. In essence, the separation of 
player agency and luck is a perennial problem in poker analysis, and while large 
samples can reduce this risk, there would always exist the problem of mislabeling 
players who hit certain cards on certain rounds as a function of their purposeful choice. 
      
""")