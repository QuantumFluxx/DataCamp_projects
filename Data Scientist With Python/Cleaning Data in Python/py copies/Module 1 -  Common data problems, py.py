{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d0173974",
   "metadata": {},
   "source": [
    "# Cleaning Data in Python\n",
    "\n",
    "## Common data problems\n",
    "\n",
    "## Numeric data or ... ?\n",
    "In this exercise, and throughout this chapter, you'll be working with bicycle ride sharing data in San Francisco called `ride_sharing`. It contains information on the start and end stations, the trip duration, and some user information for a bike sharing service.\n",
    "\n",
    "The `user_type` column contains information on whether a user is taking a free ride and takes on the following values:\n",
    "\n",
    "1. for free riders.\n",
    "2. for pay per ride.\n",
    "3. for monthly subscribers.\n",
    "\n",
    "In this instance, you will print the information of ride_sharing using `.info()` and see a firsthand example of how an incorrect data type can flaw your analysis of the dataset. The pandas package is imported as pd.\n",
    "\n",
    "* Print the information of ride_sharing.\n",
    "* Use `.describe()` to print the summary statistics of the `user_type` column from `ride_sharing`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "09e608e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 25760 entries, 0 to 25759\n",
      "Data columns (total 10 columns):\n",
      " #   Column           Non-Null Count  Dtype \n",
      "---  ------           --------------  ----- \n",
      " 0   Unnamed: 0       25760 non-null  int64 \n",
      " 1   duration         25760 non-null  object\n",
      " 2   station_A_id     25760 non-null  int64 \n",
      " 3   station_A_name   25760 non-null  object\n",
      " 4   station_B_id     25760 non-null  int64 \n",
      " 5   station_B_name   25760 non-null  object\n",
      " 6   bike_id          25760 non-null  int64 \n",
      " 7   user_type        25760 non-null  int64 \n",
      " 8   user_birth_year  25760 non-null  int64 \n",
      " 9   user_gender      25760 non-null  object\n",
      "dtypes: int64(6), object(4)\n",
      "memory usage: 2.0+ MB\n",
      "None\n",
      "count    25760.000000\n",
      "mean         2.008385\n",
      "std          0.704541\n",
      "min          1.000000\n",
      "25%          2.000000\n",
      "50%          2.000000\n",
      "75%          3.000000\n",
      "max          3.000000\n",
      "Name: user_type, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "ride_sharing = pd.read_csv('datasets/ride_sharing_new.csv')\n",
    "\n",
    "# Print the information of ride_sharing\n",
    "print(ride_sharing.info())\n",
    "\n",
    "# Print summary statistics of user_type column\n",
    "print(ride_sharing['user_type'].describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "221768bb",
   "metadata": {},
   "source": [
    "By looking at the summary statistics - they don't really seem to offer much description on how users are distributed along their purchase type, why do you think that is?\n",
    "\n",
    "* The user_type column is not of the correct type, it should be converted to str.\n",
    "\n",
    "* The user_type column has an infinite set of possible values, it should be converted to category.\n",
    "\n",
    "* **The user_type column has an finite set of possible values that represent groupings of data, it should be converted to category.**\n",
    "--------\n",
    "* Convert `user_type` into categorical by assigning it the 'category' data type and store it in the `user_type_cat` column.\n",
    "* Make sure you converted `user_type_cat` correctly by using an assert statement."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a2993f04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count     25760\n",
      "unique        3\n",
      "top           2\n",
      "freq      12972\n",
      "Name: user_type_cat, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Convert user_type from integer to category\n",
    "ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')\n",
    "\n",
    "# Write an assert statement confirming the change\n",
    "assert ride_sharing['user_type_cat'].dtype == 'category'\n",
    "\n",
    "# Print new summary statistics \n",
    "print(ride_sharing['user_type_cat'].describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47f4ef8c",
   "metadata": {},
   "source": [
    "Awesome work! Take a look at the new summary statistics, it seems that most users are pay per ride users!\n",
    "\n",
    "## Summing strings and concatenating numbers\n",
    "In the previous exercise, you were able to identify that category is the correct data type for user_type and convert it in order to extract relevant statistical summaries that shed light on the distribution of user_type.\n",
    "\n",
    "Another common data type problem is importing what should be numerical values as strings, as mathematical operations such as summing and multiplication lead to string concatenation, not numerical outputs.\n",
    "\n",
    "In this exercise, you'll be converting the string column duration to the type int. Before that however, you will need to make sure to strip \"minutes\" from the column in order to make sure pandas reads it as numerical. The pandas package has been imported as pd.\n",
    "\n",
    "* Use the `.strip()` method to strip duration of \"minutes\" and store it in the duration_trim column.\n",
    "* Convert `duration_trim` to int and store it in the duration_time column.\n",
    "* Write an assert statement that checks if `duration_time's` data type is now an int.\n",
    "* Print the average ride duration."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "21564169",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         duration duration_trim  duration_time\n",
      "0      12 minutes           12              12\n",
      "1      24 minutes           24              24\n",
      "2       8 minutes            8               8\n",
      "3       4 minutes            4               4\n",
      "4      11 minutes           11              11\n",
      "...           ...           ...            ...\n",
      "25755  11 minutes           11              11\n",
      "25756  10 minutes           10              10\n",
      "25757  14 minutes           14              14\n",
      "25758  14 minutes           14              14\n",
      "25759  29 minutes           29              29\n",
      "\n",
      "[25760 rows x 3 columns]\n",
      "11.389052795031056\n"
     ]
    }
   ],
   "source": [
    "# Strip duration of minutes\n",
    "ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes') \n",
    "\n",
    "# Convert duration to integer\n",
    "ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')\n",
    "\n",
    "# Write an assert statement making sure of conversion\n",
    "assert ride_sharing['duration_time'].dtype == 'int'\n",
    "\n",
    "# Print formed columns and calculate average ride duration \n",
    "print(ride_sharing[['duration','duration_trim','duration_time']])\n",
    "print(ride_sharing['duration_time'].mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b265934d",
   "metadata": {},
   "source": [
    "Great work! 11 minutes is really not bad for an average ride duration in a city like San-Francisco. In the next lesson, you're going to jump right ahead into sanity checking the range of values in your data.\n",
    "\n",
    "## Tire size constraints\n",
    "In this lesson, you're going to build on top of the work you've been doing with the `ride_sharing` DataFrame. You'll be working with the `tire_sizes` column which contains data on each bike's tire size.\n",
    "\n",
    "Bicycle tire sizes could be either 26″, 27″ or 29″ and are here correctly stored as a categorical value. In an effort to cut maintenance costs, the ride sharing provider decided to set the maximum tire size to be 27″.\n",
    "\n",
    "In this exercise, you will make sure the `tire_sizes` column has the correct range by first converting it to an integer, then setting and testing the new upper limit of 27″ for tire sizes.\n",
    "\n",
    "* Convert the `tire_sizes` column from category to 'int'.\n",
    "* Use `.loc[]` to set all values of `tire_sizes` above 27 to 27.\n",
    "* Reconvert back tire_sizes to 'category' from int.\n",
    "* Print the description of the `tire_sizes`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a9f17ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert tire_sizes to integer\n",
    "ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')\n",
    "\n",
    "# Set all values above 27 to 27\n",
    "ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27\n",
    "\n",
    "# Reconvert tire_sizes back to categorical\n",
    "ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')\n",
    "\n",
    "# Print tire size description\n",
    "print(ride_sharing['tire_sizes'].describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59e41a3a",
   "metadata": {},
   "source": [
    "Awesome work! You can look at the new maximum by looking at the top row in the description. Notice how essential it was to convert tire_sizes into integer before setting a new maximum.\n",
    "\n",
    "## Back to the future\n",
    "A new update to the data pipeline feeding into the ride_sharing DataFrame has been updated to register each ride's date. This information is stored in the `ride_date` column of the type object, which represents strings in pandas.\n",
    "\n",
    "A bug was discovered which was relaying rides taken today as taken next year. To fix this, you will find all instances of the `ride_date` column that occur anytime in the future, and set the maximum possible value of this column to today's date. Before doing so, you would need to convert ride_date to a datetime object.\n",
    "\n",
    "The `datetime` package has been imported as dt, alongside all the packages you've been using till now.\n",
    "\n",
    "* Convert `ride_date` to a datetime object using `to_datetime()`, then convert the datetime object into a date and store it in `ride_dt column`.\n",
    "* Create the variable today, which stores today's date by using the `dt.date.today()` function.\n",
    "* For all instances of `ride_dt` in the future, set them to today's date.\n",
    "* Print the maximum date in the `ride_dt` column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9071fd7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "\n",
    "# Convert ride_date to date\n",
    "ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date\n",
    "\n",
    "# Save today's date\n",
    "today = dt.date.today()\n",
    "\n",
    "# Set all in the future to today's date\n",
    "ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today\n",
    "\n",
    "# Print maximum of ride_dt column\n",
    "print(ride_sharing['ride_dt'].max())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33d230f4",
   "metadata": {},
   "source": [
    "Great job! Imagine counting the number of rides taken today without having cleaned your ranges correctly. You would have wildly underreported your findings!\n",
    "\n",
    "## How big is your subset?\n",
    "You have the following loans DataFrame which contains loan and credit score data for consumers, and some metadata such as their first and last names. You want to find both complete and incomplete duplicates using `.duplicated()`.\n",
    "```\n",
    "first_name\tlast_name\tcredit_score\thas_loan\n",
    "Justin\tSaddlemeyer\t600\t1\n",
    "Hadrien\tLacroix\t450\t0\n",
    "```\n",
    "Choose the correct usage of `.duplicated()` below:\n",
    "\n",
    "\n",
    "* loans.duplicated() Because the default method returns both complete and incomplete duplicates.\n",
    "\n",
    "* loans.duplicated(subset = 'first_name') Because constraining the duplicate rows to the first name lets me find incomplete duplicates as well.\n",
    "\n",
    "* **loans.duplicated(subset = ['first_name', 'last_name'], keep = False) Because subsetting on consumer metadata and not discarding any duplicate returns all duplicated rows.**\n",
    "\n",
    "* loans.duplicated(subset = ['first_name', 'last_name'], keep = 'first') Because this drops all duplicates.\n",
    "\n",
    "Correct! Subsetting on metadata and keeping all duplicate records gives you a better bird-eye's view over your data and how to duplicate it! You can even subset the loans DataFrame using bracketing and sort the values so you can properly identify the duplicates.\n",
    "\n",
    "## Finding duplicates\n",
    "A new update to the data pipeline feeding into `ride_sharing` has added the `ride_id` column, which represents a unique identifier for each ride.\n",
    "\n",
    "The update however coincided with radically shorter average ride duration times and irregular user birth dates set in the future. Most importantly, the number of rides taken has increased by 20% overnight, leading you to think there might be both complete and incomplete duplicates in the `ride_sharing` DataFrame.\n",
    "\n",
    "In this exercise, you will confirm this suspicion by finding those duplicates. A sample of `ride_sharing` is in your environment, as well as all the packages you've been working with thus far.\n",
    "\n",
    "* Find duplicated rows of `ride_id` in the ride_sharing DataFrame while setting keep to False.\n",
    "* Subset `ride_sharing` on duplicates and sort by `ride_id` and assign the results to `duplicated_rides`.\n",
    "* Print the `ride_id`, duration and `user_birth_year` columns of `duplicated_rides` in that order."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "49f2ab6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       bike_id    duration  user_birth_year\n",
      "3638        11  12 minutes             1988\n",
      "6088        11   5 minutes             1985\n",
      "10857       11   4 minutes             1987\n",
      "10045       27  13 minutes             1989\n",
      "16104       27  10 minutes             1970\n",
      "...        ...         ...              ...\n",
      "8812      6638  10 minutes             1986\n",
      "6815      6638   5 minutes             1995\n",
      "8456      6638   7 minutes             1983\n",
      "8300      6638   6 minutes             1962\n",
      "8380      6638   8 minutes             1984\n",
      "\n",
      "[25717 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "# Find duplicates\n",
    "duplicates = ride_sharing.duplicated(subset = 'bike_id', keep = False)\n",
    "\n",
    "# Sort your duplicated rides\n",
    "duplicated_rides = ride_sharing[duplicates].sort_values('bike_id')\n",
    "\n",
    "# Print relevant columns\n",
    "print(duplicated_rides[['bike_id','duration','user_birth_year']])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee8a7860",
   "metadata": {},
   "source": [
    "Great job! Notice that rides 33 and 89 are incomplete duplicates, whereas the remaining are complete. You'll learn how to treat them in the next exercise!\n",
    "\n",
    "## Treating duplicates\n",
    "In the last exercise, you were able to verify that the new update feeding into ride_sharing contains a bug generating both complete and incomplete duplicated rows for some values of the `ride_id` column, with occasional discrepant values for the `user_birth_year` and duration columns.\n",
    "\n",
    "In this exercise, you will be treating those duplicated rows by first dropping complete duplicates, and then merging the incomplete duplicate rows into one while keeping the average duration, and the minimum `user_birth_year` for each set of incomplete duplicate rows.\n",
    "\n",
    "* Drop complete duplicates in `ride_sharing` and store the results in `ride_dup`.\n",
    "* Create the statistics dictionary which holds minimum aggregation for `user_birth_year` and mean aggregation for duration.\n",
    "* Drop incomplete duplicates by grouping by ride_id and applying the aggregation in statistics.\n",
    "* Find duplicates again and run the assert statement to verify de-duplication."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d68b871e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop complete duplicates from ride_sharing\n",
    "ride_dup = ride_sharing.drop_duplicates()\n",
    "\n",
    "# Create statistics dictionary for aggregation function\n",
    "statistics = {'user_birth_year': 'min'}\n",
    "\n",
    "# Group by ride_id and compute new statistics\n",
    "ride_unique = ride_dup.groupby('bike_id').agg(statistics).reset_index()\n",
    "\n",
    "# Find duplicated values again\n",
    "duplicates = ride_unique.duplicated(subset = 'bike_id', keep = False)\n",
    "duplicated_rides = ride_unique[duplicates == True]\n",
    "\n",
    "# Assert duplicates are processed\n",
    "assert duplicated_rides.shape[0] == 0"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a8b8b04",
   "metadata": {},
   "source": [
    "Awesome work! You can bet after this fix that ride sharing KPIs will come back to normal."
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
