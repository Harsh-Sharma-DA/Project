import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#to import csv
df=pd.read_csv("netflix_titles.csv")

#for deleting duplicate data
print(df.drop_duplicates())

#for data cleaning
df=df.dropna(subset='rating')
df=df.dropna(subset='date_added')
df['director']=df['director'].fillna('not known')
df['cast']=df['cast'].fillna('no cast')
df['country']=df['country'].fillna('no country')
print(df.info())

#for ploting graphs 

#for ploting number of movies releasing per year
year_count = (df['release_year'].astype(int).value_counts().sort_index())
plt.figure(figsize=(12,6))
plt.bar(year_count.index,year_count.values)
plt.title('Number of movies releases per year')
plt.xlabel('Years')
plt.ylabel('Number of movies')
plt.xticks(rotation=90)
plt.tight_layout()
#for saving image into png
plt.savefig('Movies_per_year.png')
plt.show()

#for showing the difference between the no. of movies and shows
type_split=(df['type'].value_counts())
plt.figure(figsize=(6,6))
plt.bar(type_split.index, type_split.values)
plt.title('Split between movie and tv show')
plt.xlabel('Types')
plt.ylabel('No. of movie or show')
plt.tight_layout()
#for saving image into png
plt.savefig('movies_Vs_Tv.png')
plt.show()

#for top 10 genre
genre=(df['listed_in'].value_counts().head(10))
plt.figure(figsize=(12,6))
plt.bar(genre.index, genre.values)
plt.title('Genre')
plt.xlabel('Genre type')
plt.ylabel('No. of movie')
plt.xticks(rotation=90)
plt.tight_layout()
#for saving image into png
plt.savefig('Top_10_movies.png')
plt.show()

