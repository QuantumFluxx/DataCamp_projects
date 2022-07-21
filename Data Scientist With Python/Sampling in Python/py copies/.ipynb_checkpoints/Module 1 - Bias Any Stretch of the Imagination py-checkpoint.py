{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "050b2ca7",
   "metadata": {},
   "source": [
    "# Sampling in Python\n",
    "\n",
    "# Bias Any Stretch of the Imagination\n",
    "\n",
    "## Reasons for sampling\n",
    "Sampling is an important technique in your statistical arsenal. It isn't always appropriate though—you need to know when to use it and when to work with the whole dataset.\n",
    "\n",
    "Which of the following is not a good scenario to use sampling?\n",
    "\n",
    "* You've been handed one terabyte of data about error logs for your company's device.\n",
    "\n",
    "* You wish to learn about the travel habits of all Pakistani adult citizens.\n",
    "\n",
    "* **You've finished collecting data on a small study of the wing measurements for 10 butterflies.**\n",
    "\n",
    "* You are working to predict customer turnover on a big data project for your marketing firm.\n",
    "\n",
    "Commendations on your justifications for not sampling! Ten butterflies is a small dataset, so sampling isn't useful here.\n",
    "\n",
    "## Simple sampling with pandas\n",
    "Throughout this chapter, you'll be exploring song data from Spotify. Each row of this population dataset represents a song, and there are over 40,000 rows. Columns include the song name, the artists who performed it, the release year, and attributes of the song like its duration, tempo, and danceability. You'll start by looking at the durations.\n",
    "\n",
    "Your first task is to sample the Spotify dataset and compare the mean duration of the population with the sample.\n",
    "\n",
    "* Sample 1000 rows from `spotify_population`, assigning to `spotify_sample`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "17326e47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       acousticness                                          artists  \\\n",
      "23898      0.000073                            ['A Day To Remember']   \n",
      "26862      0.218000                                  ['Roddy Ricch']   \n",
      "325        0.005890                           ['David Crowder Band']   \n",
      "17340      0.000102                            ['Killswitch Engage']   \n",
      "21746      0.122000  ['Akon', \"Colby O'Donis\", 'Kardinal Offishall']   \n",
      "...             ...                                              ...   \n",
      "24684      0.472000                                ['Billie Eilish']   \n",
      "23936      0.000096                                     ['Paramore']   \n",
      "39941      0.065400                                  ['Terri Clark']   \n",
      "12344      0.481000                                  ['Kevin Gates']   \n",
      "16245      0.544000                                ['William Singe']   \n",
      "\n",
      "       danceability  duration_ms  duration_minutes  energy  explicit  \\\n",
      "23898         0.241     180840.0          3.014000   0.970       0.0   \n",
      "26862         0.688     157657.0          2.627617   0.656       1.0   \n",
      "325           0.549     348400.0          5.806667   0.728       0.0   \n",
      "17340         0.442     243213.0          4.053550   0.971       0.0   \n",
      "21746         0.743     312987.0          5.216450   0.948       0.0   \n",
      "...             ...          ...               ...     ...       ...   \n",
      "24684         0.692     170852.0          2.847533   0.394       0.0   \n",
      "23936         0.436     253947.0          4.232450   0.942       0.0   \n",
      "39941         0.574     206400.0          3.440000   0.896       0.0   \n",
      "12344         0.776     176471.0          2.941183   0.812       1.0   \n",
      "16245         0.689     121739.0          2.028983   0.311       0.0   \n",
      "\n",
      "                           id  instrumentalness   key  liveness  loudness  \\\n",
      "23898  1fTNpl2mxqHVlLqRNbyDhR          0.000000  10.0    0.9040    -4.246   \n",
      "26862  3wLtYwtqvKK2ewelSVPeDK          0.000000   4.0    0.1150    -5.541   \n",
      "325    2iFqa5oxkAE3eJor4tVE8v          0.000000  10.0    0.0884    -5.682   \n",
      "17340  050DHpB2u2E8i9JL6syLaS          0.008700   8.0    0.4390    -2.280   \n",
      "21746  7rv0UuxMX7CpUUwEE1jVrd          0.000000   0.0    0.1120    -4.445   \n",
      "...                       ...               ...   ...       ...       ...   \n",
      "24684  1RGasjWLZ4qMN7wbtkLa3u          0.000191  11.0    0.1170    -8.745   \n",
      "23936  1a9YW7fATU351ok4zWjU7a          0.000438   9.0    0.2090    -2.206   \n",
      "39941  3BcCqaxGznRqmB1BIerea2          0.000000  10.0    0.3100    -4.478   \n",
      "12344  3o1a1gcKSInPVgH5GmITxW          0.000019   2.0    0.1240    -4.772   \n",
      "16245  4Lj8paMFwyKTGfILLELVxt          0.000000  11.0    0.0841   -10.821   \n",
      "\n",
      "       mode                                           name  popularity  \\\n",
      "23898   0.0  I'm Made of Wax, Larry, What Are You Made Of?        62.0   \n",
      "26862   0.0                                      Die Young        74.0   \n",
      "325     1.0             O Praise Him (All This For A King)        42.0   \n",
      "17340   1.0                                        For You        43.0   \n",
      "21746   0.0                                      Beautiful        63.0   \n",
      "...     ...                                            ...         ...   \n",
      "24684   0.0                                         my boy        77.0   \n",
      "23936   1.0                          Brick by Boring Brick        63.0   \n",
      "39941   1.0                            I Just Wanna Be Mad        43.0   \n",
      "12344   1.0                                      Great Man        58.0   \n",
      "16245   0.0                                           Pony        55.0   \n",
      "\n",
      "      release_date  speechiness    tempo  valence    year  \n",
      "23898         2009       0.1040  159.930    0.621  2009.0  \n",
      "26862   2018-11-02       0.2760  160.414    0.365  2018.0  \n",
      "325     2003-01-01       0.0401  115.029    0.253  2003.0  \n",
      "17340   2006-01-21       0.0592  182.119    0.525  2006.0  \n",
      "21746   2008-01-01       0.0893  130.024    0.614  2008.0  \n",
      "...            ...          ...      ...      ...     ...  \n",
      "24684   2017-12-22       0.2070   89.936    0.324  2017.0  \n",
      "23936   2009-09-28       0.0496  164.975    0.500  2009.0  \n",
      "39941   2003-01-01       0.0393   99.974    0.731  2003.0  \n",
      "12344   2018-09-28       0.3260  136.051    0.710  2018.0  \n",
      "16245   2015-11-03       0.0783  137.958    0.417  2015.0  \n",
      "\n",
      "[1000 rows x 20 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import pyarrow.feather as feather\n",
    "\n",
    "spotify_population = feather.read_feather('datasets/spotify_2000_2020.feather')\n",
    "\n",
    "# Sample 1000 rows from spotify_population\n",
    "spotify_sample = spotify_population.sample(n=1000)\n",
    "\n",
    "# Print the sample\n",
    "print(spotify_sample)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f826ea8",
   "metadata": {},
   "source": [
    "* Calculate the mean duration in minutes from `spotify_population` using pandas.\n",
    "* Calculate the mean duration in minutes from `spotify_sample` using pandas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cbdd17ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       acousticness                                     artists  danceability  \\\n",
      "1459        0.01290                              ['Khruangbin']         0.661   \n",
      "10341       0.15500            ['Bethel Music', 'Jenn Johnson']         0.466   \n",
      "33605       0.13600                      ['South Park Mexican']         0.870   \n",
      "23035       0.30100                                   ['JAY-Z']         0.800   \n",
      "35328       0.76900                                   ['Drake']         0.854   \n",
      "...             ...                                         ...           ...   \n",
      "8942        0.28200  ['Mos Def', 'Pharoahe Monch', 'Nate Dogg']         0.654   \n",
      "31515       0.01420                      ['Fat Joe', 'Ashanti']         0.829   \n",
      "23250       0.59900                             ['Robert John']         0.431   \n",
      "30401       0.12900                                ['Maroon 5']         0.675   \n",
      "27943       0.00341                              ['Fireflight']         0.458   \n",
      "\n",
      "       duration_ms  duration_minutes  energy  explicit  \\\n",
      "1459      250780.0          4.179667   0.837       0.0   \n",
      "10341     296400.0          4.940000   0.670       0.0   \n",
      "33605     252907.0          4.215117   0.492       1.0   \n",
      "23035     227867.0          3.797783   0.922       1.0   \n",
      "35328     163121.0          2.718683   0.554       1.0   \n",
      "...            ...               ...     ...       ...   \n",
      "8942      223147.0          3.719117   0.864       1.0   \n",
      "31515     230400.0          3.840000   0.688       0.0   \n",
      "23250     253213.0          4.220217   0.463       0.0   \n",
      "30401     229827.0          3.830450   0.790       0.0   \n",
      "27943     201160.0          3.352667   0.849       0.0   \n",
      "\n",
      "                           id  instrumentalness  key  liveness  loudness  \\\n",
      "1459   4BTp7Ad6LZMebeYc3gQIfP          0.884000  7.0    0.2890    -7.450   \n",
      "10341  1gj9poFl2mLKkguqWo5Y1i          0.000000  8.0    0.1450    -4.701   \n",
      "33605  28DmL4rDQvqZVqvVzVfkQa          0.000034  9.0    0.0747    -6.175   \n",
      "23035  0s46SltT4On0Z6kglK1I5c          0.000009  4.0    0.0352    -5.125   \n",
      "35328  5r7WvQtyPfy1xch5zMgGRp          0.000002  8.0    0.0749    -4.684   \n",
      "...                       ...               ...  ...       ...       ...   \n",
      "8942   5Xd8DxeYKZHYNgQdignYCI          0.000000  8.0    0.1490    -4.420   \n",
      "31515  2eSJflipjhSKLExuSwuFrO          0.000002  8.0    0.0461    -7.652   \n",
      "23250  3w3rLh6wmne91BS2rwgcog          0.002820  0.0    0.1320    -7.342   \n",
      "30401  12tUCBq7V9qCF8qGOLpcnu          0.000000  1.0    0.1210    -6.295   \n",
      "27943  6M9vEm3Cy3PHr3QkXRX6x3          0.000001  3.0    0.1610    -4.244   \n",
      "\n",
      "       mode                                name  popularity release_date  \\\n",
      "1459    1.0                   The Infamous Bill        55.0   2014-10-13   \n",
      "10341   1.0              Goodness of God (Live)        64.0   2019-01-25   \n",
      "33605   0.0                              Iatola        44.0   2002-04-30   \n",
      "23035   0.0  I Just Wanna Love U (Give It 2 Me)        58.0   2000-10-31   \n",
      "35328   1.0                 Behind Barz - Bonus        72.0   2019-09-13   \n",
      "...     ...                                 ...         ...          ...   \n",
      "8942    1.0  Oh No - (best of decade I version)        42.0   2005-12-13   \n",
      "31515   1.0         What's Luv? (feat. Ashanti)        55.0   2002-02-05   \n",
      "23250   1.0               Sad Eyes - Remastered        57.0         2002   \n",
      "30401   1.0                       Love Somebody        57.0   2012-01-01   \n",
      "27943   0.0                         Unbreakable        56.0   2008-03-04   \n",
      "\n",
      "       speechiness    tempo  valence    year  \n",
      "1459        0.0369   88.456    0.927  2014.0  \n",
      "10341       0.0297  126.142    0.395  2019.0  \n",
      "33605       0.3040  162.030    0.576  2002.0  \n",
      "23035       0.2400   98.631    0.801  2000.0  \n",
      "35328       0.1720  142.069    0.272  2019.0  \n",
      "...            ...      ...      ...     ...  \n",
      "8942        0.4340   93.941    0.696  2005.0  \n",
      "31515       0.0978   93.857    0.869  2002.0  \n",
      "23250       0.0268  107.190    0.687  2002.0  \n",
      "30401       0.0369  120.015    0.423  2012.0  \n",
      "27943       0.0404   89.916    0.389  2008.0  \n",
      "\n",
      "[1000 rows x 20 columns]\n",
      "3.8521519140899896\n",
      "3.8172335166666653\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Sample 1000 rows from spotify_population\n",
    "spotify_sample = spotify_population.sample(n=1000)\n",
    "\n",
    "# Print the sample\n",
    "print(spotify_sample)\n",
    "\n",
    "# Calculate the mean duration in mins from spotify_population\n",
    "mean_dur_pop = spotify_population[\"duration_minutes\"].mean()\n",
    "\n",
    "# Calculate the mean duration in mins from spotify_sample\n",
    "mean_dur_samp = spotify_sample[\"duration_minutes\"].mean()\n",
    "\n",
    "# Print the means\n",
    "print(mean_dur_pop)\n",
    "print(mean_dur_samp)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "921eadc0",
   "metadata": {},
   "source": [
    "Powerful point estimating! Notice that the mean song duration in the sample is similar, but not identical to the mean song duration in the whole population.\n",
    "\n",
    "## Simple sampling and calculating with NumPy\n",
    "You can also use numpy to calculate parameters or statistics from a list or pandas Series.\n",
    "\n",
    "You'll be turning it up to eleven and looking at the loudness property of each song.\n",
    "\n",
    "* Create a pandas Series from the loudness column of `spotify_population`, assigning it to `loudness_pop`.\n",
    "* Sample `loudness_pop` to get 100 random values, assigning to `loudness_samp`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0e8e90b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "37004   -12.679\n",
      "12492    -6.038\n",
      "6863     -6.158\n",
      "41627    -6.246\n",
      "14534    -8.833\n",
      "          ...  \n",
      "11629   -13.024\n",
      "10538    -8.600\n",
      "22652    -6.474\n",
      "35904    -4.505\n",
      "7097    -10.073\n",
      "Name: loudness, Length: 100, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Create a pandas Series from the loudness column of spotify_population\n",
    "loudness_pop = spotify_population['loudness']\n",
    "\n",
    "# Sample 100 values of loudness_pop\n",
    "loudness_samp = loudness_pop.sample(n=100)\n",
    "\n",
    "# Print the sample\n",
    "print(loudness_samp)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0da33fc8",
   "metadata": {},
   "source": [
    "* Calculate the mean of `loudness_pop` using numpy.\n",
    "* Calculate the mean of `loudness_samp` using numpy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0ee23e62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-7.366856851353918\n",
      "-7.372889999999997\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Create a pandas Series from the loudness column of spotify_population\n",
    "loudness_pop = spotify_population['loudness']\n",
    "\n",
    "# Sample 100 values of loudness_pop\n",
    "loudness_samp = loudness_pop.sample(n=100)\n",
    "\n",
    "# Calculate the mean of loudness_pop\n",
    "mean_loudness_pop = np.mean(loudness_pop)\n",
    "\n",
    "# Calculate the mean of loudness_samp\n",
    "mean_loudness_samp = np.mean(loudness_samp)\n",
    "\n",
    "# Print the means\n",
    "print(mean_loudness_pop)\n",
    "print(mean_loudness_samp)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7355d8a7",
   "metadata": {},
   "source": [
    "Devious means! Again, notice that the calculated value (the mean) is close but not identical in each case.\n",
    "\n",
    "## Are the findings from this sample generalizable?\n",
    "You just saw how convenience sampling—collecting data using the easiest method—can result in samples that aren't representative of the population. Equivalently, this means findings from the sample are not generalizable to the population. Visualizing the distributions of the population and the sample can help determine whether or not the sample is representative of the population.\n",
    "\n",
    "The Spotify dataset contains an acousticness column, which is a confidence measure from zero to one of whether the track was made with instruments that aren't plugged in. You'll compare the acousticness distribution of the total population of songs with a sample of those songs.\n",
    "\n",
    "* Plot a histogram of the acousticness from `spotify_population` with bins of width 0.01 from 0 to 1 using pandas `.hist()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "88dbcf3b",
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
    "import matplotlib.pyplot as plt \n",
    "\n",
    "# Visualize the distribution of acousticness with a histogram\n",
    "spotify_population['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a7c6bc5",
   "metadata": {},
   "source": [
    "* Update the histogram code to use the `spotify_mysterious_sample` dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3478066e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Update the histogram to use spotify_mysterious_sample\n",
    "spotify_mysterious_sample['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ebc3a35e",
   "metadata": {},
   "source": [
    "Compare the two histograms you drew. Are the acousticness values in the sample generalizable to the general population?\n",
    "\n",
    "* Yes. Any sample should lead to a generalizable result about the population.\n",
    "\n",
    "* Yes. The sample selected is likely a random sample of all songs in our population.\n",
    "\n",
    "* No. Samples can never lead to generalizable results about the population.\n",
    "\n",
    "* **No. The acousticness samples are consistently higher than those in the general population.**\n",
    "\n",
    "* No. The acousticness samples are consistently lower than those in the general population.\n",
    "\n",
    "Ace acouticness analysis! The acousticness values in the sample are all greater than 0.95, whereas they range from 0 to 1 in the whole population.\n",
    "\n",
    "## Are these findings generalizable?\n",
    "Let's look at another sample to see if it is representative of the population. This time, you'll look at the duration_minutes column of the Spotify dataset, which contains the length of the song in minutes.\n",
    "\n",
    "* Plot a histogram of `duration_minutes` from `spotify_population` with bins of width 0.5 from 0 to 15 using pandas `.hist()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f3994c8f",
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
    "# Visualize the distribution of duration_minutes as a histogram\n",
    "spotify_population['duration_minutes'].hist(bins=np.arange(0, 15.5, 0.5))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f45b8d13",
   "metadata": {},
   "source": [
    "* Update the histogram code to use the `spotify_mysterious_sample2` dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3ffe00b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Update the histogram to use spotify_mysterious_sample2\n",
    "spotify_mysterious_sample2['duration_minutes'].hist(bins=np.arange(0, 15.5, 0.5))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "683fcdad",
   "metadata": {},
   "source": [
    "Compare the two histograms you drew. Are the duration values in the sample generalizable to the general population?\n",
    "\n",
    "* Yes. Any sample should lead to a generalizable result about the population.\n",
    "\n",
    "* **Yes. The sample selected is likely a random sample of all songs in the population.**\n",
    "\n",
    "* No. Samples can never lead to generalizable results about the population.\n",
    "\n",
    "* No. The duration samples are consistently higher than those in the general population.\n",
    "\n",
    "* No. The duration samples are consistently lower than those in the general population.\n",
    "\n",
    "Delightful duration distribution analysis! The duration values in the sample show a similar distribution to those in the whole population, so the results are generalizable.\n",
    "\n",
    "## Generating random numbers\n",
    "You've used `.sample()` to generate pseudo-random numbers from a set of values in a DataFrame. A related task is to generate random numbers that follow a statistical distribution, like the uniform distribution or the normal distribution.\n",
    "\n",
    "Each random number generation function has distribution-specific arguments and an argument for specifying the number of random numbers to generate.\n",
    "\n",
    "* Generate 5000 numbers from a uniform distribution, setting the parameters low to -3 and high to 3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f2c14460",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-2.90613058 -2.89808906  0.69691224 ...  2.08064709  2.89140952\n",
      " -0.05835649]\n"
     ]
    }
   ],
   "source": [
    "# Generate random numbers from a Uniform(-3, 3)\n",
    "uniforms = np.random.uniform(low=-3, high=3, size=5000)\n",
    "\n",
    "# Print uniforms\n",
    "print(uniforms)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f6887192",
   "metadata": {},
   "source": [
    "* Generate 5000 numbers from a normal distribution, setting the parameters loc to 5 and scale to 2."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "fd54b5a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[9.83668323 9.72215221 7.12665881 ... 5.73179277 5.76906889 4.48213925]\n"
     ]
    }
   ],
   "source": [
    "# Generate random numbers from a Normal(5, 2)\n",
    "normals = np.random.normal(loc=5, scale=2, size=5000)\n",
    "\n",
    "# Print normals\n",
    "print(normals)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32f0bf0a",
   "metadata": {},
   "source": [
    "* Plot a histogram of uniforms with bins of width of 0.25 from -3 to 3 using pandas `.hist()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "614b86d1",
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
    "# Generate random numbers from a Uniform(-3, 3)\n",
    "uniforms = np.random.uniform(low=-3, high=3, size=5000)\n",
    "\n",
    "# Plot a histogram of uniform values, binwidth 0.25\n",
    "plt.hist(uniforms, bins=np.arange(-3, 3.25, 0.25))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60c32233",
   "metadata": {},
   "source": [
    "* Plot a histogram of normals with bins of width of 0.5 from -2 to 13 using pandas `.hist()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "edda863c",
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
    "# Plot a histogram of normal values, binwidth 0.5\n",
    "plt.hist(normals, bins=np.arange(-2, 13.5, 0.5))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1faa12b2",
   "metadata": {},
   "source": [
    "Hunky-dory histogramming! Notice how the histograms almost take the flat and bell curve shapes of the uniform and normal distributions, but there is a bit of random noise.\n",
    "\n",
    "## Understanding random seeds\n",
    "While random numbers are important for many analyses, they create a problem: the results you get can vary slightly. This can cause awkward conversations with your boss when your script for calculating the sales forecast gives different answers each time.\n",
    "\n",
    "Setting the seed for numpy's random number generator helps avoid such problems by making the random number generation reproducible.\n",
    "\n",
    "* Which statement about x and y is true?\n",
    "```python\n",
    "import numpy as np\n",
    "np.random.seed(123)\n",
    "x = np.random.normal(size=5)\n",
    "y = np.random.normal(size=5)\n",
    "```\n",
    "\n",
    "* **x and y have identical values.**\n",
    "\n",
    "* The first value of x is identical to the first value of y, but other values are different.\n",
    "\n",
    "* The values of x are different from those of y.\n",
    "\n",
    "Which statement about x and y is true?\n",
    "```python\n",
    "import numpy as np\n",
    "np.random.seed(123)\n",
    "x = np.random.normal(size=5)\n",
    "np.random.seed(456)\n",
    "y = np.random.normal(size=5)\n",
    "```\n",
    "* x and y have identical values.\n",
    "\n",
    "* The first value of x is identical to the first value of y, but other values are different.\n",
    "\n",
    "* **The values of x are different from those of y.**\n",
    "\n",
    "Correct! Since different seeds are used, the generation will be different for x and y."
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
