import streamlit as st

st.set_page_config(page_title='Modelling Choice, Models and Results')
st.markdown('# Modelling Choice, Models and Results')
st.sidebar.header("Modelling Choice, Models and Results")

st.markdown("""
## Model & Parameter Choice
For my first goal of classifying players into different categories, K-means clustering appeared to be the best model. The other model I considered for clustering was hierarchical agglomerative clustering, but hierarchical clustering was extremely computationally time-intensive, and my cleaned data contained more than 360k hands. K-means assumed distinct clusters, which I hypothesized could be true (with four distinct types of players), and aggression factors from the preliminary data analysis seemed to support my hypothesis that aggression followed normal distributions. However, now in retrospect, it would appear that I should’ve also checked for the distribution of tightness frequencies. To choose a target k, I would examine the “elbow plot” of inter-cluster variance to determine the ideal number of clusters.
	
For my second goal of identifying the strategy that would be the most profitable, I sought to use LASSO regression on players in the TAG cluster such that I could identify if their playstyle led to long term edge on others. I chose LASSO due to its ability to regularize many features into few select ones of importance, and reduce the impact of multicollinearity as many statistics (such as equities of hands) were not independently distributed and collinear.

""")

st.markdown("""
## Modelling & Results
In the modeling process, I first ensured that the features I chose were standardized using the StandardScaler method to ensure that k-means, which uses Euclidean distances, would process correctly for each of the features. I then encoded dummy variables to indicate the length in which players participated in the board to avoid punishing those who forced a fold earlier against opponents. I then fit different values of k for the features that I obtained to calculate the within-cluster variance of datapoints within each cluster, which my target statistic to optimize. Given the elbow plot of k-means, I saw that within cluster variance was most optimized at either k=2 or k=4 clusters, which demonstrated some validity to my hypothesis that players could be clustered into 4 groups. However, after plotting and labeling a random but equal subset of players, I realized that my clusters were not distinct enough to qualify for k-means analysis. I had overestimated the clustering effect of players into distinct groups, and did not think enough about how players often tended towards the mean in both tightness and aggressiveness. 

For the LASSO regression, I took the standardized features and performed k-fold cross validation on the dataset such that I could obtain the optimize lambda, or the threshold of my regularization. After investigating the k-fold CV, I identified the most important features when regressed against earnings, which were river equity and river aggression. LASSO had allowed me to reduce collinear variables to river equity such as preflop and flop equity such that I could isolate river equity as a defining factor. However, as river equity is a binary variable that is often controlled through random chance, its significance failed to grant me insights into how players’ actions could influence earnings. 

""")

st.image('figures/kmeans_elbow.png')




