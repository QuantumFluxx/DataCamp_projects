{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "96c55c5f",
   "metadata": {},
   "source": [
    "# Importing data from other file types\n",
    "\n",
    "## Not so flat any more\n",
    "In Chapter 1, you learned how to use the IPython magic command ! ls to explore your current working directory. You can also do this natively in Python using the library os, which consists of miscellaneous operating system interfaces.\n",
    "\n",
    "The first line of the following code imports the library os, the second line stores the name of the current directory in a string called wd and the third outputs the contents of the directory in a list to the shell.\n",
    "```python\n",
    "import os\n",
    "wd = os.getcwd()\n",
    "os.listdir(wd)\n",
    "```\n",
    "Run this code in the IPython shell and answer the following questions. Ignore the files that begin with ..\n",
    "\n",
    "Check out the contents of your current directory and answer the following questions: (1) which file is in your directory and NOT an example of a flat file; (2) why is it not a flat file?\n",
    "\n",
    "\n",
    "* database.db is not a flat file because relational databases contain structured relationships and flat files do not.\n",
    "\n",
    "* **battledeath.xlsx is not a flat because it is a spreadsheet consisting of many sheets, not a single table.**\n",
    "\n",
    "* titanic.txt is not a flat file because it is a .txt, not a .csv.\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Loading a pickled file\n",
    "There are a number of datatypes that cannot be saved easily to flat files, such as lists and dictionaries. If you want your files to be human readable, you may want to save them as text files in a clever manner. JSONs, which you will see in a later chapter, are appropriate for Python dictionaries.\n",
    "\n",
    "However, if you merely want to be able to import them into Python, you can serialize them. All this means is converting the object into a sequence of bytes, or a bytestream.\n",
    "\n",
    "In this exercise, you'll import the pickle package, open a previously pickled data structure from a file and load it.\n",
    "\n",
    "* Import the `pickle` package.\n",
    "* Complete the second argument of `open()` so that it is read only for a binary file. This argument will be a string of two letters, one signifying 'read only', the other 'binary'.\n",
    "* Pass the correct argument to `pickle.load()`; it should use the variable that is bound to open.\n",
    "* Print the data, d.\n",
    "* Print the datatype of d; take your mind back to your previous use of the function `type()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d66970e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import pickle package\n",
    "import pickle\n",
    "\n",
    "# Open pickle file and load data\n",
    "with open('data.pkl', 'rb') as file:\n",
    "    d = pickle.load(file)\n",
    "\n",
    "# Print data\n",
    "print(d)\n",
    "\n",
    "# Print datatype\n",
    "print(type(d))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f80815df",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Listing sheets in Excel files\n",
    "Whether you like it or not, any working data scientist will need to deal with Excel spreadsheets at some point in time. You won't always want to do so in Excel, however!\n",
    "\n",
    "Here, you'll learn how to use pandas to import Excel spreadsheets and how to list the names of the sheets in any loaded .xlsx file.\n",
    "\n",
    "Recall from the video that, given an Excel file imported into a variable spreadsheet, you can retrieve a list of the sheet names using the attribute `spreadsheet.sheet_names`.\n",
    "\n",
    "Specifically, you'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace Research Institute Oslo's (PRIO) dataset. This data contains age-adjusted mortality rates due to war in various countries over several years.\n",
    "\n",
    "* Assign the spreadsheet filename (provided above) to the variable file.\n",
    "* Pass the correct argument to `pd.ExcelFile()` to load the file using pandas, assigning the result to the variable xls.\n",
    "* Print the sheetnames of the Excel spreadsheet by passing the necessary argument to the `print()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "269428d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['2002', '2004']\n"
     ]
    }
   ],
   "source": [
    "# Import pandas\n",
    "import pandas as pd\n",
    "\n",
    "# Assign spreadsheet filename: file\n",
    "file = 'datasets/battledeath.xlsx'\n",
    "\n",
    "# Load spreadsheet: xls\n",
    "xls = pd.ExcelFile(file)\n",
    "\n",
    "# Print sheet names\n",
    "print(xls.sheet_names)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2bb39fd0",
   "metadata": {},
   "source": [
    "Great job!\n",
    "\n",
    "## Importing sheets from Excel files\n",
    "In the previous exercises, you saw that the Excel file contains two sheets, '2002' and '2004'. The next step is to import these.\n",
    "\n",
    "In this exercise, you'll learn how to import any given sheet of your loaded .xlsx file as a DataFrame. You'll be able to do so by specifying either the sheet's name or its index.\n",
    "\n",
    "* Load the sheet '2004' into the DataFrame df1 using its name as a string.\n",
    "* Print the head of df1 to the shell.\n",
    "* Load the sheet 2002 into the DataFrame df2 using its index (0).\n",
    "* Print the head of df2 to the shell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a5ce3fba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  War(country)      2004\n",
      "0  Afghanistan  9.451028\n",
      "1      Albania  0.130354\n",
      "2      Algeria  3.407277\n",
      "3      Andorra  0.000000\n",
      "4       Angola  2.597931\n",
      "  War, age-adjusted mortality due to       2002\n",
      "0                        Afghanistan  36.083990\n",
      "1                            Albania   0.128908\n",
      "2                            Algeria  18.314120\n",
      "3                            Andorra   0.000000\n",
      "4                             Angola  18.964560\n"
     ]
    }
   ],
   "source": [
    "# Load a sheet into a DataFrame by name: df1\n",
    "df1 = xls.parse('2004')\n",
    "\n",
    "# Print the head of the DataFrame df1\n",
    "print(df1.head())\n",
    "\n",
    "# Load a sheet into a DataFrame by index: df2\n",
    "df2 = xls.parse(0)\n",
    "\n",
    "# Print the head of the DataFrame df2\n",
    "print(df2.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d29b1f5",
   "metadata": {},
   "source": [
    "Awesome! You'll typically find yourself referring to the Excel sheet by name, but it's good to know you can also use indexes.\n",
    "\n",
    "## Customizing your spreadsheet import\n",
    "Here, you'll parse your spreadsheets and use additional arguments to skip rows, rename columns and select only particular columns.\n",
    "\n",
    "The spreadsheet `'battledeath.xlsx'` is already loaded as xls.\n",
    "\n",
    "As before, you'll use the method `parse()`. This time, however, you'll add the additional arguments skiprows, names and usecols. These skip rows, name the columns and designate which columns to parse, respectively. All these arguments can be assigned to lists containing the specific row numbers, strings and column numbers, as appropriate.\n",
    "\n",
    "* Parse the first sheet by index. In doing so, skip the first row of data and name the columns 'Country' and 'AAM due to War (2002)' using the argument names. The values passed to skiprows and names all need to be of type list.\n",
    "* Parse the second sheet by index. In doing so, parse only the first column with the usecols parameter, skip the first row and rename the column 'Country'. The argument passed to usecols also needs to be of type list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "65e6e381",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Country  AAM due to War (2002)\n",
      "0              Albania               0.128908\n",
      "1              Algeria              18.314120\n",
      "2              Andorra               0.000000\n",
      "3               Angola              18.964560\n",
      "4  Antigua and Barbuda               0.000000\n",
      "               Country\n",
      "0              Albania\n",
      "1              Algeria\n",
      "2              Andorra\n",
      "3               Angola\n",
      "4  Antigua and Barbuda\n"
     ]
    }
   ],
   "source": [
    "# Parse the first sheet and rename the columns: df1\n",
    "df1 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])\n",
    "\n",
    "# Print the head of the DataFrame df1\n",
    "print(df1.head())\n",
    "\n",
    "# Parse the first column of the second sheet and rename the column: df2\n",
    "df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])\n",
    "\n",
    "# Print the head of the DataFrame df2\n",
    "print(df2.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9695d3f",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## How to import SAS7BDAT\n",
    "How do you correctly import the function SAS7BDAT() from the package sas7bdat?\n",
    "\n",
    "\n",
    "* import SAS7BDAT from sas7bdat\n",
    "\n",
    "* from SAS7BDAT import sas7bdat\n",
    "\n",
    "* import sas7bdat from SAS7BDAT\n",
    "\n",
    "* **from sas7bdat import SAS7BDAT**\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Importing SAS files\n",
    "In this exercise, you'll figure out how to import a SAS file as a DataFrame using SAS7BDAT and pandas. The file `'sales.sas7bdat'` is already in your working directory and both pandas and matplotlib.pyplot have already been imported as follows:\n",
    "```python\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "```\n",
    "The data are adapted from the website of the undergraduate text book Principles of Econometrics by Hill, Griffiths and Lim.\n",
    "\n",
    "* Import the module `SAS7BDAT` from the library sas7bdat.\n",
    "* In the context of the file `'sales.sas7bdat'`, load its contents to a DataFrame `df_sas`, using the method `to_data_frame()` on the object file.\n",
    "* Print the head of the DataFrame `df_sas`.\n",
    "* Execute your entire script to produce a histogram plot!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bed0304c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     YEAR     P           S\n",
      "0  1950.0  12.9  181.899994\n",
      "1  1951.0  11.9  245.000000\n",
      "2  1952.0  10.7  250.199997\n",
      "3  1953.0  11.3  265.899994\n",
      "4  1954.0  11.2  248.500000\n"
     ]
    },
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
    "# Import sas7bdat package\n",
    "from sas7bdat import SAS7BDAT\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Save file to a DataFrame: df_sas\n",
    "with SAS7BDAT('datasets/sales.sas7bdat') as file:\n",
    "    df_sas = file.to_data_frame()\n",
    "\n",
    "# Print head of DataFrame\n",
    "print(df_sas.head())\n",
    "\n",
    "# Plot histograms of a DataFrame feature (pandas and pyplot already imported)\n",
    "pd.DataFrame.hist(df_sas[['P']])\n",
    "plt.ylabel('count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab1541c8",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Using read_stata to import Stata files\n",
    "The pandas package has been imported in the environment as pd and the file disarea.dta is in your working directory. The data consist of disease extents for several diseases in various countries (more information can be found here).\n",
    "\n",
    "What is the correct way of using the `read_stata()` function to import disarea.dta into the object df?\n",
    "\n",
    "\n",
    "* df = 'disarea.dta'\n",
    "\n",
    "* df = read_stata.pd('disarea.dta')\n",
    "\n",
    "* **df = pd.read_stata('disarea.dta')**\n",
    "\n",
    "* df = pd.read_stata(disarea.dta)\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Importing Stata files\n",
    "Here, you'll gain expertise in importing Stata files as DataFrames using the `pd.read_stata()` function from pandas. The last exercise's file, `'disarea.dta'`, is still in your working directory.\n",
    "\n",
    "* Use `pd.read_stata()` to load the file `'disarea.dta'` into the DataFrame df.\n",
    "* Print the head of the DataFrame df.\n",
    "* Visualize your results by plotting a histogram of the column disa10. We’ve already provided this code for you, so just run it!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c8cddb02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  wbcode               country  disa1  disa2  disa3  disa4  disa5  disa6  \\\n",
      "0    AFG           Afghanistan   0.00   0.00   0.76   0.73    0.0   0.00   \n",
      "1    AGO                Angola   0.32   0.02   0.56   0.00    0.0   0.00   \n",
      "2    ALB               Albania   0.00   0.00   0.02   0.00    0.0   0.00   \n",
      "3    ARE  United Arab Emirates   0.00   0.00   0.00   0.00    0.0   0.00   \n",
      "4    ARG             Argentina   0.00   0.24   0.24   0.00    0.0   0.23   \n",
      "\n",
      "   disa7  disa8  ...  disa16  disa17  disa18  disa19  disa20  disa21  disa22  \\\n",
      "0   0.00    0.0  ...     0.0     0.0     0.0    0.00    0.00     0.0    0.00   \n",
      "1   0.56    0.0  ...     0.0     0.4     0.0    0.61    0.00     0.0    0.99   \n",
      "2   0.00    0.0  ...     0.0     0.0     0.0    0.00    0.00     0.0    0.00   \n",
      "3   0.00    0.0  ...     0.0     0.0     0.0    0.00    0.00     0.0    0.00   \n",
      "4   0.00    0.0  ...     0.0     0.0     0.0    0.00    0.05     0.0    0.00   \n",
      "\n",
      "   disa23  disa24  disa25  \n",
      "0    0.02    0.00    0.00  \n",
      "1    0.98    0.61    0.00  \n",
      "2    0.00    0.00    0.16  \n",
      "3    0.00    0.00    0.00  \n",
      "4    0.01    0.00    0.11  \n",
      "\n",
      "[5 rows x 27 columns]\n"
     ]
    },
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
    "# Import pandas\n",
    "import pandas as pd\n",
    "\n",
    "# Load Stata file into a pandas DataFrame: df\n",
    "df = pd.read_stata('datasets/disarea.dta')\n",
    "\n",
    "# Print the head of the DataFrame df\n",
    "print(df.head())\n",
    "\n",
    "# Plot histogram of one column of the DataFrame\n",
    "pd.DataFrame.hist(df[['disa10']])\n",
    "plt.xlabel('Extent of disease')\n",
    "plt.ylabel('Number of countries')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aca2d8b5",
   "metadata": {},
   "source": [
    "Great job!\n",
    "\n",
    "## Using File to import HDF5 files\n",
    "The h5py package has been imported in the environment and the file `LIGO_data.hdf5` is loaded in the object `h5py_file`.\n",
    "\n",
    "What is the correct way of using the h5py function, `File()`, to import the file in h5py_file into an object, `h5py_data`, for reading only?\n",
    "\n",
    "* h5py_data = File(h5py_file, 'r')\n",
    "\n",
    "* **h5py_data = h5py.File(h5py_file, 'r')**\n",
    "\n",
    "* h5py_data = h5py.File(h5py_file, read)\n",
    "\n",
    "* h5py_data = h5py.File(h5py_file, 'read')\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Using h5py to import HDF5 files\n",
    "The file `'LIGO_data.hdf5'` is already in your working directory. In this exercise, you'll import it using the h5py library. You'll also print out its datatype to confirm you have imported it correctly. You'll then study the structure of the file in order to see precisely what HDF groups it contains.\n",
    "\n",
    "You can find the LIGO data plus loads of documentation and tutorials here. There is also a great tutorial on Signal Processing with the data here.\n",
    "\n",
    "* Import the package `h5py`.\n",
    "* Assign the name of the file to the variable file.\n",
    "* Load the file as read only into the variable data.\n",
    "* Print the datatype of data.\n",
    "* Print the names of the groups in the HDF5 file `'LIGO_data.hdf5'`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d71b6981",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'h5py._hl.files.File'>\n",
      "meta\n",
      "quality\n",
      "strain\n"
     ]
    }
   ],
   "source": [
    "# Import packages\n",
    "import numpy as np\n",
    "import h5py\n",
    "\n",
    "# Assign filename: file\n",
    "file = 'datasets/L-L1_LOSC_4_V1-1126259446-32.hdf5'\n",
    "\n",
    "# Load file: data\n",
    "data = h5py.File(file, 'r')\n",
    "\n",
    "# Print the datatype of the loaded file\n",
    "print(type(data))\n",
    "\n",
    "# Print the keys of the file\n",
    "for key in data.keys():\n",
    "    print(key)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b316108",
   "metadata": {},
   "source": [
    "Great job!\n",
    "\n",
    "## Extracting data from your HDF5 file\n",
    "In this exercise, you'll extract some of the LIGO experiment's actual data from the HDF5 file and you'll visualize it.\n",
    "\n",
    "To do so, you'll need to first explore the HDF5 group 'strain'.\n",
    "\n",
    "* Assign the HDF5 group `data['strain']` to group.\n",
    "* In the for loop, print out the keys of the HDF5 group in group.\n",
    "* Assign the time series data `data['strain']['Strain']` to a NumPy array called strain.\n",
    "* Set `num_samples` equal to 10000, the number of time points we wish to sample.\n",
    "* Execute the rest of the code to produce a plot of the time series data in `LIGO_data.hdf5`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c0dec1df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Strain\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYoAAAERCAYAAABl3+CQAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAABQjUlEQVR4nO2dd9gcVfXHvye9F9L7m55ASIEACb2ElgQCCIqIXREVf1hQqqCCgmJDQRFRsYBIbwktQOgJJKSQkJCE9F5II72c3x+7k707e+fOnTt3dmb3vZ/nyZN9Z2dn78zO3HPvued8DzEzHA6Hw+EIok7aDXA4HA5HtnGGwuFwOBxKnKFwOBwOhxJnKBwOh8OhxBkKh8PhcChxhsLhcDgcSqrWUBDR34loHRHNtnS854hoMxE949t+GhG9R0QziOgNIupj4/scDocjK1StoQBwH4CzLB7vdgCfl2z/M4DPMfNQAA8AuMHidzocDkfqVK2hYObXAHwsbiOi3vmZwTQiep2IBkQ43ksAtsneAtAi/7olgFWmbXY4HI4sUi/tBpSZewBczswLiOgYAH8CcGrMY34NwAQi2glgK4ARMY/ncDgcmaLWGAoiagbgWAAPE5G3uWH+vQsA/EzysZXMfGbIob8HYDQzTyGiHwL4LXLGw+FwOKqCWmMokHOzbc6vJRTBzI8BeCzqAYmoHYAhzDwlv+l/AJ6L00iHw+HIGlW7RuGHmbcCWExEFwEA5RgS87CbALQkon75v08HMDfmMR0OhyNTULWqxxLRfwGcDKAtgLUAbgLwMnJRSp0A1AfwIDPLXE6y470OYACAZgA2AvgqMz9PROcj57Y6gJzh+AozL7J7Ng6Hw5EeVWsoHA6Hw2GHWuN6cjgcDocZVbmY3bZtW66pqUm7GQ6Hw1ExTJs2bQMzt5O9V5WGoqamBlOnTk27GQ6Hw1ExENHSoPdScT0R0UVENIeIDhDR8IB9uhHRK0Q0N7/vleVup8PhcDjSW6OYDeACAK8p9tkH4AfMPBC5bOdvE9Gh5Wicw+FwOAqk4npi5rkAIGRIy/ZZDWB1/vU2IpoLoAuAD8rRRofD4XDkqIioJyKqATAMwBTFPpcR0VQimrp+/fqytc3hcDiqncRmFEQ0EUBHyVvXM/OTEY7TDMCjAL6bz66Wwsz3ICf6h+HDh7vkEIfD4bBEYoaCmUfFPQYR1UfOSNyf12NyOBwOR5nJrOuJcgsYfwMwl5l/m3Z7HA6Ho7aSVnjs+US0AsBIAOOJ6Pn89s5ENCG/23HIVZQ7NV9mdAYRjU6jvQ6HwyFj2669eHLGyrSbkThpRT09DuBxyfZVAEbnX78BIDgsyuFwOFLm5NsnYeP2Pdi7n3HhkV3Tbk5iZNb15HA4HFln4/Y9AICrHp6ZckuSxRkKh8PhcChxhsKROU741cuouWY8du7Zn3ZTHI5AalOJBmcoHJmCmbH8450AgMenV/8ioaNymbliS9pNKBvOUDgyxb4DhVHaL5+bl2JLHA41e/YdSLsJZcMZCkem+GBVIfl+y869KbbE4VCzesvOtJtQNpyhcGSK/3twetpNcDi0uPrRWUV/b9lRvQMbZygcmWLpxh1pN8HhMGL11uqdYThD4XA4HAbs2lu8RlHNQVDOUDgcDodDiTMUDofDYYFX51dvHRxnKBwOh8MCD09dnnYTEsMZCofDgPlrt+HOlxek3QyHoyykoh7rcFQ6Z/zuNQDA/gPAlaP6ptyaYnbu2Y+G9eqgTh0nvlxO3GK2IxXeWrgB1/hitauZ95ZtKtm2Ka/OmSXWbdt18PXvJs5PsSWlHDjAGHjjc+h13YTwnR1WOVDFlsIZigxzyb1T8OC7y3Hbs7VDymLd1l0l215fuCGFlqiZvmxz2k0I5OlZq9JuQq1lSRXnADlDkVFWbS4k79z96kcptiRdDhzI3ijt2sfeT7sJgXy4ZtvB1wvWblPs6XDo4wxFRpm6tNQNU+3kyqRnn48z6A7zuO+tJQdfP1ELSnSmxcJ1tcsIO0ORUe56eWHR36JfvFq503fOAFAJtmPzjuwYjh1CDY+7Xqm9M9Gk2bMvezPdJHGGIqN86HMbzFpe/dr3768sPcc1W7JvILft2pd2ExyORHGGokK44YnZaTehbAzo2Pzg61tryUJ+Vtm8Y0+tquTmkOMMRYWwRhIRVK2cM6Rz2k0IROYC/Nsbi1NoSfJMeH81hv7sRRx328tpNyVzrK0FrmARZygyyL79tadyVqWxdsvukm1zV2+V7Fn5fOv+9wAAq7bscvekj5uf/iDtJpSVVAwFEV1ERHOI6AARDQ/Zty4RTSeiZ8rVvrSp7ZXdsuzqmLVyc8m2enUrYMU9JvdPWZZ2ExwpktaMYjaACwC8prHvlQDmJtucbPH3N6vTlaFLo/p18dXje6bdDCl/kkQSzV1d/aGSNz01J+0mOFIkFUPBzHOZ+cOw/YioK4AxAO5NvlXZYe3WUvdGbeIzR3VDl1aN026GlJWbS6uYZTmvwpRde/eH71Sbqf5JZBFZX6P4PYAfAQh1kBLRZUQ0lYimrl9f2brwj0xbkXYTUqVBvazflpXD6i1m5TnnrKrOdRdbLFq/Pe0mlJXEnkgimkhEsyX/xml+fiyAdcw8TWd/Zr6HmYcz8/B27drFantWWbqxdtycdYkqItEua0xetLFk26sfVvagyZENEpMZZ+ZRMQ9xHIBziWg0gEYAWhDRf5j50vitq0z21pLIkzpE2Lc/uwvaWWXm8s0l20yv4ktz15Zs27ZrL5o3qm94xOrlzMM64Pk5uetVrdcos3N8Zr6Wmbsycw2AiwG8XJuNBFDdevciRMBO5yO3guk988A7pVFOGz+pvrUYG/zwzAEHX2/eUZ0Ri2mFx55PRCsAjAQwnoiez2/vTEROSD+Ad5Z8nHYTygIR4eKju6XdjKrg2dmrjT4n8/z96+2l8RpTpTSsBWtqaUU9PZ6fLTRk5g7MfGZ++ypmHi3ZfxIzjy1/S7PFfybXnlj21k0apN2EErIuzCiLlnt9gVk9j02SkXG1JhbGpWnDgge/Wmf91W8KKwxVWGKWE9Hi4j+3LK5l79idbXdY0vk3stBgB9CsYfylXmbGUzNXZTbZ1hmKjKGK9qlmv/17vqpxWaxN8cIHa9JuQqos+9isgtuBA4yaa8aj5prxlltkh4/Wf4Kaa8ZLKyzqIIZzm5ZDfXz6Svzff6djyE9fMPp80jhDkTFU99nSKi616J9JZc9MABM/WHfwde92TdGjTZODf3+y20mNB7FRSEjctit7I+bTfvMqAOCUX0+KfSzTOf/3H5p58PVyQ4OcJM5QZAxZTQYbvDxvLWquGZ/Zqa3fMGRwQlHEqQPao2vrQvb4fhfOG8gfXlpw8PUT07NbdW/7nvgzdtMZhcgzs8wCEJLEGYqMMeF9+zfJWx9twFfumwoAmZ3a+l1NWXQ9iVFnXzuhF747ql/hzew1NzP8e3IhWurvby5J9Lt27d2PeWuSXXRXZbvf+3r8daJfPpe9GizOUGQMSqDHueSvU4r+PnAg/qjnwAG2Kj1dp8I62rp1CHVEY+YmFFos3pCsusCAHz+Hs37/Ohau+ySx71Alg85fG10g0sbzmDTOUGQM/9T1D58dZv07Hn0vnpbU3v0H0Ou6Cehz/bPYaWG6DgBvLjQL40yLlo3r45CmhRBeriWWYmsG1xhkjPrtq6l8r4nrafLiUumVrOEMRca4760lRX8P69Yq1vH2S0YrP3xkVqxjihXPBt74nJWw3bsmlcp3Z5n6deugZ9umB/+uRgVZGVmWVpkhkTAJw1Q0MQiT2cGj07K7buPhDEXG6dSyEc4e1NH480kkSa3bVpzY1fPa+Mn0dSvN9+TjLkmdikpFZfhfnb8u8L2ox7LNYwYzZRNZEvGUjuzRuug9Ey9S3Bl+OXCGIuPUq1snVrbn2D++Ya8xCVI3g4vXIrKZmUg1uZ4+Ukhovz4/mouwnDmifomR3fvC3aL+9m38JLwWzD2vFwYFTRrULXrPRtRTFnGGogLo0jo7RXyCHqRpSzfFOq5qRvHhmvQryIUp99bRNHS79+1HzTXj8QMhbj5plkReQA7u7OZF/C3S7DY3bQ9fT3nw3WJZnKUaOQwfrStcT79hCBtQVCrOUFQAXzuhUBY0bRmPmSs2S7d/738zYh3XS1i7dET3kveymIDkR9dzdtKvJgEor7thVsTcHJXR+yCiK1OmJlCuznTR+vDIp1fmFbvSos5rmzQolu+wNaPImsFxhiImd0xcgAcSLjwvPrj+9QEVGxTTaFntAh2ue2y2dLupvIMfmQsqC9P5fcKD20tYxPbQnVGsEWQi7n19UfyGJYB4Lqcf2iHWsR56d3nJtudml0cKRUf7yn9n6eTv1BF6ze+fnsulGTO4EwBg/tpoYblBA78nZ2RrgdsZihis2bILv5s4H9c9/n4iI32vbrTYUUb5mtfmB1c3MxV4W2Ooh6OL7EHNQvLdfUKnU79u6WOzakv06/K3N5IR8fvpuYcV/R313hQvd8vG8YrwyIz8nv3l0iwLv2/87duqoVyw/OPCs9O4fm6Nop5hMMZTM1dJt+/el60iZc5QxODY2146+HpSAiUnPZ17MV4/Clc9HOwHTzrxqdx4EiVJjVZFvaL9ks5PZZSDWG1gXHTwd+5Rr8kaoV1XntY3VluekIyM9+4rzwxxoqRKnx+/NPuNT8pnzCLi7Nk7E9NgjMfek88cshYE6AxFDEQ34m3P2k+7v3REDwBAw3qFyIooN5DKzXn78x+aNiuQ9RHcYkGYzsw8iZLL/6NVYj0yYrO+O6rQeXojSh3KVc/BP0p+NqKhuFW4lxvWj9dFzF5Zes43aHTGUbFVJthU76mOYc/+asAA488ZyytyhsISHxqk7ocxsneb0o0ZG2mIvLM4fgW+Pu2bWWiJfcRESLGNUVwO5RJkHN7jkFifr1+3cE7MQPdDmhS9vyemWyTu52W8FzPqziNqf9+0YTzXUxBLMqYU7QxFhtAZTaeZAbwlpB6wDWM5bliXkm2bd0Q75wUJGG0R8WfaE2EkO08yozCtgeBHjJLp3qaJYs9wxFDl1k0aoH3zhrGOVw7qSdaNTGgUYYYIAO2bNwIAdGzZyMr3ZxVnKBKm5prx+OLf39Ha128nBnRsXrLPrxNwGemyKkTuQJSTNkUWPdRTEmUkssq3MH/6716L3Q4V4u8UJcfllvFzS7ZNsTALA4BnZhUvit487rCAPcMRhSkb1KuDa84eUPR+FkvC2tIcM6358oWRNZE/o4pKzBrOUBiik/U56cNcjHaQH9KP37csi/bRDa9elsDUdcee5IvzyGbwE+eqZSPeKLOgoOh6+tm5g7Q/J/vpvvPf6RZaBOz1aTB1aGE+wvVnmftH2f/2ZUBngZuf+SDV7zeRoBl355sJtCQZnKEwxP9gyvjSP96NdExZQXs/ujkFYaN/E34uGRHbRiazfver9hf2Hpq6HDXXjDdy5YmlLxs30HdVJJlEZcnzAgCYvKh4luM/x627slfNb3vAIEZVg94mJoaikmqQO0NhyF7Jgpwq5FRHhuJ/79pL3JMlOsVls2Qx9pwhnWMfV4xYMYkyvGNidJfXj/IKuqf+ZlL0L6wAjukpCYQwpHe74gCD/76TbIKpCSs2FTpd8Z4sV65m1sJZbZOKoSCii4hoDhEdIKLhiv1aEdEjRDSPiOYS0chytlPFXyVZtaJkgF9ueMnG8uYtPJ5AZucin1jcDWMG4rITesU+7qwVBYkJcWT2teN7ynYvQTYyU80UxFHmZo1ZXNJc8cB7OOrnE63Wk27ZJF6iXCXz64sGH3ytG2xwXJ94hlU3M9/DRoRgOUlrRjEbwAUAwlYd7wDwHDMPADAEQPK+D01kbiIxO3eXbw3j8YDEGhGde1q3cpdsJPUz3wJn3Njz84Z1weFdW8Y6BlA8ixDDDJs1qifZW4+nFIYya0WSnpm1Guu37cbhP8lmmdpKQ8w70q3RXW5tpUvvnSLdftM5h5a1HbqkYiiYeS4zK8N3iKgFgBMB/C3/mT3MvLkMzdNCVunrx08UEolmLNtc9N5zc8KTnlTrD4PzHbI4xY6KPzIjbofZtpmdsElxLGZLruMnTwcvbv5igr3xRp92dvM+TAMG3liQvSppSeRLREU3QivuvRx1jSJopiMauahc/u9p6HnteOPPq8jyGkUvAOsB/IOIphPRvUQUGCdJRJcR0VQimrp+vX05DT/jZ61Wvi+TLghD7CSaNTQfTct49Js5r91dlxxxcFsSGkomVcaCSKJ+OFBabyFO7W/bLp5HppmpyiahRntY5xaxPu8P2dVl/wHGLc98YCVBUVVQSnzePHG/MIJyiWT6XyYM6WY+Q39uzprE1mQSMxRENJGIZkv+jdM8RD0ARwD4MzMPA7AdwDVBOzPzPcw8nJmHt2vXzsIZxOOhqdEf3L++XhCJsy0yeGQ+W3f04YVqeUkIGZo83EG1LMpVnznOLM02Nz45J5HjrjHQlYoiTyJD5c1RGecjbn4R976xGEN+mqwrbsO2wjpWvTp6XaFM58smh3WO78pNgsQMBTOPYuZBkn9Pah5iBYAVzOw58x5BznDUCr7mWyS2VSpUnEX88eWFVo4pYhKOGBT+6j2TjWLqDYUR9uhnwYUSFxOdqbidouqOfUUholkuqRNxQm1yrv06mLkdN1VgffXMup6YeQ2A5UTUP7/pNADpZtWUkRP7tS36+7rRA42P9aVja6Tbo1Sl8z+8FwhSGz8RFuB++pTJiFjepXiJX7qjPVNmBRRj8vjP5EKCWcN6wW3xR7qZUq6OMgyx74w7ULlxbPEirW4+kM6s19R1WGQoDugdQ7wK+zRyqWRMXy5/7n71qcFFf0ed8Z9xaAdjpekw0gqPPZ+IVgAYCWA8ET2f396ZiCYIu34HwP1ENAvAUAC/KHtjU8J/j7RoZO4L//zIHjFbA6z0uWdEWY3DuhSmyyZ1GYKWSrxr4FW/i4pMI0oWgvpPQfBPhlilTfXoqkIxF67T159KQmXWJKrntAHtD76+3jdQ0ZFVv+uVwozVnymua3Z0pNhXbS7s0yJCpJwY0tq1tZ4+lmjgTGdc/3xLntnul4N5fUG0YJMXPlibmBZcWlFPjzNzV2ZuyMwdmPnM/PZVzDxa2G9Gft1hMDOfx8x2JCITxobujF9FNcqD7vdH+xOmTPB35mIE1VE18dRKgwarcSvbvfJhqfRH1ApkflRBBqrm7tqrP+q97rH3ozSpiIGd5AvQJrLyXtU2ADjUt7CtY8wWCQmoJ/cvXjcMUjbwly+d8L46aAQovjcvOKJr6P4e4jMlypSoZij/FORLTGcUQZI+fpXecmWV65BZ11OlsnPPfiuLsK2aFE8ho3SaYXUhLjmmtC51GP6Hwma0j794jMeFR+o/9DJkkWl/nlS6LrM+RJxNdCn94vxgbSdbJVsXxSgqdcnR3aTbTZR9VWcTtQJbU5+BDdJm8ldQ/Pdk+eg7CM9o+N04Mv74sjyjX6WwsGJTQUPt3KFyVYKoasce3XyGwta6pA2cobDMjOWbA2/AOOyLMKPwi7r5qTGQof7ti+VXre2lMRNS+XFlYoKyTlgsbSnjNy/OP/jab8CL2qI8SpkQhtcjesWb6YmXdmi3VkXv/Va4JiYEldS931d/XkfNdaawxnTmYbmovvYtwvMivGi3o2paF21XhY2LIdtjDu8k3cdW7l7UbO8kcYbCAFXntP8A4z+T7WvhRHE9hQ1sRwfc4CrSCCHVeUymRixY45chsYmtGYUtxgyOq8Mld80kiY6ryY+oZjuwY7zcD0CtNxY2CAMsZnlnx044Q2GCqj+49dngrN840Sz+EZ2KsFrBXrGVrKMzoLJVh0AX1SjvnUXB+j33T4nmQrGS42JwDPF740iVm2Jy2uJnvI68v6SWiw3KKfXxYIbEF52hEPjMX97G7c+H174Wb5Vbziv2Wav8mzNjZC1H8Vc+NLWgHHvVGaUZpyZlG/3aVeUgqczsOBzZo3Xgex+tD14of21+tAgW1bFU9BKi0Uy6NLEfbB4j0k6GrBCXDcSZnJch3alleEEp75nyL6yrjNWTM1aF7qcz69Dh+TnqAZ9I0kWQnKEQmLL4Y2XKv4d4Y/qjQXaUeYQrQ3zYj5B0bCaF4MP8+DboXAHlJFUGO8o6Uhhrtpg9+Mf1KeTfmLgYkxwxf/Pk3okcV3Q/+hfNgeDBm5dz0NwXUqs7m2vbPGC9SvHxD1aFR4sF5T2pMK3Mp4szFAaIhuKI7sEjTD/lWpsSb/Rje7dV7JktRvQqlnrWuV5h7rx3lxTcQXHVcsPQTbj7+gnh8um3jI+fW2oidJfkOouptljcRMagWjAbP8lFJ117dnGOyHjNdZKgWYuquUE5QT8XoulaNM6eRLwzFAbs2mOYCarpSlFl/wLhkhIbPklWIuD0QzuUbBNF1Yzjvw36kWsenaV8X6w3kbQUh24C1nCNvJNtKVWRS3JGYTpOiislEmT8vBK6/hnFJIW8SJzvA4JzNDrFnE0nPQh1hsKAv7+5OHwnCbq+y7CwOJ163bqY+MK7ti4dSTURymXOXrml5H0dTNYktoe4+l6dXwiRTbrzVY18xeJKx/cJn+WlVSZT1cmdKmRqm3Bsb7PiQHE77rCZpP9xi2ssVZ+/9Vn5GuhJ/eJd26RxhsKAqMlGHr9+QS/2PGwJweaYzyQS65snlfqaRd99lNGNaKj8523DCyKGKt/5SnB+Sxypce/cddco6hApF8WTQqcDVGWQX3J09ERNkTaGNR/eWxZPkCEsJNp/n71vONDxUF3nBQFSLuLzc5FBomkSStAizlAYYBrVoBv1NLhrK/X3W7wnWhr4Q2XRMCf0FSUa9C2FaKj8C5ENQlxwUREzwMf5smrjhC57HcOfJoUHQgBA4wZ1ce3ZA4y/z5TpGh3u394Ini239gnOTVuqV87zZl9lxSDEQcNJ/Qr30+4I8icy7nhJnQCrWy41DK/N975RWibZQ2fWrJMs6OcvrwZ/pw2coTDB11GfppiSN20QPVHpylF9I31/HGzlIYjaVFt26q+R1BWmH9/yRcXYljB48YNCuOF3RxWHDZc7Vc5GCdkk2K4QYPTPgjZqroU11EzWE79bLNtr6urVxSRcXIY32FBFIO3UWL+ra7DgMHlRshUOnaEwwB8C27t9sNSEXxEyCFFdNKyDtBWnDQTXglDROMT4Xf/4bOX7IuJCpW6HYgP/4mGcWdqXj6uJ/Bmdkpe67oR5a/TUZoOE+ESihPjaXvcW1xL8AnlBiG6eDgYjcQDo0SawcGYkPIMTdY3j8yOK1Z2zpPHk4QyFAX6hMlXJyBvH6k27Zy4v+EXDbhMbridP3yaJRJ0ouSS/eaGgIZVU5Iasw7UpSTGyl9kirT9Z00+QHpIf1SxA5JfPhSeT6tZlAPTl0Js2kCvu+sUrbxMWenVDaUXj4g+vjkoU9QMZXn5S1BDjm333gUkYcRJljUWcobDAWYM6Br6nW51NvLnCfnPdSCVRJtqPN2qZrJCd8NAtUO+hM732WLKhME1P6lYP0oMS3YKmip+A+QjwUt9I0o9+f6P3/Tr1zKMMhlW+/wWCWu3ZAc/HAp+irVhXQpei5ybyp4uJO5L3XEYRbC2W3DYm1nd66A4WTHGGImF0p7XiDR/2mf+9u1z5vocq0zmKMmXUxcQo+Qq2p9lnHVbaKf31NflCnxg08LuJ5mqocVQ+l9w2BktuG4NHv3lsyXtzNLJ4bWMr4a4omi3gN/YbJZPIHfEYR8asi3L1WeoAg7DEP68Qo+41fPCyEVr76WBTFUCGMxQx8KJyVKU62zVviHOGhKt4ij90WEatbr+k6sC+c2rIgnmZWPZxYUbRJMBFEQVZydgXPlgrHXE10Qg00KpMZ8HWycJlH9AWEgzuJL5xUq/A92Q8M1OdlSzLoZETflH8a20m1RHfE2aLQbLfurRorL7/9oZMFerm+wHdTjuuq6ycOEMhYZmmbsrvPj0UQPioWEfDSEemoG2zXHhivbrBP5tYNGmUJIPao0sr3Qe+fNiYXXQPqLVx3eOFqnG92+VmbD8KGUECwFsfhUeTJOUy26wZsqsawDZXVOST4YWKBt2zYga+Cp3BzMNTV2i3K4jn56wpfKfvvR9ottUjLNpIDG1tIHkG6+bfzprcvA2coZCwaoteVmxri1XedCIlvJGKKpzvYyFkcbAiBFMxCSohC/e9jltCZfxE1c+fnJsLMNCZUaQZfzJ92Wat/aJWgdMhaHFUt3a7znV7auYq5fuqsrMeqqzrHm3tRDN5iDMgWeThYZ1zz5tuxFYl4QyFBN2OUXfRVkfk604N1VqvXbqdlyq5Ryc80+PPrxbKh8rWAMqBzkLslafpudM6SuosBBpqocMMCg4YEpIgKaIy3u2bm4V3viyp5Odxii/HJ27ezGkD9aQm4pRzPTGfuKbj5hJDfuv7EjRVE9S4ul+yPuIzR+XK0J7Yr13pmz76d1BLrg9PIXNfhTMUEnQX1XTVSHVkg3XCVL12qULhdAf/7YROKex8dSXGPZdOEmzfHd7B1a+Xuy53XXKEcr+a/EizXt3CddTR/j9/aBfpdn/Gsop2ivUnlRFRofr1vFGuR9xwaN0wzNsCNI0+qyED0iQfunzDmEND9318+sqDr3VmIB4muUjiYyKTTPdcp3dMDC+FfHRP9cK7d0+Vs1CSCmcoJOj+NP01yy6KHZINgqSK/ehKYITdi2LfoOon4orG6bYhiHPypT/PPCx4bQaIVtxmaYyRsYeopqu61FdIAgx0Bi1ROpPXFugJ7CWlHdSzbbhb5gvH5sKGxdBy2+2RHa5ZI7WhefS9wprKcRJhR89QBAk6iuHAAzqpZxSeioBurkrSOEMhYZNmTH3PEB+op6Nkq0i6t0bxyLTgRcBZQqF5XT4JUVUVR5FfPi64lkLdKAsfEdG5gt4iv2qxPyr3CtpHpl3VaiGaR9XhyTKLdfrHKKPjB9/RC60eYaj0aop4Xfq0K1U6mPD+mpJtYZzSP3jgIltwDhs4hBUHCnvMRRWCC4bpCf+Vq4ZNGKkYCiK6iIjmENEBIhqu2O97+f1mE9F/iagsJdCufez98J18+EXmAODWCw4HYG9BVMfV9c+3lkQ+7t8UImYAsHhDISa+RjEi7CtImXy8PdzYRk3kSxvT31H8nCqyS+aW0pFG9xRfRw1Uz6QAfWXUrygGBHEIWjdbInTC3oBIHIitN7hXZNXuPEw8OmLLZQY8bEAoRlXpGgBV6L2MFiGzIlO0WkFE/Yjor0T0AhG97P2L8b2zAVwA4DXFd3YB8H8AhjPzIAB1AVwc4zu1MalbILspvagaWzOKy04Mj4k3GfWGLcrrrlGIi706RmBrFMVWySVcsSnZ8o9+bEyYrlGoxspmQn99XV8VtNsh2Qt59vPp/IKvH/Hn9VxAoix53IQy/yDLKJNZaKRsFhf2lIuJh2ESMl7yn07XIdanMSl/q4Purf8wgPcA3ADgh8I/I5h5LjN/GL4n6gFoTET1ADQBoI6nS5ErTulTsm1Yt1zkgniD6OZoyDixb3g0hcnzFEVyQ4UYtqtjHKO4qmRV//xaQSLXjbYv4z1Ac03Kj3gpWjbWX/gGiv3iYdhSQU2SxgEdpJh4KQvBjZub8PK84siwewKy9VWIs6HDOkUPPIhyCjX5fCCxQmMQYk3woCz4uOg+qfuY+c/M/A4zT/P+JdKiPMy8EsCvASwDsBrAFmZ+IWh/IrqMiKYS0dT16+NVxDJBNkJoKcmz2LPfvFPWMgIGD5RY3CcMVdROUfEijWO9ICRLyUJWRRrXL52xqc40aGH9x2PDI2mC6GwhSTHqouzqCNnKNjsJVTPjJGsGjR/++LI6UsikY1fhjcIPiRCx9snuQqcte7bDIsKCpGRkvLYgV6b1Z8/MCd03LBHQBrpHfZqIvkVEnYjoEO+f6gNENDG/tuD/N07nC4moNYBxAHoC6AygKRFdGrQ/M9/DzMOZeXi7duEjb1OCHvRWmgWA4sygdRYtV2xKtoSm6mEQ35sbUNBeRKwPMTAkCiSq26dPe/nxkgzhDUJ0m8St/6wiaBYXJWzUQ3WvfeuUQmioadlbP2G++Lh14P1XJmpOEhBtQCVjyUb9CDrPkG3aHq2g1oCO6ufIFN3H74vIuZreAjAt/2+q6gPMPIqZB0n+Pan5naMALGbm9cy8F8BjAEqV08pM0HOuO5qLM4XW+ehGjUXkcvBnjWpvYthw2GjMpJ62jGN6ll9f54+CympYKKtKsj6M+gH34IW+0po6/nnd21Q3VNsjyD0Wd/0nLC/BT5hndJVBzfIwgxzlyY9yvz/4bsGAqZSs46D18zBzT8m/aGpj0VkGYAQRNaFcL3IagLkJf2coSY4Iw7D91UnqPenYzfeWbtY+3ger7Yxcw4ouJYEonx0mQX1UDAXULwYkdvqFAbfvCe/c2yqyxFs3Kbhrog58/AMCr+jSmwvjVWgLu93u8g1cvI44qP26ybQiDerVQZdWjfGpIwJCXyNcqrH5wJBTBoR7R95cuOHg66TqUigNBRGdmv//Atk/0y8lovOJaAWAkQDGE9Hz+e2diWgCADDzFACPILeI/n6+rfeYfqct5q/VUBNVoBM2GkSUh1JHasN2IqCIzmK2WKs4LKLrusdKq+aFXY7vhpWUBTCoi/kIXhvhUoTVQ/7cMaWZy0EJXH6CwkH9bh0d+QrVIEKsLxH2G4RlYseRFBHdwGH3m79efZjgomlG9MrNOzFlsdzo7dqnf65D8kWU+ga4UEXE2UdSeRdhM4qT8v+fI/k31vRLmflxZu7KzA2ZuQMzn5nfvoqZRwv73cTMA/Iuq88zs/1ybBF5Y8GG8J0AfCOg47t1grrKmCx6yqNXBP+6jhJrUASKDXTj9T26hQipyU5HXBwc1r1VyftfPT6ZXICoiG0PC4tsJxnJf/M/enEjQZ1Ec19s/V2vLJTvqIk4an1oqjqBL6w86e4YmktiX65SSpbxdF6QMMgcxHERB60TzlqReyZ0Kul5z+9NT4UvZm8RjF4qi9nMfFP+/y9L/n0lkRZlHFWOhZhw9r0AieOweHBZXQKPrq31VSl1RhZxIoDKhSd3LRsxThZGbrJaBH6fsezaiqOxpHR1ovibWzUpjcLxOpgwgmSy/cZpS5T8lRBEVV4TfuUrzxrFHSr+XqdrJBvKuC2fFOtHp764Ka00VKejhDqLJXNtlvgV0TY/RDSGiH5ERDd6/xJpUcaRjfg8/vqFQpJ50A8WGh5paeqoE/0ghgYmpe2jS9BzcYbnQgu5LjJD4vfX3jCmtKiROHI08Uv72SRxLZZLhkE3sfPZ2dHlMJJisU9LS6cT9RBdOabXOEi2w8a9EISOEbBd+TEuupnZdwP4DIDvIPfIXgRAXfC3SlH59WvaNsUbV5+CBT8/O3CfMtkJXHJM+M8jdixB7dodwa8ah/bN1XkUYZ1g0NvfG1WY2Q3rXjqj0JG9iMI7S0prkJfNUGh2LkG/dRKDhbBiQP6Re5RZ3b8M5Gp02RWx/G8UZPehn6RcSKbotuZYZv4CgE3M/FPkFqHlufgVjM4CcNjiW9fWTQ6qk8rYF6Xyegx0ugyxXwl6PEV57yEaMtinaSrI+g1Q0AjKW/yXuUvEfi2oVsSVo/rilatOxvQfny59X6dMbRRkne37mq4jFUH33WrNIls6JOF6GxRyz/jDa/0lem8NcA0BwHbhmqh0nVQEnXEU6ZSoXHRkuCBgnTqEDi0aFgUOpImuofCcYDuIqDOAvcglwlUV/TqUqlb6uWV8LkL3lvMGRTq25wr6aL066aa3RDkzKXoJ37X8Y7m0SFH3rTE01pU2j9opyeqIi52yakbSs21TrZoRNgbUMo/F1ojaYTKbKZb8FNGReADCM9+BeMmgQYzUqAu9RTiH3u2LAzZU7RbvoSgZ1iJBi9ZiMqhtdENYmzaoV1TaOE2iZGa3AnA7cuGqSwD8N6E2pUcEH0HUjq5vSEUrj7DoH5uIo3ixAIxIUS2KiMdUoRs37x1PVrbUdr9mUszGj408G1nQwnf/NyPWMYd0C58N2qr1vE+wljKX4diA2V9UZmiWilWRhTK/QSzasD12foktQg0FEdUB8BIzb2bmR5FbmxjAzLVyMdsj6lTXtps6zJ8cVfcn6GhixI7OqDQo6cvPCwEjZD9e5yWz4SYqvypsuF72W3At/mzcYdr76o5t/FF4svvHlvzLlMWFdRrZwMFfGlg00KqQbf/oWrYeFBXb7jadkHOb69QbY1Ys1CXUUDDzAQC/Ef7ezcx20mRrEbaDGMJGQi01tac8FgQkEr69qJA38t3TwxPYOrXUKxnysKL4koywojGmiJnaT/hmVfsMIl9shFVG+e10R8T+dTNZmPb4Wau1v1eF2CbZfX/A993j3y98b482xa4ncYb9oka52qh4Kq2628M4a1BHdA/xCjSXqOOasitm7W9ddF1PLxDRpyip/PCMIBb9CNN6iSq0prp0uwxkvmVugs2alflkBIVMviA8nFEjMWxE0SRdMliM2/crtZqEkdoYoQ7sJM8Wlx37Xc1RddfWxWGgsp8mitusv8KVWlw6t/S+v3REcUSeSsqlj5CbZHJlZbWtRdoHzJJVCgo/CMiRAnK/UVgtFt11PDEvK4hZvozzpNB98r+PXE2K3US0lYi2EVE2irla5GJBbiDoRvEWVcPqMvtRWVi/Vr4Osv4okYSxkIfej9jXrNKUyFbFzpczv8PfUZrE0qvK1OoSlIMjy4K+780lWsdsWK/4mLJF0ihus3OGBK8zhN0lNb4Swro1N0zuBZUsvgp/AIL43YcpZF+emrkKu/YesPIsDu7aKnSfB9/VK20bF11RwObMXIeZGzBzi/zfZRDJKS9iIkzQD70h7xOMOrlS1ZrW0d7xY2vh0TYdBddT0BXyP/DtFUmMqgRH2/hdIlEY0Ssn5jdt6SZbzSnBpERvELL6DlHsovL+D3k0TO/dZQGReSqiJq4FzZTE7Ged5vvD4E2MnGdAVTOUV+cXau9492AS6CbcvaSzzRGMqkylyYOThp3Qqbkh+sKD+pI9vh5JlUwX5jqwib+jFJvl10vyc9oAu4l7SSMbCEW5D/so3CJhkiWm9+4fX46uURU1qOOagMqIL80tzPp12u+fnOmGMcvYnWDyny7Ku5+IGiFXgrRtvpCQd9VbIFdMqKoQOwajmrqqYyseHpNp6rbde8simT1vdWGRWycXQSTonP0FYK44NVgIsb6NQtWaLFz/SeB7N4boYul0SIM1EhajYjpekEXLRJlRqTLan5whD7X2iBpoEQcxM3z77n2h0YpB91vU1Vmb5Qh0vzvJ9bywp/AbyBUpGoDigkVPArgzuWalg9ix/fTpD2wfPBCTe+rJ6aVibCYRN43qq2+BD1abL0X96+0l0u13v1pcG0AlpVzO8InX5heX0BUX8lXZ9gCgo9iuq8Wkwu+G8GslqegsuAWfkIj5vZBPMgu7JwB1FF+5/OYeKiFB8VxmaCz8Bv1E4jN6hEK408PGGoU3ONkX8Fz7o/JMovR0CVOPvYOZewL4OYCh+df/ALAIwNuJtSolxJvfekak4r4xcT353TcA8JfXwqvK+bHReQURVPpx/bbi0WySdTHiIEY9hSXj6fjCo/zOQTL1C9cFz3rCOKSZekborQHo6ByJaxRbfG6VcsdGqiadMokW1XpB0FsvzS0MGnSywOOsd3l463M7JVGR/3hzMQ696fmibVed0T/2dwahO6+/kJm3EtHxAE4HcB+APyfWqpSoJ4wak5KclmFLLsCkfGOShkJXXrtX2+A6G7ZKoMYlrI+vq+Eii1R4KkDj5xcTzIs83jAmGVl5/4AgTAgwCFPFVNX3yWaCqp8haEDwyofrpduD8LueTHoTr3LdHRMXFG1/aOpy/PTpD0qCYDpq5jCZoGsoPJM2BsDd+brXZuIqtRRSXOmXDMJjZZjMPL92QnKSXbp1D1QRNDZkNWwQ1onpSEdHSdoOUhidvVLuCtQRN4ya+6OL3wCaDj4GdTFbw/m+5kjaa6Zq/SDuwMkrO+u/JlsNaoBsyudFfeRbO/vRI7Ok+6e5RuGxkoj+AuDTACYQUcMIn61I1m2zmxrfQsjG3KFRszgM2fTZJATv+D5tD7627eN8Y2FpNcCoRXOyEgXcpIG6k7XteoqKjvcuqUVk/1nJ3KI6/NDQddJHU0jTq+z3lKLY0ggNEUMVPQ7JzY79g4I/vLRAsreaVo1zY3ExaEX1jOusLZmie+RPA3gewFnMvBnAIQB+mFSjqh2/tLIJsvvF23R4hJGZOJq3kSwWxuOayVUeGbETGDVQLZ9+uEZEk84iqCk6UVe6gpPNI848bPjjAf2MZQBYIizi604C3l6UE9hTuWjjFgzyPF3+WctuA+P51fxsX6yjPml+sAssSgXMqOgm3O1g5seYeUH+79XM/EJircooyxLSGzJhpeRmVwnoBSG6I2SLZrb5ScRoMp1ZUjlqY4clWPYMWGcRZVW+rCmY6BEkFSGrTWFzrelXFw6OtP/f31wc+TtkhldXJwwAXl9Q6DCzKCxUkkSbv42j1L1vmDecVz9aSLQsx2BORlW7j2yzcbsld5SFAZgsBHFSfsEtStZ4f6FkapRQSxUySXBTdAarWegnghZUw2qkq/jGSfJkQ1mGsk3RybYRs+Hf+ii6FLbsukSR2Bc/3qZptPYmOUt9YEouR+g+n/H01tqiGHTZvraEG6PiDEUErBVcT7hnMz38v95eGvieSmbDj44cuUdYxnPQYvbSjdFdD0GYFr0RCWqDuDmqzQhyxcjCji8PMComRL2c+w2eiyEaOkYeJ/dvV7JNFNKMKvOSZETjtrxbeaNPK85bs4hi0KNmlSdJKoaCiG4nonlENIuIHs8XRZLtdxYRfUhEC4nomjI3s4QkE1oAvYddR8HV1qKlqe95dwTtqnNDonWCRosbPik8iFl4oIJmceJ2kwguWTTT716cD6B4ratVE3tBiFF1zIJ2H9AxOJHyQo1yoB6fOqKw78J1OaWAW5+dp/15P3cYLCzr4s0s/cbI034KS9ws+kzC/U0U0ppRvAhgEDMPBjAfwLX+HYioLoC7AJwN4FAAnyWiZALBNXksX6/g4qPilQsPyrQc2Cm8Ct6vPz0kdJ8fnWUn8UZ0D0SZMkdZ6wjrMIIWF8XmmMbtl4OiGYXBc//LT5XWjJ63JtdZbhJGrSaLsEEja91DjRuaM2L1Ajo/lWRJC8OaDItCSgmnjfc7+K/tjOW5Ej5B10pGWF2LcpKKoWDmF5jZGw5NBiDrLY4GsJCZFzHzHgAPAhhXrjbKmJAvsGJayN3DL2HhodMZN2sY7v8PC+U0IcosRazQJs5KZAvTKvkFFeKV+qwgD29CkmGr4k9qMqPQ/S118jj8PDJNLrWhOyjwRCKDJPlVl7WlQlreT/E1zDaeofDfU57q9FVnBNey8JOl8j9ZWKP4CoBnJdu7ABDv5BX5bVKI6DIimkpEU9evj5ZFqYvnUmkYIYxPhr9AjofOfVHOTGXxZr/xHP3JXI1QpUyMqZctegYVjolCXClyW+GdMsTfq7Whe+hrAVFd4oxPd0Yh3mN+P7psHxVhLj9bV1VcQ/qHQYRVORmZz8PoHZDb0S1GCKtf+kYkyhqiCYkZCiKaSESzJf/GCftcD2AfgPtlh5BsC7z3mPkeZh7OzMPbtStd/DLBr2HjTSfjziiCQj61jEBKg4woWb1iwR/R2Eyca7+UJRA/NPSbJwer18Zl885CZ9zZcPZ07eiB0u1eAhkQvfqgigEd9UrNhLlGovwq/3dacJndY3sXkkInL4pfJ1sXLwR38iL9qK5P593SQXk1ce7V2auCK1B/eng8d3gYiRkKZh7FzIMk/54EACL6IoCxAD7H8p5zBQDx7LsCCE6pTIANAeGwUavb+QnyDevNKMKxVRVOjK6JcoOLMeRzBfXZf2hWYwtCzGgXp+Vx17KPSbDgy+8nxl84lc0WmBlrhWI6ugv6Xz+hIDYYdJvoJr6NOTy4yl1UTurXNnwny4Td0t7MX7zOZwdocHnUCVjMjsvWXXvxb0VU4umHJlsPJa2op7MAXA3gXGYOymJ7F0BfIupJRA0AXAzgqaTbdooQihfU4XZpFW+RKegWOqFv+MOi47e0FfX0yNRCck+UgZDoV3/2/eh1p4OYs6pgdLz1IiC+L1f8mW2XXk2qlOuarbuMlGTFUNOlAeq+usiu++59hUAGf8lTPw9fPvLg6yN7JGesReavLdRX+c1F6sAQ2W8XJNboEbRGEZe9+w4oSyYH1Vm3RVprFHcCaA7gRSKaQUR3AwARdSaiCQCQX+y+AjnpkLkAHmLmOUk3TCzOEyS3HDfNP2iw0VwjEqS+xne3MawT7Ec8T1VFMz/itFslwPbz8wcZt+dRIUPVZnRsGUWDYzFv9bbAtS5dHpoaL8tXZp9FY35JSJDBUTWHYNzQzvjHl46K1Y4oiFntYWtGJveCF4G38ZOABX7DlZuwGUoU+RMT0op66sPM3Zh5aP7f5fntq5h5tLDfBGbux8y9mfnn5W7nL5+Tx2qbRJiI+AvkRCGuaFkYy8WsX+E0G9U3y7ZWuZvOPEw9OvMjur/ETir+jKLwEHp1ipOaCZjyhZE9iv5+OCBiKQybUh+yY1HI+37uuHgYThmg1tHyYyKn7yG6U8M6bU/+f+bywtpA2G3hnfIt4+Vy8KYdepK5HzpkIeops2zaIR8VmCZ4De3WKkZr4n23iq6tC4usbwsLd3MCJK1t0TbizEc8c5uhg+KzvyY/Sn/bQJYiSY7pWTxAmGDo0juqxp6Lp3HY4CGhwAuxfkuHFtHuoZufKWiNheW1eK4eEy2rIDq1NAtouH9KcflgMRHziW8fF6tNOjhDoUAmvhaH+glWcoszAhbrQYstlMmEp0nRLMLicRvVE2Wcc/9vj/HblwjCWUAmY2FCkNvU5P6R1WyngFmfTW56quCB/tm4cPflRUJSp5jRb7KOcFqIinC5+MPFQ7HktjFYctsYKwPQMJyh8PGFkTUHX39kOQs0yQSaKLIZfhoKI8N7XltkozklzPGF9vXvEJ6F7kd0f9m8lDoS4VGYurQQwhl3HcEjaR+0rSqL82LUWDdBRxI9bFE90vcZZpSbEqghVuZkPGcofNS0kUc0LZcodkYlA5JEUsR2LYhRk1nFGl+HaVJZT8wVSDrx0NbRpyy2E/cfRSPIhA0Bi6+6eDXmf5PXoSoXOoElQX3qiN7JrvfZ4PxhgTnGZcUZCh9Bs9Gg9YooyDo3/0jblDjheIcmHFoHAD97prgORdy47zVb7YzU/WzLd3imVdoqFVV0mg6e7pSou2UzCTCIXhrV7YK0wIL0pi44wrxz9tb7bLkKZYl0R3RvZeXYUXCGwkfQ42IzWkRk847otXRlxEnwsRVOq2Kpr+iTidqpLTeOinvfyC1c3vjkbONjlFNmBQD6RghdDiKujIl3zuIA3zRSLgo68i1Rw9l18pmCICK0alLfmqCfbAD4+88Ms3LsKDhDoYmNKJjzJSOVODMB8eHOcvy/Lbnkqx+VF5VPAtEV842Tein2TB8bhaLiZhJ746itu+KX+bXNxRFFI+vVidct1iUqup5xAk1kdTu6B7jHk8QZCh9+wT/vR/7X5CWxjz2iZ6lPNM7zKRoZMSM2a8iq8ZlgmqwUl84RQxrL3c64biMAeDVGbg9QCNu2UQ/eNlF0yoD40Yl16lDRsxnHjRlXV84WzlD48P8wnmKjFzNuKosNyBfV4kz5xZyH+2LqKCWJDb0jIDn3n3USshOyOtOAWZ0LP3ENxXOz7Um1yLgpgnpxXOLeZ+u37cb0ZZvtNCYjOEMRgjdam782Fw00qIvdhd+9MUYbYh2ALTvtrHXIOCtiBrUfT4s/LpViKLzCQrY5uqc8WS4LrrGXElIG9ghN7rNIr3aFcNrVW8yywMV7IGNJ/kY4QxHCMt8irO0f/bUF5iO5/UVrFLnXcWszAMBbvkS7Lx5bE/kYR/ZoHbsdfhZvyHZ1Mw9/hJctxg2VR+P0M8hJ8bAR9g3Ey+PJGn3aF67npA/j17ax2Wd848R0BgXOUITgT0CzHTb5n8nLwncKQDQU3msbZUGnL99c9LfJIS9T3NDfHRVceyCL2JBNadssfk3roFZEXYj+7NGFkMv3lm2K0aICC9YmM4vyGCxZ1C0HNoJY4irJinXlv3VKcrVTVDhDEYK//vPgLuZZvK2E8o825EH2SaKebCT13f78h5gudCC2XT4dI1a1O75PLlxRJlVQDpdEL83MXq9OSVNJFJKNUWWLAPn4qMc+dUAhhyVuJ+ZlRkepBW3CoZ1LXb5HW9StCuKpmfFL4MS9xrdeUKibbquEQFScoQjBX74zaqidiO30/12CEVuxKedCsCUaKBaxH27gRlI9GxceKSuRHoxnp2T2ylZik4rj+ujF1ffIl4CVDfBt1CcIykvodoh5gMWrMV0r3fL5AkF1s5Mk6WI9fkzdPttihgw3bVjvoK5TWjhDERFbg2t/CKVfRlqHh4V6Al6JSNN4eH/VvpfmFRYnTYzPwE7BfnPT0ecMn0ssa3j3hixcNck8l6jJi+Kv+cSM4hHz4Ii6V+L9Vu7Q2HKHIevmL4zodUiRFFBS+mnlxBkKDcSR+779dm5Of4duIj/8gUSA7WYNNU0ZZxxaHNlkKmPt4Y2ubSIblGcposRbH5IZa9sVz+IwQGHEv3Vy70jHEtfsVseoE2HC2YPslWK1SesmDYpEHL37oXWTdNxGNnCGQoOVwgNgS5zN35fYkiBvH1Gf38N2jd/aiCcVIbuWWQrt7dpaNTKO1k4xma3cp9jNkkyGLv7BVBB161DR+qFHuRVfbeIMhQS/T37d1kIeQMeW0RZigxg/a3XR30mrg4bRt0N8vaBqwTS3xd8RiNnyv/zU4f7djRhiWRI9Lj8WapmUQ4srTXRDz6ct3VS0xpeWooBNnKGQ0LB+8WX57F8nW/+OhT4573oJFjXSYVh3+3kPtlB5bZIYpL1jKA2uWsppHzHSKwibFepsIM4oxNLBp0Usb1puvm4gc69LkMGs3PmEMxRSyuFO9o9axw7uHLCnwz8iE5PEfnBGf+vf90q+BGZUVO4lW/fUZ48xj7rToVVEP7r42+zaW7ins+Zl+dQRxZF2fSwo7obh6cRt352bWSZRxrhcOEMh4fAYuRK6+A1Fi0b64l/Xjx4Y+F5rA/nuciIme+niDyDYvqcQXRO1Y9PhoalmIob+OgbFxsGOpehgaWYSxIhe5sV8/LNk23xvVD/jz3byuYzLUW7EW6t6fPpKAPF04tLGGQoJnzsmeqhqVDb64s6jLHSp1knKvcAXlXOHRC8K49f2F+s92Bqp//z8QrSYqVS2yodtq51+JdQ2TeMPDOJocQWdVxKz8q8cX3PwddQ1nzN9emUdWyZfg8UfJn3N2QMS/86kSMVQENHtRDSPiGYR0eNE1EqyTzcieoWI5hLRHCK6slztK8fiU5waxVmb1kdhRK/oPvYrTi2WLRDP39ZvFVVKXIbf9SRm3yd1R/36oiGxjzF5kblMRe+ACnOfOSr6zDEMMWFVVvlNxWG+zG4xO13GZ2Mk1no5Sf7ot7QDVuKQVstfBDCImQcDmA/gWsk++wD8gJkHAhgB4NtEVD6t4QxTzgpq3z/dfLp/w5hSF5lJiKC/Ay76K0MBJX6drb+UIdHqcAtRUP565lFoHFA0yUa7ZHgZylHvo6i3nYkagYcXcLDX5zKNU8AobVIxFMz8AjN78/vJAEo0HZh5NTO/l3+9DcBcAGWpNF7JvkTb9IhRTeuwzsl0FsUziuzg74z2CIqqNkeTD1424uDrthbK2M5eaaduu0jW+sSohqV/R3NFXu+39s8oKjmPIgvlk74C4H+qHYioBsAwAFPK0aAkBc56tm16UC57i2G97HLeb3E6uJG9zRdGVXhRJEC2OiR/RyD+aTP/YUSvNrjlvEE4qZ8dnSu/jIcDGOQLaIkSJeUFN/lLANdzUU+lENFEIpot+TdO2Od65FxM9yuO0wzAowC+y8ylmhWF/S4joqlENHX9+vga8jLEgiamiLfK0o/N6isM7FTsb7U1pR03tDRE178IGAfTkET/6d367NyDr9tYkO8GkEiQu3hI26PJS0f0iBW4kES0WDUTpSbLf9/JRc09MWNl0fa6zlCUwsyjmHmQ5N+TAEBEXwQwFsDnOKCnI6L6yBmJ+5n5sZDvu4eZhzPz8HbtElIUtdEfW7hXevpkr/2+UFNk+kw2b+4Hvn6M0ef8C9aiGqctl043payFGVn2NKhCrG2QRUPUtbW5S7ldhAGJVxVvxaZi7asBMdxZaZNW1NNZAK4GcC4zS0tsUW4I9jcAc5n5t+VsXxC2s6dtySvNXmXHx/zV45LLVgWAtk3N/On+YUQSHbDtBKx9+w/ghRiRbUmTtBJAkwZZ8GoXM+mqk3HFKX0w92dnRf5slJl13Tq5btU/gEu6ZkeSpNXyOwE0B/AiEc0gorsBgIg6E9GE/D7HAfg8gFPz+8wgotEptRcAcOPYw2If4whBKuNpC0VRAODNBRvCd9KgeYSkP10++sVonNivHSZddbJxZqrfnmZJYC+IOau2YulGO2VGk6CckXNZoV7dOrjqzP6BkVoqorgOe+dd1FmcVZmSVtRTH2buxsxD8/8uz29fxcyj86/fYGZi5sHCfhPUR06WQywkN331+MKo/YnpKxV76rFi0w5jETs/SfS/desQ/vWVo1GjWSVOhpi1vmXH3oqIHsl6E0eVuehPJTLthlFGn7vqzJyszFE12dVPi0r25ocZoaZNEyzxjQjrWDCrYgcikyKOytKNO7DH0hpFVjvgNkII6MrNO7Fhm3kmcVQuHZGstlJa+DO8HaW0adbQqKpck/yMZc++DIXkxaRynWYJc2SP0gzifu3tLkZt2WkWHivCDGzMSzDIajVXG3XrUFF9kKRp1yxZbaVqoGE9142IeNfD1kw/C7hfOABRV8bDhvqjzDd87hBz5VgG4+FpuZKo2wXJCFOaCyPNazOoTVMpEYbvLd2UdhPKRvWMm+3gReLNzHjp3ig4QxFAUiqsMuG4pjHcAHHkF2T8+JyCSsp5w8qSCB+Jcks1mwaqlEO+wzamonW9Yqw/VSO78xn5976xuKJlO0ScoQigc0IyHrIF8ThRcz98ZNbB12MOj19D+EJBtz9pSWsT6ttYKIpAXcPvq5CJTxENDG/E6yWaXrUZ8TpWiZ1wi9lZYHCXVlaO8/mR8eXR69QhowW8clG3zJUATxlglryZ1cAAFf7Kjrr4DUy/Wl5WV1QLOFAllsLNKDLAyYadkZ/K65qi87fXF5f1+/oaBjCUc8HdFsf2bmv0OX9XWK/Ms76sIcqhz1uzLcWW2KN2/6IRaJJgRFGLRnYScypxFBuVactqzyJxuelhqB3lr0lxqK/2Q22lV7umxmV1s4YzFApEkbxLRyRX9c6WXlFtiI0XPU+N6ycfDlwpUVY2MB1n+AM0Ljuxl4XWVDY1bZpgUEIy+2ngDIWCK04pVFa7/KTeiX2PLeG92jCSE/Vz/FXLkqA2zNI8bJ2r6aJ4NbFk4w48ZUmiJwu4X1RB3w7NMWpge/zi/MOtyHc44rNuWyEcuDqWCdNDVoHQBnHkWqqND9e6NYpawb1fPAqXHFOdMg6VyNqtBfkO2zHqg7rEn6GMGRw/RLlcNCqD666288ys1Wk3wQrOUKSADVfTj8e68uG2ZxRfP6F2+dYvPLKkArHDIcUZihSwoY3TvBYsXIdhO0Q9qfWItraq8FnG5oxi0lUnAwBudAMYKacOaJ92E2LhepsUOH9YF9w/ZRkAoKNp9nPtWWMNZLDFOtSAnUsqc4fdct4gC0dOlm+dHC9Yo6Zt00wnaqZNlFKqWcTNKFLggiMKGkotG5vlUPTrULllFW1h++GzcU33S6TjG2Z4LWB4j1zNhCtH9U25JdVNpWs+uRlFCogd0nWGkSdDu7Wy1JrKoGOLRliztVgA0faz199CTeNKqL4n8tA3RmLn3v1oWC+7xqwaqGwz4WYUqSCm+Pd3MwMtZOUrszhK+8EZ/Us3Zq+ZB6lTh2KpFzv02L23smtTuDskJb5xYi98vH0POra0o9DaydJxsopMXC2L/W9rSZ1kzmRLHeWkRxszeZSs4AxFSlw72m6y003nVHe0iWzykLST50sGayD7JQ1NqraJI7uc3L8dJn24/uDfAztVtmqCcz1VCSN6tUm7CWUnaZeJiey2zKAN697aQmsclYQtoc+s4AxFlVDtfmaZhEpSxaU8RvSMbnxlUU+O2keSatNp4AxFlWBLgTarJKVLpOL4vtHrMzhD4QAq39XkJ5XehYhuJ6J5RDSLiB4nolaKfesS0XQieqaMTawIflLl6xIiaegSmayBJD3LcVQGn6oyeZS0hqEvAhjEzIMBzAdwrWLfKwHMLUurKowvHluDY3u3wVNXHJd2U6oGcQG7nsEszZZkvKOysSHTkyVSORtmfoGZ9+X/nAxAan6JqCuAMQDuLVfbKgkiwgNfH4HBXVul3ZSq4euu6I7DAvWqbMCQhRXQrwD4X8B7vwfwIwChWWlEdBmAywCge3cnC15tlCu3rkurxphx4+lVHxzgSJZqK3iV2IyCiCYS0WzJv3HCPtcD2AfgfsnnxwJYx8zTdL6Pme9h5uHMPLxdu3bWzsORDTq3Kl9CYasmDao+OMBRPrq2rvx1q8SGTcw8SvU+EX0RwFgAp7Fci+E4AOcS0WgAjQC0IKL/MPOl9lvryDptmjUM38nhyBCfH9ED/568FA98bUTaTYlNWlFPZwG4GsC5zLxDtg8zX8vMXZm5BsDFAF52RsLhcFQKN583CEtuG4PuFS7fAaQX9XQncusOLxLRDCK6GwCIqDMRTUipTQ6Hw+GQkMqKHTP3Cdi+CsBoyfZJACYl2yqHw+FwyHArdo6KpGmGJRLEGPpLjnEReI7KxxkKR0WS5QJB3Q8p+KRPH9ghxZY4HHZwhsJRkWR5gVAMrTVRoHU4soa7ix0VyfWW63nY5MdjCxpcI2uh/Luj+nCGwlGRZHmk3u2QQoJVtWXoOmon2X3aHA4fonxOy8bZrRrXtXXOLTakW6t0G+JwWMIJ2jgqhpP6tcMr+fKSfdo3S7k1apbcNibtJjgc1nAzCkfF8O1TpOk3DocjYdyMwlExHNmjNfq0b4Yfntk/7aY4HLUKZygcFQMRYeL3T0q7GQ5HrcO5nhwOh8OhxBkKh8PhcChxhsLhcDgcSpyhcDgcDocSZygcDofDocQZCofD4XAocYbC4XA4HEqcoXA4HA6HEmLmtNtgHSJaD2Cp4cfbAthgsTmVgDvn6qe2nS/gzjkqPZi5neyNqjQUcSCiqcw8PO12lBN3ztVPbTtfwJ2zTZzryeFwOBxKnKFwOBwOhxJnKEq5J+0GpIA75+qntp0v4M7ZGm6NwuFwOBxK3IzC4XA4HEqcoXA4HA6HklppKIjoLCL6kIgWEtE1kveJiP6Qf38WER2RRjttonHOn8uf6ywieouIhqTRTpuEnbOw31FEtJ+ILixn+5JA55yJ6GQimkFEc4jo1XK30TYa93ZLInqaiGbmz/nLabTTFkT0dyJaR0SzA963338xc636B6AugI8A9ALQAMBMAIf69hkN4FkABGAEgClpt7sM53wsgNb512fXhnMW9nsZwAQAF6bd7jL8zq0AfACge/7v9mm3uwznfB2AX+ZftwPwMYAGabc9xjmfCOAIALMD3rfef9XGGcXRABYy8yJm3gPgQQDjfPuMA/AvzjEZQCsi6lTuhlok9JyZ+S1m3pT/czKArmVuo210fmcA+A6ARwGsK2fjEkLnnC8B8BgzLwMAZq7089Y5ZwbQnIgIQDPkDMW+8jbTHsz8GnLnEIT1/qs2GoouAJYLf6/Ib4u6TyUR9Xy+ityIpJIJPWci6gLgfAB3l7FdSaLzO/cD0JqIJhHRNCL6Qtlalww653wngIEAVgF4H8CVzHygPM1LBev9V71YzalMSLLNHyOss08loX0+RHQKcobi+ERblDw65/x7AFcz8/7cYLPi0TnnegCOBHAagMYA3iaiycw8P+nGJYTOOZ8JYAaAUwH0BvAiEb3OzFsTbltaWO+/aqOhWAGgm/B3V+RGGlH3qSS0zoeIBgO4F8DZzLyxTG1LCp1zHg7gwbyRaAtgNBHtY+YnytJC++je2xuYeTuA7UT0GoAhACrVUOic85cB3MY5B/5CIloMYACAd8rTxLJjvf+qja6ndwH0JaKeRNQAwMUAnvLt8xSAL+SjB0YA2MLMq8vdUIuEnjMRdQfwGIDPV/DoUiT0nJm5JzPXMHMNgEcAfKuCjQSgd28/CeAEIqpHRE0AHANgbpnbaROdc16G3AwKRNQBQH8Ai8rayvJivf+qdTMKZt5HRFcAeB65iIm/M/McIro8//7dyEXAjAawEMAO5EYkFYvmOd8IoA2AP+VH2Pu4gpU3Nc+5qtA5Z2aeS0TPAZgF4ACAe5lZGmZZCWj+zjcDuI+I3kfOLXM1M1es/DgR/RfAyQDaEtEKADcBqA8k1385CQ+Hw+FwKKmNrieHw+FwRMAZCofD4XAocYbC4XA4HEqcoXA4HA6HEmcoHA6Hw6HEGQpHrYOIOhDRA0S0KC9j8TYRnZ9/72Qi2kJE04loLhHdlN/ehIjuJ6L3iWg2Eb1BRM18x52SV2VdRkTr869nENGxRPRIQudyHhHdqHj/cCK6L4nvdtQeal0ehaN2kxeGewLAP5n5kvy2HgDOFXZ7nZnHElFTADOI6BkAZwBYy8yH5z/TH8Be8djMfEz+vS8BGM7MVwhvv5XMGeFHvrYXwczvE1FXIuruCQE6HFFxMwpHbeNUAHvEhDtmXsrMf/TvmJe5mIacPlAnACuF9z5k5t06X0hENV7tACL6EhE9ka+PsJiIriCi7+dnMJOJ6JD8fr2J6Ln8jOd1IhogOW4/ALu95DEiuig/25mZl+bweBq5jGWHwwhnKBy1jcMAvKezIxG1QU7Pfw6AvwO4Ou+muoWI+sZowyDk5L6PBvBzADuYeRiAtwF4aq73APgOMx8J4CoAf5Ic5zjfudwI4ExmHoLiWcZUACfEaK+jluNcT45aDRHdhZxS7h5mPiq/+QQimo6cxMVtzDwnv28v5FxQowC8S0QjmdlEJ+kVZt4GYBsRbUFuxA/kJLAH59c+jgXwsKBq21BynE4A1gt/v4mcVMVDyOl2eawD0NmgnQ4HAGcoHLWPOQA+5f3BzN8morbIjbo9Xmfmsf4PMvMnyHXAjxHRAeT0dEwMheiyOiD8fQC5Z7IOgM3MPDTkODsBtBTadzkRHQNgDHJrK0PzKsCN8vs6HEY415OjtvEygEZE9E1hW5OwDxHRcUTUOv+6AYBDASxNooH5OgmLieii/PcRyWuYzwXQR2hjb2aewsw3AtiAgtR0PwAVK/znSB9nKBy1inxNgvMAnJRfTH4HwD8BXB3y0d4AXs0rkE5HbgbyaIJN/RyArxLRTORmQbIyrq8BGEYF/9TtXvhu/r2Z+e2nABifYFsdVY5Tj3U4KhgiugPA08w8MeD9hgBeBXA8M1dsnWhHurgZhcNR2fwCatdZdwDXOCPhiIObUTgcDodDiZtROBwOh0OJMxQOh8PhUOIMhcPhcDiUOEPhcDgcDiXOUDgcDodDyf8D6kkawgOhAh0AAAAASUVORK5CYII=\n",
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
    "# Get the HDF5 group: group\n",
    "group = data['strain']\n",
    "\n",
    "# Check out keys of group\n",
    "for key in group.keys():\n",
    "    print(key)\n",
    "\n",
    "# Set variable equal to time series data: strain\n",
    "strain = np.array(data['strain']['Strain'])\n",
    "\n",
    "# Set number of time points to sample: num_samples\n",
    "num_samples = 10000\n",
    "\n",
    "# Set time vector\n",
    "time = np.arange(0, 1, 1/num_samples)\n",
    "\n",
    "# Plot data\n",
    "plt.plot(time, strain[:num_samples])\n",
    "plt.xlabel('GPS Time (s)')\n",
    "plt.ylabel('strain')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7fb2517f",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Loading .mat files\n",
    "In this exercise, you'll figure out how to load a MATLAB file using `scipy.io.loadmat()` and you'll discover what Python datatype it yields.\n",
    "\n",
    "The file `'albeck_gene_expression.mat'` is in your working directory. This file contains gene expression data from the Albeck Lab at UC Davis. You can find the data and some great documentation here.\n",
    "\n",
    "* Import the package `scipy.io`.\n",
    "* Load the file `'albeck_gene_expression.mat'` into the variable mat; do so using the function `scipy.io.loadmat()`.\n",
    "* Use the function `type()` to print the datatype of mat to the IPython shell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b846b500",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "# Import package\n",
    "import scipy.io\n",
    "\n",
    "# Load MATLAB file: mat\n",
    "mat = scipy.io.loadmat('datasets/ja_data2.mat')\n",
    "\n",
    "# Print the datatype type of mat\n",
    "print(type(mat))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa869fb3",
   "metadata": {},
   "source": [
    "Great job!\n",
    "\n",
    "## The structure of .mat in Python\n",
    "Here, you'll discover what is in the MATLAB dictionary that you loaded in the previous exercise.\n",
    "\n",
    "The file `'albeck_gene_expression.mat'` is already loaded into the variable mat. The following libraries have already been imported as follows:\n",
    "```python\n",
    "import scipy.io\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "```\n",
    "Once again, this file contains gene expression data from the Albeck Lab at UCDavis. You can find the data and some great documentation here.\n",
    "\n",
    "* Use the method `.keys()` on the dictionary mat to print the keys. Most of these keys (in fact the ones that do NOT begin and end with '__') are variables from the corresponding MATLAB environment.\n",
    "* Print the type of the value corresponding to the key 'CYratioCyt' in mat. Recall that `mat['CYratioCyt']` accesses the value.\n",
    "* Print the shape of the value corresponding to the key 'CYratioCyt' using the numpy function `shape()`.\n",
    "* Execute the entire script to see some oscillatory gene expression data!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "48190f50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['__header__', '__version__', '__globals__', 'rfpCyt', 'rfpNuc', 'cfpNuc', 'cfpCyt', 'yfpNuc', 'yfpCyt', 'CYratioCyt'])\n",
      "<class 'numpy.ndarray'>\n",
      "(200, 137)\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEVCAYAAAD6u3K7AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAABX5UlEQVR4nO2deXhddZn4P+9dszVN042udGMrhbKUtSiCgMio4C6KK4qO6DjjrrPoDD+HcWZ0RscFUREdEQUVBETAUVZZW5a2QCnd9zZNmjT73d7fH+ecm5vkLufc5CY39P08z32Se8493/Mmbb7veXdRVQzDMAxjKKHxFsAwDMOoTkxBGIZhGHkxBWEYhmHkxRSEYRiGkRdTEIZhGEZeTEEYhmEYeTEFYRiGYeTFFIRhGIaRl0ixkyJSA7wBeBUwG+gF1gG/V9XnKy+eYRiGMV5IoUpqEfkq8EbgAWA1sB+oAY4GznO//4yqrhkLQQ3DMIyxpZiC+CtV/X3BC0VmAPNVdVWlhDMMwzDGj4IKwjAMwzi8KRqDABCRo4HPAUfmfl5Vz6+gXIZhGMY4U9KCEJHngOtw4hBp77iqrq6saIZhGMZ44kdBrFbVU8dIHsMwDKNK8KMgvoqTwXQb0O8dV9W2ikpmGIZhjCt+FMSWPIdVVRdVRiTDMAyjGrAsJsMwDCMvfrKYosBfA692Dz0A/EBVkxWUyzAMwxhn/LiYfgREgZ+6h94LpFX1wxWWzTAMwxhHfKW5quryUseqgWnTpumCBQvGWwzDMIwJw+rVqw+o6vR850q6mIC0iCxW1U0AIrKInHqIamLBggWsWmWdPwzDMPwiItsKnfOjID4H3C8imwHBqaj+4CjJZhiGYVQpJRWEqv5JRI4CjsFREOtVtb/EZYZhGMYEp6CCEJHzVfXPIvKWIacWiwiq+tsKy2YYhmGMI8UsiHOBP+PMhBiKAqYgDMMwXsEUVBCq+hX3q8UbDMMwDkNKzqQWkU+JSKM4/EhEnhaRi8ZCOMMwDGP8KKkggA+p6iHgImAGTgbTv1VUKsMwDGPc8aMgxP16CfATVX0u55gxAp7ZfpBnd7SPtxiGYRh58aMgVovIfTgK4l4RmQRkKivW4cFX73ieL/127XiLYRiGkRc/hXJXAicBm1W1R0SasUK5UWFbWw+dfSn6kmlqouHxFscwDGMQfiyIs4CXVLVdRK4A/gHoqKxYY09HT5Lfr9nDAy/tH5v79SZp70mSzigv7Dk0Jvc0DMMIgh8F8X2gR0SWA58HtgE/K3WRiNwgIvtFZF2Jz50mImkReVvOsa0islZEnhWRijZX6kumedv3H+Xka+7j6l88zYd/uop1uyqv/3a09WS/H4v7GYZhBMWPgkip0/L1UuBbqvotYJKP624ELi72AREJA18H7s1z+jxVPUlVV/i4V9nURMPMaqrl6vOWcNOHz6C5PsZnb32ORKqyYZZcBbFmpykIwzCqDz8KolNEvoQzB+L37qYeLXWRqj4ElJpb/UngNzgzr8eN/7n8ZD5z0TGsXDKNa99yAuv3dvI/f365ovfc7iqIU4+cYhaEYRhViR8F8U6gH6ceYi8wB/iPkd5YROYAbwauy3NagftEZLWIXDXSewXhtcfN5K2nzOV7D2xie2tP6QvKZMfBHprqopy9eCob9nXSm6jKDuqGYRzGlFQQrlL4DRB3Dx0AbhuFe/838AVVzbczrlTVU4DXA1eLyKvzfAYAEblKRFaJyKqWlpZREAs+ef4S0hnlwQ2VM2y2t/Uyv7mOE+ZMJqNYoNowjKrDT6uNjwC/Bn7gHpoD3D4K914B/FJEtgJvA74nIpcBqOpu9+t+HGV0eqFFVPV6VV2hqiumT887FCkwR06tY05TLX/Z2Doq6+VjR1sP86bUccLcyQCs3dlesXsZhmGUgx8X09XASuAQgKq+jNNyY0So6kJVXaCqC3AU0MdV9XYRqXeL8RCRepwWH0UzoUYbEeHsxVN5bHMr6UzxkazlkM4oOw/2MK+5jiMaa5jWEGftLrMgDMOoLvwoiH5VTXhvRCSCEyMoiojcDDwGHCMiO0XkShH5mIh8rMSlM4FHROQ54Eng96p6jw85R5WVS6bR0Zvkhd2jv3HvPdRHMq3Mb65DRDhhTiNrd7WP+n0MwzBGgp9K6gdF5MtArYhcCHwcuLPURap6uV8hVPUDOd9vBpb7vbZSnL14KgCPbjqQdQONFl7we35zHQAnzJnMgxtarKLaMIyqwo8F8QWgBVgLfBS4G6ea+hXNjMYalsxo4C+bRj8OsePgYAUxbVKcjEJXf2rU72UYhlEuRS0IEQkBa1R1GfDDsRGpeli5eCq3rNpJIpUhFvGjS/2xo62HkMCsphoAIiFn7VR69OMdhmEY5VJ011PVDPCciMwfI3mqirOXTKM3meaZ7QdHdd3tbT3MbqolGnZ+/dGw0z09mbYmuYZhVA9+YhCzgOdF5Emg2zuoqm+qmFRVwpmLphISePjlA5yxaOqorbu9rSfrXgKyisIUhGEY1YQfBfHPFZeiSplcG+X0hc3c8/xePvu6Y0Zt3R1tPVxw3Mzs+wEFYS4mwzCqBz+V1A8CLwGTgUac1t8PVlqwauGSE2axcX8XL+/rHJX1ehNpDnQlmJdjQUTMxWQYRhXip5L6wzj1CG/BqXh+XEQ+VGnBqoXXHX8EIvCHdXtHZb1DfUkAptTFssdi5mIyDKMK8ZOa8zngZFX9gKq+HzgVJ/X1sGBmYw2nzp/C3Wv3jMp6XlO+mujAr96zIFIVqNo2DMMoFz8KYieQ61/pBHZURpzq5PUnzGL93k62HOgu/eES9KUcBVGbUxCXjUFUeAaFYRhGEPwoiF3AEyLyVRH5CvA4sFFEPi0in66seNXBxcuOAOAP60ZuRQxYELkKwo1BmAVhGEYV4UdBbMLp3urtXr8D9uBMlfMzWW7CM6eplpPmNXHLUzvodGMI5dKXdKyEeI6LySwIwzCqET9prl9X1b7cAyIyTVUPVEimquRzrzuG99/wJFf/4hl+/P4V2U09KPlcTNlK6owpCMMwqgc/u9yTInKm90ZE3go8WjmRqpOVS6bxtTcv46ENLfzT78rvPt6Xx8UUizgupoTVQRiGUUX4sSDeA9wgIg8As4GpwPmVFKpaeedp89mwr4sfP7KFvz53CfOn1pW+aAhFLQhLczUMo4rwUyi3Fvga8DHgPOATqrqz0oJVK6cvbAYG6hmC0ptwlMCgIHXE6iAMw6g+SloQIvJjYDFwInA0cKeIfEdVv1tp4aoRr6troszNvC+ZL83VXEyGYVQffmIQ64DzVHWLqt4LnAmcUlmxqpe4G5xOlJlx1OsqiEFZTOZiMgyjCvHjYvovYL6IXOAeSgB/W0mhqpmsBVGmguhPphGBeM58CXMxGYZRjfjpxfQR4NfAD9xDc3HqIg5L4hHHNdRfpoLoS2WoiYQRkeyxSMhr1mcuJsMwqgc/LqargZXAIQBVfRmYUUmhqpmRWhC9ifSgPkxg8yAMw6hO/CiIflVNeG9EJMJAVXVBROQGEdkvIkWLBkTkNBFJi8jbco5dLCIvichGEfmiDxnHjIEgdbqs6/uS6UEBaoBwSAiJjRw1DKO68KMgHhSRLwO1InIhcCtwp4/rbgQuLvYBEQkDXwfuHXLsu8DrgaXA5SKy1Mf9xoQRWxDJ9KAUV49oOGQWhGEYVYUfBfFFoAVYC3wUuBv4h1IXqepDQFuJj30S+A2wP+fY6cBGVd3sWi6/BC71IeeY4AWXy45BJDPECyoIsyAMw6geStZBqGoG+KH7GjVEZA7wZpyq7NNyTs1hcDvxncAZo3nvkTDiLKZUmtrocL0cDYtZEIZhVBXldZwbHf4b+IKqDnXmS57PFny0FpGrRGSViKxqaWkZTfny4k1/K9eCcILUwy2ISDhkzfoMw6gq/PRiqhQrgF+66Z7TgEtEJIVjMczL+dxcYHehRVT1euB6gBUrVlTcRxMbYaFcXyrN5Npo3nUTKXMxGYZRPRS0IETkf92vn6rEjVV1oaouUNUFOHUWH1fV24GngKNEZKGIxIB3AXdUQoZyCIWEaFgqYEGIWRCGYVQVxSyIU0XkSOBDIvIzhrh+VLVoAFpEbgZeA0wTkZ3AV4Coe+11ha5T1ZSIfAInsykM3KCqz/v4WcaMeCRcvgWRzFgWk2EYE4JiCuI64B5gEbCawQpC3eMFUdXL/Qqhqh8Y8v5unGypqiQWCY2oDmJooRw41dSWxWQYRjVR0MWkqt9W1eNwnuAXuS4h71VUObzSceIF5XdzzWdBxCJmQRiGUV34SXP9axFZDrzKPfSQqq6prFjVTSxSnoJQVfpSmWGV1OBYEFZJbRhGNeGnWd/fADfh9F+aAdwkIp+stGDVTDwSKitInUwr6YzmdTFFw6GyZ0wYhmFUAj9prh8GzlDVbgAR+TrwGPA/lRSsminXgvDGjRYKUvckUiOWrT+VJhYODeoWaxiGUQ5+FIQAuRHZNPmL2Q4bnCB1GQoiUUxBlB+kTqQyXHPXCzy1tY0N+zr54MqF/OMbqqZ9lWEYExQ/CuInwBMicpv7/jLgxxWTaAIQC5fnYupLDp9H7REZQZrrppYu/vfxbZw0r4kpdTG2HOguax3DMIxc/EyU+ybwQZzGeweBD6rqf1dYrqomVmYMojfPPOrsmiNQEN6c609dcBSLZzTQ1T9yV5VhGIavVhuq+jTwdIVlmTA4hXKJ0h8cgreR562DCAupTHkupqxlEgkzKR5h76G+stYxDMPIZTyb9U1Y4pEQiVTwQrm+IhZENBwiOYL+TgDxaIj6eIRusyAMwxgFTEGUQblBas/FlH8ehJAs04Lo9yyTSJj6eISu/vKqvA3DMHLxpSBE5EgRucD9vlZEJlVWrOqm3EpqzxVU0IIoOwbhBb9DNMTDdPUny1rHMAwjFz+Fch/B6bb6A/fQXOD2CspU9cSj5WYxFYlBhEJlV1L359RX1Mcj9CUzpMpUNql0ht6EWSCGYfizIK4GVgKHAFT1ZZyK6sOW8i2IInUQESm7kjo3fbYh7uQddJe5yX/3/k284X8eLutawzBeWfhREP3ubGgARCRCkQlvhwPlVlIXS3ONhkJlP/V7iiceCQ0oiDID1TsO9rCppTtrlRiGcfjiR0E8KCJfBmpF5ELgVuDOyopV3cQiIVIZp69SEIoVykXDITJK4DWHrls/QgXhtfvYf6i/rOsNw3jl4EdBfAFoAdYCH8WZ0/APlRSq2olHnA0+qBWR+6Q/lEjY6V5STqC6L5UmGhbCIclaEJ1lKwhHxv2dVkthGIc7RQvlRCQErFHVZcAPx0ak6icWGZhLXRsbbg0Uoi+ZJh4JEQoNb2XlzbpOpvNPnCu1bo2rtEZuQTgKYm+HWRCGcbhT1IJQ1QzwnIjMHyN5JgSegugPOFWu0LAgGLAgyslk6k9lsrUVI41BeBlM+6wa2zAOe/y02pgFPC8iTwLZLnCq+qaKSVXlxMMDFkQQepPpvAFqcGIQUKaLKWeMqacgyi2W63ZjEKYgDMPwoyD+ueJSTDCyFkTgGEQmbw0E5LiYyghS9ycz2bhGfdxRQCO1IKyfk2EYfkaOPjgWgkwk4pHyLYhSLqZy+jHluq7qsxbEyGIQZkEYhuGnkrpTRA65rz4RSYvIIR/X3SAi+0VkXYHzl4rIGhF5VkRWicg5Oee2isha71ywH6nyxMpUEMViEJ6LKZUpL4vJWzceCREJyQgUhOdiGlmQWlW54JsP8qunto9oHcMwxg8/8yAmqWqj+6oB3gp8x8faNwIXFzn/J2C5qp4EfAj40ZDz56nqSaq6wse9xpSsgggYL+hPZorEIBwLIpEqrw7Cc12JCA015XV0TaYz2al2+w71oVp+PWRnf4qN+7u4f31L2WsYhjG+BO7mqqq3A+f7+NxDOEOGCp3v0oEdqJ4JVJ0dG0GQulAMYiQWRH9qIM0VoD4WKcuC8NxLMxvj9CTSZddSABzsdorv1+3uKHsNwzDGl5IxCBF5S87bELCCUdrMReTNwLU4vZ3+KueUAveJiAI/UNXri6xxFXAVwPz5Y5ON66WUBm1HUTzNdSRZTBniOYqnIR6hqy/45u4FqBdOq2ffoX72dfTRWBMNvA5Am6sgdh7spb0nQVNdrKx1DMMYP/xYEG/Meb0O6AQuHY2bq+ptqnoszpzra3JOrVTVU4DXA1eLyKuLrHG9qq5Q1RXTp08fDbFKMhILojIupiEWRDycTVcNgnfNoukNwMjiEAd7BibuPb+7ZMjKMIwqxE8W0wcrLYSqPiQii0VkmqoeUNXd7vH9InIbcDrwUKXl8MtI0lzzDQuCEQaph6xbH49waCQWxNR6YGSprq1dAwpi3a4OVi6ZVvZahmGMD36ymP5dRBpFJCoifxKRAyJyxUhvLCJLRETc708BYkCriNR7A4lEpB64CMibCTVelJvm2l+hQrn+IbGNSWUGqb0YxIJpjoIYSaqrZ0FMqYuyziwIw5iQ+CmUu0hVP+/GC3YCbwfuB35e7CIRuRl4DTBNRHYCXwGiAKp6HU421PtEJAn0Au9UVRWRmcBtru6IAL9Q1XvK+eEqRbkWRLEgdSTkNesrw8WUGhzbqI+VqyCca5rrY0yujY5IQbR1J4mFQ6xY0MzzFqg2jAmJHwXhRSkvAW5W1TZ38y6Kql5e4vzXga/nOb4ZWO5DrnGjHAsimc6QymjBILWndIJaEOmMkkzrkBhEeUFqz4Koi4WZ2Rhnb8cILIjuBFPqo5wwZzL/9+I+uvpT2TYghmFMDPwEqe8UkfU42Ut/EpHpwGFdZltOHURfkWFBMGBBBG3W52VSDc1i6k6kAtcxDFYQNezrLD9I3dqdYEpdjGVzGlGFF/eYm8kwJhp+CuW+CJwFrFDVJE7DvlHJYpqolJPFNDDUp3gdRNDiu+y6OTMm6uMRMjowwc4vva6LqTYW5ojGGvaNxILoSTC1IcbxsycDTqDaMIyJhV+bfw5woYjU5Bz7WQXkmRBEwiFCEqwOotg8asjJYgpoQeRbt6FmoB9TXcy/W8ezIOpjEWY21tDS1U86o4TzzK8oxcHuBEtnNzJjUpxpDXHW7TILwjAmGn4K5b6CE2xeijNN7vXAIxzGCgKcqXLBLIhSCqK8iXJ5FUS2o2saJvlfqzsx4AabObmGdEZp7epnRmNNiSuH09aToLk+hoiwdHYj6/eagjCMiYafGMTbgNcCe92aiOVAvKJSTQBikVCZLqbRraTO57qqd62GoIHq3kSKmqgz8W7mJOefuJxaiFQ6Q0dvkilu9fTk2mjZ7ccNwxg//CiIXneyXEpEGoH9wKLKilX9xCKhQPGC3hJB6oGRo2UGqSO5FkR5Lb97EumscvFaY3SWkQ3V3ptE1UmXBednKyd91zCM8cWPglglIk04M6lXA08DT1ZSqIlALBwKVAcx4AoqUAeRHTlangUxKIuppryxo72JdHbGdjxb6xF8Mp3XqC+rICISuGYkl437O/n8r58LXJhoGMbI8JPF9HFVbXeL2y4E3j8W7TeqnXgkmILoLRGDGCiUC6ggUsPX9YYGBe3H1J1IUecpCFfh9CeDb8ptQxVEOFRWhbjHvc/v45ZVO1m1rWBzYMMwKoCfVhsiIleIyD+p6lagXUROr7xo1U3wGERxBSEiRMMSeORov7fuKLmYal0Xk+ey6ivHgsi22fAsiGC/q6HsPNgLwKMbW8tewzCM4PhxMX0Ppw7Cq4zuBL5bMYkmCPGyFUThX3k0HAo8cjRvkDpebpA6Tb1rQdSMwIJoHWJBREdoQexqdxTEXzYdKHsNwzCC40dBnKGqV+NWT6vqQZzGeoc1QZ+KPXdUIQsCHDdTKqAF4Sme3G6udVEvzTW4BZF1MUW8mRfBN3YvBjGl3unSEouESGWUTMCfzWPnwR4A1uzsoLMvWdYahmEEx4+CSIpIGHdIkNtq47CPFsYioUABXE+ZeAVxhdYMPMbUUzw5ldShkDhDg/qDuYd6EqkcF1P5Qeq27iQN8UhWyZRbJQ7ObOvd7b0sm9NIOqM8sdniEIYxVvhREN8GbgNmiMjXcIrk/rWiUk0A4pFwoA3P28jjkcK/8kgoVEYWU/7YRn08XJ4FER2cxdRXhovpYE8iaz3krlWOgmjtTtCXzPCm5bOJR0LmZjKMMcTPwKCbRGQ1TrGcAJep6osVl6zKiYWDuZg8H3ysiAURjUjgeoFCBXj18eBzqXsTaercKuxIOEQkJGVaEAmac0aMZmddlOGu8gLUC6c1cNqCZgtUG8YY4seCANgHPAw8CtS6A34Oa4LGIBKpDJGQECrS1ygaCh7M7UuliYZlWL+khoAKQlXpSQ7EIMBN5S0zzXVK/YCCKKf7rccuV0HMaarl7CVTeWlfJy0j6DJrGIZ//PRiugb4ALAJNw7hfj2/cmJVP+UoiFgR9xKUl+0zdB61R9ChQf2pDOmMDmruVxMNl5Xm2tad4KiZDdn3AxZE8CD1rnYnQD1nSi0rF08DXuLxza28cfnswGsZhhEMP60+3wEsVtVEyU8eRsQCFsol0qUVRCQsZXRzzQyqovZoqImwo63H9zq9ieGtQMq1IA72DHYxDVgQwZXNzoO9TKqJMLk2mh2Fut8sCMMYE/y4mNYBTRWWY8IRtA4ikcoUjT+A86QdPIspPagPk4c3NMgvPW6wuz6eoyCi4cBprn3JND2J9GAXk9tGJFGOBXGwlzlNtY48I8isMgwjOH4siGuBZ0RkHZB9dFPVN1VMqglALBKiP8Bm7s/FFNyC6E9m8hbf1cfDgQrlBoYFDfyXiAdM5YXhbTZghDGI9l7mTqnLygPlFe8ZhhEcPwripzizo9di9Q9Z4m4Wk6riZ0Z3vw8XUzRgZhS4MYg8xXf18YgzD8In3mfrooMtiKBprvkURLTMVuaqys6DvZy5aCrgtCMJ6tozDKN8/LiYDqjqt1X1flV90HuVukhEbhCR/a7lke/8pSKyRkSeFZFVInJOzrmLReQlEdkoIl8M8POMGUGfiv24mCLhUOBeTH2p/Aqixq3T8Fu9nDuP2qMcC8LrwzTIgihjRCvAod4UXf2prIsJHMVsLibDGBv8KIjVInKtiJwlIqd4Lx/X3QhcXOT8n4DlqnoS8CHgRwBu1fZ3cSbXLQUuF5GlPu43pnh+f7+bnh8XUywsZfViyld8F1SB9SYdF1NdfKiLKZg8Hb1OK4zGmoFCuWiZLqadbgbT3Ck5CiJqFoRhjBV+XEwnu1/PzDlWMs1VVR8SkQVFznflvK1nIIX2dGCjqm4GEJFfApcCL/iQdczIbsBBFISPIHUqE9zFNLk2Ouz4QEA3U7T/k0c+C6ImGuZAV7Dktexc65xgd7kWhFckNydXQUTCFoMwjDHCTyX1eZW6uYi8GScIPgP4K/fwHGBHzsd2AmdUSoZyCfqEnvSV5hp88pqjAIavGw+owHr6C6S5BnTn9Li1F7n1FN7PHTQGkVsklytTOcFuwzCCU3DHcmdAFDu/ODduUA6qepuqHgtcBlzjLZ3vo0XkuMqNYaxqaWkZiTiB8J6K/T7N+qmDiIZl1ArlBrqx+tvgexLexp6rIII/rXvpsrnrlGtB7GrvpSYaGpYR5c3AMAyjshSzIKbipLeuxhk12gLUAEuAc4EDwKgEkF131GIRmYZjMczLOT0X2F3k2uuB6wFWrFgxZoOPKxGkLqvVRjIzqNX3MPn8WhDZOoicGEQZ/v6e/jQhGdyUMFqmBbHzYA9zp9QNyhIrpzbDMIzyKKggVPVbIvIdnFjDSuBEoBd4EXivqm4fyY1FZAmwSVXVDXrHgFagHThKRBYCu4B3Ae8eyb0qQVAXjq86iEg5dRDpoi4mv5tpbyKNDNnYayLhwE/rPYk09bHIoE29XAuitSvB9Ib4oGPluL0MwyiPojEIVU0Df3RfgRCRm4HXANNEZCfwFSDqrnsd8FbgfSKSxFE871RVBVIi8gngXiAM3KCqzwe9f6WJBdyA+30oiEgouH+9r0AldVALorvfafU9+Gm9DAsikaI2NlierDsuaJprX5JF0xoGHYtHQoG71Obyd796liOn1vG3Fxxd9hqGcbjgJ4upLFT18hLnv45TgJfv3N3A3ZWQa7QInMWUzp+OOnTNIBZEOqMk05rXggiqwHqTqUFV1DAQEM5ktGgX2ly6E+lBbqpcWYIG4A/1pmisHSpTmNaAmVUeqXSGu9fuyRbeGYZRHL/tvo0hBO0L5KtQLhQsSO3dO18aa9A6jZ5EelBqau66QZ78exOpQQFqCK5MPQ71JQfVU4Bn1ZTnYtrU0k1/KkOvBbkNwxemIMqkEoVyTh2E4njaSpMdFlS0UM7fZtjdnx6U4grlNcfr7k8PUxDhkBCSYEHqZDpDTyJN45Aaj3KK9zzW7eoABqbwGYZRnJIKQkRmisiPReQP7vulInJl5UWrbgJnMflMcwX/rphC40YheGO73uTwJ/+BVFn/G7IzdGi45zLovO1D2Yrs4S6mshXEbkdBeMV8hmEUx48FcSNOwNib0LIB+NsKyTNhCJKZk84o6Yxmm9YVwjvvt5raUxD55kEEVWA9ieEbezndU3v6hysaCN6I8JDbiTavBVGmBfD8rkPAwOwLwzCK40dBTFPVW3A7uapqCjjs/8KCBIGz86h9VFKD/8lrAy6mUbAgEsNdQ55lEmSqXD5F48lTjgUxtI1Iub2YMhnledeCsBiEYfjDj4LoFpGpuNXMInIm0FFRqSYAQQKv3oZWKkidHazjcyPtKxKkziown2t15wkul2VB5FkH3HGqgSwI18U0zIJwXEx+4zQeW1u76U6kmVIXNQvCMHziR0F8GrgDWCwifwF+BnyyolJNAIIUynmfKZXmGgnoYvI27nwupnjYjR/4fFruTaSHp7lGgwepexJp6uL5FVYwC8J1MQ3NYiqzM+y63Y57acWCZnqTad9t0A3jcKakglDVp3Faa5wNfBQ4XlXXVFqwaicWIMMn4dPFFA3qYiqW5hoNtpF29aeYNCQgnHUx+bQgUukM/akMddHhLqZoOFgbkQELokBcJKCb6fldHcQiIU6cM7ms6w3jcMRPFtPVQIOqPq+q64AGEfl45UWrbmLhEPFIKBtMLYZnQfjOYvJtQbgKIl8ldYAgeiqdoS+Zob5QkNpvw788c61z5QkUpM4zVwLI9p0K2kRw3e4Ojj1iUlYJWhzCMErjx8X0EVVt996o6kHgIxWTaIIgIkypi3Gwu3RVb1ZBhIvPZQg6mrOviIspFBKiYfH1pOyNGx26sQdNc+3NzpTIY0FEQiQCVFIf6ksSDknhuEgAt5eqsm7XIY6fPTnbBsTrXmsYRmH8KIiQ5DTocSe+xYp8/rBhSn0sO2KzGH4tiIjbzsJvu41idRDg/6m9y90sh7qYgm7G3f3DW4Zn1wqHSATY1A/1pmisiQyb912Oi2l3Rx8dvUmWzm7MxlnKLZbbcqCbe9btKetaw5ho+FEQ9wK3iMhrReR84GbgnsqKNTGYUhflYE+y5Oe8aubS3VyDxQ28TTJfJTV4rbFLb4RdrptsaA+loDGIfFPpPKIRCdSLqaM3WWBSXnAXU0tnPwCzGmuy1eLlFstd98AmPn3Lc2VdaxgTDT/N+r6AE5z+a5xhPvfhzo8+3JlSH+NFNzumGH7TXKMhN4tprC2I/vwKYiDN1e/QocIuplg4lM1M8sOhvuSwFFcoL7Oq3bXyptRHs8qu3FTXTS1d9CTSpDNK2GcDQ8OYqPgZOZoBvu++jBwcCyKIi6n4hjLQasNvewy3krqgBeGvqMxzDU0aqiCiwdw52al0eYLUgbOYeoc36oPyXEwd2aK7GOB8X26QevOB7uz1DfGKNUM2jKrATxbTShH5o4hsEJHNIrJFRDaPhXDVTnNdjPbeJOkSOfWea6VUkDoSMEjd0ZukIR7JXjcUvxZEd0ELYvRcTLFI8FYbQ1Ncc2UKoiC8RIIpddGsi6kcC6K9J0Gbu1bPCGZSGMZEwc8j0I+Bv8MZO2q5gTk01cVQdZ52p9QXjtv7DVLHsgrCn4upkJ8+u57PTbnT3eyGPhGHs5lQwVxMQ9NlwVVWo2lBBLAA2nPadnS68ZZyLIhNLd3Z77utGts4DPCjIDpU9Q8Vl2QCMqXe2cAO9iSKKwifQepI2Mti8mlB9BRXEH5bY3cXUBDOGv67p3oupqET5aAcCyJ/DKImoNsLoL0nyaQax9IaSHMNvsFvbunKft9tFoRxGOBHQdwvIv8B/Bbo9w66FdaHNVPqHKVQKg7hv1AuWBZTe2+SprqRWxCFXEzgbMj+01wLWxBBYhD9qTR9ycywVt8w4KYLpiAS2d+TpyDKSXP14g9gLcONwwM/CuIM9+uKnGMKnD/64kwssgqiu3iqa8JvFlM4WB1ER2+So2c2FDwfj4SzGTzF6OxPEQuH8iqweCTsOwbRm0ghQsERqH4tCM8NlDfNtYwspoM9yey/1UhiELkWhBXaGYcDfrKYzhsLQSYiza5bqa3EJtxfKQuiJ+lm5uQnFsDF1JDnaR2CTXDrTqSpi4aHFbd5sviNrWTbbOStgwjeYbY9J1YTDYeIhiXbFiQIm1u6OXJqHdtae8yCMA4LbKLcCPDcFqWe0r0Nv1Q317oA7g9VpaM3UTIG4c/FNHwetUcswIAep5NrfkUTdYPUftp0dxTowwTlZTG19ySyFgQ4dSNBLYhUOsPW1m6Wuc3+LAZhHA5UbKKciNwgIvtFZF2B8+8RkTXu61ERWZ5zbquIrBWRZ0VklQ8Zx4WGeIRoWGgbJReTV2Dm5+m0N5kmmdaSMQg/G2lnXypv3ACczbQvQJA6X4orDChHP1bEwDS5/KNLwf8scHAsrdzfU20ZCmLnwV6SaeUEV0GYBWEcDlRyotyNwMVFzm8BzlXVE4FrgOuHnD9PVU9S1RXDL60ORISmulhpCyKVIRISQiUqb2MRx/3R5ePptN1t8dFUyoLw4a7qztPqO3eNQBZEAUUTDTAMqVAnVwieepvOKIf6koN+T3WxcOA0180HnPjDstmuBWExCOMwoGIT5VT1IaCtyPlH3c6wAI8Dc33IUnU015Vu2JdIZUrOo/aoi0V8FWF5CqK4iynsa3PvTqTyZjCB189p5BZEkPbjhabJZWUKkHp7qDeJqlOz4lETLUNBuDUQS2c3EhLo6TcLwnjlUy0T5a4EcmstFLhPRFaLyFXFLhSRq0RklYisamlpGWWxStNUFy2ZxZRMZ0oGqD3qY2FfRVjZ9hGl0lx9PLF39RVWEDWRkO+U0J48c609olkXkx8LIv80OQ8ncO5PJq9ILtfFVBcL7mLa1NLNlLoozfUx6mMRczEZhwV+spieFpFzgWNwmvW9pKqlW5j6RETOw1EQ5+QcXqmqu0VkBvBHEVnvWiT55Lse1z21YsWKMZ8jOaUuxqac9Md8JAIoiLp4xFcKZUevY7U0Fcli8jKQVDVvZpFHV39qWB+m7BrRsG9/f09/mhmT4nnPBbUgYuFQ3nRZ8Nxe/mTyrLvcIHVtOS6mli4WTXdSiuviYUtzNQ4LxnWinIiciNMZ9lJVbfWOq+pu9+t+4Dbg9NG4XyXwMxOiP5UpGaD2qI+FswVnxci6mIpZEOEQqpAq0Suqu7+IiylQmmvhYHc2uOwzBtFYO3wWRFamAG6vjjy/p9pocAtge1sPC6bWA04hoLXaMA4Hxm2inIjMx6nOfq+qbsg5Xi8ik7zvgYuAvJlQ1YA3E6JY+mYilSmZ4upRF/NrQfgIUvtoS5HJKN2JdAkF4W8z7E2k87bZgKAWRKqgeymoTIUsiCCV1KrKga5+ZjTGs9dbsz7jcMBPJXVIRETdHdDvRDkRuRl4DTBNRHYCXwGiAKp6HfBPwFTge+6TYsrNWJoJ3OYeiwC/UNWqHVDUXB9zM2VSBQPGiVSAGEQ8wu723pKfa+9NEg0PH8mZy6BNOb/nJ5uNU8jFVBP1X0ldLNgdZJzqod4kk0ahxxTkz/aqjYYCxSAO9aVIppWpbmGkY0EEUxCrtx1kc0sXb18xL9B1hjGe+FEQ3kS563CCxx/Dx0Q5Vb28xPkPAx/Oc3wzsHz4FdWJlx3T3lO4aC1IDKLep3+73W3UVyy2EMsWlRXeDAfmUY/MgkhnlL5kpnAWU4D6hY7eZN4+TAMyhX3HINp7EogMzojya6V5tHY5LcimNThati4ezrb99ssPH9rMU1vbTEEYEwo/u9YXgD/hTJS72v3+85UUaiLRnO3oWjhunwgQg6iLRejyEYM4VKLVNwwUpxXblAemyRUqcAuTTGvJmRde0LdgFlOANiKFOrlmZQrQQLDdbRueO/0tiFUE0Ooqg6kNAxZE0BjGtrYeOnqLuyINo9rwO1HuOuA6EWkG5qqqRehcmrIN+wo/UQZyMcV8WhC9iUG5/fnw89TuKYhChXI1Oc3xChXBQc40uVJBaj8xiN7SMYi2bv8upilDAvl1sTCJdIZUOlNw2FIungUxtT6evT5IDEJV2d7aTSqj9BSJ9xhGteEni+kBEWl0lcOzwE9E5JsVl2yC0Oyj5XfwNNc0mRJP7O0lZkGAv/Gc2VbfBTZ2v83xvMKxUoVy/lptlJpz4T+L6WBPgslDFGm2o6vPQPWBLuffdppnQcSDZTG1dSeyn/eSCwxjIuBn15qsqoeAtwA/UdVTgQsqK9bEwcuOKeaTDuJiqo/527w6epNFM5hg4Km92GbaVWQWBDgppaXWgNxxoyOzIPqSaRKpTEGLBoJlMXX0Drcgan3+jj1aXQXhDYWq9WnleWxr6xkkj2FMFPzsWhERmQW8A7irwvJMOCbVRAjJQLZMPhLpTLaSuBReN9RSWTIdPcmiNRCQ2/m08EbY1VfcxTRghRTfTAdcTIViEE4MoFQW0/5DjjunUMEduDGIAIVyQxVp0JkQB7r6aaqLZuMo9TEnLuO3gHB7qykIY2LiZ9f6F5xMpk2q+pSILAJerqxYE4dQSJhSFys6EyKRyhAPaEEU6/WTSmfo7C+cVuvh56ndU0QFW21EvRbkxTdDz4VSrG14KVkAdrkpvnOaagt+JoiLyenkOsTFFNSC6O7PprhCbtddf1bENlMQxgTFT5D6VuDWnPebgbdWUqiJRlNdtGhH16B1EFDcgvDaYZdyMfmJQXQVmUc9eI3im2mvN486WsDF5DOLyVMQs4sqCH8uplQ6Q2dfalhL9KBzqQ90JZjaMGDReEqwO5Gmqa709dvaugmHhHRGTUEYEwo/QeqjReRP3lwHETlRRP6h8qJNHJrrY8VjEIGa9ZWeCeEpo1JZTL7SXPtSREJSsNLb74CegXqKkVkQXpHgEZNrCn4mt8dUMbzNeEqBIHWfTwXR2tXP9BwF4VkQvT4tiB1tPRw9cxIw0MrcMCYCfnatHwJfApIAqroGeFclhZpoODMhRqkOwt1gi82EyHZyHQ0Xk9uHqVDBnZfmWqo1RU+yeJDabyX17vZepk+KZ11b+YhHw6iWzojyalOGWhB1gV1MiWwNBORYED5bfm9r7eH42Y2ImIvJmFj42bXqVPXJIcesEU0OTbXRon/4weogXAuiyObT7qPVN/h7+u/qTxd0Lw1ao2Saa/EgdZAYRDH3kiOTP7dXtuNtAQvCj4spmc7Q3pPM1kA41/tLJAAnEL6/s58FU+torCn+/8Qwqg0/u9YBEVnMwMCgtwF7KirVBGNybbSgBZHJKKmM+q+DiHn+7SIWhI9pcpC7KRfJYupPFlcQPhr+wcBmW1vgyT8SEkT8WRBzmgq7l8BfbAUKT90LEqQ+OKSKGgYsCD9Dg7a7Ka7zp9bTWBsxBWFMKPyUdF6NM2/hWBHZhTMq9D0VlWqC0VQXpTeZpj+Vzj5xe3hB2aBB6mKVutlOrj5jEMUL5dIF4waD1yid5lobDRccqyoiRMMh+osoCFVld3sf5x0zo+i9/MZFCrmYgqS5tmT7MA3PYvJjQWQVRHMdk0tYmoZRbRRVEG7n1r9W1Qvc1tshVe0cG9EmDl4soKM3yYxJgzdbbxPz34tpIEOmEN6TcbGGduC/1UaxojS/aa5OC4nCigYgHg6RTBWOG7T3JOlNpku7mDyrpoQFkA3m15af5uoVyeXLYvLjotrW6owqPdIUhDEBKbpruT2XTnW/7zblkB+vlUO+DBVvc/Y7DyIeCREOSdEc+/beBJPikZJ9hCIhISSl01xLVS1DaQuiuz9VtFcTOGNHE+nC6/hJcYUBZVvKgth5sJf6WJjG2sFy1UT8b/Ct3V4fpnx1EP5cTJNqIjTVRZlcG7UsJmNC4cfF9IyI3IFTC9HtHVTV31ZMqgmGZ0Hki0N4PveoTwtCREpOlevoLV1F7a1Vai51d3/hKXDg353T0tU/yE+fj1gJC8JPkRz4j4tsa+3myKn1wzK0QiGhJupv1nY+C6IuW8xY2sW0rbWH+c11iIhrQVh+hzFx8KMgmoFW4PycY4ozDc5gIAiaz33gWRB+YxDgxCGKWRAdPhr1ecTCoZIupmLdRT0LotRmuv9QP4vdmc2FiEakqLLanbUgSgWpvcyq4jJtbe1h6azGvOfqYhFfMYgDXQmiYRnkzouGQ8TCIV8N+7a39XDcLKcGotG1IErNCDeMasFPJfUHx0KQiYwXBM1nQQQNUoPzhFrMgmjvTQ4LvBbCmd+cfy1VpbuEiykUEmLh0hPc9nf2c9biqUU/EwsXt2Z2t/dSEw3RXD/y4HsqnWFHWw+vX3ZE3vO10bA/F1NXP1Pr48M29Dofg536kml2tPVwyQmODJNroyTSGfqSmYKjWQ2jmvBTST1XRG4Tkf0isk9EfiMic8dCuInCZD8WhE8XE3jtpAtvPq1d/cOqgwtRbHPvTabJaOE+TB7xSHF3TF8y7QboCzfYA+fJu5g1s7u9j9lNtSWfrv24vXa195LKKAum1ec973cudWt3gmmThv+u62ORkoVyL+45RCqjnDCnCSj+/8QwqhE/u9ZPgDuA2cAc4E73mOEyqSaKyEABWy79ZbiYnIE0hZ/693T0lQzkejjT1/JvpKVafXtMqonQ2VdYYbV0uh1YG0vXLxSrg9jV3lsy/gADMYhiymbLASdctmBqAQUR9dey+4BrQQylzkfL77W7OgA4Ye5kwBSEMfHws2tNV9WfqGrKfd0ITK+wXBOKcEiYFI8UzWIKFIOIFbYg2roT9KcyzCrSqyiXYjEI7wl4UgkFMblEK5H9nX1A8Rbd4MeC6GX2ZB8KwkdmlddBdcG0/N30aqNh32mu+YLvdT6GBq3d2cHU+hiz3X+rIAri9md2sSNnjoRhjAd+K6mvEJGw+7oCJ2hdFBG5wXVLrStw/j0issZ9PSoiy3POXSwiL4nIRhH5ov8fZ/xw+jENb9jn+dz9prnCwFS5fOzpcDbjWT42UvBiEAUsiD5/FkRTifTMfdkZDsWVVixSWEH0p5yWFH4sIz8upi0HuqmPhQc12culNhamt0Rth6pyoKufaXnWqI+FSzbrW7urgxPmTs66zPwqiP2dffztr57lmrteKPo5w6g0fnatD+EMC9qL02Ljbe6xUtwIXFzk/BbgXFU9EbgGp1rbK877LvB6YClwuYgs9XG/caVQEdRADMJ/UNJJc82/+fjN9PGIh0MFW21s2OeUtZRy6zTVRWnvLdytdv8hR2nNbCxtQRRyMe11FZ+fn2tgDGoxCyJ/iqtHbbT0Bt+dSNOfygyqgfAolUjQm0jz8v4uTpgzOXvMr4J4fHMbAP/34r5s6q9hjAclFYSqblfVN6nqdFWdoaqXqeo2H9c9BLQVOf+oqh503z4OeIHv04GNqrpZVRPAL4FLS/4k44yziY5mmuvoWBCxSOEYxMMvtzC1PsaxR0wqukaxXlMA+zr7ibiDk8qVxW8NBPirg9ja2sPCAgFqcDb4Ui6mVrfNxtQ8FkRdrHgq8gt7DpHOaFkK4rFNrdl2IDc9XvJPzTAqRsk0VxH5CW6jvlxU1Y8V4ZcrgT+4388BduSc2wmcMYr3qgiNtVF2HRz+tOdVDgeLQYTpTqTy5svv7uglFg7lfarNRzwS4mDP8I00k1Ee2djKOUdNK9g/yWNyAeXnsf9QP9MnxUuuEytiQWxucYLKc6eUnsBTqpK6VIorQE0sXLIOYkebO5siT/C9Ph4uGoNYu7MdgBPnNmWPTarxpyCe2NzKWYunEgkJv3xqB3/z2qOKtj83jErhZ9e6C/i9+/oT0Ah0jZYAInIejoL4gncoz8cKlt+KyFUiskpEVrW0tIyWWIEp1PLbqxz2ZjL7oS4eQTV/r6A97X0cMbmm5GbsUcjvv35vJwe6+jlnybSSazTVxkikMgXTQvd39pXMYMrKUkBB/Hn9fuY11zKvubQFEQmHiISkYJC6VIorQF20tIJ4dodj4HpZSIOuj0WKVlKv3XWIaQ3xQW63YskMHvsO9bH5QDdnLZrK+89eQFt3gt+vsebJxvjgx8X0m5zXTTjxiGWjcXMRORH4EXCpqnqB753AvJyPzQV2F5HvelVdoaorpk8fv+Qqz8U0dMpZfxmFct5c6nw+7j0dvb4zmGBg+tpQHtnoKNNXHVX6d1aslQg4FkSpDCZwlGS+Vhtd/Ske2XiAi5Ye4bvCOB4JFZxRsdXLYCqQ4gpOkLonmS6advvM9naWzGjIW7Ve715faKrd2l3tnJgToPZoLNGw7/HNzp/BWYuncvbiqSyZ0cAvntxe8PO5ZDLKjx7ezM6Dlv1kjA7+d60BjgLmj/TGIjIfp13He1V1Q86pp4CjRGShiMRwptfdMdL7VZrJtVHSGR3mdsg26wsQpB5oBjf8CdUrJvNLIQvi4ZcPcNSMhqKjPT2yleIFAtX7O/t8KYhCFsSDL7WQSGW4aOnMkmt4FMvO2urVQBRIcQU4aV4TqvB/L+zLe15VeWZHOyfPa8p73rPy8nW57Umk2DgkQO1RqmHfY5taaayJcNysRkSE1y87gmd3tBedMOjx4IYW/t/vX+SWVTtLftYw/OCnkrpTRA55X3EK5b7g47qbgceAY0Rkp4hcKSIfE5GPuR/5J2Aq8D0ReVZEVgGoagr4BHAv8CJwi6o+X9ZPN4Z4LaWHprqWF6TOb0GkM8q+Q30BLYjhrTb6kmme3NLGOUeVdi/BQK+pfBZEfyrNwZ4kM324mKLhEMk8m/p9L+yluT7GigXNvuQBzzLK7yIqleIK8JpjZjB3Si0/fWxr3vPb23po605w8vwpec8XGuykqtz46FYyCifmcU2Vavn9+OZWTl84lbDrQjx9YTPpjPL0toMFr/G4/qHNwICCNIyR4qcXU/EUl8LXXV7i/IeBDxc4dzdwdzn3HS8aczJU5ubsKeUoiEIWxIGuflIZZdYILYhVWw/Sn8rwKp8Kwuscm29jy1ZR+7Qghg4MSqQy/Hn9fl6/7IjspuiHQq4zKJ3iCk484Iozj+Tf/rCel/Z2csyQTK6ntzsb8snzm/JeX5c7GtbtUZhMZ/in3z3PzU9u56KlM3n10cPdd5Nro2xqyR/C29PRy9bWHq4488jssVPmTyEcEp7a2pZ3PY+1Ozt4bHMrIRmoIjeMkVJw1xKRU4q9xlLIiYDnhukY8pSdSKcJhyTQ5pe1IIa4q7I1EAEsiHyppX9ev59oWDhjYfHmeh7Z9Mw8FsT+bJuN0goi7mYx5frtH9/cSmdfiouWFs44yrtWJJw3BqGqrN3VMWzDz8c7V8wjHgnxszxWxDPb26mPhTl6Zv516odYEAe7E7z3x09w85Pbufq8xVx3xal5W7wXsyAe3TgQf8jeJx5h2exGnthSMGMcgB8+vJmGeITLTp7DlgPdBWMjhhGEYhbEN4qcUwa3/z7sKZTjnkhlAjXqg8JjR4PWQIDzpJ3KKJmMEgoJiVSG25/dxQXHzSxZQe3hjTbNF4PwiuRKVVGD42JShVRGs1ld972wl7pY2Le7y8PpMTXcxfTSvk4OdCU4u0RnWYAp9THetHw2v316F5+/+NhBwehntrezfF5TQcVe5/7uVm07SHtPki/9dg272/v4r3cu580nF+5lObmusIJ4cEML0xriHHfE4Bblpy9s5qePbaMvmc6b7rqjrYffr93Dh1YuYE5TLb99ehctXf2+/k0MoxjFdq7vq+p5wJWqet6QlymHIQwEcvMoiADuJSA7wKegBeGzihpyxo66rp3/e3Efbd0J3nnavGKXDZEnTCQkeTe2IBaEJ4uXOZTJKPc9v49zj54eOM+/LhamLY9F88jLBwBY6SN9F+D9Zy+gN5nm+oc2ZY/1JtK8uOdQQfcSDFSN/+Pt67j8h4/T1Z/i5qvOLKocwHmQ6M+TMpzOKA+93MK5R08flsJ8+sKpJFIZ1uzsGLZeIpXh7371LNGw8MGVC1nozuTY0mJuJmPkFNu5vB5Ivx4LQSY6BS2IdHAFkQ2A5rEgaqNh38OCIHe4jrMp3/zkdmZPrvGV3urhTUPLF6Tef6ifcEjydjwdiudy8WIiz+1sZ39nPxcd7z97yeP0Bc2s3dlOW/dgq+YvGw+waHq970yvZXMm85ZT5nD9Q5vZuN9pPbJudwepjHLyvPwBaoBjj2jk/s++hl985Ayuu+IU7v7Uqzj1yMKf9/BiVUMzmdbsbKe9J8m5xwz/dzltgbPuk1sGt0BTVf7x9nWs2naQ/3jbcmY31bLIrf3Y2moKwhg5xXauVhG5H1goIncMfY2VgBOF2miYWDg0bBPtH4GLaWiGzJ6OXmY11QSaRuYpp/60M7zmkY0HePuKeYFiIlC4mnrfoT6mNcR8rTfUmrn3+X1EQsL5xwRXEBcuPYKMOvEUj0QqwxNb2nwV/+Xy5UuOozYa5h9uX0d7T4KfProVgJOKWBAAC6fVc/biaVy8bJZvd46n3IcGkh94qYWQwKvyyN5U57RDeWJLG6rKul0d/PLJ7Xz21jX8atUOPnHeEt64fDbgzPOOhUNsDhCozmSUHz+yJesuNAyPYk7ovwJOAf6X4vEIA/cpO49/OZnWwBZEPBIiJAybCbG7vc9XO+yha4FjQdy62smPf0cA95JHU220YJDa7+YYG2JB3PfCXs5cNNXXfO2hLJvTyBGNNfzxhb287VTHrfPsjnZ6Emnf7iWPaQ1xPn/xsfzD7es469o/05dKc+U5C/N2cR0py2Y3Eo+EuPyHj3PxsiP4/OuOZcG0eh7c0MLyeU1MKdBC5fSFzdyyagev/caD2c2/JhriHSvm8ukLj85+LhwS5k+tC+RiemZHO9fc9QJ/fGEvv/jwmb6r9I1XPgUVhNso73EROVtVx6+HxQTCyVAZWgeRDmxBiEjemRB7Onp5dQDXEAwoiO5Eilue2sGrjpruqyHeUJrqYtmU1lz2Hepj7hT/jQPB6dzal0yzuaWbD5y9ILAs4PyOLlg6g9+s3pUN3j6y8QAhgTMX+cvOyuXdp8/ngZf2k1H43OuO4bgCs6xHyqLpDTz0+fO48dGt/Pzxbaza+hjfv+JUntvZzqdee1TB684/dgY/e2wb0ybFuerVizh78TTmTqnNu5kvnFYfKNX1sU1O3ObxzW3c8JctfPhVi4L/YMYrEj91EKYcfJKvH1M5QWpwZx7nWBDJdIb9nf2BaiBgQEHc9vQu9h7q49q3nBBYFnCU38uujz6Xls7+gsVkQzl78VSmT4rziV88w2uPmwHAhQGqp4dy4dIj+Pnj2/nLxgO89riZ/GXjAU6c2xQoRuMRCgk/ev9pZcsShJmNNXzh4mN5y8lzeNf1j/Ou6x9D1SneK8RrjpnB+msu9hXMX+haJOmM+nL9PbqpleNmNTJ3Si3/fu9LvPro6QXTe43Di3JabRgFGBrIzWSUDfu6fLWzGMpQC2JHWw+qwWogYOCp/eePb2PJjAbOLVJsVYx8Qerd7b20didYPL1wz6NcZjTW8LMPnU5PIsVNT2xn+dzJgVJ2h3LmomYa4hHufX4vv316J8/uaA8cfxhPjpo5iZs+cgYN8QhT62N5W3Pk4jfTa+G0ehKpTDbrrRh9yTSrth1k5eKpXPuWE5gUj5QcVLS/s48/vZi/RYnxysIUxCgyuW7wJrp6+0F2tffyhhNnBV6rPh7hYE7bjj+s2wv4T9/08AYVdSfSfORVC8v2LzfVRensS5HODBRgPfyy/4Z/HsfNauQnHzyNSfFINnZQLvFImHOPmc4tq3by6Vue47hZk3j3GSNuEzamHHtEI3d+8hxu+sgZgRMHCuHNwfDjZnp620ESqQxnL5nKtIY47zljPo9sPMC+IgHr792/iSt/uio7atZ45VLQxSQi/0ORNtuq+jcVkWgCM7QR2++e3UVNNMQFxwV3o5y1eCo/fmQLu9ud7q23PbOL0xZMYV5z6XkJuXjDdaY1xLj0pDmB5fCYnJOe6QVSH3r5ADMb4xw9syHQWqce2cyqf7wgcGwmH+8780haOvt5/1kLeP2yIyZkgNXPDIwgLMpREMXacwD8ZdMBwiHhdLeq/tKT5/DtP2/kzud2F4xFeB1nH93YymUnO/+n/vXuF1kyo4F3rAieAGFUL8X+QlcBq4EanGyml93XSUDpae+HIU21MTr7U6TSGZLpDL9fs4cLlx7hu2I5l/eeeSSqys8f38bzuw+xcX9X9o8xCN5ksvedtWBEQ2eGFgKmM8ojLx/gVUdND5R26xGPhMu6bihnLJrKLR89i786cdaEVA6VYPqkOPWxsC8L4tFNrSyfO5kG9//o4ukNnDh3Mrc/uyvv59t7Eqzf68SiHnaLEvcf6uOHD2/mJ3/ZOjo/gFE1FMti+imAiHwAOE9Vk+7764D7xkS6CcbkWufX2dqd4IXdhzjYk+RSNz89KPOa67hw6UxufnI7h/qSRMPCX50Q3FW1dFYj//7WE7N58uUyuFttPWt3ddDRm/Td8M8YO0SEBdPqCzYF9OjsS7JmZwcff83iQccvPWkO19z1Ahv3d7FkxmDr8KmtThPDOU21PLKxBVXlnuf3ogrr9x6ivSeRbc1iTHz82PizgdyUhgb3mDGEE+ZORgTedt2jfPf+jUyujZY08YvxgbMXcrAnyc8f3855x8wo6w8vFBLecdo8amMjG1k5tKPrwxtaEAkWfzDGjlOPnMKTW9qGVePn8uSWNtIZHdQcEOCNy2cREsdFOpQnNrcSi4S46tWL2Heon00tXfx+zR5qo2FUnTWNVw5+FMS/Ac+IyI0iciPwNPCvFZVqgnLqkc3c8tGzCIuwattBLjnhiLJSXD3OXNTMsW5X0jeX4V4aTYa2Enn45QMsmz2ZZp+zsY2x5ZITZtGfynD/S/sLfubO53YzKR7hlCFpyjMm1bByyTR+9+zuYV1hn9zaxknzmjj/WCcl97dP7+LJrW18YOUC4pEQj282BfFKws/I0Z8AZwC3ua+zPPeTMZzTFjRz96dexVfeuJRPvfbo0hcUQUT49IVHc8r8Js47tnCO/FiQOzSosy/J09sPmnupijltQTPTGuLcvTb/POu27gR3r93LW0+dmzc2delJc9je1sPT29uzxzr7kqzb1cGZC5uZ11zHgql1/OjhLag6DzCnHjklG8DOx9PbD/KN+17ip49u5aENLdaSfALgZ6KcABcAy1X1d0BMRE6vuGQTmLpYhA+uXFhW/cNQLjr+CH778ZUjCjCPBrkWxAMvtZDK6IjcZ0ZlCYeEi5fN5M/r9+cdXXvrqh0k0pmCacGvO34m8UhokJtp9baDZJRsxtM5R00jkc5w1IwGjp45iTMXTeVFNw6RcpM0Nu7vRFX5yV+28I7rHuN//ryRr9zxPO+74Ul+4E7Ay0VVbaZ2FeHH//E94CzAmxDXCXy3YhIZVUkkHKIhHqG9J8nNT25n7pRaTg8wItQYey45YRZ9yQz3rx/cDCGTUX7x5HZOX9BcsGJ6Uk2UC5bO5K41e7Lt2Z/c0kYkJJxyZBMA5yyZnr0PwBkLm7NxiH+/9yWu/sXTXPDNhzjta//HP9/5Aq85ZgbP/dNFPPX3F3DR0pl8874NbNg3uDr/+oc2c87X7887xMkYe/woiDNU9WqgD0BVDwLmeD4MmVwb5dkdB3l0UyuXnz7f0kqrnDMWTmVaQ4y71w12Mz2y8QDbWnt4z5nFiwovO2kObd0JHnn5AIlUhj+9uJ8T5k7Ojlt9zTHTufKchdl1ls9rIh4J8c0/buD6hzbzzhXz+H+XLeO0Bc18+ZJjuf69pzK5Lsr0SXH+9S0n0FAT4TO3PJdVQI9tauXr96ynPhbmmrte4Lkd7aP/SzEC4UdBJEUkjFs0JyLTgfzDgI1XNE11UZ7e3k4kJLx9xciqoI3KEw4Jrzv+CP704j6+98BGNrd0ceuqHfzznc/TXB/j4mXFx7yee/R0muqi3P7sLv7x9nW8tK+TK89ZmD1fEw3zj29Ymu3mWxMNc8r8Kazf28lpC6ZwzWXLuOLMI/n+Fady1asXD3qgmNYQ51/fvIy1uzp49w8f5wcPbuKTNz/Dgmn13Pt3r2bGpBqu/sXTeTsIl0tfMs2Xb1vLQxusvZxf/CiIb+MEp2eIyNeAR/CRxSQiN4jIfhFZV+D8sSLymIj0i8hnh5zbKiJrReRZEVnlQ0ZjDPDiEBcunWnjLCcIH331YpbNnsy/3/MS53/jQT736zWowrVvOSE7TKoQsUiIS06YxR3P7c7OnXjDicUz3N+wfBaLp9fz3fecUjKD7+Jls/jyJcdysCfJtX9YT3d/iuuuOJW5U+r4zrtPZt+hPj5x89NZC2OkfP2e9fziie185GereKJIMN0YQPxkEojIscBrAQH+pKov+rjm1UAX8DNVXZbn/AzgSOAy4KCq/mfOua3AClU94O/HcFixYoWuWmX6pFJ8/KbV3L12Lz/70OkWoJ5gbG/t4c/r93H8nMmsOHKK7yr2VVvbeNt1j/G642fy/fecWjG34q72XtJpZf7UgbYjt6zawed/vYZ3nTaPa99ywogq7+9/aT8f/MlTvP3UuTy9/SD7D/Vz81VnsqxEg8TDARFZraor8p3zk8X0Y6BGVb+rqt9R1RdF5KulrlPVh4CCSdGqul9VnwJGz4Y0KsrSWY0sm9M4oTqmGg7zp9bxgZULOW1Bc6CNdsWCZn778bP51rtOrmjMaU5T7SDlAPCOFfP4xHlL+OVTO/jGfRuylsShviQ/eHATq7cd9LX2hn2dfO7W5zj2iElcc9kyfv7hM2isjfK5X68Z9Z/jlYafJkGvA04VkW+q6s/cY28CvloxqZx4x30iosAPVPX6Ct7L8Mknzj+Kq89bMio9lIyJw9BCurHkMxcdze6OXr5z/0bueG43f3XiLH711A7auhOEBP72gqO5+rwl2U64a3d28O/3ricSEpbNmczG/V38Yd1eJtVE+PblJ1MTDTNrci3vO+tIrv3DevZ29I1KOvorFT8KYj/wGuAmETkD+BSOq6mSrFTV3a4b6o8ist61SIYhIlcBVwHMnz+xWj1PREw5GGOJiPCNty/njSfO5j/ve4nvP7CJsxZN5VMXHMXNT27nm3/cwB3P7easRVNRlF88sZ3m+jhT62M8uKGF+niEvzl/CR9cuXDQONdzj5nOtX9Yz0MbWsoawXu44EdBiKoeAt7oupYeBCrquFPV3e7X/SJyG3A6kFdBuNbF9eDEICopl2EYY4+IcN6xMzj36Ons6+zjiMYaRIQzFjZz3jEzuHX1Dm57Zhdd/SnefcZ8vnDxsUyujdKbSCOSf9DSMTMnMbMxzoMvm4Iohh8FcYf3jap+1c0q+nSlBBKReiCkqp3u9xcB/1Kp+xmGMTEIhWTQBEIR4bKT53DZyXNIZ5SuvlS2qSRQtEGliPDqo6Zz3wv7SKUzREZhNskrET+9mL4y5P1dqnp+qetE5GbgMeAYEdkpIleKyMdE5GPu+SNEZCeOsvkH9zONwEzgERF5DngS+L2q3hP8RzMM43AhHJJBysEPrz56Oh29SZ7b2THo+KaWLl7cc8j3Ok9tbeOF3YfoT73yxuQUmyj3iKqeIyKdDJ4sJ4CqamOxhVX18hLn9wL5qq0OAcuLXWsYhjFSzlkyjZDAQxtaOPVIJxD/2KZWrvzpU/Qk0lx20mw+d/GxzGkqPDf9N6t38plbnwMgEhKufNVCvvT648ZE/rGgoAWhque4XyepamPOa1Ip5WAYhlHtTKmPsXxeEw9saKGzL8k96/bwgZ88yZymWj567iL+sG4vr/3GA/zv49vydp7duL+Tf7h9HacvaObbl5/M+cfO4AcPbmbNzvZhn73piW189tbnuPbuF7njud1lyduXTPO/j23l8usf5+nt/lJ8R0rBQjkRKdqJTVWrrvG7FcoZhhGE//rjBr71p5ez75fNaeRnHzqD5voYu9p7+dJvndYc5x87g89edAzHzZqEiNDRk+TtP3iU1q4Ed3/qVcxsrKGzL8l5//kAC6bWc+vHzspm/N353G4+efMzTKmL0t2fJpHO8LU3L+M9ZxzpW87HN7fyyZufoaWzPztG+Lr3nsq5o1CwWqxQrliQejWOaylfXqMC+SeaG4ZhTBCuOPNIMqpMqokwY1INFyydmZ3PPaeplhs/cBo/e2wr1/5hPX9ev58lMxpoiEdYu6uDjCo//eDpzGx06igm1UT57EXH8MXfruWuNXt44/LZbG7p4ou/WcMp85v41UfPIiTCh258iq/87nmWTG/gjEVTi4mX5bv3byQswi8+cgZLZjTw/hue4sM/fYpvvevkbDfdSuCr1cZEwSwIwzAqQWtXP3ev28tdz+0mmc5w9uJpXLh0JsvnNQ36XDqjvPF/HmHHwR6Wz21iW1s3XX0pfv83r2K2G8vo6E3y5u/+hfbeJHd+8pyiMQ6Arv4UJ//LfXxw5UK+fMlx2TWuvPEpnt3RzvfecwoXHV+88WIxilkQfnsxTQGOArIlh4UK18YTUxCGYYw3G/Z18q3/e5ld7b1096f4yhuP55wh0xc3tXRx6Xf+wpIZDdzy0bOIRUL8ZvVOHtvcyv+7bNmg2o171u3hYz9/ml9edSZn5lgcnX1Jrvjxk7y4+xDXv+9UXnNMeVMnR6QgROTDONXTc4FngTOBx/ykuo41piAMw5go3L12Dx+/6Wk+tHIhc6bUcs1dLwDwlpPn8I13LM/GMD5363Pc+/xeVv/jhUSH1Gt09CS5/IePs6ejl4e/cH7WPRaEcmMQHp8CTgMeV9Xz3M6u/xxYCsMwDCPLJSfM4gNnL+CGv2wB4PXLjuCoGQ18+88bOeaISXz03MVkMsr9L7Vw7jEzhikHgMl1UX7+4TPY2tpdlnIohZ8V+1S1T0QQkbiqrheRY0ZdEsMwjMOML11yLNtau5nVVMu/vOl4wiFh04Fu/u2e9UxriLNkRgMHuvo5/9jC2UrN9TGa6ysz5NOPgtgpIk3A7TiN8w4C5SXyGoZhGFnikTA/+eDpg47959uW096T4DO3PseyOY2EBM49urz4wkgpqSBU9c3ut18VkftxGvVZ6wvDMIwKUBsLc8MHTuNvf/ksf1i3lxVHTqmYhVAKX04rN4tpHtDpvpYBT1dQLsMwjMOWeCTMd959Cj98eDMnD0mlHUtKKggRuQb4ALAZ8IbDKlB1WUyGYRivFMIh4WPnLh5XGfxYEO8AFqtqotLCGIZhGNWDnybo64CmCsthGIZhVBl+LIhrgWdEZB3Q7x1U1TdVTCrDMAxj3PGjIH4KfB1Yy0AMwjAMw3iF40dBHFDVb1dcEsMwDKOq8KMgVovItTizqXNdTJbmahiG8QrGj4I42f16Zs4xS3M1DMN4hVNUQYhIGLhDVf9rjOQxDMMwqgQ/7b7vV9XzxkieESEiLcC2Mi+fBhwYRXHGiokqN0xc2Seq3DBxZZ+ockP1y36kqubtBuhHQXwNp//Sr4Bu7/grLQYhIqsK9USvZiaq3DBxZZ+ocsPElX2iyg0TW3Y/MYiz3a//knPMYhCGYRivcPx0c50Q7iXDMAxjdCnZakNEJovIN0Vklfv6hohMHgvhxpjrx1uAMpmocsPElX2iyg0TV/aJKjdMYNn9xCB+g9OP6afuofcCy1X1LRWWzTAMwxhH/CiIZ1X1pFLHDMMwjFcWfrq59orIOd4bEVkJ9FZOpLFFRC4WkZdEZKOIfHG85SmGiMwTkftF5EUReV5EPuUebxaRP4rIy+7XKeMtaz5EJCwiz4jIXe77iSJ3k4j8WkTWu7/7syaC7CLyd+7/k3UicrOI1FSr3CJyg4jsd5uCescKyioiX3L/Zl8SkdeNj9QF5f4P9//KGhG5zR3Z7J2rCrn94kdBfAz4rohsFZFtwHfcYxMetxDwu8DrgaXA5SKydHylKkoK+IyqHodT2X61K+8XgT+p6lHAn9z31cingBdz3k8Uub8F3KOqxwLLcX6GqpZdROYAfwOsUNVlQBh4F9Ur943AxUOO5ZXV/T//LuB495rvuX/L48GNDJf7j8AyVT0R2AB8CapObn+oqq8X0Ag0+v38RHgBZwH35rz/EvCl8ZYrgPy/Ay4EXgJmucdmAS+Nt2x5ZJ2L80d+PnCXe2wiyN0IbMF1x+Ycr2rZgTnADqAZJ1vxLuCiapYbWACsK/U7Hvp3CtwLnFUtcg8592bgpmqU28/Lz8jROPBW95cQERFPsfxLkcsmCt4fkcdO4IxxkiUQIrIAp0/WE8BMVd0DoKp7RGTGeMpWgP8GPg9Myjk2EeReBLQAPxGR5cBqHEuoqmVX1V0i8p/AdhyX8H2qep+IVLXcQygk6xzg8ZzP7XSPVSMfwikyhoklN+DPxfQ74FIc90Z3zuuVgOQ5VjxqXwWISAPwG+BvVfXQeMtTChF5A7BfVVePtyxlEAFOAb6vqifj/N+vFrdMQVx//aXAQmA2UC8iV4yvVKPGhPi7FZG/x9k3b/IO5flY1cmdi59K6rmqOtTH9kphJzAv5/1cYPc4yeILEYniKIebVPW37uF9IjLLfcqaBewfPwnzshJ4k4hcAtQAjSLyc6pfbnD+j+xU1Sfc97/GURDVLvsFwBZVbQEQkd/idEWodrlzKSRr1f/disj7gTcAr1XXn8QEkHsofiyIR0XkhIpLMj48BRwlIgtFJIYTQLpjnGUqiDj+vR8DL6rqN3NO3QG83/3+/ThWX9Wgql9S1bmqugDnd/xnVb2CKpcbQFX3AjtE5Bj30GuBF6h+2bcDZ4pInfv/5rU4wfVqlzuXQrLeAbxLROIishA4CnhyHOTLi4hcDHwBeJOq9uScqmq58+IjAPMCkMAJGK3BGT26ZryDJ6P1Ai7ByTTYBPz9eMtTQtZzcEzSNcCz7usSYCpOAPhl92vzeMta5Gd4DQNB6gkhN3ASsMr9vd8OTJkIsgP/DKzHKXT9XyBerXIDNwN7gCTOk/aVxWQF/t79m30JeH2Vyb0RJ7bp/Y1eV21y+335KZQ7Mt9xVS23rbZhGIYxASipIAzDMIzDEz8xCMMwDOMwxBSEYRiGkRdTEIZhGEZeTEEYhmEYeTEFYRiGYeTFFIRxWOK28P54zvvZIvLrCt3rMhH5p4DX3J3bJtrH598gIv8cWDjDKIKluRqHJW6zw7vUaYVd6Xs9ilNVe6CC9xDgaWClDq7eNYyyMQvCOFz5N2CxiDzrDnhZ4A19EZEPiMjtInKniGwRkU+IyKfFGXb0uIg0u59bLCL3iMhqEXlYRI4dehMRORro95SDiNwoIt8XZ/DTZhE51x0686KI3Jhz3VYRmebK9aKI/FCc4T/3iUjt0Puo86T3AE7/H8MYFUxBGIcrXwQ2qepJqvq5POeXAe8GTge+BvSo0831MeB97meuBz6pqqcCnwW+l2edlThP9rlMwZmL8XfAncB/4QyROUFETsqzxlHAd1X1eKAdp/1+PlYBrypwzjAC46ebq2Ecjtyvqp1Ap4h04Gzk4PQiO9FtuX42cKs3IwWn19FQZuHMk8jlTlVVEVkL7FPVtQAi8jzO3JVnh3x+i6p6x1a7n8nHfpzW3oYxKpiCMIz89Od8n8l5n8H5uwkB7ap6Uol1eoHJBdbOXTd37WKypIFhLiaXGl5B8+KN8cdcTMbhSieDp9sFQp1BTVtE5O3gBIndiXNDeRFYUu59AnI0TudWwxgVTEEYhyWq2gr8RUTWich/lLnMe4ArReQ54HmcCW5DeQg4WXL8UKOFiHxMRD6Wc+g84PejfR/j8MXSXA2jwojIt3DiDv9XwXvMBH6hqq+t1D2Mww+zIAyj8vwrUFfhe8wHPlPhexiHGWZBGIZhGHkxC8IwDMPIiykIwzAMIy+mIAzDMIy8mIIwDMMw8mIKwjAMw8jL/wewpdu8ZSEBngAAAABJRU5ErkJggg==\n",
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
    "# Print the keys of the MATLAB dictionary\n",
    "print(mat.keys())\n",
    "\n",
    "# Print the type of the value corresponding to the key 'CYratioCyt'\n",
    "print(type(mat['CYratioCyt']))\n",
    "\n",
    "# Print the shape of the value corresponding to the key 'CYratioCyt'\n",
    "print(np.shape(mat['CYratioCyt']))\n",
    "\n",
    "# Subset the array and plot it\n",
    "data = mat['CYratioCyt'][25, 5:]\n",
    "fig = plt.figure()\n",
    "plt.plot(data)\n",
    "plt.xlabel('time (min.)')\n",
    "plt.ylabel('normalized fluorescence (measure of expression)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "efd31447",
   "metadata": {},
   "source": [
    "Great job!"
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
