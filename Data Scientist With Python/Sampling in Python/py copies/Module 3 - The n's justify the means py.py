{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "04e86710",
   "metadata": {},
   "source": [
    "# The n's justify the means\n",
    "\n",
    "## Calculating relative errors\n",
    "The size of the sample you take affects how accurately the point estimates reflect the corresponding population parameter. For example, when you calculate a sample mean, you want it to be close to the population mean. However, if your sample is too small, this might not be the case.\n",
    "\n",
    "The most common metric for assessing accuracy is relative error. This is the absolute difference between the population parameter and the point estimate, all divided by the population parameter. It is sometimes expressed as a percentage.\n",
    "\n",
    "* Generate a simple random sample from `attrition_pop` of fifty rows, setting the seed to 2022.\n",
    "* Calculate the mean employee Attrition in the sample.\n",
    "* Calculate the relative error between `mean_attrition_srs50` and `mean_attrition_pop` as a percentage."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bdae2978",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RelationshipSatisfaction\n",
      "Low          70.947368\n",
      "Medium       59.600000\n",
      "High         61.211268\n",
      "Very_High    59.500000\n",
      "Name: Attrition, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import pyarrow.feather as feather\n",
    "import numpy as np\n",
    "\n",
    "attrition_pop = feather.read_feather('datasets/attrition.feather')\n",
    "mean_attrition_pop = attrition_pop.groupby('RelationshipSatisfaction')['Attrition'].mean()\n",
    "\n",
    "# Generate a simple random sample of 50 rows, with seed 2022\n",
    "attrition_srs50 = attrition_pop.sample(n=50, random_state=2022)\n",
    "\n",
    "# Calculate the mean employee attrition in the sample\n",
    "mean_attrition_srs50 = attrition_srs50['Attrition'].mean()\n",
    "\n",
    "# Calculate the relative error percentage\n",
    "rel_error_pct50 = 100 * abs(mean_attrition_pop-mean_attrition_srs50) / mean_attrition_pop\n",
    "\n",
    "# Print rel_error_pct50\n",
    "print(rel_error_pct50)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37f1c086",
   "metadata": {},
   "source": [
    "* Calculate the relative error percentage again. This time, use a simple random sample of one hundred rows of `attrition_pop`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "08630b7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RelationshipSatisfaction\n",
      "Low          27.368421\n",
      "Medium        1.000000\n",
      "High          3.028169\n",
      "Very_High     1.250000\n",
      "Name: Attrition, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Generate a simple random sample of 100 rows, with seed 2022\n",
    "attrition_srs100 = attrition_pop.sample(n=100, random_state=2022)\n",
    "\n",
    "# Calculate the mean employee attrition in the sample\n",
    "mean_attrition_srs100 = attrition_srs100['Attrition'].mean()\n",
    "\n",
    "# Calculate the relative error percentage\n",
    "rel_error_pct100 = 100 * abs(mean_attrition_pop-mean_attrition_srs100) / mean_attrition_pop\n",
    "\n",
    "# Print rel_error_pct100\n",
    "print(rel_error_pct100)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee8c255e",
   "metadata": {},
   "source": [
    "Samply the best! As you increase the sample size, the sample mean generally gets closer to the population mean, and the relative error decreases.\n",
    "\n",
    "## Relative error vs. sample size\n",
    "The plot shows the relative error in the proportion of employee attritions, using simple random sampling, for sample sizes from 2 to 1470 (the size of the population).\n",
    "\n",
    "Clicking \"Regenerate plot\" will select new samples for each sample size, and calculate the relative errors again.\n",
    "\n",
    "Which statement about relative errors and sample sizes is true?\n",
    "\n",
    "* For any given sample size, the relative error between the sample mean and the population mean is fixed at a specific value.\n",
    "\n",
    "* When the sample is as large as the whole population, the relative error is small, but never zero.\n",
    "\n",
    "* If the sample mean is greater than the population mean, the relative error can be less than zero.\n",
    "\n",
    "* The relative error can never be greater than 100%.\n",
    "\n",
    "* **For small sample sizes, each additional entry in a sample can result in substantial decreases to the relative error.**\n",
    "\n",
    "You're relatively great at this! As you increase the sample size, the relative error decreases quickly at first, then more slowly as it drops to zero.\n",
    "\n",
    "## Replicating samples\n",
    "When you calculate a point estimate such as a sample mean, the value you calculate depends on the rows that were included in the sample. That means that there is some randomness in the answer. In order to quantify the variation caused by this randomness, you can create many samples and calculate the sample mean (or another statistic) for each sample.\n",
    "\n",
    "* Replicate the provided code so that it runs 500 times. Assign the resulting list of sample means to `mean_attritions`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5f53128a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.2, 0.11666666666666667, 0.08333333333333333, 0.2, 0.15]\n"
     ]
    }
   ],
   "source": [
    "# Create an empty list\n",
    "mean_attritions = []\n",
    "# Loop 500 times to create 500 sample means\n",
    "for i in range(500):\n",
    "    mean_attritions.append(\n",
    "    attrition_pop.sample(n=60)['Attrition'].mean())\n",
    "  \n",
    "# Print out the first few entries of the list\n",
    "print(mean_attritions[0:5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c0ec7e1c",
   "metadata": {},
   "source": [
    "* Draw a histogram of the `mean_attritions` list with 16 bins."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9dddf8ec",
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
    "# Create a histogram of the 500 sample means\n",
    "plt.hist(mean_attritions, bins=16)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47b9fd13",
   "metadata": {},
   "source": [
    "Resplendent replicating! By generating the sample statistic many times with different samples, you can quantify the amount of variation in those statistics.\n",
    "\n",
    "## Replication parameters\n",
    "The dashboard shows a histogram of sample mean proportions of employee attrition. There are two parameters: the size of each simple random sample, and the number of replicates. It's important to understand how each of these parameters affects the result. Use the parameter sliders to explore different values and note their effect on the histogram.\n",
    "\n",
    "Which statement about the effect of each parameter on the distribution of sample means is true?\n",
    "\n",
    "* As the sample size increases, the range of calculated sample means tends to increase.\n",
    "\n",
    "* As the number of replicates increases, the range of calculated sample means tends to increase.\n",
    "\n",
    "* **As the sample size increases, the range of calculated sample means tends to decrease.**\n",
    "\n",
    "* As the number of replicates increases, the range of calculated sample means tends to decrease.\n",
    "\n",
    "Powerful parameter play! As sample size increases, on average each sample mean has a lower relative error compared to the population mean, thus reducing the range of the distribution.\n",
    "\n",
    "## Exact sampling distribution\n",
    "To quantify how the point estimate (sample statistic) you are interested in varies, you need to know all the possible values it can take and how often. That is, you need to know its distribution.\n",
    "\n",
    "The distribution of a sample statistic is called the sampling distribution. When we can calculate this exactly, rather than using an approximation, it is known as the exact sampling distribution.\n",
    "\n",
    "Let's take another look at the sampling distribution of dice rolls. This time, we'll look at five eight-sided dice. (These have the numbers one to eight.)\n",
    "![](https://assets.datacamp.com/production/repositories/5975/datasets/001ee1102f4838b0806d9b3592ce76ce454c3892/shutterstock_231673213_8_sided_die.jpeg)\n",
    "\n",
    "* Expand a grid representing 5 8-sided dice. That is, create a DataFrame with five columns from a dictionary, named die1 to die5. The rows should contain all possibilities for throwing five dice, each numbered 1 to 8."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "73016e1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       die1  die2  die3  die4  die5\n",
      "0         1     1     1     1     1\n",
      "1         1     1     1     1     2\n",
      "2         1     1     1     1     3\n",
      "3         1     1     1     1     4\n",
      "4         1     1     1     1     5\n",
      "...     ...   ...   ...   ...   ...\n",
      "32763     8     8     8     8     4\n",
      "32764     8     8     8     8     5\n",
      "32765     8     8     8     8     6\n",
      "32766     8     8     8     8     7\n",
      "32767     8     8     8     8     8\n",
      "\n",
      "[32768 rows x 5 columns]\n"
     ]
    }
   ],
   "source": [
    "import itertools\n",
    "\n",
    "def expand_grid(data_dict):\n",
    "    rows = itertools.product(*data_dict.values())\n",
    "    return pd.DataFrame.from_records(rows, columns=data_dict.keys())\n",
    "\n",
    "# Expand a grid representing 5 8-sided dice\n",
    "dice = expand_grid(\n",
    "  {'die1': [1, 2, 3, 4, 5, 6, 7, 8],\n",
    "   'die2': [1, 2, 3, 4, 5, 6, 7, 8],\n",
    "   'die3': [1, 2, 3, 4, 5, 6, 7, 8],\n",
    "   'die4': [1, 2, 3, 4, 5, 6, 7, 8],\n",
    "   'die5': [1, 2, 3, 4, 5, 6, 7, 8]\n",
    "  })\n",
    "\n",
    "# Print the result\n",
    "print(dice)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "419764bc",
   "metadata": {},
   "source": [
    "* Add a column, `mean_roll`, to dice, that contains the mean of the five rolls as a categorical."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5f646206",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       die1  die2  die3  die4  die5 mean_roll\n",
      "0         1     1     1     1     1       1.0\n",
      "1         1     1     1     1     2       1.2\n",
      "2         1     1     1     1     3       1.4\n",
      "3         1     1     1     1     4       1.6\n",
      "4         1     1     1     1     5       1.8\n",
      "...     ...   ...   ...   ...   ...       ...\n",
      "32763     8     8     8     8     4       7.2\n",
      "32764     8     8     8     8     5       7.4\n",
      "32765     8     8     8     8     6       7.6\n",
      "32766     8     8     8     8     7       7.8\n",
      "32767     8     8     8     8     8       8.0\n",
      "\n",
      "[32768 rows x 6 columns]\n"
     ]
    }
   ],
   "source": [
    "# Add a column of mean rolls and convert to a categorical\n",
    "dice['mean_roll'] = (dice['die1'] + dice['die2'] + \n",
    "                     dice['die3'] + dice['die4'] + \n",
    "                     dice['die5']) / 5\n",
    "dice['mean_roll'] = dice['mean_roll'].astype('category')\n",
    "\n",
    "# Print result\n",
    "print(dice)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cef6338c",
   "metadata": {},
   "source": [
    "* Create a bar plot of the `mean_roll` categorical column, so it displays the count of each `mean_roll` in increasing order from 1.0 to 8.0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "849d9cb8",
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
    "# Draw a bar plot of mean_roll\n",
    "dice['mean_roll'].value_counts(sort=False).plot(kind=\"bar\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47303550",
   "metadata": {},
   "source": [
    "Exactly right! The exact sampling distribution shows all possible variations of the point estimate that you are interested in.\n",
    "\n",
    "## Approximate sampling distribution\n",
    "Calculating the exact sampling distribution is only possible in very simple situations. With just five eight-sided dice, the number of possible rolls is 8 ** 5, which is over thirty thousand. When the dataset is more complicated, for example, where a variable has hundreds or thousands of categories, the number of possible outcomes becomes too difficult to compute exactly.\n",
    "\n",
    "In this situation, you can calculate an approximate sampling distribution by simulating the exact sampling distribution. That is, you can repeat a procedure over and over again to simulate both the sampling process and the sample statistic calculation process.\n",
    "\n",
    "* Sample one to eight, five times, with replacement. Assign to `five_rolls`.\n",
    "* Calculate the mean of `five_rolls`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cbf8dfa7",
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
    "# Sample one to eight, five times, with replacement\n",
    "five_rolls = np.random.choice(list(range(1, 9)), size=5, replace=True)\n",
    "\n",
    "# Print the mean of five_rolls\n",
    "print(five_rolls.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c201b968",
   "metadata": {},
   "source": [
    "* Replicate the sampling code 1000 times, assigning each result to the list `sample_means_1000`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "db0d8983",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4.2, 3.6, 5.4, 3.4, 3.6, 6.0, 5.8, 4.2, 6.4, 5.0]\n"
     ]
    }
   ],
   "source": [
    "# Replicate the sampling code 1000 times\n",
    "sample_means_1000 = []\n",
    "for i in range(1000):\n",
    "    sample_means_1000.append(\n",
    "    np.random.choice(list(range(1, 9)), size=5, replace=True).mean()\n",
    "    )\n",
    "\n",
    "# Print the first 10 entries of the result\n",
    "print(sample_means_1000[0:10])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be195f34",
   "metadata": {},
   "source": [
    "* Plot `sample_means_1000` as a histogram with 20 bins."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0c084938",
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
    "# Draw a histogram of sample_means_1000 with 20 bins\n",
    "plt.hist(sample_means_1000, bins=20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72505c4b",
   "metadata": {},
   "source": [
    "Applaudable approximating! Once your dataset gets sufficiently big, exact sampling distributions cannot be calculated, so an approximate sampling distribution must be used. Notice that the histogram is close to but not exactly the same as the shape of the bar graph from the previous exercise.\n",
    "\n",
    "## Exact vs. approximate\n",
    "You've seen two types of sampling distribution now (exact and approximate). It's really important to understand when each should be computed.\n",
    "\n",
    "Should we always be able to compute the exact sampling distribution directly?\n",
    "\n",
    "* No, the exact sampling distribution is always unknown even for calculating the sample mean of a small number of die tosses like 2 or 3.\n",
    "\n",
    "* Yes, the population will always be known ahead of time, so one extra calculation is no problem.\n",
    "\n",
    "* Yes, the exact sampling distribution can be generated using a for loop, so it should be possible in all circumstances.\n",
    "\n",
    "* **No, the computational time and resources needed to look at the population of values could be too much for our problem.**\n",
    "\n",
    "Delightful sampling distribution distinguishing! The exact sampling distribution can only be calculated if you know what the population is and if the problems are small and simple enough to compute. Otherwise, the approximate sampling distribution must be used.\n",
    "\n",
    "## Population & sampling distribution means\n",
    "One of the useful features of sampling distributions is that you can quantify them. Specifically, you can calculate summary statistics on them. Here, you'll look at the relationship between the mean of the sampling distribution and the population parameter's mean.\n",
    "\n",
    "Three sampling distributions are provided. For each, the employee attrition dataset was sampled using simple random sampling, then the mean attrition was calculated. This was done 1000 times to get a sampling distribution of mean attritions. One sampling distribution used a sample size of 5 for each replicate, one used 50, and one used 500.\n",
    "\n",
    "* Calculate the mean of `sampling_distribution_5`, `sampling_distribution_50`, and `sampling_distribution_500` (a mean of sample means)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "575708af",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the mean of the mean attritions for each sampling distribution\n",
    "mean_of_means_5 = np.mean(sampling_distribution_5)\n",
    "mean_of_means_50 = np.mean(sampling_distribution_50)\n",
    "mean_of_means_500 = np.mean(sampling_distribution_500)\n",
    "\n",
    "# Print the results\n",
    "print(mean_of_means_5)\n",
    "print(mean_of_means_50)\n",
    "print(mean_of_means_500)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33865982",
   "metadata": {},
   "source": [
    "How does sample size affect the mean of the sample means?\n",
    "\n",
    "* As the sample size increases, the mean of the sampling distribution decreases until it reaches the population mean.\n",
    "\n",
    "* As the sample size increases, the mean of the sampling distribution increases until it reaches the population mean.\n",
    "\n",
    "* **Regardless of sample size, the mean of the sampling distribution is a close approximation to the population mean.**\n",
    "\n",
    "* Regardless of sample size, the mean of the sampling distribution is biased and cannot approximate the population mean.\n",
    "\n",
    "Mind-blowing mean manipulation! Even for small sample sizes, the mean of the sampling distribution is a good approximation of the population mean.\n",
    "\n",
    "## Population & sampling distribution variation\n",
    "You just calculated the mean of the sampling distribution and saw how it is an estimate of the corresponding population parameter. Similarly, as a result of the central limit theorem, the standard deviation of the sampling distribution has an interesting relationship with the population parameter's standard deviation and the sample size.\n",
    "\n",
    "* Calculate the standard deviation of `sampling_distribution_5`, `sampling_distribution_50`, and `sampling_distribution_500` (a standard deviation of sample means)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1da0f38c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the std. dev. of the mean attritions for each sampling distribution\n",
    "sd_of_means_5 = np.std(sampling_distribution_5, ddof=1)\n",
    "sd_of_means_50 = np.std(sampling_distribution_50, ddof=1)\n",
    "sd_of_means_500 = np.std(sampling_distribution_500, ddof=1)\n",
    "\n",
    "# Print the results\n",
    "print(sd_of_means_5)\n",
    "print(sd_of_means_50)\n",
    "print(sd_of_means_500)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d87f3ff5",
   "metadata": {},
   "source": [
    "How are the standard deviations of the sampling distributions related to the population standard deviation and the sample size?\n",
    "\n",
    "* The standard deviation of the sampling distribution is approximately equal to the population standard deviation, regardless of sample size.\n",
    "\n",
    "* The standard deviation of the sampling distribution is approximately equal to the population standard deviation multiplied by the sample size.\n",
    "\n",
    "* The standard deviation of the sampling distribution is approximately equal to the population standard deviation multiplied by the square root of the sample size.\n",
    "\n",
    "* The standard deviation of the sampling distribution is approximately equal to the population standard deviation divided by the sample size.\n",
    "\n",
    "* **The standard deviation of the sampling distribution is approximately equal to the population standard deviation divided by the square root of the sample size.**\n",
    "\n",
    "You set the gold standard for standard deviation! The amount of variation in the sampling distribution is related to the amount of variation in the population and the sample size. This is another consequence of the Central Limit Theorem."
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
