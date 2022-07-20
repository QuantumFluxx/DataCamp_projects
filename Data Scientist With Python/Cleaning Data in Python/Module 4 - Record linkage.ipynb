{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bd8afe5c",
   "metadata": {},
   "source": [
    "# Record linkage\n",
    "\n",
    "## Minimum edit distance\n",
    "In the video exercise, you saw how minimum edit distance is used to identify how similar two strings are. As a reminder, minimum edit distance is the minimum number of steps needed to reach from String A to String B, with the operations available being:\n",
    "\n",
    "* Insertion of a new character.\n",
    "* Deletion of an existing character.\n",
    "* Substitution of an existing character.\n",
    "* Transposition of two existing consecutive characters.\n",
    "\n",
    "What is the minimum edit distance from 'sign' to 'sing', and which operation(s) gets you there?\n",
    "\n",
    "\n",
    "* 2 by substituting 'g' with 'n' and 'n' with 'g'.\n",
    "\n",
    "* **1 by transposing 'g' with 'n'.**\n",
    "\n",
    "* 1 by substituting 'g' with 'n'.\n",
    "\n",
    "* 2 by deleting 'g' and inserting a new 'g' at the end.\n",
    "\n",
    "Correct! Transposing the last two letters of 'sign' is the easiest way to get to 'sing' - in the next exercise, you'll use edit distance at scale to remap categories!\n",
    "\n",
    "## The cutoff point\n",
    "In this exercise, and throughout this chapter, you'll be working with the restaurants DataFrame which has data on various restaurants. Your ultimate goal is to create a restaurant recommendation engine, but you need to first clean your data.\n",
    "\n",
    "This version of restaurants has been collected from many sources, where the `cuisine_type` column is riddled with typos, and should contain only italian, american and asian cuisine types. There are so many unique categories that remapping them manually isn't scalable, and it's best to use string similarity instead.\n",
    "\n",
    "Before doing so, you want to establish the cutoff point for the similarity score using the fuzzywuzzy's `process.extract()` function by finding the similarity score of the most distant typo of each category.\n",
    "\n",
    "* Import `process` from `fuzzywuzzy`.\n",
    "* Store the unique `cuisine_types` into `unique_types`.\n",
    "* Calculate the similarity of 'asian', 'american', and 'italian' to all possible cuisine_types using `process.extract()`, while returning all possible matches."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c60ae34a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('asian', 100), ('indonesian', 72), ('italian', 67), ('russian', 67), ('american', 62), ('californian', 54), ('japanese', 54), ('mexican/tex-mex', 54), ('american ( new )', 54), ('mexican', 50), ('cajun/creole', 36), ('middle eastern', 36), ('vietnamese', 36), ('pacific new wave', 36), ('fast food', 36), ('chicken', 33), ('hamburgers', 27), ('hot dogs', 26), ('coffeebar', 26), ('continental', 26), ('steakhouses', 25), ('southern/soul', 22), ('delis', 20), ('eclectic', 20), ('pizza', 20), ('health food', 19), ('diners', 18), ('coffee shops', 18), ('noodle shops', 18), ('french ( new )', 18), ('desserts', 18), ('seafood', 17), ('chinese', 17)]\n",
      "[('american', 100), ('american ( new )', 90), ('mexican', 80), ('mexican/tex-mex', 68), ('asian', 62), ('italian', 53), ('russian', 53), ('middle eastern', 51), ('pacific new wave', 45), ('hamburgers', 44), ('indonesian', 44), ('chicken', 40), ('southern/soul', 39), ('japanese', 38), ('eclectic', 38), ('delis', 36), ('pizza', 36), ('cajun/creole', 34), ('french ( new )', 34), ('vietnamese', 33), ('californian', 32), ('diners', 29), ('desserts', 25), ('coffeebar', 24), ('steakhouses', 21), ('seafood', 13), ('chinese', 13), ('fast food', 12), ('coffee shops', 11), ('noodle shops', 11), ('health food', 11), ('continental', 11), ('hot dogs', 0)]\n",
      "[('italian', 100), ('asian', 67), ('californian', 56), ('continental', 51), ('indonesian', 47), ('russian', 43), ('mexican', 43), ('american', 40), ('japanese', 40), ('mexican/tex-mex', 39), ('american ( new )', 39), ('pacific new wave', 39), ('vietnamese', 35), ('delis', 33), ('pizza', 33), ('diners', 31), ('middle eastern', 30), ('chicken', 29), ('chinese', 29), ('health food', 27), ('southern/soul', 27), ('cajun/creole', 26), ('steakhouses', 26), ('seafood', 14), ('hot dogs', 13), ('noodle shops', 13), ('eclectic', 13), ('french ( new )', 13), ('desserts', 13), ('hamburgers', 12), ('fast food', 12), ('coffeebar', 12), ('coffee shops', 0)]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "restaurants = pd.read_csv('datasets/restaurants_L2_dirty.csv')\n",
    "\n",
    "# Import process from fuzzywuzzy\n",
    "from fuzzywuzzy import process\n",
    "\n",
    "# Store the unique values of cuisine_type in unique_types\n",
    "unique_types = restaurants['type'].unique()\n",
    "\n",
    "# Calculate similarity of 'asian' to all values of unique_types\n",
    "print(process.extract('asian', unique_types, limit = len(unique_types)))\n",
    "\n",
    "# Calculate similarity of 'american' to all values of unique_types\n",
    "print(process.extract('american', unique_types, limit = len(unique_types)))\n",
    "\n",
    "# Calculate similarity of 'italian' to all values of unique_types\n",
    "print(process.extract('italian', unique_types, limit = len(unique_types)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "626c57f2",
   "metadata": {},
   "source": [
    "Take a look at the output, what do you think should be the similarity cutoff point when remapping categories?\n",
    "\n",
    "* **80**\n",
    "\n",
    "* 70\n",
    "\n",
    "* 60\n",
    "\n",
    "Correct! 80 is that sweet spot where you convert all incorrect typos without remapping incorrect categories. Often times though, you may need to combine the techniques learned in chapter 2, especially since there could be strings that make it beyond our cutoff point, but are not actually a match!\n",
    "\n",
    "## Remapping categories II\n",
    "In the last exercise, you determined that the distance cutoff point for remapping typos of 'american', 'asian', and 'italian' cuisine types stored in the cuisine_type column should be 80.\n",
    "\n",
    "In this exercise, you're going to put it all together by finding matches with similarity scores equal to or higher than 80 by using `fuzywuzzy.process's extract()` function, for each correct cuisine type, and replacing these matches with it. Remember, when comparing a string with an array of strings using `process.extract()`, the output is a list of tuples where each is formatted like:\n",
    "```\n",
    "(closest match, similarity score, index of match)\n",
    "```\n",
    "The restaurants DataFrame is in your environment, and you have access to a categories list containing the correct cuisine types ('italian', 'asian', and 'american').\n",
    "\n",
    "* Return all of the unique values in the `cuisine_type` column of restaurants\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b93293a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['american' 'californian' 'japanese' 'cajun/creole' 'hot dogs' 'diners'\n",
      " 'delis' 'hamburgers' 'seafood' 'italian' 'coffee shops' 'russian'\n",
      " 'steakhouses' 'mexican/tex-mex' 'noodle shops' 'mexican' 'middle eastern'\n",
      " 'asian' 'vietnamese' 'health food' 'american ( new )' 'pacific new wave'\n",
      " 'indonesian' 'eclectic' 'chicken' 'fast food' 'southern/soul' 'coffeebar'\n",
      " 'continental' 'french ( new )' 'desserts' 'chinese' 'pizza']\n"
     ]
    }
   ],
   "source": [
    "# Inspect the unique values of the cuisine_type column\n",
    "print(restaurants['type'].unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c4e22d3",
   "metadata": {},
   "source": [
    "Okay! Looks like you will need to use some string matching to correct these misspellings!\n",
    "\n",
    "* As a first step, create a list of all possible matches, comparing 'italian' with the restaurant types listed in the `cuisine_type` column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "696702ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('italian', 100, 14), ('italian', 100, 21), ('italian', 100, 47), ('italian', 100, 57), ('italian', 100, 73)]\n"
     ]
    }
   ],
   "source": [
    "# Create a list of matches, comparing 'italian' with the cuisine_type column\n",
    "matches = process.extract('italian', restaurants['type'], limit=len(restaurants.type))\n",
    "\n",
    "# Inspect the first 5 matches\n",
    "print(matches[0:5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c41923ed",
   "metadata": {},
   "source": [
    "Now you're getting somewhere! Now you can iterate through matches to reassign similar entries.\n",
    "\n",
    "* Within the for loop, use an if statement to check whether the similarity score in each match is greater than or equal to 80.\n",
    "* If it is, use `.loc` to select rows where `cuisine_type` in restaurants is equal to the current match (which is the first element of match), and reassign them to be 'italian'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b9d14f0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Iterate through the list of matches to italian\n",
    "for match in matches:\n",
    "  # Check whether the similarity score is greater than or equal to 80\n",
    "  if match[1] >= 80:\n",
    "    # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine\n",
    "    restaurants.loc[restaurants['type'] == match[0]] = 'italian'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52923cd9",
   "metadata": {},
   "source": [
    "Finally, you'll adapt your code to work with every restaurant type in categories.\n",
    "\n",
    "* Using the variable cuisine to iterate through categories, embed your code from the previous step in an outer for loop.\n",
    "* Inspect the final result. This has been done for you."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaa09da8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Iterate through categories\n",
    "for cuisine in categories:  \n",
    "  # Create a list of matches, comparing cuisine with the cuisine_type column\n",
    "  matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))\n",
    "\n",
    "  # Iterate through the list of matches\n",
    "  for match in matches:\n",
    "     # Check whether the similarity score is greater than or equal to 80\n",
    "    if match[1] >= 80:\n",
    "      # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine\n",
    "      restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine\n",
    "      \n",
    "# Inspect the final result\n",
    "print(restaurants['cuisine_type'].unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29c738e6",
   "metadata": {},
   "source": [
    "Tremendous work! All your cuisine types are properly mapped! Now you'll build on string similarity, by jumping into record linkage!\n",
    "\n",
    "## Pairs of restaurants\n",
    "In the last lesson, you cleaned the restaurants dataset to make it ready for building a restaurants recommendation engine. You have a new DataFrame named `restaurants_new` with new restaurants to train your model on, that's been scraped from a new data source.\n",
    "\n",
    "You've already cleaned the `cuisine_type` and city columns using the techniques learned throughout the course. However you saw duplicates with typos in restaurants names that require record linkage instead of joins with restaurants.\n",
    "\n",
    "In this exercise, you will perform the first step in record linkage and generate possible pairs of rows between restaurants and restaurants_new. Both DataFrames, pandas and recordlinkage are in your environment.\n",
    "\n",
    "* Instantiate an indexing object by using the `Index()` function from recordlinkage.\n",
    "* Block your pairing on cuisine_type by using indexer's' `.block()` method.\n",
    "* Generate pairs by indexing restaurants and `restaurants_new` in that order."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "fa7c909c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import recordlinkage\n",
    "\n",
    "restaurants_new = pd.read_csv('datasets/restaurants_L2.csv')\n",
    "\n",
    "# Create an indexer and object and find possible pairs\n",
    "indexer = recordlinkage.Index()\n",
    "\n",
    "# Block pairing on cuisine_type\n",
    "indexer.block('type')\n",
    "\n",
    "# Generate pairs\n",
    "pairs = indexer.index(restaurants, restaurants_new)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c331ec24",
   "metadata": {},
   "source": [
    "Now that you've generated your pairs, you've achieved the first step of record linkage. What are the steps remaining to link both restaurants DataFrames, and in what order?\n",
    "\n",
    "* **Compare between columns, score the comparison, then link the DataFrames.**\n",
    "\n",
    "* Clean the data, compare between columns, link the DataFrames, then score the comparison.\n",
    "\n",
    "* Clean the data, compare between columns, score the comparison, then link the DataFrames.\n",
    "\n",
    "Correct! In the next exercise, you will compare between columns and check out the matching potentially rows between both DataFrames!\n",
    "\n",
    "## Similar restaurants\n",
    "In the last exercise, you generated pairs between restaurants and restaurants_new in an effort to cleanly merge both DataFrames using record linkage.\n",
    "\n",
    "When performing record linkage, there are different types of matching you can perform between different columns of your DataFrames, including exact matches, string similarities, and more.\n",
    "\n",
    "Now that your pairs have been generated and stored in pairs, you will find exact matches in the city and `cuisine_type` columns between each pair, and similar strings for each pair in the rest_name column. Both DataFrames, pandas and recordlinkage are in your environment."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "25103e70",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a comparison object\n",
    "comp_cl = recordlinkage.Compare()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80858c0c",
   "metadata": {},
   "source": [
    "* Use the appropriate `comp_cl` method to find exact matches between the city and `cuisine_type` columns of both DataFrames.\n",
    "* Use the appropriate `comp_cl` method to find similar strings with a 0.8 similarity threshold in the `rest_name` column of both DataFrames."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4fed3273",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Compare>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find exact matches on city, cuisine_types \n",
    "comp_cl.exact('city', 'city', label='city')\n",
    "comp_cl.exact('type', 'type', label='type')\n",
    "\n",
    "# Find similar matches of rest_name\n",
    "comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8dea28a4",
   "metadata": {},
   "source": [
    "* Compute the comparison of the pairs by using the `.compute()` method of `comp_cl`.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c2587c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get potential matches and print\n",
    "potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new) \n",
    "print(potential_matches)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ab098d0",
   "metadata": {},
   "source": [
    "Print out potential_matches, the columns are the columns being compared, with values being 1 for a match, and 0 for not a match for each pair of rows in your DataFrames. To find potential matches, you need to find rows with more than matching value in a column. You can find them with\n",
    "```python\n",
    "potential_matches[potential_matches.sum(axis = 1) >= n]\n",
    "```\n",
    "Where n is the minimum number of columns you want matching to ensure a proper duplicate find, what do you think should the value of n be?\n",
    "\n",
    "* **3 because I need to have matches in all my columns.**\n",
    "\n",
    "* 2 because matching on any of the 2 columns or more is enough to find potential duplicates.\n",
    "\n",
    "* 1 because matching on just 1 column like the restaurant name is enough to find potential duplicates.\n",
    "\n",
    "That's correct! For this example, tightening your selection criteria will ensure good duplicate finds! In the next lesson, you're gonna build on what you learned to link these two DataFrames!\n",
    "\n",
    "## Getting the right index\n",
    "Here's a DataFrame named matches containing potential matches between two DataFrames, `users_1` and `users_2`. Each DataFrame's row indices is stored in `uid_1` and `uid_2` respectively.\n",
    "```\n",
    "             first_name  address_1  address_2  marriage_status  date_of_birth\n",
    "uid_1 uid_2                                                                  \n",
    "0     3              1          1          1                1              0\n",
    "     ...            ...         ...        ...              ...            ...\n",
    "     ...            ...         ...        ...              ...            ...\n",
    "1     3              1          1          1                1              0\n",
    "     ...            ...         ...        ...              ...            ...\n",
    "     ...            ...         ...        ...              ...            ...\n",
    "```\n",
    "How do you extract all values of the `uid_1` index column?\n",
    "\n",
    "\n",
    "* matches.index.get_level_values(0)\n",
    "\n",
    "* matches.index.get_level_values(1)\n",
    "\n",
    "* matches.index.get_level_values('uid_1')\n",
    "\n",
    "* **Both 1 and 3 are correct.**\n",
    "\n",
    "Correct! In the next exercise, you'll use these functions to subset your data and link your DataFrames!\n",
    "\n",
    "## Linking them together!\n",
    "In the last lesson, you've finished the bulk of the work on your effort to link restaurants and restaurants_new. You've generated the different pairs of potentially matching rows, searched for exact matches between the cuisine_type and city columns, but compared for similar strings in the rest_name column. You stored the DataFrame containing the scores in potential_matches.\n",
    "\n",
    "Now it's finally time to link both DataFrames. You will do so by first extracting all row indices of restaurants_new that are matching across the columns mentioned above from potential_matches. Then you will subset restaurants_new on these indices, then append the non-duplicate values to restaurants. All DataFrames are in your environment, alongside pandas imported as pd.\n",
    "\n",
    "* Isolate instances of `potential_matches` where the row sum is above or equal to 3 by using the `.sum()` method.\n",
    "* Extract the second column index from matches, which represents row indices of matching record from `restaurants_new` by using the `.get_level_values()` method.\n",
    "* Subset `restaurants_new` for rows that are not in `matching_indices`.\n",
    "* Append `non_dup` to restaurants."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0dd32b24",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Isolate potential matches with row sum >=3\n",
    "matches = potential_matches[potential_matches.sum(axis = 1) >= 3]\n",
    "\n",
    "# Get values of second column index of matches\n",
    "matching_indices = matches.index.get_level_values(1)\n",
    "\n",
    "# Subset restaurants_new based on non-duplicate values\n",
    "non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]\n",
    "\n",
    "# Append non_dup to restaurants\n",
    "full_restaurants = restaurants.append(non_dup)\n",
    "print(full_restaurants)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99159a9e",
   "metadata": {},
   "source": [
    "Awesome work! Linking the DataFrames is arguably the most straightforward step of record linkage. You are now ready to get started on that recommendation engine!"
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
