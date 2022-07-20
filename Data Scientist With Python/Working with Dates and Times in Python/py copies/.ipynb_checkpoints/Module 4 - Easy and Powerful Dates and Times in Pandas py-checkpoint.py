{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "981445ba",
   "metadata": {},
   "source": [
    "# Easy and Powerful: Dates and Times in Pandas\n",
    "\n",
    "## Loading a csv file in Pandas\n",
    "The `capital_onebike.csv` file covers the October, November and December rides of the Capital Bikeshare bike W20529.\n",
    "\n",
    "Here are the first two columns:\n",
    "```\n",
    "Start date\tEnd date\t...\n",
    "2017-10-01 15:23:25\t2017-10-01 15:26:26\t...\n",
    "2017-10-01 15:42:57\t2017-10-01 17:49:59\t...\n",
    "```\n",
    "\n",
    "* Import Pandas.\n",
    "* Complete the call to `read_csv()` so that it correctly parses the date columns Start date and End date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c4a96883",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Start date                        2017-10-01 15:23:25\n",
      "End date                          2017-10-01 15:26:26\n",
      "Start station number                            31038\n",
      "Start station                    Glebe Rd & 11th St N\n",
      "End station number                              31036\n",
      "End station             George Mason Dr & Wilson Blvd\n",
      "Bike number                                    W20529\n",
      "Member type                                    Member\n",
      "Name: 0, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Import pandas\n",
    "import pandas as pd\n",
    "\n",
    "# Load CSV into the rides variable\n",
    "rides = pd.read_csv('datasets/capital-onebike.csv', \n",
    "                    parse_dates = ['Start date', 'End date'])\n",
    "\n",
    "# Print the initial (0th) row\n",
    "print(rides.iloc[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54f4a201",
   "metadata": {},
   "source": [
    "Geat! Did you know that pandas has a pd.read_excel(), pd.read_json(), and even a pd.read_clipboard() function to read tabular data that you've copied from a document or website? Most have date parsing functionality too.\n",
    "\n",
    "## Making timedelta columns\n",
    "Earlier in this course, you wrote a loop to subtract datetime objects and determine how long our sample bike had been out of the docks. Now you'll do the same thing with Pandas.\n",
    "\n",
    "rides has already been loaded for you.\n",
    "\n",
    "* Subtract the Start date column from the End date column to get a Series of timedeltas; assign the result to `ride_durations`.\n",
    "* Convert `ride_durations` into seconds and assign the result to the 'Duration' column of rides."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c3dbe920",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     181.0\n",
      "1    7622.0\n",
      "2     343.0\n",
      "3    1278.0\n",
      "4    1277.0\n",
      "Name: Duration, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Subtract the start date from the end date\n",
    "ride_durations = rides['End date'] - rides['Start date']\n",
    "\n",
    "# Convert the results to seconds\n",
    "rides['Duration'] = ride_durations.dt.total_seconds()\n",
    "\n",
    "print(rides['Duration'].head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e400b8e",
   "metadata": {},
   "source": [
    "Great! Because Pandas supports method chaining, you could also perform this operation in one line: rides['Duration'] = (rides['End date'] - rides['Start date']).dt.total_seconds()\n",
    "\n",
    "## How many joyrides?\n",
    "Suppose you have a theory that some people take long bike rides before putting their bike back in the same dock. Let's call these rides \"joyrides\".\n",
    "\n",
    "You only have data on one bike, so while you can't draw any bigger conclusions, it's certainly worth a look.\n",
    "\n",
    "Are there many joyrides? How long were they in our data set? Use the median instead of the mean, because we know there are some very long trips in our data set that might skew the answer, and the median is less sensitive to outliers.\n",
    "\n",
    "* Create a Pandas Series which is True when Start station and End station are the same, and assign the result to joyrides.\n",
    "* Calculate the median duration of all rides.\n",
    "* Calculate the median duration of joyrides."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "cc734e24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6 rides were joyrides\n",
      "The median duration overall was 660.00 seconds\n",
      "The median duration for joyrides was 2642.50 seconds\n"
     ]
    }
   ],
   "source": [
    "# Create joyrides\n",
    "joyrides = (rides['Start station'] == rides['End station'])\n",
    "\n",
    "# Total number of joyrides\n",
    "print(\"{} rides were joyrides\".format(joyrides.sum()))\n",
    "\n",
    "# Median of all rides\n",
    "print(\"The median duration overall was {:.2f} seconds\"\\\n",
    "      .format(rides['Duration'].median()))\n",
    "\n",
    "# Median of joyrides\n",
    "print(\"The median duration for joyrides was {:.2f} seconds\"\\\n",
    "      .format(rides[joyrides]['Duration'].median()))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3537f1cd",
   "metadata": {},
   "source": [
    "Great work! Pandas makes analyses like these concise to write and reason about. Writing this as a for loop would have been more complex.\n",
    "\n",
    "## It's getting cold outside, W20529\n",
    "Washington, D.C. has mild weather overall, but the average high temperature in October (68ºF / 20ºC) is certainly higher than the average high temperature in December (47ºF / 8ºC). People also travel more in December, and they work fewer days so they commute less.\n",
    "\n",
    "How might the weather or the season have affected the length of bike trips?\n",
    "\n",
    "* Resample rides to the daily level, based on the Start date column.\n",
    "* Plot the `.size()` of each result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9c1a7c3d",
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
    "# Import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Resample rides to daily, take the size, plot the results\n",
    "rides.resample('D', on = 'Start date')\\\n",
    "  .size()\\\n",
    "  .plot(ylim = [0, 15])\n",
    "\n",
    "# Show the results\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "611d5eab",
   "metadata": {},
   "source": [
    "* Since the daily time series is so noisy for this one bike, change the resampling to be monthly."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6d8af691",
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
    "# Resample rides to monthly, take the size, plot the results\n",
    "rides.resample('M', on = 'Start date')\\\n",
    "  .size()\\\n",
    "  .plot(ylim = [0, 150])\n",
    "\n",
    "# Show the results\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c18d462",
   "metadata": {},
   "source": [
    "Nice! As you can see, the pattern is clearer at the monthly level: there were fewer rides in November, and then fewer still in December, possibly because the temperature got colder.\n",
    "\n",
    "## Members vs casual riders over time\n",
    "Riders can either be \"Members\", meaning they pay yearly for the ability to take a bike at any time, or \"Casual\", meaning they pay at the kiosk attached to the bike dock.\n",
    "\n",
    "Do members and casual riders drop off at the same rate over October to December, or does one drop off faster than the other?\n",
    "\n",
    "As before, rides has been loaded for you. You're going to use the Pandas method `.value_counts()`, which returns the number of instances of each value in a Series. In this case, the counts of \"Member\" or \"Casual\".\n",
    "\n",
    "* Set monthly_rides to be a resampled version of rides, by month, based on start date.\n",
    "* Use the method `.value_counts()` to find out how many Member and Casual rides there were, and divide them by the total number of rides per month."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d5a4fddc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Start date  Member type\n",
      "2017-10-31  Member         0.768519\n",
      "            Casual         0.231481\n",
      "2017-11-30  Member         0.825243\n",
      "            Casual         0.174757\n",
      "2017-12-31  Member         0.860759\n",
      "            Casual         0.139241\n",
      "Name: Member type, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Resample rides to be monthly on the basis of Start date\n",
    "monthly_rides = rides.resample('M', on = 'Start date')['Member type']\n",
    "\n",
    "# Take the ratio of the .value_counts() over the total number of rides\n",
    "print(monthly_rides.value_counts() / monthly_rides.size())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00667fd3",
   "metadata": {},
   "source": [
    "Nice! Note that by default, .resample() labels Monthly resampling with the last day in the month and not the first. It certainly looks like the fraction of Casual riders went down as the number of rides dropped. With a little more digging, you could figure out if keeping Member rides only would be enough to stabilize the usage numbers throughout the fall.\n",
    "\n",
    "## Combining groupby() and resample()\n",
    "A very powerful method in Pandas is `.groupby()`. Whereas `.resample()` groups rows by some time or date information, `.groupby()` groups rows based on the values in one or more columns. For example, rides.groupby('Member type')`.size()` would tell us how many rides there were by member type in our entire DataFrame.\n",
    "\n",
    "`.resample()` can be called after `.groupby()`. For example, how long was the median ride by month, and by Membership type?\n",
    "\n",
    "* Complete the `groupby()` call to group by 'Member type', and the `.resample()` call to resample according to 'Start date', by month.\n",
    "* Print the median Duration for each group."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "04c29206",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Member type  Start date\n",
      "Casual       2017-10-31    1636.0\n",
      "             2017-11-30    1159.5\n",
      "             2017-12-31     850.0\n",
      "Member       2017-10-31     671.0\n",
      "             2017-11-30     655.0\n",
      "             2017-12-31     387.5\n",
      "Name: Duration, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Group rides by member type, and resample to the month\n",
    "grouped = rides.groupby('Member type')\\\n",
    "  .resample('M', on = 'Start date')\n",
    "\n",
    "# Print the median duration for each group\n",
    "print(grouped['Duration'].median())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f496ed9",
   "metadata": {},
   "source": [
    "Nice! It looks like casual riders consistently took longer rides, but that both groups took shorter rides as the months went by. Note that, by combining grouping and resampling, you can answer a lot of questions about nearly any data set that includes time as a feature. Keep in mind that you can also group by more than one column at once.\n",
    "\n",
    "## Timezones in Pandas\n",
    "Earlier in this course, you assigned a timezone to each datetime in a list. Now with Pandas you can do that with a single method call.\n",
    "\n",
    "(Note that, just as before, your data set actually includes some ambiguous datetimes on account of daylight saving; for now, we'll tell Pandas to not even try on those ones. Figuring them out would require more work.)\n",
    "\n",
    "* Make the Start date column timezone aware by localizing it to 'America/New_York' while ignoring any ambiguous datetimes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b678497f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-10-01 15:23:25-04:00\n"
     ]
    }
   ],
   "source": [
    "# Localize the Start date column to America/New_York\n",
    "rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', \n",
    "                                                        ambiguous='NaT')\n",
    "\n",
    "# Print first value\n",
    "print(rides['Start date'].iloc[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1715047",
   "metadata": {},
   "source": [
    "* Now switch the Start date column to the timezone 'Europe/London' using the `.dt.tz_convert()` method."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a263094d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-10-01 20:23:25+01:00\n"
     ]
    }
   ],
   "source": [
    "# Convert the Start date column to Europe/London\n",
    "rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')\n",
    "\n",
    "# Print the new value\n",
    "print(rides['Start date'].iloc[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54330df4",
   "metadata": {},
   "source": [
    "Nicely done! dt.tz_convert() converts to a new timezone, whereas dt.tz_localize() sets a timezone in the first place. You now know how to deal with datetimes in Pandas.\n",
    "\n",
    "## How long per weekday?\n",
    "Pandas has a number of datetime-related attributes within the `.dt` accessor. Many of them are ones you've encountered before, like `.dt.month`. Others are convenient and save time compared to standard Python, like `.dt.day_name()`.\n",
    "\n",
    "* Add a new column to rides called 'Ride start weekday', which is the weekday of the Start date.\n",
    "* Print the median ride duration for each weekday."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f6cc6116",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ride start weekday\n",
      "Friday       684.0\n",
      "Monday       922.5\n",
      "Saturday     610.0\n",
      "Sunday       625.0\n",
      "Thursday     659.0\n",
      "Tuesday      644.0\n",
      "Wednesday    629.0\n",
      "Name: Duration, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Add a column for the weekday of the start of the ride\n",
    "rides['Ride start weekday'] = rides['Start date'].dt.day_name()\n",
    "\n",
    "# Print the median trip time per weekday\n",
    "print(rides.groupby('Ride start weekday')['Duration'].median())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "843ef7db",
   "metadata": {},
   "source": [
    "Well done! There are .dt attributes for all of the common things you might want to pull out of a datetime, such as the day, month, year, hour, and so on, and also some additional convenience ones, such as quarter and week of the year out of 52.\n",
    "\n",
    "## How long between rides?\n",
    "For your final exercise, let's take advantage of Pandas indexing to do something interesting. How much time elapsed between rides?\n",
    "\n",
    "* Calculate the difference in the Start date of the current row and the End date of the previous row and assign it to `rides['Time since']`.\n",
    "* Convert `rides['Time since']` to seconds to make it easier to work with.\n",
    "* Resample rides to be in monthly buckets according to the Start date.\n",
    "* Divide the average by (60 * 60) to get the number of hours on average that W20529 waited in the dock before being picked up again."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7476c90",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Shift the index of the end date up one; now subract it from the start date\n",
    "rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))\n",
    "\n",
    "# Move from a timedelta to a number of seconds, which is easier to work with\n",
    "rides['Time since'] = rides['Time since'].dt.total_seconds()\n",
    "\n",
    "# Resample to the month\n",
    "monthly = rides.resample('M', on = 'Start date')\n",
    "\n",
    "# Print the average hours between rides each month\n",
    "print(monthly['Time since'].mean()/(60*60))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0e89964",
   "metadata": {},
   "source": [
    "Great job! As you can see, there are a huge number of Pandas tricks that let you express complex logic in just a few lines, assuming you understand how the indexes actually work."
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
