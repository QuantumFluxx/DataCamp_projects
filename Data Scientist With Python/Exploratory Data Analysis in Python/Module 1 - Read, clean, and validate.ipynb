{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ef1b82e2",
   "metadata": {},
   "source": [
    "# Exploratory Data Analysis in Python\n",
    "\n",
    "# Read, clean, and validate\n",
    "\n",
    "## Read the codebook\n",
    "When you work with datasets like the NSFG, it is important to read the documentation carefully. If you interpret a variable incorrectly, you can generate nonsense results and never realize it. So before you start coding, you'll need to get familiar with the NSFG codebook, which describes every variable.\n",
    "\n",
    "Here is the documentation from the NSFG codebook for \"BIRTHWGT_OZ1\":\n",
    "\n",
    "![](https://assets.datacamp.com/production/repositories/4025/datasets/0d2a0c18b63f3ddf056858c145a6bdc022d8656c/Screenshot%202019-03-31%2019.16.14.png)\n",
    "\n",
    "How many respondents refused to answer this question?\n",
    "\n",
    "* **1**\n",
    "\n",
    "* 35\n",
    "\n",
    "* 48-49\n",
    "\n",
    "* 2967\n",
    "\n",
    "You got it. Remember, the codebook is your friend!\n",
    "\n",
    "## Exploring the NSFG data\n",
    "To get the number of rows and columns in a DataFrame, you can read its `shape` attribute.\n",
    "\n",
    "To get the column names, you can read the columns attribute. The result is an Index, which is a Pandas data structure that is similar to a list. Let's begin exploring the NSFG data! It has been pre-loaded for you into a DataFrame called nsfg.\n",
    "\n",
    "* Calculate the number of rows and columns in the DataFrame `nsfg`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57dc84d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import h5py\n",
    "\n",
    "# Display the number of rows and columns\n",
    "nsfg.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5a468ff",
   "metadata": {},
   "source": [
    "* Display the names of the columns in nsfg.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe9947e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Display the names of the columns\n",
    "nsfg.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "350ccb60",
   "metadata": {},
   "source": [
    "* Select the column 'birthwgt_oz1' and assign it to a new variable called ounces."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "613f1b31",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Select column birthwgt_oz1: ounces\n",
    "ounces = nsfg['birthwgt_oz1']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "caf95ebf",
   "metadata": {},
   "source": [
    "* Display the first 5 elements of ounces."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f46efc2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the first 5 elements of ounces\n",
    "print(ounces.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24d3fc00",
   "metadata": {},
   "source": [
    "Nice job! Remember these attributes and methods; they are useful when you are exploring a new dataset. It's now time to check for errors and prepare the data for analysis. Keep going!\n",
    "\n",
    "## Validate a variable\n",
    "In the NSFG dataset, the variable 'outcome' encodes the outcome of each pregnancy as shown below:\n",
    "```\n",
    "value\tlabel\n",
    "1\tLive birth\n",
    "2\tInduced abortion\n",
    "3\tStillbirth\n",
    "4\tMiscarriage\n",
    "5\tEctopic pregnancy\n",
    "6\tCurrent pregnancy\n",
    "```\n",
    "The nsfg DataFrame has been pre-loaded for you. Explore it in the IPython Shell and use the methods Allen showed you in the video to answer the following question: How many pregnancies in this dataset ended with a live birth?\n",
    "\n",
    "\n",
    "* **6489**\n",
    "\n",
    "* 9538\n",
    "\n",
    "* 1469\n",
    "\n",
    "* 6\n",
    "\n",
    "Correct! By comparing your results with the codebook, you confirm you are interpreting the data correctly.\n",
    "\n",
    "## Clean a variable\n",
    "In the NSFG dataset, the variable 'nbrnaliv' records the number of babies born alive at the end of a pregnancy.\n",
    "\n",
    "If you use `.value_counts()` to view the responses, you'll see that the value 8 appears once, and if you consult the codebook, you'll see that this value indicates that the respondent refused to answer the question.\n",
    "\n",
    "Your job in this exercise is to replace this value with np.nan. Recall from the video how Allen replaced the values 98 and 99 in the ounces column using the `.replace()` method:\n",
    "```python\n",
    "ounces.replace([98, 99], np.nan, inplace=True)\n",
    "```\n",
    "\n",
    "* In the 'nbrnaliv' column, replace the value 8, in place, with the special value NaN.\n",
    "* Confirm that the value 8 no longer appears in this column by printing the values and their frequencies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7939e6de",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Replace the value 8 with NaN\n",
    "nsfg['nbrnaliv'].replace([8], np.nan, inplace=True)\n",
    "\n",
    "# Print the values and their frequencies\n",
    "print(nsfg['nbrnaliv'].value_counts())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8921ce81",
   "metadata": {},
   "source": [
    "Excellent. If you are careful about this kind of cleaning and validation, it will save time (in the long run) and avoid potentially serious errors.\n",
    "\n",
    "## Compute a variable\n",
    "For each pregnancy in the NSFG dataset, the variable 'agecon' encodes the respondent's age at conception, and 'agepreg' the respondent's age at the end of the pregnancy.\n",
    "\n",
    "Both variables are recorded as integers with two implicit decimal places, so the value 2575 means that the respondent's age was 25.75.\n",
    "\n",
    "* Select 'agecon' and 'agepreg', divide them by 100, and assign them to the local variables agecon and agepreg."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1bc5495d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Select the columns and divide by 100\n",
    "agecon = nsfg['agecon'] / 100\n",
    "agepreg = nsfg['agepreg'] / 100"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f69dda1",
   "metadata": {},
   "source": [
    "* Compute the difference, which is an estimate of the duration of the pregnancy. Keep in mind that for each pregnancy, agepreg will be larger than agecon."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b9920e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Compute the difference\n",
    "preg_length = agepreg - agecon"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51291f5d",
   "metadata": {},
   "source": [
    "* Use `.describe()` to compute the mean duration and other summary statistics."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4bb6fb75",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Compute summary statistics\n",
    "print(preg_length.describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0343554e",
   "metadata": {},
   "source": [
    "Good job. A variable that's computed from other variables is sometimes called a 'recode'. It's now time to get back to the motivating question for this chapter: what is the average birth weight for babies in the U.S.? See you in the next video!\n",
    "\n",
    "## Make a histogram\n",
    "Histograms are one of the most useful tools in exploratory data analysis. They quickly give you an overview of the distribution of a variable, that is, what values the variable can have, and how many times each value appears.\n",
    "\n",
    "As we saw in a previous exercise, the NSFG dataset includes a variable 'agecon' that records age at conception for each pregnancy. Here, you're going to plot a histogram of this variable. You'll use the bins parameter that you saw in the video, and also a new parameter - histtype - which you can read more about here in the matplotlib documentation. Learning how to read documentation is an essential skill. If you want to learn more about matplotlib, you can check out DataCamp's Introduction to Data Visualization with Matplotlib course.\n",
    "\n",
    "* Plot a histogram of agecon with 20 bins."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04bd800a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Plot the histogram\n",
    "plt.hist(agecon, bins=20)\n",
    "\n",
    "# Label the axes\n",
    "plt.xlabel('Age at conception')\n",
    "plt.ylabel('Number of pregnancies')\n",
    "\n",
    "# Show the figure\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f260350",
   "metadata": {},
   "source": [
    "* Adapt your code to make an unfilled histogram by setting the parameter histtype to be 'step'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65b2aea0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the histogram\n",
    "plt.hist(agecon, bins=20, histtype='step')\n",
    "\n",
    "# Label the axes\n",
    "plt.xlabel('Age at conception')\n",
    "plt.ylabel('Number of pregnancies')\n",
    "\n",
    "# Show the figure\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d5a1a55",
   "metadata": {},
   "source": [
    "Nice job! matplotlib functions provide a lot of options; be sure to read the documentation so you know what they can do.\n",
    "\n",
    "## Compute birth weight\n",
    "Now let's pull together the steps in this chapter to compute the average birth weight for full-term babies.\n",
    "\n",
    "I've provided a function, `resample_rows_weighted`, that takes the NSFG data and resamples it using the sampling weights in `wgt2013_2015`. The result is a sample that is representative of the U.S. population.\n",
    "\n",
    "Then I extract `birthwgt_lb1` and `birthwgt_oz1`, replace special codes with NaN, and compute total birth weight in pounds, birth_weight.\n",
    "```python\n",
    "# Resample the data\n",
    "nsfg = resample_rows_weighted(nsfg, 'wgt2013_2015')\n",
    "\n",
    "# Clean the weight variables\n",
    "pounds = nsfg['birthwgt_lb1'].replace([98, 99], np.nan)\n",
    "ounces = nsfg['birthwgt_oz1'].replace([98, 99], np.nan)\n",
    "\n",
    "# Compute total birth weight\n",
    "birth_weight = pounds + ounces/16\n",
    "```\n",
    "\n",
    "* Make a Boolean Series called full_term that is true for babies with 'prglngth' greater than or equal to 37 weeks.\n",
    "* Use `full_term` and birth_weight to select birth weight in pounds for full-term babies. Store the result in `full_term_weight`.\n",
    "* Compute the mean weight of full-term babies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a07c60bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a Boolean Series for full-term babies\n",
    "full_term = nsfg['prglngth'] >= 37\n",
    "\n",
    "# Select the weights of full-term babies\n",
    "full_term_weight = birth_weight[full_term]\n",
    "\n",
    "# Compute the mean weight of full-term babies\n",
    "print(full_term_weight.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ad14879",
   "metadata": {},
   "source": [
    "Nice job. You're almost done, but there's one last thing we have to check...\n",
    "\n",
    "## Filter\n",
    "In the previous exercise, you computed the mean birth weight for full-term babies; you filtered out preterm babies because their distribution of weight is different.\n",
    "\n",
    "The distribution of weight is also different for multiple births, like twins and triplets. In this exercise, you'll filter them out, too, and see what effect it has on the mean.\n",
    "\n",
    "* Use the variable 'nbrnaliv' to make a Boolean Series that is True for single births (where 'nbrnaliv' equals 1) and False otherwise.\n",
    "* Use Boolean Series and logical operators to select single, full-term babies and compute their mean birth weight.\n",
    "* For comparison, select multiple, full-term babies and compute their mean birth weight."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ea6677e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Filter full-term babies\n",
    "full_term = nsfg['prglngth'] >= 37\n",
    "\n",
    "# Filter single births\n",
    "single = nsfg['nbrnaliv'] == 1\n",
    "\n",
    "# Compute birth weight for single full-term babies\n",
    "single_full_term_weight = birth_weight[single & full_term]\n",
    "print('Single full-term mean:', single_full_term_weight.mean())\n",
    "\n",
    "# Compute birth weight for multiple full-term babies\n",
    "mult_full_term_weight = birth_weight[~single & full_term]\n",
    "print('Multiple full-term mean:', mult_full_term_weight.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c2ae145",
   "metadata": {},
   "source": [
    "Congratulations on completing Chapter 1! Now that we have clean data, we're ready to explore. Coming up in Chapter 2, we'll look at distributions of variables in the General Social Survey and explore the relationship between education and income."
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
