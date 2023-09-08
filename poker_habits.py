import pandas as pd
import numpy as np
import streamlit as st #can incorporate streamlit last, first use matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.cluster import KMeans, AgglomerativeClustering

hand_rankings = {
    'AAo':1,
    'KKo':2,
    'QQo':3,
    'AKs':4,
    'JJo':5,
    'AQs':6,
    'KQs':7,
    'AJs':8,
    'KJs':9,
    'TTo':10,
    'AKo':11,
    'ATs':12,
    'QJs':13,
    'KTs':14,
    'QTs':15,
    'JTs':16,
    '99o':17,
    'AQo':18,
    'A9s':19,
    'KQo':20,
    '88o':21,
    'K9s':22,
    'T9s':23,
    'A8s':24,
    'Q9s':25,
    'J9s':26,
    'AJo':27,
    'A5s':28,
    '77o':29,
    'A7s':30,
    'KJo':31,
    'A4s':32,
    'A3s':33,
    'A6s':34,
    'QJo':35,
    '66o':36,
    'K8s':37,
    'T8s':38,
    'A2s':39,
    '98s':40,
    'J8s':41,
    'ATo':42,
    'Q8s':43,
    'K7s':44,
    'KTo':45,
    '55o':46,
    'JTo':47,
    '87s':48,
    'QTo':49,
    '44o':50,
    '33o':51,
    '22o':52,
    'K6s':53,
    '97s':54,
    'K5s':55,
    '76s':56,
    'T7s':57,
    'K4s':58,
    'K3s':59,
    'K2s':60,
    'Q7s':61,
    '86s':62,
    '65s':63,
    'J7s':64,
    '54s':65,
    'Q6s':66,
    '75s':67,
    '96s':68,
    'Q5s':69,
    '64s':70,
    'Q4s':71,
    'Q3s':72,
    'T9o':73,
    'T6s':74,
    'Q2s':75,
    'A9o':76,
    '53s':77,
    '85s':78,
    'J6s':79,
    'J9o':80,
    'K9o':81,
    'J5s':82,
    'Q9o':83,
    '43s':84,
    '74s':85,
    'J4s':86,
    'J3s':87,
    '95s':88,
    'J2s':89,
    '63s':90,
    'A8o':91,
    '52s':92,
    'T5s':93,
    '84s':94,
    'T4s':95,
    'T3s':96,
    '42s':97,
    'T2s':98,
    '98o':99,
    'T8o':100,
    'A5o':101,
    'A7o':102,
    '73s':103,
    'A4o':104,
    '32s':105,
    '94s':106,
    '93s':107,
    'J8o':108,
    'A3o':109,
    '62s':110,
    '92s':111,
    'K8o':112,
    'A6o':113,
    '87o':114,
    'Q8o':115,
    '83s':116,
    'A2o':117,
    '82s':118,
    '97o':119,
    '72s':120,
    '76o':121,
    'K7o':122,
    '65o':123,
    'T7o':124,
    'K6o':125,
    '86o':126,
    '54o':127,
    'K5o':128,
    'J7o':129,
    '75o':130,
    'Q7o':131,
    'K4o':132,
    'K3o':133,
    '96o':134,
    'K2o':135,
    '64o':136,
    'Q6o':137,
    '53o':138,
    '85o':139,
    'T6o':140,
    'Q5o':141,
    '43o':142,
    'Q4o':143,
    'Q3o':144,
    '74o':145,
    'Q2o':146,
    'J6o':147,
    '63o':148,
    'J5o':149,
    '95o':150,
    '52o':151,
    'J4o':152,
    'J3o':153,
    '42o':154,
    'J2o':155,
    '84o':156,
    'T5o':157,
    'T4o':158,
    '32o':159,
    'T3o':160,
    '73o':161,
    'T2o':162,
    '62o':163,
    '94o':164,
    '93o':165,
    '92o':166,
    '83o':167,
    '82o':168,
    '72o':169  
}
#no hand is -1

