{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "586d37b2",
   "metadata": {},
   "source": [
    "# Text and categorical data problems\n",
    "\n",
    "## Finding consistency\n",
    "In this exercise and throughout this chapter, you'll be working with the airlines DataFrame which contains survey responses on the San Francisco Airport from airline customers.\n",
    "\n",
    "The DataFrame contains flight metadata such as the airline, the destination, waiting times as well as answers to key questions regarding cleanliness, safety, and satisfaction. Another DataFrame named categories was created, containing all correct possible values for the survey columns.\n",
    "\n",
    "In this exercise, you will use both of these DataFrames to find survey answers with inconsistent values, and drop them, effectively performing an outer and inner join on both these DataFrames as seen in the video exercise. The pandas package has been imported as pd, and the airlines and categories DataFrames are in your environment.\n",
    "\n",
    "* Print the categories DataFrame and take a close look at all possible correct categories of the survey columns.\n",
    "* Print the unique values of the survey columns in airlines using the `.unique()` method."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "419679aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Unnamed: 0     cleanliness           safety          satisfaction\n",
      "0           0           Clean          Neutral        Very satisfied\n",
      "1           1         Average        Very safe               Neutral\n",
      "2           2  Somewhat clean    Somewhat safe    Somewhat satisfied\n",
      "3           3  Somewhat dirty      Very unsafe  Somewhat unsatisfied\n",
      "4           4           Dirty  Somewhat unsafe      Very unsatisfied\n",
      "Cleanliness:  ['Clean' 'Average' 'Somewhat clean' 'Somewhat dirty' 'Dirty'] \n",
      "\n",
      "Safety:  ['Neutral' 'Very safe' 'Somewhat safe' 'Very unsafe' 'Somewhat unsafe'] \n",
      "\n",
      "Satisfaction:  ['Very satisfied' 'Neutral' 'Somewhat satsified' 'Somewhat unsatisfied'\n",
      " 'Very unsatisfied'] \n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "airlines = pd.read_csv('datasets/airlines_final.csv')\n",
    "categories = pd.read_csv('datasets/categories.csv', sep=';')\n",
    "\n",
    "# Print categories DataFrame\n",
    "print(categories)\n",
    "\n",
    "# Print unique values of survey columns in airlines\n",
    "print('Cleanliness: ', airlines['cleanliness'].unique(), \"\\n\")\n",
    "print('Safety: ', airlines['safety'].unique(), \"\\n\")\n",
    "print('Satisfaction: ', airlines['satisfaction'].unique(),\"\\n\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4744194e",
   "metadata": {},
   "source": [
    "Take a look at the output. Out of the cleanliness, safety and satisfaction columns, which one has an inconsistent category and what is it?\n",
    "\n",
    "* cleanliness because it has an Unacceptable category.\n",
    "\n",
    "* cleanliness because it has a Terribly dirty category.\n",
    "\n",
    "* satisfaction because it has a Very satisfied category.\n",
    "\n",
    "* safety because it has a Neutral category.\n",
    "------\n",
    "\n",
    "* Create a set out of the cleanliness column in airlines using `set()` and find the inconsistent category by finding the difference in the cleanliness column of categories.\n",
    "* Find rows of airlines with a cleanliness value not in categories and print the output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8e21bdee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: [Unnamed: 0, id, day, airline, destination, dest_region, dest_size, boarding_area, dept_time, wait_min, cleanliness, safety, satisfaction]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "# Find the cleanliness category in airlines not in categories\n",
    "cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])\n",
    "\n",
    "# Find rows with that category\n",
    "cat_clean_rows = airlines['cleanliness'].isin(cat_clean)\n",
    "\n",
    "# Print rows with inconsistent category\n",
    "print(airlines[cat_clean_rows])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c1a2dc3",
   "metadata": {},
   "source": [
    "## Finding consistency\n",
    "In this exercise and throughout this chapter, you'll be working with the airlines DataFrame which contains survey responses on the San Francisco Airport from airline customers.\n",
    "\n",
    "The DataFrame contains flight metadata such as the airline, the destination, waiting times as well as answers to key questions regarding cleanliness, safety, and satisfaction. Another DataFrame named categories was created, containing all correct possible values for the survey columns.\n",
    "\n",
    "In this exercise, you will use both of these DataFrames to find survey answers with inconsistent values, and drop them, effectively performing an outer and inner join on both these DataFrames as seen in the video exercise. The pandas package has been imported as pd, and the airlines and categories DataFrames are in your environment...\n",
    "\n",
    "* Print the rows with the consistent categories of `cleanliness` only."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f7b2f874",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Unnamed: 0    id        day        airline        destination  \\\n",
      "0              0  1351    Tuesday    UNITED INTL             KANSAI   \n",
      "1              1   373     Friday         ALASKA  SAN JOSE DEL CABO   \n",
      "2              2  2820   Thursday          DELTA        LOS ANGELES   \n",
      "3              3  1157    Tuesday      SOUTHWEST        LOS ANGELES   \n",
      "4              4  2992  Wednesday       AMERICAN              MIAMI   \n",
      "...          ...   ...        ...            ...                ...   \n",
      "2472        2804  1475    Tuesday         ALASKA       NEW YORK-JFK   \n",
      "2473        2805  2222   Thursday      SOUTHWEST            PHOENIX   \n",
      "2474        2806  2684     Friday         UNITED            ORLANDO   \n",
      "2475        2807  2549    Tuesday        JETBLUE         LONG BEACH   \n",
      "2476        2808  2162   Saturday  CHINA EASTERN            QINGDAO   \n",
      "\n",
      "        dest_region dest_size boarding_area   dept_time  wait_min  \\\n",
      "0              Asia       Hub  Gates 91-102  2018-12-31     115.0   \n",
      "1     Canada/Mexico     Small   Gates 50-59  2018-12-31     135.0   \n",
      "2           West US       Hub   Gates 40-48  2018-12-31      70.0   \n",
      "3           West US       Hub   Gates 20-39  2018-12-31     190.0   \n",
      "4           East US       Hub   Gates 50-59  2018-12-31     559.0   \n",
      "...             ...       ...           ...         ...       ...   \n",
      "2472        East US       Hub   Gates 50-59  2018-12-31     280.0   \n",
      "2473        West US       Hub   Gates 20-39  2018-12-31     165.0   \n",
      "2474        East US       Hub   Gates 70-90  2018-12-31      92.0   \n",
      "2475        West US     Small    Gates 1-12  2018-12-31      95.0   \n",
      "2476           Asia     Large    Gates 1-12  2018-12-31     220.0   \n",
      "\n",
      "         cleanliness         safety        satisfaction  \n",
      "0              Clean        Neutral      Very satisfied  \n",
      "1              Clean      Very safe      Very satisfied  \n",
      "2            Average  Somewhat safe             Neutral  \n",
      "3              Clean      Very safe  Somewhat satsified  \n",
      "4     Somewhat clean      Very safe  Somewhat satsified  \n",
      "...              ...            ...                 ...  \n",
      "2472  Somewhat clean        Neutral  Somewhat satsified  \n",
      "2473           Clean      Very safe      Very satisfied  \n",
      "2474           Clean      Very safe      Very satisfied  \n",
      "2475           Clean  Somewhat safe      Very satisfied  \n",
      "2476           Clean      Very safe  Somewhat satsified  \n",
      "\n",
      "[2477 rows x 13 columns]\n"
     ]
    }
   ],
   "source": [
    "# Print rows with consistent categories only\n",
    "print(airlines[~cat_clean_rows])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76b3ccd3",
   "metadata": {},
   "source": [
    "Great consistent work! Keep it up! In the next lesson, we'll be looking at more in depth solutions to dealing with dirty categorical data.\n",
    "\n",
    "## Inconsistent categories\n",
    "In this exercise, you'll be revisiting the airlines DataFrame from the previous lesson.\n",
    "\n",
    "As a reminder, the DataFrame contains flight metadata such as the airline, the destination, waiting times as well as answers to key questions regarding cleanliness, safety, and satisfaction on the San Francisco Airport.\n",
    "\n",
    "In this exercise, you will examine two categorical columns from this DataFrame, dest_region and dest_size respectively, assess how to address them and make sure that they are cleaned and ready for analysis. The pandas package has been imported as pd, and the airlines DataFrame is in your environment.\n",
    "\n",
    "* Print the unique values in dest_region and dest_size respectively."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fb17356e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Asia' 'Canada/Mexico' 'West US' 'East US' 'Midwest US' 'EAST US'\n",
      " 'Middle East' 'Europe' 'eur' 'Central/South America'\n",
      " 'Australia/New Zealand' 'middle east']\n",
      "['Hub' 'Small' '    Hub' 'Medium' 'Large' 'Hub     ' '    Small'\n",
      " 'Medium     ' '    Medium' 'Small     ' '    Large' 'Large     ']\n"
     ]
    }
   ],
   "source": [
    "# Print unique values of both columns\n",
    "print(airlines['dest_region'].unique())\n",
    "print(airlines['dest_size'].unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cecec965",
   "metadata": {},
   "source": [
    "From looking at the output, what do you think is the problem with these columns?\n",
    "\n",
    "\n",
    "* The dest_region column has only inconsistent values due to capitalization.\n",
    "\n",
    "* The dest_region column has inconsistent values due to capitalization and has one value that needs to be remapped.\n",
    "\n",
    "* The dest_size column has only inconsistent values due to leading and trailing spaces.\n",
    "\n",
    "* **Both 2 and 3 are correct.**\n",
    "-----\n",
    "* Change the capitalization of all values of dest_region to lowercase.\n",
    "* Replace the 'eur' with 'europe' in dest_region using the `.replace()` method."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "92a09415",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Lower dest_region column and then replace \"eur\" with \"europe\"\n",
    "airlines['dest_region'] = airlines['dest_region'].str.lower() \n",
    "airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "302451ce",
   "metadata": {},
   "source": [
    "* Strip white spaces from the `dest_size` column using the `.strip()` method.\n",
    "* Verify that the changes have been into effect by printing the unique values of the columns using `.unique()` ."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d06fb118",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['asia' 'canada/mexico' 'west us' 'east us' 'midwest us' 'middle east'\n",
      " 'europe' 'central/south america' 'australia/new zealand']\n",
      "['Hub' 'Small' 'Medium' 'Large']\n"
     ]
    }
   ],
   "source": [
    "# Remove white spaces from `dest_size`\n",
    "airlines['dest_size'] = airlines['dest_size'].str.strip()\n",
    "\n",
    "# Verify changes have been effected\n",
    "print(airlines['dest_region'].unique())\n",
    "print(airlines['dest_size'].unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "94fbed97",
   "metadata": {},
   "source": [
    "Great work! Notice how all categories have been properly treated?\n",
    "\n",
    "## Remapping categories\n",
    "To better understand survey respondents from airlines, you want to find out if there is a relationship between certain responses and the day of the week and wait time at the gate.\n",
    "\n",
    "The airlines DataFrame contains the day and wait_min columns, which are categorical and numerical respectively. The day column contains the exact day a flight took place, and `wait_min` contains the amount of minutes it took travelers to wait at the gate. To make your analysis easier, you want to create two new categorical variables:\n",
    "\n",
    "* `wait_type`: 'short' for 0-60 min, 'medium' for 60-180 and long for 180+\n",
    "* `day_week`: 'weekday' if day is in the weekday, 'weekend' if day is in the weekend.\n",
    "\n",
    "The pandas and numpy packages have been imported as pd and np. Let's create some new categorical data!\n",
    "\n",
    "* Create the ranges and labels for the `wait_type` column mentioned in the description.\n",
    "* Create the `wait_type` column by from `wait_min` by using `pd.cut()`, while inputting `label_ranges` and `label_names` in the correct arguments.\n",
    "* Create the mapping dictionary mapping weekdays to 'weekday' and weekend days to 'weekend'.\n",
    "* Create the `day_week` column by using `.replace()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "dcd9634d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Create ranges for categories\n",
    "label_ranges = [0, 60, 180, np.inf]\n",
    "label_names = ['short', 'medium', 'long']\n",
    "\n",
    "# Create wait_type column\n",
    "airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, \n",
    "                               labels = label_names)\n",
    "\n",
    "# Create mappings and replace\n",
    "mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', \n",
    "            'Thursday': 'weekday', 'Friday': 'weekday', \n",
    "            'Saturday': 'weekend', 'Sunday': 'weekend'}\n",
    "\n",
    "airlines['day_week'] = airlines['day'].replace(mappings)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f926ad7f",
   "metadata": {},
   "source": [
    "Awesome work! You just created two new categorical variables, that when combined with other columns, could produce really interesting analysis. Don't forget, you can always use an assert statement to check your changes passed.\n",
    "\n",
    "## Removing titles and taking names\n",
    "While collecting survey respondent metadata in the `airlines` DataFrame, the full name of respondents was saved in the `full_name` column. However upon closer inspection, you found that a lot of the different names are prefixed by honorifics such as \"Dr.\", \"Mr.\", \"Ms.\" and \"Miss\".\n",
    "\n",
    "Your ultimate objective is to create two new columns named `first_name` and `last_name`, containing the first and last names of respondents respectively. Before doing so however, you need to remove honorifics.\n",
    "\n",
    "* Remove \"Dr.\", \"Mr.\", \"Miss\" and \"Ms.\" from `full_name` by replacing them with an empty string \"\" in that order.\n",
    "* Run the assert statement using `.str.contains()` that tests whether `full_name` still contains any of the honorifics."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "007ba397",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "# Replace \"Dr.\" with empty string \"\"\n",
    "airlines['destination'] = airlines['destination'].str.replace(\"Dr.\", \"\")\n",
    "\n",
    "# Replace \"Mr.\" with empty string \"\"\n",
    "airlines['destination'] = airlines['destination'].str.replace(\"Mr.\", \"\")\n",
    "\n",
    "# Replace \"Miss\" with empty string \"\"\n",
    "airlines['destination'] = airlines['destination'].str.replace(\"Miss\", \"\")\n",
    "\n",
    "# Replace \"Ms.\" with empty string \"\"\n",
    "airlines['destination'] = airlines['destination'].str.replace(\"Ms.\", \"\")\n",
    "\n",
    "# Assert that full_name has no honorifics\n",
    "assert airlines['destination'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29910be5",
   "metadata": {},
   "source": [
    "Great work! By normalizing full names this way, you can now easily split them into first names and last names!\n",
    "\n",
    "## Keeping it descriptive\n",
    "To further understand travelers' experiences in the San Francisco Airport, the quality assurance department sent out a qualitative questionnaire to all travelers who gave the airport the worst score on all possible categories. The objective behind this questionnaire is to identify common patterns in what travelers are saying about the airport.\n",
    "\n",
    "Their response is stored in the `survey_response` column. Upon a closer look, you realized a few of the answers gave the shortest possible character amount without much substance. In this exercise, you will isolate the responses with a character count higher than 40 , and make sure your new DataFrame contains responses with 40 characters or more using an assert statement.\n",
    "\n",
    "* Using the `airlines` DataFrame, store the length of each instance in the `survey_response` column in `resp_length` by using `.str.len()`.\n",
    "* Isolate the rows of airlines with `resp_length` higher than 40.\n",
    "* Assert that the smallest `survey_response` length in `airlines_survey` is now bigger than 40."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e1bf9c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store length of each row in survey_response column\n",
    "resp_length = airlines['survey_response'].str.len()\n",
    "\n",
    "# Find rows in airlines where resp_length > 40\n",
    "airlines_survey = airlines[resp_length > 40]\n",
    "\n",
    "# Assert minimum survey_response length is > 40\n",
    "assert airlines_survey['survey_response'].str.len().min() > 40\n",
    "\n",
    "# Print new survey_response column\n",
    "print(airlines_survey['survey_response'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2c2f1cf",
   "metadata": {},
   "source": [
    "Phenomenal work! These types of feedbacks are essential to improving any service. Coupled with some wordcount analysis, you can find common patterns across all survey responses in no time!"
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
