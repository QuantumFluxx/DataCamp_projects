{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "18e9c725",
   "metadata": {},
   "source": [
    "# Working with Dates and Times in Python\n",
    "\n",
    "##  Dates and Calendars\n",
    "\n",
    "## Which day of the week?\n",
    "Hurricane Andrew, which hit Florida on August 24, 1992, was one of the costliest and deadliest hurricanes in US history. Which day of the week did it make landfall?\n",
    "\n",
    "Let's walk through all of the steps to figure this out.\n",
    "\n",
    "* Import `date` from `datetime`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bd15540b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import date from datetime\n",
    "from datetime import date"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65d0254b",
   "metadata": {},
   "source": [
    "* Create a date object for August 24, 1992."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7a9c30e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a date object\n",
    "hurricane_andrew = date(1992, 8, 24)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eaa0d179",
   "metadata": {},
   "source": [
    "* Now ask Python what day of the week Hurricane Andrew hit (remember that Python counts days of the week starting from Monday as 0, Tuesday as 1, and so on)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9eddf64c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "# Which day of the week is the date?\n",
    "print(hurricane_andrew.weekday())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6df4e22",
   "metadata": {},
   "source": [
    "Great! What day does the week begin for you? It depends where you are from! In the United States, Canada, and Japan, Sunday is often considered the first day of the week. Everywhere else, it usually begins on Monday.\n",
    "\n",
    "## How many hurricanes come early?\n",
    "In this chapter, you will work with a list of the hurricanes that made landfall in Florida from 1950 to 2017. There were 235 in total. Check out the variable `florida_hurricane_dates`, which has all of these dates.\n",
    "\n",
    "Atlantic hurricane season officially begins on June 1. How many hurricanes since 1950 have made landfall in Florida before the official start of hurricane season?\n",
    "\n",
    "* Complete the `for` loop to iterate through `florida_hurricane_dates`.\n",
    "* Complete the if statement to increment the counter (early_hurricanes) if the hurricane made landfall before June."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f32bd1e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "florida_hurricane_dates = pd.read_pickle('datasets/florida_hurricane_dates.pkl')\n",
    "\n",
    "# Counter for how many before June 1\n",
    "early_hurricanes = 0\n",
    "\n",
    "# We loop over the dates\n",
    "for hurricane in florida_hurricane_dates:\n",
    "  # Check if the month is before June (month number 6)\n",
    "  if hurricane.month < 6:\n",
    "    early_hurricanes = early_hurricanes + 1\n",
    "    \n",
    "print(early_hurricanes)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5cb0422b",
   "metadata": {},
   "source": [
    "Great! Using this same pattern, you could do more complex counting by using .day, .year, .weekday(), and so on.\n",
    "\n",
    "## Subtracting dates\n",
    "Python date objects let us treat calendar dates as something similar to numbers: we can compare them, sort them, add, and even subtract them. This lets us do math with dates in a way that would be a pain to do by hand.\n",
    "\n",
    "The 2007 Florida hurricane season was one of the busiest on record, with 8 hurricanes in one year. The first one hit on May 9th, 2007, and the last one hit on December 13th, 2007. How many days elapsed between the first and last hurricane in 2007?\n",
    "\n",
    "* Import `date` from `datetime`.\n",
    "* Create a date object for May 9th, 2007, and assign it to the start variable.\n",
    "* Create a date object for December 13th, 2007, and assign it to the end variable.\n",
    "* Subtract start from end, to print the number of days in the resulting timedelta object."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "52db3767",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "218\n"
     ]
    }
   ],
   "source": [
    "# Import date\n",
    "# from datetime import date\n",
    "\n",
    "# Create a date object for May 9th, 2007\n",
    "start = date(2007, 5, 9)\n",
    "\n",
    "# Create a date object for December 13th, 2007\n",
    "end = date(2007, 12, 13)\n",
    "\n",
    "# Subtract the two dates and print the number of days\n",
    "print((end - start).days)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d730bfe",
   "metadata": {},
   "source": [
    "Good job! One thing to note: be careful using this technique for historical dates hundreds of years in the past. Our calendar systems have changed over time, and not every date from then would be the same day and month today.\n",
    "\n",
    "## Counting events per calendar month\n",
    "Hurricanes can make landfall in Florida throughout the year. As we've already discussed, some months are more hurricane-prone than others.\n",
    "\n",
    "Using `florida_hurricane_dates`, let's see how hurricanes in Florida were distributed across months throughout the year.\n",
    "\n",
    "We've created a dictionary called `hurricanes_each_month` to hold your counts and set the initial counts to zero. You will loop over the list of hurricanes, incrementing the correct month in `hurricanes_each_month` as you go, and then print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "09261451",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 0, 2: 1, 3: 0, 4: 1, 5: 8, 6: 32, 7: 21, 8: 49, 9: 70, 10: 43, 11: 9, 12: 1}\n"
     ]
    }
   ],
   "source": [
    "# A dictionary to count hurricanes per calendar month\n",
    "hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,\n",
    "                         7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}\n",
    "\n",
    "# Loop over all hurricanes\n",
    "for hurricane in florida_hurricane_dates:\n",
    "  # Pull out the month\n",
    "  month = hurricane.month\n",
    "  # Increment the count in your dictionary by one\n",
    "  hurricanes_each_month[month] += 1\n",
    "  \n",
    "print(hurricanes_each_month)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b1e43a1",
   "metadata": {},
   "source": [
    "Success! This illustrated a generally useful pattern for working with complex data: creating a dictionary, performing some operation on each element, and storing the results back in the dictionary.\n",
    "\n",
    "## Putting a list of dates in order\n",
    "Much like numbers and strings, date objects in Python can be put in order. Earlier dates come before later ones, and so we can sort a list of date objects from earliest to latest.\n",
    "\n",
    "What if our Florida hurricane dates had been scrambled? We've gone ahead and shuffled them so they're in random order and saved the results as dates_scrambled. Your job is to put them back in chronological order, and then print the first and last dates from this sorted list.\n",
    "\n",
    "* Print the first and last dates in `dates_scrambled`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f3ebff1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the first and last scrambled dates\n",
    "print(dates_scrambled[0])\n",
    "print(dates_scrambled[-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b92bfa10",
   "metadata": {},
   "source": [
    "* Sort `dates_scrambled` using Python's built-in `sorted()` function, and save the results to `dates_ordered`.\n",
    "* Print the first and last dates in `dates_ordered`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0faab226",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Put the dates in order\n",
    "dates_ordered = sorted(dates_scrambled)\n",
    "\n",
    "# Print the first and last ordered dates\n",
    "print(dates_ordered[0])\n",
    "print(dates_ordered[-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e27421e6",
   "metadata": {},
   "source": [
    "Excellent! You can use sorted() on several data types in Python, including sorting lists of numbers, lists of strings, or even lists of lists, which by default are compared on the first element.\n",
    "\n",
    "## Printing dates in a friendly format\n",
    "Because people may want to see dates in many different formats, Python comes with very flexible functions for turning date objects into strings.\n",
    "\n",
    "Let's see what event was recorded first in the Florida hurricane data set. In this exercise, you will format the earliest date in the `florida_hurricane_dates` list in two ways so you can decide which one you want to use: either the ISO standard or the typical US style."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "8fc02ca6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ISO: Our earliest hurricane date: 1950-08-31\n",
      "US: Our earliest hurricane date: 08/31/1950\n"
     ]
    }
   ],
   "source": [
    "# Assign the earliest date to first_date\n",
    "first_date = min(florida_hurricane_dates)\n",
    "\n",
    "# Convert to ISO and US formats\n",
    "iso = \"Our earliest hurricane date: \" + first_date.isoformat()\n",
    "us = \"Our earliest hurricane date: \" + first_date.strftime(\"%m/%d/%Y\")\n",
    "\n",
    "print(\"ISO: \" + iso)\n",
    "print(\"US: \" + us)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a55db6d",
   "metadata": {},
   "source": [
    "Correct! When in doubt, use the ISO format for dates. ISO dates are unambiguous. And if you sort them 'alphabetically', for example, in filenames, they will be in the correct order.\n",
    "\n",
    "## Representing dates in different ways\n",
    "date objects in Python have a great number of ways they can be printed out as strings. In some cases, you want to know the date in a clear, language-agnostic format. In other cases, you want something which can fit into a paragraph and flow naturally.\n",
    "\n",
    "Let's try printing out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall in Florida), in a number of different ways, to practice using the `.strftime()` method.\n",
    "\n",
    "A date object called andrew has already been created.\n",
    "\n",
    "* Print andrew in the format 'YYYY-MM'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "74b4db62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1992-08\n"
     ]
    }
   ],
   "source": [
    "# Import date\n",
    "# from datetime import date\n",
    "\n",
    "# Create a date object\n",
    "andrew = date(1992, 8, 26)\n",
    "\n",
    "# Print the date in the format 'YYYY-MM'\n",
    "print(andrew.strftime('%Y-%m'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e373e437",
   "metadata": {},
   "source": [
    "* Print andrew in the format 'MONTH (YYYY)', using %B for the month's full name, which in this case will be August."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5d05ed05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "August (1992)\n"
     ]
    }
   ],
   "source": [
    "# Print the date in the format 'MONTH (YYYY)'\n",
    "print(andrew.strftime('%B (%Y)'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c77cc365",
   "metadata": {},
   "source": [
    "* Print andrew in the format 'YYYY-DDD' (where DDD is the day of the year) using %j."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "750af118",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1992-239\n"
     ]
    }
   ],
   "source": [
    "# Print the date in the format 'YYYY-DDD'\n",
    "print(andrew.strftime('%Y-%j'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98570fd9",
   "metadata": {},
   "source": [
    "Nice! Pick the format that best matches your needs. For example, astronomers usually use the 'day number' out of 366 instead of the month and date, to avoid ambiguities between languages."
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
