import streamlit as st

st.set_page_config(page_title='Background & Summary of Findings')
st.markdown('# Background')
st.sidebar.header("Background & Summary of Findings")
st.markdown("""

Texas Hold’em poker emerged as a relatively new game when it was introduced 
to Las Vegas in 1963. The game is played with 2 private cards and 5 community 
cards, where each player would form the best five-card hand from the 7 cards 
that are available. What made poker exceedingly interesting, however, is its 
involvement of four rounds of betting between 0,3,4, and 5 cards on the board. 
At each juncture of play, the players could either check (to pass the action onto 
the next player), fold (discard the hand), bet (to put more money into the pot when 
no one had done before), raise (to put more money into the pot when someone had already bet), 
or call (to put the minimum amount of money into the pot to see the next community card). 
These actions, in turn, were a way for others to glean the information of their opponents’ hand. 
If the opponent had a good hand, they would be more inclined to put more money into the pot such 
that they would win more. 

However, players’ bets conveyed incomplete information; a small bet could either signal that the 
opponent had a weak hand, or that the opponent had a very strong hand but wanted to extract more value
and didn’t want to scare away existing players. A large bet, in contrast, could either indicate the 
opponent’s strength or be a complete bluff to force a fold. 

In poker, even before the advent of computer simulations, the idea of two axes to
classify players into four categories has become apocryphal. On one axis,
“tightness” described a player’s willingness to put money in preflop by ascribing  
a set of hands that a player would be willing to play. The more a player would be 
willing to enter with a subpar hand, the more the player would be described as 
“loose.” On the other axis, players would measure how “aggressive” they are, 
which is commonly seen through the amount of bets and raises compared to 
passive actions such as checking and calling. These two axes form the majority 
of the advice given to new players: that new players should play “tight and 
aggressive (TAG),” or in other words, only play a small number of hands, but play 
the hands aggressively, which is to raise and bet much more than they check and 
call. 
                  
""")
st.markdown('# Hypothesis')
st.markdown("""
Given that there is often anecdotal evidence on tight and aggressive play, I 
sought to answer two questions: 1. Whether the players could be classified into 
four categories along the tightness and aggressiveness axes, and 2. Whether 
TAG players were truly more profitable in the long run after thousands of hands.   
""")

st.markdown('# Summary of Findings')
st.markdown('## Summary of Findings for Goal 1')

st.markdown("""
For Goal 1, although trying both rudimentary aggression and later robust variables
failed to generate extremely meaningful results on clustering analysis, I found several conclusions from
the clustering experiment:
* Within cluster variance was reduced by 14% using more robust aggression variables that are commonly used in poker analysis
* Reducing the universe of players sampled only marginally decreased within cluster variance, because although luck would become normalized over large number of hands, this sampling would generally exclude more novice players in favor of professional players who were constantly on the site.
* Player habits can better be modeled with Gaussian Mixture Models instead of distinct clusters, as both aggression and tightness often followed Gaussian Distributions.
                   
""")
st.image('figures/robust_clustering.png')
st.caption('Figure 1. Cluster modelling on x-axis of mean Aggression Factor and y-axis of mean hand_rank')



st.markdown('## Summary of Findings for Goal 2')
st.markdown("""
For Goal 2, the results of clustering was confirmed by how a regression of TAG players against earnings yielded minimal results (with an r-squared of 0.04). When applying LASSO to other features, however, I concluded some interesting results below:
* TAG Players as identified by clustering analysis not only did not earn more than the average player, but also had mean aggression and tightness features that did not significantly deviate from the average, as hypothesis tests returned p-values of 0.44 under the null hypothesis that TAG players and regular players had equal aggression.
* Aggression across different streets were tied more to the player and not the hand, as we saw strong correlation (R-squared of 0.56) between preflop and flop aggression even when the board was not in the player's favor.
                   
""")
st.image('figures/preflop_vs_flop_agg.png')
st.caption('Figure 2. Player mean preflop vs postflop aggression scores for players that have played more than 1000 hands')

