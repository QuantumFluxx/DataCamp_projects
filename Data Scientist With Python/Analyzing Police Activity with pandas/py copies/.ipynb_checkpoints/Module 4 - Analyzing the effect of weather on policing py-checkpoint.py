{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "92d8140a",
   "metadata": {},
   "source": [
    "# Analyzing the effect of weather on policing\n",
    "\n",
    "## Plotting the temperature\n",
    "In this exercise, you'll examine the temperature columns from the weather dataset to assess whether the data seems trustworthy. First you'll print the summary statistics, and then you'll visualize the data using a box plot.\n",
    "\n",
    "When deciding whether the values seem reasonable, keep in mind that the temperature is measured in degrees Fahrenheit, not Celsius!\n",
    "\n",
    "* Read `weather.csv` into a DataFrame named weather.\n",
    "* Select the temperature columns (TMIN, TAVG, TMAX) and print their summary statistics using the `.describe()` method.\n",
    "* Create a box plot to visualize the temperature columns.\n",
    "* Display the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "295f179d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              TMIN         TAVG         TMAX\n",
      "count  4017.000000  1217.000000  4017.000000\n",
      "mean     43.484441    52.493016    61.268608\n",
      "std      17.020298    17.830714    18.199517\n",
      "min      -5.000000     6.000000    15.000000\n",
      "25%      30.000000    39.000000    47.000000\n",
      "50%      44.000000    54.000000    62.000000\n",
      "75%      58.000000    68.000000    77.000000\n",
      "max      77.000000    86.000000   102.000000\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Read 'weather.csv' into a DataFrame named 'weather'\n",
    "weather = pd.read_csv('datasets/weather.csv')\n",
    "\n",
    "# Describe the temperature columns\n",
    "print(weather[['TMIN', 'TAVG', 'TMAX']].describe())\n",
    "\n",
    "# Create a box plot of the temperature columns\n",
    "weather[['TMIN', 'TAVG', 'TMAX']].plot(kind='box')\n",
    "\n",
    "# Display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b877a01d",
   "metadata": {},
   "source": [
    "Nice job! The temperature data looks good so far: the TAVG values are in between TMIN and TMAX, and the measurements and ranges seem reasonable.\n",
    "\n",
    "## Plotting the temperature difference\n",
    "In this exercise, you'll continue to assess whether the dataset seems trustworthy by plotting the difference between the maximum and minimum temperatures.\n",
    "\n",
    "What do you notice about the resulting histogram? Does it match your expectations, or do you see anything unusual?\n",
    "\n",
    "* Create a new column in the weather DataFrame named TDIFF that represents the difference between the maximum and minimum temperatures.\n",
    "* Print the summary statistics for TDIFF using the `.describe()` method.\n",
    "* Create a histogram with 20 bins to visualize TDIFF.\n",
    "* Display the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b2db9400",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count    4017.000000\n",
      "mean       17.784167\n",
      "std         6.350720\n",
      "min         2.000000\n",
      "25%        14.000000\n",
      "50%        18.000000\n",
      "75%        22.000000\n",
      "max        43.000000\n",
      "Name: TDIFF, dtype: float64\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a 'TDIFF' column that represents temperature difference\n",
    "weather['TDIFF'] = weather.TMAX - weather.TMIN\n",
    "\n",
    "# Describe the 'TDIFF' column\n",
    "print(weather.TDIFF.describe())\n",
    "\n",
    "# Create a histogram with 20 bins to visualize 'TDIFF'\n",
    "weather.TDIFF.plot(kind='hist', bins=20)\n",
    "\n",
    "# Display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e82e81a4",
   "metadata": {},
   "source": [
    "Great work! The TDIFF column has no negative values and its distribution is approximately normal, both of which are signs that the data is trustworthy.\n",
    "\n",
    "## Counting bad weather conditions\n",
    "The weather DataFrame contains 20 columns that start with 'WT', each of which represents a bad weather condition. For example:\n",
    "\n",
    "* WT05 indicates \"Hail\"\n",
    "* WT11 indicates \"High or damaging winds\"\n",
    "* WT17 indicates \"Freezing rain\"\n",
    "\n",
    "For every row in the dataset, each WT column contains either a 1 (meaning the condition was present that day) or NaN (meaning the condition was not present).\n",
    "\n",
    "In this exercise, you'll quantify \"how bad\" the weather was each day by counting the number of 1 values in each row.\n",
    "\n",
    "* Copy the columns WT01 through WT22 from weather to a new DataFrame named WT.\n",
    "* Calculate the sum of each row in WT, and store the results in a new weather column named bad_conditions.\n",
    "* Replace any missing values in `bad_conditions` with a 0. (This has been done for you.)\n",
    "* Create a histogram to visualize `bad_conditions`, and then display the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0bcb745e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Copy 'WT01' through 'WT22' to a new DataFrame\n",
    "WT = weather.loc[:, 'WT01':'WT22']\n",
    "\n",
    "# Calculate the sum of each row in 'WT'\n",
    "weather['bad_conditions'] = WT.sum(axis='columns')\n",
    "\n",
    "# Replace missing values in 'bad_conditions' with '0'\n",
    "weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')\n",
    "\n",
    "# Create a histogram to visualize 'bad_conditions'\n",
    "weather.bad_conditions.plot(kind='hist')\n",
    "\n",
    "# Display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e13079fe",
   "metadata": {},
   "source": [
    "Excellent work! It looks like many days didn't have any bad weather conditions, and only a small portion of days had more than four bad weather conditions.\n",
    "\n",
    "## Rating the weather conditions\n",
    "In the previous exercise, you counted the number of bad weather conditions each day. In this exercise, you'll use the counts to create a rating system for the weather.\n",
    "\n",
    "The counts range from 0 to 9, and should be converted to ratings as follows:\n",
    "\n",
    "* Convert 0 to 'good'\n",
    "* Convert 1 through 4 to 'bad'\n",
    "* Convert 5 through 9 to 'worse'\n",
    "-----\n",
    "* Count the unique values in the `bad_conditions` column and sort the index. (This has been done for you.)\n",
    "* Create a dictionary called mapping that maps the `bad_conditions` integers to the specified strings.\n",
    "* Convert the `bad_conditions` integers to strings using the mapping and store the results in a new column called rating.\n",
    "* Count the unique values in rating to verify that the integers were properly converted to strings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "99e74521",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    1749\n",
      "1     613\n",
      "2     367\n",
      "3     380\n",
      "4     476\n",
      "5     282\n",
      "6     101\n",
      "7      41\n",
      "8       4\n",
      "9       4\n",
      "Name: bad_conditions, dtype: int64\n",
      "bad      1836\n",
      "good     1749\n",
      "worse     432\n",
      "Name: rating, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Count the unique values in 'bad_conditions' and sort the index\n",
    "print(weather.bad_conditions.value_counts().sort_index())\n",
    "\n",
    "# Create a dictionary that maps integers to strings\n",
    "mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad', 4:'bad', 5:'worse', 6:'worse', 7:'worse', 8:'worse', 9:'worse'}\n",
    "\n",
    "# Convert the 'bad_conditions' integers to strings using the 'mapping'\n",
    "weather['rating'] = weather.bad_conditions.map(mapping)\n",
    "\n",
    "# Count the unique values in 'rating'\n",
    "print(weather.rating.value_counts())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8ede85f",
   "metadata": {},
   "source": [
    "Nice job! This rating system should make the weather condition data easier to understand.\n",
    "\n",
    "## Changing the data type to category\n",
    "Since the rating column only has a few possible values, you'll change its data type to category in order to store the data more efficiently. You'll also specify a logical order for the categories, which will be useful for future exercises.\n",
    "\n",
    "* Create a CategoricalDtype object called cats that lists the weather ratings in a logical order: 'good', 'bad', 'worse'. Make sure to specify that the categories should be treated as ordered.\n",
    "* Use the cats object to change the data type of the rating column from object to category.\n",
    "* Examine the head of the rating column to confirm that the categories are logically ordered."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "717f7fd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    bad\n",
      "1    bad\n",
      "2    bad\n",
      "3    bad\n",
      "4    bad\n",
      "Name: rating, dtype: category\n",
      "Categories (3, object): ['good' < 'bad' < 'worse']\n"
     ]
    }
   ],
   "source": [
    "# Specify the logical order of the weather ratings\n",
    "cats = pd.CategoricalDtype(['good', 'bad', 'worse'], ordered=True)\n",
    "\n",
    "# Change the data type of 'rating' to category\n",
    "weather['rating'] = weather.rating.astype(cats)\n",
    "\n",
    "# Examine the head of 'rating'\n",
    "print(weather.rating.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d9bd74b",
   "metadata": {},
   "source": [
    "Excellent! You'll use the rating column in future exercises to analyze the effects of weather on police behavior.\n",
    "\n",
    "## Preparing the DataFrames\n",
    "In this exercise, you'll prepare the traffic stop and weather rating DataFrames so that they're ready to be merged:\n",
    "\n",
    "1. With the ri DataFrame, you'll move the stop_datetime index to a column since the index will be lost during the merge.\n",
    "2. With the weather DataFrame, you'll select the DATE and rating columns and put them in a new DataFrame.\n",
    "\n",
    "* Reset the index of the ri DataFrame.\n",
    "* Examine the head of ri to verify that `stop_datetime` is now a DataFrame column, and the index is now the default integer index.\n",
    "* Create a new DataFrame named `weather_rating` that contains only the DATE and rating columns from the weather DataFrame.\n",
    "* Examine the head of `weather_rating` to verify that it contains the proper columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0a2fa176",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index state   stop_date stop_time  county_name driver_gender driver_race  \\\n",
      "0      0    RI  2005-01-04     12:55          NaN             M       White   \n",
      "1      1    RI  2005-01-23     23:15          NaN             M       White   \n",
      "2      2    RI  2005-02-17     04:15          NaN             M       White   \n",
      "3      3    RI  2005-02-20     17:15          NaN             M       White   \n",
      "4      4    RI  2005-02-24     01:20          NaN             F       White   \n",
      "\n",
      "                    violation_raw  violation  search_conducted search_type  \\\n",
      "0  Equipment/Inspection Violation  Equipment             False         NaN   \n",
      "1                        Speeding   Speeding             False         NaN   \n",
      "2                        Speeding   Speeding             False         NaN   \n",
      "3                Call for Service      Other             False         NaN   \n",
      "4                        Speeding   Speeding             False         NaN   \n",
      "\n",
      "    stop_outcome is_arrested stop_duration  drugs_related_stop district  \n",
      "0       Citation       False      0-15 Min               False  Zone X4  \n",
      "1       Citation       False      0-15 Min               False  Zone K3  \n",
      "2       Citation       False      0-15 Min               False  Zone X4  \n",
      "3  Arrest Driver        True     16-30 Min               False  Zone X1  \n",
      "4       Citation       False      0-15 Min               False  Zone X3  \n",
      "         DATE rating\n",
      "0  2005-01-01    bad\n",
      "1  2005-01-02    bad\n",
      "2  2005-01-03    bad\n",
      "3  2005-01-04    bad\n",
      "4  2005-01-05    bad\n"
     ]
    }
   ],
   "source": [
    "# Read 'police.csv' into a DataFrame named ri\n",
    "ri = pd.read_csv('datasets/police.csv')\n",
    "\n",
    "# Reset the index of 'ri'\n",
    "ri.reset_index(inplace=True)\n",
    "\n",
    "# Examine the head of 'ri'\n",
    "print(ri.head())\n",
    "\n",
    "# Create a DataFrame from the 'DATE' and 'rating' columns\n",
    "weather_rating = weather[['DATE', 'rating']]\n",
    "\n",
    "# Examine the head of 'weather_rating'\n",
    "print(weather_rating.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af4529ef",
   "metadata": {},
   "source": [
    "Great work! The ri and weather_rating DataFrames are now ready to be merged.\n",
    "\n",
    "## Merging the DataFrames\n",
    "In this exercise, you'll merge the ri and `weather_rating` DataFrames into a new DataFrame, `ri_weather`.\n",
    "\n",
    "The DataFrames will be joined using the stop_date column from ri and the DATE column from `weather_rating`. Thankfully the date formatting matches exactly, which is not always the case!\n",
    "\n",
    "Once the merge is complete, you'll set `stop_datetime` as the index, which is the column you saved in the previous exercise.\n",
    "\n",
    "* Examine the shape of the ri DataFrame.\n",
    "* Merge the ri and `weather_rating` DataFrames using a left join.\n",
    "* Examine the shape of `ri_weather` to confirm that it has two more columns but the same number of rows as ri.\n",
    "* Replace the index of `ri_weather` with the `stop_datetime` column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "816d2fe2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(91741, 16)\n",
      "(91741, 18)\n"
     ]
    }
   ],
   "source": [
    "# Examine the shape of 'ri'\n",
    "print(ri.shape)\n",
    "\n",
    "# Merge 'ri' and 'weather_rating' using a left join\n",
    "ri_weather = pd.merge(left=ri, right=weather_rating, left_on='stop_date', right_on='DATE', how='left')\n",
    "\n",
    "# Examine the shape of 'ri_weather'\n",
    "print(ri_weather.shape)\n",
    "\n",
    "# Set 'stop_datetime' as the index of 'ri_weather'\n",
    "ri_weather.set_index('stop_time', inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bfd033fe",
   "metadata": {},
   "source": [
    "Fantastic! In the next section, you'll use ri_weather to analyze the relationship between weather conditions and police behavior.\n",
    "\n",
    "## Comparing arrest rates by weather rating\n",
    "Do police officers arrest drivers more often when the weather is bad? Let's find out!\n",
    "\n",
    "* First, you'll calculate the overall arrest rate.\n",
    "* Then, you'll calculate the arrest rate for each of the weather ratings you previously assigned.\n",
    "* Finally, you'll add violation type as a second factor in the analysis, to see if that accounts for any differences in the arrest rate.\n",
    "\n",
    "Since you previously defined a logical order for the weather categories, `good < bad < worse`, they will be sorted that way in the results.\n",
    "\n",
    "* Calculate the overall arrest rate by taking the mean of the `is_arrested` Series."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "78578c10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.03556777868937704\n"
     ]
    }
   ],
   "source": [
    "# Calculate the overall arrest rate\n",
    "print(ri_weather.is_arrested.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b341c432",
   "metadata": {},
   "source": [
    "* Calculate the arrest rate for each weather rating using a `.groupby()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d2ae86b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rating\n",
      "good     0.033712\n",
      "bad      0.036261\n",
      "worse    0.041667\n",
      "Name: is_arrested, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate the arrest rate for each 'rating'\n",
    "print(ri_weather.groupby('rating').is_arrested.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "939d7857",
   "metadata": {},
   "source": [
    "* Calculate the arrest rate for each combination of violation and rating. How do the arrest rates differ by group?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "539ad1b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "violation            rating\n",
      "Equipment            good      0.058995\n",
      "                     bad       0.066311\n",
      "                     worse     0.097357\n",
      "Moving violation     good      0.056227\n",
      "                     bad       0.058050\n",
      "                     worse     0.065860\n",
      "Other                good      0.076923\n",
      "                     bad       0.087443\n",
      "                     worse     0.062893\n",
      "Registration/plates  good      0.081574\n",
      "                     bad       0.098160\n",
      "                     worse     0.115625\n",
      "Seat belt            good      0.028587\n",
      "                     bad       0.022493\n",
      "                     worse     0.000000\n",
      "Speeding             good      0.013404\n",
      "                     bad       0.013314\n",
      "                     worse     0.016886\n",
      "Name: is_arrested, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate the arrest rate for each 'violation' and 'rating'\n",
    "print(ri_weather.groupby(['violation', 'rating']).is_arrested.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c920d07",
   "metadata": {},
   "source": [
    "Wow! The arrest rate increases as the weather gets worse, and that trend persists across many of the violation types. This doesn't prove a causal link, but it's quite an interesting result!\n",
    "\n",
    "## Selecting from a multi-indexed Series\n",
    "The output of a single `.groupby()` operation on multiple columns is a Series with a MultiIndex. Working with this type of object is similar to working with a DataFrame:\n",
    "\n",
    "* The outer index level is like the DataFrame rows.\n",
    "* The inner index level is like the DataFrame columns.\n",
    "\n",
    "In this exercise, you'll practice accessing data from a multi-indexed Series using the `.loc[]` accessor.\n",
    "\n",
    "* Save the output of the `.groupby()` operation from the last exercise as a new object, `arrest_rate`. (This has been done for you.)\n",
    "* Print the `arrest_rate` Series and examine it.\n",
    "* Print the arrest rate for moving violations in bad weather.\n",
    "* Print the arrest rates for speeding violations in all three weather conditions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8ef9a20d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "violation            rating\n",
      "Equipment            good      0.058995\n",
      "                     bad       0.066311\n",
      "                     worse     0.097357\n",
      "Moving violation     good      0.056227\n",
      "                     bad       0.058050\n",
      "                     worse     0.065860\n",
      "Other                good      0.076923\n",
      "                     bad       0.087443\n",
      "                     worse     0.062893\n",
      "Registration/plates  good      0.081574\n",
      "                     bad       0.098160\n",
      "                     worse     0.115625\n",
      "Seat belt            good      0.028587\n",
      "                     bad       0.022493\n",
      "                     worse     0.000000\n",
      "Speeding             good      0.013404\n",
      "                     bad       0.013314\n",
      "                     worse     0.016886\n",
      "Name: is_arrested, dtype: float64\n",
      "0.05804964058049641\n",
      "rating\n",
      "good     0.013404\n",
      "bad      0.013314\n",
      "worse    0.016886\n",
      "Name: is_arrested, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Save the output of the groupby operation from the last exercise\n",
    "arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()\n",
    "\n",
    "# Print the 'arrest_rate' Series\n",
    "print(arrest_rate)\n",
    "\n",
    "# Print the arrest rate for moving violations in bad weather\n",
    "print(arrest_rate.loc['Moving violation', 'bad'])\n",
    "\n",
    "# Print the arrest rates for speeding violations in all three weather conditions\n",
    "print(arrest_rate.loc['Speeding'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b57018ec",
   "metadata": {},
   "source": [
    "Great job! The .loc[ ] accessor is a powerful and flexible tool for data selection.\n",
    "\n",
    "## Reshaping the arrest rate data\n",
    "In this exercise, you'll start by reshaping the arrest_rate Series into a DataFrame. This is a useful step when working with any multi-indexed Series, since it enables you to access the full range of DataFrame methods.\n",
    "\n",
    "Then, you'll create the exact same DataFrame using a pivot table. This is a great example of how pandas often gives you more than one way to reach the same result!\n",
    "\n",
    "* Unstack the `arrest_rate` Series to reshape it into a DataFrame.\n",
    "* Create the exact same DataFrame using a pivot table! Each of the three `.pivot_table()` parameters should be specified as one of the `ri_weather` columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ab63f047",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rating                   good       bad     worse\n",
      "violation                                        \n",
      "Equipment            0.058995  0.066311  0.097357\n",
      "Moving violation     0.056227  0.058050  0.065860\n",
      "Other                0.076923  0.087443  0.062893\n",
      "Registration/plates  0.081574  0.098160  0.115625\n",
      "Seat belt            0.028587  0.022493  0.000000\n",
      "Speeding             0.013404  0.013314  0.016886\n",
      "rating                   good       bad     worse\n",
      "violation                                        \n",
      "Equipment            0.058995  0.066311  0.097357\n",
      "Moving violation     0.056227  0.058050  0.065860\n",
      "Other                0.076923  0.087443  0.062893\n",
      "Registration/plates  0.081574  0.098160  0.115625\n",
      "Seat belt            0.028587  0.022493  0.000000\n",
      "Speeding             0.013404  0.013314  0.016886\n"
     ]
    }
   ],
   "source": [
    "# Unstack the 'arrest_rate' Series into a DataFrame\n",
    "print(arrest_rate.unstack())\n",
    "\n",
    "# Create the same DataFrame using a pivot table\n",
    "print(ri_weather.pivot_table(index='violation', columns='rating', values='is_arrested'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3fa25d1a",
   "metadata": {},
   "source": [
    "Excellent work! In the future, when you need to create a DataFrame like this, you can choose whichever method makes the most sense to you."
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
