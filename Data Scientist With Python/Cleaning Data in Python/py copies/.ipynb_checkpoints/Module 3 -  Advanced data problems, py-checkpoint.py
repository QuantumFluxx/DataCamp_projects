{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bb716563",
   "metadata": {},
   "source": [
    "# Advanced data problems\n",
    "\n",
    "## Ambiguous dates\n",
    "You have a DataFrame containing a subscription_date column that was collected from various sources with different Date formats such as YYYY-mm-dd and YYYY-dd-mm. What is the best way to unify the formats for ambiguous values such as 2019-04-07?\n",
    "\n",
    "\n",
    "* Set them to NA and drop them.\n",
    "\n",
    "* Infer the format of the data in question by checking the format of subsequent and previous values.\n",
    "\n",
    "* Infer the format from the original data source.\n",
    "\n",
    "* **All of the above are possible, as long as we investigate where our data comes from, and understand the dynamics affecting it before cleaning it.**\n",
    "\n",
    "Great work! Like most cleaning data tasks, ambiguous dates require a thorough understanding of where your data comes from. Diagnosing problems is the first step in finding the best solution!\n",
    "\n",
    "## Uniform currencies\n",
    "In this exercise and throughout this chapter, you will be working with a retail banking dataset stored in the banking DataFrame. The dataset contains data on the amount of money stored in accounts (acct_amount), their currency (acct_cur), amount invested (inv_amount), account opening date (account_opened), and last transaction date (last_transaction) that were consolidated from American and European branches.\n",
    "\n",
    "You are tasked with understanding the average account size and how investments vary by the size of account, however in order to produce this analysis accurately, you first need to unify the currency amount into dollars. The pandas package has been imported as pd, and the banking DataFrame is in your environment.\n",
    "\n",
    "* Find the rows of `acct_cur` in banking that are equal to 'euro' and store them in the variable `acct_eu`.\n",
    "* Find all the rows of `acct_amount` in banking that fit the `acct_eu` condition, and convert them to USD by multiplying them with 1.1.\n",
    "* Find all the rows of `acct_cur` in banking that fit the `acct_eu` condition, set them to 'dollar'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c2db72b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "banking = pd.read_csv('datasets/banking_dirty.csv')\n",
    "\n",
    "# Find values of acct_cur that are equal to 'euro'\n",
    "acct_eu = banking['acct_cur'] == 'euro'\n",
    "\n",
    "# Convert acct_amount where it is in euro to dollars\n",
    "banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1 \n",
    "\n",
    "# Unify acct_cur column by changing 'euro' values to 'dollar'\n",
    "banking.loc[acct_eu, 'acct_cur'] = 'dollar'\n",
    "\n",
    "# Assert that only dollar currency remains\n",
    "assert banking['acct_cur'].unique() == 'dollar'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00d610a3",
   "metadata": {},
   "source": [
    "Crafty currency conversion! With just a few lines of code, you made this column ready for analysis!\n",
    "\n",
    "## Uniform dates\n",
    "After having unified the currencies of your different account amounts, you want to add a temporal dimension to your analysis and see how customers have been investing their money given the size of their account over each year. The account_opened column represents when customers opened their accounts and is a good proxy for segmenting customer activity and investment over time.\n",
    "\n",
    "However, since this data was consolidated from multiple sources, you need to make sure that all dates are of the same format. You will do so by converting this column into a datetime object, while making sure that the format is inferred and potentially incorrect formats are set to missing. The banking DataFrame is in your environment and pandas was imported as pd.\n",
    "\n",
    "* Print the header of `account_opened` from the banking DataFrame and take a look at the different results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b01a9ebb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    02-09-18\n",
      "1    28-02-19\n",
      "2    25-04-18\n",
      "3    07-11-17\n",
      "4    14-05-18\n",
      "Name: account_opened, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Print the header of account_opened\n",
    "print(banking['account_opened'].head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc943355",
   "metadata": {},
   "source": [
    "Take a look at the output. You tried converting the values to datetime using the default to_datetime() function without changing any argument, however received the following error:\n",
    "```\n",
    "ValueError: month must be in 1..12\n",
    "```\n",
    "Why do you think that is?\n",
    "\n",
    "* The to_datetime() function needs to be explicitly told which date format each row is in.\n",
    "\n",
    "* The to_datetime() function can only be applied on YY-mm-dd date formats.\n",
    "\n",
    "* **The 21-14-17 entry is erroneous and leads to an error.**\n",
    "-------\n",
    "* Convert the `account_opened` column to datetime, while making sure the date format is inferred and that erroneous formats that raise error return a missing value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cbf5a075",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert account_opened to datetime\n",
    "banking['account_opened'] = pd.to_datetime(banking['account_opened'],\n",
    "                                           # Infer datetime format\n",
    "                                           infer_datetime_format = True,\n",
    "                                           # Return missing value for error\n",
    "                                           errors = 'coerce') "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28802891",
   "metadata": {},
   "source": [
    "* Extract the year from the amended `account_opened` column and assign it to the `acct_year` column.\n",
    "* Print the newly created `acct_year` column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b5d65f0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     2018\n",
      "1     2019\n",
      "2     2018\n",
      "3     2017\n",
      "4     2018\n",
      "      ... \n",
      "95    2018\n",
      "96    2017\n",
      "97    2017\n",
      "98    2017\n",
      "99    2017\n",
      "Name: acct_year, Length: 100, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Get year of account opened\n",
    "banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')\n",
    "\n",
    "# Print acct_year\n",
    "print(banking['acct_year'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "373dd8f8",
   "metadata": {},
   "source": [
    "Cunning calendar cleaning! Now that the acct_year column is created, a simple .groupby() will show you how accounts are opened on a yearly!\n",
    "\n",
    "## How's our data integrity?\n",
    "New data has been merged into the banking DataFrame that contains details on how investments in the `inv_amount` column are allocated across four different funds A, B, C and D.\n",
    "\n",
    "Furthermore, the age and birthdays of customers are now stored in the age and `birth_date` columns respectively.\n",
    "\n",
    "You want to understand how customers of different age groups invest. However, you want to first make sure the data you're analyzing is correct. You will do so by cross field checking values of `inv_amount` and age against the amount invested in different funds and customers' birthdays. Both pandas and datetime have been imported as pd and dt respectively.\n",
    "\n",
    "* Find the rows where the sum of all rows of the `fund_columns` in banking are equal to the `inv_amount` column.\n",
    "* Store the values of banking with consistent `inv_amount` in `consistent_inv`, and those with inconsistent ones in `inconsistent_inv`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5a81af0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of inconsistent investments:  8\n"
     ]
    }
   ],
   "source": [
    "# Store fund columns to sum against\n",
    "fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']\n",
    "\n",
    "# Find rows where fund_columns row sum == inv_amount\n",
    "inv_equ = banking[fund_columns].sum(axis = 1) == banking['inv_amount']\n",
    "\n",
    "# Store consistent and inconsistent data\n",
    "consistent_inv = banking[inv_equ]\n",
    "inconsistent_inv = banking[~inv_equ]\n",
    "\n",
    "# Store consistent and inconsistent data\n",
    "print(\"Number of inconsistent investments: \", inconsistent_inv.shape[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5984c51c",
   "metadata": {},
   "source": [
    "* Store today's date into today, and manually calculate customers' ages and store them in `ages_manual`.\n",
    "* Find all rows of banking where the age column is equal to ages_manual and then filter banking into `consistent_ages` and `inconsistent_ages`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ee32a51b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of inconsistent ages:  100\n"
     ]
    }
   ],
   "source": [
    "import datetime as dt\n",
    "\n",
    "# Store today's date and find ages\n",
    "today = dt.date.today()\n",
    "ages_manual = today.year - banking['birth_date'].dt.year\n",
    "\n",
    "# Find rows where age column == ages_manual\n",
    "age_equ = banking['Age'] == ages_manual\n",
    "\n",
    "# Store consistent and inconsistent data\n",
    "consistent_ages = banking[age_equ]\n",
    "inconsistent_ages = banking[~age_equ]\n",
    "\n",
    "# Store consistent and inconsistent data\n",
    "print(\"Number of inconsistent ages: \", inconsistent_ages.shape[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e62937e",
   "metadata": {},
   "source": [
    "Awesome work! There are only 8 and 4 rows affected by inconsistent inv_amount and age values, respectively. In this case, it's best to investigate the underlying data sources before deciding on a course of action!\n",
    "\n",
    "## Is this missing at random?\n",
    "You've seen in the video exercise how there are a variety of missingness types when observing missing data. As a reminder, missingness types can be described as the following:\n",
    "\n",
    "* Missing Completely at Random: No systematic relationship between a column's missing values and other or own values.\n",
    "* Missing at Random: There is a systematic relationship between a column's missing values and other observed values.\n",
    "* Missing not at Random: There is a systematic relationship between a column's missing values and unobserved values.\n",
    "\n",
    "You have a DataFrame containing customer satisfaction scores for a service. What type of missingness is the following?\n",
    "\n",
    "* Missing completely at random.\n",
    "\n",
    "* Missing at random.\n",
    "\n",
    "* **Missing not at random.**\n",
    "\n",
    "Awesome work! This is a clear example of missing not at random, where low values of satisfaction_score are missing because of inherently low satisfaction!\n",
    "\n",
    "## Missing investors\n",
    "Dealing with missing data is one of the most common tasks in data science. There are a variety of types of missingness, as well as a variety of types of solutions to missing data.\n",
    "\n",
    "You just received a new version of the banking DataFrame containing data on the amount held and invested for new and existing customers. However, there are rows with missing `inv_amount` values.\n",
    "\n",
    "You know for a fact that most customers below 25 do not have investment accounts yet, and suspect it could be driving the missingness. The pandas, missingno and matplotlib.pyplot packages have been imported as pd, msno and plt respectively. The banking DataFrame is in your environment.\n",
    "\n",
    "* Print the number of missing values by column in the `banking` DataFrame.\n",
    "* Plot and show the missingness matrix of banking with the `msno.matrix()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1f88c0ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unnamed: 0          0\n",
      "cust_id             0\n",
      "birth_date          0\n",
      "Age                 0\n",
      "acct_amount         0\n",
      "inv_amount          0\n",
      "fund_A              0\n",
      "fund_B              0\n",
      "fund_C              0\n",
      "fund_D              0\n",
      "account_opened      0\n",
      "last_transaction    0\n",
      "acct_year           0\n",
      "dtype: int64\n"
     ]
    },
    {
     "data": {
      "image/png": "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AABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAs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\n",
      "text/plain": [
       "<Figure size 1800x720 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import missingno as msno\n",
    "\n",
    "# Print number of missing values in banking\n",
    "print(banking.isna().sum())\n",
    "\n",
    "# Visualize missingness matrix\n",
    "msno.matrix(banking)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01a835a2",
   "metadata": {},
   "source": [
    "* Isolate the values of banking missing values of inv_amount into missing_investors and with non-missing `inv_amount` values into investors."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "16cd6add",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Isolate missing and non missing values of inv_amount\n",
    "missing_investors = banking[banking['inv_amount'].isna()]\n",
    "investors = banking[~banking['inv_amount'].isna()]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ff88b16",
   "metadata": {},
   "source": [
    "Now that you've isolated banking into investors and `missing_investors`, use the `.describe()` method on both of these DataFrames in the IPython shell to understand whether there are structural differences between them. What do you think is going on?\n",
    "\n",
    "* The data is missing completely at random and there are no drivers behind the missingness.\n",
    "\n",
    "* **The inv_amount is missing only for young customers, since the average age in missing_investors is 22 and the maximum age is 25.**\n",
    "\n",
    "* The inv_amount is missing only for old customers, since the average age in missing_investors is 42 and the maximum age is 59.\n",
    "\n",
    "------------\n",
    "\n",
    "* Sort the banking DataFrame by the age column and plot the missingness matrix of `banking_sorted`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8e15bdc5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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AABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAsCcABAAAAAJglATgAAAAAALMkAAcAAAAAYJYE4AAAAAAAzJIAHAAAAACAWRKAAwAAAAAwSwJwAAAAAABmSQAOAAAAAMAs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\n",
      "text/plain": [
       "<Figure size 1800x720 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Sort banking by age and visualize\n",
    "banking_sorted = banking.sort_values(by = 'Age')\n",
    "msno.matrix(banking_sorted)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5f6fe4c",
   "metadata": {},
   "source": [
    "Great job! Notice how all the white spaces for inv_amount are on top? Indeed missing values are only due to young bank account holders not investing their money! Better set it to 0 with .fillna().\n",
    "\n",
    "##  Follow the money\n",
    "In this exercise, you're working with another version of the banking DataFrame that contains missing values for both the `cust_id` column and the `acct_amount` column.\n",
    "\n",
    "You want to produce analysis on how many unique customers the bank has, the average amount held by customers and more. You know that rows with missing `cust_id` don't really help you, and that on average acct_amount is usually 5 times the amount of `inv_amount`.\n",
    "\n",
    "In this exercise, you will drop rows of banking with missing `cust_ids`, and impute missing values of `acct_amount` with some domain knowledge.\n",
    "\n",
    "* Use `.dropna()` to drop missing values of the `cust_id` column in banking and store the results in `banking_fullid`.\n",
    "* Use `inv_amount` to compute the estimated account amounts for `banking_fullid` by setting the amounts equal to `inv_amount * 5`, and assign the results to `acct_imp`.\n",
    "* Impute the missing values of `acct_amount` in `banking_fullid` with the newly created `acct_imp` using `.fillna()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "8844bd1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unnamed: 0          0\n",
      "cust_id             0\n",
      "birth_date          0\n",
      "Age                 0\n",
      "acct_amount         0\n",
      "inv_amount          0\n",
      "fund_A              0\n",
      "fund_B              0\n",
      "fund_C              0\n",
      "fund_D              0\n",
      "account_opened      0\n",
      "last_transaction    0\n",
      "acct_year           0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Drop missing values of cust_id\n",
    "banking_fullid = banking.dropna(subset = ['cust_id'])\n",
    "\n",
    "# Compute estimated acct_amount\n",
    "acct_imp = banking_fullid['inv_amount'] * 5\n",
    "\n",
    "# Impute missing acct_amount with corresponding acct_imp\n",
    "banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp})\n",
    "\n",
    "# Print number of missing values\n",
    "print(banking_imputed.isna().sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b554d68",
   "metadata": {},
   "source": [
    "Awesome work! As you can see no missing data left, you can definitely bank on getting your analysis right!"
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
