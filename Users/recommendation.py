from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
# import pandas as pd


def get_rec(ip_rec, df, indices):
    cl_rec = df['CleanedIngredients']

    # Appending the input recipe to the copy of the recipes
    cl_rec.loc[len(cl_rec)] = ip_rec
    vectorizer_op = CountVectorizer().fit_transform(cl_rec)
    vectors_op = vectorizer_op.toarray()

    # Calculating cosine similarity
    cosine_sim = cosine_similarity(vectors_op)

    # Index of our input recipe is always last index
    idx = len(indices)

    # Extracting sim_scores for idx index movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sorted using lambda function where sim_scores is the x for lambda function
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Extracting the top 5 scored movies as our 5 recommendations
    sim_scores = sim_scores[1:21]

    # print(sim_scores)

    # Getting a list giving the index of our 5 movies
    recipe_idx = [i[0] for i in sim_scores]

    # Removing the recipe from the dataset
    cl_rec = cl_rec.drop(cl_rec.tail(1).index, inplace=True)

    # Returning the 5 titles of movies from our dataframe
    # return df['RecipeName'].iloc[recipe_idx]
    return recipe_idx