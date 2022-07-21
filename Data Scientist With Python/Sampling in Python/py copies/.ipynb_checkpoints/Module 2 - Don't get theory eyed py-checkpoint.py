{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "62c741d9",
   "metadata": {},
   "source": [
    "# Don't get theory eyed\n",
    "\n",
    "## Simple random sampling\n",
    "The simplest method of sampling a population is the one you've seen already. It is known as simple random sampling (sometimes abbreviated to \"SRS\"), and involves picking rows at random, one at a time, where each row has the same chance of being picked as any other.\n",
    "\n",
    "In this chapter, you'll apply sampling methods to a synthetic (fictional) employee attrition dataset from IBM, where \"attrition\" in this context means leaving the company.\n",
    "\n",
    "* Sample 70 rows from `attrition_pop` using simple random sampling, setting the random seed to 18900217.\n",
    "* Print the sample dataset, `attrition_samp`. What do you notice about the indices?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ff48a41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Age  Attrition     BusinessTravel  DailyRate            Department  \\\n",
      "1134   35        0.0      Travel_Rarely        583  Research_Development   \n",
      "1150   52        0.0         Non-Travel        585                 Sales   \n",
      "531    33        0.0      Travel_Rarely        931  Research_Development   \n",
      "395    31        0.0      Travel_Rarely       1332  Research_Development   \n",
      "392    29        0.0      Travel_Rarely        942  Research_Development   \n",
      "...   ...        ...                ...        ...                   ...   \n",
      "361    27        0.0  Travel_Frequently       1410                 Sales   \n",
      "1180   36        0.0      Travel_Rarely        530                 Sales   \n",
      "230    26        0.0      Travel_Rarely       1443                 Sales   \n",
      "211    29        0.0  Travel_Frequently        410  Research_Development   \n",
      "890    30        0.0  Travel_Frequently       1312  Research_Development   \n",
      "\n",
      "      DistanceFromHome      Education    EducationField  \\\n",
      "1134                25         Master           Medical   \n",
      "1150                29         Master     Life_Sciences   \n",
      "531                 14       Bachelor           Medical   \n",
      "395                 11        College           Medical   \n",
      "392                 15  Below_College     Life_Sciences   \n",
      "...                ...            ...               ...   \n",
      "361                  3  Below_College           Medical   \n",
      "1180                 2         Master     Life_Sciences   \n",
      "230                 23       Bachelor         Marketing   \n",
      "211                  2  Below_College     Life_Sciences   \n",
      "890                  2         Master  Technical_Degree   \n",
      "\n",
      "     EnvironmentSatisfaction  Gender  ...  PerformanceRating  \\\n",
      "1134                    High  Female  ...          Excellent   \n",
      "1150                     Low    Male  ...          Excellent   \n",
      "531                Very_High  Female  ...          Excellent   \n",
      "395                     High    Male  ...          Excellent   \n",
      "392                   Medium  Female  ...          Excellent   \n",
      "...                      ...     ...  ...                ...   \n",
      "361                Very_High  Female  ...        Outstanding   \n",
      "1180                    High  Female  ...          Excellent   \n",
      "230                     High  Female  ...          Excellent   \n",
      "211                Very_High  Female  ...          Excellent   \n",
      "890                Very_High  Female  ...          Excellent   \n",
      "\n",
      "     RelationshipSatisfaction  StockOptionLevel TotalWorkingYears  \\\n",
      "1134                     High                 1                16   \n",
      "1150                   Medium                 2                16   \n",
      "531                 Very_High                 1                 8   \n",
      "395                 Very_High                 0                 6   \n",
      "392                       Low                 1                 6   \n",
      "...                       ...               ...               ...   \n",
      "361                    Medium                 2                 6   \n",
      "1180                     High                 0                17   \n",
      "230                      High                 1                 5   \n",
      "211                      High                 3                 4   \n",
      "890                 Very_High                 0                10   \n",
      "\n",
      "     TrainingTimesLastYear WorkLifeBalance  YearsAtCompany  \\\n",
      "1134                     3            Good              16   \n",
      "1150                     3            Good               9   \n",
      "531                      5          Better               8   \n",
      "395                      2            Good               6   \n",
      "392                      2            Good               5   \n",
      "...                    ...             ...             ...   \n",
      "361                      3          Better               6   \n",
      "1180                     2            Good              13   \n",
      "230                      2            Good               2   \n",
      "211                      3          Better               3   \n",
      "890                      2          Better               9   \n",
      "\n",
      "      YearsInCurrentRole  YearsSinceLastPromotion YearsWithCurrManager  \n",
      "1134                  10                       10                    1  \n",
      "1150                   8                        0                    0  \n",
      "531                    7                        1                    6  \n",
      "395                    5                        0                    1  \n",
      "392                    4                        1                    3  \n",
      "...                  ...                      ...                  ...  \n",
      "361                    5                        0                    4  \n",
      "1180                   7                        6                    7  \n",
      "230                    2                        0                    0  \n",
      "211                    2                        0                    2  \n",
      "890                    7                        0                    7  \n",
      "\n",
      "[70 rows x 31 columns]\n"
     ]
    }
   ],
   "source": [
    "import pyarrow.feather as feather\n",
    "import pandas as pd\n",
    "\n",
    "attrition_pop = feather.read_feather('datasets/attrition.feather')\n",
    "\n",
    "# Sample 70 rows using simple random sampling and set the seed\n",
    "attrition_samp = attrition_pop.sample(n=70, random_state=18900217)\n",
    "\n",
    "# Print the sample\n",
    "print(attrition_samp)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5910771b",
   "metadata": {},
   "source": [
    "Simply the best! Notice how the indexes in the sample aren't always in increasing order. They are just random.\n",
    "\n",
    "## Systematic sampling\n",
    "One sampling method that avoids randomness is called systematic sampling. Here, you pick rows from the population at regular intervals.\n",
    "\n",
    "For example, if the population dataset had one thousand rows, and you wanted a sample size of five, you could pick rows 0, 200, 400, 600, and 800.\n",
    "\n",
    "* Set the sample size to 70.\n",
    "* Calculate the population size from `attrition_pop`.\n",
    "* Calculate the interval between the rows to be sampled."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8c182fd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the sample size to 70\n",
    "sample_size = 70\n",
    "\n",
    "# Calculate the population size from attrition_pop\n",
    "pop_size = len(attrition_pop)\n",
    "\n",
    "# Calculate the interval\n",
    "interval = pop_size // sample_size"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84acb8af",
   "metadata": {},
   "source": [
    "* Systematically sample `attrition_pop` to get the rows of the population at each interval, starting at 0; assign the rows to `attrition_sys_samp`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "88351398",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Age  Attrition BusinessTravel  DailyRate            Department  \\\n",
      "0      21        0.0  Travel_Rarely        391  Research_Development   \n",
      "21     19        0.0  Travel_Rarely       1181  Research_Development   \n",
      "42     45        0.0  Travel_Rarely        252  Research_Development   \n",
      "63     23        0.0  Travel_Rarely        373  Research_Development   \n",
      "84     30        1.0  Travel_Rarely        945                 Sales   \n",
      "...   ...        ...            ...        ...                   ...   \n",
      "1365   48        0.0  Travel_Rarely        715  Research_Development   \n",
      "1386   48        0.0  Travel_Rarely       1355  Research_Development   \n",
      "1407   50        0.0  Travel_Rarely        989  Research_Development   \n",
      "1428   50        0.0     Non-Travel        881  Research_Development   \n",
      "1449   52        0.0  Travel_Rarely        699  Research_Development   \n",
      "\n",
      "      DistanceFromHome      Education EducationField EnvironmentSatisfaction  \\\n",
      "0                   15        College  Life_Sciences                    High   \n",
      "21                   3  Below_College        Medical                  Medium   \n",
      "42                   2       Bachelor  Life_Sciences                  Medium   \n",
      "63                   1        College  Life_Sciences               Very_High   \n",
      "84                   9       Bachelor        Medical                  Medium   \n",
      "...                ...            ...            ...                     ...   \n",
      "1365                 1       Bachelor  Life_Sciences               Very_High   \n",
      "1386                 4         Master  Life_Sciences                    High   \n",
      "1407                 7        College        Medical                  Medium   \n",
      "1428                 2         Master  Life_Sciences                     Low   \n",
      "1449                 1         Master  Life_Sciences                    High   \n",
      "\n",
      "      Gender  ...  PerformanceRating RelationshipSatisfaction  \\\n",
      "0       Male  ...          Excellent                Very_High   \n",
      "21    Female  ...          Excellent                Very_High   \n",
      "42    Female  ...          Excellent                Very_High   \n",
      "63      Male  ...        Outstanding                Very_High   \n",
      "84      Male  ...          Excellent                     High   \n",
      "...      ...  ...                ...                      ...   \n",
      "1365    Male  ...          Excellent                     High   \n",
      "1386    Male  ...          Excellent                   Medium   \n",
      "1407  Female  ...          Excellent                Very_High   \n",
      "1428    Male  ...          Excellent                Very_High   \n",
      "1449    Male  ...          Excellent                      Low   \n",
      "\n",
      "      StockOptionLevel TotalWorkingYears TrainingTimesLastYear  \\\n",
      "0                    0                 0                     6   \n",
      "21                   0                 1                     3   \n",
      "42                   0                 1                     3   \n",
      "63                   1                 1                     2   \n",
      "84                   0                 1                     3   \n",
      "...                ...               ...                   ...   \n",
      "1365                 0                25                     3   \n",
      "1386                 0                27                     3   \n",
      "1407                 1                29                     2   \n",
      "1428                 1                31                     3   \n",
      "1449                 1                34                     5   \n",
      "\n",
      "     WorkLifeBalance  YearsAtCompany  YearsInCurrentRole  \\\n",
      "0             Better               0                   0   \n",
      "21            Better               1                   0   \n",
      "42            Better               1                   0   \n",
      "63            Better               1                   0   \n",
      "84              Good               1                   0   \n",
      "...              ...             ...                 ...   \n",
      "1365            Best               1                   0   \n",
      "1386          Better              15                  11   \n",
      "1407            Good              27                   3   \n",
      "1428          Better              31                   6   \n",
      "1449          Better              33                  18   \n",
      "\n",
      "      YearsSinceLastPromotion YearsWithCurrManager  \n",
      "0                           0                    0  \n",
      "21                          0                    0  \n",
      "42                          0                    0  \n",
      "63                          0                    1  \n",
      "84                          0                    0  \n",
      "...                       ...                  ...  \n",
      "1365                        0                    0  \n",
      "1386                        4                    8  \n",
      "1407                       13                    8  \n",
      "1428                       14                    7  \n",
      "1449                       11                    9  \n",
      "\n",
      "[70 rows x 31 columns]\n"
     ]
    }
   ],
   "source": [
    "# Systematically sample 70 rows\n",
    "attrition_sys_samp = attrition_pop.iloc[::interval]\n",
    "\n",
    "# Print the sample\n",
    "print(attrition_sys_samp)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "837b2232",
   "metadata": {},
   "source": [
    "Systematic success! Systematic sampling avoids randomness by picking rows at regular intervals.\n",
    "\n",
    "## Is systematic sampling OK?\n",
    "Systematic sampling has a problem: if the data has been sorted, or there is some sort of pattern or meaning behind the row order, then the resulting sample may not be representative of the whole population. The problem can be solved by shuffling the rows, but then systematic sampling is equivalent to simple random sampling.\n",
    "\n",
    "Here you'll look at how to determine whether or not there is a problem.\n",
    "\n",
    "* Add an index column to `attrition_pop`, assigning the result to `attrition_pop_id`.\n",
    "* Create a scatter plot of YearsAtCompany versus index for `attrition_pop_id`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "367f135e",
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
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Add an index column to attrition_pop\n",
    "attrition_pop_id = attrition_pop.reset_index()\n",
    "\n",
    "# Plot YearsAtCompany vs. index for attrition_pop_id\n",
    "attrition_pop_id.plot(x=\"index\", y=\"YearsAtCompany\", kind=\"scatter\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "025c0b71",
   "metadata": {},
   "source": [
    "* Randomly shuffle the rows of `attrition_pop`.\n",
    "* Reset the row indexes, and add an index column to `attrition_pop`.\n",
    "* Repeat the scatter plot of YearsAtCompany versus index, this time using `attrition_shuffled`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "393312df",
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
    "# Shuffle the rows of attrition_pop\n",
    "attrition_shuffled = attrition_pop.sample(frac=1)\n",
    "\n",
    "# Reset the row indexes and create an index column\n",
    "attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()\n",
    "\n",
    "# Plot YearsAtCompany vs. index for attrition_shuffled\n",
    "attrition_shuffled.plot(x=\"index\", y=\"YearsAtCompany\", kind=\"scatter\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8701c891",
   "metadata": {},
   "source": [
    "Does a systematic sample always produce a sample similar to a simple random sample?\n",
    "\n",
    "* Yes. All sampling (random or non-random) methods will lead us to similar results.\n",
    "\n",
    "* Yes. We should always expect a representative sample for both systematic and simple random sampling.\n",
    "\n",
    "* No. This only holds if a seed has been set for both processes.\n",
    "\n",
    "* **No. This is not true if the data is sorted in some way.**\n",
    "\n",
    "Your sample skills are ample! Systematic sampling has problems when the data are sorted or contain a pattern. Shuffling the rows makes it equivalent to simple random sampling.\n",
    "\n",
    "## Proportional stratified sampling\n",
    "If you are interested in subgroups within the population, then you may need to carefully control the counts of each subgroup within the population. Proportional stratified sampling results in subgroup sizes within the sample that are representative of the subgroup sizes within the population. It is equivalent to performing a simple random sample on each subgroup.\n",
    "\n",
    "* Get the proportion of employees by Education level from `attrition_pop`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1161356d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bachelor         0.389116\n",
      "Master           0.270748\n",
      "College          0.191837\n",
      "Below_College    0.115646\n",
      "Doctor           0.032653\n",
      "Name: Education, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Proportion of employees by Education level\n",
    "education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)\n",
    "\n",
    "# Print education_counts_pop\n",
    "print(education_counts_pop)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfc1d947",
   "metadata": {},
   "source": [
    "* Use proportional stratified sampling on `attrition_pop` to sample 40% of each Education group, setting the seed to 2022."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "82f360cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Age  Attrition     BusinessTravel  DailyRate            Department  \\\n",
      "1191   53        0.0      Travel_Rarely        238                 Sales   \n",
      "407    29        0.0  Travel_Frequently        995  Research_Development   \n",
      "1233   59        0.0  Travel_Frequently       1225                 Sales   \n",
      "366    37        0.0      Travel_Rarely        571  Research_Development   \n",
      "702    31        0.0  Travel_Frequently        163  Research_Development   \n",
      "...   ...        ...                ...        ...                   ...   \n",
      "733    38        0.0  Travel_Frequently        653  Research_Development   \n",
      "1061   44        0.0  Travel_Frequently        602       Human_Resources   \n",
      "1307   41        0.0      Travel_Rarely       1276                 Sales   \n",
      "1060   33        0.0      Travel_Rarely        516  Research_Development   \n",
      "177    29        0.0      Travel_Rarely        738  Research_Development   \n",
      "\n",
      "      DistanceFromHome      Education    EducationField  \\\n",
      "1191                 1  Below_College           Medical   \n",
      "407                  2  Below_College     Life_Sciences   \n",
      "1233                 1  Below_College     Life_Sciences   \n",
      "366                 10  Below_College     Life_Sciences   \n",
      "702                 24  Below_College  Technical_Degree   \n",
      "...                ...            ...               ...   \n",
      "733                 29         Doctor     Life_Sciences   \n",
      "1061                 1         Doctor   Human_Resources   \n",
      "1307                 2         Doctor     Life_Sciences   \n",
      "1060                 8         Doctor     Life_Sciences   \n",
      "177                  9         Doctor             Other   \n",
      "\n",
      "     EnvironmentSatisfaction  Gender  ...  PerformanceRating  \\\n",
      "1191               Very_High  Female  ...        Outstanding   \n",
      "407                      Low    Male  ...          Excellent   \n",
      "1233                     Low  Female  ...          Excellent   \n",
      "366                Very_High  Female  ...          Excellent   \n",
      "702                Very_High  Female  ...        Outstanding   \n",
      "...                      ...     ...  ...                ...   \n",
      "733                Very_High  Female  ...          Excellent   \n",
      "1061                     Low    Male  ...          Excellent   \n",
      "1307                  Medium  Female  ...          Excellent   \n",
      "1060               Very_High    Male  ...          Excellent   \n",
      "177                   Medium    Male  ...          Excellent   \n",
      "\n",
      "     RelationshipSatisfaction  StockOptionLevel TotalWorkingYears  \\\n",
      "1191                Very_High                 0                18   \n",
      "407                 Very_High                 1                 6   \n",
      "1233                Very_High                 0                20   \n",
      "366                    Medium                 2                 6   \n",
      "702                 Very_High                 0                 9   \n",
      "...                       ...               ...               ...   \n",
      "733                 Very_High                 0                10   \n",
      "1061                     High                 0                14   \n",
      "1307                   Medium                 1                22   \n",
      "1060                      Low                 0                14   \n",
      "177                      High                 0                 4   \n",
      "\n",
      "     TrainingTimesLastYear WorkLifeBalance  YearsAtCompany  \\\n",
      "1191                     2            Best              14   \n",
      "407                      0            Best               6   \n",
      "1233                     2            Good               4   \n",
      "366                      3            Good               5   \n",
      "702                      3            Good               5   \n",
      "...                    ...             ...             ...   \n",
      "733                      2          Better              10   \n",
      "1061                     3          Better              10   \n",
      "1307                     2          Better              18   \n",
      "1060                     6          Better               0   \n",
      "177                      2          Better               3   \n",
      "\n",
      "      YearsInCurrentRole  YearsSinceLastPromotion YearsWithCurrManager  \n",
      "1191                   7                        8                   10  \n",
      "407                    4                        1                    3  \n",
      "1233                   3                        1                    3  \n",
      "366                    3                        4                    3  \n",
      "702                    4                        1                    4  \n",
      "...                  ...                      ...                  ...  \n",
      "733                    3                        9                    9  \n",
      "1061                   7                        0                    2  \n",
      "1307                  16                       11                    8  \n",
      "1060                   0                        0                    0  \n",
      "177                    2                        2                    2  \n",
      "\n",
      "[588 rows x 31 columns]\n"
     ]
    }
   ],
   "source": [
    "# Proportional stratified sampling for 40% of each Education group\n",
    "attrition_strat = attrition_pop.groupby('Education')\\\n",
    "                               .sample(frac=0.4, random_state=2022)\n",
    "\n",
    "# Print the sample\n",
    "print(attrition_strat)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a5f35a5",
   "metadata": {},
   "source": [
    "* Get the proportion of employees by Education level from `attrition_strat`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "53b92674",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bachelor         0.389456\n",
      "Master           0.270408\n",
      "College          0.192177\n",
      "Below_College    0.115646\n",
      "Doctor           0.032313\n",
      "Name: Education, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate the Education level proportions from attrition_strat\n",
    "education_counts_strat = attrition_strat['Education'].value_counts(normalize=True)\n",
    "\n",
    "# Print education_counts_strat\n",
    "print(education_counts_strat)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37243f47",
   "metadata": {},
   "source": [
    "Perfectly proportioned! By grouping then sampling, the size of each group in the sample is representative of the size of the sample in the population.\n",
    "\n",
    "## Equal counts stratified sampling\n",
    "If one subgroup is larger than another subgroup in the population, but you don't want to reflect that difference in your analysis, then you can use equal counts stratified sampling to generate samples where each subgroup has the same amount of data. For example, if you are analyzing blood types, O is the most common blood type worldwide, but you may wish to have equal amounts of O, A, B, and AB in your sample.\n",
    "\n",
    "* Use equal counts stratified sampling on `attrition_pop` to get 30 employees from each Education group, setting the seed to 2022."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d67154ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Age  Attrition     BusinessTravel  DailyRate            Department  \\\n",
      "1191   53        0.0      Travel_Rarely        238                 Sales   \n",
      "407    29        0.0  Travel_Frequently        995  Research_Development   \n",
      "1233   59        0.0  Travel_Frequently       1225                 Sales   \n",
      "366    37        0.0      Travel_Rarely        571  Research_Development   \n",
      "702    31        0.0  Travel_Frequently        163  Research_Development   \n",
      "...   ...        ...                ...        ...                   ...   \n",
      "774    33        0.0      Travel_Rarely        922  Research_Development   \n",
      "869    45        0.0      Travel_Rarely       1015  Research_Development   \n",
      "530    32        0.0      Travel_Rarely        120  Research_Development   \n",
      "1049   48        0.0      Travel_Rarely        163                 Sales   \n",
      "350    29        1.0      Travel_Rarely        408  Research_Development   \n",
      "\n",
      "      DistanceFromHome      Education    EducationField  \\\n",
      "1191                 1  Below_College           Medical   \n",
      "407                  2  Below_College     Life_Sciences   \n",
      "1233                 1  Below_College     Life_Sciences   \n",
      "366                 10  Below_College     Life_Sciences   \n",
      "702                 24  Below_College  Technical_Degree   \n",
      "...                ...            ...               ...   \n",
      "774                  1         Doctor           Medical   \n",
      "869                  5         Doctor           Medical   \n",
      "530                  6         Doctor     Life_Sciences   \n",
      "1049                 2         Doctor         Marketing   \n",
      "350                 25         Doctor  Technical_Degree   \n",
      "\n",
      "     EnvironmentSatisfaction  Gender  ...  PerformanceRating  \\\n",
      "1191               Very_High  Female  ...        Outstanding   \n",
      "407                      Low    Male  ...          Excellent   \n",
      "1233                     Low  Female  ...          Excellent   \n",
      "366                Very_High  Female  ...          Excellent   \n",
      "702                Very_High  Female  ...        Outstanding   \n",
      "...                      ...     ...  ...                ...   \n",
      "774                      Low  Female  ...          Excellent   \n",
      "869                     High  Female  ...          Excellent   \n",
      "530                     High    Male  ...        Outstanding   \n",
      "1049                  Medium  Female  ...          Excellent   \n",
      "350                     High  Female  ...          Excellent   \n",
      "\n",
      "     RelationshipSatisfaction  StockOptionLevel TotalWorkingYears  \\\n",
      "1191                Very_High                 0                18   \n",
      "407                 Very_High                 1                 6   \n",
      "1233                Very_High                 0                20   \n",
      "366                    Medium                 2                 6   \n",
      "702                 Very_High                 0                 9   \n",
      "...                       ...               ...               ...   \n",
      "774                      High                 1                10   \n",
      "869                       Low                 0                10   \n",
      "530                       Low                 0                 8   \n",
      "1049                      Low                 1                14   \n",
      "350                    Medium                 0                 6   \n",
      "\n",
      "     TrainingTimesLastYear WorkLifeBalance  YearsAtCompany  \\\n",
      "1191                     2            Best              14   \n",
      "407                      0            Best               6   \n",
      "1233                     2            Good               4   \n",
      "366                      3            Good               5   \n",
      "702                      3            Good               5   \n",
      "...                    ...             ...             ...   \n",
      "774                      2          Better               6   \n",
      "869                      3          Better              10   \n",
      "530                      2          Better               5   \n",
      "1049                     2          Better               9   \n",
      "350                      2            Best               2   \n",
      "\n",
      "      YearsInCurrentRole  YearsSinceLastPromotion YearsWithCurrManager  \n",
      "1191                   7                        8                   10  \n",
      "407                    4                        1                    3  \n",
      "1233                   3                        1                    3  \n",
      "366                    3                        4                    3  \n",
      "702                    4                        1                    4  \n",
      "...                  ...                      ...                  ...  \n",
      "774                    1                        0                    5  \n",
      "869                    7                        1                    4  \n",
      "530                    4                        1                    4  \n",
      "1049                   7                        6                    7  \n",
      "350                    2                        1                    1  \n",
      "\n",
      "[150 rows x 31 columns]\n"
     ]
    }
   ],
   "source": [
    "# Get 30 employees from each Education group\n",
    "attrition_eq = attrition_pop.groupby('Education')\\\n",
    "                            .sample(n=30, random_state=2022)      \n",
    "         \n",
    "# Print the sample\n",
    "print(attrition_eq)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "359d5e9a",
   "metadata": {},
   "source": [
    "* Get the proportion of employees by Education level from `attrition_eq`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "565ecd25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Below_College    0.2\n",
      "College          0.2\n",
      "Bachelor         0.2\n",
      "Master           0.2\n",
      "Doctor           0.2\n",
      "Name: Education, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Get the proportions from attrition_eq\n",
    "education_counts_eq = attrition_eq['Education'].value_counts(normalize=True) \n",
    "\n",
    "# Print the results\n",
    "print(education_counts_eq)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "affc0187",
   "metadata": {},
   "source": [
    "Elegant equal count creation! If you want each subgroup to have equal weight in your analysis, then equal counts stratified sampling is the appropriate technique.\n",
    "\n",
    "## Weighted sampling\n",
    "Stratified sampling provides rules about the probability of picking rows from your dataset at the subgroup level. A generalization of this is weighted sampling, which lets you specify rules about the probability of picking rows at the row level. The probability of picking any given row is proportional to the weight value for that row.\n",
    "\n",
    "* Plot YearsAtCompany from `attrition_pop` as a histogram with bins of width 1 from 0 to 40."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "48a7eaa4",
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
    "import numpy as np\n",
    "\n",
    "# Plot YearsAtCompany from attrition_pop as a histogram\n",
    "attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08b556d2",
   "metadata": {},
   "source": [
    "* Sample 400 employees from `attrition_pop` weighted by YearsAtCompany."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "456fa4b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Age  Attrition     BusinessTravel  DailyRate            Department  \\\n",
      "1405   47        0.0      Travel_Rarely       1001  Research_Development   \n",
      "1416   58        0.0      Travel_Rarely        605                 Sales   \n",
      "785    32        0.0      Travel_Rarely        929                 Sales   \n",
      "626    27        0.0  Travel_Frequently        994                 Sales   \n",
      "1308   41        0.0      Travel_Rarely        314       Human_Resources   \n",
      "...   ...        ...                ...        ...                   ...   \n",
      "803    30        0.0  Travel_Frequently       1012  Research_Development   \n",
      "1377   52        0.0      Travel_Rarely       1053  Research_Development   \n",
      "995    42        0.0  Travel_Frequently        748  Research_Development   \n",
      "806    32        0.0  Travel_Frequently        379                 Sales   \n",
      "665    33        0.0      Travel_Rarely        586                 Sales   \n",
      "\n",
      "      DistanceFromHome Education   EducationField EnvironmentSatisfaction  \\\n",
      "1405                 4  Bachelor    Life_Sciences                    High   \n",
      "1416                21  Bachelor    Life_Sciences               Very_High   \n",
      "785                 10  Bachelor        Marketing               Very_High   \n",
      "626                  8  Bachelor    Life_Sciences               Very_High   \n",
      "1308                 1  Bachelor  Human_Resources               Very_High   \n",
      "...                ...       ...              ...                     ...   \n",
      "803                  5    Master    Life_Sciences                  Medium   \n",
      "1377                 1   College    Life_Sciences               Very_High   \n",
      "995                  9   College          Medical                     Low   \n",
      "806                  5   College    Life_Sciences                  Medium   \n",
      "665                  1  Bachelor          Medical                     Low   \n",
      "\n",
      "      Gender  ...  PerformanceRating RelationshipSatisfaction  \\\n",
      "1405  Female  ...          Excellent                     High   \n",
      "1416  Female  ...          Excellent                     High   \n",
      "785     Male  ...          Excellent                Very_High   \n",
      "626     Male  ...          Excellent                Very_High   \n",
      "1308    Male  ...          Excellent                   Medium   \n",
      "...      ...  ...                ...                      ...   \n",
      "803     Male  ...          Excellent                   Medium   \n",
      "1377    Male  ...          Excellent                   Medium   \n",
      "995   Female  ...          Excellent                     High   \n",
      "806     Male  ...          Excellent                Very_High   \n",
      "665     Male  ...        Outstanding                      Low   \n",
      "\n",
      "      StockOptionLevel TotalWorkingYears TrainingTimesLastYear  \\\n",
      "1405                 1                28                     4   \n",
      "1416                 1                29                     2   \n",
      "785                  0                10                     2   \n",
      "626                  0                 9                     0   \n",
      "1308                 1                22                     3   \n",
      "...                ...               ...                   ...   \n",
      "803                  1                10                     3   \n",
      "1377                 1                26                     2   \n",
      "995                  0                12                     3   \n",
      "806                  1                10                     3   \n",
      "665                  1                 9                     5   \n",
      "\n",
      "     WorkLifeBalance  YearsAtCompany  YearsInCurrentRole  \\\n",
      "1405          Better              22                  11   \n",
      "1416            Good               1                   0   \n",
      "785             Good              10                   7   \n",
      "626           Better               9                   8   \n",
      "1308          Better              22                   7   \n",
      "...              ...             ...                 ...   \n",
      "803             Good               5                   4   \n",
      "1377            Good               9                   8   \n",
      "995           Better              12                   9   \n",
      "806           Better              10                   8   \n",
      "665           Better               9                   8   \n",
      "\n",
      "      YearsSinceLastPromotion YearsWithCurrManager  \n",
      "1405                       14                   10  \n",
      "1416                        0                    0  \n",
      "785                         0                    8  \n",
      "626                         1                    7  \n",
      "1308                        2                   10  \n",
      "...                       ...                  ...  \n",
      "803                         0                    3  \n",
      "1377                        7                    8  \n",
      "995                         5                    8  \n",
      "806                         5                    3  \n",
      "665                         0                    8  \n",
      "\n",
      "[400 rows x 31 columns]\n"
     ]
    }
   ],
   "source": [
    "# Sample 400 employees weighted by YearsAtCompany\n",
    "attrition_weight = attrition_pop.sample(n=400, weights=\"YearsAtCompany\")\n",
    "\n",
    "# Print the sample\n",
    "print(attrition_weight)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb785af3",
   "metadata": {},
   "source": [
    "* Plot YearsAtCompany from `attrition_weight` as a histogram with bins of width 1 from 0 to 40."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0e80e80c",
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
    "# Plot YearsAtCompany from attrition_weight as a histogram\n",
    "attrition_weight['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b421ef1b",
   "metadata": {},
   "source": [
    "Which is higher? The mean YearsAtCompany from attrition_pop or the mean YearsAtCompany from attrition_weight?\n",
    "\n",
    "* Population mean.\n",
    "\n",
    "* Both means are identical.\n",
    "\n",
    "* **Sample mean.**\n",
    "\n",
    "* It is impossible to calculate the two means.\n",
    "\n",
    "Marvelous means! The weighted sample mean is around 11, which is higher than the population mean of around 7. The fact that the two numbers are different means that the weighted simple random sample is biased.\n",
    "\n",
    "## Benefits of clustering\n",
    "Cluster sampling is a two-stage sampling technique that is closely related to stratified sampling. First, you randomly sample which subgroups to include in the sample, then randomly sample rows within each subgroup.\n",
    "\n",
    "In which of the following situations would cluster sampling be preferable to stratified sampling?\n",
    "\n",
    "* The interest is on ensuring each rare group will be represented in the sample selected.\n",
    "\n",
    "* Cost is not a limitation, and time can be spent carefully sampling from each group in the population.\n",
    "\n",
    "* **Collecting an overall sample requires lots of travel from one group to another to collect samples within each group.**\n",
    "\n",
    "* The focus is on comparing particular subgroups within the population.\n",
    "\n",
    "Delightful decision-making! The main benefit of cluster sampling over stratified sampling is that you can save time and money by not including every subgroup in your sample.\n",
    "\n",
    "## Cluster sampling\n",
    "Now that you know when to use cluster sampling, it's time to put it into action. In this exercise, you'll explore the JobRole column of the attrition dataset. You can think of each job role as a subgroup of the whole population of employees.\n",
    "\n",
    "* Create a list of unique JobRole values from `attrition_pop`, and assign to `job_roles_pop`.\n",
    "* Randomly sample four JobRole values from job_roles_pop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4e6bdc0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Research_Scientist', 'Manufacturing_Director', 'Research_Director', 'Human_Resources']\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "# Create a list of unique JobRole values\n",
    "job_roles_pop = list(attrition_pop['JobRole'].unique())\n",
    "\n",
    "# Randomly sample four JobRole values\n",
    "job_roles_samp = random.sample(job_roles_pop, k=4)\n",
    "\n",
    "# Print the result\n",
    "print(job_roles_samp)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2dc50b42",
   "metadata": {},
   "source": [
    "* Subset `attrition_pop` for the sampled job roles by filtering for rows where JobRole is in `job_roles_samp`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "18b4027d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Age  Attrition BusinessTravel  DailyRate            Department  \\\n",
      "0      21        0.0  Travel_Rarely        391  Research_Development   \n",
      "5      27        0.0     Non-Travel        443  Research_Development   \n",
      "6      18        0.0     Non-Travel        287  Research_Development   \n",
      "10     18        0.0     Non-Travel       1431  Research_Development   \n",
      "17     31        0.0  Travel_Rarely       1082  Research_Development   \n",
      "...   ...        ...            ...        ...                   ...   \n",
      "1455   53        0.0  Travel_Rarely        447  Research_Development   \n",
      "1457   55        0.0  Travel_Rarely        692  Research_Development   \n",
      "1459   54        0.0  Travel_Rarely        685  Research_Development   \n",
      "1463   56        0.0  Travel_Rarely       1400  Research_Development   \n",
      "1469   58        1.0  Travel_Rarely        286  Research_Development   \n",
      "\n",
      "      DistanceFromHome Education EducationField EnvironmentSatisfaction  \\\n",
      "0                   15   College  Life_Sciences                    High   \n",
      "5                    3  Bachelor        Medical               Very_High   \n",
      "6                    5   College  Life_Sciences                  Medium   \n",
      "10                  14  Bachelor        Medical                  Medium   \n",
      "17                   1    Master        Medical                    High   \n",
      "...                ...       ...            ...                     ...   \n",
      "1455                 2  Bachelor        Medical               Very_High   \n",
      "1457                14    Master        Medical                    High   \n",
      "1459                 3  Bachelor  Life_Sciences               Very_High   \n",
      "1463                 7  Bachelor  Life_Sciences               Very_High   \n",
      "1469                 2    Master  Life_Sciences               Very_High   \n",
      "\n",
      "      Gender  ...  PerformanceRating RelationshipSatisfaction  \\\n",
      "0       Male  ...          Excellent                Very_High   \n",
      "5       Male  ...          Excellent                     High   \n",
      "6       Male  ...          Excellent                Very_High   \n",
      "10    Female  ...          Excellent                     High   \n",
      "17      Male  ...          Excellent                   Medium   \n",
      "...      ...  ...                ...                      ...   \n",
      "1455    Male  ...          Excellent                   Medium   \n",
      "1457    Male  ...          Excellent                Very_High   \n",
      "1459    Male  ...          Excellent                      Low   \n",
      "1463    Male  ...          Excellent                      Low   \n",
      "1469    Male  ...          Excellent                Very_High   \n",
      "\n",
      "      StockOptionLevel TotalWorkingYears TrainingTimesLastYear  \\\n",
      "0                    0                 0                     6   \n",
      "5                    3                 0                     6   \n",
      "6                    0                 0                     2   \n",
      "10                   0                 0                     4   \n",
      "17                   0                 1                     4   \n",
      "...                ...               ...                   ...   \n",
      "1455                 0                35                     2   \n",
      "1457                 0                36                     3   \n",
      "1459                 0                36                     2   \n",
      "1463                 0                37                     3   \n",
      "1469                 0                40                     2   \n",
      "\n",
      "     WorkLifeBalance  YearsAtCompany  YearsInCurrentRole  \\\n",
      "0             Better               0                   0   \n",
      "5               Good               0                   0   \n",
      "6             Better               0                   0   \n",
      "10               Bad               0                   0   \n",
      "17            Better               1                   1   \n",
      "...              ...             ...                 ...   \n",
      "1455            Good               9                   8   \n",
      "1457          Better              24                  15   \n",
      "1459          Better              10                   9   \n",
      "1463            Good               6                   4   \n",
      "1469          Better              31                  15   \n",
      "\n",
      "      YearsSinceLastPromotion YearsWithCurrManager  \n",
      "0                           0                    0  \n",
      "5                           0                    0  \n",
      "6                           0                    0  \n",
      "10                          0                    0  \n",
      "17                          1                    0  \n",
      "...                       ...                  ...  \n",
      "1455                        8                    8  \n",
      "1457                        2                   15  \n",
      "1459                        0                    9  \n",
      "1463                        0                    2  \n",
      "1469                       13                    8  \n",
      "\n",
      "[569 rows x 31 columns]\n"
     ]
    }
   ],
   "source": [
    "# Filter for rows where JobRole is in job_roles_samp\n",
    "jobrole_condition = attrition_pop['JobRole'].isin(job_roles_samp)\n",
    "attrition_filtered = attrition_pop[jobrole_condition]\n",
    "\n",
    "# Print the result\n",
    "print(attrition_filtered)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6fbe969",
   "metadata": {},
   "source": [
    "* Remove any unused categories from JobRole.\n",
    "* For each job role in the filtered dataset, take a random sample of ten rows, setting the seed to 2022."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "94177a35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Age  Attrition     BusinessTravel  DailyRate            Department  \\\n",
      "1348   44        1.0      Travel_Rarely       1376       Human_Resources   \n",
      "886    41        0.0         Non-Travel        552       Human_Resources   \n",
      "983    39        0.0      Travel_Rarely        141       Human_Resources   \n",
      "88     27        1.0  Travel_Frequently       1337       Human_Resources   \n",
      "189    34        0.0      Travel_Rarely        829       Human_Resources   \n",
      "160    24        0.0  Travel_Frequently        897       Human_Resources   \n",
      "839    46        0.0      Travel_Rarely        991       Human_Resources   \n",
      "966    30        0.0      Travel_Rarely       1240       Human_Resources   \n",
      "162    28        0.0         Non-Travel        280       Human_Resources   \n",
      "1231   37        0.0      Travel_Rarely       1239       Human_Resources   \n",
      "743    34        0.0  Travel_Frequently       1069  Research_Development   \n",
      "1448   56        0.0      Travel_Rarely       1369  Research_Development   \n",
      "333    27        0.0  Travel_Frequently        472  Research_Development   \n",
      "297    33        0.0      Travel_Rarely        575  Research_Development   \n",
      "1306   40        0.0      Travel_Rarely        302  Research_Development   \n",
      "1431   58        1.0      Travel_Rarely        601  Research_Development   \n",
      "1119   49        0.0      Travel_Rarely        470  Research_Development   \n",
      "1366   59        0.0      Travel_Rarely       1429  Research_Development   \n",
      "1051   32        0.0      Travel_Rarely        859  Research_Development   \n",
      "875    45        0.0      Travel_Rarely       1329  Research_Development   \n",
      "1062   43        0.0      Travel_Rarely       1291  Research_Development   \n",
      "1444   53        0.0      Travel_Rarely        102  Research_Development   \n",
      "1290   45        0.0      Travel_Rarely       1005  Research_Development   \n",
      "1302   40        0.0      Travel_Rarely       1416  Research_Development   \n",
      "1303   49        0.0  Travel_Frequently        636  Research_Development   \n",
      "787    32        0.0      Travel_Rarely       1018  Research_Development   \n",
      "1407   50        0.0      Travel_Rarely        989  Research_Development   \n",
      "1420   50        0.0      Travel_Rarely        691  Research_Development   \n",
      "1250   40        0.0  Travel_Frequently        593  Research_Development   \n",
      "1121   51        0.0      Travel_Rarely       1469  Research_Development   \n",
      "1054   33        1.0  Travel_Frequently        827  Research_Development   \n",
      "1227   38        0.0  Travel_Frequently       1189  Research_Development   \n",
      "916    35        0.0      Travel_Rarely       1395  Research_Development   \n",
      "1110   36        0.0      Travel_Rarely        430  Research_Development   \n",
      "803    30        0.0  Travel_Frequently       1012  Research_Development   \n",
      "225    29        1.0      Travel_Rarely       1092  Research_Development   \n",
      "1234   40        0.0  Travel_Frequently       1395  Research_Development   \n",
      "1257   38        0.0  Travel_Frequently       1394  Research_Development   \n",
      "341    31        0.0      Travel_Rarely        691  Research_Development   \n",
      "550    45        0.0      Travel_Rarely        192  Research_Development   \n",
      "\n",
      "      DistanceFromHome      Education    EducationField  \\\n",
      "1348                 1        College           Medical   \n",
      "886                  4       Bachelor   Human_Resources   \n",
      "983                  3       Bachelor   Human_Resources   \n",
      "88                  22       Bachelor   Human_Resources   \n",
      "189                  3        College   Human_Resources   \n",
      "160                 10       Bachelor           Medical   \n",
      "839                  1        College     Life_Sciences   \n",
      "966                  9       Bachelor   Human_Resources   \n",
      "162                  1        College     Life_Sciences   \n",
      "1231                 8        College             Other   \n",
      "743                  2  Below_College     Life_Sciences   \n",
      "1448                23       Bachelor     Life_Sciences   \n",
      "333                  1  Below_College  Technical_Degree   \n",
      "297                 25       Bachelor     Life_Sciences   \n",
      "1306                 6       Bachelor     Life_Sciences   \n",
      "1431                 7         Master           Medical   \n",
      "1119                20         Master           Medical   \n",
      "1366                18         Master           Medical   \n",
      "1051                 4       Bachelor     Life_Sciences   \n",
      "875                  2        College             Other   \n",
      "1062                15        College     Life_Sciences   \n",
      "1444                23         Master     Life_Sciences   \n",
      "1290                28        College  Technical_Degree   \n",
      "1302                 2        College           Medical   \n",
      "1303                10         Master     Life_Sciences   \n",
      "787                  3        College     Life_Sciences   \n",
      "1407                 7        College           Medical   \n",
      "1420                 2       Bachelor           Medical   \n",
      "1250                 9         Master           Medical   \n",
      "1121                 8         Master     Life_Sciences   \n",
      "1054                29         Master           Medical   \n",
      "1227                 1       Bachelor     Life_Sciences   \n",
      "916                  9         Master           Medical   \n",
      "1110                 2         Master             Other   \n",
      "803                  5         Master     Life_Sciences   \n",
      "225                  1         Master           Medical   \n",
      "1234                26       Bachelor           Medical   \n",
      "1257                 8       Bachelor           Medical   \n",
      "341                  5         Master  Technical_Degree   \n",
      "550                 10        College     Life_Sciences   \n",
      "\n",
      "     EnvironmentSatisfaction  Gender  ...  PerformanceRating  \\\n",
      "1348                  Medium    Male  ...          Excellent   \n",
      "886                     High    Male  ...          Excellent   \n",
      "983                     High  Female  ...          Excellent   \n",
      "88                       Low  Female  ...          Excellent   \n",
      "189                     High    Male  ...          Excellent   \n",
      "160                      Low    Male  ...          Excellent   \n",
      "839                Very_High  Female  ...          Excellent   \n",
      "966                     High    Male  ...          Excellent   \n",
      "162                     High    Male  ...          Excellent   \n",
      "1231                    High    Male  ...          Excellent   \n",
      "743                Very_High    Male  ...          Excellent   \n",
      "1448               Very_High    Male  ...          Excellent   \n",
      "333                     High    Male  ...          Excellent   \n",
      "297                Very_High    Male  ...          Excellent   \n",
      "1306                  Medium  Female  ...          Excellent   \n",
      "1431                    High  Female  ...          Excellent   \n",
      "1119                    High  Female  ...          Excellent   \n",
      "1366               Very_High    Male  ...          Excellent   \n",
      "1051                    High  Female  ...          Excellent   \n",
      "875                Very_High  Female  ...          Excellent   \n",
      "1062                    High    Male  ...        Outstanding   \n",
      "1444               Very_High  Female  ...          Excellent   \n",
      "1290               Very_High  Female  ...          Excellent   \n",
      "1302                     Low    Male  ...          Excellent   \n",
      "1303                    High  Female  ...          Excellent   \n",
      "787                     High  Female  ...          Excellent   \n",
      "1407                  Medium  Female  ...          Excellent   \n",
      "1420                    High    Male  ...          Excellent   \n",
      "1250                  Medium  Female  ...          Excellent   \n",
      "1121                  Medium    Male  ...          Excellent   \n",
      "1054                     Low  Female  ...        Outstanding   \n",
      "1227               Very_High    Male  ...          Excellent   \n",
      "916                   Medium    Male  ...          Excellent   \n",
      "1110               Very_High  Female  ...        Outstanding   \n",
      "803                   Medium    Male  ...          Excellent   \n",
      "225                      Low    Male  ...          Excellent   \n",
      "1234                  Medium  Female  ...          Excellent   \n",
      "1257               Very_High  Female  ...          Excellent   \n",
      "341                     High    Male  ...          Excellent   \n",
      "550                      Low    Male  ...        Outstanding   \n",
      "\n",
      "     RelationshipSatisfaction  StockOptionLevel TotalWorkingYears  \\\n",
      "1348                Very_High                 1                24   \n",
      "886                    Medium                 1                10   \n",
      "983                      High                 1                12   \n",
      "88                        Low                 0                 1   \n",
      "189                      High                 1                 4   \n",
      "160                 Very_High                 1                 3   \n",
      "839                      High                 0                10   \n",
      "966                 Very_High                 0                12   \n",
      "162                    Medium                 1                 3   \n",
      "1231                     High                 0                19   \n",
      "743                      High                 0                10   \n",
      "1448                      Low                 1                33   \n",
      "333                      High                 1                 6   \n",
      "297                 Very_High                 0                 5   \n",
      "1306                     High                 0                22   \n",
      "1431                Very_High                 0                31   \n",
      "1119                     High                 0                16   \n",
      "1366                Very_High                 0                25   \n",
      "1051                     High                 1                14   \n",
      "875                       Low                 2                10   \n",
      "1062                      Low                 1                14   \n",
      "1444                     High                 0                33   \n",
      "1290                     High                 0                21   \n",
      "1302                Very_High                 1                22   \n",
      "1303                Very_High                 0                22   \n",
      "787                 Very_High                 0                10   \n",
      "1407                Very_High                 1                29   \n",
      "1420                Very_High                 0                30   \n",
      "1250                     High                 0                20   \n",
      "1121                Very_High                 2                16   \n",
      "1054                   Medium                 0                14   \n",
      "1227                Very_High                 2                19   \n",
      "916                    Medium                 0                10   \n",
      "1110                Very_High                 1                15   \n",
      "803                    Medium                 1                10   \n",
      "225                    Medium                 3                 4   \n",
      "1234                      Low                 1                20   \n",
      "1257                     High                 1                20   \n",
      "341                      High                 1                 6   \n",
      "550                 Very_High                 2                 8   \n",
      "\n",
      "     TrainingTimesLastYear WorkLifeBalance  YearsAtCompany  \\\n",
      "1348                     1          Better              20   \n",
      "886                      4          Better               3   \n",
      "983                      3             Bad               8   \n",
      "88                       2          Better               1   \n",
      "189                      1             Bad               3   \n",
      "160                      2          Better               2   \n",
      "839                      3            Best               7   \n",
      "966                      2             Bad              11   \n",
      "162                      2          Better               3   \n",
      "1231                     4            Good              10   \n",
      "743                      2            Good              10   \n",
      "1448                     0          Better              19   \n",
      "333                      1          Better               2   \n",
      "297                      2          Better               5   \n",
      "1306                     3          Better              20   \n",
      "1431                     0            Good              10   \n",
      "1119                     2            Good              15   \n",
      "1366                     6            Good               9   \n",
      "1051                     3          Better              14   \n",
      "875                      3          Better              10   \n",
      "1062                     3          Better              14   \n",
      "1444                     0          Better              12   \n",
      "1290                     2          Better              21   \n",
      "1302                     5          Better              21   \n",
      "1303                     4          Better               3   \n",
      "787                      6          Better               7   \n",
      "1407                     2            Good              27   \n",
      "1420                     3          Better               4   \n",
      "1250                     3            Good              18   \n",
      "1121                     5             Bad              10   \n",
      "1054                     4          Better              13   \n",
      "1227                     4            Best              13   \n",
      "916                      5          Better              10   \n",
      "1110                     2          Better               1   \n",
      "803                      3            Good               5   \n",
      "225                      3            Best               2   \n",
      "1234                     2          Better              20   \n",
      "1257                     3          Better              20   \n",
      "341                      4          Better               5   \n",
      "550                      3            Good               2   \n",
      "\n",
      "      YearsInCurrentRole  YearsSinceLastPromotion YearsWithCurrManager  \n",
      "1348                   6                        3                    6  \n",
      "886                    2                        1                    2  \n",
      "983                    3                        3                    6  \n",
      "88                     0                        0                    0  \n",
      "189                    2                        0                    2  \n",
      "160                    2                        2                    1  \n",
      "839                    6                        5                    7  \n",
      "966                    9                        4                    7  \n",
      "162                    2                        2                    2  \n",
      "1231                   0                        4                    7  \n",
      "743                    9                        1                    9  \n",
      "1448                  16                       15                    9  \n",
      "333                    2                        2                    0  \n",
      "297                    3                        0                    2  \n",
      "1306                   6                        5                   13  \n",
      "1431                   9                        5                    9  \n",
      "1119                  11                        5                   11  \n",
      "1366                   7                        5                    4  \n",
      "1051                  13                        6                    8  \n",
      "875                    7                        3                    9  \n",
      "1062                  10                        6                   11  \n",
      "1444                   9                        3                    8  \n",
      "1290                   6                        8                    6  \n",
      "1302                   7                        3                    9  \n",
      "1303                   2                        1                    2  \n",
      "787                    7                        7                    7  \n",
      "1407                   3                       13                    8  \n",
      "1420                   3                        0                    3  \n",
      "1250                   7                        2                   13  \n",
      "1121                   9                        4                    7  \n",
      "1054                   7                        3                    8  \n",
      "1227                  11                        2                    9  \n",
      "916                    7                        0                    8  \n",
      "1110                   0                        0                    0  \n",
      "803                    4                        0                    3  \n",
      "225                    2                        2                    2  \n",
      "1234                   7                        2                   13  \n",
      "1257                  11                        0                    7  \n",
      "341                    2                        0                    3  \n",
      "550                    2                        0                    2  \n",
      "\n",
      "[40 rows x 31 columns]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Александр\\AppData\\Local\\Temp\\ipykernel_5768\\3076348811.py:2: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  attrition_filtered['JobRole'] = attrition_filtered['JobRole'].cat.remove_unused_categories()\n"
     ]
    }
   ],
   "source": [
    "# Remove categories with no rows\n",
    "attrition_filtered['JobRole'] = attrition_filtered['JobRole'].cat.remove_unused_categories()\n",
    "\n",
    "# Randomly sample 10 employees from each sampled job role\n",
    "attrition_clust = attrition_filtered.groupby(\"JobRole\")\\\n",
    "    .sample(n=10, random_state=2022)\n",
    "\n",
    "# Print the sample\n",
    "print(attrition_clust)       "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a3e7b35",
   "metadata": {},
   "source": [
    "Classy cluster sampling! The two-stage sampling technique gives you control over sampling both between subgroups and within subgroups.\n",
    "\n",
    "## 3 kinds of sampling\n",
    "You're going to compare the performance of point estimates using simple, stratified, and cluster sampling. Before doing that, you'll have to set up the samples.\n",
    "\n",
    "You'll use the RelationshipSatisfaction column of the attrition_pop dataset, which categorizes the employee's relationship with the company. It has four levels: `Low`, `Medium`, `High`, and `Very_High`. pandas has been loaded with its usual alias, and the random package has been loaded.\n",
    "\n",
    "* Perform simple random sampling on `attrition_pop` to get one-quarter of the population, setting the seed to 2022."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c4aad813",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform simple random sampling to get 0.25 of the population\n",
    "attrition_srs = attrition_pop.sample(frac=0.25, random_state=2022)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f552a958",
   "metadata": {},
   "source": [
    "* Perform stratified sampling on `attrition_pop` to sample one-quarter of each RelationshipSatisfaction group, setting the seed to 2022."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "bf0ed0be",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform stratified sampling to get 0.25 of each relationship group\n",
    "attrition_strat = attrition_pop.groupby(\"RelationshipSatisfaction\")\\\n",
    "                               .sample(frac=0.25, random_state=2022)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a6d6cd9",
   "metadata": {},
   "source": [
    "* Create a list of unique values from `attrition_pop's` RelationshipSatisfaction column.\n",
    "* Randomly sample `satisfaction_unique` to get two values.\n",
    "* Subset the population for rows where RelationshipSatisfaction is in `satisfaction_samp` and clear any unused categories from RelationshipSatisfaction; assign to `attrition_clust_prep`.\n",
    "* Perform cluster sampling on the selected satisfaction groups, sampling one quarter of the population and setting the seed to 2022."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a9e2645b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a list of unique RelationshipSatisfaction values\n",
    "satisfaction_unique = list(attrition_pop['RelationshipSatisfaction'].unique())\n",
    "\n",
    "# Randomly sample 2 unique satisfaction values\n",
    "satisfaction_samp = random.sample(satisfaction_unique, k=2)\n",
    "\n",
    "# Filter for satisfaction_samp and clear unused categories from RelationshipSatisfaction\n",
    "satis_condition = attrition_pop['RelationshipSatisfaction'].isin(satisfaction_samp)\n",
    "attrition_clust_prep = attrition_pop[satis_condition]\n",
    "attrition_clust_prep['RelationshipSatisfaction'] = attrition_clust_prep['RelationshipSatisfaction'].cat.remove_unused_categories()\n",
    "\n",
    "# Perform cluster sampling on the selected group, getting 0.25 of attrition_pop\n",
    "attrition_clust = attrition_clust_prep.groupby(\"RelationshipSatisfaction\")\\\n",
    "                                      .sample(n=len(attrition_pop) // 4, random_state=2022)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "850d4011",
   "metadata": {},
   "source": [
    "Terrific triple! Now we have the three samples set up, let's calculate some summary statistics.\n",
    "\n",
    "## Comparing point estimates\n",
    "Now that you have three types of sample (simple, stratified, and cluster), you can compare point estimates from each sample to the population parameter. That is, you can calculate the same summary statistic on each sample and see how it compares to the summary statistic for the population.\n",
    "\n",
    "Here, we'll look at how satisfaction with the company affects whether or not the employee leaves the company. That is, you'll calculate the proportion of employees who left the company (they have an Attrition value of 1) for each value of RelationshipSatisfaction.\n",
    "\n",
    "* Group `attrition_pop` by RelationshipSatisfaction levels and calculate the mean of Attrition for each level."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a1175203",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RelationshipSatisfaction\n",
      "Low          0.206522\n",
      "Medium       0.148515\n",
      "High         0.154684\n",
      "Very_High    0.148148\n",
      "Name: Attrition, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Mean Attrition by RelationshipSatisfaction group\n",
    "mean_attrition_pop = attrition_pop.groupby('RelationshipSatisfaction')['Attrition'].mean()\n",
    "\n",
    "# Print the result\n",
    "print(mean_attrition_pop)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3fccf5e3",
   "metadata": {},
   "source": [
    "* Calculate the proportion of employee attrition for each relationship satisfaction group, this time on the simple random sample, `attrition_srs`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7e63799a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RelationshipSatisfaction\n",
      "Low          0.134328\n",
      "Medium       0.164179\n",
      "High         0.160000\n",
      "Very_High    0.155963\n",
      "Name: Attrition, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate the same thing for the simple random sample \n",
    "mean_attrition_srs = attrition_srs.groupby('RelationshipSatisfaction')['Attrition'].mean()\n",
    "\n",
    "# Print the result\n",
    "print(mean_attrition_srs)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2d5a8d2",
   "metadata": {},
   "source": [
    "* Calculate the proportion of employee attrition for each relationship satisfaction group, this time on the stratified sample, `attrition_strat`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "b91e4bbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RelationshipSatisfaction\n",
      "Low          0.144928\n",
      "Medium       0.078947\n",
      "High         0.165217\n",
      "Very_High    0.129630\n",
      "Name: Attrition, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate the same thing for the stratified sample \n",
    "mean_attrition_strat = attrition_strat.groupby('RelationshipSatisfaction')['Attrition'].mean()\n",
    "\n",
    "# Print the result\n",
    "print(mean_attrition_strat)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "93c4e1cb",
   "metadata": {},
   "source": [
    "* Calculate the proportion of employee attrition for each relationship satisfaction group, this time on the cluster sample, `attrition_clust`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "27176acb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RelationshipSatisfaction\n",
      "Low          0.200000\n",
      "Medium       0.333333\n",
      "High         0.000000\n",
      "Very_High    0.133333\n",
      "Name: Attrition, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate the same thing for the cluster sample \n",
    "mean_attrition_clust = attrition_clust.groupby('RelationshipSatisfaction')['Attrition'].mean()\n",
    "\n",
    "# Print the result\n",
    "print(mean_attrition_clust)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80385402",
   "metadata": {},
   "source": [
    "Super summary statistics! The numbers are all fairly similar, with the notable exception that cluster sampling only gives results for the clusters included in the sample."
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
