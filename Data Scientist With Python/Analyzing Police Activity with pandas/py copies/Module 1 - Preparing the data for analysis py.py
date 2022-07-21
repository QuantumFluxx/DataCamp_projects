{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d66c2bb6",
   "metadata": {},
   "source": [
    "# Analyzing Police Activity with pandas\n",
    "\n",
    "## Preparing the data for analysis\n",
    "\n",
    "## Examining the dataset\n",
    "Throughout this course, you'll be analyzing a dataset of traffic stops in Rhode Island that was collected by the Stanford Open Policing Project.\n",
    "\n",
    "Before beginning your analysis, it's important that you familiarize yourself with the dataset. In this exercise, you'll read the dataset into pandas, examine the first few rows, and then count the number of missing values.\n",
    "\n",
    "* Import pandas using the alias pd.\n",
    "* Read the file `police.csv` into a DataFrame named ri.\n",
    "* Examine the first 5 rows of the DataFrame (known as the \"head\").\n",
    "* Count the number of missing values in each column: Use `.isnull()` to check which DataFrame elements are missing, and then take the `.sum()` to count the number of True values in each column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8a3ea46e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  state   stop_date stop_time  county_name driver_gender driver_race  \\\n",
      "0    RI  2005-01-04     12:55          NaN             M       White   \n",
      "1    RI  2005-01-23     23:15          NaN             M       White   \n",
      "2    RI  2005-02-17     04:15          NaN             M       White   \n",
      "3    RI  2005-02-20     17:15          NaN             M       White   \n",
      "4    RI  2005-02-24     01:20          NaN             F       White   \n",
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
      "state                     0\n",
      "stop_date                 0\n",
      "stop_time                 0\n",
      "county_name           91741\n",
      "driver_gender          5205\n",
      "driver_race            5202\n",
      "violation_raw          5202\n",
      "violation              5202\n",
      "search_conducted          0\n",
      "search_type           88434\n",
      "stop_outcome           5202\n",
      "is_arrested            5202\n",
      "stop_duration          5202\n",
      "drugs_related_stop        0\n",
      "district                  0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Import the pandas library as pd\n",
    "import pandas as pd\n",
    "\n",
    "# Read 'police.csv' into a DataFrame named ri\n",
    "ri = pd.read_csv('datasets/police.csv')\n",
    "\n",
    "# Examine the head of the DataFrame\n",
    "print(ri.head())\n",
    "\n",
    "# Count the number of missing values in each column\n",
    "print(ri.isnull().sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8971ea1",
   "metadata": {},
   "source": [
    "It looks like most of the columns have at least some missing values. We'll figure out how to handle these values in the next exercise!\n",
    "\n",
    "## Dropping columns\n",
    "Often, a DataFrame will contain columns that are not useful to your analysis. Such columns should be dropped from the DataFrame, to make it easier for you to focus on the remaining columns.\n",
    "\n",
    "In this exercise, you'll drop the `county_name` column because it only contains missing values, and you'll drop the state column because all of the traffic stops took place in one state (Rhode Island). Thus, these columns can be dropped because they contain no useful information. The number of missing values in each column has been printed in the IPython Shell for you.\n",
    "\n",
    "* Examine the DataFrame's `.shape` to find out the number of rows and columns.\n",
    "* Drop both the `county_name` and state columns by passing the column names to the `.drop()` method as a list of strings.\n",
    "* Examine the `.shape` again to verify that there are now two fewer columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5743d830",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(91741, 15)\n",
      "(91741, 13)\n"
     ]
    }
   ],
   "source": [
    "# Examine the shape of the DataFrame\n",
    "print(ri.shape)\n",
    "\n",
    "# Drop the 'county_name' and 'state' columns\n",
    "ri.drop(['county_name', 'state'], axis='columns', inplace=True)\n",
    "\n",
    "# Examine the shape of the DataFrame (again)\n",
    "print(ri.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1f555391",
   "metadata": {},
   "source": [
    "Great job! We'll continue to remove unnecessary data from the DataFrame in the next exercise.\n",
    "\n",
    "## Dropping rows\n",
    "When you know that a specific column will be critical to your analysis, and only a small fraction of rows are missing a value in that column, it often makes sense to remove those rows from the dataset.\n",
    "\n",
    "During this course, the `driver_gender` column will be critical to many of your analyses. Because only a small fraction of rows are missing `driver_gender`, we'll drop those rows from the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d3e69193",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "stop_date                 0\n",
      "stop_time                 0\n",
      "driver_gender          5205\n",
      "driver_race            5202\n",
      "violation_raw          5202\n",
      "violation              5202\n",
      "search_conducted          0\n",
      "search_type           88434\n",
      "stop_outcome           5202\n",
      "is_arrested            5202\n",
      "stop_duration          5202\n",
      "drugs_related_stop        0\n",
      "district                  0\n",
      "dtype: int64\n",
      "stop_date                 0\n",
      "stop_time                 0\n",
      "driver_gender             0\n",
      "driver_race               0\n",
      "violation_raw             0\n",
      "violation                 0\n",
      "search_conducted          0\n",
      "search_type           83229\n",
      "stop_outcome              0\n",
      "is_arrested               0\n",
      "stop_duration             0\n",
      "drugs_related_stop        0\n",
      "district                  0\n",
      "dtype: int64\n",
      "(86536, 13)\n"
     ]
    }
   ],
   "source": [
    "# Count the number of missing values in each column\n",
    "print(ri.isnull().sum())\n",
    "\n",
    "# Drop all rows that are missing 'driver_gender'\n",
    "ri.dropna(subset=['driver_gender'], inplace=True)\n",
    "\n",
    "# Count the number of missing values in each column (again)\n",
    "print(ri.isnull().sum())\n",
    "\n",
    "# Examine the shape of the DataFrame\n",
    "print(ri.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23e54873",
   "metadata": {},
   "source": [
    "Excellent! We dropped around 5,000 rows, which is a small fraction of the dataset, and now only one column remains with any missing values.\n",
    "\n",
    "## Finding an incorrect data type\n",
    "The dtypes attribute of the ri DataFrame has been printed for you. Your task is to explore the ri DataFrame in the IPython Shell to determine which column's data type should be changed.\n",
    "\n",
    "* stop_time should have a data type of float\n",
    "\n",
    "* search_conducted should have a data type of object\n",
    "\n",
    "* **is_arrested should have a data type of bool**\n",
    "\n",
    "* district should have a data type of int\n",
    "\n",
    "Correct! We'll fix the data type of the is_arrested column in the next exercise.\n",
    "\n",
    "## Fixing a data type\n",
    "We saw in the previous exercise that the is_arrested column currently has the object data type. In this exercise, we'll change the data type to bool, which is the most suitable type for a column containing True and False values.\n",
    "\n",
    "Fixing the data type will enable us to use mathematical operations on the `is_arrested` column that would not be possible otherwise.\n",
    "\n",
    "* Examine the head of the `is_arrested` column to verify that it contains True and False values and to check the column's data type.\n",
    "* Use the `.astype()` method to convert is_arrested to a bool column.\n",
    "* Check the new data type of `is_arrested` to confirm that it is now a bool column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d1a7825e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    False\n",
      "1    False\n",
      "2    False\n",
      "3     True\n",
      "4    False\n",
      "Name: is_arrested, dtype: object\n",
      "bool\n"
     ]
    }
   ],
   "source": [
    "# Examine the head of the 'is_arrested' column\n",
    "print(ri.is_arrested.head())\n",
    "\n",
    "# Change the data type of 'is_arrested' to 'bool'\n",
    "ri['is_arrested'] = ri.is_arrested.astype('bool')\n",
    "\n",
    "# Check the data type of 'is_arrested' \n",
    "print(ri.is_arrested.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97db7c85",
   "metadata": {},
   "source": [
    "Great! It's best to fix these data type problems early, before you begin your analysis.\n",
    "\n",
    "## Combining object columns\n",
    "Currently, the date and time of each traffic stop are stored in separate object columns: `stop_date` and `stop_time`.\n",
    "\n",
    "In this exercise, you'll combine these two columns into a single column, and then convert it to `datetime` format. This will enable convenient date-based attributes that we'll use later in the course.\n",
    "\n",
    "* Use a string method to concatenate `stop_date` and `stop_time` (separated by a space), and store the result in combined.\n",
    "* Convert combined to datetime format, and store the result in a new column named `stop_datetime`.\n",
    "* Examine the DataFrame `.dtypes` to confirm that stop_datetime is a datetime column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "198ea506",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "stop_date                     object\n",
      "stop_time                     object\n",
      "driver_gender                 object\n",
      "driver_race                   object\n",
      "violation_raw                 object\n",
      "violation                     object\n",
      "search_conducted                bool\n",
      "search_type                   object\n",
      "stop_outcome                  object\n",
      "is_arrested                     bool\n",
      "stop_duration                 object\n",
      "drugs_related_stop              bool\n",
      "district                      object\n",
      "stop_datetime         datetime64[ns]\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Concatenate 'stop_date' and 'stop_time' (separated by a space)\n",
    "combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')\n",
    "\n",
    "# Convert 'combined' to datetime format\n",
    "ri['stop_datetime'] = pd.to_datetime(combined)\n",
    "\n",
    "# Examine the data types of the DataFrame\n",
    "print(ri.dtypes)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a17efc82",
   "metadata": {},
   "source": [
    "Excellent! Now we're ready to set the stop_datetime column as the index.\n",
    "\n",
    "## Setting the index\n",
    "The last step that you'll take in this chapter is to set the stop_datetime column as the DataFrame's index. By replacing the default index with a `DatetimeIndex`, you'll make it easier to analyze the dataset by date and time, which will come in handy later in the course!\n",
    "\n",
    "* Set `stop_datetime` as the DataFrame index.\n",
    "* Examine the index to verify that it is a `DatetimeIndex`.\n",
    "* Examine the DataFrame columns to confirm that stop_datetime is no longer one of the columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "91a76d5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DatetimeIndex(['2005-01-04 12:55:00', '2005-01-23 23:15:00',\n",
      "               '2005-02-17 04:15:00', '2005-02-20 17:15:00',\n",
      "               '2005-02-24 01:20:00', '2005-03-14 10:00:00',\n",
      "               '2005-03-29 21:55:00', '2005-04-04 21:25:00',\n",
      "               '2005-07-14 11:20:00', '2005-07-14 19:55:00',\n",
      "               ...\n",
      "               '2015-12-31 13:23:00', '2015-12-31 18:59:00',\n",
      "               '2015-12-31 19:13:00', '2015-12-31 20:20:00',\n",
      "               '2015-12-31 20:50:00', '2015-12-31 21:21:00',\n",
      "               '2015-12-31 21:59:00', '2015-12-31 22:04:00',\n",
      "               '2015-12-31 22:09:00', '2015-12-31 22:47:00'],\n",
      "              dtype='datetime64[ns]', name='stop_datetime', length=86536, freq=None)\n",
      "Index(['stop_date', 'stop_time', 'driver_gender', 'driver_race',\n",
      "       'violation_raw', 'violation', 'search_conducted', 'search_type',\n",
      "       'stop_outcome', 'is_arrested', 'stop_duration', 'drugs_related_stop',\n",
      "       'district'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Set 'stop_datetime' as the index\n",
    "ri.set_index('stop_datetime', inplace=True)\n",
    "\n",
    "# Examine the index\n",
    "print(ri.index)\n",
    "\n",
    "# Examine the columns\n",
    "print(ri.columns)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c6cff11",
   "metadata": {},
   "source": [
    "Congratulations! Now that you have cleaned the dataset, you can begin analyzing it in the next chapter."
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