df = pd.read_csv('new_cleaned_dataset.csv')
st.write(df)

# In[5]:


#hand_rankings
plt.figure(figsize = (35,10))
plt.tight_layout()

plt.bar(np.sort(df['preflop_rank'].dropna().unique()),df.groupby('preflop_rank').count()['index'])
plt.xticks(range(1,len(hand_rankings.keys())+1),hand_rankings.keys(), rotation = 'vertical')

plt.xlabel('Poker Hand')
plt.ylabel('Frequency of Play')
plt.title('Frequency of Poker Hand Occurence Post-flop')
st.pyplot(plt)


# In[81]:


#boxplot
plt.figure(figsize = (35,10))
plt.tight_layout()

plt.boxplot(df.groupby('preflop_rank')['preflop_equity'].apply(list),showfliers=True,showmeans=True)
plt.xticks(range(1,len(hand_rankings.keys())+1),hand_rankings.keys(), rotation = 'vertical')

plt.xlabel('Poker Hand')
plt.ylabel('Pre-flop Winning Probability')
plt.title('Preflop Winning Probability of Hand (1000 Monte Carlo Simulations against all other cards in play)')
st.pyplot(plt)


# In[ ]:


#can additionally show how different people bet on the same type of hands


# In[97]:


#histogram of Aces' probability
plt.hist(df.groupby('preflop_rank')['preflop_equity'].apply(list)[78.0],bins=30)
st.pyplot(plt)


# In[129]:


#barplot of mean preflop aggression across players
plt.hist(df.groupby('player')['preflop_cat_action'].mean(),bins=30)
st.pyplot(plt)


# In[120]:


#barplot of mean flop aggression across players
#very interesting, all other stats quite spiked in the middle, but much more variance on mean flop aggression?
plt.hist(df.groupby('player')['flop_cat_action'].mean(),bins=30)
st.pyplot(plt)


# In[119]:


#barplot of turn flop aggression across players
plt.hist(df.groupby('player')['turn_cat_action'].mean(),bins=30)
st.pyplot(plt)


# In[118]:


#barplot of river flop aggression across players
plt.hist(df.groupby('player')['river_cat_action'].mean(),bins=30)
st.pyplot(plt)


# In[157]:


#how percentage to win the pot is directly correlated with final earnings
data = df[['preflop_equity','flop_equity','turn_equity','river_equity','earnings']].corr()
htmp = sns.heatmap(data)
st.pyplot(htmp)


# In[160]:


sns.heatmap(df[['pos','bankroll','preflop_equity','preflop_rank','preflop_pot','flop_equity','flop_pot','turn_equity',
               'turn_pot','river_equity','river_pot','earnings','preflop_cat_action','flop_cat_action','turn_cat_action',
               'river_cat_action']].corr())


# Interesting things to note:
# 1. Position is relatively uncorrelated in general play to either aggression on all four streets and negatively correlated to the preflop rank of a particular hand
# 2. Bankroll seems to have no bearing on the particular decisions of players on a whole in individual hands (makes sense, as the game is a cash game, in tournament, this might drastically change where players apply ICM pressure)
# 3. Preflop equity seems to be relatively uncorrelated with preflop aggression, and this trend follows through the streets
# 4. Preflop hand rank seem to be negatively correlated (as expected) with action, as better hands would be acted upon through more aggressive betting

# # Part 5. Modelling Part 1. Clustering

# In[55]:



# In[193]:


filtered_df = df.groupby('player').filter(lambda x:x['player'].count()>30)
filtered_df = filtered_df.groupby('player').mean()


# In[200]:


#need to ensure that those who win the flop and make others fold are not punished
feature_df = filtered_df[['preflop_cat_action','preflop_rank']].fillna(0)
feature_df


# In[201]:


X_1 = preprocessing.StandardScaler().fit(feature_df).transform(feature_df)
print(X_1)


# In[202]:


kmeans1 = KMeans(n_clusters=4,n_init=20)
clust_1 = kmeans1.fit(X_1)
feature_df['clusters'] = clust_1.labels_
feature_df


