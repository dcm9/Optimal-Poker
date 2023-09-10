import streamlit as st

st.set_page_config(page_title='Data Description & Preliminary Data Analysis')
st.markdown('# Data Description & Preliminary Data Analysis')
st.sidebar.header("Data Description & Preliminary Data Analysis")

st.markdown("## Data Description")

st.markdown("""

The dataset I used was IRC Poker Dataset, a datamined set of observations that logged every poker hand played on the usenet poker enthusiast site. From 1995-2001, the program logged more than 10 million hands of poker. However, these 10 million hands were not all Texas Hold’em, and a lot of them were missing critical information, such as betting quantities, players’ cards, and the board. I’ve detailed most of the data cleaning process in Poker Hand Cleaning.ipynb in the Optimal-Poker repo, where I detail in depth my methodology in preserving data structure and cleanliness. I then engineered a set of features I wished to analyze, including position, bankroll, blinds, and pocket cards for each hand, and put them into a dataframe for preliminary data analysis and aggregation. 

             
""")

st.markdown("""
            
## Preliminary Data Analysis
I found four points that would pertain the most to my hypothesis and investigation through preliminary analysis:
* Players often overplay Ax hands (where one card is an ace), where aggression would not fit the strength of their hand relative to other cards on the board.
* Aggression is relatively player dependent rather than hand dependent, which can be seen by how many players often continue aggressing on subsequent streets after their initial aggressive plays although the next card completes an opponent’s draws or is generally unfavorable for their card combination. 
* Bankroll seems to have no bearing on the particular decisions of players on a whole in individual hands 
* Aggression on all streets appear to follow a relatively normal distribution

                  
""")

st.image('figures/feature_corr_matrix')