{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6937b0c1",
   "metadata": {},
   "source": [
    "# Writing your own functions\n",
    "\n",
    "### Here you will learn how to write your very own functions. In this Chapter, you'll learn how to write simple functions, as well as functions that accept multiple arguments and return multiple values. You'll also have the opportunity to apply these newfound skills to questions that commonly arise in Data Science contexts.\n",
    "\n",
    "### Strings in Python\n",
    "Strings represent textual data. To assign the string 'DataCamp' to a variable company, you execute:\n",
    "\n",
    "company = 'DataCamp'\n",
    "You've also learned to use the operations + and * with strings. Unlike with numeric types such as ints and floats, the + operator concatenates strings together, while the * concatenates multiple copies of a string together. In this exercise, you will use the + and * operations on strings to answer the question below. Execute the following code in the shell:\n",
    "```python\n",
    "object1 = \"data\" + \"analysis\" + \"visualization\"  \n",
    "object2 = 1 * 3  \n",
    "object3 = \"1\" * 3  \n",
    "```\n",
    "What are the values in object1, object2, and object3, respectively?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "03b16046",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dataanalysisvisualization\n",
      "3\n",
      "111\n"
     ]
    }
   ],
   "source": [
    "object1 = 'data' + 'analysis' + 'visualization'\n",
    "object2 = 1*3\n",
    "object3 = \"1\"*3\n",
    "\n",
    "print(object1)\n",
    "print(object2)\n",
    "print(object3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5e2e690",
   "metadata": {},
   "source": [
    "### Recapping built-in functions\n",
    "In the video, Hugo briefly examined the return behavior of the built-in functions print() and str(). Here, you will use both functions and examine their return values. A variable x has been preloaded for this exercise. Run the code below in the console. Pay close attention to the results to answer the question that follows.\n",
    "\n",
    "- Assign str(x) to a variable y1: y1 = str(x)\n",
    "- Assign print(x) to a variable y2: y2 = print(x)\n",
    "- Check the types of the variables x, y1, and y2.\n",
    "\n",
    "What are the types of x, y1, and y2?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b9b7e792",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 4.89"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "25529862",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.89\n"
     ]
    }
   ],
   "source": [
    "y1 = str(x)\n",
    "y2 = print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9da49dd9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n",
      "<class 'str'>\n",
      "<class 'NoneType'>\n"
     ]
    }
   ],
   "source": [
    "print(type(x))\n",
    "print(type(y1))\n",
    "print(type(y2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ea8ba1a",
   "metadata": {},
   "source": [
    "Correct! It is important to remember that assigning a variable y2 to a function that prints a value but does not return a value will result in that variable y2 being of type NoneType.\n",
    "\n",
    "### Write a simple function\n",
    "You will now write your own function!\n",
    "\n",
    "Define a function, shout(), which simply prints out a string with three exclamation marks '!!!' at the end. The code for the square() function is found below. You can use it as a pattern to define shout().\n",
    "\n",
    "```python\n",
    "def square():\n",
    "    new_value = 4 ** 2\n",
    "    return new_value\n",
    "```\n",
    "Function bodies need to be indented by a consistent number of spaces and the choice of 4 is common\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "915c91f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "congratulations!!!\n"
     ]
    }
   ],
   "source": [
    "# Define the function shout\n",
    "def shout():\n",
    "    \"\"\"Print a string with three exclamation marks\"\"\"\n",
    "    # Concatenate the strings: shout_word\n",
    "    shout_word = 'congratulations' + '!!!'\n",
    "\n",
    "    # Print shout_word\n",
    "    print(shout_word)\n",
    "\n",
    "# Call shout\n",
    "shout()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "015034ba",
   "metadata": {},
   "source": [
    "### Single-parameter functions\n",
    "Congratulations! You have successfully defined and called your own function! That's pretty cool.\n",
    "\n",
    "In the previous exercise, you defined and called the function shout(), which printed out a string concatenated with '!!!'. You will now update shout() by adding a parameter so that it can accept and process any string argument passed to it. Also note that shout(word), the part of the header that specifies the function name and parameter(s), is known as the signature of the function. You may encounter this term in the wild!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b0922381",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "congratulations!!!\n"
     ]
    }
   ],
   "source": [
    "# Define shout with the parameter, word\n",
    "def shout(word):\n",
    "    \"\"\"Print a string with three exclamation marks\"\"\"\n",
    "    # Concatenate the strings: shout_word\n",
    "    shout_word = word + '!!!'\n",
    "\n",
    "    # Print shout_word\n",
    "    print(shout_word)\n",
    "\n",
    "# Call shout with the string 'congratulations'\n",
    "shout('congratulations')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc706b84",
   "metadata": {},
   "source": [
    "### Functions that return single values\n",
    "You're getting very good at this! Try your hand at another modification to the shout() function so that it now returns a single value instead of printing within the function. Recall that the return keyword lets you return values from functions.Returning values is generally more desirable than printing them out because, as you saw earlier, a print() call assigned to a variable has type NoneType"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "23f287a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "congratulations!!!\n"
     ]
    }
   ],
   "source": [
    "# Define shout with the parameter, word\n",
    "def shout(word):\n",
    "    \"\"\"Return a string with three exclamation marks\"\"\"\n",
    "    # Concatenate the strings: shout_word\n",
    "    shout_word = word + '!!!'\n",
    "\n",
    "    # Replace print with return\n",
    "    return shout_word\n",
    "\n",
    "# Pass 'congratulations' to shout: yell\n",
    "yell = shout('congratulations')\n",
    "\n",
    "# Print yell\n",
    "print(yell)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6aae8d1c",
   "metadata": {},
   "source": [
    "Great work! Here it made sense to assign the output of shout('congratulations') to a variable yell because the function shout actually returns a value, it does not merely print one.\n",
    "\n",
    "### Functions with multiple parameters\n",
    "You are now going to use what you've learned to modify the shout() function further. Here, you will modify shout() to accept two arguments."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "eddea378",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "congratulations!!!you!!!\n"
     ]
    }
   ],
   "source": [
    "# Define shout with parameters word1 and word2\n",
    "def shout(word1, word2):\n",
    "    \"\"\"Concatenate strings with three exclamation marks\"\"\"\n",
    "    # Concatenate word1 with '!!!': shout1\n",
    "    shout1 = word1 + '!!!'\n",
    "    \n",
    "    # Concatenate word2 with '!!!': shout2\n",
    "    shout2 = word2 + '!!!'\n",
    "    \n",
    "    # Concatenate shout1 with shout2: new_shout\n",
    "    new_shout = shout1 + shout2\n",
    "\n",
    "    # Return new_shout\n",
    "    return new_shout\n",
    "\n",
    "# Pass 'congratulations' and 'you' to shout(): yell\n",
    "yell = shout('congratulations', 'you')\n",
    "\n",
    "# Print yell\n",
    "print(yell)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c413c6df",
   "metadata": {},
   "source": [
    "### A brief introduction to tuples\n",
    "Alongside learning about functions, you've also learned about tuples! Here, you will practice what you've learned about tuples: how to construct, unpack, and access tuple elements."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "338f4cc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "nums = (3, 4, 6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7853afa5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(nums)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4eb2c305",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Unpack nums into num1, num2, and num3\n",
    "num1, num2, num3 = nums"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "db949b97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "4\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "print(num1)\n",
    "print(num2)\n",
    "print(num3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1c71c3d",
   "metadata": {},
   "source": [
    "### Functions that return multiple values\n",
    "In the previous exercise, you constructed tuples, assigned tuples to variables, and unpacked tuples. Here you will return multiple values from a function using tuples. Let's now update our shout() function to return multiple values. Instead of returning just one string, we will return two strings with the string !!! concatenated to each.\n",
    "\n",
    "Note that the return statement return x, y has the same result as return (x, y): the former actually packs x and y into a tuple under the hood!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fa8b3b53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "congratulations!!!\n",
      "you!!!\n"
     ]
    }
   ],
   "source": [
    "# Define shout_all with parameters word1 and word2\n",
    "def shout_all(word1, word2):\n",
    "    \n",
    "    # Concatenate word1 with '!!!': shout1\n",
    "    shout1 = word1 + '!!!'\n",
    "    \n",
    "    # Concatenate word2 with '!!!': shout2\n",
    "    shout2 = word2 + '!!!'\n",
    "    \n",
    "    # Construct a tuple with shout1 and shout2: shout_words\n",
    "    shout_words = (shout1, shout2)\n",
    "\n",
    "    # Return shout_words\n",
    "    return shout_words\n",
    "\n",
    "# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2\n",
    "yell1, yell2 = shout_all('congratulations', 'you')\n",
    "\n",
    "# Print yell1 and yell2\n",
    "print(yell1)\n",
    "print(yell2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b405f0d",
   "metadata": {},
   "source": [
    "### Bringing it all together (1)\n",
    "You've got your first taste of writing your own functions in the previous exercises. You've learned how to add parameters to your own function definitions, return a value or multiple values with tuples, and how to call the functions you've defined.\n",
    "\n",
    "In this and the following exercise, you will bring together all these concepts and apply them to a simple data science problem. You will load a dataset and develop functionalities to extract simple insights from the data.\n",
    "\n",
    "For this exercise, your goal is to recall how to load a dataset into a DataFrame. The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which the keys are the names of languages and the values are the number of tweets in the given language. The file tweets.csv is available in your current directory."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1db07310",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'en': 97, 'et': 1, 'und': 2}\n"
     ]
    }
   ],
   "source": [
    "# Import pandas\n",
    "import pandas as pd\n",
    "\n",
    "# Import Twitter data as DataFrame: df\n",
    "df_tweets = pd.read_csv('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Python Data Science Toolbox (Part 1)/datasets/tweets.csv')\n",
    "\n",
    "# Initialize an empty dictionary: langs_count\n",
    "langs_count = {}\n",
    "\n",
    "# Extract column from DataFrame: col\n",
    "col = df_tweets['lang']\n",
    "\n",
    "# Iterate over lang column in DataFrame\n",
    "for entry in col:\n",
    "\n",
    "    # If the language is in langs_count, add 1\n",
    "    if entry in langs_count.keys():\n",
    "        langs_count[entry] +=1\n",
    "    # Else add the language to langs_count, set the value to 1\n",
    "    else:\n",
    "        langs_count[entry] = 1\n",
    "\n",
    "# Print the populated dictionary\n",
    "print(langs_count)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11088edd",
   "metadata": {},
   "source": [
    "### Bringing it all together (2)\n",
    "Great job! You've now defined the functionality for iterating over entries in a column and building a dictionary with keys the names of languages and values the number of tweets in the given language.\n",
    "\n",
    "In this exercise, you will define a function with the functionality you developed in the previous exercise, return the resulting dictionary from within the function, and call the function with the appropriate arguments."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "61fc93e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'en': 97, 'et': 1, 'und': 2}\n"
     ]
    }
   ],
   "source": [
    "# Define count_entries()\n",
    "def count_entries(df_tweets, col_name):\n",
    "    \"\"\"Return a dictionary with counts of \n",
    "    occurrences as value for each key.\"\"\"\n",
    "\n",
    "    # Initialize an empty dictionary: langs_count\n",
    "    langs_count = {}\n",
    "    \n",
    "    # Extract column from DataFrame: col\n",
    "    col = df_tweets[col_name]\n",
    "    \n",
    "    # Iterate over lang column in DataFrame\n",
    "    for entry in col:\n",
    "\n",
    "        # If the language is in langs_count, add 1\n",
    "        if entry in langs_count.keys():\n",
    "            langs_count[entry] += 1\n",
    "        # Else add the language to langs_count, set the value to 1\n",
    "        else:\n",
    "            langs_count[entry] = 1\n",
    "\n",
    "    # Return the langs_count dictionary\n",
    "    return langs_count\n",
    "\n",
    "# Call count_entries(): result\n",
    "result = count_entries(df_tweets, 'lang')\n",
    "\n",
    "# Print the result\n",
    "print(result)"
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
