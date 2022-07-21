{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "691e7ffa",
   "metadata": {},
   "source": [
    "# Multivariate Thinking\n",
    "\n",
    "## Regression and causation\n",
    "In the BRFSS dataset, there is a strong relationship between vegetable consumption and income. The income of people who eat 8 servings of vegetables per day is double the income of people who eat none, on average.\n",
    "\n",
    "Which of the following conclusions can we draw from this data?\n",
    "\n",
    "A. Eating a good diet leads to better health and higher income.\n",
    "\n",
    "B. People with higher income can afford a better diet.\n",
    "\n",
    "C. People with high income are more likely to be vegetarians.\n",
    "\n",
    "* A only.\n",
    "\n",
    "* B only.\n",
    "\n",
    "* B and C.\n",
    "\n",
    "* **None of them.**\n",
    "\n",
    "That's right. This data is consistent with all of these conclusions, but it does not provide conclusive evidence for any of them.\n",
    "\n",
    "## Using StatsModels\n",
    "Let's run the same regression using `SciPy` and `StatsModels`, and confirm we get the same results.\n",
    "\n",
    "* Compute the regression of '_VEGESU1' as a function of 'INCOME2' using SciPy's `linregress()`.\n",
    "* Compute the regression of '_VEGESU1' as a function of 'INCOME2' using StatsModels' `smf.ols()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62185ad2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import linregress\n",
    "import statsmodels.formula.api as smf\n",
    "\n",
    "# Run regression with linregress\n",
    "subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])\n",
    "xs = subset['INCOME2']\n",
    "ys = subset['_VEGESU1']\n",
    "res = linregress(xs, ys)\n",
    "print(res)\n",
    "\n",
    "# Run regression with StatsModels\n",
    "results = smf.ols('_VEGESU1 ~ INCOME2', data=brfss).fit()\n",
    "print(results.params)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f522510d",
   "metadata": {},
   "source": [
    "Nice job. When you start working with a new library, checks like this help ensure that you are doing it right.\n",
    "\n",
    "## Plot income and education\n",
    "To get a closer look at the relationship between income and education, let's use the variable 'educ' to group the data, then plot mean income in each group.\n",
    "\n",
    "Here, the GSS dataset has been pre-loaded into a DataFrame called gss.\n",
    "\n",
    "* Group gss by 'educ'. Store the result in grouped.\n",
    "* From grouped, extract 'realinc' and compute the mean.\n",
    "* Plot `mean_income_by_educ` as a scatter plot. Specify 'o' and alpha=0.5."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef8cf317",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Group by educ\n",
    "grouped = gss.groupby('educ')\n",
    "\n",
    "# Compute mean income in each group\n",
    "mean_income_by_educ = grouped['realinc'].mean()\n",
    "\n",
    "# Plot mean income as a scatter plot\n",
    "plt.clf()\n",
    "plt.plot(mean_income_by_educ, 'o', alpha=0.5)\n",
    "\n",
    "# Label the axes\n",
    "plt.xlabel('Education (years)')\n",
    "plt.ylabel('Income (1986 $)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d8b7eed",
   "metadata": {},
   "source": [
    "Well done. It looks like the relationship between income and education is non-linear.\n",
    "\n",
    "## Non-linear model of education\n",
    "The graph in the previous exercise suggests that the relationship between income and education is non-linear. So let's try fitting a non-linear model.\n",
    "\n",
    "* Add a column named 'educ2' to the gss DataFrame; it should contain the values from 'educ' squared.\n",
    "* Run a regression model that uses 'educ', 'educ2', 'age', and 'age2' to predict 'realinc'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d421732f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import statsmodels.formula.api as smf\n",
    "\n",
    "# Add a new column with educ squared\n",
    "gss['educ2'] = gss['educ']**2\n",
    "\n",
    "# Run a regression model with educ, educ2, age, and age2\n",
    "results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()\n",
    "\n",
    "# Print the estimated parameters\n",
    "print(results.params)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b01a687",
   "metadata": {},
   "source": [
    "Excellent. The slope associated with educ2 is positive, so the model curves upward.\n",
    "\n",
    "## Making predictions\n",
    "At this point, we have a model that predicts income using age, education, and sex.\n",
    "\n",
    "Let's see what it predicts for different levels of education, holding age constant.\n",
    "\n",
    "* Using `np.linspace()`, add a variable named 'educ' to df with a range of values from 0 to 20.\n",
    "* Add a variable named 'age' with the constant value 30.\n",
    "* Use df to generate predicted income as a function of education."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b1a446a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run a regression model with educ, educ2, age, and age2\n",
    "results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()\n",
    "\n",
    "# Make the DataFrame\n",
    "df = pd.DataFrame()\n",
    "df['educ'] = np.linspace(0, 20)\n",
    "df['age'] = 30\n",
    "df['educ2'] = df['educ']**2\n",
    "df['age2'] = df['age']**2\n",
    "\n",
    "# Generate and plot the predictions\n",
    "pred = results.predict(df)\n",
    "print(pred.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71baf194",
   "metadata": {},
   "source": [
    "Nice job. Now let's see what the results look like.\n",
    "\n",
    "## Visualizing predictions\n",
    "Now let's visualize the results from the previous exercise!\n",
    "\n",
    "* Plot `mean_income_by_educ` using circles ('o'). Specify an alpha of 0.5.\n",
    "* Plot the prediction results with a line, with `df['educ']` on the x-axis and pred on the y-axis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bcaa34e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot mean income in each age group\n",
    "plt.clf()\n",
    "grouped = gss.groupby('educ')\n",
    "mean_income_by_educ = grouped['realinc'].mean()\n",
    "plt.plot(mean_income_by_educ, 'o', alpha=0.5)\n",
    "\n",
    "# Plot the predictions\n",
    "pred = results.predict(df)\n",
    "plt.plot(df['educ'], pred, label='Age 30')\n",
    "\n",
    "# Label axes\n",
    "plt.xlabel('Education (years)')\n",
    "plt.ylabel('Income (1986 $)')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1904a406",
   "metadata": {},
   "source": [
    "Looks like this model captures the relationship pretty well. Nice job.\n",
    "\n",
    "## Predicting a binary variable\n",
    "Let's use logistic regression to predict a binary variable. Specifically, we'll use age, sex, and education level to predict support for legalizing cannabis (marijuana) in the U.S.\n",
    "\n",
    "In the GSS dataset, the variable grass records the answer to the question \"Do you think the use of marijuana should be made legal or not?\"\n",
    "\n",
    "* Fill in the parameters of `smf.logit()` to predict grass using the variables age, age2, educ, and educ2, along with sex as a categorical variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f5ad0c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Recode grass\n",
    "gss['grass'].replace(2, 0, inplace=True)\n",
    "\n",
    "# Run logistic regression\n",
    "results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()\n",
    "results.params"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28dd47ae",
   "metadata": {},
   "source": [
    "* Add a column called educ and set it to 12 years; then compute a second column, educ2, which is the square of educ."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8899abd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Recode grass\n",
    "gss['grass'].replace(2, 0, inplace=True)\n",
    "\n",
    "# Run logistic regression\n",
    "results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()\n",
    "results.params\n",
    "\n",
    "# Make a DataFrame with a range of ages\n",
    "df = pd.DataFrame()\n",
    "df['age'] = np.linspace(18, 89)\n",
    "df['age2'] = df['age']**2\n",
    "\n",
    "# Set the education level to 12\n",
    "df['educ'] = 12\n",
    "df['educ2'] = df['educ']**2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4b29c45",
   "metadata": {},
   "source": [
    "* Generate separate predictions for men and women."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "873596bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate predictions for men and women\n",
    "df['sex'] = 1\n",
    "pred1 = results.predict(df)\n",
    "\n",
    "df['sex'] = 2\n",
    "pred2 = results.predict(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ca99ae2",
   "metadata": {},
   "source": [
    "* Fill in the missing code to compute the mean of 'grass' for each age group, and then the arguments of `plt.plot()` to plot pred2 versus `df['age']` with the label 'Female'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f06a7724",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.clf()\n",
    "grouped = gss.groupby('age')\n",
    "favor_by_age = grouped['grass'].mean()\n",
    "plt.plot(favor_by_age, 'o', alpha=0.5)\n",
    "\n",
    "plt.plot(df['age'], pred1, label='Male')\n",
    "plt.plot(df['age'], pred2, label='Female')\n",
    "\n",
    "plt.xlabel('Age')\n",
    "plt.ylabel('Probability of favoring legalization')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9688664b",
   "metadata": {},
   "source": [
    "You made it! Congratulations on completing this course. I hope you enjoyed it and learned a lot. Should you wish to use the Pmf and Cdf classes from this course in your own work, you can download the empiricaldist library here."
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
