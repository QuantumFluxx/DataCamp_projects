{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "52365126",
   "metadata": {},
   "source": [
    "# More Distributions and the Central Limit Theorem\n",
    "\n",
    "## Distribution of Amir's sales\n",
    "Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. These values are stored in the amount column of amir_deals As part of Amir's performance review, you want to be able to estimate the probability of him selling different amounts, but before you can do this, you'll need to determine what kind of distribution the amount variable follows.\n",
    "\n",
    "* Create a histogram with 10 bins to visualize the distribution of the amount. Show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cf0b5a5d",
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
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "amir_deals = pd.read_csv('datasets/amir_deals.csv')\n",
    "\n",
    "# Histogram of amount with 10 bins and show plot\n",
    "amir_deals['amount'].hist(bins=10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "599a6019",
   "metadata": {},
   "source": [
    "Which probability distribution do the sales amounts most closely follow?\n",
    "\n",
    "* Uniform\n",
    "\n",
    "* Binomial\n",
    "\n",
    "* **Normal**\n",
    "\n",
    "* None of the above\n",
    "\n",
    "Fabulous work! Now that you've visualized the data, you know that you can approximate probabilities of different amounts using the normal distribution.\n",
    "\n",
    "## Probabilities from the normal distribution\n",
    "Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. These values are stored in the amount column of amir_deals and follow a normal distribution with a mean of 5000 dollars and a standard deviation of 2000 dollars. As part of his performance metrics, you want to calculate the probability of Amir closing a deal worth various amounts.\n",
    "\n",
    "* What's the probability of Amir closing a deal worth less than $7500?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "52a3e237",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8943502263331446\n"
     ]
    }
   ],
   "source": [
    "from scipy.stats import norm\n",
    "\n",
    "# Probability of deal < 7500\n",
    "prob_less_7500 = norm.cdf(7500, 5000, 2000)\n",
    "\n",
    "print(prob_less_7500)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07ba9e2f",
   "metadata": {},
   "source": [
    "* What's the probability of Amir closing a deal worth more than $1000?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b5876b2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9772498680518208\n"
     ]
    }
   ],
   "source": [
    "# Probability of deal > 1000\n",
    "prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)\n",
    "\n",
    "print(prob_over_1000)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cd8a2437",
   "metadata": {},
   "source": [
    "* What's the probability of Amir closing a deal worth between `$3000 and $7000`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f27fcb1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6826894921370859\n"
     ]
    }
   ],
   "source": [
    "# Probability of deal between 3000 and 7000\n",
    "prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)\n",
    "\n",
    "print(prob_3000_to_7000)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3c67079",
   "metadata": {},
   "source": [
    "* What amount will 25% of Amir's sales be less than?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cf95bc5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3651.0204996078364\n"
     ]
    }
   ],
   "source": [
    "# Calculate amount that 25% of deals will be less than\n",
    "pct_25 = norm.ppf(0.25, 5000, 2000)\n",
    "\n",
    "print(pct_25)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "162b5799",
   "metadata": {},
   "source": [
    "Nifty normal distribution usage! You know that you can count on Amir 75% (1-0.25) of the time to make a sale worth at least $3651.02. This information could be useful in making company-wide sales projections.\n",
    "\n",
    "## Simulating sales under new market conditions\n",
    "The company's financial analyst is predicting that next quarter, the worth of each sale will increase by 20% and the volatility, or standard deviation, of each sale's worth will increase by 30%. To see what Amir's sales might look like next quarter under these new market conditions, you'll simulate new sales amounts using the normal distribution and store these in the `new_sales` DataFrame, which has already been created for you.\n",
    "\n",
    "* Currently, Amir's average sale amount is `$5000`. Calculate what his new average amount will be if it increases by 20% and store this in new_mean.\n",
    "* Amir's current standard deviation is `$2000`. Calculate what his new standard deviation will be if it increases by 30% and store this in new_sd.\n",
    "* Create a variable called `new_sales`, which contains 36 simulated amounts from a normal distribution with a mean of new_mean and a standard deviation of `new_sd`.\n",
    "* Plot the distribution of the `new_sales` amounts using a histogram and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0aad8e79",
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
    "# Calculate new average amount\n",
    "new_mean = 5000 * 1.2\n",
    "\n",
    "# Calculate new standard deviation\n",
    "new_sd = 2000 * 1.3\n",
    "\n",
    "# Simulate 36 new sales\n",
    "new_sales = norm.rvs(new_mean, new_sd, size=36)\n",
    "\n",
    "# Create histogram and show\n",
    "plt.hist(new_sales)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c10f913",
   "metadata": {},
   "source": [
    "Successful simulating! Although the average sale amount went up, the variation also increased, so it's not straightforward to decide whether these sales are better than his current ones. In the next exercise, you'll explore the effects of higher variation.\n",
    "\n",
    "## Which market is better?\n",
    "The key metric that the company uses to evaluate salespeople is the percent of sales they make over $1000 since the time put into each sale is usually worth a bit more than that, so the higher this metric, the better the salesperson is performing.\n",
    "\n",
    "Recall that Amir's current sales amounts have a mean of $5000 and a standard deviation of $2000, and Amir's predicted amounts in next quarter's market have a mean of $6000 and a standard deviation of $2600.\n",
    "\n",
    "norm from scipy.stats is imported.\n",
    "\n",
    "Based only on the metric of percent of sales over $1000, does Amir perform better in the current market or the predicted market?\n",
    "\n",
    "* Amir performs much better in the current market.\n",
    "\n",
    "* Amir performs much better in next quarter's predicted market.\n",
    "\n",
    "* **Amir performs about equally in both markets.**\n",
    "\n",
    "Great work! In the current market, Amir makes sales over $1000 about 97.7% of the time, and about 97.3% of the time in the predicted market, so there's not much of a difference. However, his average sale amount is higher in the predicted market, so your company may want to consider other metrics as well.\n",
    "\n",
    "## Visualizing sampling distributions\n",
    "On the right, try creating sampling distributions of different summary statistics from samples of different distributions. Which distribution does the central limit theorem not apply to?\n",
    "\n",
    "\n",
    "* Discrete uniform distribution\n",
    "\n",
    "* Continuous uniform distribution\n",
    "\n",
    "* Binomial distribution\n",
    "\n",
    "* All of the above\n",
    "\n",
    "* **None of the above**\n",
    "\n",
    "Victorious visualizing! Regardless of the shape of the distribution you're taking sample means from, the central limit theorem will apply if the sampling distribution contains enough sample means.\n",
    "\n",
    "## The CLT in action\n",
    "The central limit theorem states that a sampling distribution of a sample statistic approaches the normal distribution as you take more samples, no matter the original distribution being sampled from.\n",
    "\n",
    "In this exercise, you'll focus on the sample mean and see the central limit theorem in action while examining the `num_users` column of `amir_deals` more closely, which contains the number of people who intend to use the product Amir is selling.\n",
    "\n",
    "* Create a histogram of the `num_users` column of `amir_deals` and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2127f762",
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
    "# Create a histogram of num_users and show\n",
    "amir_deals['num_users'].hist()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c792c13",
   "metadata": {},
   "source": [
    "* Set the seed to 104.\n",
    "* Take a sample of size 20 with replacement from the `num_users` column of `amir_deals`, and take the mean."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c48c862c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32.0\n"
     ]
    }
   ],
   "source": [
    "# Set seed to 104\n",
    "np.random.seed(104)\n",
    "\n",
    "# Sample 20 num_users with replacement from amir_deals\n",
    "samp_20 = amir_deals['num_users'].sample(20, replace=True)\n",
    "\n",
    "# Take mean of samp_20\n",
    "print(np.mean(samp_20))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "159253af",
   "metadata": {},
   "source": [
    "* Repeat this 100 times using a for loop and store as `sample_means`. This will take 100 different samples and calculate the mean of each."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a559774f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[31.35, 45.05, 33.55, 38.15, 50.85, 31.85, 34.65, 36.25, 38.9, 44.05, 35.45, 37.6, 37.95, 28.85, 33.3, 31.65, 45.5, 43.2, 24.4, 41.05, 37.2, 39.3, 29.45, 33.55, 45.3, 45.1, 30.95, 36.25, 37.65, 42.55, 34.55, 41.1, 36.9, 42.45, 38.45, 45.9, 42.7, 38.4, 32.55, 30.25, 38.0, 38.75, 49.3, 39.55, 49.05, 42.05, 41.0, 40.6, 58.25, 34.55, 51.2, 34.15, 36.95, 42.45, 41.85, 33.2, 36.15, 37.55, 34.2, 29.75, 42.35, 43.75, 29.0, 32.05, 31.65, 44.6, 30.85, 29.6, 37.7, 33.1, 36.35, 40.65, 45.7, 33.8, 40.1, 39.9, 33.5, 32.65, 32.85, 42.85, 35.4, 31.7, 32.0, 33.85, 36.6, 44.35, 39.9, 37.0, 37.3, 42.5, 38.35, 42.8, 44.55, 30.3, 50.45, 42.35, 40.65, 29.85, 39.3, 33.1]\n"
     ]
    }
   ],
   "source": [
    "sample_means = []\n",
    "# Loop 100 times\n",
    "for i in range(100):\n",
    "    # Take sample of 20 num_users\n",
    "    samp_20 = amir_deals['num_users'].sample(20, replace=True)\n",
    "    # Calculate mean of samp_20\n",
    "    samp_20_mean = np.mean(samp_20)\n",
    "    # Append samp_20_mean to sample_means\n",
    "    sample_means.append(samp_20_mean)\n",
    "  \n",
    "print(sample_means)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c076271e",
   "metadata": {},
   "source": [
    "* Convert `sample_means` into a pd.Series, create a histogram of the `sample_means`, and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1edb3319",
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
    "# Convert to Series and plot histogram\n",
    "sample_means_series = pd.Series(sample_means)\n",
    "sample_means_series.hist()\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3cfd101",
   "metadata": {},
   "source": [
    "Fabulous job! You've just seen the central limit thorem at work. Even though the distribution of num_users is not normal, the distribution of its sample means resembles the normal distribution.\n",
    "\n",
    "## The mean of means\n",
    "You want to know what the average number of users (`num_users`) is per deal, but you want to know this number for the entire company so that you can see if Amir's deals have more or fewer users than the company's average deal. The problem is that over the past year, the company has worked on more than ten thousand deals, so it's not realistic to compile all the data. Instead, you'll estimate the mean by taking several random samples of deals, since this is much easier than collecting data from everyone in the company.\n",
    "\n",
    "* Set the random seed to 321.\n",
    "* Take 30 samples (with replacement) of size 20 from `all_deals['num_users']` and take the mean of each sample. Store the sample means in `sample_means`.\n",
    "* Print the mean of `sample_means`.\n",
    "* Print the mean of the `num_users` column of `amir_deals`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "03d31314",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "38.821666666666665\n",
      "37.651685393258425\n"
     ]
    }
   ],
   "source": [
    "# Set seed to 321\n",
    "np.random.seed(321)\n",
    "\n",
    "sample_means = []\n",
    "# Loop 30 times to take 30 means\n",
    "for i in range(30):\n",
    "    # Take sample of size 20 from num_users col of all_deals with replacement\n",
    "    cur_sample = amir_deals['num_users'].sample(20, replace=True)\n",
    "    # Take mean of cur_sample\n",
    "    cur_mean = np.mean(cur_sample)\n",
    "    # Append cur_mean to sample_means\n",
    "    sample_means.append(cur_mean)\n",
    "\n",
    "# Print mean of sample_means\n",
    "print(np.mean(sample_means))\n",
    "\n",
    "# Print mean of num_users in amir_deals\n",
    "print(np.mean(amir_deals['num_users']))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3af9aa20",
   "metadata": {},
   "source": [
    "Magnificent mean calculation! Amir's average number of users is very close to the overall average, so it looks like he's meeting expectations. Make sure to note this in his performance review!\n",
    "\n",
    "## Tracking lead responses\n",
    "Your company uses sales software to keep track of new sales leads. It organizes them into a queue so that anyone can follow up on one when they have a bit of free time. Since the number of lead responses is a countable outcome over a period of time, this scenario corresponds to a Poisson distribution. On average, Amir responds to 4 leads each day. In this exercise, you'll calculate probabilities of Amir responding to different numbers of leads.\n",
    "\n",
    "* Import `poisson` from `scipy.stats` and calculate the probability that Amir responds to 5 leads in a day, given that he responds to an average of 4."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "cc62b865",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.1562934518505317\n"
     ]
    }
   ],
   "source": [
    "# Import poisson from scipy.stats\n",
    "from scipy.stats import poisson\n",
    "\n",
    "# Probability of 5 responses\n",
    "prob_5 = poisson.pmf(5, 4)\n",
    "\n",
    "print(prob_5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "111757d9",
   "metadata": {},
   "source": [
    "* Amir's coworker responds to an average of 5.5 leads per day. What is the probability that she answers 5 leads in a day?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "27674a69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.17140068409793663\n"
     ]
    }
   ],
   "source": [
    "# Probability of 5 responses\n",
    "prob_coworker = poisson.pmf(5, 5.5)\n",
    "\n",
    "print(prob_coworker)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7040145d",
   "metadata": {},
   "source": [
    "* What's the probability that Amir responds to 2 or fewer leads in a day?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "891d694a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.23810330555354436\n"
     ]
    }
   ],
   "source": [
    "# Probability of 2 or fewer responses\n",
    "prob_2_or_less = poisson.cdf(2, 4)\n",
    "\n",
    "print(prob_2_or_less)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ac4cf13",
   "metadata": {},
   "source": [
    "* What's the probability that Amir responds to more than 10 leads in a day?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f72fc675",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0028397661205137315\n"
     ]
    }
   ],
   "source": [
    "# Probability of > 10 responses\n",
    "prob_over_10 = 1 - poisson.cdf(10, 4)\n",
    "\n",
    "print(prob_over_10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6df28bb5",
   "metadata": {},
   "source": [
    "Perfect Poisson probabilities! Note that if you provide poisson.pmf() or poisson.cdf() with a non-integer, it throws an error since the Poisson distribution only applies to integers.\n",
    "\n",
    "## Modeling time between leads\n",
    "To further evaluate Amir's performance, you want to know how much time it takes him to respond to a lead after he opens it. On average, it takes 2.5 hours for him to respond. In this exercise, you'll calculate probabilities of different amounts of time passing between Amir receiving a lead and sending a response.\n",
    "\n",
    "* Import `expon` from `scipy.stats`. What's the probability it takes Amir less than an hour to respond to a lead?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d608e1b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.3296799539643607\n"
     ]
    }
   ],
   "source": [
    "# Import expon from scipy.stats\n",
    "from scipy.stats import expon\n",
    "\n",
    "# Print probability response takes < 1 hour\n",
    "print(expon.cdf(1, scale=2.5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c4d8e06d",
   "metadata": {},
   "source": [
    "* What's the probability it takes Amir more than 4 hours to respond to a lead?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "cbdd606f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.20189651799465536\n"
     ]
    }
   ],
   "source": [
    "# Print probability response takes > 4 hours\n",
    "print(1 - expon.cdf(4, scale=2.5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a71a5d8f",
   "metadata": {},
   "source": [
    "* What's the probability it takes Amir 3-4 hours to respond to a lead?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "fc0a4a83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.09929769391754684\n"
     ]
    }
   ],
   "source": [
    "# Print probability response takes 3-4 hours\n",
    "print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "467fc73c",
   "metadata": {},
   "source": [
    "Excellent exponential computations! There's only about a 20% chance it will take Amir more than 4 hours to respond, so he's pretty speedy in his responses.\n",
    "\n",
    "## The t-distribution\n",
    "Which statement is not true regarding the t-distribution?\n",
    "\n",
    "* The t-distribution has thicker tails than the normal distribution.\n",
    "\n",
    "* A t-distribution with high degrees of freedom resembles the normal distribution.\n",
    "\n",
    "* The number of degrees of freedom affects the distribution's variance.\n",
    "\n",
    "* **The t-distribution is skewed.**\n",
    "\n",
    "Terrific! The t-distribution is not skewed, just like the normal distribution, but it does have thicker tails and higher variance than the normal distribution."
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
