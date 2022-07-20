{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e5c687ad",
   "metadata": {},
   "source": [
    "# Time Zones and Daylight Saving\n",
    "\n",
    "## Creating timezone aware datetimes\n",
    "In this exercise, you will practice setting timezones manually.\n",
    "\n",
    "* Import `timezone`.\n",
    "* Set the tzinfo to UTC, without using timedelta."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fdb5c833",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-10-01T15:26:26+00:00\n"
     ]
    }
   ],
   "source": [
    "# Import datetime, timezone\n",
    "from datetime import datetime, timezone\n",
    "\n",
    "# October 1, 2017 at 15:26:26, UTC\n",
    "dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)\n",
    "\n",
    "# Print results\n",
    "print(dt.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd1f374b",
   "metadata": {},
   "source": [
    "* Set `pst` to be a timezone set for `UTC-8`.\n",
    "* Set `dt's` timezone to be `pst`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ba113570",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-10-01T15:26:26-08:00\n"
     ]
    }
   ],
   "source": [
    "# Import datetime, timedelta, timezone\n",
    "from datetime import datetime, timedelta, timezone\n",
    "\n",
    "# Create a timezone for Pacific Standard Time, or UTC-8\n",
    "pst = timezone(timedelta(hours=-8))\n",
    "\n",
    "# October 1, 2017 at 15:26:26, UTC-8\n",
    "dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)\n",
    "\n",
    "# Print results\n",
    "print(dt.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "841f1e11",
   "metadata": {},
   "source": [
    "* Set `aedt` to be a timezone set for `UTC+11`.\n",
    "* Set `dt's` timezone to be `aedt`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0edc466a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-10-01T15:26:26+11:00\n"
     ]
    }
   ],
   "source": [
    "# Create a timezone for Australian Eastern Daylight Time, or UTC+11\n",
    "aedt = timezone(timedelta(hours=11))\n",
    "\n",
    "# October 1, 2017 at 15:26:26, UTC+11\n",
    "dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)\n",
    "\n",
    "# Print results\n",
    "print(dt.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bacb2a3",
   "metadata": {},
   "source": [
    "Great! Did you know that Russia and France are tied for the most number of time zones, with 12 each? The French mainland only has one timezone, but because France has so many overseas dependencies they really add up!\n",
    "\n",
    "## Setting timezones\n",
    "Now that you have the hang of setting timezones one at a time, let's look at setting them for the first ten trips that W20529 took.\n",
    "\n",
    "`timezone` and `timedelta` have already been imported. Make the change using `.replace()`\n",
    "\n",
    "* Create `edt`, a timezone object whose UTC offset is -4 hours.\n",
    "* Within the for loop:\n",
    "* Set the tzinfo for `trip['start']`.\n",
    "* Set the tzinfo for `trip['end']`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "422d9733",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a timezone object corresponding to UTC-4\n",
    "edt = timezone(timedelta(hours=-4))\n",
    "\n",
    "# Loop over trips, updating the start and end datetimes to be in UTC-4\n",
    "for trip in onebike_datetimes[:10]:\n",
    "    # Update trip['start'] and trip['end']\n",
    "    trip['start'] = trip['start'].replace(tzinfo = edt)\n",
    "    trip['end'] = trip['end'].replace(tzinfo = edt)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac0caf89",
   "metadata": {},
   "source": [
    "Awesome! Did you know that despite being over 2,500 miles (4,200 km) wide (about as wide as the continential United States or the European Union) China has only one official timezone? There's a second, unofficial timezone, too. It is used by much of the Uyghurs population in the Xinjiang province in the far west of China.\n",
    "\n",
    "## What time did the bike leave in UTC?\n",
    "Having set the timezone for the first ten rides that W20529 took, let's see what time the bike left in UTC. We've already loaded the results of the previous exercise into memory.\n",
    "\n",
    "* Within the for loop, move dt to be in UTC. Use `timezone.utc` as a convenient shortcut for UTC."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0224f8c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop over the trips\n",
    "for trip in onebike_datetimes[:10]:\n",
    "    # Pull out the start\n",
    "    dt = trip['start']\n",
    "    # Move dt to be in UTC\n",
    "    dt = dt.astimezone(timezone.utc)\n",
    "  \n",
    "    # Print the start time in UTC\n",
    "    print('Original:', trip['start'], '| UTC:', dt.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1c2cfcc",
   "metadata": {},
   "source": [
    "Excellent! Did you know that there is no official time zone at the North or South pole? Since all the lines of longitude meet each other, it's up to each traveler (or research station) to decide what time they want to use.\n",
    "\n",
    "## Putting the bike trips into the right time zone\n",
    "Instead of setting the timezones for W20529 by hand, let's assign them to their IANA timezone: 'America/New_York'. Since we know their political jurisdiction, we don't need to look up their UTC offset. Python will do that for us.\n",
    "\n",
    "* Import `tz` from `dateutil`.\n",
    "* Assign et to be the timezone 'America/New_York'.\n",
    "* Within the for loop, set start and end to have et as their timezone (use `.replace()`)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f0ac6ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import tz\n",
    "from dateutil import tz\n",
    "\n",
    "# Create a timezone object for Eastern Time\n",
    "et = tz.gettz('America/New_York')\n",
    "\n",
    "# Loop over trips, updating the datetimes to be in Eastern Time\n",
    "for trip in onebike_datetimes[:10]:\n",
    "    # Update trip['start'] and trip['end']\n",
    "    trip['start'] = trip['start'].replace(tzinfo = et)\n",
    "    trip['end'] = trip['end'].replace(tzinfo = et)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e2b097c",
   "metadata": {},
   "source": [
    "Great! Time zone rules actually change quite frequently. IANA time zone data gets updated every 3-4 months, as different jurisdictions make changes to their laws about time or as more historical information about timezones are uncovered. tz is smart enough to use the date in your datetime to determine which rules to use historically.\n",
    "\n",
    "## What time did the bike leave? (Global edition)\n",
    "When you need to move a datetime from one timezone into another, use `.astimezone()` and `tz`. Often you will be moving things into UTC, but for fun let's try moving things from 'America/New_York' into a few different time zones.\n",
    "\n",
    "* Set uk to be the timezone for the UK: 'Europe/London'.\n",
    "* Change local to be in the uk timezone and assign it to notlocal."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58cdd249",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the timezone object\n",
    "uk = tz.gettz('Europe/London')\n",
    "\n",
    "# Pull out the start of the first trip\n",
    "local = onebike_datetimes[0]['start']\n",
    "\n",
    "# What time was it in the UK?\n",
    "notlocal = local.astimezone(uk)\n",
    "\n",
    "# Print them out and see the difference\n",
    "print(local.isoformat())\n",
    "print(notlocal.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5525b1d",
   "metadata": {},
   "source": [
    "* Set ist to be the timezone for India: 'Asia/Kolkata'.\n",
    "* Change local to be in the ist timezone and assign it to notlocal."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70660d7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the timezone object\n",
    "ist = tz.gettz('Asia/Kolkata')\n",
    "\n",
    "# Pull out the start of the first trip\n",
    "local = onebike_datetimes[0]['start']\n",
    "\n",
    "# What time was it in the UK?\n",
    "notlocal = local.astimezone(ist)\n",
    "\n",
    "# Print them out and see the difference\n",
    "print(local.isoformat())\n",
    "print(notlocal.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "258f8f92",
   "metadata": {},
   "source": [
    "* Set sm to be the timezone for Samoa: 'Pacific/Apia'.\n",
    "* Change local to be in the sm timezone and assign it to notlocal."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "138fe639",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the timezone object\n",
    "sm = tz.gettz('Pacific/Apia')\n",
    "\n",
    "# Pull out the start of the first trip\n",
    "local = onebike_datetimes[0]['start']\n",
    "\n",
    "# What time was it in Samoa?\n",
    "notlocal = local.astimezone(sm)\n",
    "\n",
    "# Print them out and see the difference\n",
    "print(local.isoformat())\n",
    "print(notlocal.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4bd2ec26",
   "metadata": {},
   "source": [
    "Did you notice the time offset for this one? It's at UTC+14! Samoa used to be UTC-10, but in 2011 it changed to the other side of the International Date Line to better match New Zealand, its closest trading partner. However, they wanted to keep the clocks the same, so the UTC offset shifted from -10 to +14, since 24-10 is 14. Timezones... not simple!\n",
    "\n",
    "## How many hours elapsed around daylight saving?\n",
    "Since our bike data takes place in the fall, you'll have to do something else to learn about the start of daylight savings time.\n",
    "\n",
    "Let's look at March 12, 2017, in the Eastern United States, when Daylight Saving kicked in at 2 AM.\n",
    "\n",
    "If you create a `datetime` for midnight that night, and add 6 hours to it, how much time will have elapsed?\n",
    "\n",
    "* You already have a datetime called start, set for March 12, 2017 at midnight, set to the timezone 'America/New_York'.\n",
    "* Add six hours to start and assign it to end. Look at the UTC offset for the two results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ca998924",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-03-12T00:00:00-05:00 to 2017-03-12T06:00:00-04:00\n"
     ]
    }
   ],
   "source": [
    "# Import datetime, timedelta, tz, timezone\n",
    "from datetime import datetime, timedelta, timezone\n",
    "from dateutil import tz\n",
    "\n",
    "# Start on March 12, 2017, midnight, then add 6 hours\n",
    "start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))\n",
    "end = start + timedelta(hours=6)\n",
    "print(start.isoformat() + \" to \" + end.isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b50fb0d4",
   "metadata": {},
   "source": [
    "You added 6 hours, and got 6 AM, despite the fact that the clocks springing forward means only 5 hours would have actually elapsed!\n",
    "\n",
    "Calculate the time between start and end. How much time does Python think has elapsed?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bab114ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6.0\n"
     ]
    }
   ],
   "source": [
    "# How many hours have elapsed?\n",
    "print((end - start).total_seconds()/(60*60))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9dfa9458",
   "metadata": {},
   "source": [
    "Move your `datetime` objects into UTC and calculate the elapsed time again.\n",
    "\n",
    "Once you're in UTC, what result do you get?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f71a247e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0\n"
     ]
    }
   ],
   "source": [
    "# What if we move to UTC?\n",
    "print((end.astimezone(timezone.utc) - start.astimezone(timezone.utc))\\\n",
    "      .total_seconds()/(60*60))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9e8f670",
   "metadata": {},
   "source": [
    "When we compare times in local time zones, everything gets converted into clock time. Remember if you want to get absolute time differences, always move to UTC!\n",
    "\n",
    "## March 29, throughout a decade\n",
    "Daylight Saving rules are complicated: they're different in different places, they change over time, and they usually start on a Sunday (and so they move around the calendar).\n",
    "\n",
    "For example, in the United Kingdom, as of the time this lesson was written, Daylight Saving begins on the last Sunday in March. Let's look at the UTC offset for March 29, at midnight, for the years 2000 to 2010.\n",
    "\n",
    "* Using `tz`, set the timezone for dt to be 'Europe/London'.\n",
    "* Within the for loop:\n",
    "  + Use the `.replace()` method to change the year for dt to be y.\n",
    "  + Call `.isoformat()` on the result to observe the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "33108e25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2000-03-29T00:00:00+01:00\n",
      "2001-03-29T00:00:00+01:00\n",
      "2002-03-29T00:00:00+00:00\n",
      "2003-03-29T00:00:00+00:00\n",
      "2004-03-29T00:00:00+01:00\n",
      "2005-03-29T00:00:00+01:00\n",
      "2006-03-29T00:00:00+01:00\n",
      "2007-03-29T00:00:00+01:00\n",
      "2008-03-29T00:00:00+00:00\n",
      "2009-03-29T00:00:00+00:00\n",
      "2010-03-29T00:00:00+01:00\n"
     ]
    }
   ],
   "source": [
    "# Create starting date\n",
    "dt = datetime(2000, 3, 29, tzinfo = tz.gettz('Europe/London'))\n",
    "\n",
    "# Loop over the dates, replacing the year, and print the ISO timestamp\n",
    "for y in range(2000, 2011):\n",
    "    print(dt.replace(year=y).isoformat())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03d4892d",
   "metadata": {},
   "source": [
    "Nice! As you can see, the rules for Daylight Saving are not trivial. When in doubt, always use tz instead of hand-rolling timezones, so it will catch the Daylight Saving rules (and rule changes!) for you.\n",
    "\n",
    "## Finding ambiguous datetimes\n",
    "At the end of lesson 2, we saw something anomalous in our bike trip duration data. Let's see if we can identify what the problem might be.\n",
    "\n",
    "The data is loaded as `onebike_datetimes`, and tz has already been imported from dateutil.\n",
    "\n",
    "* Loop over the trips in `onebike_datetimes`:\n",
    "  + Print any rides whose start is ambiguous.\n",
    "  + Print any rides whose end is ambiguous."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4d2f797",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop over trips\n",
    "for trip in onebike_datetimes:\n",
    "    # Rides with ambiguous start\n",
    "    if tz.datetime_ambiguous(trip['start']):\n",
    "        print(\"Ambiguous start at \" + str(trip['start']))\n",
    "    # Rides with ambiguous end\n",
    "    if tz.datetime_ambiguous(trip['end']):\n",
    "        print(\"Ambiguous end at \" + str(trip['end']))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02e24037",
   "metadata": {},
   "source": [
    "Good work! Avoid ambiguous datetimes in practice by storing datetimes in UTC.\n",
    "\n",
    "## Cleaning daylight saving data with fold\n",
    "As we've just discovered, there is a ride in our data set which is being messed up by a Daylight Savings shift. Let's clean up the data set so we actually have a correct minimum ride length. We can use the fact that we know the end of the ride happened after the beginning to fix up the duration messed up by the shift out of Daylight Savings.\n",
    "\n",
    "Since Python does not handle `tz.enfold()` when doing arithmetic, we must put our datetime objects into UTC, where ambiguities have been resolved.\n",
    "\n",
    "`onebike_datetimes` is already loaded and in the right timezone. tz and timezone have been imported. Use tz.UTC for the timezone.\n",
    "\n",
    "* Complete the if statement to be true only when a ride's start comes after its end.\n",
    "* When start is after end, call `tz.enfold()` on the end so you know it refers to the one after the daylight savings time change.\n",
    "* After the if statement, convert the start and end to UTC so you can make a proper"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "044d222e",
   "metadata": {},
   "outputs": [],
   "source": [
    "trip_durations = []\n",
    "for trip in onebike_datetimes:\n",
    "    # When the start is later than the end, set the fold to be 1\n",
    "    if trip['start'] > trip['end']:\n",
    "        trip['end'] = tz.enfold(trip['end'])\n",
    "    # Convert to UTC\n",
    "    start = trip['start'].astimezone(tz.UTC)\n",
    "    end = trip['end'].astimezone(tz.UTC)\n",
    "\n",
    "    # Subtract the difference\n",
    "    trip_length_seconds = (end-start).total_seconds()\n",
    "    trip_durations.append(trip_length_seconds)\n",
    "\n",
    "# Take the shortest trip duration\n",
    "print(\"Shortest trip: \" + str(min(trip_durations)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8760638",
   "metadata": {},
   "source": [
    "Good work! Now you know how to handle some pretty gnarly edge cases in datetime data. To give a sense for how tricky these things are: we actually still don't know how long the rides are which only started or ended in our ambiguous hour but not both. If you're collecting data, store it in UTC or with a fixed UTC offset!"
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
