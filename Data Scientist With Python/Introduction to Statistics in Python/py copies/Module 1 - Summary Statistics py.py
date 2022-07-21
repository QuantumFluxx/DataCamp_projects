{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bbc5bb2b",
   "metadata": {},
   "source": [
    "# Introduction to Statistics in Python\n",
    "\n",
    "# Summary Statistics\n",
    "\n",
    "## Mean and median\n",
    "In this chapter, you'll be working with the 2018 Food Carbon Footprint Index from nu3. The food_consumption dataset contains information about the kilograms of food consumed per person per year in each country in each food category (consumption) as well as information about the carbon footprint of that food category (co2_emissions) measured in kilograms of carbon dioxide, or CO2, per person per year in each country.\n",
    "\n",
    "In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.\n",
    "\n",
    "pandas is imported as pd for you and `food_consumption` is pre-loaded.\n",
    "\n",
    "* Import numpy with the alias np.\n",
    "* Create two DataFrames: one that holds the rows of food_consumption for 'Belgium' and another that holds rows for 'USA'. Call these `be_consumption` and `usa_consumption`.\n",
    "* Calculate the mean and median of kilograms of food consumed per person per year for both countries."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "55b3a312",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "42.132727272727266\n",
      "12.59\n",
      "44.650000000000006\n",
      "14.58\n"
     ]
    }
   ],
   "source": [
    "# Import numpy with alias np\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "food_consumption = pd.read_csv('datasets/food_consumption.csv')\n",
    "\n",
    "# Filter for Belgium\n",
    "be_consumption = food_consumption[food_consumption['country'] == 'Belgium']\n",
    "\n",
    "# Filter for USA\n",
    "usa_consumption = food_consumption[food_consumption['country'] == 'USA']\n",
    "\n",
    "# Calculate mean and median consumption in Belgium\n",
    "print(np.mean(be_consumption['consumption']))\n",
    "print(np.median(be_consumption['consumption']))\n",
    "\n",
    "# Calculate mean and median consumption in USA\n",
    "print(np.mean(usa_consumption['consumption']))\n",
    "print(np.median(usa_consumption['consumption']))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52a77792",
   "metadata": {},
   "source": [
    "* Subset food_consumption for rows with data about Belgium and the USA.\n",
    "* Group the subsetted data by country and select only the consumption column.\n",
    "* Calculate the mean and median of the kilograms of food consumed per person per year in each country using `.agg()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5edc36e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              mean  median\n",
      "country                   \n",
      "Belgium  42.132727   12.59\n",
      "USA      44.650000   14.58\n"
     ]
    }
   ],
   "source": [
    "# Subset for Belgium and USA only\n",
    "be_and_usa = food_consumption[(food_consumption['country'] == \"Belgium\") | (food_consumption['country'] == 'USA')]\n",
    "\n",
    "# Group by country, select consumption column, and compute mean and median\n",
    "print(be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60a9d9ca",
   "metadata": {},
   "source": [
    "Marvelous mean and median calculation! When you want to compare summary statistics between groups, it's much easier to use .groupby() and .agg() instead of subsetting and calling the same functions multiple times.\n",
    "\n",
    "## Mean vs. median\n",
    "In the video, you learned that the mean is the sum of all the data points divided by the total number of data points, and the median is the middle value of the dataset where 50% of the data is less than the median, and 50% of the data is greater than the median. In this exercise, you'll compare these two measures of center.\n",
    "\n",
    "* Import `matplotlib.pyplot` with the alias plt.\n",
    "* Subset `food_consumption` to get the rows where food_category is 'rice'.\n",
    "* Create a histogram of `co2_emission` for rice and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dcaa1b54",
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
    "# Import matplotlib.pyplot with alias plt\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Subset for food_category equals rice\n",
    "rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']\n",
    "\n",
    "# Histogram of co2_emission for rice and show plot\n",
    "rice_consumption['co2_emission'].hist()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f2944f1",
   "metadata": {},
   "source": [
    "Take a look at the histogram you just created of different countries' CO2 emissions for rice. Which of the following terms best describes the shape of the data?\n",
    "\n",
    "* No skew\n",
    "\n",
    "* Left-skewed\n",
    "\n",
    "* **Right-skewed**\n",
    "----\n",
    "* Use `.agg()` to calculate the mean and median of `co2_emission` for rice."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e9515d97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mean      37.591615\n",
      "median    15.200000\n",
      "Name: co2_emission, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Subset for food_category equals rice\n",
    "rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']\n",
    "\n",
    "# Calculate mean and median of co2_emission with .agg()\n",
    "print(rice_consumption['co2_emission'].agg([np.mean, np.median]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e29f161b",
   "metadata": {},
   "source": [
    "Given the skew of this data, what measure of central tendency best summarizes the kilograms of CO2 emissions per person per year for rice?\n",
    "\n",
    "* Mean\n",
    "\n",
    "* **Median**\n",
    "\n",
    "* Both mean and median\n",
    "\n",
    "Great work! The mean is substantially higher than the median since it's being pulled up by the high values over 100 kg/person/year.\n",
    "\n",
    "## Quartiles, quantiles, and quintiles\n",
    "Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread, as well as to get a sense of where a data point stands in relation to the rest of the data set. For example, you might want to give a discount to the 10% most active users on a website.\n",
    "\n",
    "In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a dataset into 4, 5, and 10 pieces, respectively.\n",
    "\n",
    "* Calculate the quartiles of the `co2_emission` column of `food_consumption`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a6fbe516",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[   0.        5.21     16.53     62.5975 1712.    ]\n"
     ]
    }
   ],
   "source": [
    "# Calculate the quartiles of co2_emission\n",
    "print(np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f15af5d0",
   "metadata": {},
   "source": [
    "* Calculate the six quantiles that split up the data into 5 pieces (quintiles) of the `co2_emission` column of `food_consumption`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9f654bdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[   0.       3.54    11.026   25.59    99.978 1712.   ]\n"
     ]
    }
   ],
   "source": [
    "# Calculate the quintiles of co2_emission\n",
    "print(np.quantile(food_consumption['co2_emission'], [0, 0.2, 0.4, 0.6, 0.8, 1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e1a0674",
   "metadata": {},
   "source": [
    "* Calculate the eleven quantiles of `co2_emission` that split up the data into ten pieces (deciles)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "53b7704a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.00000e+00 6.68000e-01 3.54000e+00 7.04000e+00 1.10260e+01 1.65300e+01\n",
      " 2.55900e+01 4.42710e+01 9.99780e+01 2.03629e+02 1.71200e+03]\n"
     ]
    }
   ],
   "source": [
    "# Calculate the deciles of co2_emission\n",
    "print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a208c3f",
   "metadata": {},
   "source": [
    "Those are some high-quality quantiles! While calculating more quantiles gives you a more detailed look at the data, it also produces more numbers, making the summary more difficult to quickly understand.\n",
    "\n",
    "## Variance and standard deviation\n",
    "Variance and standard deviation are two of the most common ways to measure the spread of a variable, and you'll practice calculating these in this exercise. Spread is important since it can help inform expectations. For example, if a salesperson sells a mean of 20 products a day, but has a standard deviation of 10 products, there will probably be days where they sell 40 products, but also days where they only sell one or two. Information like this is important, especially when making predictions.\n",
    "\n",
    "* Calculate the variance and standard deviation of `co2_emission` for each food_category by grouping and aggregating.\n",
    "* Import `matplotlib.pyplot` with alias plt.\n",
    "* Create a histogram of `co2_emission` for the beef `food_category` and show the plot.\n",
    "* Create a histogram of `co2_emission` for the eggs `food_category` and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "53e8d351",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                        var         std\n",
      "food_category                          \n",
      "beef           88748.408132  297.906710\n",
      "dairy          17671.891985  132.935669\n",
      "eggs              21.371819    4.622966\n",
      "fish             921.637349   30.358481\n",
      "lamb_goat      16475.518363  128.356996\n",
      "nuts              35.639652    5.969895\n",
      "pork            3094.963537   55.632396\n",
      "poultry          245.026801   15.653332\n",
      "rice            2281.376243   47.763754\n",
      "soybeans           0.879882    0.938020\n",
      "wheat             71.023937    8.427570\n"
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
    "# Print variance and sd of co2_emission for each food_category\n",
    "print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))\n",
    "\n",
    "# Import matplotlib.pyplot with alias plt\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Create histogram of co2_emission for food_category 'beef'\n",
    "food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()\n",
    "# Show plot\n",
    "plt.show()\n",
    "\n",
    "# Create histogram of co2_emission for food_category 'eggs'\n",
    "food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5b827be2",
   "metadata": {},
   "source": [
    "Superb spread measurement! Beef has the largest amount of variation in its CO2 emissions, while eggs have a relatively small amount of variation.\n",
    "\n",
    "## Finding outliers using IQR\n",
    "Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean, such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread that's less influenced by outliers. IQR is also often used to find outliers. If a value is less than Q1 - 1.5 x IQR or greater than Q3 + 1.5 x IQR, it's considered an outlier. In fact, this is how the lengths of the whiskers in a matplotlib box plot are calculated.\n",
    "![](https://assets.datacamp.com/production/repositories/5758/datasets/ca7e6e1832be7ec1842f62891815a9b0488efa83/Screen%20Shot%202020-04-28%20at%2010.04.54%20AM.png)\n",
    "\n",
    "* Calculate the total `co2_emission` per country by grouping by country and taking the sum of `co2_emission`. Store the resulting DataFrame as `emissions_by_country`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2a6f4aab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "country\n",
      "Albania      1777.85\n",
      "Algeria       707.88\n",
      "Angola        412.99\n",
      "Argentina    2172.40\n",
      "Armenia      1109.93\n",
      "              ...   \n",
      "Uruguay      1634.91\n",
      "Venezuela    1104.10\n",
      "Vietnam       641.51\n",
      "Zambia        225.30\n",
      "Zimbabwe      350.33\n",
      "Name: co2_emission, Length: 130, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate total co2_emission per country: emissions_by_country\n",
    "emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()\n",
    "\n",
    "print(emissions_by_country)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a445311d",
   "metadata": {},
   "source": [
    "* Compute the first and third quartiles of `emissions_by_country` and store these as q1 and q3.\n",
    "* Calculate the interquartile range of `emissions_by_country` and store it as iqr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d5984d23",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Compute the first and third quartiles and IQR of emissions_by_country\n",
    "q1 = np.quantile(emissions_by_country, 0.25)\n",
    "q3 = np.quantile(emissions_by_country, 0.75)\n",
    "iqr = q3 - q1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b771ea2",
   "metadata": {},
   "source": [
    "* Calculate the lower and upper cutoffs for outliers of `emissions_by_country`, and store these as lower and upper."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "604fc5dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the lower and upper cutoffs for outliers\n",
    "lower = q1 - 1.5 * iqr\n",
    "upper = q3 + 1.5 * iqr"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f018a3aa",
   "metadata": {},
   "source": [
    "* Subset `emissions_by_country` to get countries with a total emission greater than the upper cutoff or a total emission less than the lower cutoff."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "11c9b050",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "country\n",
      "Argentina    2172.4\n",
      "Name: co2_emission, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Subset emissions_by_country to find outliers\n",
    "outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]\n",
    "print(outliers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e634b3c5",
   "metadata": {},
   "source": [
    "Outstanding outlier detection! It looks like Argentina has a substantially higher amount of CO2 emissions per person than other countries in the world."
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
