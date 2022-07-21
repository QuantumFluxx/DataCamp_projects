{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6aa43786",
   "metadata": {},
   "source": [
    "# Random Numbers and Probability\n",
    "\n",
    "## Calculating probabilities\n",
    "You're in charge of the sales team, and it's time for performance reviews, starting with Amir. As part of the review, you want to randomly select a few of the deals that he's worked on over the past year so that you can look at them more deeply. Before you start selecting deals, you'll first figure out what the chances are of selecting certain deals.\n",
    "\n",
    "Recall that the probability of an event can be calculated by\n",
    "```\n",
    "P(event) = #ways event can happen / total # of possible outcomes\n",
    "```\n",
    "* Count the number of deals Amir worked on for each product type and store in counts."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f5c5959b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product B    62\n",
      "Product D    40\n",
      "Product A    23\n",
      "Product C    15\n",
      "Product F    11\n",
      "Product H     8\n",
      "Product I     7\n",
      "Product E     5\n",
      "Product N     3\n",
      "Product G     2\n",
      "Product J     2\n",
      "Name: product, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "amir_deals = pd.read_csv('datasets/amir_deals.csv')\n",
    "\n",
    "# Count the deals for each product\n",
    "counts = amir_deals['product'].value_counts()\n",
    "print(counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1fb9e48",
   "metadata": {},
   "source": [
    "* Calculate the probability of selecting a deal for the different product types by dividing the counts by the total number of deals Amir worked on. Save this as probs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b53755da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product B    0.348315\n",
      "Product D    0.224719\n",
      "Product A    0.129213\n",
      "Product C    0.084270\n",
      "Product F    0.061798\n",
      "Product H    0.044944\n",
      "Product I    0.039326\n",
      "Product E    0.028090\n",
      "Product N    0.016854\n",
      "Product G    0.011236\n",
      "Product J    0.011236\n",
      "Name: product, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate probability of picking a deal with each product\n",
    "probs = counts / amir_deals.shape[0]\n",
    "print(probs)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "78b78208",
   "metadata": {},
   "source": [
    "If you randomly select one of Amir's deals, what's the probability that the deal will involve Product C?\n",
    "\n",
    "* 15%\n",
    "\n",
    "* 80.43%\n",
    "\n",
    "* **8.43%**\n",
    "\n",
    "* 22.5%\n",
    "\n",
    "* 124.3%\n",
    "\n",
    "Perfect probability calculations! Now that you know what the chances are, it's time to start sampling.\n",
    "\n",
    "## Sampling deals\n",
    "In the previous exercise, you counted the deals Amir worked on. Now it's time to randomly pick five deals so that you can reach out to each customer and ask if they were satisfied with the service they received. You'll try doing this both with and without replacement.\n",
    "\n",
    "Additionally, you want to make sure this is done randomly and that it can be reproduced in case you get asked how you chose the deals, so you'll need to set the random seed before sampling from the deals.\n",
    "\n",
    "* Set the random seed to 24.\n",
    "* Take a sample of 5 deals without replacement and store them as `sample_without_replacement`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f25effaa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Unnamed: 0    product   client status   amount  num_users\n",
      "127         128  Product B  Current    Won  2070.25          7\n",
      "148         149  Product D  Current    Won  3485.48         52\n",
      "77           78  Product B  Current    Won  6252.30         27\n",
      "104         105  Product D  Current    Won  4110.98         39\n",
      "166         167  Product C      New   Lost  3779.86         11\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Set random seed\n",
    "np.random.seed(24)\n",
    "\n",
    "# Sample 5 deals without replacement\n",
    "sample_without_replacement = amir_deals.sample(5)\n",
    "print(sample_without_replacement)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4c883ca8",
   "metadata": {},
   "source": [
    "* Take a sample of 5 deals with replacement and save as `sample_with_replacement`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "16aead5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Unnamed: 0    product   client status   amount  num_users\n",
      "133         134  Product D  Current    Won  5992.86         98\n",
      "101         102  Product H  Current    Won  5116.34         63\n",
      "110         111  Product B  Current    Won   696.88         44\n",
      "49           50  Product B  Current    Won  3488.36         79\n",
      "56           57  Product D  Current    Won  6820.84         42\n"
     ]
    }
   ],
   "source": [
    "# Sample 5 deals with replacement\n",
    "sample_with_replacement = amir_deals.sample(5, replace=True)\n",
    "print(sample_with_replacement)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c66311f",
   "metadata": {},
   "source": [
    "What type of sampling is better to use for this situation?\n",
    "\n",
    "* With replacement\n",
    "\n",
    "* **Without replacement**\n",
    "\n",
    "* It doesn't matter\n",
    "\n",
    "Spectactular sampling! It's important to consider how you'll take a sample since there's no one-size-fits-all way to sample, and this can have an effect on your results.\n",
    "\n",
    "## Creating a probability distribution\n",
    "A new restaurant opened a few months ago, and the restaurant's management wants to optimize its seating space based on the size of the groups that come most often. On one night, there are 10 groups of people waiting to be seated at the restaurant, but instead of being called in the order they arrived, they will be called randomly. In this exercise, you'll investigate the probability of groups of different sizes getting picked first. Data on each of the ten groups is contained in the restaurant_groups DataFrame.\n",
    "\n",
    "* Create a histogram of the `group_size` column of restaurant_groups, setting bins to [2, 3, 4, 5, 6]. Remember to show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "061e3d2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Create a histogram of restaurant_groups and show plot\n",
    "restaurant_groups['group_size'].hist(bins=np.linspace(2,6,5))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f5e442b",
   "metadata": {},
   "source": [
    "* Count the number of each `group_size` in restaurant_groups, then divide by the number of rows in `restaurant_groups` to calculate the probability of randomly selecting a group of each size. Save as `size_dist`.\n",
    "* Reset the index of `size_dist`.\n",
    "* Rename the columns of `size_dist` to `group_size` and prob."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec288c25",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create probability distribution\n",
    "size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]\n",
    "\n",
    "# Reset index and rename columns\n",
    "size_dist = size_dist.reset_index()\n",
    "size_dist.columns = ['group_size', 'prob']\n",
    "\n",
    "print(size_dist)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "670dcfd2",
   "metadata": {},
   "source": [
    "* Calculate the expected value of the `size_distribution`, which represents the expected group size, by multiplying the `group_size` by the prob and taking the sum."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7222e499",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Expected value\n",
    "expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])\n",
    "print(expected_value)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38d6b7c5",
   "metadata": {},
   "source": [
    "* Calculate the probability of randomly picking a group of 4 or more people by subsetting for groups of size 4 or more and summing the probabilities of selecting those groups."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "785d6e9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Subset groups of size 4 or more\n",
    "groups_4_or_more = size_dist[size_dist['group_size'] >= 4]\n",
    "\n",
    "# Sum the probabilities of groups_4_or_more\n",
    "prob_4_or_more = np.sum(groups_4_or_more['prob'])\n",
    "print(prob_4_or_more)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4770197",
   "metadata": {},
   "source": [
    "Dexterous distribution utilization! You'll continue to build upon these skills since many statistical tests and methods use probability distributions as their foundation.\n",
    "\n",
    "## Identifying distributions\n",
    "Which sample is most likely to have been taken from a uniform distribution?\n",
    "![](https://assets.datacamp.com/production/repositories/5786/datasets/bd64d4775ec28f36b081d92aa38a391033c03b8f/Screen%20Shot%202020-05-04%20at%204.35.58%20PM.png)\n",
    "\n",
    "\n",
    "* A\n",
    "\n",
    "* **B**\n",
    "\n",
    "* C\n",
    "\n",
    "Impressive identification! Since the histogram depicts a sample and not the actual probability distribution, each outcome won't happen the exact same number of times due to randomness, but they're similar in number.\n",
    "\n",
    "## Expected value vs. sample mean\n",
    "The app to the right will take a sample from a discrete uniform distribution, which includes the numbers 1 through 9, and calculate the sample's mean. You can adjust the size of the sample using the slider. Note that the expected value of this distribution is 5.\n",
    "\n",
    "A sample is taken, and you win twenty dollars if the sample's mean is less than 4. There's a catch: you get to pick the sample's size.\n",
    "\n",
    "Which sample size is most likely to win you the twenty dollars?\n",
    "\n",
    "\n",
    "* **10**\n",
    "\n",
    "* 100\n",
    "\n",
    "* 1000\n",
    "\n",
    "* 5000\n",
    "\n",
    "* 10000\n",
    "\n",
    "Nice work! Since the sample mean will likely be closer to 5 (the expected value) with larger sample sizes, you have a better chance of getting a sample mean further away from 5 with a smaller sample.\n",
    "\n",
    "## Data back-ups\n",
    "The sales software used at your company is set to automatically back itself up, but no one knows exactly what time the back-ups happen. It is known, however, that back-ups happen exactly every 30 minutes. Amir comes back from sales meetings at random times to update the data on the client he just met with. He wants to know how long he'll have to wait for his newly-entered data to get backed up. Use your new knowledge of continuous uniform distributions to model this situation and answer Amir's questions.\n",
    "\n",
    "* To model how long Amir will wait for a back-up using a continuous uniform distribution, save his lowest possible wait time as `min_time` and his longest possible wait time as `max_time`. Remember that back-ups happen every 30 minutes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bda3feb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Min and max wait times for back-up that happens every 30 min\n",
    "min_time = 0\n",
    "max_time = 30"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9cc980f6",
   "metadata": {},
   "source": [
    "* Import `uniform` from `scipy.stats` and calculate the probability that Amir has to wait less than 5 minutes, and store in a variable called `prob_less_than_5`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9a45638d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.16666666666666666\n"
     ]
    }
   ],
   "source": [
    "# Import uniform from scipy.stats\n",
    "from scipy.stats import uniform\n",
    "\n",
    "# Calculate probability of waiting less than 5 mins\n",
    "prob_less_than_5 = uniform.cdf(5, min_time, max_time)\n",
    "print(prob_less_than_5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9084643e",
   "metadata": {},
   "source": [
    "* Calculate the probability that Amir has to wait more than 5 minutes, and store in a variable called `prob_greater_than_5`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2d4a71fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8333333333333334\n"
     ]
    }
   ],
   "source": [
    "# Calculate probability of waiting more than 5 mins\n",
    "prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time)\n",
    "print(prob_greater_than_5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28513ba5",
   "metadata": {},
   "source": [
    "* Calculate the probability that Amir has to wait between 10 and 20 minutes, and store in a variable called `prob_between_10_and_20`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2d4ab45c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.3333333333333333\n"
     ]
    }
   ],
   "source": [
    "# Calculate probability of waiting 10-20 mins\n",
    "prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)\n",
    "print(prob_between_10_and_20)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df6aa4b7",
   "metadata": {},
   "source": [
    "Wonderful wait-time calculations! There's a 33% chance that Amir will wait 10-20 minutes. In the next exercise, you'll make sure this calculation holds up by simulating some wait times.\n",
    "\n",
    "## Simulating wait times\n",
    "To give Amir a better idea of how long he'll have to wait, you'll simulate Amir waiting 1000 times and create a histogram to show him what he should expect. Recall from the last exercise that his minimum wait time is 0 minutes and his maximum wait time is 30 minutes.\n",
    "\n",
    "* Set the random seed to 334."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6b8d9bae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set random seed to 334\n",
    "np.random.seed(334)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5271ca39",
   "metadata": {},
   "source": [
    "* Import uniform from scipy.stats."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "13262ae7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import uniform\n",
    "# import uniform from scipy.stats"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53933ae4",
   "metadata": {},
   "source": [
    "* Generate 1000 wait times from the continuous uniform distribution that models Amir's wait time. Save this as `wait_times`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d7255a3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 7.144097    0.97455866  3.72802787  5.11644319  8.70602482 24.69140099\n",
      " 23.98012075  3.19592668 25.1985306  17.89048629 24.68695356 18.27160808\n",
      " 22.85829011  0.12929581 15.67789664  2.3262095  15.79151771 21.90473557\n",
      " 18.25817257 15.78657023 28.74328434  9.38971275 17.0010565   0.95433991\n",
      " 15.96917606  2.16395679  8.903302   19.24982156  6.52414731 14.10185677\n",
      " 27.86973455 14.38121016 28.59233824 13.17550521 22.96382405  2.52904371\n",
      "  6.2163781   8.40217036  4.48079914 28.16365298 19.73302715  3.63959282\n",
      "  1.74002295  1.5324219  26.97096908 29.37490861  4.71379092  6.44990488\n",
      "  6.81999564 22.81302458 12.41563042 11.14591581  8.08043184 29.60574053\n",
      "  3.24571518 19.66709277 13.38939302 29.56433707 24.84697258  6.249684\n",
      " 15.07668579  5.27474477 27.27430815  2.42084219 27.88317515  0.81231424\n",
      "  3.48564273 19.80738592  6.11128124 19.10323692  9.12156821 28.31696467\n",
      " 20.80158047 17.0840986  26.59969632 28.38502685 20.75398728 11.73610958\n",
      " 20.55950389 18.20349931  4.68857179 17.67638417 29.99091109 18.67756789\n",
      " 11.16391438  3.53028943 14.93882748 24.89203249 17.47310051 20.8740314\n",
      " 16.6070177  19.19564265  8.96414904  5.28451257  1.05350993 21.77737031\n",
      " 23.61684528 22.72809506 24.8322021  14.36218169  8.6091251  25.13656432\n",
      " 11.45898163 19.92575672 25.12266034  7.63273768  5.0240165  20.92435348\n",
      " 13.23933607  0.6401269  15.6813087  13.98669465  5.00961969 26.55407346\n",
      " 15.6478544   5.36392254 22.2807534  22.95452053 12.09657902 15.33347354\n",
      " 29.36367996 27.32761079 16.57775534 13.28054948 17.09693671 27.45768651\n",
      "  2.59501602  9.41004409  9.14688319 19.72368555  0.8399502   1.36535784\n",
      "  8.24745591 10.2650512  29.95498509 20.64562623  5.93986334 11.17818273\n",
      " 26.32817252  8.07638083  6.6348515  16.29376148 29.99092275 25.71567927\n",
      " 11.55546768 21.91960495 11.23343293 12.37874514 15.0825809  28.02838931\n",
      " 22.8535862   8.8911682  27.94808637 18.59880054 19.31673054  4.78414772\n",
      " 24.68245155  4.61858339  4.34185585  9.86285797 22.64196176 20.70638537\n",
      "  2.07610021 16.5432359   0.83932634 26.55708037 11.96557209  8.07255521\n",
      " 10.80342781 23.29099616 22.86574237 14.34997804  5.88657148 13.93691899\n",
      "  3.85622609 15.39470306 21.25310818 18.36870054  8.06383855 27.35806466\n",
      "  8.24616015 21.22703251 17.37235409  4.83719581 17.84253763  3.31270513\n",
      " 28.05979944 28.42309918  8.73094692 25.71299775  2.22366188  4.30187426\n",
      " 21.89436597 29.49072021 15.30664125 22.3802789   0.08102944 14.78896917\n",
      " 16.40399119  7.68390804  2.10437223  6.68794817 10.19108918 22.31258787\n",
      "  5.8189225  27.60781938 19.51339944 21.33124269  1.6294243  15.51174843\n",
      " 13.47212795 16.24027513 22.10266715  5.52406499  7.22056009  7.36829948\n",
      " 18.91081125 19.80927487 12.80401324  2.70031211 26.86102574 22.01951095\n",
      " 17.17665123 18.81827876  3.67837051 15.46293386 29.51597515 15.89595847\n",
      " 17.41855781 25.55857784 25.65737763 16.4151132   5.00323267 11.63197386\n",
      " 17.66808546 25.466024   15.18486451  0.85940046 27.00984537 14.42468181\n",
      " 27.4812224   9.47231537  2.05988889 17.30621667 24.95053845  5.57417231\n",
      " 16.0357139  13.26420998 29.46815429  1.16904392  4.53575356 10.65537707\n",
      " 11.26270564  6.0214732  27.64202445 10.29940068 28.54836132 22.22931556\n",
      " 17.55762098 28.31703818  3.20547158  6.51317017  9.60103128 11.55504752\n",
      "  1.10769737 25.19601111 26.41265999  3.17669809 29.03461951 23.78452941\n",
      " 22.35394515 18.03280452 11.23378656 25.18138124 23.9597556  10.58566727\n",
      "  2.56203807 16.32353266  8.34705721 21.65497161 27.82670318  3.24006097\n",
      "  9.48180202  1.48689026 12.89086955  0.84704402 21.10201173  9.14793573\n",
      " 27.17361576 18.45069642 14.49691685  3.98370201  0.44134824  5.05259221\n",
      " 18.47816542  8.11334339 19.95136747  7.1754582  20.10018729  4.97982617\n",
      "  8.81527565  5.76132824 15.72125645  4.76049255  4.76730185  4.54755451\n",
      " 11.99610604 22.19271804  7.0054561   0.9554475  12.72622458  5.10178612\n",
      "  3.46974455  7.75842307 13.13578589  3.8451399  11.02848319  5.77758805\n",
      " 16.19423275 23.15484726 20.1239129   8.50840771 10.91441361  7.11704929\n",
      " 20.25016912 28.69395694 20.42004446 24.35824921 24.56208344 18.70863082\n",
      "  1.55698104 27.49671811  2.57368945 23.03303579  2.38875615 13.98131955\n",
      " 21.8838685   8.44024292 25.05019036 21.95993093  8.76034493 22.85418651\n",
      " 26.07063198  5.46361622 25.58172855 15.67874872 17.81956733 26.81841668\n",
      " 13.19033546 23.19910687 23.62718492 13.15663104 23.41668296  1.87489683\n",
      " 25.2484807   8.4845543   4.92042842 22.73961665 20.2466653  19.58723259\n",
      "  2.03270822 22.9895573   7.3372969  17.54273192 21.09771191 16.96192787\n",
      "  3.48948107 16.15590988 17.70440831  1.60420151 19.81559878 25.80086106\n",
      " 15.68959678 18.83009183 23.19198615 12.66930187  7.00118096  6.64600958\n",
      " 19.87400439 19.55842619 25.54278522 14.27653959 12.0734572  22.78237983\n",
      " 17.15165279 24.08463516 28.59624819 28.16152099  5.93891699 16.94105605\n",
      " 20.80665928  9.99890108  8.79730012  7.05110922  3.8104523   5.62610024\n",
      "  5.58639014 18.78260685  9.95891585 20.62479473 28.77797774 25.81469814\n",
      "  2.25609181 13.65905187 21.1528068   8.01290913  7.73848867 26.88193447\n",
      " 21.44953343 10.12615075 19.75731318  4.27872352 20.30849315 26.77882578\n",
      "  1.351449   20.8075843   0.46173517 19.80997905  9.7624355  17.37924972\n",
      "  1.43062491 22.20157066 25.1824487  28.8357933  16.09702531 24.73842767\n",
      "  0.2308042   6.13048075 29.614561    8.33629603 16.12795224 29.21240454\n",
      " 13.45025092 28.92901674 28.68113999 18.76015795  8.85400148  0.72177506\n",
      " 18.5678127   1.5946721   6.51114298  0.14954964  8.40759558 15.3456776\n",
      " 18.16257912 21.48146244 19.35734786  6.69307887 11.14786018  5.19542535\n",
      " 20.11979092 15.36643858  1.75976538  1.88235419 14.67047828 17.87206607\n",
      " 23.89728101 11.53568193 19.55519337 12.9925055   3.75560435  8.84921298\n",
      " 10.41509647 10.05015649  2.08203941 13.95507535 18.69687686  3.65394569\n",
      " 16.73715719 25.9668531  19.90170356 10.66486523 27.98606183 19.33610382\n",
      " 27.37475735 24.1411498  28.39648506 10.56397635 17.67065935 19.81446104\n",
      "  5.08556252 21.61589418  4.91334443 10.25571404 13.86547777 28.5015485\n",
      " 19.52083861 22.05488912  9.17148377  1.11732389 18.30445657 13.80853\n",
      "  2.00270834 26.65687785  8.33324258 16.37203881 24.89846207  8.62610704\n",
      " 29.82242843 16.81338141 17.33734435  1.0612399  29.2449401   6.66842773\n",
      " 14.65276829 11.46127532  5.94042969  8.51718703 19.16192131 27.77484802\n",
      " 26.80478414 18.46459441 14.64021886 10.41881806  5.05273386 22.93123257\n",
      " 12.32037453 29.07333784 19.8933068  19.33393445 23.75624561 27.41576612\n",
      "  4.89400728 27.97022569  5.46431449 26.39553105 23.10148492  5.59326106\n",
      "  5.43438053 12.80881651 22.58136604  6.81522341  1.29891598  8.92824717\n",
      "  0.06222649  0.31415758  1.49504525 14.46068646 17.65853438  7.4496374\n",
      " 17.22446855 21.84287476 21.60599421 28.86047834 28.24253893  7.10948381\n",
      " 26.95417677 22.69920835 14.85402627  8.3681587  29.58708806 13.78486659\n",
      " 17.35864925 26.46297136 21.22739031 28.53046947  8.93805023  7.02914326\n",
      " 11.80133052 18.99940059 14.08892962  3.85612353 13.56279119 20.12274586\n",
      " 16.74078625 29.53044614  5.18316362 11.53812907 27.43654492  0.42476924\n",
      " 29.87062735  5.50874294  3.8568494   6.41204685 20.30702925  3.32308882\n",
      "  3.94770677  6.87059867  3.93014852 21.98204107  0.86507581 20.56982783\n",
      " 10.47517828  5.51681714 28.14377379 29.45286026 11.06512511 16.61676719\n",
      "  1.98579434  5.54260989  1.07592481  2.31764882  8.88290412 21.4881271\n",
      " 22.64224754  7.27994039  9.37643238 10.83908073  0.69663121 21.23717882\n",
      "  9.66027816 16.97956524 14.81638878 16.5534871   9.75601043  5.93087217\n",
      " 28.36797115 21.09462207 13.03173376  0.7983171   3.50516639 19.00649926\n",
      "  5.82081691  5.81833671 20.61983383 28.71056507  6.91237663 12.4619051\n",
      " 12.30761644 19.84040954  4.64447622  0.64917761 19.86567877  5.99418851\n",
      "  1.35794716 27.48067897 29.73644518 28.6065078   8.5299145   4.12152041\n",
      "  0.5607774  18.57081877 22.17373158  7.58966957 18.2784296  10.70211771\n",
      " 11.13177466 29.30678999  1.2423198  14.35713294 17.35500663 17.14866592\n",
      " 10.3789623  24.17742423 14.94162775  2.59992154 11.85508506 27.4947809\n",
      " 22.37927752 16.63597764  2.18654009 27.58998237 24.9960839  18.97091648\n",
      " 19.87097998 29.71143066 18.15641786  8.02594757 12.34873726  6.39950324\n",
      " 26.71285573  5.72013105 27.25611587 11.11118651 13.14563054 24.3161132\n",
      "  9.12227066  6.09164062  7.61512695 15.27894726  1.55172543 16.11462964\n",
      " 20.01927489  0.36023495 22.18975204 10.68017381 26.67207213 18.49390616\n",
      " 14.12316947 12.30157185 24.46937392  2.94349773  2.71721257 19.89328934\n",
      " 11.60564868 20.99716418  6.83938153  3.15126472 21.18057782 23.04084254\n",
      " 29.52319489 13.41468779  8.36540008  1.17474372 16.52320975 16.29079038\n",
      " 23.68058086  9.73990339 21.21125025 11.64009223  8.27581985 25.34508281\n",
      " 27.14020237 20.99498767 26.36379634 22.12460919 14.38182874 12.83843751\n",
      "  2.4921115   3.30654254 15.38775096  9.47486316 16.53719202 12.18243936\n",
      "  6.94896378  5.99117553 16.06222869  5.82268307 10.69273715  8.58678605\n",
      " 27.77414396  6.29565658 22.85039389 22.68722007  0.43084526 19.12501901\n",
      " 23.05647004  6.23804663 16.49611786 10.854354   12.4620608  26.2548841\n",
      " 19.76816626  6.54492209 28.71514653  7.80202629 16.96751571 11.15377563\n",
      " 22.80092952  5.09403519 24.00001246  8.21769557 13.53560859  2.94076629\n",
      "  4.02757203  8.96659938  6.86912639 12.0326642  27.15751025 15.4782868\n",
      "  7.22781653 17.19415714 10.47116023 21.49491811  5.4747806  26.51862933\n",
      " 26.16289208 29.74722369 26.5735013  16.7792301  15.31299374  5.97510684\n",
      " 14.539767    5.34494067  8.90650139 13.70810391  0.63137974  9.78624106\n",
      " 22.98898991 21.52163702  5.36747243  2.08048168  7.42243152 25.8369847\n",
      " 25.40242175 13.07497422 28.66966768 24.04491316 21.29637332  7.42492739\n",
      "  2.11604443 29.49179095  4.27645773  8.61358603 17.16555207 26.59803794\n",
      " 13.78944191 15.62067191  9.21670849 12.14562662 10.52617782 25.98579879\n",
      " 14.39787573  8.08763319 16.78552727 22.79597812  8.7695133  17.27072338\n",
      " 24.43151203 16.88485001 24.44534146 16.21756467 13.61941002 19.87394843\n",
      " 12.63576776 14.50185412 26.83264391  3.00081583 16.48057545  2.45212633\n",
      " 18.83439311 13.19865842  9.40766691 15.60923545  1.63933761 23.76828936\n",
      " 10.15252566  0.40447879 24.59292978  1.3675066   9.71814934 12.16659686\n",
      " 23.04867235 20.03414656  8.5168254  19.59414161  6.77825259  8.8070403\n",
      "  5.87152425  2.5970591   4.93086037 21.00689143 10.53794997  4.50059669\n",
      "  4.80161712 19.86587841 13.82231035 25.92370876 16.76861995 19.88191792\n",
      "  5.11770677 29.00105159 25.65446515  6.84179709 22.57233685  8.15577205\n",
      " 24.13735729  4.03149435  4.13231282 16.12464321 22.48533776 20.282976\n",
      "  5.74012718 22.43342651  2.60477234  3.21766129  5.65283575 28.84370986\n",
      " 23.65634284 21.7798963  16.85637734  0.61478999  4.53882038  4.65444933\n",
      "  9.04857098 19.63428333 15.00766938 17.76592972 21.46082362 25.77459268\n",
      " 19.85548771  8.20584755  8.47650143 21.69630957  3.13097349 10.20447772\n",
      " 29.66564838 23.56946713 26.2778947  23.81853285 10.81655255  6.05639951\n",
      "  2.85441413 19.56517693 23.71136826 20.36624573  6.59131157 23.74895849\n",
      " 22.42574624 10.31297875  6.60447634  5.37750477 29.10394928 12.33961909\n",
      " 14.61065264 27.83726115  5.16829978 19.01401557  5.2640168  10.30361904\n",
      " 24.32169445  3.18704573 25.06890427 26.01541021 13.94792952 21.25266832\n",
      " 25.93658805 16.80375076  1.50816509  2.64600638 13.47500562 15.08548187\n",
      " 14.90796765 20.88436957 22.53457433 15.84915157  8.86204958 27.73245412\n",
      " 11.22385246 15.78749796 15.91197569 22.37113884  3.19226887  4.65976517\n",
      "  9.30923397 10.77526643  3.97151627 29.28059273 29.27602822 20.71976894\n",
      " 18.60895651  4.29611269 23.93608872 22.58290622  4.47426371  7.2489746\n",
      " 15.22674952 27.63320022  8.78304562 28.40607909 17.1539386   2.61718331\n",
      " 10.65596075 29.8980006  29.91966885 27.34174997  0.61629001 15.17716754\n",
      "  9.90825324 16.72368794 12.96779625 10.46723235  1.79071474  4.91140186\n",
      "  0.71891742 27.83882355 26.95599526 19.63276655 25.02837667  6.70120501\n",
      " 27.8039181   3.93032514 29.20218039 20.45922096 18.39870488  6.64103042\n",
      " 15.9427296  29.26956198 29.75236465  6.24029179 10.9032813  25.74945237\n",
      " 19.34538144 16.31296664 10.93219849 10.70922385 21.19432171 10.39189311\n",
      "  1.8610141  24.11741202 25.59864155  0.68627027 15.7876837   1.10010957\n",
      "  3.47094738 27.61646738 10.07577678 19.84021078 27.29452887  8.52034156\n",
      "  5.181769   12.92311547 14.25423041 26.70151037 27.44545754 24.06119139\n",
      " 14.00076717  8.56031135 25.99043117 20.11722212]\n"
     ]
    }
   ],
   "source": [
    "# Generate 1000 wait times between 0 and 30 mins\n",
    "wait_times = uniform.rvs(0, 30, size=1000)\n",
    "\n",
    "print(wait_times)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca09455c",
   "metadata": {},
   "source": [
    "* Create a histogram of the simulated wait times and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f8169ff2",
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
    "# Create a histogram of simulated times and show plot\n",
    "plt.hist(wait_times)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f362bf5f",
   "metadata": {},
   "source": [
    "Superb simulating! Unless Amir figures out exactly what time each backup happens, he won't be able to time his data entry so it gets backed up sooner, but it looks like he'll wait about 15 minutes on average.\n",
    "\n",
    "## Simulating sales deals\n",
    "Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals he works on. Each deal has a binary outcome: it's either lost, or won, so you can model his sales deals with a binomial distribution. In this exercise, you'll help Amir simulate a year's worth of his deals so he can better understand his performance.\n",
    "\n",
    "* Import `binom` from `scipy.stats` and set the random seed to 10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "707e7637",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import binom from scipy.stats\n",
    "from scipy.stats import binom\n",
    "\n",
    "# Set random seed to 10\n",
    "np.random.seed(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38026030",
   "metadata": {},
   "source": [
    "* Simulate 1 deal worked on by Amir, who wins 30% of the deals he works on."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "394757b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n"
     ]
    }
   ],
   "source": [
    "# Simulate a single deal\n",
    "print(binom.rvs(1, 0.3, size=1))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "273488f2",
   "metadata": {},
   "source": [
    "* Simulate a typical week of Amir's deals, or one week of 3 deals."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "eea9569a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0]\n"
     ]
    }
   ],
   "source": [
    "# Simulate 1 week of 3 deals\n",
    "print(binom.rvs(3, 0.3, size=1))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0a1f45a",
   "metadata": {},
   "source": [
    "* Simulate a year's worth of Amir's deals, or 52 weeks of 3 deals each, and store in deals.\n",
    "* Print the mean number of deals he won per week."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6c7fceb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8461538461538461\n"
     ]
    }
   ],
   "source": [
    "# Simulate 52 weeks of 3 deals\n",
    "deals = binom.rvs(3, 0.3, size=52)\n",
    "\n",
    "# Print mean deals won per week\n",
    "print(np.mean(deals))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1324d5e3",
   "metadata": {},
   "source": [
    "Brilliant binomial simulation! In this simulated year, Amir won 0.83 deals on average each week.\n",
    "\n",
    "## Calculating binomial probabilities\n",
    "Just as in the last exercise, assume that Amir wins 30% of deals. He wants to get an idea of how likely he is to close a certain number of deals each week. In this exercise, you'll calculate what the chances are of him closing different numbers of deals using the binomial distribution.\n",
    "\n",
    "* What's the probability that Amir closes all 3 deals in a week? Save this as `prob_3`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "013d3c23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.026999999999999996\n"
     ]
    }
   ],
   "source": [
    "# Probability of closing 3 out of 3 deals\n",
    "prob_3 = binom.pmf(3, 3, 0.3)\n",
    "\n",
    "print(prob_3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ebadf95",
   "metadata": {},
   "source": [
    "* What's the probability that Amir closes 1 or fewer deals in a week? Save this as `prob_less_than_or_equal_1`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ec654ee1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.784\n"
     ]
    }
   ],
   "source": [
    "# Probability of closing <= 1 deal out of 3 deals\n",
    "prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)\n",
    "\n",
    "print(prob_less_than_or_equal_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7933f8d2",
   "metadata": {},
   "source": [
    "* What's the probability that Amir closes more than 1 deal? Save this as `prob_greater_than_1`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c954df37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.21599999999999997\n"
     ]
    }
   ],
   "source": [
    "# Probability of closing > 1 deal out of 3 deals\n",
    "prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)\n",
    "\n",
    "print(prob_greater_than_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f538c0e7",
   "metadata": {},
   "source": [
    "Powerful probability calculations! Amir has about a 22% chance of closing more than one deal in a week.\n",
    "\n",
    "## How many sales will be won?\n",
    "Now Amir wants to know how many deals he can expect to close each week if his win rate changes. Luckily, you can use your binomial distribution knowledge to help him calculate the expected value in different situations. Recall from the video that the expected value of a binomial distribution can be calculated by `n x p`.\n",
    "\n",
    "* Calculate the expected number of sales out of the 3 he works on that Amir will win each week if he maintains his 30% win rate.\n",
    "* Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.\n",
    "* Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bf096e05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8999999999999999\n",
      "0.75\n",
      "1.0499999999999998\n"
     ]
    }
   ],
   "source": [
    "# Expected number won with 30% win rate\n",
    "won_30pct = 3 * 0.3\n",
    "print(won_30pct)\n",
    "\n",
    "# Expected number won with 25% win rate\n",
    "won_25pct = 3 * 0.25\n",
    "print(won_25pct)\n",
    "\n",
    "# Expected number won with 35% win rate\n",
    "won_35pct = 3 * 0.35\n",
    "print(won_35pct)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f0e6347",
   "metadata": {},
   "source": [
    "Excellent expectation experimentation! If Amir's win rate goes up by 5%, he can expect to close more than 1 deal on average each week."
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
