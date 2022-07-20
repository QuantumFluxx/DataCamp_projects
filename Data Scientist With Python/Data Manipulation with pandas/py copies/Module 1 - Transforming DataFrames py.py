{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "afa7f2c7",
   "metadata": {},
   "source": [
    "# Transforming Data\n",
    "\n",
    "## Inspecting a DataFrame\n",
    "When you get a new DataFrame to work with, the first thing you need to do is explore it\n",
    "and see what it contains.There are several useful methods and attributes for this.\n",
    " - `.head()` returns the first few rows (the “head” of the DataFrame).\n",
    " - `.info()` shows information on each of the columns, such as the data type and number\n",
    "   of missing values.\n",
    " - `.shape` returns the number of rows and columns of the DataFrame.\n",
    " - `.describe()` calculates a few summary statistics for each column.\n",
    " \n",
    "homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018.\n",
    "The individual column is the number of homeless individuals not part of a family with children.\n",
    "The family_members column is the number of homeless individuals part of a family with children.\n",
    "The state_pop column is the state's total population.\n",
    "\n",
    "`pandas` is imported for you.\n",
    "\n",
    "\n",
    "Print the head of the `homelessness` DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "54efbbfc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Unnamed: 0              region       state  individuals  family_members  \\\n",
      "0           0  East South Central     Alabama       2570.0           864.0   \n",
      "1           1             Pacific      Alaska       1434.0           582.0   \n",
      "2           2            Mountain     Arizona       7259.0          2606.0   \n",
      "3           3  West South Central    Arkansas       2280.0           432.0   \n",
      "4           4             Pacific  California     109008.0         20964.0   \n",
      "\n",
      "   state_pop  \n",
      "0    4887681  \n",
      "1     735139  \n",
      "2    7158024  \n",
      "3    3009733  \n",
      "4   39461588  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "homelessness = pd.read_csv('datasets/homelessness.csv')\n",
    "\n",
    "# Print the head of the homelessness data\n",
    "print(homelessness.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ad280c31",
   "metadata": {},
   "source": [
    "Print information about the column types and missing values in homelessness."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f0cb5ccf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 51 entries, 0 to 50\n",
      "Data columns (total 6 columns):\n",
      " #   Column          Non-Null Count  Dtype  \n",
      "---  ------          --------------  -----  \n",
      " 0   Unnamed: 0      51 non-null     int64  \n",
      " 1   region          51 non-null     object \n",
      " 2   state           51 non-null     object \n",
      " 3   individuals     51 non-null     float64\n",
      " 4   family_members  51 non-null     float64\n",
      " 5   state_pop       51 non-null     int64  \n",
      "dtypes: float64(2), int64(2), object(2)\n",
      "memory usage: 2.5+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "# Print information about homelessness\n",
    "print(homelessness.info())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "524a5d57",
   "metadata": {},
   "source": [
    "Print the number of rows and columns in homelessness."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dd428afb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(51, 6)\n"
     ]
    }
   ],
   "source": [
    "# Print the shape of homelessness\n",
    "print(homelessness.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "295720dc",
   "metadata": {},
   "source": [
    "Print some summary statistics that `describe` the homelessness DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "edc052ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Unnamed: 0    individuals  family_members     state_pop\n",
      "count   51.000000      51.000000       51.000000  5.100000e+01\n",
      "mean    25.000000    7225.784314     3504.882353  6.405637e+06\n",
      "std     14.866069   15991.025083     7805.411811  7.327258e+06\n",
      "min      0.000000     434.000000       75.000000  5.776010e+05\n",
      "25%     12.500000    1446.500000      592.000000  1.777414e+06\n",
      "50%     25.000000    3082.000000     1482.000000  4.461153e+06\n",
      "75%     37.500000    6781.500000     3196.000000  7.340946e+06\n",
      "max     50.000000  109008.000000    52070.000000  3.946159e+07\n"
     ]
    }
   ],
   "source": [
    "# Print a description of homelessness\n",
    "print(homelessness.describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7917781f",
   "metadata": {},
   "source": [
    "## Parts of a DataFrame\n",
    "To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:\n",
    "\n",
    "* `values`: A two-dimensional NumPy array of values.\n",
    "* `columns`: An index of columns: the column names.\n",
    "* `index`: An index for the rows: either row numbers or row names.\n",
    "\n",
    "You can usually think of indexes as a list of strings or numbers, though the pandas Index data type allows for more sophisticated options. (These will be covered later in the course.)\n",
    "\n",
    "`homelessness` is available.\n",
    "\n",
    "\n",
    "* Import `pandas` using the alias pd.\n",
    "* Print a 2D `NumPy` array of the values in homelessness.\n",
    "* Print the column names of `homelessness`.\n",
    "* Print the index of `homelessness`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7bb02384",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 'East South Central' 'Alabama' 2570.0 864.0 4887681]\n",
      " [1 'Pacific' 'Alaska' 1434.0 582.0 735139]\n",
      " [2 'Mountain' 'Arizona' 7259.0 2606.0 7158024]\n",
      " [3 'West South Central' 'Arkansas' 2280.0 432.0 3009733]\n",
      " [4 'Pacific' 'California' 109008.0 20964.0 39461588]\n",
      " [5 'Mountain' 'Colorado' 7607.0 3250.0 5691287]\n",
      " [6 'New England' 'Connecticut' 2280.0 1696.0 3571520]\n",
      " [7 'South Atlantic' 'Delaware' 708.0 374.0 965479]\n",
      " [8 'South Atlantic' 'District of Columbia' 3770.0 3134.0 701547]\n",
      " [9 'South Atlantic' 'Florida' 21443.0 9587.0 21244317]\n",
      " [10 'South Atlantic' 'Georgia' 6943.0 2556.0 10511131]\n",
      " [11 'Pacific' 'Hawaii' 4131.0 2399.0 1420593]\n",
      " [12 'Mountain' 'Idaho' 1297.0 715.0 1750536]\n",
      " [13 'East North Central' 'Illinois' 6752.0 3891.0 12723071]\n",
      " [14 'East North Central' 'Indiana' 3776.0 1482.0 6695497]\n",
      " [15 'West North Central' 'Iowa' 1711.0 1038.0 3148618]\n",
      " [16 'West North Central' 'Kansas' 1443.0 773.0 2911359]\n",
      " [17 'East South Central' 'Kentucky' 2735.0 953.0 4461153]\n",
      " [18 'West South Central' 'Louisiana' 2540.0 519.0 4659690]\n",
      " [19 'New England' 'Maine' 1450.0 1066.0 1339057]\n",
      " [20 'South Atlantic' 'Maryland' 4914.0 2230.0 6035802]\n",
      " [21 'New England' 'Massachusetts' 6811.0 13257.0 6882635]\n",
      " [22 'East North Central' 'Michigan' 5209.0 3142.0 9984072]\n",
      " [23 'West North Central' 'Minnesota' 3993.0 3250.0 5606249]\n",
      " [24 'East South Central' 'Mississippi' 1024.0 328.0 2981020]\n",
      " [25 'West North Central' 'Missouri' 3776.0 2107.0 6121623]\n",
      " [26 'Mountain' 'Montana' 983.0 422.0 1060665]\n",
      " [27 'West North Central' 'Nebraska' 1745.0 676.0 1925614]\n",
      " [28 'Mountain' 'Nevada' 7058.0 486.0 3027341]\n",
      " [29 'New England' 'New Hampshire' 835.0 615.0 1353465]\n",
      " [30 'Mid-Atlantic' 'New Jersey' 6048.0 3350.0 8886025]\n",
      " [31 'Mountain' 'New Mexico' 1949.0 602.0 2092741]\n",
      " [32 'Mid-Atlantic' 'New York' 39827.0 52070.0 19530351]\n",
      " [33 'South Atlantic' 'North Carolina' 6451.0 2817.0 10381615]\n",
      " [34 'West North Central' 'North Dakota' 467.0 75.0 758080]\n",
      " [35 'East North Central' 'Ohio' 6929.0 3320.0 11676341]\n",
      " [36 'West South Central' 'Oklahoma' 2823.0 1048.0 3940235]\n",
      " [37 'Pacific' 'Oregon' 11139.0 3337.0 4181886]\n",
      " [38 'Mid-Atlantic' 'Pennsylvania' 8163.0 5349.0 12800922]\n",
      " [39 'New England' 'Rhode Island' 747.0 354.0 1058287]\n",
      " [40 'South Atlantic' 'South Carolina' 3082.0 851.0 5084156]\n",
      " [41 'West North Central' 'South Dakota' 836.0 323.0 878698]\n",
      " [42 'East South Central' 'Tennessee' 6139.0 1744.0 6771631]\n",
      " [43 'West South Central' 'Texas' 19199.0 6111.0 28628666]\n",
      " [44 'Mountain' 'Utah' 1904.0 972.0 3153550]\n",
      " [45 'New England' 'Vermont' 780.0 511.0 624358]\n",
      " [46 'South Atlantic' 'Virginia' 3928.0 2047.0 8501286]\n",
      " [47 'Pacific' 'Washington' 16424.0 5880.0 7523869]\n",
      " [48 'South Atlantic' 'West Virginia' 1021.0 222.0 1804291]\n",
      " [49 'East North Central' 'Wisconsin' 2740.0 2167.0 5807406]\n",
      " [50 'Mountain' 'Wyoming' 434.0 205.0 577601]]\n"
     ]
    }
   ],
   "source": [
    "# Import pandas using the alias pd\n",
    "import pandas as pd\n",
    "\n",
    "# Print the values of homelessness\n",
    "print(homelessness.values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8718a28e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Unnamed: 0', 'region', 'state', 'individuals', 'family_members',\n",
      "       'state_pop'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Print the column index of homelessness\n",
    "print(homelessness.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e06a5f6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RangeIndex(start=0, stop=51, step=1)\n"
     ]
    }
   ],
   "source": [
    "# Print the row index of homelessness\n",
    "print(homelessness.index)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62bad780",
   "metadata": {},
   "source": [
    "## Sorting rows\n",
    "Finding interesting bits of data in a DataFrame is often easier if you change the order of the rows. You can sort the rows by passing a column name to `.sort_values()`.\n",
    "\n",
    "In cases where rows have the same value (this is common if you sort on a categorical variable), you may wish to break the ties by sorting on another column. You can sort on multiple columns in this way by passing a list of column names.\n",
    "\n",
    "```python\n",
    "one column\tdf.sort_values(\"breed\")\n",
    "multiple columns\tdf.sort_values([\"breed\", \"weight_kg\"])\n",
    "```\n",
    "\n",
    "By combining `.sort_values()` with `.head()`, you can answer questions in the form, \"What are the top cases where…?\".\n",
    "\n",
    "homelessness is available and `pandas` is loaded as pd.\n",
    "\n",
    "* Sort `homelessness` by the number of homeless individuals, from smallest to largest, and save this as `homelessness_ind`.\n",
    "* Print the head of the sorted DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0bad7fac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Unnamed: 0              region         state  individuals  family_members  \\\n",
      "50          50            Mountain       Wyoming        434.0           205.0   \n",
      "34          34  West North Central  North Dakota        467.0            75.0   \n",
      "7            7      South Atlantic      Delaware        708.0           374.0   \n",
      "39          39         New England  Rhode Island        747.0           354.0   \n",
      "45          45         New England       Vermont        780.0           511.0   \n",
      "\n",
      "    state_pop  \n",
      "50     577601  \n",
      "34     758080  \n",
      "7      965479  \n",
      "39    1058287  \n",
      "45     624358  \n"
     ]
    }
   ],
   "source": [
    "# Sort homelessness by individuals\n",
    "homelessness_ind = homelessness.sort_values('individuals')\n",
    "\n",
    "# Print the top few rows\n",
    "print(homelessness_ind.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b740c86",
   "metadata": {},
   "source": [
    "* Sort `homelessness` by the number of homeless family_members in descending order, and save this as `homelessness_fam`.\n",
    "* Print the head of the sorted DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9aee4b1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Unnamed: 0              region          state  individuals  \\\n",
      "32          32        Mid-Atlantic       New York      39827.0   \n",
      "4            4             Pacific     California     109008.0   \n",
      "21          21         New England  Massachusetts       6811.0   \n",
      "9            9      South Atlantic        Florida      21443.0   \n",
      "43          43  West South Central          Texas      19199.0   \n",
      "\n",
      "    family_members  state_pop  \n",
      "32         52070.0   19530351  \n",
      "4          20964.0   39461588  \n",
      "21         13257.0    6882635  \n",
      "9           9587.0   21244317  \n",
      "43          6111.0   28628666  \n"
     ]
    }
   ],
   "source": [
    "# Sort homelessness by descending family members\n",
    "homelessness_fam = homelessness.sort_values('family_members', ascending=False)\n",
    "\n",
    "# Print the top few rows\n",
    "print(homelessness_fam.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66bc7ff5",
   "metadata": {},
   "source": [
    "* Sort `homelessness` first by region (ascending), and then by number of family members (descending). Save this as `homelessness_reg_fam`.\n",
    "* Print the head of the sorted DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7ce64cea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Unnamed: 0              region      state  individuals  family_members  \\\n",
      "13          13  East North Central   Illinois       6752.0          3891.0   \n",
      "35          35  East North Central       Ohio       6929.0          3320.0   \n",
      "22          22  East North Central   Michigan       5209.0          3142.0   \n",
      "49          49  East North Central  Wisconsin       2740.0          2167.0   \n",
      "14          14  East North Central    Indiana       3776.0          1482.0   \n",
      "\n",
      "    state_pop  \n",
      "13   12723071  \n",
      "35   11676341  \n",
      "22    9984072  \n",
      "49    5807406  \n",
      "14    6695497  \n"
     ]
    }
   ],
   "source": [
    "# Sort homelessness by region, then descending family members\n",
    "homelessness_reg_fam = homelessness.sort_values([\"region\", \"family_members\"], ascending=[True, False])\n",
    "\n",
    "# Print the top few rows\n",
    "print(homelessness_reg_fam.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "659596c3",
   "metadata": {},
   "source": [
    "## Subsetting columns\n",
    "When working with data, you may not need all of the variables in your dataset. Square brackets ([]) can be used to select only the columns that matter to you in an order that makes sense to you. To select only \"col_a\" of the DataFrame df, use\n",
    "```PYTHON\n",
    "df[\"col_a\"]\n",
    "```\n",
    "\n",
    "To select \"col_a\" and \"col_b\" of df, use\n",
    "```PYTHON\n",
    "df[[\"col_a\", \"col_b\"]]\n",
    "```\n",
    "\n",
    "`homelessness` is available and `pandas` is loaded as pd.\n",
    "\n",
    "* Create a DataFrame called `individuals` that contains only the individuals column of `homelessness`.\n",
    "* Print the head of the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "afa72306",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      2570.0\n",
      "1      1434.0\n",
      "2      7259.0\n",
      "3      2280.0\n",
      "4    109008.0\n",
      "Name: individuals, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Select the individuals column\n",
    "individuals = homelessness['individuals']\n",
    "\n",
    "# Print the head of the result\n",
    "print(individuals.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16df19be",
   "metadata": {},
   "source": [
    "* Create a DataFrame called `state_fam` that contains only the state and family_members columns of `homelessness`, in that order.\n",
    "* Print the head of the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e28f7af9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        state  family_members\n",
      "0     Alabama           864.0\n",
      "1      Alaska           582.0\n",
      "2     Arizona          2606.0\n",
      "3    Arkansas           432.0\n",
      "4  California         20964.0\n"
     ]
    }
   ],
   "source": [
    "# Select the state and family_members columns\n",
    "state_fam = homelessness[['state', 'family_members']]\n",
    "\n",
    "# Print the head of the result\n",
    "print(state_fam.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5c7015f",
   "metadata": {},
   "source": [
    "* Create a DataFrame called `ind_state` that contains the individuals and state columns of `homelessness`, in that order.\n",
    "* Print the head of the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ce93b977",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   individuals       state\n",
      "0       2570.0     Alabama\n",
      "1       1434.0      Alaska\n",
      "2       7259.0     Arizona\n",
      "3       2280.0    Arkansas\n",
      "4     109008.0  California\n"
     ]
    }
   ],
   "source": [
    "# Select only the individuals and state columns, in that order\n",
    "ind_state = homelessness[['individuals', 'state']]\n",
    "\n",
    "# Print the head of the result\n",
    "print(ind_state.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f605e22",
   "metadata": {},
   "source": [
    "## Subsetting rows\n",
    "A large part of data science is about finding which bits of your dataset are interesting. One of the simplest techniques for this is to find a subset of rows that match some criteria. This is sometimes known as filtering rows or selecting rows.\n",
    "\n",
    "There are many ways to subset a DataFrame, perhaps the most common is to use relational operators to return True or False for each row, then pass that inside square brackets.\n",
    "\n",
    "```PYTHON\n",
    "dogs[dogs[\"height_cm\"] > 60]\n",
    "dogs[dogs[\"color\"] == \"tan\"]\n",
    "```\n",
    "\n",
    "You can filter for multiple conditions at once by using the \"bitwise and\" operator, &.\n",
    "\n",
    "```PYTHON\n",
    "dogs[(dogs[\"height_cm\"] > 60) & (dogs[\"color\"] == \"tan\")]\n",
    "```\n",
    "\n",
    "`homelessness` is available and `pandas` is loaded as pd.\n",
    "\n",
    "* Filter `homelessness` for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "258d563d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Unnamed: 0              region       state  individuals  family_members  \\\n",
      "4            4             Pacific  California     109008.0         20964.0   \n",
      "9            9      South Atlantic     Florida      21443.0          9587.0   \n",
      "32          32        Mid-Atlantic    New York      39827.0         52070.0   \n",
      "37          37             Pacific      Oregon      11139.0          3337.0   \n",
      "43          43  West South Central       Texas      19199.0          6111.0   \n",
      "47          47             Pacific  Washington      16424.0          5880.0   \n",
      "\n",
      "    state_pop  \n",
      "4    39461588  \n",
      "9    21244317  \n",
      "32   19530351  \n",
      "37    4181886  \n",
      "43   28628666  \n",
      "47    7523869  \n"
     ]
    }
   ],
   "source": [
    "# Filter for rows where individuals is greater than 10000\n",
    "ind_gt_10k = homelessness[homelessness[\"individuals\"] > 10000]\n",
    "\n",
    "# See the result\n",
    "print(ind_gt_10k)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2452d08",
   "metadata": {},
   "source": [
    "Filter `homelessness` for cases where the USA Census region is \"Mountain\", assigning to `mountain_reg`. View the printed result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2b3f31ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Unnamed: 0    region       state  individuals  family_members  state_pop\n",
      "2            2  Mountain     Arizona       7259.0          2606.0    7158024\n",
      "5            5  Mountain    Colorado       7607.0          3250.0    5691287\n",
      "12          12  Mountain       Idaho       1297.0           715.0    1750536\n",
      "26          26  Mountain     Montana        983.0           422.0    1060665\n",
      "28          28  Mountain      Nevada       7058.0           486.0    3027341\n",
      "31          31  Mountain  New Mexico       1949.0           602.0    2092741\n",
      "44          44  Mountain        Utah       1904.0           972.0    3153550\n",
      "50          50  Mountain     Wyoming        434.0           205.0     577601\n"
     ]
    }
   ],
   "source": [
    "# Filter for rows where region is Mountain\n",
    "mountain_reg = homelessness[homelessness[\"region\"] == \"Mountain\"]\n",
    "\n",
    "# See the result\n",
    "print(mountain_reg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96d62d7a",
   "metadata": {},
   "source": [
    "Filter `homelessness` for cases where the number of `family_members` is less than one thousand and the region is \"Pacific\", assigning to `fam_lt_1k_pac`. View the printed result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "04d557d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Unnamed: 0   region   state  individuals  family_members  state_pop\n",
      "1           1  Pacific  Alaska       1434.0           582.0     735139\n"
     ]
    }
   ],
   "source": [
    "# Filter for rows where family_members is less than 1000 \n",
    "# and region is Pacific\n",
    "fam_lt_1k_pac = homelessness[(homelessness[\"family_members\"] < 1000) & (homelessness[\"region\"] == \"Pacific\")]\n",
    "\n",
    "# See the result\n",
    "print(fam_lt_1k_pac)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8978f274",
   "metadata": {},
   "source": [
    "## Subsetting rows by categorical variables\n",
    "Subsetting data based on a categorical variable often involves using the \"or\" operator (|) to select rows from multiple categories. This can get tedious when you want all states in one of three different regions, for example. Instead, use the `.isin()` method, which will allow you to tackle this problem by writing one condition instead of three separate ones.\n",
    "\n",
    "```PYTHON\n",
    "colors = [\"brown\", \"black\", \"tan\"]\n",
    "condition = dogs[\"color\"].isin(colors)\n",
    "dogs[condition]\n",
    "```\n",
    "`homelessness` is available and `pandas` is loaded as pd.\n",
    "\n",
    "Filter `homelessness` for cases where the USA census region is \"South Atlantic\" or it is \"Mid-Atlantic\", assigning to `south_mid_atlantic`. View the printed result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "fa55085e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Unnamed: 0          region                 state  individuals  \\\n",
      "7            7  South Atlantic              Delaware        708.0   \n",
      "8            8  South Atlantic  District of Columbia       3770.0   \n",
      "9            9  South Atlantic               Florida      21443.0   \n",
      "10          10  South Atlantic               Georgia       6943.0   \n",
      "20          20  South Atlantic              Maryland       4914.0   \n",
      "30          30    Mid-Atlantic            New Jersey       6048.0   \n",
      "32          32    Mid-Atlantic              New York      39827.0   \n",
      "33          33  South Atlantic        North Carolina       6451.0   \n",
      "38          38    Mid-Atlantic          Pennsylvania       8163.0   \n",
      "40          40  South Atlantic        South Carolina       3082.0   \n",
      "46          46  South Atlantic              Virginia       3928.0   \n",
      "48          48  South Atlantic         West Virginia       1021.0   \n",
      "\n",
      "    family_members  state_pop  \n",
      "7            374.0     965479  \n",
      "8           3134.0     701547  \n",
      "9           9587.0   21244317  \n",
      "10          2556.0   10511131  \n",
      "20          2230.0    6035802  \n",
      "30          3350.0    8886025  \n",
      "32         52070.0   19530351  \n",
      "33          2817.0   10381615  \n",
      "38          5349.0   12800922  \n",
      "40           851.0    5084156  \n",
      "46          2047.0    8501286  \n",
      "48           222.0    1804291  \n"
     ]
    }
   ],
   "source": [
    "# Subset for rows in South Atlantic or Mid-Atlantic regions\n",
    "south_mid_atlantic = homelessness[(homelessness[\"region\"] == \"South Atlantic\") | (homelessness[\"region\"] == \"Mid-Atlantic\")]\n",
    "\n",
    "# See the result\n",
    "print(south_mid_atlantic)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a24eda4e",
   "metadata": {},
   "source": [
    "Filter `homelessness` for cases where the USA census state is in the list of Mojave states, canu, assigning to `mojave_homelessness`. View the printed result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "74dec4d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Unnamed: 0    region       state  individuals  family_members  state_pop\n",
      "2            2  Mountain     Arizona       7259.0          2606.0    7158024\n",
      "4            4   Pacific  California     109008.0         20964.0   39461588\n",
      "28          28  Mountain      Nevada       7058.0           486.0    3027341\n",
      "44          44  Mountain        Utah       1904.0           972.0    3153550\n"
     ]
    }
   ],
   "source": [
    "# The Mojave Desert states\n",
    "canu = [\"California\", \"Arizona\", \"Nevada\", \"Utah\"]\n",
    "\n",
    "# Filter for rows in the Mojave Desert states\n",
    "mojave_homelessness = homelessness[homelessness[\"state\"].isin(canu)]\n",
    "\n",
    "# See the result\n",
    "print(mojave_homelessness)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d2a4026",
   "metadata": {},
   "source": [
    "## Adding new columns\n",
    "You aren't stuck with just the data you are given. Instead, you can add new columns to a DataFrame. This has many names, such as transforming, mutating, and feature engineering.\n",
    "\n",
    "You can create new columns from scratch, but it is also common to derive them from other columns, for example, by adding columns together or by changing their units.\n",
    "\n",
    "`homelessness` is available and `pandas` is loaded as pd.\n",
    "\n",
    "* Add a new column to `homelessness`, named `total`, containing the sum of the `individuals` and `family_members` columns.\n",
    "* Add another column to` homelessness`, named `p_individuals`, containing the proportion of homeless people in each state who are individuals."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "08355382",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Unnamed: 0              region                 state  individuals  \\\n",
      "0            0  East South Central               Alabama       2570.0   \n",
      "1            1             Pacific                Alaska       1434.0   \n",
      "2            2            Mountain               Arizona       7259.0   \n",
      "3            3  West South Central              Arkansas       2280.0   \n",
      "4            4             Pacific            California     109008.0   \n",
      "5            5            Mountain              Colorado       7607.0   \n",
      "6            6         New England           Connecticut       2280.0   \n",
      "7            7      South Atlantic              Delaware        708.0   \n",
      "8            8      South Atlantic  District of Columbia       3770.0   \n",
      "9            9      South Atlantic               Florida      21443.0   \n",
      "10          10      South Atlantic               Georgia       6943.0   \n",
      "11          11             Pacific                Hawaii       4131.0   \n",
      "12          12            Mountain                 Idaho       1297.0   \n",
      "13          13  East North Central              Illinois       6752.0   \n",
      "14          14  East North Central               Indiana       3776.0   \n",
      "15          15  West North Central                  Iowa       1711.0   \n",
      "16          16  West North Central                Kansas       1443.0   \n",
      "17          17  East South Central              Kentucky       2735.0   \n",
      "18          18  West South Central             Louisiana       2540.0   \n",
      "19          19         New England                 Maine       1450.0   \n",
      "20          20      South Atlantic              Maryland       4914.0   \n",
      "21          21         New England         Massachusetts       6811.0   \n",
      "22          22  East North Central              Michigan       5209.0   \n",
      "23          23  West North Central             Minnesota       3993.0   \n",
      "24          24  East South Central           Mississippi       1024.0   \n",
      "25          25  West North Central              Missouri       3776.0   \n",
      "26          26            Mountain               Montana        983.0   \n",
      "27          27  West North Central              Nebraska       1745.0   \n",
      "28          28            Mountain                Nevada       7058.0   \n",
      "29          29         New England         New Hampshire        835.0   \n",
      "30          30        Mid-Atlantic            New Jersey       6048.0   \n",
      "31          31            Mountain            New Mexico       1949.0   \n",
      "32          32        Mid-Atlantic              New York      39827.0   \n",
      "33          33      South Atlantic        North Carolina       6451.0   \n",
      "34          34  West North Central          North Dakota        467.0   \n",
      "35          35  East North Central                  Ohio       6929.0   \n",
      "36          36  West South Central              Oklahoma       2823.0   \n",
      "37          37             Pacific                Oregon      11139.0   \n",
      "38          38        Mid-Atlantic          Pennsylvania       8163.0   \n",
      "39          39         New England          Rhode Island        747.0   \n",
      "40          40      South Atlantic        South Carolina       3082.0   \n",
      "41          41  West North Central          South Dakota        836.0   \n",
      "42          42  East South Central             Tennessee       6139.0   \n",
      "43          43  West South Central                 Texas      19199.0   \n",
      "44          44            Mountain                  Utah       1904.0   \n",
      "45          45         New England               Vermont        780.0   \n",
      "46          46      South Atlantic              Virginia       3928.0   \n",
      "47          47             Pacific            Washington      16424.0   \n",
      "48          48      South Atlantic         West Virginia       1021.0   \n",
      "49          49  East North Central             Wisconsin       2740.0   \n",
      "50          50            Mountain               Wyoming        434.0   \n",
      "\n",
      "    family_members  state_pop     total  p_individuals  \n",
      "0            864.0    4887681    3434.0       0.748398  \n",
      "1            582.0     735139    2016.0       0.711310  \n",
      "2           2606.0    7158024    9865.0       0.735834  \n",
      "3            432.0    3009733    2712.0       0.840708  \n",
      "4          20964.0   39461588  129972.0       0.838704  \n",
      "5           3250.0    5691287   10857.0       0.700654  \n",
      "6           1696.0    3571520    3976.0       0.573441  \n",
      "7            374.0     965479    1082.0       0.654344  \n",
      "8           3134.0     701547    6904.0       0.546060  \n",
      "9           9587.0   21244317   31030.0       0.691041  \n",
      "10          2556.0   10511131    9499.0       0.730919  \n",
      "11          2399.0    1420593    6530.0       0.632619  \n",
      "12           715.0    1750536    2012.0       0.644632  \n",
      "13          3891.0   12723071   10643.0       0.634408  \n",
      "14          1482.0    6695497    5258.0       0.718144  \n",
      "15          1038.0    3148618    2749.0       0.622408  \n",
      "16           773.0    2911359    2216.0       0.651173  \n",
      "17           953.0    4461153    3688.0       0.741594  \n",
      "18           519.0    4659690    3059.0       0.830337  \n",
      "19          1066.0    1339057    2516.0       0.576312  \n",
      "20          2230.0    6035802    7144.0       0.687850  \n",
      "21         13257.0    6882635   20068.0       0.339396  \n",
      "22          3142.0    9984072    8351.0       0.623758  \n",
      "23          3250.0    5606249    7243.0       0.551291  \n",
      "24           328.0    2981020    1352.0       0.757396  \n",
      "25          2107.0    6121623    5883.0       0.641849  \n",
      "26           422.0    1060665    1405.0       0.699644  \n",
      "27           676.0    1925614    2421.0       0.720777  \n",
      "28           486.0    3027341    7544.0       0.935578  \n",
      "29           615.0    1353465    1450.0       0.575862  \n",
      "30          3350.0    8886025    9398.0       0.643541  \n",
      "31           602.0    2092741    2551.0       0.764014  \n",
      "32         52070.0   19530351   91897.0       0.433387  \n",
      "33          2817.0   10381615    9268.0       0.696051  \n",
      "34            75.0     758080     542.0       0.861624  \n",
      "35          3320.0   11676341   10249.0       0.676066  \n",
      "36          1048.0    3940235    3871.0       0.729269  \n",
      "37          3337.0    4181886   14476.0       0.769481  \n",
      "38          5349.0   12800922   13512.0       0.604130  \n",
      "39           354.0    1058287    1101.0       0.678474  \n",
      "40           851.0    5084156    3933.0       0.783626  \n",
      "41           323.0     878698    1159.0       0.721311  \n",
      "42          1744.0    6771631    7883.0       0.778764  \n",
      "43          6111.0   28628666   25310.0       0.758554  \n",
      "44           972.0    3153550    2876.0       0.662031  \n",
      "45           511.0     624358    1291.0       0.604183  \n",
      "46          2047.0    8501286    5975.0       0.657406  \n",
      "47          5880.0    7523869   22304.0       0.736370  \n",
      "48           222.0    1804291    1243.0       0.821400  \n",
      "49          2167.0    5807406    4907.0       0.558386  \n",
      "50           205.0     577601     639.0       0.679186  \n"
     ]
    }
   ],
   "source": [
    "# Add total col as sum of individuals and family_members\n",
    "homelessness[\"total\"] = homelessness[\"individuals\"] + homelessness[\"family_members\"]\n",
    "\n",
    "# Add p_individuals col as proportion of total that are individuals\n",
    "homelessness[\"p_individuals\"] = homelessness[\"individuals\"] / homelessness[\"total\"]\n",
    "\n",
    "# See the result\n",
    "print(homelessness)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b86bb374",
   "metadata": {},
   "source": [
    "## Combo-attack!\n",
    "You've seen the four most common types of data manipulation: sorting rows, subsetting columns, subsetting rows, and adding new columns. In a real-life data analysis, you can mix and match these four manipulations to answer a multitude of questions.\n",
    "\n",
    "In this exercise, you'll answer the question, \"Which state has the highest number of homeless individuals per 10,000 people in the state?\" Combine your new `pandas` skills to find out.\n",
    "\n",
    "* Add a column to `homelessness`, `indiv_per_10k`, containing the number of homeless individuals per ten thousand people in each state.\n",
    "* Subset rows where `indiv_per_10k` is higher than 20, assigning to `high_homelessness`.\n",
    "* Sort `high_homelessness` by descending `indiv_per_10k`, assigning to `high_homelessness_srt`.\n",
    "* Select only the state and `indiv_per_10k` columns of `high_homelessness_srt` and save as result. Look at the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5f3aa23a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   state  indiv_per_10k\n",
      "8   District of Columbia      53.738381\n",
      "11                Hawaii      29.079406\n",
      "4             California      27.623825\n",
      "37                Oregon      26.636307\n",
      "28                Nevada      23.314189\n",
      "47            Washington      21.829195\n",
      "32              New York      20.392363\n"
     ]
    }
   ],
   "source": [
    "# Create indiv_per_10k col as homeless individuals per 10k state pop\n",
    "homelessness[\"indiv_per_10k\"] = 10000 * homelessness[\"individuals\"] / homelessness[\"state_pop\"] \n",
    "\n",
    "# Subset rows for indiv_per_10k greater than 20\n",
    "high_homelessness = homelessness[homelessness[\"indiv_per_10k\"] > 20]\n",
    "\n",
    "# Sort high_homelessness by descending indiv_per_10k\n",
    "high_homelessness_srt = high_homelessness.sort_values(\"indiv_per_10k\", ascending=False)\n",
    "\n",
    "# From high_homelessness_srt, select the state and indiv_per_10k cols\n",
    "result = high_homelessness_srt[[\"state\", \"indiv_per_10k\"]]\n",
    "\n",
    "# See the result\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5adf9cc8",
   "metadata": {},
   "source": [
    "Cool combination! District of Columbia has the highest number of homeless individuals - almost 54 per ten thousand people. This is almost double the number of the next-highest state, Hawaii. If you combine new column addition, row subsetting, sorting, and column selection, you can answer lots of questions like this."
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
