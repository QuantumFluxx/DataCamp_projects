{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8b65faa8",
   "metadata": {},
   "source": [
    "# Combining Dates and Times\n",
    "\n",
    "## Creating datetimes by hand\n",
    "Often you create datetime objects based on outside data. Sometimes though, you want to create a datetime object from scratch.\n",
    "\n",
    "You're going to create a few different datetime objects from scratch to get the hang of that process. These come from the bikeshare data set that you'll use throughout the rest of the chapter.\n",
    "\n",
    "* Import the `datetime` class.\n",
    "* Create a datetime for October 1, 2017 at 15:26:26.\n",
    "* Print the results in ISO format."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dfbfd4b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-10-01T15:26:26\n"
     ]
    }
   ],
   "source": [
    "# Import datetime\n",
    "from datetime import datetime\n",
    "\n",
    "# Create a datetime object\n",
    "dt = datetime(2017, 10, 1, 15, 26, 26)\n",
    "\n",
    "# Print the results in ISO 8601 format\n",
    "print(dt.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f102778",
   "metadata": {},
   "source": [
    "* Import the `datetime` class.\n",
    "* Create a datetime for December 31, 2017 at 15:19:13.\n",
    "* Print the results in ISO format."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fb7b4b78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-12-31T15:19:13\n"
     ]
    }
   ],
   "source": [
    "# Import datetime\n",
    "# from datetime import datetime\n",
    "\n",
    "# Create a datetime object\n",
    "dt = datetime(2017, 12, 31, 15, 19, 13)\n",
    "\n",
    "# Print the results in ISO 8601 format\n",
    "print(dt.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a2208c8",
   "metadata": {},
   "source": [
    "* Create a new datetime by replacing the year in dt with 1917 (instead of 2017)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a4269153",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1917-12-31 15:19:13\n"
     ]
    }
   ],
   "source": [
    "# Replace the year with 1917\n",
    "dt_old = dt.replace(year=1917)\n",
    "\n",
    "# Print the results in ISO 8601 format\n",
    "print(dt_old)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ce17317",
   "metadata": {},
   "source": [
    "Well done! You can now create datetime objects.\n",
    "\n",
    "## Counting events before and after noon\n",
    "In this chapter, you will be working with a list of all bike trips for one Capital Bikeshare bike, W20529, from October 1, 2017 to December 31, 2017. This list has been loaded as `onebike_datetimes`.\n",
    "\n",
    "Each element of the list is a dictionary with two entries: start is a datetime object corresponding to the start of a trip (when a bike is removed from the dock) and end is a datetime object corresponding to the end of a trip (when a bike is put back into a dock).\n",
    "\n",
    "You can use this data set to understand better how this bike was used. Did more trips start before noon or after noon?\n",
    "\n",
    "* Within the for loop, complete the if statement to check if the trip started before noon.\n",
    "* Within the for loop, increment `trip_counts['AM']` if the trip started before noon, and `trip_counts['PM']` if it started after noon."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "35fac0e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "onebike_datetimes = pd.read_csv('datasets/capital-onebike.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b536ba98",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create dictionary to hold results\n",
    "trip_counts = {'AM': 0, 'PM': 0}\n",
    "  \n",
    "# Loop over all trips\n",
    "for trip in onebike_datetimes:\n",
    "  # Check to see if the trip starts before noon\n",
    "    if trip['start'].hour < 12:\n",
    "    # Increment the counter for before noon\n",
    "        trip_counts['AM'] += 1\n",
    "    else:\n",
    "    # Increment the counter for after noon\n",
    "        trip_counts['PM'] += 1\n",
    "  \n",
    "print(trip_counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca5a2f88",
   "metadata": {},
   "source": [
    "Great! It looks like this bike is used about twice as much after noon than it is before noon. One obvious follow up would be to see which hours the bike is most likely to be taken out for a ride.\n",
    "\n",
    "## Turning strings into datetimes\n",
    "When you download data from the Internet, dates and times usually come to you as strings. Often the first step is to turn those strings into datetime objects.\n",
    "\n",
    "In this exercise, you will practice this transformation.\n",
    "```\n",
    "Reference\t\n",
    "%Y\t4 digit year (0000-9999)\n",
    "%m\t2 digit month (1-12)\n",
    "%d\t2 digit day (1-31)\n",
    "%H\t2 digit hour (0-23)\n",
    "%M\t2 digit minute (0-59)\n",
    "%S\t2 digit second (0-59)\n",
    "```\n",
    "\n",
    "* Determine the format needed to convert s to datetime and assign it to fmt.\n",
    "* Convert the string s to datetime using fmt."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e64d891c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-02-03 00:00:01\n"
     ]
    }
   ],
   "source": [
    "# Import the datetime class\n",
    "# from datetime import datetime\n",
    "\n",
    "# Starting string, in YYYY-MM-DD HH:MM:SS format\n",
    "s = '2017-02-03 00:00:01'\n",
    "\n",
    "# Write a format string to parse s\n",
    "fmt = '%Y-%m-%d %H:%M:%S'\n",
    "\n",
    "# Create a datetime object d\n",
    "d = datetime.strptime(s, fmt)\n",
    "\n",
    "# Print d\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b93095d",
   "metadata": {},
   "source": [
    "* Determine the format needed to convert s to datetime and assign it to fmt.\n",
    "* Convert the string s to datetime using fmt."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "085ce571",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2030-10-15 00:00:00\n"
     ]
    }
   ],
   "source": [
    "# Starting string, in YYYY-MM-DD format\n",
    "s = '2030-10-15'\n",
    "\n",
    "# Write a format string to parse s\n",
    "fmt = '%Y-%m-%d'\n",
    "\n",
    "# Create a datetime object d\n",
    "d = datetime.strptime(s, fmt)\n",
    "\n",
    "# Print d\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b4b2298",
   "metadata": {},
   "source": [
    "* Determine the format needed to convert s to datetime and assign it to fmt.\n",
    "* Convert the string s to datetime using fmt."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "83bf4445",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1986-12-15 08:00:00\n"
     ]
    }
   ],
   "source": [
    "# Starting string, in MM/DD/YYYY HH:MM:SS format\n",
    "s = '12/15/1986 08:00:00'\n",
    "\n",
    "# Write a format string to parse s\n",
    "fmt = '%m/%d/%Y %H:%M:%S'\n",
    "\n",
    "# Create a datetime object d\n",
    "d = datetime.strptime(s, fmt)\n",
    "\n",
    "# Print d\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8d58f10",
   "metadata": {},
   "source": [
    "Great! Now you can parse dates in most common formats. Unfortunately, Python does not have the ability to parse non-zero-padded dates and times out of the box (such as 1/2/2018). If needed, you can use other string methods to create zero-padded strings suitable for strptime().\n",
    "\n",
    "## Parsing pairs of strings as datetimes\n",
    "Up until now, you've been working with a pre-processed list of datetimes for W20529's trips. For this exercise, you're going to go one step back in the data cleaning pipeline and work with the strings that the data started as.\n",
    "\n",
    "Explore `onebike_datetime_strings` in the IPython shell to determine the correct format. datetime has already been loaded for you.\n",
    "```\n",
    "Reference\t\n",
    "%Y\t4 digit year (0000-9999)\n",
    "%m\t2 digit month (1-12)\n",
    "%d\t2 digit day (1-31)\n",
    "%H\t2 digit hour (0-23)\n",
    "%M\t2 digit minute (0-59)\n",
    "%S\t2 digit second (0-59)\n",
    "```\n",
    "\n",
    "* Outside the for loop, fill out the fmt string with the correct parsing format for the data.\n",
    "* Within the for loop, parse the start and end strings into the trip dictionary with start and end keys and datetime objects for values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37b0f4a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write down the format string\n",
    "fmt = \"%Y-%m-%d %H:%M:%S\"\n",
    "\n",
    "# Initialize a list for holding the pairs of datetime objects\n",
    "onebike_datetimes = []\n",
    "\n",
    "# Loop over all trips\n",
    "for (start, end) in onebike_datetime_strings:\n",
    "    trip = {'start': datetime.strptime(start, fmt),\n",
    "            'end': datetime.strptime(end, fmt)}\n",
    "  \n",
    "    # Append the trip\n",
    "    onebike_datetimes.append(trip)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45812a16",
   "metadata": {},
   "source": [
    "Excellent! Now you know how to process lists of strings into a more useful structure. If you haven't come across this approach before, many complex data cleaning tasks follow this same format: start with a list, process each element, and add the processed data to a new list.\n",
    "\n",
    "## Recreating ISO format with strftime()\n",
    "In the last chapter, you used `strftime()` to create strings from date objects. Now that you know about datetime objects, let's practice doing something similar.\n",
    "\n",
    "Re-create the `.isoformat()` method, using `.strftime()`, and print the first trip start in our data set.\n",
    "```\n",
    "Reference\t\n",
    "%Y\t4 digit year (0000-9999)\n",
    "%m\t2 digit month (1-12)\n",
    "%d\t2 digit day (1-31)\n",
    "%H\t2 digit hour (0-23)\n",
    "%M\t2 digit minute (0-59)\n",
    "%S\t2 digit second (0-59)\n",
    "```\n",
    "\n",
    "* Complete fmt to match the format of ISO 8601.\n",
    "* Print `first_start` with both `.isoformat()` and `.strftime()`; they should match."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a55f2618",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import datetime\n",
    "from datetime import datetime\n",
    "\n",
    "# Pull out the start of the first trip\n",
    "first_start = onebike_datetimes[0]['start']\n",
    "\n",
    "# Format to feed to strftime()\n",
    "fmt = \"%Y-%m-%dT%H:%M:%S\"\n",
    "\n",
    "# Print out date with .isoformat(), then with .strftime() to compare\n",
    "print(first_start.isoformat())\n",
    "print(first_start.strftime(fmt))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4788648",
   "metadata": {},
   "source": [
    "Awesome! There are a wide variety of time formats you can create with strftime(), depending on your needs. However, if you don't know exactly what you need, .isoformat() is a perfectly fine place to start.\n",
    "\n",
    "## Unix timestamps\n",
    "Datetimes are sometimes stored as Unix timestamps: the number of seconds since January 1, 1970. This is especially common with computer infrastructure, like the log files that websites keep when they get visitors.\n",
    "\n",
    "* Complete the for loop to loop over `timestamps`.\n",
    "* Complete the code to turn each timestamp ts into a datetime."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a87f66b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[datetime.datetime(2017, 12, 30, 23, 19, 13), datetime.datetime(2017, 12, 30, 23, 9, 3)]\n"
     ]
    }
   ],
   "source": [
    "# Starting timestamps\n",
    "timestamps = [1514665153, 1514664543]\n",
    "\n",
    "# Datetime objects\n",
    "dts = []\n",
    "\n",
    "# Loop\n",
    "for ts in timestamps:\n",
    "    dts.append(datetime.fromtimestamp(ts))\n",
    "\n",
    "# Print results\n",
    "print(dts)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91a2ec5f",
   "metadata": {},
   "source": [
    "Nice! The largest number that some older computers can hold in one variable is 2147483648, which as a Unix timestamp is in January 2038. On that day, many computers which haven't been upgraded will fail. Hopefully, none of them are running anything critical!\n",
    "\n",
    "## Turning pairs of datetimes into durations\n",
    "When working with timestamps, we often want to know how much time has elapsed between events. Thankfully, we can use datetime arithmetic to ask Python to do the heavy lifting for us so we don't need to worry about day, month, or year boundaries. Let's calculate the number of seconds that the bike was out of the dock for each trip.\n",
    "\n",
    "Continuing our work from a previous coding exercise, the bike trip data has been loaded as the list `onebike_datetimes`. Each element of the list consists of two datetime objects, corresponding to the start and end of a trip, respectively.\n",
    "\n",
    "* Use arithmetic on the start and end elements to find the length of the trip\n",
    "* Save the results to `trip_duration`.\n",
    "* Calculate `trip_length_seconds` from `trip_duration`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "655380b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize a list for all the trip durations\n",
    "onebike_durations = []\n",
    "\n",
    "for trip in onebike_datetimes:\n",
    "  # Create a timedelta object corresponding to the length of the trip\n",
    "    trip_duration = trip['end'] - trip['start']\n",
    "  \n",
    "  # Get the total elapsed seconds in trip_duration\n",
    "    trip_length_seconds = trip_duration.total_seconds()\n",
    "  \n",
    "  # Append the results to our list\n",
    "    onebike_durations.append(trip_length_seconds)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "965806b1",
   "metadata": {},
   "source": [
    "Success! Remember that timedelta objects are represented in Python as a number of days and seconds of elapsed time. Be careful not to use .seconds on a timedelta object, since you'll just get the number of seconds without the days!\n",
    "\n",
    "## Average trip time\n",
    "W20529 took 291 trips in our data set. How long were the trips on average? We can use the built-in Python functions `sum()` and `len()` to make this calculation.\n",
    "\n",
    "Based on your last coding exercise, the data has been loaded as onebike_durations. Each entry is a number of seconds that the bike was out of the dock.\n",
    "\n",
    "* Calculate `total_elapsed_time` across all trips in onebike_durations.\n",
    "* Calculate `number_of_trips` for `onebike_durations`.\n",
    "* Divide `total_elapsed_time` by `number_of_trips` to get the average trip length."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cb5ebf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# What was the total duration of all trips?\n",
    "total_elapsed_time = sum(onebike_durations)\n",
    "\n",
    "# What was the total number of trips?\n",
    "number_of_trips = len(onebike_durations)\n",
    "  \n",
    "# Divide the total duration by the number of trips\n",
    "print(total_elapsed_time / number_of_trips)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d4a733c",
   "metadata": {},
   "source": [
    "Great work, and not remotely average! For the average to be a helpful summary of the data, we need for all of our durations to be reasonable numbers, and not a few that are way too big, way too small, or even malformed. For example, if there is anything fishy happening in the data, and our trip ended before it started, we'd have a negative trip length.\n",
    "\n",
    "## The long and the short of why time is hard\n",
    "Out of 291 trips taken by W20529, how long was the longest? How short was the shortest? Does anything look fishy?\n",
    "\n",
    "As before, data has been loaded as `onebike_durations`.\n",
    "\n",
    "* Calculate `shortest_trip` from `onebike_durations`.\n",
    "* Calculate `longest_trip` from `onebike_durations`.\n",
    "* Print the results, turning `shortest_trip` and `longest_trip` into strings so they can print."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdc9ec49",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate shortest and longest trips\n",
    "shortest_trip = min(onebike_durations)\n",
    "longest_trip = max(onebike_durations)\n",
    "\n",
    "# Print out the results\n",
    "print(\"The shortest trip was \" + str(shortest_trip) + \" seconds\")\n",
    "print(\"The longest trip was \" + str(longest_trip) + \" seconds\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "528c2286",
   "metadata": {},
   "source": [
    "Weird huh?! For at least one trip, the bike returned before it left. Why could that be? Here's a hint: it happened in early November, around 2AM local time. What happens to clocks around that time each year? By the end of the next chapter, we'll have all the tools we need to deal with this situation!"
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
