{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fcde6a68",
   "metadata": {},
   "source": [
    "# Writing Functions in Python\n",
    "\n",
    "## Best Practices\n",
    "\n",
    "## Crafting a docstring\n",
    "You've decided to write the world's greatest open-source natural language processing Python package. It will revolutionize working with free-form text, the way numpy did for arrays, pandas did for tabular data, and scikit-learn did for machine learning.\n",
    "\n",
    "The first function you write is `count_letter()`. It takes a string and a single letter and returns the number of times the letter appears in the string. You want the users of your open-source package to be able to understand how this function works easily, so you will need to give it a docstring. Build up a Google Style docstring for this function by following these steps.\n",
    "\n",
    "\n",
    "* Copy the following string and add it as the docstring for the function: Count the number of times `letter` appears in `content`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f065fb50",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add a docstring to count_letter()\n",
    "def count_letter(content, letter):\n",
    "    '''\n",
    "    Count the number of times `letter` appears in `content`\n",
    "    '''\n",
    "    if (not isinstance(letter, str)) or len(letter) != 1:\n",
    "        raise ValueError('`letter` must be a single character string.')\n",
    "    return len([char for char in content if char == letter])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0132e5b",
   "metadata": {},
   "source": [
    "* Now add the arguments section, using the Google style for docstrings. Use str to indicate a string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "32312a04",
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_letter(content, letter):\n",
    "    \"\"\"Count the number of times `letter` appears in `content`.\n",
    "\n",
    "    # Add a Google-style arguments section\n",
    "    Args:\n",
    "      content (str): The string to search.\n",
    "      letter (str): The letter to search for.\n",
    "    \"\"\"\n",
    "    if (not isinstance(letter, str)) or len(letter) != 1:\n",
    "        raise ValueError('`letter` must be a single character string.')\n",
    "    return len([char for char in content if char == letter])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c099d9a7",
   "metadata": {},
   "source": [
    "* Add a returns section that informs the user the return value is an int."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fded1989",
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_letter(content, letter):\n",
    "    \"\"\"Count the number of times `letter` appears in `content`.\n",
    "\n",
    "    Args:\n",
    "      content (str): The string to search.\n",
    "      letter (str): The letter to search for.\n",
    "\n",
    "    # Add a returns section\n",
    "    Returns:\n",
    "      int\n",
    "    \"\"\"\n",
    "    if (not isinstance(letter, str)) or len(letter) != 1:\n",
    "        raise ValueError('\"letter\" must be a single character string.')\n",
    "    return len([char for char in content if char == letter])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47ab8eaf",
   "metadata": {},
   "source": [
    "* Finally, add some information about the ValueError that gets raised when the arguments aren't correct."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ef7eb2f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_letter(content, letter):\n",
    "    \"\"\"Count the number of times `letter` appears in `content`.\n",
    "\n",
    "    Args:\n",
    "        content (str): The string to search.\n",
    "        letter (str): The letter to search for.\n",
    "\n",
    "    Returns:\n",
    "        int\n",
    "\n",
    "    # Add a section detailing what errors might be raised\n",
    "    Raises:\n",
    "        ValueError: If `letter` is not a one-character string.\n",
    "    \"\"\"\n",
    "    if (not isinstance(letter, str)) or len(letter) != 1:\n",
    "        raise ValueError('`letter` must be a single character string.')\n",
    "    return len([char for char in content if char == letter])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe7fe683",
   "metadata": {},
   "source": [
    "What a delightful docstring! While it does require a bit more typing, the information presented here will make it very easy for others to use this code in the future. Remember that even though computers execute it, code is actually written for humans to read (otherwise you'd just be writing the 1s and 0s that the computer operates on).\n",
    "\n",
    "## Retrieving docstrings\n",
    "You and a group of friends are working on building an amazing new Python IDE (integrated development environment -- like PyCharm, Spyder, Eclipse, Visual Studio, etc.). The team wants to add a feature that displays a tooltip with a function's docstring whenever the user starts typing the function name. That way, the user doesn't have to go elsewhere to look up the documentation for the function they are trying to use. You've been asked to complete the `build_tooltip()` function that retrieves a docstring from an arbitrary function.\n",
    "\n",
    "You will be reusing the `count_letter()` function that you developed in the last exercise to show that we can properly extract its docstring.\n",
    "\n",
    "* Begin by getting the docstring for the function `count_letter()`. Use an attribute of the `count_letter()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fe587423",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "############################\n",
      "Count the number of times `letter` appears in `content`.\n",
      "\n",
      "    Args:\n",
      "        content (str): The string to search.\n",
      "        letter (str): The letter to search for.\n",
      "\n",
      "    Returns:\n",
      "        int\n",
      "\n",
      "    # Add a section detailing what errors might be raised\n",
      "    Raises:\n",
      "        ValueError: If `letter` is not a one-character string.\n",
      "    \n",
      "############################\n"
     ]
    }
   ],
   "source": [
    "# Get the \"count_letter\" docstring by using an attribute of the function\n",
    "docstring = count_letter.__doc__\n",
    "\n",
    "border = '#' * 28\n",
    "print('{}\\n{}\\n{}'.format(border, docstring, border))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe55169a",
   "metadata": {},
   "source": [
    "* Now use a function from the inspect module to get a better-formatted version of `count_letter()'s` docstring."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "711c3295",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "############################\n",
      "Count the number of times `letter` appears in `content`.\n",
      "\n",
      "Args:\n",
      "    content (str): The string to search.\n",
      "    letter (str): The letter to search for.\n",
      "\n",
      "Returns:\n",
      "    int\n",
      "\n",
      "# Add a section detailing what errors might be raised\n",
      "Raises:\n",
      "    ValueError: If `letter` is not a one-character string.\n",
      "############################\n"
     ]
    }
   ],
   "source": [
    "import inspect\n",
    "\n",
    "# Inspect the count_letter() function to get its docstring\n",
    "docstring = inspect.getdoc(count_letter)\n",
    "\n",
    "border = '#' * 28\n",
    "print('{}\\n{}\\n{}'.format(border, docstring, border))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f564532",
   "metadata": {},
   "source": [
    "* Now create a `build_tooltip()` function that can extract the docstring from any function that we pass to it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "85730bdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "############################\n",
      "Count the number of times `letter` appears in `content`.\n",
      "\n",
      "Args:\n",
      "    content (str): The string to search.\n",
      "    letter (str): The letter to search for.\n",
      "\n",
      "Returns:\n",
      "    int\n",
      "\n",
      "# Add a section detailing what errors might be raised\n",
      "Raises:\n",
      "    ValueError: If `letter` is not a one-character string.\n",
      "############################\n",
      "############################\n",
      "range(stop) -> range object\n",
      "range(start, stop[, step]) -> range object\n",
      "\n",
      "Return an object that produces a sequence of integers from start (inclusive)\n",
      "to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.\n",
      "start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.\n",
      "These are exactly the valid indices for a list of 4 elements.\n",
      "When step is given, it specifies the increment (or decrement).\n",
      "############################\n",
      "############################\n",
      "print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n",
      "\n",
      "Prints the values to a stream, or to sys.stdout by default.\n",
      "Optional keyword arguments:\n",
      "file:  a file-like object (stream); defaults to the current sys.stdout.\n",
      "sep:   string inserted between values, default a space.\n",
      "end:   string appended after the last value, default a newline.\n",
      "flush: whether to forcibly flush the stream.\n",
      "############################\n"
     ]
    }
   ],
   "source": [
    "import inspect\n",
    "\n",
    "def build_tooltip(function):\n",
    "    \"\"\"Create a tooltip for any function that shows the\n",
    "    function's docstring.\n",
    "\n",
    "    Args:\n",
    "        function (callable): The function we want a tooltip for.\n",
    "\n",
    "    Returns:\n",
    "        str\n",
    "    \"\"\"\n",
    "    # Get the docstring for the \"function\" argument by using inspect\n",
    "    docstring = inspect.getdoc(function)\n",
    "    border = '#' * 28\n",
    "    return '{}\\n{}\\n{}'.format(border, docstring, border)\n",
    "\n",
    "print(build_tooltip(count_letter))\n",
    "print(build_tooltip(range))\n",
    "print(build_tooltip(print))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b8cfb97",
   "metadata": {},
   "source": [
    "This IDE is going to be an incredibly delightful experience for your users now! Notice how the count_letter.__doc__ version of the docstring had strange whitespace at the beginning of all but the first line. That's because the docstring is indented to line up visually when reading the code. But when we want to print the docstring, removing those leading spaces with inspect.getdoc() will look much better.\n",
    "\n",
    "## Docstrings to the rescue!\n",
    "Some maniac has corrupted your installation of numpy! All of the functions still exist, but they've been given random names. You desperately need to call the `numpy.histogram()` function and you don't have time to reinstall the package. Fortunately for you, the maniac didn't think to alter the docstrings, and you know how to access them. numpy has a lot of functions in it, so we've narrowed it down to four possible functions that could be `numpy.histogram()` in disguise: `numpy.leyud()`, `numpy.uqka()`, `numpy.fywdkxa()` or `numpy.jinzyxq()`.\n",
    "\n",
    "Examine each of these functions' docstrings in the IPython shell to determine which of them is actually `numpy.histogram()`.\n",
    "\n",
    "* numpy.leyud()\n",
    "\n",
    "* numpy.uqka()\n",
    "\n",
    "* **numpy.fywdkxa()**\n",
    "\n",
    "* numpy.jinzyxq()\n",
    "\n",
    "You found it! numpy.fywdkxa() is actually numpy.histogram() in disguise. If you've spent any time browsing numpy's online documentation, you will notice that it is built directly from the docstrings. There are some wonderful tools like sphinx and pydoc that will automatically generate online documentation for you based off of your docstrings.\n",
    "\n",
    "## Extract a function\n",
    "While you were developing a model to predict the likelihood of a student graduating from college, you wrote this bit of code to get the z-scores of students' yearly GPAs. Now you're ready to turn it into a production-quality system, so you need to do something about the repetition. Writing a function to calculate the z-scores would improve this code.\n",
    "```python\n",
    "# Standardize the GPAs for each year\n",
    "df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()\n",
    "df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()\n",
    "df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()\n",
    "df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()\n",
    "```\n",
    "Note: df is a pandas DataFrame where each row is a student with 4 columns of yearly student GPAs: y1_gpa, y2_gpa, y3_gpa, y4_gpa\n",
    "\n",
    "* Finish the function so that it returns the z-scores of a column.\n",
    "* Use the function to calculate the z-scores for each year (df['y1_z'], df['y2_z'], etc.) from the raw GPA scores (df.y1_gpa, df.y2_gpa, etc.)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e647fb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def standardize(column):\n",
    "    \"\"\"Standardize the values in a column.\n",
    "\n",
    "    Args:\n",
    "        column (pandas Series): The data to standardize.\n",
    "\n",
    "    Returns:\n",
    "        pandas Series: the values as z-scores\n",
    "    \"\"\"\n",
    "    # Finish the function so that it returns the z-scores\n",
    "    z_score = (column - column.mean()) / column.std()\n",
    "    return z_score\n",
    "\n",
    "# Use the standardize() function to calculate the z-scores\n",
    "df['y1_z'] = standardize(df.y1_gpa)\n",
    "df['y2_z'] = standardize(df.y2_gpa)\n",
    "df['y3_z'] = standardize(df.y3_gpa)\n",
    "df['y4_z'] = standardize(df.y4_gpa)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "929d748b",
   "metadata": {},
   "source": [
    "That's a fantastic function! standardize() will probably be useful in other places in your code, and now it is easy to use, test, and update if you need to. It's also easier to tell what the code is doing because of the docstring and the name of the function.\n",
    "\n",
    "## Split up a function\n",
    "Another engineer on your team has written this function to calculate the mean and median of a sorted list. You want to show them how to split it into two simpler functions: mean() and median()\n",
    "```python\n",
    "def mean_and_median(values):\n",
    "    \"\"\"Get the mean and median of a sorted list of `values`\n",
    "\n",
    "    Args:\n",
    "        values (iterable of float): A list of numbers\n",
    "\n",
    "    Returns:\n",
    "        tuple (float, float): The mean and median\n",
    "    \"\"\"\n",
    "    mean = sum(values) / len(values)\n",
    "    midpoint = int(len(values) / 2)\n",
    "    if len(values) % 2 == 0:\n",
    "        median = (values[midpoint - 1] + values[midpoint]) / 2\n",
    "    else:\n",
    "        median = values[midpoint]\n",
    "\n",
    "    return mean, median\n",
    "```\n",
    "\n",
    "* Write the `mean()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd5788dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mean(values):\n",
    "    \"\"\"Get the mean of a sorted list of values\n",
    "\n",
    "    Args:\n",
    "        values (iterable of float): A list of numbers\n",
    "\n",
    "    Returns:\n",
    "        float\n",
    "    \"\"\"\n",
    "    # Write the mean() function\n",
    "    mean = sum(values) / len(values)\n",
    "    return mean"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce50aa16",
   "metadata": {},
   "source": [
    "* Write the `median()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64facfaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "def median(values):\n",
    "    \"\"\"Get the median of a sorted list of values\n",
    "\n",
    "    Args:\n",
    "        values (iterable of float): A list of numbers\n",
    "\n",
    "    Returns:\n",
    "        float\n",
    "    \"\"\"\n",
    "    # Write the median() function\n",
    "    midpoint = int(len(values) / 2)\n",
    "    if len(values) % 2 == 0:\n",
    "        median = (values[midpoint - 1] + values[midpoint]) / 2\n",
    "    else:\n",
    "        median = values[midpoint]\n",
    "    return median"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "891b499d",
   "metadata": {},
   "source": [
    "A perfect split! Each function does one thing and does it well. Using, testing, and maintaining these will be a breeze (although you'll probably just use numpy.mean() and numpy.median() for this in real life).\n",
    "\n",
    "## Mutable or immutable?\n",
    "The following function adds a mapping between a string and the lowercase version of that string to a dictionary. What do you expect the values of d and s to be after the function is called?\n",
    "```python\n",
    "def store_lower(_dict, _string):\n",
    "    \"\"\"Add a mapping between `_string` and a lowercased version of `_string` to `_dict`\n",
    "\n",
    "    Args:\n",
    "        _dict (dict): The dictionary to update.\n",
    "        _string (str): The string to add.\n",
    "    \"\"\"\n",
    "    orig_string = _string\n",
    "    _string = _string.lower()\n",
    "    _dict[orig_string] = _string\n",
    "\n",
    "d = {}\n",
    "s = 'Hello'\n",
    "\n",
    "store_lower(d, s)\n",
    "```\n",
    "\n",
    "\n",
    "* d = {}, s = 'Hello'\n",
    "\n",
    "* d = {}, s = 'hello'\n",
    "\n",
    "* **d = {'Hello': 'hello'}, s = 'Hello'**\n",
    "\n",
    "* d = {'Hello': 'hello'}, s = 'hello'\n",
    "\n",
    "* d = {'hello': 'hello'}, s = 'hello'\n",
    "\n",
    "Correct! Dictionaries are mutable objects in Python, so the function can directly change it in the _dict[_orig_string] = _string statement. Strings, on the other hand, are immutable. When the function creates the lowercase version, it has to assign it to the _string variable. This disconnects what happens to _string from the external s variable.\n",
    "\n",
    "## Best practice for default arguments\n",
    "One of your co-workers (who obviously didn't take this course) has written this function for adding a column to a pandas DataFrame. Unfortunately, they used a mutable variable as a default argument value! Please show them a better way to do this so that they don't get unexpected behavior.\n",
    "```python\n",
    "def add_column(values, df=pandas.DataFrame()):\n",
    "    \"\"\"Add a column of `values` to a DataFrame `df`.\n",
    "    The column will be named \"col_<n>\" where \"n\" is\n",
    "    the numerical index of the column.\n",
    "\n",
    "    Args:\n",
    "        values (iterable): The values of the new column\n",
    "        df (DataFrame, optional): The DataFrame to update.\n",
    "        If no DataFrame is passed, one is created by default.\n",
    "\n",
    "    Returns:\n",
    "        DataFrame\n",
    "    \"\"\"\n",
    "    df['col_{}'.format(len(df.columns))] = values\n",
    "    return df\n",
    "```\n",
    "\n",
    "* Change the default value of df to an immutable value to follow best practices.\n",
    "* Update the code of the function so that a new DataFrame is created if the caller didn't pass one."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76aec98b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use an immutable variable for the default argument\n",
    "def better_add_column(values, df=None):\n",
    "    \"\"\"Add a column of `values` to a DataFrame `df`.\n",
    "    The column will be named \"col_<n>\" where \"n\" is\n",
    "    the numerical index of the column.\n",
    "\n",
    "    Args:\n",
    "        values (iterable): The values of the new column\n",
    "        df (DataFrame, optional): The DataFrame to update.\n",
    "        If no DataFrame is passed, one is created by default.\n",
    "\n",
    "    Returns:\n",
    "        DataFrame\n",
    "    \"\"\"\n",
    "    # Update the function to create a default DataFrame\n",
    "    if df is None:\n",
    "    df = pandas.DataFrame()\n",
    "    df['col_{}'.format(len(df.columns))] = values\n",
    "    return df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c238edcc",
   "metadata": {},
   "source": [
    "Beautiful and best practice! When you need to set a mutable variable as a default argument, always use None and then set the value in the body of the function. This prevents unexpected behavior like adding multiple columns if you call the function more than once."
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
