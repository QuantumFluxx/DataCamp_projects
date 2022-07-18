{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d267ecd1",
   "metadata": {},
   "source": [
    "# Merging Tables With Different Join Types\n",
    "\n",
    "## Counting missing rows with left join\n",
    "The Movie Database is supported by volunteers going out into the world, collecting data, and entering it into the database. This includes financial data, such as movie budget and revenue. If you wanted to know which movies are still missing data, you could use a left join to identify them. Practice using a left join by merging the `movies` table and the `financials` table.\n",
    "\n",
    "What column is likely the best column to merge the two tables on?\n",
    "\n",
    "* on='budget'\n",
    "\n",
    "* on='popularity'\n",
    "\n",
    "* **on='id'**\n",
    "\n",
    "* Merge the `movies` table, as the left table, with the `financials` table using a left join, and save the result to `movies_financials`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5edf6cde",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "financials = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/financials.p')\n",
    "movies = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/movies.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b280f238",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge the movies table with the financials table with a left join\n",
    "movies_financials = movies.merge(financials, on='id', how='left')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d7634d4",
   "metadata": {},
   "source": [
    "* Count the number of rows in `movies_financials` with a null value in the budget column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "76d960b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1574\n"
     ]
    }
   ],
   "source": [
    "# Count the number of rows in the budget column that are missing\n",
    "number_of_missing_fin = movies_financials['budget'].isnull().sum()\n",
    "\n",
    "# Print the number of movies missing financials\n",
    "print(number_of_missing_fin)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c0fcdde6",
   "metadata": {},
   "source": [
    "Great job! You used a left join to find out which rows in the financials table were missing data. When performing a left join, the .merge() method returns a row full of null values for columns in the right table if the key column does not have a matching value in both tables. We see that there are at least 1,500 rows missing data. Wow! That sounds like a lot of work.\n",
    "\n",
    "## Enriching a dataset\n",
    "Setting `how='left'` with the `.merge()` method is a useful technique for enriching or enhancing a dataset with additional information from a different table. In this exercise, you will start off with a sample of movie data from the movie series Toy Story. Your goal is to enrich this data by adding the marketing tag line for each movie. You will compare the results of a left join versus an inner join.\n",
    "\n",
    "* Merge `toy_story` and `taglines` on the id column with a left join, and save the result as `toystory_tag`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fd759799",
   "metadata": {},
   "outputs": [],
   "source": [
    "toy_story = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/movies.p')\n",
    "taglines = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/taglines.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9b5aeded",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         id                 title  popularity release_date  \\\n",
      "0       257          Oliver Twist   20.415572   2005-09-23   \n",
      "1     14290  Better Luck Tomorrow    3.877036   2002-01-12   \n",
      "2     38365             Grown Ups   38.864027   2010-06-24   \n",
      "3      9672              Infamous    3.680896   2006-11-16   \n",
      "4     12819       Alpha and Omega   12.300789   2010-09-17   \n",
      "...     ...                   ...         ...          ...   \n",
      "4798   3089             Red River    5.344815   1948-08-26   \n",
      "4799  11934   The Hudsucker Proxy   14.188982   1994-03-11   \n",
      "4800  13807                Exiled    8.486390   2006-09-06   \n",
      "4801  73873          Albert Nobbs    7.802245   2011-12-21   \n",
      "4802  11622   Blast from the Past    8.737058   1999-02-12   \n",
      "\n",
      "                                                tagline  \n",
      "0                                                   NaN  \n",
      "1                  Never underestimate an overachiever.  \n",
      "2       Boys will be boys. . . some longer than others.  \n",
      "3               There's more to the story than you know  \n",
      "4                                A Pawsome 3D Adventure  \n",
      "...                                                 ...  \n",
      "4798  Big as the men who faced this challenge! Bold ...  \n",
      "4799  They took him for a fall guy... but he threw t...  \n",
      "4800                                                NaN  \n",
      "4801         A man with a secret. A woman with a dream.  \n",
      "4802  She'd never met anyone like him. He's never me...  \n",
      "\n",
      "[4803 rows x 5 columns]\n",
      "(4803, 5)\n"
     ]
    }
   ],
   "source": [
    "# Merge the toy_story and taglines tables with a left join\n",
    "toystory_tag = toy_story.merge(taglines, on='id', how='left')\n",
    "\n",
    "# Print the rows and shape of toystory_tag\n",
    "print(toystory_tag)\n",
    "print(toystory_tag.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "106e5dd2",
   "metadata": {},
   "source": [
    "* With `toy_story` as the left table, merge to it taglines on the id column with an inner join, and save as `toystory_tag`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "55ae0f44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         id                 title  popularity release_date  \\\n",
      "0     14290  Better Luck Tomorrow    3.877036   2002-01-12   \n",
      "1     38365             Grown Ups   38.864027   2010-06-24   \n",
      "2      9672              Infamous    3.680896   2006-11-16   \n",
      "3     12819       Alpha and Omega   12.300789   2010-09-17   \n",
      "4     49529           John Carter   43.926995   2012-03-07   \n",
      "...     ...                   ...         ...          ...   \n",
      "3950  12281            Mean Creek    8.519202   2004-01-15   \n",
      "3951   3089             Red River    5.344815   1948-08-26   \n",
      "3952  11934   The Hudsucker Proxy   14.188982   1994-03-11   \n",
      "3953  73873          Albert Nobbs    7.802245   2011-12-21   \n",
      "3954  11622   Blast from the Past    8.737058   1999-02-12   \n",
      "\n",
      "                                                tagline  \n",
      "0                  Never underestimate an overachiever.  \n",
      "1       Boys will be boys. . . some longer than others.  \n",
      "2               There's more to the story than you know  \n",
      "3                                A Pawsome 3D Adventure  \n",
      "4                  Lost in our world, found in another.  \n",
      "...                                                 ...  \n",
      "3950        Beneath the surface, everyone has a secret.  \n",
      "3951  Big as the men who faced this challenge! Bold ...  \n",
      "3952  They took him for a fall guy... but he threw t...  \n",
      "3953         A man with a secret. A woman with a dream.  \n",
      "3954  She'd never met anyone like him. He's never me...  \n",
      "\n",
      "[3955 rows x 5 columns]\n",
      "(3955, 5)\n"
     ]
    }
   ],
   "source": [
    "# Merge the toy_story and taglines tables with a inner join\n",
    "toystory_tag = toy_story.merge(taglines, on='id', how='inner')\n",
    "\n",
    "# Print the rows and shape of toystory_tag\n",
    "print(toystory_tag)\n",
    "print(toystory_tag.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1d04ee2",
   "metadata": {},
   "source": [
    "## How many rows with a left join?\n",
    "Select the true statement about left joins.\n",
    "\n",
    "Try running the following code statements in the IPython shell.\n",
    "```python\n",
    "left_table.merge(one_to_one, on='id', how='left').shape\n",
    "left_table.merge(one_to_many, on='id', how='left').shape\n",
    "```\n",
    "Note that the `left_table` starts out with 4 rows.\n",
    "\n",
    "* The output of a one-to-one merge with a left join will have more rows than the left table.\n",
    "\n",
    "* The output of a one-to-one merge with a left join will have fewer rows than the left table.\n",
    "\n",
    "* **The output of a one-to-many merge with a left join will have greater than or equal rows than the left table.**\n",
    "\n",
    "That's correct! A left join will return all of the rows from the left table. If those rows in the left table match multiple rows in the right table, then all of those rows will be returned. Therefore, the returned rows must be equal to if not greater than the left table. Knowing what to expect is useful in troubleshooting any suspicious merges.\n",
    "\n",
    "## Right join to find unique movies\n",
    "Most of the recent big-budget science fiction movies can also be classified as action movies. You are given a table of science fiction movies called scifi_movies and another table of action movies called action_movies. Your goal is to find which movies are considered only science fiction movies. Once you have this table, you can merge the movies table in to see the movie names. Since this exercise is related to science fiction movies, use a right join as your superhero power to solve this problem.\n",
    "\n",
    "The `movies`, `scifi_movies`, and `action_movies` tables have been loaded for you.\n",
    "\n",
    "* Merge `action_movies` and `scifi_movies` tables with a right join on `movie_id`. Save the result as `action_scifi`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b6ae653b",
   "metadata": {},
   "outputs": [],
   "source": [
    "genres = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/movie_to_genres.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2aa9f55c",
   "metadata": {},
   "outputs": [],
   "source": [
    "scifi_movies = genres.query(\"genre == 'Science Fiction'\")\n",
    "action_movies = genres.query(\"genre == 'Action'\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b6cae5d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge action_movies to scifi_movies with right join\n",
    "action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "957650de",
   "metadata": {},
   "source": [
    "* Update the merge to add suffixes, where `'_act'` and `'_sci'` are suffixes for the left and right tables, respectively."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "414c3ac4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   movie_id genre_act        genre_sci\n",
      "0        11    Action  Science Fiction\n",
      "1        18    Action  Science Fiction\n",
      "2        19       NaN  Science Fiction\n",
      "3        38       NaN  Science Fiction\n",
      "4        62       NaN  Science Fiction\n"
     ]
    }
   ],
   "source": [
    "# Merge action_movies to scifi_movies with right join\n",
    "action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',\n",
    "                                   suffixes=('_act','_sci'))\n",
    "\n",
    "# Print the first few rows of action_scifi to see the structure\n",
    "print(action_scifi.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71615d8b",
   "metadata": {},
   "source": [
    "* From `action_scifi`, subset only the rows where the `genre_act` column is null."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "748e9927",
   "metadata": {},
   "outputs": [],
   "source": [
    "# From action_scifi, select only the rows where the genre_act column is null\n",
    "scifi_only = action_scifi[action_scifi['genre_act'].isnull()]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e7d1f47",
   "metadata": {},
   "source": [
    "* Merge movies and `scifi_only` using the id column in the left table and the `movie_id` column in the right table with an inner join."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f45323ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      id                         title  popularity release_date  movie_id  \\\n",
      "0  18841  The Lost Skeleton of Cadavra    1.680525   2001-09-12     18841   \n",
      "1  26672     The Thief and the Cobbler    2.439184   1993-09-23     26672   \n",
      "2  15301      Twilight Zone: The Movie   12.902975   1983-06-24     15301   \n",
      "3   8452                   The 6th Day   18.447479   2000-11-17      8452   \n",
      "4   1649    Bill & Ted's Bogus Journey   11.349664   1991-07-19      1649   \n",
      "\n",
      "  genre_act        genre_sci  \n",
      "0       NaN  Science Fiction  \n",
      "1       NaN  Science Fiction  \n",
      "2       NaN  Science Fiction  \n",
      "3       NaN  Science Fiction  \n",
      "4       NaN  Science Fiction  \n",
      "(258, 7)\n"
     ]
    }
   ],
   "source": [
    "# Merge the movies and scifi_only tables with an inner join\n",
    "movies_and_scifi_only = movies.merge(scifi_only, how='inner',\n",
    "                                     left_on='id', right_on='movie_id')\n",
    "\n",
    "# Print the first few rows and shape of movies_and_scifi_only\n",
    "print(movies_and_scifi_only.head())\n",
    "print(movies_and_scifi_only.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b894b9ca",
   "metadata": {},
   "source": [
    "Well done, right join to the rescue! You found over 250 action only movies by merging action_movies and scifi_movies using a right join. With this, you were able to find the rows not found in the action_movies table. Additionally, you used the left_on and right_on arguments to merge in the movies table. Wow! You are a superhero."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "705501db",
   "metadata": {},
   "source": [
    "## Popular genres with right join\n",
    "What are the genres of the most popular movies? To answer this question, you need to merge data from the movies and `movie_to_genres` tables. In a table called pop_movies, the top 10 most popular movies in the movies table have been selected. To ensure that you are analyzing all of the popular movies, merge it with the `movie_to_genres` table using a right join. To complete your analysis, count the number of different genres. Also, the two tables can be merged by the movie ID. However, in `pop_movies` that column is called id, and in movies_to_genres it's called `movie_id`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "babbcb08",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "pop_movies = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/ratings.p')\n",
    "movie_to_genres = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/movies.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cde07dee",
   "metadata": {},
   "outputs": [],
   "source": [
    "genres_movies = movie_to_genres.merge(pop_movies, how='right', \n",
    "                                      left_on='movie_id', \n",
    "                                      right_on='id')\n",
    "\n",
    "# Count the number of genres\n",
    "genre_count = genres_movies.groupby('genre').agg({'id':'count'})\n",
    "\n",
    "# Plot a bar chart of the genre_count\n",
    "genre_count.plot(kind='bar')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1584b908",
   "metadata": {},
   "source": [
    "![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIKICAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyBoZWlnaHQ9IjQyNnB0IiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCA1NjYgNDI2IiB3aWR0aD0iNTY2cHQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPgogPG1ldGFkYXRhPgogIDxyZGY6UkRGIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgPGNjOldvcms+CiAgICA8ZGM6dHlwZSByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIi8+CiAgICA8ZGM6ZGF0ZT4yMDIyLTA3LTE4VDIxOjQzOjAwLjk3MTA5ODwvZGM6ZGF0ZT4KICAgIDxkYzpmb3JtYXQ+aW1hZ2Uvc3ZnK3htbDwvZGM6Zm9ybWF0PgogICAgPGRjOmNyZWF0b3I+CiAgICAgPGNjOkFnZW50PgogICAgICA8ZGM6dGl0bGU+TWF0cGxvdGxpYiB2My40LjMsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvPC9kYzp0aXRsZT4KICAgICA8L2NjOkFnZW50PgogICAgPC9kYzpjcmVhdG9yPgogICA8L2NjOldvcms+CiAgPC9yZGY6UkRGPgogPC9tZXRhZGF0YT4KIDxkZWZzPgogIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+KntzdHJva2UtbGluZWNhcDpidXR0O3N0cm9rZS1saW5lam9pbjpyb3VuZDt9PC9zdHlsZT4KIDwvZGVmcz4KIDxnIGlkPSJmaWd1cmVfMSI+CiAgPGcgaWQ9InBhdGNoXzEiPgogICA8cGF0aCBkPSJNIDAgNDI2IApMIDU2NiA0MjYgCkwgNTY2IDAgCkwgMCAwIAp6CiIgc3R5bGU9ImZpbGw6I2ZmZmZmZjsiLz4KICA8L2c+CiAgPGcgaWQ9ImF4ZXNfMSI+CiAgIDxnIGlkPSJwYXRjaF8yIj4KICAgIDxwYXRoIGQ9Ik0gMjQuMTYyNSAzMjAuMTE4NzUgCkwgNTU1LjIgMzIwLjExODc1IApMIDU1NS4yIDEwLjggCkwgMjQuMTYyNSAxMC44IAp6CiIgc3R5bGU9ImZpbGw6I2ZmZmZmZjsiLz4KICAgPC9nPgogICA8ZyBpZD0icGF0Y2hfMyI+CiAgICA8cGF0aCBjbGlwLXBhdGg9InVybCgjcDVkNTU4YzYzNDgpIiBkPSJNIDM4LjkxMzU0MiAzMjAuMTE4NzUgCkwgNjguNDE1NjI1IDMyMC4xMTg3NSAKTCA2OC40MTU2MjUgOTAuOTkzNzUgCkwgMzguOTEzNTQyIDkwLjk5Mzc1IAp6CiIgc3R5bGU9ImZpbGw6IzFmNzdiNDsiLz4KICAgPC9nPgogICA8ZyBpZD0icGF0Y2hfNCI+CiAgICA8cGF0aCBjbGlwLXBhdGg9InVybCgjcDVkNTU4YzYzNDgpIiBkPSJNIDk3LjkxNzcwOCAzMjAuMTE4NzUgCkwgMTI3LjQxOTc5MiAzMjAuMTE4NzUgCkwgMTI3LjQxOTc5MiAyNS41Mjk0NjQgCkwgOTcuOTE3NzA4IDI1LjUyOTQ2NCAKegoiIHN0eWxlPSJmaWxsOiMxZjc3YjQ7Ii8+CiAgIDwvZz4KICAgPGcgaWQ9InBhdGNoXzUiPgogICAgPHBhdGggY2xpcC1wYXRoPSJ1cmwoI3A1ZDU1OGM2MzQ4KSIgZD0iTSAxNTYuOTIxODc1IDMyMC4xMTg3NSAKTCAxODYuNDIzOTU4IDMyMC4xMTg3NSAKTCAxODYuNDIzOTU4IDI1NC42NTQ0NjQgCkwgMTU2LjkyMTg3NSAyNTQuNjU0NDY0IAp6CiIgc3R5bGU9ImZpbGw6IzFmNzdiNDsiLz4KICAgPC9nPgogICA8ZyBpZD0icGF0Y2hfNiI+CiAgICA8cGF0aCBjbGlwLXBhdGg9InVybCgjcDVkNTU4YzYzNDgpIiBkPSJNIDIxNS45MjYwNDIgMzIwLjExODc1IApMIDI0NS40MjgxMjUgMzIwLjExODc1IApMIDI0NS40MjgxMjUgMjIxLjkyMjMyMSAKTCAyMTUuOTI2MDQyIDIyMS45MjIzMjEgCnoKIiBzdHlsZT0iZmlsbDojMWY3N2I0OyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF83Ij4KICAgIDxwYXRoIGNsaXAtcGF0aD0idXJsKCNwNWQ1NThjNjM0OCkiIGQ9Ik0gMjc0LjkzMDIwOCAzMjAuMTE4NzUgCkwgMzA0LjQzMjI5MiAzMjAuMTE4NzUgCkwgMzA0LjQzMjI5MiAyNTQuNjU0NDY0IApMIDI3NC45MzAyMDggMjU0LjY1NDQ2NCAKegoiIHN0eWxlPSJmaWxsOiMxZjc3YjQ7Ii8+CiAgIDwvZz4KICAgPGcgaWQ9InBhdGNoXzgiPgogICAgPHBhdGggY2xpcC1wYXRoPSJ1cmwoI3A1ZDU1OGM2MzQ4KSIgZD0iTSAzMzMuOTM0Mzc1IDMyMC4xMTg3NSAKTCAzNjMuNDM2NDU4IDMyMC4xMTg3NSAKTCAzNjMuNDM2NDU4IDI1NC42NTQ0NjQgCkwgMzMzLjkzNDM3NSAyNTQuNjU0NDY0IAp6CiIgc3R5bGU9ImZpbGw6IzFmNzdiNDsiLz4KICAgPC9nPgogICA8ZyBpZD0icGF0Y2hfOSI+CiAgICA8cGF0aCBjbGlwLXBhdGg9InVybCgjcDVkNTU4YzYzNDgpIiBkPSJNIDM5Mi45Mzg1NDIgMzIwLjExODc1IApMIDQyMi40NDA2MjUgMzIwLjExODc1IApMIDQyMi40NDA2MjUgMjg3LjM4NjYwNyAKTCAzOTIuOTM4NTQyIDI4Ny4zODY2MDcgCnoKIiBzdHlsZT0iZmlsbDojMWY3N2I0OyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF8xMCI+CiAgICA8cGF0aCBjbGlwLXBhdGg9InVybCgjcDVkNTU4YzYzNDgpIiBkPSJNIDQ1MS45NDI3MDggMzIwLjExODc1IApMIDQ4MS40NDQ3OTIgMzIwLjExODc1IApMIDQ4MS40NDQ3OTIgMTIzLjcyNTg5MyAKTCA0NTEuOTQyNzA4IDEyMy43MjU4OTMgCnoKIiBzdHlsZT0iZmlsbDojMWY3N2I0OyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF8xMSI+CiAgICA8cGF0aCBjbGlwLXBhdGg9InVybCgjcDVkNTU4YzYzNDgpIiBkPSJNIDUxMC45NDY4NzUgMzIwLjExODc1IApMIDU0MC40NDg5NTggMzIwLjExODc1IApMIDU0MC40NDg5NTggMTg5LjE5MDE3OSAKTCA1MTAuOTQ2ODc1IDE4OS4xOTAxNzkgCnoKIiBzdHlsZT0iZmlsbDojMWY3N2I0OyIvPgogICA8L2c+CiAgIDxnIGlkPSJtYXRwbG90bGliLmF4aXNfMSI+CiAgICA8ZyBpZD0ieHRpY2tfMSI+CiAgICAgPGcgaWQ9ImxpbmUyZF8xIj4KICAgICAgPGRlZnM+CiAgICAgICA8cGF0aCBkPSJNIDAgMCAKTCAwIDMuNSAKIiBpZD0ibTU4ZjQzNTgwNGIiIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIvPgogICAgICA8L2RlZnM+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjUzLjY2NDU4MyIgeGxpbms6aHJlZj0iI201OGY0MzU4MDRiIiB5PSIzMjAuMTE4NzUiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgICA8ZyBpZD0idGV4dF8xIj4KICAgICAgPCEtLSBBY3Rpb24gLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDU2LjQyMzk1OCAzNTguNDM3NSlyb3RhdGUoLTkwKXNjYWxlKDAuMSAtMC4xKSI+CiAgICAgICA8ZGVmcz4KICAgICAgICA8cGF0aCBkPSJNIDIxODggNDA0NCAKTCAxMzMxIDE3MjIgCkwgMzA0NyAxNzIyIApMIDIxODggNDA0NCAKegpNIDE4MzEgNDY2NiAKTCAyNTQ3IDQ2NjYgCkwgNDMyNSAwIApMIDM2NjkgMCAKTCAzMjQ0IDExOTcgCkwgMTE0MSAxMTk3IApMIDcxNiAwIApMIDUwIDAgCkwgMTgzMSA0NjY2IAp6CiIgaWQ9IkRlamFWdVNhbnMtNDEiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICAgPHBhdGggZD0iTSAzMTIyIDMzNjYgCkwgMzEyMiAyODI4IApRIDI4NzggMjk2MyAyNjMzIDMwMzAgClEgMjM4OCAzMDk3IDIxMzggMzA5NyAKUSAxNTc4IDMwOTcgMTI2OCAyNzQyIApRIDk1OSAyMzg4IDk1OSAxNzQ3IApRIDk1OSAxMTA2IDEyNjggNzUxIApRIDE1NzggMzk3IDIxMzggMzk3IApRIDIzODggMzk3IDI2MzMgNDY0IApRIDI4NzggNTMxIDMxMjIgNjY2IApMIDMxMjIgMTM0IApRIDI4ODEgMjIgMjYyMyAtMzQgClEgMjM2NiAtOTEgMjA3NSAtOTEgClEgMTI4NCAtOTEgODE4IDQwNiAKUSAzNTMgOTAzIDM1MyAxNzQ3IApRIDM1MyAyNjAzIDgyMyAzMDkzIApRIDEyOTQgMzU4NCAyMTEzIDM1ODQgClEgMjM3OCAzNTg0IDI2MzEgMzUyOSAKUSAyODg0IDM0NzUgMzEyMiAzMzY2IAp6CiIgaWQ9IkRlamFWdVNhbnMtNjMiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICAgPHBhdGggZD0iTSAxMTcyIDQ0OTQgCkwgMTE3MiAzNTAwIApMIDIzNTYgMzUwMCAKTCAyMzU2IDMwNTMgCkwgMTE3MiAzMDUzIApMIDExNzIgMTE1MyAKUSAxMTcyIDcyNSAxMjg5IDYwMyAKUSAxNDA2IDQ4MSAxNzY2IDQ4MSAKTCAyMzU2IDQ4MSAKTCAyMzU2IDAgCkwgMTc2NiAwIApRIDExMDAgMCA4NDcgMjQ4IApRIDU5NCA0OTcgNTk0IDExNTMgCkwgNTk0IDMwNTMgCkwgMTcyIDMwNTMgCkwgMTcyIDM1MDAgCkwgNTk0IDM1MDAgCkwgNTk0IDQ0OTQgCkwgMTE3MiA0NDk0IAp6CiIgaWQ9IkRlamFWdVNhbnMtNzQiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICAgPHBhdGggZD0iTSA2MDMgMzUwMCAKTCAxMTc4IDM1MDAgCkwgMTE3OCAwIApMIDYwMyAwIApMIDYwMyAzNTAwIAp6Ck0gNjAzIDQ4NjMgCkwgMTE3OCA0ODYzIApMIDExNzggNDEzNCAKTCA2MDMgNDEzNCAKTCA2MDMgNDg2MyAKegoiIGlkPSJEZWphVnVTYW5zLTY5IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgIDxwYXRoIGQ9Ik0gMTk1OSAzMDk3IApRIDE0OTcgMzA5NyAxMjI4IDI3MzYgClEgOTU5IDIzNzUgOTU5IDE3NDcgClEgOTU5IDExMTkgMTIyNiA3NTggClEgMTQ5NCAzOTcgMTk1OSAzOTcgClEgMjQxOSAzOTcgMjY4NyA3NTkgClEgMjk1NiAxMTIyIDI5NTYgMTc0NyAKUSAyOTU2IDIzNjkgMjY4NyAyNzMzIApRIDI0MTkgMzA5NyAxOTU5IDMwOTcgCnoKTSAxOTU5IDM1ODQgClEgMjcwOSAzNTg0IDMxMzcgMzA5NiAKUSAzNTY2IDI2MDkgMzU2NiAxNzQ3IApRIDM1NjYgODg4IDMxMzcgMzk4IApRIDI3MDkgLTkxIDE5NTkgLTkxIApRIDEyMDYgLTkxIDc3OSAzOTggClEgMzUzIDg4OCAzNTMgMTc0NyAKUSAzNTMgMjYwOSA3NzkgMzA5NiAKUSAxMjA2IDM1ODQgMTk1OSAzNTg0IAp6CiIgaWQ9IkRlamFWdVNhbnMtNmYiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICAgPHBhdGggZD0iTSAzNTEzIDIxMTMgCkwgMzUxMyAwIApMIDI5MzggMCAKTCAyOTM4IDIwOTQgClEgMjkzOCAyNTkxIDI3NDQgMjgzNyAKUSAyNTUwIDMwODQgMjE2MyAzMDg0IApRIDE2OTcgMzA4NCAxNDI4IDI3ODcgClEgMTE1OSAyNDkxIDExNTkgMTk3OCAKTCAxMTU5IDAgCkwgNTgxIDAgCkwgNTgxIDM1MDAgCkwgMTE1OSAzNTAwIApMIDExNTkgMjk1NiAKUSAxMzY2IDMyNzIgMTY0NSAzNDI4IApRIDE5MjUgMzU4NCAyMjkxIDM1ODQgClEgMjg5NCAzNTg0IDMyMDMgMzIxMSAKUSAzNTEzIDI4MzggMzUxMyAyMTEzIAp6CiIgaWQ9IkRlamFWdVNhbnMtNmUiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTQxIi8+CiAgICAgICA8dXNlIHg9IjY2LjY1ODIwMyIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjMiLz4KICAgICAgIDx1c2UgeD0iMTIxLjYzODY3MiIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNzQiLz4KICAgICAgIDx1c2UgeD0iMTYwLjg0NzY1NiIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjkiLz4KICAgICAgIDx1c2UgeD0iMTg4LjYzMDg1OSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmYiLz4KICAgICAgIDx1c2UgeD0iMjQ5LjgxMjUiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTZlIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyBpZD0ieHRpY2tfMiI+CiAgICAgPGcgaWQ9ImxpbmUyZF8yIj4KICAgICAgPGc+CiAgICAgICA8dXNlIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIgeD0iMTEyLjY2ODc1IiB4bGluazpocmVmPSIjbTU4ZjQzNTgwNGIiIHk9IjMyMC4xMTg3NSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzIiPgogICAgICA8IS0tIEFkdmVudHVyZSAtLT4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTE1LjQyODEyNSAzNzguODM5MDYzKXJvdGF0ZSgtOTApc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgIDxkZWZzPgogICAgICAgIDxwYXRoIGQ9Ik0gMjkwNiAyOTY5IApMIDI5MDYgNDg2MyAKTCAzNDgxIDQ4NjMgCkwgMzQ4MSAwIApMIDI5MDYgMCAKTCAyOTA2IDUyNSAKUSAyNzI1IDIxMyAyNDQ4IDYxIApRIDIxNzIgLTkxIDE3ODQgLTkxIApRIDExNTAgLTkxIDc1MSA0MTUgClEgMzUzIDkyMiAzNTMgMTc0NyAKUSAzNTMgMjU3MiA3NTEgMzA3OCAKUSAxMTUwIDM1ODQgMTc4NCAzNTg0IApRIDIxNzIgMzU4NCAyNDQ4IDM0MzIgClEgMjcyNSAzMjgxIDI5MDYgMjk2OSAKegpNIDk0NyAxNzQ3IApRIDk0NyAxMTEzIDEyMDggNzUyIApRIDE0NjkgMzkxIDE5MjUgMzkxIApRIDIzODEgMzkxIDI2NDMgNzUyIApRIDI5MDYgMTExMyAyOTA2IDE3NDcgClEgMjkwNiAyMzgxIDI2NDMgMjc0MiAKUSAyMzgxIDMxMDMgMTkyNSAzMTAzIApRIDE0NjkgMzEwMyAxMjA4IDI3NDIgClEgOTQ3IDIzODEgOTQ3IDE3NDcgCnoKIiBpZD0iRGVqYVZ1U2Fucy02NCIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgICA8cGF0aCBkPSJNIDE5MSAzNTAwIApMIDgwMCAzNTAwIApMIDE4OTQgNTYzIApMIDI5ODggMzUwMCAKTCAzNTk3IDM1MDAgCkwgMjI4NCAwIApMIDE1MDMgMCAKTCAxOTEgMzUwMCAKegoiIGlkPSJEZWphVnVTYW5zLTc2IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgIDxwYXRoIGQ9Ik0gMzU5NyAxODk0IApMIDM1OTcgMTYxMyAKTCA5NTMgMTYxMyAKUSA5OTEgMTAxOSAxMzExIDcwOCAKUSAxNjMxIDM5NyAyMjAzIDM5NyAKUSAyNTM0IDM5NyAyODQ1IDQ3OCAKUSAzMTU2IDU1OSAzNDYzIDcyMiAKTCAzNDYzIDE3OCAKUSAzMTUzIDQ3IDI4MjggLTIyIApRIDI1MDMgLTkxIDIxNjkgLTkxIApRIDEzMzEgLTkxIDg0MiAzOTYgClEgMzUzIDg4NCAzNTMgMTcxNiAKUSAzNTMgMjU3NSA4MTcgMzA3OSAKUSAxMjgxIDM1ODQgMjA2OSAzNTg0IApRIDI3NzUgMzU4NCAzMTg2IDMxMjkgClEgMzU5NyAyNjc1IDM1OTcgMTg5NCAKegpNIDMwMjIgMjA2MyAKUSAzMDE2IDI1MzQgMjc1OCAyODE1IApRIDI1MDAgMzA5NyAyMDc1IDMwOTcgClEgMTU5NCAzMDk3IDEzMDUgMjgyNSAKUSAxMDE2IDI1NTMgOTcyIDIwNTkgCkwgMzAyMiAyMDYzIAp6CiIgaWQ9IkRlamFWdVNhbnMtNjUiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICAgPHBhdGggZD0iTSA1NDQgMTM4MSAKTCA1NDQgMzUwMCAKTCAxMTE5IDM1MDAgCkwgMTExOSAxNDAzIApRIDExMTkgOTA2IDEzMTIgNjU3IApRIDE1MDYgNDA5IDE4OTQgNDA5IApRIDIzNTkgNDA5IDI2MjkgNzA2IApRIDI5MDAgMTAwMyAyOTAwIDE1MTYgCkwgMjkwMCAzNTAwIApMIDM0NzUgMzUwMCAKTCAzNDc1IDAgCkwgMjkwMCAwIApMIDI5MDAgNTM4IApRIDI2OTEgMjE5IDI0MTQgNjQgClEgMjEzOCAtOTEgMTc3MiAtOTEgClEgMTE2OSAtOTEgODU2IDI4NCAKUSA1NDQgNjU5IDU0NCAxMzgxIAp6Ck0gMTk5MSAzNTg0IApMIDE5OTEgMzU4NCAKegoiIGlkPSJEZWphVnVTYW5zLTc1IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgIDxwYXRoIGQ9Ik0gMjYzMSAyOTYzIApRIDI1MzQgMzAxOSAyNDIwIDMwNDUgClEgMjMwNiAzMDcyIDIxNjkgMzA3MiAKUSAxNjgxIDMwNzIgMTQyMCAyNzU1IApRIDExNTkgMjQzOCAxMTU5IDE4NDQgCkwgMTE1OSAwIApMIDU4MSAwIApMIDU4MSAzNTAwIApMIDExNTkgMzUwMCAKTCAxMTU5IDI5NTYgClEgMTM0MSAzMjc1IDE2MzEgMzQyOSAKUSAxOTIyIDM1ODQgMjMzOCAzNTg0IApRIDIzOTcgMzU4NCAyNDY5IDM1NzYgClEgMjU0MSAzNTY5IDI2MjggMzU1MyAKTCAyNjMxIDI5NjMgCnoKIiBpZD0iRGVqYVZ1U2Fucy03MiIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNDEiLz4KICAgICAgIDx1c2UgeD0iNjYuNjU4MjAzIiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02NCIvPgogICAgICAgPHVzZSB4PSIxMzAuMTM0NzY2IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03NiIvPgogICAgICAgPHVzZSB4PSIxODkuMzE0NDUzIiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02NSIvPgogICAgICAgPHVzZSB4PSIyNTAuODM3ODkxIiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02ZSIvPgogICAgICAgPHVzZSB4PSIzMTQuMjE2Nzk3IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03NCIvPgogICAgICAgPHVzZSB4PSIzNTMuNDI1NzgxIiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03NSIvPgogICAgICAgPHVzZSB4PSI0MTYuODA0Njg4IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03MiIvPgogICAgICAgPHVzZSB4PSI0NTUuNjY3OTY5IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02NSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgPC9nPgogICAgPGcgaWQ9Inh0aWNrXzMiPgogICAgIDxnIGlkPSJsaW5lMmRfMyI+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjE3MS42NzI5MTciIHhsaW5rOmhyZWY9IiNtNThmNDM1ODA0YiIgeT0iMzIwLjExODc1Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICAgPGcgaWQ9InRleHRfMyI+CiAgICAgIDwhLS0gQW5pbWF0aW9uIC0tPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNzQuNDMyMjkyIDM3OC4wOTg0Mzcpcm90YXRlKC05MClzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSAzMzI4IDI4MjggClEgMzU0NCAzMjE2IDM4NDQgMzQwMCAKUSA0MTQ0IDM1ODQgNDU1MCAzNTg0IApRIDUwOTcgMzU4NCA1Mzk0IDMyMDEgClEgNTY5MSAyODE5IDU2OTEgMjExMyAKTCA1NjkxIDAgCkwgNTExMyAwIApMIDUxMTMgMjA5NCAKUSA1MTEzIDI1OTcgNDkzNCAyODQwIApRIDQ3NTYgMzA4NCA0MzkxIDMwODQgClEgMzk0NCAzMDg0IDM2ODQgMjc4NyAKUSAzNDI1IDI0OTEgMzQyNSAxOTc4IApMIDM0MjUgMCAKTCAyODQ3IDAgCkwgMjg0NyAyMDk0IApRIDI4NDcgMjYwMCAyNjY5IDI4NDIgClEgMjQ5MSAzMDg0IDIxMTkgMzA4NCAKUSAxNjc4IDMwODQgMTQxOCAyNzg2IApRIDExNTkgMjQ4OCAxMTU5IDE5NzggCkwgMTE1OSAwIApMIDU4MSAwIApMIDU4MSAzNTAwIApMIDExNTkgMzUwMCAKTCAxMTU5IDI5NTYgClEgMTM1NiAzMjc4IDE2MzEgMzQzMSAKUSAxOTA2IDM1ODQgMjI4NCAzNTg0IApRIDI2NjYgMzU4NCAyOTMzIDMzOTAgClEgMzIwMCAzMTk3IDMzMjggMjgyOCAKegoiIGlkPSJEZWphVnVTYW5zLTZkIiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgIDxwYXRoIGQ9Ik0gMjE5NCAxNzU5IApRIDE0OTcgMTc1OSAxMjI4IDE2MDAgClEgOTU5IDE0NDEgOTU5IDEwNTYgClEgOTU5IDc1MCAxMTYxIDU3MCAKUSAxMzYzIDM5MSAxNzA5IDM5MSAKUSAyMTg4IDM5MSAyNDc3IDczMCAKUSAyNzY2IDEwNjkgMjc2NiAxNjMxIApMIDI3NjYgMTc1OSAKTCAyMTk0IDE3NTkgCnoKTSAzMzQxIDE5OTcgCkwgMzM0MSAwIApMIDI3NjYgMCAKTCAyNzY2IDUzMSAKUSAyNTY5IDIxMyAyMjc1IDYxIApRIDE5ODEgLTkxIDE1NTYgLTkxIApRIDEwMTkgLTkxIDcwMSAyMTEgClEgMzg0IDUxMyAzODQgMTAxOSAKUSAzODQgMTYwOSA3NzkgMTkwOSAKUSAxMTc1IDIyMDkgMTk1OSAyMjA5IApMIDI3NjYgMjIwOSAKTCAyNzY2IDIyNjYgClEgMjc2NiAyNjYzIDI1MDUgMjg4MCAKUSAyMjQ0IDMwOTcgMTc3MiAzMDk3IApRIDE0NzIgMzA5NyAxMTg3IDMwMjUgClEgOTAzIDI5NTMgNjQxIDI4MDkgCkwgNjQxIDMzNDEgClEgOTU2IDM0NjMgMTI1MyAzNTIzIApRIDE1NTAgMzU4NCAxODMxIDM1ODQgClEgMjU5MSAzNTg0IDI5NjYgMzE5MCAKUSAzMzQxIDI3OTcgMzM0MSAxOTk3IAp6CiIgaWQ9IkRlamFWdVNhbnMtNjEiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTQxIi8+CiAgICAgICA8dXNlIHg9IjY4LjQwODIwMyIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmUiLz4KICAgICAgIDx1c2UgeD0iMTMxLjc4NzEwOSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjkiLz4KICAgICAgIDx1c2UgeD0iMTU5LjU3MDMxMiIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmQiLz4KICAgICAgIDx1c2UgeD0iMjU2Ljk4MjQyMiIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjEiLz4KICAgICAgIDx1c2UgeD0iMzE4LjI2MTcxOSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNzQiLz4KICAgICAgIDx1c2UgeD0iMzU3LjQ3MDcwMyIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjkiLz4KICAgICAgIDx1c2UgeD0iMzg1LjI1MzkwNiIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmYiLz4KICAgICAgIDx1c2UgeD0iNDQ2LjQzNTU0NyIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmUiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgIDwvZz4KICAgIDxnIGlkPSJ4dGlja180Ij4KICAgICA8ZyBpZD0ibGluZTJkXzQiPgogICAgICA8Zz4KICAgICAgIDx1c2Ugc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjg7IiB4PSIyMzAuNjc3MDgzIiB4bGluazpocmVmPSIjbTU4ZjQzNTgwNGIiIHk9IjMyMC4xMTg3NSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzQiPgogICAgICA8IS0tIENvbWVkeSAtLT4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjMzLjQzNjQ1OCAzNjguMzgxMjUpcm90YXRlKC05MClzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSA0MTIyIDQzMDYgCkwgNDEyMiAzNjQxIApRIDM4MDMgMzkzOCAzNDQyIDQwODQgClEgMzA4MSA0MjMxIDI2NzUgNDIzMSAKUSAxODc1IDQyMzEgMTQ1MCAzNzQyIApRIDEwMjUgMzI1MyAxMDI1IDIzMjggClEgMTAyNSAxNDA2IDE0NTAgOTE3IApRIDE4NzUgNDI4IDI2NzUgNDI4IApRIDMwODEgNDI4IDM0NDIgNTc1IApRIDM4MDMgNzIyIDQxMjIgMTAxOSAKTCA0MTIyIDM1OSAKUSAzNzkxIDEzNCAzNDIwIDIxIApRIDMwNTAgLTkxIDI2MzggLTkxIApRIDE1NzggLTkxIDk2OCA1NTcgClEgMzU5IDEyMDYgMzU5IDIzMjggClEgMzU5IDM0NTMgOTY4IDQxMDEgClEgMTU3OCA0NzUwIDI2MzggNDc1MCAKUSAzMDU2IDQ3NTAgMzQyNiA0NjM5IApRIDM3OTcgNDUyOCA0MTIyIDQzMDYgCnoKIiBpZD0iRGVqYVZ1U2Fucy00MyIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgICA8cGF0aCBkPSJNIDIwNTkgLTMyNSAKUSAxODE2IC05NTAgMTU4NCAtMTE0MCAKUSAxMzUzIC0xMzMxIDk2NiAtMTMzMSAKTCA1MDYgLTEzMzEgCkwgNTA2IC04NTAgCkwgODQ0IC04NTAgClEgMTA4MSAtODUwIDEyMTIgLTczNyAKUSAxMzQ0IC02MjUgMTUwMyAtMjA2IApMIDE2MDYgNTYgCkwgMTkxIDM1MDAgCkwgODAwIDM1MDAgCkwgMTg5NCA3NjMgCkwgMjk4OCAzNTAwIApMIDM1OTcgMzUwMCAKTCAyMDU5IC0zMjUgCnoKIiBpZD0iRGVqYVZ1U2Fucy03OSIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNDMiLz4KICAgICAgIDx1c2UgeD0iNjkuODI0MjE5IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02ZiIvPgogICAgICAgPHVzZSB4PSIxMzEuMDA1ODU5IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02ZCIvPgogICAgICAgPHVzZSB4PSIyMjguNDE3OTY5IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02NSIvPgogICAgICAgPHVzZSB4PSIyODkuOTQxNDA2IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02NCIvPgogICAgICAgPHVzZSB4PSIzNTMuNDE3OTY5IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03OSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgPC9nPgogICAgPGcgaWQ9Inh0aWNrXzUiPgogICAgIDxnIGlkPSJsaW5lMmRfNSI+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjI4OS42ODEyNSIgeGxpbms6aHJlZj0iI201OGY0MzU4MDRiIiB5PSIzMjAuMTE4NzUiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgICA8ZyBpZD0idGV4dF81Ij4KICAgICAgPCEtLSBEcmFtYSAtLT4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjkyLjQ0MDYyNSAzNjAuOTI2NTYzKXJvdGF0ZSgtOTApc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgIDxkZWZzPgogICAgICAgIDxwYXRoIGQ9Ik0gMTI1OSA0MTQ3IApMIDEyNTkgNTE5IApMIDIwMjIgNTE5IApRIDI5ODggNTE5IDM0MzYgOTU2IApRIDM4ODQgMTM5NCAzODg0IDIzMzggClEgMzg4NCAzMjc1IDM0MzYgMzcxMSAKUSAyOTg4IDQxNDcgMjAyMiA0MTQ3IApMIDEyNTkgNDE0NyAKegpNIDYyOCA0NjY2IApMIDE5MjUgNDY2NiAKUSAzMjgxIDQ2NjYgMzkxNSA0MTAyIApRIDQ1NTAgMzUzOCA0NTUwIDIzMzggClEgNDU1MCAxMTMxIDM5MTIgNTY1IApRIDMyNzUgMCAxOTI1IDAgCkwgNjI4IDAgCkwgNjI4IDQ2NjYgCnoKIiBpZD0iRGVqYVZ1U2Fucy00NCIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNDQiLz4KICAgICAgIDx1c2UgeD0iNzcuMDAxOTUzIiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03MiIvPgogICAgICAgPHVzZSB4PSIxMTguMTE1MjM0IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02MSIvPgogICAgICAgPHVzZSB4PSIxNzkuMzk0NTMxIiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02ZCIvPgogICAgICAgPHVzZSB4PSIyNzYuODA2NjQxIiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02MSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgPC9nPgogICAgPGcgaWQ9Inh0aWNrXzYiPgogICAgIDxnIGlkPSJsaW5lMmRfNiI+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjM0OC42ODU0MTciIHhsaW5rOmhyZWY9IiNtNThmNDM1ODA0YiIgeT0iMzIwLjExODc1Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICAgPGcgaWQ9InRleHRfNiI+CiAgICAgIDwhLS0gRmFtaWx5IC0tPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzNTEuNDQ0NzkyIDM1OS4zMDE1NjMpcm90YXRlKC05MClzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSA2MjggNDY2NiAKTCAzMzA5IDQ2NjYgCkwgMzMwOSA0MTM0IApMIDEyNTkgNDEzNCAKTCAxMjU5IDI3NTkgCkwgMzEwOSAyNzU5IApMIDMxMDkgMjIyOCAKTCAxMjU5IDIyMjggCkwgMTI1OSAwIApMIDYyOCAwIApMIDYyOCA0NjY2IAp6CiIgaWQ9IkRlamFWdVNhbnMtNDYiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICAgPHBhdGggZD0iTSA2MDMgNDg2MyAKTCAxMTc4IDQ4NjMgCkwgMTE3OCAwIApMIDYwMyAwIApMIDYwMyA0ODYzIAp6CiIgaWQ9IkRlamFWdVNhbnMtNmMiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTQ2Ii8+CiAgICAgICA8dXNlIHg9IjQ4LjM5NDUzMSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjEiLz4KICAgICAgIDx1c2UgeD0iMTA5LjY3MzgyOCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmQiLz4KICAgICAgIDx1c2UgeD0iMjA3LjA4NTkzOCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjkiLz4KICAgICAgIDx1c2UgeD0iMjM0Ljg2OTE0MSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmMiLz4KICAgICAgIDx1c2UgeD0iMjYyLjY1MjM0NCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNzkiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgIDwvZz4KICAgIDxnIGlkPSJ4dGlja183Ij4KICAgICA8ZyBpZD0ibGluZTJkXzciPgogICAgICA8Zz4KICAgICAgIDx1c2Ugc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjg7IiB4PSI0MDcuNjg5NTgzIiB4bGluazpocmVmPSIjbTU4ZjQzNTgwNGIiIHk9IjMyMC4xMTg3NSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzciPgogICAgICA8IS0tIEZhbnRhc3kgLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQxMC40NDg5NTggMzY1LjYpcm90YXRlKC05MClzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSAyODM0IDMzOTcgCkwgMjgzNCAyODUzIApRIDI1OTEgMjk3OCAyMzI4IDMwNDAgClEgMjA2NiAzMTAzIDE3ODQgMzEwMyAKUSAxMzU2IDMxMDMgMTE0MiAyOTcyIApRIDkyOCAyODQxIDkyOCAyNTc4IApRIDkyOCAyMzc4IDEwODEgMjI2NCAKUSAxMjM0IDIxNTAgMTY5NyAyMDQ3IApMIDE4OTQgMjAwMyAKUSAyNTA2IDE4NzIgMjc2NCAxNjMzIApRIDMwMjIgMTM5NCAzMDIyIDk2NiAKUSAzMDIyIDQ3OCAyNjM2IDE5MyAKUSAyMjUwIC05MSAxNTc1IC05MSAKUSAxMjk0IC05MSA5ODkgLTM2IApRIDY4NCAxOSAzNDcgMTI4IApMIDM0NyA3MjIgClEgNjY2IDU1NiA5NzUgNDczIApRIDEyODQgMzkxIDE1ODggMzkxIApRIDE5OTQgMzkxIDIyMTIgNTMwIApRIDI0MzEgNjY5IDI0MzEgOTIyIApRIDI0MzEgMTE1NiAyMjczIDEyODEgClEgMjExNiAxNDA2IDE1ODEgMTUyMiAKTCAxMzgxIDE1NjkgClEgODQ3IDE2ODEgNjA5IDE5MTQgClEgMzcyIDIxNDcgMzcyIDI1NTMgClEgMzcyIDMwNDcgNzIyIDMzMTUgClEgMTA3MiAzNTg0IDE3MTYgMzU4NCAKUSAyMDM0IDM1ODQgMjMxNSAzNTM3IApRIDI1OTcgMzQ5MSAyODM0IDMzOTcgCnoKIiBpZD0iRGVqYVZ1U2Fucy03MyIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNDYiLz4KICAgICAgIDx1c2UgeD0iNDguMzk0NTMxIiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02MSIvPgogICAgICAgPHVzZSB4PSIxMDkuNjczODI4IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02ZSIvPgogICAgICAgPHVzZSB4PSIxNzMuMDUyNzM0IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03NCIvPgogICAgICAgPHVzZSB4PSIyMTIuMjYxNzE5IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02MSIvPgogICAgICAgPHVzZSB4PSIyNzMuNTQxMDE2IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03MyIvPgogICAgICAgPHVzZSB4PSIzMjUuNjQwNjI1IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy03OSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgPC9nPgogICAgPGcgaWQ9Inh0aWNrXzgiPgogICAgIDxnIGlkPSJsaW5lMmRfOCI+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjQ2Ni42OTM3NSIgeGxpbms6aHJlZj0iI201OGY0MzU4MDRiIiB5PSIzMjAuMTE4NzUiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgICA8ZyBpZD0idGV4dF84Ij4KICAgICAgPCEtLSBTY2llbmNlIEZpY3Rpb24gLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ2OS40NTMxMjUgNDAxLjUyMTg3NSlyb3RhdGUoLTkwKXNjYWxlKDAuMSAtMC4xKSI+CiAgICAgICA8ZGVmcz4KICAgICAgICA8cGF0aCBkPSJNIDM0MjUgNDUxMyAKTCAzNDI1IDM4OTcgClEgMzA2NiA0MDY5IDI3NDcgNDE1MyAKUSAyNDI4IDQyMzggMjEzMSA0MjM4IApRIDE2MTYgNDIzOCAxMzM2IDQwMzggClEgMTA1NiAzODM4IDEwNTYgMzQ2OSAKUSAxMDU2IDMxNTkgMTI0MiAzMDAxIApRIDE0MjggMjg0NCAxOTQ3IDI3NDcgCkwgMjMyOCAyNjY5IApRIDMwMzQgMjUzNCAzMzcwIDIxOTUgClEgMzcwNiAxODU2IDM3MDYgMTI4OCAKUSAzNzA2IDYwOSAzMjUxIDI1OSAKUSAyNzk3IC05MSAxOTE5IC05MSAKUSAxNTg4IC05MSAxMjE0IC0xNiAKUSA4NDEgNTkgNDQxIDIwNiAKTCA0NDEgODU2IApRIDgyNSA2NDEgMTE5NCA1MzEgClEgMTU2MyA0MjIgMTkxOSA0MjIgClEgMjQ1OSA0MjIgMjc1MyA2MzQgClEgMzA0NyA4NDcgMzA0NyAxMjQxIApRIDMwNDcgMTU4NCAyODM2IDE3NzggClEgMjYyNSAxOTcyIDIxNDQgMjA2OSAKTCAxNzU5IDIxNDQgClEgMTA1MyAyMjg0IDczNyAyNTg0IApRIDQyMiAyODg0IDQyMiAzNDE5IApRIDQyMiA0MDM4IDg1OCA0Mzk0IApRIDEyOTQgNDc1MCAyMDU5IDQ3NTAgClEgMjM4OCA0NzUwIDI3MjggNDY5MCAKUSAzMDY5IDQ2MzEgMzQyNSA0NTEzIAp6CiIgaWQ9IkRlamFWdVNhbnMtNTMiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICAgPHBhdGggaWQ9IkRlamFWdVNhbnMtMjAiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTUzIi8+CiAgICAgICA8dXNlIHg9IjYzLjQ3NjU2MiIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjMiLz4KICAgICAgIDx1c2UgeD0iMTE4LjQ1NzAzMSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjkiLz4KICAgICAgIDx1c2UgeD0iMTQ2LjI0MDIzNCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjUiLz4KICAgICAgIDx1c2UgeD0iMjA3Ljc2MzY3MiIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmUiLz4KICAgICAgIDx1c2UgeD0iMjcxLjE0MjU3OCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjMiLz4KICAgICAgIDx1c2UgeD0iMzI2LjEyMzA0NyIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjUiLz4KICAgICAgIDx1c2UgeD0iMzg3LjY0NjQ4NCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtMjAiLz4KICAgICAgIDx1c2UgeD0iNDE5LjQzMzU5NCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNDYiLz4KICAgICAgIDx1c2UgeD0iNDY5LjcwMzEyNSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjkiLz4KICAgICAgIDx1c2UgeD0iNDk3LjQ4NjMyOCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjMiLz4KICAgICAgIDx1c2UgeD0iNTUyLjQ2Njc5NyIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNzQiLz4KICAgICAgIDx1c2UgeD0iNTkxLjY3NTc4MSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjkiLz4KICAgICAgIDx1c2UgeD0iNjE5LjQ1ODk4NCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmYiLz4KICAgICAgIDx1c2UgeD0iNjgwLjY0MDYyNSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNmUiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgIDwvZz4KICAgIDxnIGlkPSJ4dGlja185Ij4KICAgICA8ZyBpZD0ibGluZTJkXzkiPgogICAgICA8Zz4KICAgICAgIDx1c2Ugc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjg7IiB4PSI1MjUuNjk3OTE3IiB4bGluazpocmVmPSIjbTU4ZjQzNTgwNGIiIHk9IjMyMC4xMTg3NSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzkiPgogICAgICA8IS0tIFRocmlsbGVyIC0tPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg1MjguNDU3MjkyIDM2Mi4yNzM0Mzgpcm90YXRlKC05MClzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSAtMTkgNDY2NiAKTCAzOTI4IDQ2NjYgCkwgMzkyOCA0MTM0IApMIDIyNzIgNDEzNCAKTCAyMjcyIDAgCkwgMTYzOCAwIApMIDE2MzggNDEzNCAKTCAtMTkgNDEzNCAKTCAtMTkgNDY2NiAKegoiIGlkPSJEZWphVnVTYW5zLTU0IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgIDxwYXRoIGQ9Ik0gMzUxMyAyMTEzIApMIDM1MTMgMCAKTCAyOTM4IDAgCkwgMjkzOCAyMDk0IApRIDI5MzggMjU5MSAyNzQ0IDI4MzcgClEgMjU1MCAzMDg0IDIxNjMgMzA4NCAKUSAxNjk3IDMwODQgMTQyOCAyNzg3IApRIDExNTkgMjQ5MSAxMTU5IDE5NzggCkwgMTE1OSAwIApMIDU4MSAwIApMIDU4MSA0ODYzIApMIDExNTkgNDg2MyAKTCAxMTU5IDI5NTYgClEgMTM2NiAzMjcyIDE2NDUgMzQyOCAKUSAxOTI1IDM1ODQgMjI5MSAzNTg0IApRIDI4OTQgMzU4NCAzMjAzIDMyMTEgClEgMzUxMyAyODM4IDM1MTMgMjExMyAKegoiIGlkPSJEZWphVnVTYW5zLTY4IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgPC9kZWZzPgogICAgICAgPHVzZSB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy01NCIvPgogICAgICAgPHVzZSB4PSI2MS4wODM5ODQiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTY4Ii8+CiAgICAgICA8dXNlIHg9IjEyNC40NjI4OTEiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTcyIi8+CiAgICAgICA8dXNlIHg9IjE2NS41NzYxNzIiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTY5Ii8+CiAgICAgICA8dXNlIHg9IjE5My4zNTkzNzUiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTZjIi8+CiAgICAgICA8dXNlIHg9IjIyMS4xNDI1NzgiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTZjIi8+CiAgICAgICA8dXNlIHg9IjI0OC45MjU3ODEiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTY1Ii8+CiAgICAgICA8dXNlIHg9IjMxMC40NDkyMTkiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTcyIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyBpZD0idGV4dF8xMCI+CiAgICAgPCEtLSBnZW5yZSAtLT4KICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNzUuMjQyMTg4IDQxMy4xMjAzMTMpc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgPGRlZnM+CiAgICAgICA8cGF0aCBkPSJNIDI5MDYgMTc5MSAKUSAyOTA2IDI0MTYgMjY0OCAyNzU5IApRIDIzOTEgMzEwMyAxOTI1IDMxMDMgClEgMTQ2MyAzMTAzIDEyMDUgMjc1OSAKUSA5NDcgMjQxNiA5NDcgMTc5MSAKUSA5NDcgMTE2OSAxMjA1IDgyNSAKUSAxNDYzIDQ4MSAxOTI1IDQ4MSAKUSAyMzkxIDQ4MSAyNjQ4IDgyNSAKUSAyOTA2IDExNjkgMjkwNiAxNzkxIAp6Ck0gMzQ4MSA0MzQgClEgMzQ4MSAtNDU5IDMwODQgLTg5NSAKUSAyNjg4IC0xMzMxIDE4NjkgLTEzMzEgClEgMTU2NiAtMTMzMSAxMjk3IC0xMjg2IApRIDEwMjggLTEyNDEgNzc1IC0xMTQ3IApMIDc3NSAtNTg4IApRIDEwMjggLTcyNSAxMjc1IC03OTAgClEgMTUyMiAtODU2IDE3NzggLTg1NiAKUSAyMzQ0IC04NTYgMjYyNSAtNTYxIApRIDI5MDYgLTI2NiAyOTA2IDMzMSAKTCAyOTA2IDYxNiAKUSAyNzI4IDMwNiAyNDUwIDE1MyAKUSAyMTcyIDAgMTc4NCAwIApRIDExNDEgMCA3NDcgNDkwIApRIDM1MyA5ODEgMzUzIDE3OTEgClEgMzUzIDI2MDMgNzQ3IDMwOTMgClEgMTE0MSAzNTg0IDE3ODQgMzU4NCAKUSAyMTcyIDM1ODQgMjQ1MCAzNDMxIApRIDI3MjggMzI3OCAyOTA2IDI5NjkgCkwgMjkwNiAzNTAwIApMIDM0ODEgMzUwMCAKTCAzNDgxIDQzNCAKegoiIGlkPSJEZWphVnVTYW5zLTY3IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICA8L2RlZnM+CiAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjciLz4KICAgICAgPHVzZSB4PSI2My40NzY1NjIiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTY1Ii8+CiAgICAgIDx1c2UgeD0iMTI1IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02ZSIvPgogICAgICA8dXNlIHg9IjE4OC4zNzg5MDYiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTcyIi8+CiAgICAgIDx1c2UgeD0iMjI3LjI0MjE4OCIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjUiLz4KICAgICA8L2c+CiAgICA8L2c+CiAgIDwvZz4KICAgPGcgaWQ9Im1hdHBsb3RsaWIuYXhpc18yIj4KICAgIDxnIGlkPSJ5dGlja18xIj4KICAgICA8ZyBpZD0ibGluZTJkXzEwIj4KICAgICAgPGRlZnM+CiAgICAgICA8cGF0aCBkPSJNIDAgMCAKTCAtMy41IDAgCiIgaWQ9Im1hODdjODY2NjkwIiBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiLz4KICAgICAgPC9kZWZzPgogICAgICA8Zz4KICAgICAgIDx1c2Ugc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjg7IiB4PSIyNC4xNjI1IiB4bGluazpocmVmPSIjbWE4N2M4NjY2OTAiIHk9IjMyMC4xMTg3NSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzExIj4KICAgICAgPCEtLSAwIC0tPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMC44IDMyMy45MTc5Njkpc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgIDxkZWZzPgogICAgICAgIDxwYXRoIGQ9Ik0gMjAzNCA0MjUwIApRIDE1NDcgNDI1MCAxMzAxIDM3NzAgClEgMTA1NiAzMjkxIDEwNTYgMjMyOCAKUSAxMDU2IDEzNjkgMTMwMSA4ODkgClEgMTU0NyA0MDkgMjAzNCA0MDkgClEgMjUyNSA0MDkgMjc3MCA4ODkgClEgMzAxNiAxMzY5IDMwMTYgMjMyOCAKUSAzMDE2IDMyOTEgMjc3MCAzNzcwIApRIDI1MjUgNDI1MCAyMDM0IDQyNTAgCnoKTSAyMDM0IDQ3NTAgClEgMjgxOSA0NzUwIDMyMzMgNDEyOSAKUSAzNjQ3IDM1MDkgMzY0NyAyMzI4IApRIDM2NDcgMTE1MCAzMjMzIDUyOSAKUSAyODE5IC05MSAyMDM0IC05MSAKUSAxMjUwIC05MSA4MzYgNTI5IApRIDQyMiAxMTUwIDQyMiAyMzI4IApRIDQyMiAzNTA5IDgzNiA0MTI5IApRIDEyNTAgNDc1MCAyMDM0IDQ3NTAgCnoKIiBpZD0iRGVqYVZ1U2Fucy0zMCIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtMzAiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgIDwvZz4KICAgIDxnIGlkPSJ5dGlja18yIj4KICAgICA8ZyBpZD0ibGluZTJkXzExIj4KICAgICAgPGc+CiAgICAgICA8dXNlIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIgeD0iMjQuMTYyNSIgeGxpbms6aHJlZj0iI21hODdjODY2NjkwIiB5PSIyNTQuNjU0NDY0Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICAgPGcgaWQ9InRleHRfMTIiPgogICAgICA8IS0tIDIgLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwLjggMjU4LjQ1MzY4MylzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSAxMjI4IDUzMSAKTCAzNDMxIDUzMSAKTCAzNDMxIDAgCkwgNDY5IDAgCkwgNDY5IDUzMSAKUSA4MjggOTAzIDE0NDggMTUyOSAKUSAyMDY5IDIxNTYgMjIyOCAyMzM4IApRIDI1MzEgMjY3OCAyNjUxIDI5MTQgClEgMjc3MiAzMTUwIDI3NzIgMzM3OCAKUSAyNzcyIDM3NTAgMjUxMSAzOTg0IApRIDIyNTAgNDIxOSAxODMxIDQyMTkgClEgMTUzNCA0MjE5IDEyMDQgNDExNiAKUSA4NzUgNDAxMyA1MDAgMzgwMyAKTCA1MDAgNDQ0MSAKUSA4ODEgNDU5NCAxMjEyIDQ2NzIgClEgMTU0NCA0NzUwIDE4MTkgNDc1MCAKUSAyNTQ0IDQ3NTAgMjk3NSA0Mzg3IApRIDM0MDYgNDAyNSAzNDA2IDM0MTkgClEgMzQwNiAzMTMxIDMyOTggMjg3MyAKUSAzMTkxIDI2MTYgMjkwNiAyMjY2IApRIDI4MjggMjE3NSAyNDA5IDE3NDIgClEgMTk5MSAxMzA5IDEyMjggNTMxIAp6CiIgaWQ9IkRlamFWdVNhbnMtMzIiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTMyIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyBpZD0ieXRpY2tfMyI+CiAgICAgPGcgaWQ9ImxpbmUyZF8xMiI+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjI0LjE2MjUiIHhsaW5rOmhyZWY9IiNtYTg3Yzg2NjY5MCIgeT0iMTg5LjE5MDE3OSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzEzIj4KICAgICAgPCEtLSA0IC0tPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMC44IDE5Mi45ODkzOTcpc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgIDxkZWZzPgogICAgICAgIDxwYXRoIGQ9Ik0gMjQxOSA0MTE2IApMIDgyNSAxNjI1IApMIDI0MTkgMTYyNSAKTCAyNDE5IDQxMTYgCnoKTSAyMjUzIDQ2NjYgCkwgMzA0NyA0NjY2IApMIDMwNDcgMTYyNSAKTCAzNzEzIDE2MjUgCkwgMzcxMyAxMTAwIApMIDMwNDcgMTEwMCAKTCAzMDQ3IDAgCkwgMjQxOSAwIApMIDI0MTkgMTEwMCAKTCAzMTMgMTEwMCAKTCAzMTMgMTcwOSAKTCAyMjUzIDQ2NjYgCnoKIiBpZD0iRGVqYVZ1U2Fucy0zNCIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtMzQiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgIDwvZz4KICAgIDxnIGlkPSJ5dGlja180Ij4KICAgICA8ZyBpZD0ibGluZTJkXzEzIj4KICAgICAgPGc+CiAgICAgICA8dXNlIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIgeD0iMjQuMTYyNSIgeGxpbms6aHJlZj0iI21hODdjODY2NjkwIiB5PSIxMjMuNzI1ODkzIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICAgPGcgaWQ9InRleHRfMTQiPgogICAgICA8IS0tIDYgLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwLjggMTI3LjUyNTExMilzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSAyMTEzIDI1ODQgClEgMTY4OCAyNTg0IDE0MzkgMjI5MyAKUSAxMTkxIDIwMDMgMTE5MSAxNDk3IApRIDExOTEgOTk0IDE0MzkgNzAxIApRIDE2ODggNDA5IDIxMTMgNDA5IApRIDI1MzggNDA5IDI3ODYgNzAxIApRIDMwMzQgOTk0IDMwMzQgMTQ5NyAKUSAzMDM0IDIwMDMgMjc4NiAyMjkzIApRIDI1MzggMjU4NCAyMTEzIDI1ODQgCnoKTSAzMzY2IDQ1NjMgCkwgMzM2NiAzOTg4IApRIDMxMjggNDEwMCAyODg2IDQxNTkgClEgMjY0NCA0MjE5IDI0MDYgNDIxOSAKUSAxNzgxIDQyMTkgMTQ1MSAzNzk3IApRIDExMjIgMzM3NSAxMDc1IDI1MjIgClEgMTI1OSAyNzk0IDE1MzcgMjkzOSAKUSAxODE2IDMwODQgMjE1MCAzMDg0IApRIDI4NTMgMzA4NCAzMjYxIDI2NTcgClEgMzY2OSAyMjMxIDM2NjkgMTQ5NyAKUSAzNjY5IDc3OCAzMjQ0IDM0MyAKUSAyODE5IC05MSAyMTEzIC05MSAKUSAxMzAzIC05MSA4NzUgNTI5IApRIDQ0NyAxMTUwIDQ0NyAyMzI4IApRIDQ0NyAzNDM0IDk3MiA0MDkyIApRIDE0OTcgNDc1MCAyMzgxIDQ3NTAgClEgMjYxOSA0NzUwIDI4NjEgNDcwMyAKUSAzMTAzIDQ2NTYgMzM2NiA0NTYzIAp6CiIgaWQ9IkRlamFWdVNhbnMtMzYiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTM2Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyBpZD0ieXRpY2tfNSI+CiAgICAgPGcgaWQ9ImxpbmUyZF8xNCI+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjI0LjE2MjUiIHhsaW5rOmhyZWY9IiNtYTg3Yzg2NjY5MCIgeT0iNTguMjYxNjA3Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICAgPGcgaWQ9InRleHRfMTUiPgogICAgICA8IS0tIDggLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwLjggNjIuMDYwODI2KXNjYWxlKDAuMSAtMC4xKSI+CiAgICAgICA8ZGVmcz4KICAgICAgICA8cGF0aCBkPSJNIDIwMzQgMjIxNiAKUSAxNTg0IDIyMTYgMTMyNiAxOTc1IApRIDEwNjkgMTczNCAxMDY5IDEzMTMgClEgMTA2OSA4OTEgMTMyNiA2NTAgClEgMTU4NCA0MDkgMjAzNCA0MDkgClEgMjQ4NCA0MDkgMjc0MyA2NTEgClEgMzAwMyA4OTQgMzAwMyAxMzEzIApRIDMwMDMgMTczNCAyNzQ1IDE5NzUgClEgMjQ4OCAyMjE2IDIwMzQgMjIxNiAKegpNIDE0MDMgMjQ4NCAKUSA5OTcgMjU4NCA3NzAgMjg2MiAKUSA1NDQgMzE0MSA1NDQgMzU0MSAKUSA1NDQgNDEwMCA5NDIgNDQyNSAKUSAxMzQxIDQ3NTAgMjAzNCA0NzUwIApRIDI3MzEgNDc1MCAzMTI4IDQ0MjUgClEgMzUyNSA0MTAwIDM1MjUgMzU0MSAKUSAzNTI1IDMxNDEgMzI5OCAyODYyIApRIDMwNzIgMjU4NCAyNjY5IDI0ODQgClEgMzEyNSAyMzc4IDMzNzkgMjA2OCAKUSAzNjM0IDE3NTkgMzYzNCAxMzEzIApRIDM2MzQgNjM0IDMyMjAgMjcxIApRIDI4MDYgLTkxIDIwMzQgLTkxIApRIDEyNjMgLTkxIDg0OCAyNzEgClEgNDM0IDYzNCA0MzQgMTMxMyAKUSA0MzQgMTc1OSA2OTAgMjA2OCAKUSA5NDcgMjM3OCAxNDAzIDI0ODQgCnoKTSAxMTcyIDM0ODEgClEgMTE3MiAzMTE5IDEzOTggMjkxNiAKUSAxNjI1IDI3MTMgMjAzNCAyNzEzIApRIDI0NDEgMjcxMyAyNjcwIDI5MTYgClEgMjkwMCAzMTE5IDI5MDAgMzQ4MSAKUSAyOTAwIDM4NDQgMjY3MCA0MDQ3IApRIDI0NDEgNDI1MCAyMDM0IDQyNTAgClEgMTYyNSA0MjUwIDEzOTggNDA0NyAKUSAxMTcyIDM4NDQgMTE3MiAzNDgxIAp6CiIgaWQ9IkRlamFWdVNhbnMtMzgiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTM4Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgIDwvZz4KICAgPGcgaWQ9InBhdGNoXzEyIj4KICAgIDxwYXRoIGQ9Ik0gMjQuMTYyNSAzMjAuMTE4NzUgCkwgMjQuMTYyNSAxMC44IAoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLWxpbmVjYXA6c3F1YXJlO3N0cm9rZS1saW5lam9pbjptaXRlcjtzdHJva2Utd2lkdGg6MC44OyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF8xMyI+CiAgICA8cGF0aCBkPSJNIDU1NS4yIDMyMC4xMTg3NSAKTCA1NTUuMiAxMC44IAoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLWxpbmVjYXA6c3F1YXJlO3N0cm9rZS1saW5lam9pbjptaXRlcjtzdHJva2Utd2lkdGg6MC44OyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF8xNCI+CiAgICA8cGF0aCBkPSJNIDI0LjE2MjUgMzIwLjExODc1IApMIDU1NS4yIDMyMC4xMTg3NSAKIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZTojMDAwMDAwO3N0cm9rZS1saW5lY2FwOnNxdWFyZTtzdHJva2UtbGluZWpvaW46bWl0ZXI7c3Ryb2tlLXdpZHRoOjAuODsiLz4KICAgPC9nPgogICA8ZyBpZD0icGF0Y2hfMTUiPgogICAgPHBhdGggZD0iTSAyNC4xNjI1IDEwLjggCkwgNTU1LjIgMTAuOCAKIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZTojMDAwMDAwO3N0cm9rZS1saW5lY2FwOnNxdWFyZTtzdHJva2UtbGluZWpvaW46bWl0ZXI7c3Ryb2tlLXdpZHRoOjAuODsiLz4KICAgPC9nPgogICA8ZyBpZD0ibGVnZW5kXzEiPgogICAgPGcgaWQ9InBhdGNoXzE2Ij4KICAgICA8cGF0aCBkPSJNIDUwNy4wNzM0MzcgMzMuNDc4MTI1IApMIDU0OC4yIDMzLjQ3ODEyNSAKUSA1NTAuMiAzMy40NzgxMjUgNTUwLjIgMzEuNDc4MTI1IApMIDU1MC4yIDE3LjggClEgNTUwLjIgMTUuOCA1NDguMiAxNS44IApMIDUwNy4wNzM0MzcgMTUuOCAKUSA1MDUuMDczNDM3IDE1LjggNTA1LjA3MzQzNyAxNy44IApMIDUwNS4wNzM0MzcgMzEuNDc4MTI1IApRIDUwNS4wNzM0MzcgMzMuNDc4MTI1IDUwNy4wNzM0MzcgMzMuNDc4MTI1IAp6CiIgc3R5bGU9ImZpbGw6I2ZmZmZmZjtvcGFjaXR5OjAuODtzdHJva2U6I2NjY2NjYztzdHJva2UtbGluZWpvaW46bWl0ZXI7Ii8+CiAgICA8L2c+CiAgICA8ZyBpZD0icGF0Y2hfMTciPgogICAgIDxwYXRoIGQ9Ik0gNTA5LjA3MzQzNyAyNy4zOTg0MzggCkwgNTI5LjA3MzQzNyAyNy4zOTg0MzggCkwgNTI5LjA3MzQzNyAyMC4zOTg0MzggCkwgNTA5LjA3MzQzNyAyMC4zOTg0MzggCnoKIiBzdHlsZT0iZmlsbDojMWY3N2I0OyIvPgogICAgPC9nPgogICAgPGcgaWQ9InRleHRfMTYiPgogICAgIDwhLS0gaWQgLS0+CiAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNTM3LjA3MzQzNyAyNy4zOTg0Mzgpc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgPHVzZSB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02OSIvPgogICAgICA8dXNlIHg9IjI3Ljc4MzIwMyIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNjQiLz4KICAgICA8L2c+CiAgICA8L2c+CiAgIDwvZz4KICA8L2c+CiA8L2c+CiA8ZGVmcz4KICA8Y2xpcFBhdGggaWQ9InA1ZDU1OGM2MzQ4Ij4KICAgPHJlY3QgaGVpZ2h0PSIzMDkuMzE4NzUiIHdpZHRoPSI1MzEuMDM3NSIgeD0iMjQuMTYyNSIgeT0iMTAuOCIvPgogIDwvY2xpcFBhdGg+CiA8L2RlZnM+Cjwvc3ZnPgo=)\n",
    "\n",
    "Nice job! The right join ensured that you were analyzing all of the pop_movies. You see from the results that adventure and action are the most popular genres.\n",
    "\n",
    "## Using outer join to select actors\n",
    "One cool aspect of using an outer join is that, because it returns all rows from both merged tables and null where they do not match, you can use it to find rows that do not have a match in the other table. To try for yourself, you have been given two tables with a list of actors from two popular movies: Iron Man 1 and Iron Man 2. Most of the actors played in both movies. Use an outer join to find actors who did not act in both movies.\n",
    "\n",
    "The Iron Man 1 table is called `iron_1_actors`, and Iron Man 2 table is called `iron_2_actors`. Both tables have been loaded for you and a few rows printed so you can see the structure.\n",
    "![](https://assets.datacamp.com/production/repositories/5486/datasets/c5d02ebba511e90ae132f89ff091e6729c040bd2/noJoin.png)\n",
    "\n",
    "* Save to `iron_1_and_2` the merge of `iron_1_actors` (left) with `iron_2_actors` tables with an outer join on the id column, and set suffixes to ('_1','_2').\n",
    "* Create an index that returns True if `name_1` or `name_2 `are null, and False otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c49024c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes\n",
    "iron_1_and_2 = iron_1_actors.merge(iron_2_actors, \n",
    "                                     on='id', \n",
    "                                     how='outer', \n",
    "                                     suffixes=('_1','_2'))\n",
    "\n",
    "# Create an index that returns true if name_1 or name_2 are null\n",
    "m = ((iron_1_and_2['name_1'].isnull()) | \n",
    "     (iron_1_and_2['name_2'].isnull()))\n",
    "\n",
    "# Print the first few rows of iron_1_and_2\n",
    "print(iron_1_and_2[m].head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "819156c3",
   "metadata": {},
   "source": [
    "Nice job! Using an outer join, you were able to pick only those rows where the actor played in only one of the two movies.\n",
    "\n",
    "## Self join\n",
    "Merging a table to itself can be useful when you want to compare values in a column to other values in the same column. In this exercise, you will practice this by creating a table that for each movie will list the movie director and a member of the crew on one row. You have been given a table called crews, which has columns id, job, and name. First, merge the table to itself using the movie ID. This merge will give you a larger table where for each movie, every job is matched against each other. Then select only those rows with a director in the left table, and avoid having a row where the director's job is listed in both the left and right tables. This filtering will remove job combinations that aren't with the director.\n",
    "\n",
    "* To a variable called `crews_self_merged`, merge the crews table to itself on the id column using an inner join, setting the suffixes to `'_dir'` and `'_crew'` for the left and right tables respectively."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "62de7d5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "crews = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/crews.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "73a86d84",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge the crews table to itself\n",
    "crews_self_merged = crews.merge(crews, on='id', how='inner',\n",
    "                                suffixes=('_dir','_crew'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "522e2044",
   "metadata": {},
   "source": [
    "* Create a Boolean index, named `boolean_filter`, that selects rows from the left table with the job of 'Director' and avoids rows with the job of 'Director' in the right table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "13f115de",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a Boolean index to select the appropriate rows\n",
    "boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & \n",
    "                  (crews_self_merged['job_crew'] != 'Director'))\n",
    "direct_crews = crews_self_merged[boolean_filter]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04ce3019",
   "metadata": {},
   "source": [
    "* Use the `.head()` method to print the first few rows of `direct_crews`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "dbbdc420",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        id department_dir   job_dir       name_dir department_crew  \\\n",
      "156  19995      Directing  Director  James Cameron         Editing   \n",
      "157  19995      Directing  Director  James Cameron           Sound   \n",
      "158  19995      Directing  Director  James Cameron      Production   \n",
      "160  19995      Directing  Director  James Cameron         Writing   \n",
      "161  19995      Directing  Director  James Cameron             Art   \n",
      "\n",
      "           job_crew          name_crew  \n",
      "156          Editor  Stephen E. Rivkin  \n",
      "157  Sound Designer  Christopher Boyes  \n",
      "158         Casting          Mali Finn  \n",
      "160          Writer      James Cameron  \n",
      "161    Set Designer    Richard F. Mays  \n"
     ]
    }
   ],
   "source": [
    "# Print the first few rows of direct_crews\n",
    "print(direct_crews.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9947c4e",
   "metadata": {},
   "source": [
    "Great job! By merging the table to itself, you compared the value of the director from the jobs column to other values from the jobs column. With the output, you can quickly see different movie directors and the people they worked with in the same movie.\n",
    "\n",
    "## How does pandas handle self joins?\n",
    "Select the false statement about merging a table to itself.\n",
    "\n",
    "\n",
    "* You can merge a table to itself with a right join.\n",
    "\n",
    "* Merging a table to itself can allow you to compare values in a column to other values in the same column.\n",
    "\n",
    "* **The pandas module limits you to one merge where you merge a table to itself. You cannot repeat this process over and over.**\n",
    "\n",
    "* Merging a table to itself is like working with two separate tables.\n",
    "\n",
    "Perfect! This statement is false. pandas treats a merge of a table to itself the same as any other merge. Therefore, it does not limit you from chaining multiple `.merge()` methods together.\n",
    "\n",
    "## Index merge for movie ratings\n",
    "To practice merging on indexes, you will merge movies and a table called ratings that holds info about movie ratings. Make sure your merge returns all of the rows from the movies table and not all the rows of ratings table need to be included in the result.\n",
    "\n",
    "* Merge `movies` and `ratings` on the index and save to a variable called `movies_ratings`, ensuring that all of the rows from the movies table are returned."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "c7c64405",
   "metadata": {},
   "outputs": [],
   "source": [
    "ratings = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/ratings.p')\n",
    "movies = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/movies.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "3fc88cae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      id                 title  popularity release_date  vote_average  \\\n",
      "0    257          Oliver Twist   20.415572   2005-09-23           6.7   \n",
      "1  14290  Better Luck Tomorrow    3.877036   2002-01-12           6.5   \n",
      "2  38365             Grown Ups   38.864027   2010-06-24           6.0   \n",
      "3   9672              Infamous    3.680896   2006-11-16           6.4   \n",
      "4  12819       Alpha and Omega   12.300789   2010-09-17           5.3   \n",
      "\n",
      "   vote_count  \n",
      "0       274.0  \n",
      "1        27.0  \n",
      "2      1705.0  \n",
      "3        60.0  \n",
      "4       124.0  \n"
     ]
    }
   ],
   "source": [
    "# Merge to the movies table the ratings table on the index\n",
    "movies_ratings = movies.merge(ratings, on='id', how='left')\n",
    "\n",
    "# Print the first few rows of movies_ratings\n",
    "print(movies_ratings.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a03b34f",
   "metadata": {},
   "source": [
    "Good work! Merging on indexes is just like merging on columns, so if you need to merge based on indexes, there's no need to turn the indexes into columns first.\n",
    "\n",
    "## Do sequels earn more?\n",
    "It is time to put together many of the aspects that you have learned in this chapter. In this exercise, you'll find out which movie sequels earned the most compared to the original movie. To answer this question, you will merge a modified version of the sequels and financials tables where their index is the movie ID. You will need to choose a merge type that will return all of the rows from the sequels table and not all the rows of financials table need to be included in the result. From there, you will join the resulting table to itself so that you can compare the revenue values of the original movie to the sequel. Next, you will calculate the difference between the two revenues and sort the resulting dataset.\n",
    "\n",
    "* With the `sequels` table on the left, merge to it the `financials` table on index named id, ensuring that all the rows from the sequels are returned and some rows from the other table may not be returned, Save the results to `sequels_fin`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "0cad8f8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "sequels = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/sequels.p')\n",
    "financials = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/financials.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "5e614a35",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge sequels and financials on index id\n",
    "sequels_fin = sequels.merge(financials, on='id', how='left')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e9e2640",
   "metadata": {},
   "source": [
    "* Merge the `sequels_fin` table to itself with an inner join, where the left and right tables merge on sequel and id respectively with suffixes equal to (`'_org','_seq'`), saving to `orig_seq`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "66c489ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "sequels_fin = sequels_fin.fillna(0)\n",
    "\n",
    "# Self merge with suffixes as inner join with left on sequel and right on id\n",
    "orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', \n",
    "                             right_on='id', right_index=True,\n",
    "                             suffixes=('_org','_seq'))\n",
    "\n",
    "# Add calculation to subtract revenue_org from revenue_seq \n",
    "orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ecb70daf",
   "metadata": {},
   "source": [
    "* Select the `title_org`, `title_seq`, and diff columns of `orig_seq` and save this as `titles_diff`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "8b3d5748",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Select the title_org, title_seq, and diff \n",
    "titles_diff = orig_seq[['title_org','title_seq','diff']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6817c16",
   "metadata": {},
   "source": [
    "* Sort by `titles_diff` by diff in descending order and print the first few rows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "70ca2bef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                title_org title_seq          diff\n",
      "3612        Class of 1984    Avatar  2.787965e+09\n",
      "3754        Extreme Movie    Avatar  2.787965e+09\n",
      "3756  Eye of the Beholder    Avatar  2.787965e+09\n",
      "3757               Fabled    Avatar  2.787965e+09\n",
      "3758         Factory Girl    Avatar  2.787965e+09\n"
     ]
    }
   ],
   "source": [
    "# Print the first rows of the sorted titles_diff\n",
    "print(titles_diff.sort_values('diff', ascending=False).head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d98838e5",
   "metadata": {},
   "source": [
    "Amazing, that was great work! To complete this exercise, you needed to merge tables on their index and merge another table to itself. After the calculations were added and sub-select specific columns, the data was sorted. You found out that Jurassic World had one of the highest of all, improvement in revenue compared to the original movie."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
