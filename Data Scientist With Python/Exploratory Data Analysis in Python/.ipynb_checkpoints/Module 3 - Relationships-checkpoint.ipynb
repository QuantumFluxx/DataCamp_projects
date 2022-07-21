{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f76d92f0",
   "metadata": {},
   "source": [
    "# Relationships\n",
    "\n",
    "## PMF of age\n",
    "Do people tend to gain weight as they get older? We can answer this question by visualizing the relationship between weight and age. But before we make a scatter plot, it is a good idea to visualize distributions one variable at a time. Here, you'll visualize age using a bar chart first. Recall that all PMF objects have a `.bar()` method to make a bar chart.\n",
    "\n",
    "The BRFSS dataset includes a variable, 'AGE' (note the capitalization!), which represents each respondent's age. To protect respondents' privacy, ages are rounded off into 5-year bins. 'AGE' contains the midpoint of the bins.\n",
    "\n",
    "* Extract the variable 'AGE' from the DataFrame brfss and assign it to age.\n",
    "* Get the PMF of age and plot it as a bar chart."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcefc8ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Extract AGE\n",
    "age = brfss['AGE']\n",
    "\n",
    "# Plot the PMF\n",
    "pmf_age = Pmf(age)\n",
    "pmf_age.bar()\n",
    "\n",
    "# Label the axes\n",
    "plt.xlabel('Age in years')\n",
    "plt.ylabel('PMF')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac4ae442",
   "metadata": {},
   "source": [
    "Ok, we're off to a good start. Notice that the last age range is bigger than the others. That's the kind of thing you see when you plot distributions.\n",
    "\n",
    "## Scatter plot\n",
    "Now let's make a scatterplot of weight versus age. To make the code run faster, I've selected only the first 1000 rows from the brfss DataFrame.\n",
    "\n",
    "weight and age have already been extracted for you. Your job is to use `plt.plot()` to make a scatter plot.\n",
    "\n",
    "* Make a scatter plot of weight and age with format string 'o' and alpha=0.1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f52ceb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Select the first 1000 respondents\n",
    "brfss = brfss[:1000]\n",
    "\n",
    "# Extract age and weight\n",
    "age = brfss['AGE']\n",
    "weight = brfss['WTKG3']\n",
    "\n",
    "# Make a scatter plot\n",
    "plt.plot(age, weight, 'o', alpha=0.1)\n",
    "\n",
    "plt.xlabel('Age in years')\n",
    "plt.ylabel('Weight in kg')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f01e38c",
   "metadata": {},
   "source": [
    "So far so good. By adjusting alpha we can avoid saturating the plot. Next we'll jitter the data to break up the columns.\n",
    "\n",
    "## Jittering\n",
    "In the previous exercise, the ages fall in columns because they've been rounded into 5-year bins. If we jitter them, the scatter plot will show the relationship more clearly. Recall how Allen jittered height and weight in the video:\n",
    "```python\n",
    "height_jitter = height + np.random.normal(0, 2, size=len(brfss))\n",
    "weight_jitter = weight + np.random.normal(0, 2, size=len(brfss))\n",
    "```\n",
    "\n",
    "* Add random noise to age with mean 0 and standard deviation 2.5.\n",
    "* Make a scatter plot between weight and age with marker size 5 and alpha=0.2. Be sure to also specify 'o'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5ea7984",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Select the first 1000 respondents\n",
    "brfss = brfss[:1000]\n",
    "\n",
    "# Add jittering to age\n",
    "age = brfss['AGE'] + np.random.normal(0, 2.5, size=len(brfss))\n",
    "# Extract weight\n",
    "weight = brfss['WTKG3']\n",
    "\n",
    "# Make a scatter plot\n",
    "plt.plot(age, weight, 'o', markersize=5, alpha=0.2)\n",
    "\n",
    "plt.xlabel('Age in years')\n",
    "plt.ylabel('Weight in kg')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a607e22",
   "metadata": {},
   "source": [
    "Excellent. By smoothing out the ages and avoiding saturation, we get the best view of the data. But in this case the nature of the relationship is still hard to see. In the next lesson, we'll see some other ways to visualize it.\n",
    "\n",
    "## Height and weight\n",
    "Previously we looked at a scatter plot of height and weight, and saw that taller people tend to be heavier. Now let's take a closer look using a box plot. The brfss DataFrame contains a variable '_HTMG10' that represents height in centimeters, binned into 10 cm groups.\n",
    "\n",
    "Recall how Allen created the box plot of 'AGE' and 'WTKG3' in the video, with the y-axis on a logarithmic scale:\n",
    "```python\n",
    "sns.boxplot(x='AGE', y='WTKG3', data=data, whis=10)\n",
    "plt.yscale('log')\n",
    "```\n",
    "\n",
    "* Fill in the parameters of `.boxplot()` to plot the distribution of weight ('WTKG3') in each height ('_HTMG10') group. Specify whis=10, just as was done in the video.\n",
    "* Add a line to plot the y-axis on a logarithmic scale."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b1ae1fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop rows with missing data\n",
    "data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])\n",
    "\n",
    "# Make a box plot\n",
    "sns.boxplot(x='_HTMG10', y='WTKG3', data=data, whis=10)\n",
    "\n",
    "# Plot the y-axis on a log scale\n",
    "plt.yscale('log')\n",
    "\n",
    "# Remove unneeded lines and label axes\n",
    "sns.despine(left=True, bottom=True)\n",
    "plt.xlabel('Height in cm')\n",
    "plt.ylabel('Weight in kg')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0fb0f5ce",
   "metadata": {},
   "source": [
    "Very good. These box plots provide a good view of the relationship between the variables. They also show the spread of the values in each column.\n",
    "\n",
    "## Distribution of income\n",
    "In the next two exercises we'll look at relationships between income and other variables. In the BRFSS, income is represented as a categorical variable; that is, respondents are assigned to one of 8 income categories. The variable name is 'INCOME2'. Before we connect income with anything else, let's look at the distribution by computing the PMF. Recall that all Pmf objects have a `.bar()` method.\n",
    "\n",
    "* Extract 'INCOME2' from the brfss DataFrame and assign it to income.\n",
    "* Plot the PMF of income as a bar chart."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38888f93",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Extract income\n",
    "income = brfss['INCOME2']\n",
    "\n",
    "# Plot the PMF\n",
    "Pmf(income).bar()\n",
    "\n",
    "# Label the axes\n",
    "plt.xlabel('Income level')\n",
    "plt.ylabel('PMF')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bef3253b",
   "metadata": {},
   "source": [
    "Good work. Almost half of the respondents are in the top income category, so this dataset doesn't distinguish between the highest incomes and the median. But maybe it can tell us something about people with incomes below the median.\n",
    "\n",
    "## Income and height\n",
    "Let's now use a violin plot to visualize the relationship between income and height.\n",
    "\n",
    "* Create a violin plot to plot the distribution of height ('HTM4') in each income ('INCOME2') group. Specify inner=None to simplify the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35ee7e66",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop rows with missing data\n",
    "data = brfss.dropna(subset=['INCOME2', 'HTM4'])\n",
    "\n",
    "# Make a violin plot\n",
    "sns.violinplot(x='INCOME2', y='HTM4', data=data, inner=None)\n",
    "\n",
    "# Remove unneeded lines and label axes\n",
    "sns.despine(left=True, bottom=True)\n",
    "plt.xlabel('Income level')\n",
    "plt.ylabel('Height in cm')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12d3753d",
   "metadata": {},
   "source": [
    "Interesting. It looks like there is a weak positive relationsip between income and height, at least for incomes below the median. In the next lesson we'll see some ways to quantify the strength of this relationship.\n",
    "\n",
    "## Computing correlations\n",
    "The purpose of the BRFSS is to explore health risk factors, so it includes questions about diet. The variable '_VEGESU1' represents the number of servings of vegetables respondents reported eating per day.\n",
    "\n",
    "Let's see how this variable relates to age and income.\n",
    "\n",
    "* From the brfss DataFrame, select the columns 'AGE', 'INCOME2', and '_VEGESU1'.\n",
    "* Compute the correlation matrix for these variables."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd92a8ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Select columns\n",
    "columns = ['AGE', 'INCOME2', '_VEGESU1']\n",
    "subset = brfss[columns]\n",
    "\n",
    "# Compute the correlation matrix\n",
    "print(subset.corr())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e885659",
   "metadata": {},
   "source": [
    "So far, so good. In the next exercise you'll think about how to interpret these results.\n",
    "\n",
    "## Interpreting correlations\n",
    "In the previous exercise, the correlation between income and vegetable consumption is about 0.12. The correlation between age and vegetable consumption is about -0.01.\n",
    "\n",
    "Which of the following are correct interpretations of these results:\n",
    "\n",
    "A: People with higher incomes eat more vegetables.\n",
    "B: The relationship between income and vegetable consumption is linear.\n",
    "C: Older people eat more vegetables.\n",
    "D: There could be a strong nonlinear relationship between age and vegetable consumption.\n",
    "\n",
    "* A and C only.\n",
    "\n",
    "* B and D only.\n",
    "\n",
    "* B and C only.\n",
    "\n",
    "* **A and D only.**\n",
    "\n",
    "Correct! The correlation between income and vegetable consumption is small, but it suggests that there is a relationship. But a correlation close to 0 does mean there is no relationship.\n",
    "\n",
    "## Income and vegetables\n",
    "As we saw in a previous exercise, the variable '_VEGESU1' represents the number of vegetable servings respondents reported eating per day.\n",
    "\n",
    "Let's estimate the slope of the relationship between vegetable consumption and income.\n",
    "\n",
    "* Extract the columns 'INCOME2' and '_VEGESU1' from subset into xs and ys respectively.\n",
    "* Compute the simple linear regression of these variables."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58576a37",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import linregress\n",
    "\n",
    "# Extract the variables\n",
    "subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])\n",
    "xs = subset['INCOME2']\n",
    "ys = subset['_VEGESU1']\n",
    "\n",
    "# Compute the linear regression\n",
    "res = linregress(xs, ys)\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8e721d4",
   "metadata": {},
   "source": [
    "Good job. The estimated slope tells you the increase in vegetable servings from one income group to the next.\n",
    "\n",
    "## Fit a line\n",
    "Continuing from the previous exercise:\n",
    "\n",
    "* Assume that xs and ys contain income codes and daily vegetable consumption, respectively, and\n",
    "\n",
    "* res contains the results of a simple linear regression of ys onto xs.\n",
    "\n",
    "Now, you're going to compute the line of best fit. NumPy has been imported for you as np. \n",
    "\n",
    "* Set fx to the minimum and maximum of xs, stored in a NumPy array.\n",
    "* Set fy to the points on the fitted line that correspond to the fx."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1c1717b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the scatter plot\n",
    "plt.clf()\n",
    "x_jitter = xs + np.random.normal(0, 0.15, len(xs))\n",
    "plt.plot(x_jitter, ys, 'o', alpha=0.2)\n",
    "\n",
    "# Plot the line of best fit\n",
    "fx = np.array([xs.min(), xs.max()])\n",
    "fy = res.intercept + res.slope * fx\n",
    "plt.plot(fx, fy, '-', alpha=0.7)\n",
    "\n",
    "plt.xlabel('Income code')\n",
    "plt.ylabel('Vegetable servings per day')\n",
    "plt.ylim([0, 6])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85ad17ed",
   "metadata": {},
   "source": [
    "Congratulations on completing Chapter 3! We've seen several ways to visualize relationships between variables and quantify their strength. In the next chapter we use regression to explore relationships among more than two variables."
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