# In[197]:


plt.scatter(filtered_df['preflop_cat_action'],filtered_df['flop_cat_action'])


# In[204]:


import matplotlib.pyplot as plt

for i in range(0,4):
    plt.scatter(feature_df.loc[feature_df['clusters'] == i, 'preflop_cat_action'],feature_df.loc[feature_df['clusters'] == i, 'preflop_rank'])


# In[13]:


filtered_df


# In[54]:


plt.scatter(df['earnings'],df['river_cat_action'])


# In[47]:


from sklearn.linear_model import LinearRegression
    
#encode dummies

x = pd.get_dummies(feature_df['clusters']).iloc[:,1].array.reshape(-1,1)
y = filtered_df['earnings']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

linreg = LinearRegression()
linreg.fit(x_train,y_train).score(x_test,y_test)


# In[302]:


num_clusters = []
cluster_var = []

for i in range(1,20):
    kmeans = KMeans(n_clusters=i,n_init=10)
    cluster = kmeans.fit(X_1)
    cluster_var.append(cluster.inertia_)
    num_clusters.append(i)


# In[303]:


plt.plot(num_clusters,cluster_var)
plt.xticks(np.arange(1,20))
plt.show()


# This seems to indicate that within-cluster variance is minimized at either k=2 or k=4, with k=4 being the more likely option. This agrees with the idea that 

# In[233]:


print(cluster_var)


# In[132]:


def tolist(one,two,three,four):

    actionlist = [one,two,three,four]
    actionlist = [i for i in actionlist if isinstance(i,str)]
    big_list = [[i[1:-1]] for i in actionlist]
    flattened_list = [i[1:-1] for i in actionlist]
        
    return big_list,flattened_list

df.apply(lambda x: tolist(x['preflop_action'], x['flop_action'],x['turn_action'],x['river_action'])[0], axis=1) 


# In[136]:


df


# In[151]:


new_frame = df.groupby('index').count()['hand_num'].to_frame().copy()
new_frame.rename(columns={'hand_num':'num_players'},inplace=True)

result = pd.merge(df,new_frame, how='left',on=['index'])


# In[152]:


result


# In[186]:


def tolist(one,two,three,four):

    actionlist = [one,two,three,four]
    actionlist = [i for i in actionlist if isinstance(i,str)]
    flattened_list = [i[1:-2].replace("'","") for i in actionlist]
    clean_list = [i.split(', ') for i in flattened_list]
    
    big_list = clean_list
    flat_list = [item for sublist in clean_list for item in sublist]
        
    return big_list, flat_list

df.apply(lambda x: tolist(x['preflop_action'], x['flop_action'],x['turn_action'],x['river_action']), axis=1)


# In[169]:


def aggression_factor(one,two,three,four):
    '''not true af, true af is bet+raise/calls'''
    actionlist = tolist(one,two,three,four)[1]
    total_len = len(actionlist)

    if actionlist[0] == 'B':
        total_len -= 1
        if total_len == 0:
            #no play, so no meaningful data; in the filtering process for modelling we will remove negative aggression
            return -1
    
    aggression_counter = 0
    aggression = ['b','r','A']
    
    for i in actionlist:
        if i in aggression:
            aggression_counter += 1

    return aggression_counter/total_len

df.apply(lambda x: aggression_factor(x['preflop_action'], x['flop_action'],x['turn_action'],x['river_action']), axis=1)


# In[172]:


def vpip(big_blind,earnings,preflop_pot,num_players,one,two,three,four):
    vpip = 0
    action_list = tolist(one,two,three,four)[0]
    if np.abs(earnings) < big_blind:
        vpip = 0
    elif np.abs(earnings) == big_blind:
        if action_list[0][-1] in exit_hand:
            vpip = 0
        else:
            vpip = ((preflop_pot-big_blind)*num_players)
    else:
        vpip = np.abs(earnings) - big_blind
        
    return vpip


# In[ ]:




