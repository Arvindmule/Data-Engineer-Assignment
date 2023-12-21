#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing pandas and sql lite lib
import pandas as pd
import sqlite3


# In[ ]:





# In[2]:


'''1. Data Import:
- Set up a PostgreSQL database. (You can setup a free PostgreSQL instance from Render)
- Create tables to store movie and rating data from the CSV files
(You can download the CSV files from here)
- Import the CSV data into the respective tables in the PostgreSQL database
'''


# In[2]:


#Reading movies csv file
df = pd.read_csv(r"C:\Users\SHREE\Desktop\movies_csv\movies.csv")
df


# In[3]:


#Reading ratings csv file
df1 = pd.read_csv(r"C:\Users\SHREE\Desktop\movies_csv\ratings.csv")
df1


# In[4]:


conn=sqlite3.connect("sqldb.db")


# In[5]:


df.to_sql('movies', conn)


# In[22]:


sql_string = 'SELECT * FROM movies'
dfsql = pd.read_sql(sql_string, conn)
dfsql


# In[17]:


df1.to_sql('ratings', conn)


# In[31]:


sql_string1 = 'SELECT * FROM ratings'
dfsql1 = pd.read_sql(sql_string1, conn)
dfsql1


# In[ ]:





# In[ ]:


#Merging both movies and ratings csv file to perform oprations


# In[28]:


df3=pd.merge(df, df1, left_index=True, right_index=True)
df3


# In[ ]:





# In[ ]:


'''
a. Top 5 Movie Titles: Sort and print the top 5 movie titles based on the following criteria:
● Duration
'''


# In[83]:


dur=df3.sort_values(by=['minutes'],ascending=False)
dur[['title']].head(5)


# In[ ]:


'''
a. Top 5 Movie Titles: Sort and print the top 5 movie titles based on the following criteria:
● Year of Release
'''


# In[82]:


release_date=df3.sort_values(by=['year'],ascending=False)
release_date[['title']].head(5)


# In[ ]:





# In[ ]:


'''
a. Top 5 Movie Titles: Sort and print the top 5 movie titles based on the following criteria:
● Average rating (consider movies with minimum 5 ratings)
'''


# In[81]:


avg_rating=df3.sort_values(by=['rating'],ascending=False)
avg_rating=avg_rating[avg_rating.rating >= 5]
avg_rating[['title']].head(5)


# In[ ]:





# In[ ]:


'''b. Number of Unique Raters: Determine and
print the count of unique rater IDs
'''


# In[109]:


uni_rater=df3['rater_id'].drop_duplicates()
uni_rater


# In[104]:


print("Number of unique records",uni_rater.shape[0])


# In[ ]:





# In[ ]:


'''
c. Top 5 Rater IDs: Sort and print the top 5 rater IDs based on:
● Most movies rated
'''


# In[114]:


ratings_count = df3['rater_id'].value_counts()
ratings_count.head(5)


# In[ ]:





# In[ ]:


'''
c. Top 5 Rater IDs: Sort and print the top 5 rater IDs based on:
● Highest Average rating given (consider raters with min 5 ratings)
'''


# In[121]:


qualified_raters = ratings_count[ratings_count >= 5].index.tolist()
avg_ratings = df3.groupby('rater_id')['rating'].mean()
top_raters_highest_avg = avg_ratings.loc[qualified_raters].nlargest(5)
top_raters_highest_avg


# In[ ]:





# In[ ]:


'''
d. Top Rated Movie:
- Find and print the top-rated movies by:
● Director 'Michael Bay'
'''


# In[143]:


filtered_movies = df3[(df3['director'] == 'Michael Bay')]
filtered_movies.sort_values(by=['rating'],ascending=False)
filtered_movies=filtered_movies[filtered_movies.rating >=7]
filtered_movies[['title']].head(5)


# In[ ]:





# In[ ]:


'''
d. Top Rated Movie:
- Find and print the top-rated movies by:
● 'Comedy'
'''


# In[139]:


filtered_movies1 = df3[(df['genre'] == 'Comedy')]
filtered_movies1.sort_values(by=['rating'],ascending=False)
filtered_movies1=filtered_movies1[filtered_movies1.rating == 10]
filtered_movies1[['title']].head(5)


# In[ ]:





# In[ ]:


'''
d. Top Rated Movie:
- Find and print the top-rated movies by:
● In the year 2013
'''


# In[138]:


filtered_movies2 = df3[(df['year'] == 2013)]
filtered_movies2.sort_values(by=['rating'],ascending=False)
filtered_movies2=filtered_movies2[filtered_movies2.rating == 10]
filtered_movies2[['title']].head(5)


# In[ ]:





# In[ ]:


'''
d. Top Rated Movie:
- Find and print the top-rated movies by:
● In India (consider movies with a minimum of 5 ratings).
'''


# In[137]:


filtered_movies3 = df3[(df['country'] == 'India')]
filtered_movies3.sort_values(by=['rating'],ascending=False)
filtered_movies3=filtered_movies3[filtered_movies3.rating == 10]
filtered_movies3[['title']].head(5)


# In[ ]:





# In[ ]:


'''e. Favorite Movie Genre of Rater ID 1040: Determine and print the favorite movie genre
for the rater with ID 1040 (defined as the genre of the movie the rater has rated most often).
'''


# In[159]:


ratings_1040 = df3[df3['rater_id'] == 104]
genre_counts = ratings_1040['genre'].value_counts()
favorite_genre = genre_counts.idxmax()
favorite_genre


# In[ ]:





# In[ ]:


'''f. Highest Average Rating for a Movie Genre by Rater ID 1040: Find and print the
highest average rating for a movie genre given by the rater with ID 1040 (consider genres with a
minimum of 5 ratings).
'''


# In[161]:


ratings_1040 = df3[df3['rater_id'] == 104]
genre_ratings_count = ratings_1040['genre'].value_counts()
qualified_genres = genre_ratings_count[genre_ratings_count >= 5].index.tolist()
qualified_ratings = ratings_1040[ratings_1040['genre'].isin(qualified_genres)]
avg_ratings_per_genre = qualified_ratings.groupby('genre')['rating'].mean()
highest_avg_rating = avg_ratings_per_genre.max()
highest_avg_rating


# In[ ]:





# In[ ]:


'''g. Year with Second-Highest Number of Action Movies: Identify and print the year with
the second-highest number of action movies from the USA that received an average rating of
6.5 or higher and had a runtime of less than 120 minutes.
'''


# In[163]:


year_counts = df3['year'].value_counts()
sorted_years = year_counts.sort_values(ascending=False)
second_highest_year = sorted_years.index[1]
second_highest_year


# In[ ]:





# In[ ]:


'''
h. Count of Movies with High Ratings: Count and print the number of movies that have
received at least five reviews with a rating of 7 or higher.
'''


# In[165]:


high_ratings_count = df3[df3['rating'] >= 7].groupby('title')['rating'].count()
qualified_movies = high_ratings_count[high_ratings_count >= 5]
num_qualified_movies = len(qualified_movies)
num_qualified_movies


# In[ ]:




