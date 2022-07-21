{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d974d0ee",
   "metadata": {},
   "source": [
    "# Assessing model fit\n",
    "\n",
    "## Coefficient of determination\n",
    "The coefficient of determination is a measure of how well the linear regression line fits the observed values. For simple linear regression, it is equal to the square of the correlation between the explanatory and response variables.\n",
    "\n",
    "Here, you'll take another look at the second stage of the advertising pipeline: modeling the click response to impressions. Two models are available: `mdl_click_vs_impression_orig` models `n_clicks` versus `n_impressions`. `mdl_click_vs_impression_trans` is the transformed model you saw in Chapter 2. It models `n_clicks` to the power of 0.25 versus `n_impressions` to the power of 0.25.\n",
    "\n",
    "* Print the summary of `mdl_click_vs_impression_orig`.\n",
    "* Do the same for `mdl_click_vs_impression_trans`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f776be9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:          qdrt_n_clicks   R-squared:                       0.945\n",
      "Model:                            OLS   Adj. R-squared:                  0.944\n",
      "Method:                 Least Squares   F-statistic:                 1.590e+04\n",
      "Date:                Thu, 21 Jul 2022   Prob (F-statistic):               0.00\n",
      "Time:                        19:07:03   Log-Likelihood:                 193.90\n",
      "No. Observations:                 936   AIC:                            -383.8\n",
      "Df Residuals:                     934   BIC:                            -374.1\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "======================================================================================\n",
      "                         coef    std err          t      P>|t|      [0.025      0.975]\n",
      "--------------------------------------------------------------------------------------\n",
      "Intercept              0.0717      0.017      4.171      0.000       0.038       0.106\n",
      "qdrt_n_impressions     0.1115      0.001    126.108      0.000       0.110       0.113\n",
      "==============================================================================\n",
      "Omnibus:                       11.447   Durbin-Watson:                   0.568\n",
      "Prob(Omnibus):                  0.003   Jarque-Bera (JB):               10.637\n",
      "Skew:                          -0.216   Prob(JB):                      0.00490\n",
      "Kurtosis:                       2.707   Cond. No.                         52.1\n",
      "==============================================================================\n",
      "\n",
      "Notes:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
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
    "ad_conversion = pd.read_csv('datasets/ad_conversion.csv')\n",
    "ad_conversion[\"qdrt_n_impressions\"] = ad_conversion[\"n_impressions\"] ** 0.25\n",
    "ad_conversion[\"qdrt_n_clicks\"] = ad_conversion[\"n_clicks\"] ** 0.25\n",
    "mdl_click_vs_impression_orig = ols(\"qdrt_n_clicks ~ qdrt_n_impressions\", data=ad_conversion).fit()\n",
    "\n",
    "# Print a summary of mdl_click_vs_impression_orig\n",
    "print(mdl_click_vs_impression_orig.summary())\n",
    "\n",
    "# Print a summary of mdl_click_vs_impression_trans\n",
    "print(mdl_click_vs_impression_trans.summary())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "852ebad1",
   "metadata": {},
   "source": [
    "* Print the coefficient of determination for `mdl_click_vs_impression_orig`.\n",
    "* Do the same for `mdl_click_vs_impression_trans`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c6a58078",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9445272817143905\n"
     ]
    }
   ],
   "source": [
    "# Print the coeff of determination for mdl_click_vs_impression_orig\n",
    "print(mdl_click_vs_impression_orig.rsquared)\n",
    "\n",
    "# Print the coeff of determination for mdl_click_vs_impression_trans\n",
    "print(mdl_click_vs_impression_trans.rsquared)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d59fed3f",
   "metadata": {},
   "source": [
    "`mdl_click_vs_impression_orig` has a coefficient of determination of 0.89. Which statement about the model is true?\n",
    "\n",
    "* The number of clicks explains 89% of the variability in the number of impressions.\n",
    "\n",
    "* **The number of impressions explains 89% of the variability in the number of clicks.**\n",
    "\n",
    "* The model is correct 89% of the time.\n",
    "\n",
    "* The correlation between the number of impressions and the number of clicks is 0.89.\n",
    "-----\n",
    "Which model does the coefficient of determination suggest gives a better fit?\n",
    "\n",
    "* The original model, mdl_click_vs_impression_orig.\n",
    "\n",
    "* **The transformed model, mdl_click_vs_impression_trans.**\n",
    "\n",
    "* Both models are equally good.\n",
    "\n",
    "* Coefficient of determination doesn't measure the goodness of fit of a regression model.\n",
    "\n",
    "Cool coefficient of determination calculating! The transformed model has a higher coefficient of determination than the original model, suggesting that it gives a better fit to the data.\n",
    "\n",
    "## Residual standard error\n",
    "Residual standard error (RSE) is a measure of the typical size of the residuals. Equivalently, it's a measure of how wrong you can expect predictions to be. Smaller numbers are better, with zero being a perfect fit to the data.\n",
    "\n",
    "Again, you'll look at the models from the advertising pipeline, `mdl_click_vs_impression_orig` and `mdl_click_vs_impression_trans`.\n",
    "\n",
    "* Calculate the MSE of `mdl_click_vs_impression_orig`, assigning to `mse_orig`.\n",
    "* Using `mse_orig`, calculate and print the RSE of `mdl_click_vs_impression_orig`.\n",
    "* Do the same for `mdl_click_vs_impression_trans`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f95293d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RSE of original model:  0.19690640896875722\n"
     ]
    }
   ],
   "source": [
    "# Calculate mse_orig for mdl_click_vs_impression_orig\n",
    "mse_orig = mdl_click_vs_impression_orig.mse_resid\n",
    "\n",
    "# Calculate rse_orig for mdl_click_vs_impression_orig and print it\n",
    "rse_orig = np.sqrt(mse_orig)\n",
    "print(\"RSE of original model: \", rse_orig)\n",
    "\n",
    "# Calculate mse_trans for mdl_click_vs_impression_trans\n",
    "mse_trans = mdl_click_vs_impression_trans.mse_resid\n",
    "\n",
    "# Calculate rse_trans for mdl_click_vs_impression_trans and print it\n",
    "rse_trans = np.sqrt(mse_trans)\n",
    "print(\"RSE of transformed model: \", rse_trans)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "55b15f91",
   "metadata": {},
   "source": [
    "`mdl_click_vs_impression_orig` has an RSE of about 20. Which statement is true?\n",
    "\n",
    "* The model explains 20% of the variability in the number of clicks.\n",
    "\n",
    "* 20% of the residuals are typically greater than the observed values.\n",
    "\n",
    "* **The typical difference between observed number of clicks and predicted number of clicks is 20.**\n",
    "\n",
    "* The typical difference between observed number of impressions and predicted number of impressions is 20.\n",
    "\n",
    "* The model predicts that you get one click for every 20 observed impressions.\n",
    "\n",
    "----\n",
    "\n",
    "Which model does the RSE suggest gives more accurate predictions? `mdl_click_vs_impression_orig` has an RSE of about 20, `mdl_click_vs_impression_trans` has an RSE of about 0.2.\n",
    "\n",
    "* The original model, mdl_click_vs_impression_orig.\n",
    "\n",
    "* **The transformed model, mdl_click_vs_impression_trans.**\n",
    "\n",
    "* Both models are equally good.\n",
    "\n",
    "* RSE doesn't measure the accuracy of a regression model.\n",
    "\n",
    "Rapid RSE wrangling! RSE is a measure of accuracy for regression models. It even works on other other statistical model types like regression trees, so you can compare accuracy across different classes of models.\n",
    "\n",
    "## Residuals vs. fitted values\n",
    "Here you can see diagnostic plots of residuals versus fitted values for two models on advertising conversion.\n",
    "\n",
    "Original model (n_clicks versus n_impressions):\n",
    "![](https://assets.datacamp.com/production/repositories/5857/datasets/8b7ec146413ba268457315e4a3ae30f6020e5251/scatter-residuals-vs-fitted-ad-conversion-orig.png)\n",
    "Transformed model (n_clicks ** 0.25 versus n_impressions ** 0.25):\n",
    "![](https://assets.datacamp.com/production/repositories/5857/datasets/165029c2c48d021b9549bf4832068ee1cac641bb/scatter-residuals-vs-fitted-ad-conversion-trans.png)\n",
    "\n",
    "Look at the numbers on the y-axis scales and how well the trend lines follow the  line. Which statement is true?\n",
    "\n",
    "\n",
    "* The residuals track the y = 0 line more closely in the original model compared to the transformed model, indicating that the original model is a better fit for the data.\n",
    "\n",
    "* The residuals track the y = 0 line more closely in the transformed model compared to the original model, indicating that the original model is a better fit for the data.\n",
    "\n",
    "* The residuals track the y = 0 line more closely in the original model compared to the transformed model, indicating that the transformed model is a better fit for the data.\n",
    "\n",
    "* **The residuals track the y = 0 line more closely in the transformed model compared to the original model, indicating that the transformed model is a better fit for the data.**\n",
    "\n",
    "Dapper diagnosis! In a good model, the residuals should have a trend line close to zero.\n",
    "\n",
    "## Q-Q plot of residuals\n",
    "Here are normal Q-Q plots of the previous two models.\n",
    "\n",
    "Original model (n_clicks versus n_impressions):\n",
    "![](https://assets.datacamp.com/production/repositories/5857/datasets/3968b9c7f5383b28c6b79942a4be7f65191bcebd/qq-ad-conversion-orig.png)\n",
    "Transformed model (n_clicks ** 0.25 versus n_impressions ** 0.25):\n",
    "![](https://assets.datacamp.com/production/repositories/5857/datasets/d2258914128ea9f8ff2849531db15a5c059aac63/qq-ad-conversion-trans.png)\n",
    "Look at how well the points track the \"normality\" line. Which statement is true?\n",
    "\n",
    "* The residuals track the \"normality\" line more closely in the original model compared to the transformed model, indicating that the original model is a better fit for the data.\n",
    "\n",
    "* The residuals track the \"normality\" line more closely in the original model compared to the transformed model, indicating that the transformed model is a better fit for the data.\n",
    "\n",
    "* **The residuals track the \"normality\" line more closely in the transformed model compared to the original model, indicating that the transformed model is a better fit for the data.**\n",
    "\n",
    "* The residuals track the \"normality\" line more closely in the transformed model compared to the original model, indicating that the original model is a better fit for the data.\n",
    "\n",
    "You have Q-Q juju! If the residuals from the model are normally distributed, then the points will track the line on the Q-Q plot. In this case, neither model is perfect, but the transformed model is closer.\n",
    "\n",
    "## Scale-location\n",
    "Here are normal scale-location plots of the previous two models. That is, they show the size of residuals versus fitted values.\n",
    "\n",
    "Original model (n_clicks versus n_impressions):\n",
    "![](https://assets.datacamp.com/production/repositories/5857/datasets/722fd0c9e2099c905be0e0f53ac173b359e7ee2f/scale-location-ad-conversion-orig.png)\n",
    "Transformed model (n_clicks ** 0.25 versus n_impressions ** 0.25):\n",
    "![](https://assets.datacamp.com/production/repositories/5857/datasets/455734d8dd11692586a5b0c23a7e3c71830ea310/scale-location-ad-conversion-trans.png)\n",
    "Look at the numbers on the y-axis and the slope of the trend line. Which statement is true?\n",
    "\n",
    "\n",
    "* The size of the standardized residuals is more consistent in the original model compared to the transformed model, indicating that the original model is a better fit for the data.\n",
    "\n",
    "* **The size of the standardized residuals is more consistent in the transformed model compared to the original model, indicating that the transformed model is a better fit for the data.**\n",
    "\n",
    "* The size of the standardized residuals is more consistent in the transformed model compared to the original model, indicating that the original model is a better fit for the data.\n",
    "\n",
    "* The size of the standardized residuals is more consistent in the original model compared to the transformed model, indicating that the transformed model is a better fit for the data.\n",
    "\n",
    "Skillful scale-location analysis! In a good model, the size of the residuals shouldn't change much as the fitted values change.\n",
    "\n",
    "## Drawing diagnostic plots\n",
    "It's time for you to draw these diagnostic plots yourself using the Taiwan real estate dataset and the model of house prices versus number of convenience stores.\n",
    "\n",
    "* Create the residuals versus fitted values plot. Add a lowess argument to visualize the trend of the residuals."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c4723c34",
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
    "taiwan_real_estate = pd.read_csv('datasets/taiwan_real_estate2.csv')\n",
    "\n",
    "# Plot the residuals vs. fitted values\n",
    "sns.residplot(x=\"n_convenience\", y=\"price_twd_msq\", data=taiwan_real_estate, lowess=True)\n",
    "plt.xlabel(\"Fitted values\")\n",
    "plt.ylabel(\"Residuals\")\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd4e7678",
   "metadata": {},
   "source": [
    "* Import `qqplot()` from `statsmodels.api`.\n",
    "* Create the Q-Q plot of the residuals."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "229eaed1",
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
    "# Import qqplot\n",
    "from statsmodels.api import qqplot\n",
    "\n",
    "mdl_price_vs_conv = ols(\"price_twd_msq ~ n_convenience\", data=taiwan_real_estate)\n",
    "mdl_price_vs_conv = mdl_price_vs_conv.fit()\n",
    "\n",
    "# Create the Q-Q plot of the residuals\n",
    "qqplot(data=mdl_price_vs_conv.resid, fit=True, line=\"45\")\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01d5afe8",
   "metadata": {},
   "source": [
    "* Create the scale-location plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f234f426",
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
    "# Preprocessing steps\n",
    "model_norm_residuals = mdl_price_vs_conv.get_influence().resid_studentized_internal\n",
    "model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))\n",
    "\n",
    "# Create the scale-location plot\n",
    "sns.regplot(x=mdl_price_vs_conv.fittedvalues, y=model_norm_residuals_abs_sqrt, ci=None, lowess=True)\n",
    "plt.xlabel(\"Fitted values\")\n",
    "plt.ylabel(\"Sqrt of abs val of stdized residuals\")\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16cef514",
   "metadata": {},
   "source": [
    "Perfect plotting! These three diagnostic plots are excellent for sanity-checking the quality of your models.\n",
    "\n",
    "## Leverage\n",
    "Leverage measures how unusual or extreme the explanatory variables are for each observation. Very roughly, high leverage means that the explanatory variable has values that are different from other points in the dataset. In the case of simple linear regression, where there is only one explanatory value, this typically means values with a very high or very low explanatory value.\n",
    "\n",
    "Here, you'll look at highly leveraged values in the model of house price versus the square root of distance from the nearest MRT station in the Taiwan real estate dataset.\n",
    "\n",
    "Guess which observations you think will have a high leverage, then move the slider to find out.\n",
    "\n",
    "Which statement is true?\n",
    "\n",
    "* Observations with a large distance to the nearest MRT station have the highest leverage, because these points are furthest away from the linear regression trend line.\n",
    "\n",
    "* Observations with a large distance to the nearest MRT station have the highest leverage, because leverage is proportional to the explanatory variable.\n",
    "\n",
    "* **Observations with a large distance to the nearest MRT station have the highest leverage, because most of the observations have a short distance, so long distances are more extreme.**\n",
    "\n",
    "* Observations with a high price have the highest leverage, because most of the observations have a low price, so high prices are most extreme.\n",
    "\n",
    "Lovely leveraging! Highly leveraged points are the ones with explanatory variables that are furthest away from the others.\n",
    "\n",
    "## Influence\n",
    "Influence measures how much a model would change if each observation was left out of the model calculations, one at a time. That is, it measures how different the prediction line would look if you would run a linear regression on all data points except that point, compared to running a linear regression on the whole dataset.\n",
    "\n",
    "The standard metric for influence is Cook's distance, which calculates influence based on the residual size and the leverage of the point.\n",
    "\n",
    "You can see the same model as last time: house price versus the square root of distance from the nearest MRT station in the Taiwan real estate dataset.\n",
    "\n",
    "Guess which observations you think will have a high influence, then move the slider to find out.\n",
    "\n",
    "Which statement is true?\n",
    "\n",
    "* **Observations far away from the trend line have high influence, because they have large residuals and are far away from other observations.**\n",
    "\n",
    "* Observations with high prices have high influence, because influence is proportional to the response variable.\n",
    "\n",
    "* Observations far away from the trend line have high influence, because the slope of the trend is negative.\n",
    "\n",
    "* Observations far away from the trend line have high influence, because that increases the leverage of those points.\n",
    "\n",
    "Impressive influence interpretation! The majority of the influential houses were those with prices that were much higher than the model predicted (and one with a price that was much lower).\n",
    "\n",
    "## Extracting leverage and influence\n",
    "In the last few exercises, you explored which observations had the highest leverage and influence. Now you'll extract those values from the model.\n",
    "\n",
    "* Get the summary frame from `mdl_price_vs_dist` and save as `summary_info`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e1825f62",
   "metadata": {},
   "outputs": [],
   "source": [
    "taiwan_real_estate[\"sqrt_dist_to_mrt_m\"] = np.sqrt(taiwan_real_estate[\"dist_to_mrt_m\"])\n",
    "mdl_price_vs_dist = ols(\"price_twd_msq ~ sqrt_dist_to_mrt_m\", data=taiwan_real_estate).fit()\n",
    "\n",
    "# Create summary_info\n",
    "summary_info = mdl_price_vs_dist.get_influence().summary_frame()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4008715",
   "metadata": {},
   "source": [
    "* Add the `hat_diag` column of `summary_info` to `taiwan_real_estate` as the leverage column.\n",
    "* Sort `taiwan_real_estate` by leverage in descending order and print the head."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "9c5b9c49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     dist_to_mrt_m  n_convenience house_age_years  price_twd_msq  \\\n",
      "347       6488.021              1        15 to 30       3.388805   \n",
      "116       6396.283              1        30 to 45       3.691377   \n",
      "249       6306.153              1        15 to 30       4.538578   \n",
      "255       5512.038              1        30 to 45       5.264750   \n",
      "8         5512.038              1        30 to 45       5.688351   \n",
      "\n",
      "     sqrt_dist_to_mrt_m  leverage  \n",
      "347           80.548253  0.026665  \n",
      "116           79.976765  0.026135  \n",
      "249           79.411290  0.025617  \n",
      "255           74.243101  0.021142  \n",
      "8             74.243101  0.021142  \n"
     ]
    }
   ],
   "source": [
    "# Add the hat_diag column to taiwan_real_estate, name it leverage\n",
    "taiwan_real_estate[\"leverage\"] = summary_info[\"hat_diag\"]\n",
    "\n",
    "# Sort taiwan_real_estate by leverage in descending order and print the head\n",
    "print(taiwan_real_estate.sort_values(\"leverage\", ascending=False).head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1150de57",
   "metadata": {},
   "source": [
    "* Add the cooks_d column from `summary_info` to `taiwan_real_estate` as the `cooks_dist` column.\n",
    "* Sort `taiwan_real_estate` by `cooks_dist` in descending order and print the head."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c86e6127",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     dist_to_mrt_m  n_convenience house_age_years  price_twd_msq  \\\n",
      "270       252.5822              1         0 to 15      35.552194   \n",
      "148      3780.5900              0        15 to 30      13.645991   \n",
      "228      3171.3290              0         0 to 15      14.099849   \n",
      "220       186.5101              9        30 to 45      23.691377   \n",
      "113       393.2606              6         0 to 15       2.299546   \n",
      "\n",
      "     sqrt_dist_to_mrt_m  leverage  cooks_dist  \n",
      "270           15.892835  0.003849    0.115549  \n",
      "148           61.486503  0.012147    0.052440  \n",
      "228           56.314554  0.009332    0.035384  \n",
      "220           13.656870  0.004401    0.025123  \n",
      "113           19.830799  0.003095    0.022813  \n"
     ]
    }
   ],
   "source": [
    "# Add the cooks_d column to taiwan_real_estate, name it cooks_dist\n",
    "taiwan_real_estate[\"cooks_dist\"] = summary_info[\"cooks_d\"]\n",
    "\n",
    "# Sort taiwan_real_estate by cooks_dist in descending order and print the head.\n",
    "print(taiwan_real_estate.sort_values(\"cooks_dist\", ascending=False).head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99f6cf44",
   "metadata": {},
   "source": [
    "Delightful outlier diagnosing! Leverage and influence are important concepts for determining whether your model is overly affected by some unusual data points."
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
