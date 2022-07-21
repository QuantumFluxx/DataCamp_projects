{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bb719ab9",
   "metadata": {},
   "source": [
    "# Exploring the relationship between gender and policing\n",
    "\n",
    "## Examining traffic violations\n",
    "Before comparing the violations being committed by each gender, you should examine the violations committed by all drivers to get a baseline understanding of the data.\n",
    "\n",
    "In this exercise, you'll count the unique values in the violation column, and then separately express those counts as proportions.\n",
    "\n",
    "* Count the unique values in the violation column of the ri DataFrame, to see what violations are being committed by all drivers.\n",
    "* Express the violation counts as proportions of the total."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7c82e395",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Speeding               48424\n",
      "Moving violation       16224\n",
      "Equipment              10922\n",
      "Other                   4410\n",
      "Registration/plates     3703\n",
      "Seat belt               2856\n",
      "Name: violation, dtype: int64\n",
      "Speeding               0.559563\n",
      "Moving violation       0.187476\n",
      "Equipment              0.126209\n",
      "Other                  0.050960\n",
      "Registration/plates    0.042790\n",
      "Seat belt              0.033002\n",
      "Name: violation, dtype: float64\n"
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
    "# Count the unique values in 'violation'\n",
    "print(ri.violation.value_counts())\n",
    "\n",
    "# Express the counts as proportions\n",
    "print(ri.violation.value_counts(normalize=True))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb4709e6",
   "metadata": {},
   "source": [
    "Interesting! More than half of all violations are for speeding, followed by other moving violations and equipment violations.\n",
    "\n",
    "## Comparing violations by gender\n",
    "The question we're trying to answer is whether male and female drivers tend to commit different types of traffic violations.\n",
    "\n",
    "In this exercise, you'll first create a DataFrame for each gender, and then analyze the violations in each DataFrame separately.\n",
    "\n",
    "* Create a DataFrame, female, that only contains rows in which `driver_gender` is 'F'.\n",
    "* Create a DataFrame, male, that only contains rows in which `driver_gender` is 'M'.\n",
    "* Count the violations committed by female drivers and express them as proportions.\n",
    "* Count the violations committed by male drivers and express them as proportions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "91373836",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Speeding               0.658114\n",
      "Moving violation       0.138218\n",
      "Equipment              0.105199\n",
      "Registration/plates    0.044418\n",
      "Other                  0.029738\n",
      "Seat belt              0.024312\n",
      "Name: violation, dtype: float64\n",
      "Speeding               0.522243\n",
      "Moving violation       0.206144\n",
      "Equipment              0.134158\n",
      "Other                  0.058985\n",
      "Registration/plates    0.042175\n",
      "Seat belt              0.036296\n",
      "Name: violation, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Create a DataFrame of female drivers\n",
    "female = ri[ri.driver_gender == 'F']\n",
    "\n",
    "# Create a DataFrame of male drivers\n",
    "male = ri[ri.driver_gender == 'M']\n",
    "\n",
    "# Compute the violations by female drivers (as proportions)\n",
    "print(female.violation.value_counts(normalize=True))\n",
    "\n",
    "# Compute the violations by male drivers (as proportions)\n",
    "print(male.violation.value_counts(normalize=True))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8cfbe273",
   "metadata": {},
   "source": [
    "About two-thirds of female traffic stops are for speeding, whereas stops of males are more balanced among the six categories. This doesn't mean that females speed more often than males, however, since we didn't take into account the number of stops or drivers.\n",
    "\n",
    "## Filtering by multiple conditions\n",
    "Which one of these commands would filter the ri DataFrame to only include female drivers who were stopped for a speeding violation?\n",
    "\n",
    "* ri[(ri.driver_gender = 'F') & (ri.violation = 'Speeding')]\n",
    "\n",
    "* ri[ri.driver_gender == 'F' & ri.violation == 'Speeding']\n",
    "\n",
    "* **ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]**\n",
    "\n",
    "* ri[(ri.driver_gender == 'F') | (ri.violation == 'Speeding')]\n",
    "\n",
    "* ri[(ri.driver_gender == 'F') and (ri.violation == 'Speeding')]\n",
    "\n",
    "Correct! We'll use this code to filter the DataFrame in the next exercise.\n",
    "\n",
    "## Comparing speeding outcomes by gender\n",
    "When a driver is pulled over for speeding, many people believe that gender has an impact on whether the driver will receive a ticket or a warning. Can you find evidence of this in the dataset?\n",
    "\n",
    "First, you'll create two DataFrames of drivers who were stopped for speeding: one containing females and the other containing males.\n",
    "\n",
    "Then, for each gender, you'll use the `stop_outcome` column to calculate what percentage of stops resulted in a \"Citation\" (meaning a ticket) versus a \"Warning\".\n",
    "\n",
    "* Create a DataFrame, `female_and_speeding`, that only includes female drivers who were stopped for speeding.\n",
    "* Create a DataFrame, `male_and_speeding`, that only includes male drivers who were stopped for speeding.\n",
    "* Count the stop outcomes for the female drivers and express them as proportions.\n",
    "* Count the stop outcomes for the male drivers and express them as proportions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5c981dd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Citation            0.952192\n",
      "Warning             0.040074\n",
      "Arrest Driver       0.005752\n",
      "N/D                 0.000959\n",
      "Arrest Passenger    0.000639\n",
      "No Action           0.000383\n",
      "Name: stop_outcome, dtype: float64\n",
      "Citation            0.944595\n",
      "Warning             0.036184\n",
      "Arrest Driver       0.015895\n",
      "Arrest Passenger    0.001281\n",
      "No Action           0.001068\n",
      "N/D                 0.000976\n",
      "Name: stop_outcome, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Create a DataFrame of female drivers stopped for speeding\n",
    "female_and_speeding = ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]\n",
    "\n",
    "# Create a DataFrame of male drivers stopped for speeding\n",
    "male_and_speeding = ri[(ri.driver_gender == 'M') & (ri.violation == 'Speeding')]\n",
    "\n",
    "# Compute the stop outcomes for female drivers (as proportions)\n",
    "print(female_and_speeding.stop_outcome.value_counts(normalize=True))\n",
    "\n",
    "# Compute the stop outcomes for male drivers (as proportions)\n",
    "print(male_and_speeding.stop_outcome.value_counts(normalize=True))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5341e2c8",
   "metadata": {},
   "source": [
    "Interesting! The numbers are similar for males and females: about 95% of stops for speeding result in a ticket. Thus, the data fails to show that gender has an impact on who gets a ticket for speeding.\n",
    "\n",
    "## Calculating the search rate\n",
    "During a traffic stop, the police officer sometimes conducts a search of the vehicle. In this exercise, you'll calculate the percentage of all stops in the ri DataFrame that result in a vehicle search, also known as the search rate.\n",
    "\n",
    "* Check the data type of `search_conducted` to confirm that it's a Boolean Series.\n",
    "* Calculate the search rate by counting the Series values and expressing them as proportions.\n",
    "* Calculate the search rate by taking the mean of the Series. (It should match the proportion of True values calculated above.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c225bf8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bool\n",
      "False    0.963953\n",
      "True     0.036047\n",
      "Name: search_conducted, dtype: float64\n",
      "0.03604713268876511\n"
     ]
    }
   ],
   "source": [
    "# Check the data type of 'search_conducted'\n",
    "print(ri.search_conducted.dtype)\n",
    "\n",
    "# Calculate the search rate by counting the values\n",
    "print(ri.search_conducted.value_counts(normalize=True))\n",
    "\n",
    "# Calculate the search rate by taking the mean\n",
    "print(ri.search_conducted.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9145d32c",
   "metadata": {},
   "source": [
    "Great! It looks like the search rate is about 3.8%. Next, you'll examine whether the search rate varies by driver gender.\n",
    "\n",
    "## Comparing search rates by gender\n",
    "In this exercise, you'll compare the rates at which female and male drivers are searched during a traffic stop. Remember that the vehicle search rate across all stops is about 3.8%.\n",
    "\n",
    "First, you'll filter the DataFrame by gender and calculate the search rate for each group separately. Then, you'll perform the same calculation for both genders at once using a `.groupby()`.\n",
    "\n",
    "* Filter the DataFrame to only include female drivers, and then calculate the search rate by taking the mean of `search_conducted`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "295e1e4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.019180617481282074\n"
     ]
    }
   ],
   "source": [
    "# Calculate the search rate for female drivers\n",
    "print(ri[ri.driver_gender == 'F'].search_conducted.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b537e688",
   "metadata": {},
   "source": [
    "* Filter the DataFrame to only include male drivers, and then repeat the search rate calculation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ade8ec5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.04542557598546892\n"
     ]
    }
   ],
   "source": [
    "# Calculate the search rate for male drivers\n",
    "print(ri[ri.driver_gender == 'M'].search_conducted.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f62471a2",
   "metadata": {},
   "source": [
    "* Group by driver gender to calculate the search rate for both groups simultaneously. (It should match the previous results.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "af1cf0b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "driver_gender\n",
      "F    0.019181\n",
      "M    0.045426\n",
      "Name: search_conducted, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate the search rate for both groups simultaneously\n",
    "print(ri.groupby('driver_gender').search_conducted.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a87d2d53",
   "metadata": {},
   "source": [
    "Wow! Male drivers are searched more than twice as often as female drivers. Why might this be?\n",
    "\n",
    "## Adding a second factor to the analysis\n",
    "Even though the search rate for males is much higher than for females, it's possible that the difference is mostly due to a second factor.\n",
    "\n",
    "For example, you might hypothesize that the search rate varies by violation type, and the difference in search rate between males and females is because they tend to commit different violations.\n",
    "\n",
    "You can test this hypothesis by examining the search rate for each combination of gender and violation. If the hypothesis was true, you would find that males and females are searched at about the same rate for each violation. Let's find out if that's the case!\n",
    "\n",
    "* Use a `.groupby()` to calculate the search rate for each combination of gender and violation. Are males and females searched at about the same rate for each violation?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "73cf8e3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "driver_gender  violation          \n",
      "F              Equipment              0.039984\n",
      "               Moving violation       0.039257\n",
      "               Other                  0.041018\n",
      "               Registration/plates    0.054924\n",
      "               Seat belt              0.017301\n",
      "               Speeding               0.008309\n",
      "M              Equipment              0.071496\n",
      "               Moving violation       0.061524\n",
      "               Other                  0.046191\n",
      "               Registration/plates    0.108802\n",
      "               Seat belt              0.035119\n",
      "               Speeding               0.027885\n",
      "Name: search_conducted, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate the search rate for each combination of gender and violation\n",
    "print(ri.groupby(['driver_gender', 'violation']).search_conducted.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f04032ef",
   "metadata": {},
   "source": [
    "* Reverse the ordering to group by violation before gender. The results may be easier to compare when presented this way."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fe35ffa6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "violation            driver_gender\n",
      "Equipment            F                0.039984\n",
      "                     M                0.071496\n",
      "Moving violation     F                0.039257\n",
      "                     M                0.061524\n",
      "Other                F                0.041018\n",
      "                     M                0.046191\n",
      "Registration/plates  F                0.054924\n",
      "                     M                0.108802\n",
      "Seat belt            F                0.017301\n",
      "                     M                0.035119\n",
      "Speeding             F                0.008309\n",
      "                     M                0.027885\n",
      "Name: search_conducted, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Reverse the ordering to group by violation before gender\n",
    "print(ri.groupby(['violation', 'driver_gender']).search_conducted.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d69b39f7",
   "metadata": {},
   "source": [
    "Great work! For all types of violations, the search rate is higher for males than for females, disproving our hypothesis.\n",
    "\n",
    "## Counting protective frisks\n",
    "During a vehicle search, the police officer may pat down the driver to check if they have a weapon. This is known as a \"protective frisk.\"\n",
    "\n",
    "In this exercise, you'll first check to see how many times \"Protective Frisk\" was the only search type. Then, you'll use a string method to locate all instances in which the driver was frisked.\n",
    "\n",
    "* Count the `search_type` values in the ri DataFrame to see how many times \"Protective Frisk\" was the only search type.\n",
    "* Create a new column, frisk, that is True if `search_type` contains the string \"Protective Frisk\" and False otherwise.\n",
    "* Check the data type of frisk to confirm that it's a Boolean Series.\n",
    "* Take the sum of frisk to count the total number of frisks."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6ef2b4d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Incident to Arrest                                          1290\n",
      "Probable Cause                                               924\n",
      "Inventory                                                    219\n",
      "Reasonable Suspicion                                         214\n",
      "Protective Frisk                                             164\n",
      "Incident to Arrest,Inventory                                 123\n",
      "Incident to Arrest,Probable Cause                            100\n",
      "Probable Cause,Reasonable Suspicion                           54\n",
      "Incident to Arrest,Inventory,Probable Cause                   35\n",
      "Probable Cause,Protective Frisk                               35\n",
      "Incident to Arrest,Protective Frisk                           33\n",
      "Inventory,Probable Cause                                      25\n",
      "Protective Frisk,Reasonable Suspicion                         19\n",
      "Incident to Arrest,Inventory,Protective Frisk                 18\n",
      "Incident to Arrest,Probable Cause,Protective Frisk            13\n",
      "Inventory,Protective Frisk                                    12\n",
      "Incident to Arrest,Reasonable Suspicion                        8\n",
      "Probable Cause,Protective Frisk,Reasonable Suspicion           5\n",
      "Incident to Arrest,Probable Cause,Reasonable Suspicion         5\n",
      "Incident to Arrest,Inventory,Reasonable Suspicion              4\n",
      "Incident to Arrest,Protective Frisk,Reasonable Suspicion       2\n",
      "Inventory,Reasonable Suspicion                                 2\n",
      "Inventory,Protective Frisk,Reasonable Suspicion                1\n",
      "Inventory,Probable Cause,Reasonable Suspicion                  1\n",
      "Inventory,Probable Cause,Protective Frisk                      1\n",
      "Name: search_type, dtype: int64\n",
      "bool\n",
      "303\n"
     ]
    }
   ],
   "source": [
    "# Count the 'search_type' values\n",
    "print(ri.search_type.value_counts())\n",
    "\n",
    "# Check if 'search_type' contains the string 'Protective Frisk'\n",
    "ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)\n",
    "\n",
    "# Check the data type of 'frisk'\n",
    "print(ri.frisk.dtype)\n",
    "\n",
    "# Take the sum of 'frisk'\n",
    "print(ri.frisk.sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56e3039b",
   "metadata": {},
   "source": [
    "Nice job! It looks like there were 303 drivers who were frisked. Next, you'll examine whether gender affects who is frisked.\n",
    "\n",
    "## Comparing frisk rates by gender\n",
    "In this exercise, you'll compare the rates at which female and male drivers are frisked during a search. Are males frisked more often than females, perhaps because police officers consider them to be higher risk?\n",
    "\n",
    "Before doing any calculations, it's important to filter the DataFrame to only include the relevant subset of data, namely stops in which a search was conducted.\n",
    "\n",
    "* Create a DataFrame, searched, that only contains rows in which `search_conducted` is True.\n",
    "* Take the mean of the frisk column to find out what percentage of searches included a frisk.\n",
    "* Calculate the frisk rate for each gender using a `.groupby()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b55e7082",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.09162382824312065\n",
      "driver_gender\n",
      "F    0.074561\n",
      "M    0.094353\n",
      "Name: frisk, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Create a DataFrame of stops in which a search was conducted\n",
    "searched = ri[ri.search_conducted == True]\n",
    "\n",
    "# Calculate the overall frisk rate by taking the mean of 'frisk'\n",
    "print(searched.frisk.mean())\n",
    "\n",
    "# Calculate the frisk rate for each gender\n",
    "print(searched.groupby('driver_gender').frisk.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ede2e66",
   "metadata": {},
   "source": [
    "Interesting! The frisk rate is higher for males than for females, though we can't conclude that this difference is caused by the driver's gender."
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
