{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5ce16721",
   "metadata": {},
   "source": [
    "# Predictions and model objects\n",
    "\n",
    "## Predicting house prices\n",
    "Perhaps the most useful feature of statistical models like linear regression is that you can make predictions. That is, you specify values for each of the explanatory variables, feed them to the model, and get a prediction for the corresponding response variable. The code flow is as follows.\n",
    "```python\n",
    "explanatory_data = pd.DataFrame({\"explanatory_var\": list_of_values})\n",
    "predictions = model.predict(explanatory_data)\n",
    "prediction_data = explanatory_data.assign(response_var=predictions)\n",
    "```\n",
    "Here, you'll make predictions for the house prices in the Taiwan real estate dataset.\n",
    "\n",
    "`taiwan_real_estate` is available. The fitted linear regression model of house price versus number of convenience stores is available as `mdl_price_vs_conv`. For future exercises, when a model is available, it will also be fitted.\n",
    "\n",
    "* Import the numpy package using the alias np.\n",
    "* Create a DataFrame of explanatory data, where the number of convenience stores, `n_convenience`, takes the integer values from zero to ten.\n",
    "* Print `explanatory_data`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9a71d78e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    n_convenience\n",
      "0               0\n",
      "1               1\n",
      "2               2\n",
      "3               3\n",
      "4               4\n",
      "5               5\n",
      "6               6\n",
      "7               7\n",
      "8               8\n",
      "9               9\n",
      "10             10\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "from statsmodels.formula.api import ols\n",
    "\n",
    "taiwan_real_estate = pd.read_csv('datasets/taiwan_real_estate2.csv')\n",
    "mdl_price_vs_conv = ols(\"price_twd_msq ~ n_convenience\", data=taiwan_real_estate)\n",
    "mdl_price_vs_conv = mdl_price_vs_conv.fit()\n",
    "\n",
    "# Create the explanatory_data \n",
    "explanatory_data = pd.DataFrame({'n_convenience': np.arange(0, 11)})\n",
    "\n",
    "# Print it\n",
    "print(explanatory_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b71bec4",
   "metadata": {},
   "source": [
    "* Use the model `mdl_price_vs_conv` to make predictions from `explanatory_data` and store it as `price_twd_msq`.\n",
    "* Print the predictions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7e5ea2e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      8.224237\n",
      "1      9.022317\n",
      "2      9.820397\n",
      "3     10.618477\n",
      "4     11.416556\n",
      "5     12.214636\n",
      "6     13.012716\n",
      "7     13.810795\n",
      "8     14.608875\n",
      "9     15.406955\n",
      "10    16.205035\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Use mdl_price_vs_conv to predict with explanatory_data, call it price_twd_msq\n",
    "price_twd_msq = mdl_price_vs_conv.predict(explanatory_data)\n",
    "\n",
    "# Print it\n",
    "print(price_twd_msq)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c6fa90a",
   "metadata": {},
   "source": [
    "* Create a DataFrame of predictions named `prediction_data`. Start with `explanatory_data`, then add an extra column, `price_twd_msq`, containing the predictions you created in the previous step."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cf07aeb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    n_convenience  price_twd_msq\n",
      "0               0       8.224237\n",
      "1               1       9.022317\n",
      "2               2       9.820397\n",
      "3               3      10.618477\n",
      "4               4      11.416556\n",
      "5               5      12.214636\n",
      "6               6      13.012716\n",
      "7               7      13.810795\n",
      "8               8      14.608875\n",
      "9               9      15.406955\n",
      "10             10      16.205035\n"
     ]
    }
   ],
   "source": [
    "# Create prediction_data\n",
    "prediction_data = explanatory_data.assign(\n",
    "                  price_twd_msq = price_twd_msq)\n",
    "\n",
    "# Print the result\n",
    "print(prediction_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4be3c4b",
   "metadata": {},
   "source": [
    "Premium predicting! Having the predictions in a DataFrame will make it easier to visualize them.\n",
    "\n",
    "## Visualizing predictions\n",
    "The prediction DataFrame you created contains a column of explanatory variable values and a column of response variable values. That means you can plot it on the same scatter plot of response versus explanatory data values.\n",
    "\n",
    "* Create a new figure to plot multiple layers.\n",
    "* Extend the plotting code to add points for the predictions in `prediction_data`. Color the points red.\n",
    "* Display the layered plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "718778c1",
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
    "# Create a new figure, fig\n",
    "fig = plt.figure()\n",
    "\n",
    "sns.regplot(x=\"n_convenience\",\n",
    "            y=\"price_twd_msq\",\n",
    "            data=taiwan_real_estate,\n",
    "            ci=None)\n",
    "# Add a scatter plot layer to the regplot\n",
    "sns.scatterplot(x=\"n_convenience\",\n",
    "                y=\"price_twd_msq\",\n",
    "                data=prediction_data,\n",
    "                color=\"red\")\n",
    "\n",
    "# Show the layered plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb17115e",
   "metadata": {},
   "source": [
    "Perfect prediction plotting! Naturally, the predicted points lie on the trend line.\n",
    "\n",
    "## The limits of prediction\n",
    "In the last exercise, you made predictions on some sensible, could-happen-in-real-life, situations. That is, the cases when the number of nearby convenience stores were between zero and ten. To test the limits of the model's ability to predict, try some impossible situations.\n",
    "\n",
    "Use the console to try predicting house prices from `mdl_price_vs_conv` when there are -1 convenience stores. Do the same for 2.5 convenience stores. What happens in each case?\n",
    "\n",
    "* Create some impossible explanatory data. Define a DataFrame impossible with one column, `n_convenience`, set to -1 in the first row, and 2.5 in the second row."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "be5c98a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define a DataFrame impossible\n",
    "impossible = pd.DataFrame({\"n_convenience\": [-1, 2.5]})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb652f3a",
   "metadata": {},
   "source": [
    "Try making predictions on your two impossible cases. What happens?\n",
    "\n",
    "* The model throws an error because these cases are impossible in real life.\n",
    "\n",
    "* The model throws a warning because these cases are impossible in real life.\n",
    "\n",
    "* **The model successfully gives a prediction about cases that are impossible in real life.**\n",
    "\n",
    "* The model throws an error for -1 stores because it violates the assumptions of a linear regression. 2.5 stores gives a successful prediction.\n",
    "\n",
    "* The model throws an error for 2.5 stores because it violates the assumptions of a linear regression. -1 stores gives a successful prediction.\n",
    "\n",
    "Legendary limit detection! Linear models don't know what is possible or not in real life. That means that they can give you predictions that don't make any sense when applied to your data. You need to understand what your data means in order to determine whether a prediction is nonsense or not.\n",
    "\n",
    "## Extracting model elements\n",
    "The model object created by `ols()` contains many elements. In order to perform further analysis on the model results, you need to extract its useful bits. The model coefficients, the fitted values, and the residuals are perhaps the most important pieces of the linear model object.\n",
    "\n",
    "* Print the parameters of `mdl_price_vs_conv`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d6321f1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Intercept        8.224237\n",
      "n_convenience    0.798080\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Print the model parameters of mdl_price_vs_conv\n",
    "print(mdl_price_vs_conv.params)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "342c1a42",
   "metadata": {},
   "source": [
    "* Print the fitted values of `mdl_price_vs_conv`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "98b7f172",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      16.205035\n",
      "1      15.406955\n",
      "2      12.214636\n",
      "3      12.214636\n",
      "4      12.214636\n",
      "         ...    \n",
      "409     8.224237\n",
      "410    15.406955\n",
      "411    13.810795\n",
      "412    12.214636\n",
      "413    15.406955\n",
      "Length: 414, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Print the fitted values of mdl_price_vs_conv\n",
    "print(mdl_price_vs_conv.fittedvalues)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29e23eb2",
   "metadata": {},
   "source": [
    "* Print the residuals of `mdl_price_vs_conv`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c202c1d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     -4.737561\n",
      "1     -2.638422\n",
      "2      2.097013\n",
      "3      4.366302\n",
      "4      0.826211\n",
      "         ...   \n",
      "409   -3.564631\n",
      "410   -0.278362\n",
      "411   -1.526378\n",
      "412    3.670387\n",
      "413    3.927387\n",
      "Length: 414, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Print the residuals of mdl_price_vs_conv\n",
    "print(mdl_price_vs_conv.resid)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "109e4309",
   "metadata": {},
   "source": [
    "* Print a summary of `mdl_price_vs_conv`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f38e5f7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:          price_twd_msq   R-squared:                       0.326\n",
      "Model:                            OLS   Adj. R-squared:                  0.324\n",
      "Method:                 Least Squares   F-statistic:                     199.3\n",
      "Date:                Thu, 21 Jul 2022   Prob (F-statistic):           3.41e-37\n",
      "Time:                        18:41:34   Log-Likelihood:                -1091.1\n",
      "No. Observations:                 414   AIC:                             2186.\n",
      "Df Residuals:                     412   BIC:                             2194.\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "=================================================================================\n",
      "                    coef    std err          t      P>|t|      [0.025      0.975]\n",
      "---------------------------------------------------------------------------------\n",
      "Intercept         8.2242      0.285     28.857      0.000       7.664       8.784\n",
      "n_convenience     0.7981      0.057     14.118      0.000       0.687       0.909\n",
      "==============================================================================\n",
      "Omnibus:                      171.927   Durbin-Watson:                   1.993\n",
      "Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1417.242\n",
      "Skew:                           1.553   Prob(JB):                    1.78e-308\n",
      "Kurtosis:                      11.516   Cond. No.                         8.87\n",
      "==============================================================================\n",
      "\n",
      "Notes:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "# Print a summary of mdl_price_vs_conv\n",
    "print(mdl_price_vs_conv.summary())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "30cabc6a",
   "metadata": {},
   "source": [
    "Marvelous model manipulation! Working with individual pieces of the model is often more useful than working with the whole model object at once.\n",
    "\n",
    "## Manually predicting house prices\n",
    "You can manually calculate the predictions from the model coefficients. When making predictions in real life, it is better to use `.predict()`, but doing this manually is helpful to reassure yourself that predictions aren't magic - they are simply arithmetic.\n",
    "\n",
    "In fact, for a simple linear regression, the predicted value is just the intercept plus the slope times the explanatory variable.\n",
    "```\n",
    "response = intercept + slope * explanatory\n",
    "```\n",
    "\n",
    "* Get the coefficients/parameters of `mdl_price_vs_conv`, assigning to coeffs.\n",
    "* Get the intercept, which is the first element of coeffs, assigning to intercept.\n",
    "* Get the slope, which is the second element of coeffs, assigning to slope.\n",
    "* Manually predict `price_twd_msq` using the formula, specifying the intercept, slope, and `explanatory_data`.\n",
    "* Run the code to compare your manually calculated predictions to the results from `.predict()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "67c15c91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    n_convenience\n",
      "0        8.224237\n",
      "1        9.022317\n",
      "2        9.820397\n",
      "3       10.618477\n",
      "4       11.416556\n",
      "5       12.214636\n",
      "6       13.012716\n",
      "7       13.810795\n",
      "8       14.608875\n",
      "9       15.406955\n",
      "10      16.205035\n",
      "    n_convenience  predictions_auto\n",
      "0        8.224237          8.224237\n",
      "1        9.022317          9.022317\n",
      "2        9.820397          9.820397\n",
      "3       10.618477         10.618477\n",
      "4       11.416556         11.416556\n",
      "5       12.214636         12.214636\n",
      "6       13.012716         13.012716\n",
      "7       13.810795         13.810795\n",
      "8       14.608875         14.608875\n",
      "9       15.406955         15.406955\n",
      "10      16.205035         16.205035\n"
     ]
    }
   ],
   "source": [
    "# Get the coefficients of mdl_price_vs_conv\n",
    "coeffs = mdl_price_vs_conv.params\n",
    "\n",
    "# Get the intercept\n",
    "intercept = coeffs[0]\n",
    "\n",
    "# Get the slope\n",
    "slope = coeffs[1]\n",
    "\n",
    "# Manually calculate the predictions\n",
    "price_twd_msq = intercept + slope * explanatory_data\n",
    "print(price_twd_msq)\n",
    "\n",
    "# Compare to the results from .predict()\n",
    "print(price_twd_msq.assign(predictions_auto=mdl_price_vs_conv.predict(explanatory_data)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc8c2454",
   "metadata": {},
   "source": [
    "Magic manual prediction! For simple linear regression, the prediction just involves one addition and one multiplication.\n",
    "\n",
    "## Home run!\n",
    "Regression to the mean is an important concept in many areas, including sports.\n",
    "\n",
    "Here you can see a dataset of baseball batting data in 2017 and 2018. Each point represents a player, and more home runs are better. A naive prediction might be that the performance in 2018 is the same as the performance in 2017. That is, a linear regression would lie on the \"y equals x\" line.\n",
    "\n",
    "Explore the plot and make predictions. What does regression to the mean say about the number of home runs in 2018 for a player who was very successful in 2017?\n",
    "\n",
    "* Someone who hit 40 home runs in 2017 is predicted to hit the same number of home runs the next year because regression to the mean states that performance is consistent over time.\n",
    "\n",
    "* If someone hit 40 home runs in 2017, we can't predict the number of home runs the next year because regression to the mean states that extremely high values are unpredictable.\n",
    "\n",
    "* **Someone who hit 40 home runs in 2017 is predicted to hit 10 fewer home runs the next year because regression to the mean states that, on average, extremely high values are not sustained.**\n",
    "\n",
    "* Someone who hit 40 home runs in 2017 is predicted to hit 10 more home runs the next year because regression to the mean states that, on average, extremely high values are amplified over time.\n",
    "\n",
    "Magnificent regression to the mean! Due to regression to the mean, it's common that one player or team that does really well one year, doesn't do as well the next. Likewise players or teams that perform very badly one year do better the next year.\n",
    "\n",
    "## Plotting consecutive portfolio returns\n",
    "Regression to the mean is also an important concept in investing. Here you'll look at the annual returns from investing in companies in the Standard and Poor 500 index (S&P 500), in 2018 and 2019.\n",
    "\n",
    "The `sp500_yearly_returns` dataset contains three columns:\n",
    "```\n",
    "variable\tmeaning\n",
    "symbol\tStock ticker symbol uniquely identifying the company.\n",
    "return_2018\tA measure of investment performance in 2018.\n",
    "return_2019\tA measure of investment performance in 2019.\n",
    "```\n",
    "A positive number for the return means the investment increased in value; negative means it lost value.\n",
    "\n",
    "Just as with baseball home runs, a naive prediction might be that the investment performance stays the same from year to year, lying on the y equals x line.\n",
    "\n",
    "* Create a new figure, fig, to enable plot layering.\n",
    "* Generate a line at y equals x. This has been done for you.\n",
    "* Using `sp500_yearly_returns`, draw a scatter plot of `return_2019` vs. `return_2018` with a linear regression trend line, without a standard error ribbon.\n",
    "* Set the axes so that the distances along the x and y axes look the same."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "78b88cd1",
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
    "sp500_yearly_returns = pd.read_csv('datasets/sp500_yearly_returns.csv')\n",
    "\n",
    "# Create a new figure, fig\n",
    "fig = plt.figure()\n",
    "\n",
    "# Plot the first layer: y = x\n",
    "plt.axline(xy1=(0,0), slope=1, linewidth=2, color=\"green\")\n",
    "\n",
    "# Add scatter plot with linear regression trend line\n",
    "sns.regplot(x=\"return_2018\", y=\"return_2019\", data=sp500_yearly_returns, ci=None)\n",
    "\n",
    "# Set the axes so that the distances along the x and y axes look the same\n",
    "plt.axis(\"equal\")\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5672f68",
   "metadata": {},
   "source": [
    "Super scatter plotting! The regression trend line looks very different to the y equals x line. As the financial advisors say, \"Past performance is no guarantee of future results.\"\n",
    "\n",
    "## Modeling consecutive returns\n",
    "Let's quantify the relationship between returns in 2019 and 2018 by running a linear regression and making predictions. By looking at companies with extremely high or extremely low returns in 2018, we can see if their performance was similar in 2019.\n",
    "\n",
    "* Run a linear regression on `return_2019` versus `return_2018` using `sp500_yearly_returns` and fit the model. Assign to `mdl_returns`.\n",
    "* Print the parameters of the model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c9209a58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Intercept      0.321321\n",
      "return_2018    0.020069\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Run a linear regression on return_2019 vs. return_2018 using sp500_yearly_returns\n",
    "mdl_returns = ols(\"return_2019 ~ return_2018\", data=sp500_yearly_returns).fit()\n",
    "\n",
    "# Print the parameters\n",
    "print(mdl_returns.params)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1dd6ae4f",
   "metadata": {},
   "source": [
    "* Create a DataFrame named `explanatory_data`. Give it one column (return_2018) with 2018 returns set to a list containing -1, 0, and 1.\n",
    "* Use `mdl_returns` to predict with `explanatory_data` in a `print()` call."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2e2f4a0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    0.301251\n",
      "1    0.321321\n",
      "2    0.341390\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Create a DataFrame with return_2018 at -1, 0, and 1 \n",
    "explanatory_data = pd.DataFrame({\"return_2018\": [-1, 0, 1]})\n",
    "\n",
    "# Use mdl_returns to predict with explanatory_data\n",
    "print(mdl_returns.predict(explanatory_data))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc60d54c",
   "metadata": {},
   "source": [
    "Incredible investment predictions! Investments that gained a lot in value in 2018 on average gained only a small amount in 2019. Similarly, investments that lost a lot of value in 2018 on average also gained a small amount in 2019.\n",
    "\n",
    "## Transforming the explanatory variable\n",
    "If there is no straight-line relationship between the response variable and the explanatory variable, it is sometimes possible to create one by transforming one or both of the variables. Here, you'll look at transforming the explanatory variable.\n",
    "\n",
    "You'll take another look at the Taiwan real estate dataset, this time using the distance to the nearest MRT (metro) station as the explanatory variable. You'll use code to make every commuter's dream come true: shortening the distance to the metro station by taking the square root. Take that, geography!\n",
    "\n",
    "* Look at the plot.\n",
    "* Add a new column to `taiwan_real_estate` called `sqrt_dist_to_mrt_m that` contains the square root of `dist_to_mrt_m`.\n",
    "* Create the same scatter plot as the first one, but use the new transformed variable on the x-axis instead.\n",
    "* Look at the new plot. Notice how the numbers on the x-axis have changed. This is a different line to what was shown before. Do the points track the line more closely?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ce20b482",
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
    "# Create sqrt_dist_to_mrt_m\n",
    "taiwan_real_estate[\"sqrt_dist_to_mrt_m\"] = np.sqrt(taiwan_real_estate[\"dist_to_mrt_m\"])\n",
    "\n",
    "plt.figure()\n",
    "\n",
    "# Plot using the transformed variable\n",
    "sns.regplot(x=\"sqrt_dist_to_mrt_m\", y=\"price_twd_msq\", data=taiwan_real_estate, ci=None)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce0adec8",
   "metadata": {},
   "source": [
    "* Run a linear regression of `price_twd_msq` versus the square root of `dist_to_mrt_m` using `taiwan_real_estate`.\n",
    "* Print the parameters."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "da181c61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Intercept             16.709799\n",
      "sqrt_dist_to_mrt_m    -0.182843\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Run a linear regression of price_twd_msq vs. square root of dist_to_mrt_m using taiwan_real_estate\n",
    "mdl_price_vs_dist = ols(\"price_twd_msq ~ sqrt_dist_to_mrt_m\", data=taiwan_real_estate).fit()\n",
    "\n",
    "# Print the parameters\n",
    "print(mdl_price_vs_dist.params)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d296f816",
   "metadata": {},
   "source": [
    "* Create a DataFrame of predictions named `prediction_data` by adding a column of predictions called `price_twd_msq` to `explanatory_data`. Predict using `mdl_price_vs_dist` and `explanatory_data`.\n",
    "* Print the predictions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fa234e90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   sqrt_dist_to_mrt_m  dist_to_mrt_m  price_twd_msq\n",
      "0                 0.0              0      16.709799\n",
      "1                10.0            100      14.881370\n",
      "2                20.0            400      13.052942\n",
      "3                30.0            900      11.224513\n",
      "4                40.0           1600       9.396085\n",
      "5                50.0           2500       7.567656\n",
      "6                60.0           3600       5.739227\n",
      "7                70.0           4900       3.910799\n",
      "8                80.0           6400       2.082370\n"
     ]
    }
   ],
   "source": [
    "explanatory_data = pd.DataFrame({\"sqrt_dist_to_mrt_m\": np.sqrt(np.arange(0, 81, 10) ** 2),\n",
    "                                \"dist_to_mrt_m\": np.arange(0, 81, 10) ** 2})\n",
    "\n",
    "# Create prediction_data by adding a column of predictions to explantory_data\n",
    "prediction_data = explanatory_data.assign(\n",
    "    price_twd_msq = mdl_price_vs_dist.predict(explanatory_data)\n",
    "    )\n",
    "\n",
    "# Print the result\n",
    "print(prediction_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "27c27aae",
   "metadata": {},
   "source": [
    "* Add a layer to your plot containing points from `prediction_data`, colored \"red\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2ade4f46",
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
    "fig = plt.figure()\n",
    "sns.regplot(x=\"sqrt_dist_to_mrt_m\", y=\"price_twd_msq\", data=taiwan_real_estate, ci=None)\n",
    "\n",
    "# Add a layer of your prediction points\n",
    "sns.scatterplot(x=\"sqrt_dist_to_mrt_m\", y=\"price_twd_msq\", data=prediction_data, color=\"red\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c791ef7e",
   "metadata": {},
   "source": [
    "You transform like a robot in disguise! By transforming the explanatory variable, the relationship with the response variable became linear, and so a linear regression became an appropriate model.\n",
    "\n",
    "## Transforming the response variable too\n",
    "The response variable can be transformed too, but this means you need an extra step at the end to undo that transformation. That is, you \"back transform\" the predictions.\n",
    "\n",
    "In the video, you saw the first step of the digital advertising workflow: spending money to buy ads, and counting how many people see them (the \"impressions\"). The next step is determining how many people click on the advert after seeing it.\n",
    "\n",
    "* Look at the plot.\n",
    "* Create a `qdrt_n_impressions` column using `n_impressions` raised to the power of 0.25.\n",
    "* Create a `qdrt_n_clicks` column using `n_clicks` raised to the power of 0.25.\n",
    "* Create a regression plot using the transformed variables. Do the points track the line more closely?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f8529d62",
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
    "ad_conversion = pd.read_csv('datasets/ad_conversion.csv')\n",
    "\n",
    "# Create qdrt_n_impressions and qdrt_n_clicks\n",
    "ad_conversion[\"qdrt_n_impressions\"] = ad_conversion[\"n_impressions\"] ** 0.25\n",
    "ad_conversion[\"qdrt_n_clicks\"] = ad_conversion[\"n_clicks\"] ** 0.25\n",
    "\n",
    "plt.figure()\n",
    "\n",
    "# Plot using the transformed variables\n",
    "sns.regplot(x=\"qdrt_n_impressions\", y=\"qdrt_n_clicks\", data=ad_conversion, ci=None)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b7f169c",
   "metadata": {},
   "source": [
    "* Run a linear regression of `qdrt_n_clicks` versus `qdrt_n_impressions` using `ad_conversion` and assign it to `mdl_click_vs_impression`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "adb43a40",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run a linear regression of your transformed variables\n",
    "mdl_click_vs_impression = ols(\"qdrt_n_clicks ~ qdrt_n_impressions\", data=ad_conversion).fit()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c24f469",
   "metadata": {},
   "source": [
    "* Complete the code to create the prediction data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "027d10bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   qdrt_n_impressions  n_impressions  qdrt_n_clicks\n",
      "0            0.000000            0.0       0.071748\n",
      "1           26.591479       500000.0       3.037576\n",
      "2           31.622777      1000000.0       3.598732\n",
      "3           34.996355      1500000.0       3.974998\n",
      "4           37.606031      2000000.0       4.266063\n",
      "5           39.763536      2500000.0       4.506696\n",
      "6           41.617915      3000000.0       4.713520\n"
     ]
    }
   ],
   "source": [
    "explanatory_data = pd.DataFrame({\"qdrt_n_impressions\": np.arange(0, 3e6+1, 5e5) ** .25,\n",
    "                                 \"n_impressions\": np.arange(0, 3e6+1, 5e5)})\n",
    "\n",
    "# Complete prediction_data\n",
    "prediction_data = explanatory_data.assign(\n",
    "    qdrt_n_clicks = mdl_click_vs_impression.predict(explanatory_data)\n",
    ")\n",
    "\n",
    "# Print the result\n",
    "print(prediction_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9ec16023",
   "metadata": {},
   "source": [
    "Terrific transformation! Since the response variable has been transformed, you'll now need to back-transform the predictions to correctly interpret your results.\n",
    "\n",
    "## Back transformation\n",
    "In the previous exercise, you transformed the response variable, ran a regression, and made predictions. But you're not done yet! In order to correctly interpret and visualize your predictions, you'll need to do a back-transformation.\n",
    "\n",
    "* Back transform the response variable in `prediction_data` by raising `qdrt_n_clicks` to the power 4 to get `n_clicks`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9c9d974c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   qdrt_n_impressions  n_impressions  qdrt_n_clicks    n_clicks\n",
      "0            0.000000            0.0       0.071748    0.000026\n",
      "1           26.591479       500000.0       3.037576   85.135121\n",
      "2           31.622777      1000000.0       3.598732  167.725102\n",
      "3           34.996355      1500000.0       3.974998  249.659131\n",
      "4           37.606031      2000000.0       4.266063  331.214159\n",
      "5           39.763536      2500000.0       4.506696  412.508546\n",
      "6           41.617915      3000000.0       4.713520  493.607180\n"
     ]
    }
   ],
   "source": [
    "# Back transform qdrt_n_clicks\n",
    "prediction_data[\"n_clicks\"] = prediction_data[\"qdrt_n_clicks\"] ** 4\n",
    "print(prediction_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "032aee4f",
   "metadata": {},
   "source": [
    "* Edit the plot to add a layer of points from `prediction_data`, colored \"red\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "7d9aa436",
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
    "# Plot the transformed variables\n",
    "fig = plt.figure()\n",
    "sns.regplot(x=\"qdrt_n_impressions\", y=\"qdrt_n_clicks\", data=ad_conversion, ci=None)\n",
    "\n",
    "# Add a layer of your prediction points\n",
    "sns.scatterplot(x=\"qdrt_n_impressions\", y=\"qdrt_n_clicks\", data=prediction_data, color=\"red\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7be31088",
   "metadata": {},
   "source": [
    "Brilliant back transformation! Notice that your back-transformed predictions nicely follow the trend line and allow you to make more accurate predictions."
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
