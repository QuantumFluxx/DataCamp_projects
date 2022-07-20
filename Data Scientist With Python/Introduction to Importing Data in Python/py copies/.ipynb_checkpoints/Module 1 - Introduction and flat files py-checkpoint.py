{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "74b34499",
   "metadata": {},
   "source": [
    "# Introduction to Importing Data in Python\n",
    "\n",
    "## Introduction and flat files\n",
    "\n",
    "## Exploring your working directory\n",
    "In order to import data into Python, you should first have an idea of what files are in your working directory.\n",
    "\n",
    "IPython, which is running on DataCamp's servers, has a bunch of cool commands, including its magic commands. For example, starting a line with ! gives you complete system shell access. This means that the IPython magic command ! ls will display the contents of your current directory. Your task is to use the IPython magic command ! ls to check out the contents of your current directory and answer the following question: which of the following files is in your working directory?\n",
    "\n",
    "\n",
    "* huck_finn.txt\n",
    "\n",
    "* titanic.csv\n",
    "\n",
    "* **moby_dick.txt**\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Importing entire text files\n",
    "In this exercise, you'll be working with the file moby_dick.txt. It is a text file that contains the opening sentences of Moby Dick, one of the great American novels! Here you'll get experience opening a text file, printing its contents to the shell and, finally, closing it.\n",
    "\n",
    "* Open the file `moby_dick.txt` as read-only and store it in the variable file. Make sure to pass the filename enclosed in quotation marks ''.\n",
    "* Print the contents of the file to the shell using the `print()` function. As Hugo showed in the video, you'll need to apply the method `read()` to the object file.\n",
    "* Check whether the file is closed by executing `print(file.closed)`.\n",
    "* Close the file using the `close()` method.\n",
    "* Check again that the file is closed as you did above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c849850c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time\tPercent\n",
      "99\t0.067\n",
      "99\t0.133\n",
      "99\t0.067\n",
      "99\t0\n",
      "99\t0\n",
      "0\t0.5\n",
      "0\t0.467\n",
      "0\t0.857\n",
      "0\t0.5\n",
      "0\t0.357\n",
      "0\t0.533\n",
      "5\t0.467\n",
      "5\t0.467\n",
      "5\t0.125\n",
      "5\t0.4\n",
      "5\t0.214\n",
      "5\t0.4\n",
      "10\t0.067\n",
      "10\t0.067\n",
      "10\t0.333\n",
      "10\t0.333\n",
      "10\t0.133\n",
      "10\t0.133\n",
      "15\t0.267\n",
      "15\t0.286\n",
      "15\t0.333\n",
      "15\t0.214\n",
      "15\t0\n",
      "15\t0\n",
      "20\t0.267\n",
      "20\t0.2\n",
      "20\t0.267\n",
      "20\t0.437\n",
      "20\t0.077\n",
      "20\t0.067\n",
      "25\t0.133\n",
      "25\t0.267\n",
      "25\t0.412\n",
      "25\t0\n",
      "25\t0.067\n",
      "25\t0.133\n",
      "30\t0\n",
      "30\t0.071\n",
      "30\t0\n",
      "30\t0.067\n",
      "30\t0.067\n",
      "30\t0.133\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Open a file: file\n",
    "file = open('datasets/seaslugs.txt', mode='r')\n",
    "\n",
    "# Print it\n",
    "print(file.read())\n",
    "\n",
    "# Check whether file is closed\n",
    "print(file.closed)\n",
    "\n",
    "# Close file\n",
    "file.close()\n",
    "\n",
    "# Check whether file is closed\n",
    "print(file.closed)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f95c6279",
   "metadata": {},
   "source": [
    "Good job!\n",
    "\n",
    "## Importing text files line by line\n",
    "For large files, we may not want to print all of their content to the shell: you may wish to print only the first few lines. Enter the readline() method, which allows you to do this. When a file called file is open, you can print out the first line by executing file.readline(). If you execute the same command again, the second line will print, and so on.\n",
    "\n",
    "In the introductory video, Hugo also introduced the concept of a context manager. He showed that you can bind a variable file by using a context manager construct:\n",
    "```python\n",
    "with open('huck_finn.txt') as file:\n",
    "```\n",
    "While still within this construct, the variable file will be bound to `open('huck_finn.txt')`; thus, to print the file to the shell, all the code you need to execute is:\n",
    "```python\n",
    "with open('huck_finn.txt') as file:\n",
    "    print(file.readline())\n",
    "```\n",
    "You'll now use these tools to print the first few lines of `moby_dick.txt`!\n",
    "\n",
    "* Open `moby_dick.txt` using the with context manager and the variable file.\n",
    "* Print the first three lines of the file to the shell by using `readline()` three times within the context manager."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e9a360fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time\tPercent\n",
      "\n",
      "99\t0.067\n",
      "\n",
      "99\t0.133\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Read & print the first 3 lines\n",
    "with open('datasets/seaslugs.txt') as file:\n",
    "    print(file.readline())\n",
    "    print(file.readline())\n",
    "    print(file.readline())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9856bc68",
   "metadata": {},
   "source": [
    "Great work!\n",
    "\n",
    "## Pop quiz: examples of flat files\n",
    "You're now well-versed in importing text files and you're about to become a wiz at importing flat files. But can you remember exactly what a flat file is? Test your knowledge by answering the following question: which of these file types below is NOT an example of a flat file?\n",
    "\n",
    "\n",
    "* A .csv file.\n",
    "\n",
    "* A tab-delimited .txt.\n",
    "\n",
    "* **A relational database (e.g. PostgreSQL).**\n",
    "\n",
    "That's correct.\n",
    "\n",
    "## Pop quiz: what exactly are flat files?\n",
    "Which of the following statements about flat files is incorrect?\n",
    "\n",
    "\n",
    "* Flat files consist of rows and each row is called a record.\n",
    "\n",
    "* **Flat files consist of multiple tables with structured relationships between the tables.**\n",
    "\n",
    "* A record in a flat file is composed of fields or attributes, each of which contains at most one item of information.\n",
    "\n",
    "* Flat files are pervasive in data science.\n",
    "\n",
    "Indeed, this is not flat at all!\"\n",
    "\n",
    "## Why we like flat files and the Zen of Python\n",
    "In PythonLand, there are currently hundreds of Python Enhancement Proposals, commonly referred to as PEPs. PEP8, for example, is a standard style guide for Python, written by our sensei Guido van Rossum himself. It is the basis for how we here at DataCamp ask our instructors to style their code. Another one of my favorites is PEP20, commonly called the Zen of Python. Its abstract is as follows:\n",
    "```\n",
    "Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding principles for Python's design into 20 aphorisms, only 19 of which have been written down.\n",
    "```\n",
    "If you don't know what the acronym `BDFL` stands for, I suggest that you look here. You can print the Zen of Python in your shell by typing import this into it! You're going to do this now and the 5th aphorism (line) will say something of particular interest.\n",
    "\n",
    "The question you need to answer is: what is the 5th aphorism of the Zen of Python?\n",
    "\n",
    "\n",
    "* **Flat is better than nested.**\n",
    "\n",
    "* Flat files are essential for data science.\n",
    "\n",
    "* The world is representable as a flat file.\n",
    "\n",
    "* Flatness is in the eye of the beholder.\n",
    "\n",
    "Yes!\n",
    "\n",
    "## Using NumPy to import flat files\n",
    "In this exercise, you're now going to load the MNIST digit recognition dataset using the numpy function loadtxt() and see just how easy it can be:\n",
    "\n",
    "* The first argument will be the filename.\n",
    "* The second will be the delimiter which, in this case, is a comma.\n",
    "\n",
    "You can find more information about the MNIST dataset here on the webpage of Yann LeCun, who is currently Director of AI Research at Facebook and Founding Director of the NYU Center for Data Science, among many other things.\n",
    "\n",
    "* Fill in the arguments of `np.loadtxt()` by passing file and a comma ',' for the delimiter.\n",
    "* Fill in the argument of `print()` to print the type of the object digits. Use the function `type()`.\n",
    "* Execute the rest of the code to visualize one of the rows of the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d3b20d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import package\n",
    "import numpy as np\n",
    "\n",
    "# Assign filename to variable: file\n",
    "file = 'digits.csv'\n",
    "\n",
    "# Load file as array: digits\n",
    "digits = np.loadtxt(file, delimiter=',')\n",
    "\n",
    "# Print datatype of digits\n",
    "print(type(digits))\n",
    "\n",
    "# Select and reshape a row\n",
    "im = digits[21, 1:]\n",
    "im_sq = np.reshape(im, (28, 28))\n",
    "\n",
    "# Plot reshaped data (matplotlib.pyplot already loaded as plt)\n",
    "plt.imshow(im_sq, cmap='Greys', interpolation='nearest')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5f695ad",
   "metadata": {},
   "source": [
    "Nice, that was a challenging one.\n",
    "\n",
    "## Customizing your NumPy import\n",
    "What if there are rows, such as a header, that you don't want to import? What if your file has a delimiter other than a comma? What if you only wish to import particular columns?\n",
    "\n",
    "There are a number of arguments that `np.loadtxt()` takes that you'll find useful:\n",
    "\n",
    "* delimiter changes the delimiter that `loadtxt()` is expecting.\n",
    "   + You can use ',' for comma-delimited.\n",
    "   + You can use '\\t' for tab-delimited.\n",
    "* skiprows allows you to specify how many rows (not indices) you wish to skip\n",
    "* usecols takes a list of the indices of the columns you wish to keep.\n",
    "\n",
    "The file that you'll be importing, `digits_header.txt`, has a header and is tab-delimited.\n",
    "\n",
    "* Complete the arguments of `np.loadtxt()`: the file you're importing is tab-delimited, you want to skip the first row and you only want to import the first and third columns.\n",
    "* Complete the argument of the `print()` call in order to print the entire array that you just imported."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55f86460",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import numpy\n",
    "import numpy as np\n",
    "\n",
    "# Assign the filename: file\n",
    "file = 'digits_header.txt'\n",
    "\n",
    "# Load the data: data\n",
    "data = np.loadtxt(file, delimiter='\\t', skiprows=1, usecols=[0, 2])\n",
    "\n",
    "# Print data\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f7a42e0",
   "metadata": {},
   "source": [
    "Good job!\n",
    "\n",
    "## Importing different datatypes\n",
    "The file `seaslug.txt`\n",
    "\n",
    "* has a text header, consisting of strings\n",
    "* is tab-delimited.\n",
    "\n",
    "These data consists of percentage of sea slug larvae that had metamorphosed in a given time period. Read more here.\n",
    "\n",
    "Due to the header, if you tried to import it as-is using `np.loadtxt()`, Python would throw you a ValueError and tell you that it could not convert string to float. There are two ways to deal with this: firstly, you can set the data type argument dtype equal to str (for string).\n",
    "\n",
    "Alternatively, you can skip the first row as we have seen before, using the skiprows argument.\n",
    "\n",
    "* Complete the first call to `np.loadtxt()` by passing file as the first argument.\n",
    "* Execute `print(data[0])` to print the first element of data.\n",
    "* Complete the second call to `np.loadtxt()`. The file you're importing is tab-delimited, the datatype is float, and you want to skip the first row.\n",
    "* Print the 10th element of data_float by completing the `print()` command. Be guided by the previous `print()` call.\n",
    "* Execute the rest of the code to visualize the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "956b2919",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Time' 'Percent']\n",
      "[0.    0.357]\n"
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
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Assign filename: file\n",
    "file = 'datasets/seaslugs.txt'\n",
    "\n",
    "# Import file: data\n",
    "data = np.loadtxt(file, delimiter='\\t', dtype=str)\n",
    "\n",
    "# Print the first element of data\n",
    "print(data[0])\n",
    "\n",
    "# Import data as floats and skip the first row: data_float\n",
    "data_float = np.loadtxt(file, delimiter='\\t', dtype=float, skiprows=1)\n",
    "\n",
    "# Print the 10th element of data_float\n",
    "print(data_float[9])\n",
    "\n",
    "# Plot a scatterplot of the data\n",
    "plt.scatter(data_float[:, 0], data_float[:, 1])\n",
    "plt.xlabel('time (min.)')\n",
    "plt.ylabel('percentage of larvae')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89350580",
   "metadata": {},
   "source": [
    "Nice!\n",
    "\n",
    "## Working with mixed datatypes (1)\n",
    "Much of the time you will need to import datasets which have different datatypes in different columns; one column may contain strings and another floats, for example. The function `np.loadtxt()` will freak at this. There is another function, `np.genfromtxt()`, which can handle such structures. If we pass dtype=None to it, it will figure out what types each column should be.\n",
    "\n",
    "Import `'titanic.csv'` using the function `np.genfromtxt()` as follows:\n",
    "```\n",
    "data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)\n",
    "```\n",
    "Here, the first argument is the filename, the second specifies the delimiter , and the third argument names tells us there is a header. Because the data are of different types, data is an object called a structured array. Because numpy arrays have to contain elements that are all the same type, the structured array solves this by being a 1D array, where each element of the array is a row of the flat file imported. You can test this by checking out the array's shape in the shell by executing np.shape(data).\n",
    "\n",
    "Accessing rows and columns of structured arrays is super-intuitive: to get the ith row, merely execute data[i] and to get the column with name 'Fare', execute `data['Fare']`.\n",
    "\n",
    "After importing the Titanic data as a structured array (as per the instructions above), print the entire column with the name Survived to the shell. What are the last 4 values of this column?\n",
    "\n",
    "\n",
    "* 1,0,0,1.\n",
    "\n",
    "* 1,2,0,0.\n",
    "\n",
    "* **1,0,1,0.**\n",
    "\n",
    "* 0,1,1,1.\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Working with mixed datatypes (2)\n",
    "You have just used `np.genfromtxt()` to import data containing mixed datatypes. There is also another function `np.recfromcsv()` that behaves similarly to `np.genfromtxt()`, except that its default dtype is None. In this exercise, you'll practice using this to achieve the same result.\n",
    "\n",
    "* Import `titanic.csv` using the function `np.recfromcsv()` and assign it to the variable, d. You'll only need to pass file to it because it has the defaults delimiter=',' and names=True in addition to `dtype=None!`\n",
    "* Run the remaining code to print the first three entries of the resulting array d."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "69602437",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, 0, 3, b'male', 22., 1, 0, b'A/5 21171',  7.25  , b'', b'S')\n",
      " (2, 1, 1, b'female', 38., 1, 0, b'PC 17599', 71.2833, b'C85', b'C')\n",
      " (3, 1, 3, b'female', 26., 0, 0, b'STON/O2. 3101282',  7.925 , b'', b'S')]\n"
     ]
    }
   ],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "# Assign the filename: file\n",
    "file = 'datasets/titanic.csv'\n",
    "\n",
    "# Import file using np.recfromcsv: d\n",
    "d = np.recfromcsv(file)\n",
    "\n",
    "# Print out first three entries of d\n",
    "print(d[:3])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa8a2484",
   "metadata": {},
   "source": [
    "Good job!\n",
    "\n",
    "## Using pandas to import flat files as DataFrames (1)\n",
    "In the last exercise, you were able to import flat files containing columns with different datatypes as numpy arrays. However, the DataFrame object in pandas is a more appropriate structure in which to store such data and, thankfully, we can easily import files of mixed data types as DataFrames using the pandas functions `read_csv()` and `read_table()`.\n",
    "\n",
    "* Import the `pandas` package using the alias pd.\n",
    "* Read `titanic.csv` into a DataFrame called df. The file name is already stored in the file object.\n",
    "* In a `print()` call, view the head of the DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e72d172a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   PassengerId  Survived  Pclass     Sex   Age  SibSp  Parch  \\\n",
      "0            1         0       3    male  22.0      1      0   \n",
      "1            2         1       1  female  38.0      1      0   \n",
      "2            3         1       3  female  26.0      0      0   \n",
      "3            4         1       1  female  35.0      1      0   \n",
      "4            5         0       3    male  35.0      0      0   \n",
      "\n",
      "             Ticket     Fare Cabin Embarked  \n",
      "0         A/5 21171   7.2500   NaN        S  \n",
      "1          PC 17599  71.2833   C85        C  \n",
      "2  STON/O2. 3101282   7.9250   NaN        S  \n",
      "3            113803  53.1000  C123        S  \n",
      "4            373450   8.0500   NaN        S  \n"
     ]
    }
   ],
   "source": [
    "# Import pandas\n",
    "import pandas as pd\n",
    "\n",
    "# Assign the filename: file\n",
    "file = 'datasets/titanic.csv'\n",
    "\n",
    "# Read the file into a DataFrame: df\n",
    "df = pd.read_csv(file)\n",
    "\n",
    "# View the head of the DataFrame\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d65d2231",
   "metadata": {},
   "source": [
    "Good job!\n",
    "\n",
    "## Using pandas to import flat files as DataFrames (2)\n",
    "In the last exercise, you were able to import flat files into a pandas DataFrame. As a bonus, it is then straightforward to retrieve the corresponding numpy array using the attribute values. You'll now have a chance to do this using the MNIST dataset, which is available as `digits.csv`.\n",
    "\n",
    "* Import the first 5 rows of the file into a DataFrame using the function `pd.read_csv()` and assign the result to data. You'll need to use the arguments nrows and header (there is no header in this file).\n",
    "* Build a numpy array from the resulting DataFrame in data and assign to `data_array`.\n",
    "* Execute `print(type(data_array))` to print the datatype of `data_array`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fe382d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Assign the filename: file\n",
    "file = 'digits.csv'\n",
    "\n",
    "# Read the first 5 rows of the file into a DataFrame: data\n",
    "data = pd.read_csv(file, nrows=5, header=None)\n",
    "\n",
    "# Build a numpy array from the DataFrame: data_array\n",
    "data_array = data.values\n",
    "\n",
    "# Print the datatype of data_array to the shell\n",
    "print(type(data_array))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29d6ffe7",
   "metadata": {},
   "source": [
    "Good job!\n",
    "\n",
    "## Customizing your pandas import\n",
    "The pandas package is also great at dealing with many of the issues you will encounter when importing data as a data scientist, such as comments occurring in flat files, empty lines and missing values. Note that missing values are also commonly referred to as NA or NaN. To wrap up this chapter, you're now going to import a slightly corrupted copy of the Titanic dataset `titanic_corrupt.txt`, which\n",
    "\n",
    "* contains comments after the character '#'\n",
    "* is tab-delimited.\n",
    "---------\n",
    "* Complete the sep (the pandas version of delim), comment and na_values arguments of `pd.read_csv()`. comment takes characters that comments occur after in the file, which in this case is '#'. na_values takes a list of strings to recognize as NA/NaN, in this case the string 'Nothing'.\n",
    "* Execute the rest of the code to print the head of the resulting DataFrame and plot the histogram of the 'Age' of passengers aboard the Titanic."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9960b540",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import matplotlib.pyplot as plt\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Assign filename: file\n",
    "file = 'titanic_corrupt.txt'\n",
    "\n",
    "# Import file: data\n",
    "data = pd.read_csv(file, sep='\\t', comment='#', na_values=['Nothing'])\n",
    "\n",
    "# Print the head of the DataFrame\n",
    "print(data.head())\n",
    "\n",
    "# Plot 'Age' variable in a histogram\n",
    "pd.DataFrame.hist(data[['Age']])\n",
    "plt.xlabel('Age (years)')\n",
    "plt.ylabel('count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a6f550d",
   "metadata": {},
   "source": [
    "Good job!"
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
