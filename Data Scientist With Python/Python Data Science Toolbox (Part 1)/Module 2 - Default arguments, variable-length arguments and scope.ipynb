{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b6a10f8b",
   "metadata": {},
   "source": [
    "# Default arguments, variable-length arguments and scope\n",
    "\n",
    "### In this chapter, you'll learn to write functions with default arguments, so that the user doesn't always need to specify them, and variable-length arguments, so that they can pass to your functions an arbitrary number of arguments. These are both incredibly useful tools! You'll also learn about the essential concept of scope. Enjoy!\n",
    "\n",
    "### Pop quiz on understanding scope\n",
    "In this exercise, you will practice what you've learned about scope in functions. The variable num has been predefined as 5, alongside the following function definitions:\n",
    "\n",
    "```python\n",
    "def func1():\n",
    "    num = 3\n",
    "    print(num)\n",
    "\n",
    "def func2():\n",
    "    global num\n",
    "    double_num = num * 2\n",
    "    num = 6\n",
    "    print(double_num)\n",
    "```\n",
    "Try calling func1() and func2() in the shell, then answer the following questions:\n",
    "\n",
    "What are the values printed out when you call func1() and func2()?\n",
    "What is the value of num in the global scope after calling func1() and func2()?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a30580d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "num = 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eb551c04",
   "metadata": {},
   "outputs": [],
   "source": [
    "def func1():\n",
    "    num = 3\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2bd0047d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "func1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "267462d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def func2():\n",
    "    global num\n",
    "    double_num = num * 2\n",
    "    num = 6\n",
    "    print(double_num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "215406fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "func2()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ad4175e9",
   "metadata": {},
   "source": [
    "## The keyword global\n",
    "Let's work more on your mastery of scope. In this exercise, you will use the keyword global within a function to alter the value of a variable defined in the global scope."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cb904d76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "teen titans\n",
      "justice league\n"
     ]
    }
   ],
   "source": [
    "# Create a string: team\n",
    "team = \"teen titans\"\n",
    "\n",
    "# Define change_team()\n",
    "def change_team():\n",
    "    \"\"\"Change the value of the global variable team.\"\"\"\n",
    "\n",
    "    # Use team in global scope\n",
    "    global team\n",
    "    \n",
    "\n",
    "    # Change the value of team in global: team\n",
    "    team = 'justice league'\n",
    "# Print team\n",
    "print(team)\n",
    "\n",
    "# Call change_team()\n",
    "change_team()\n",
    "\n",
    "# Print team\n",
    "print(team)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4cf114c2",
   "metadata": {},
   "source": [
    "### Nested Functions I\n",
    "One reason why you'd like to do this is to avoid writing out the same computations within functions repeatedly. There's nothing new about defining nested functions: you simply define it as you would a regular function with def and embed it inside another function!\n",
    "\n",
    "In this exercise, inside a function three_shouts(), you will define a nested function inner() that concatenates a string object with !!!. three_shouts() then returns a tuple of three elements, each a string concatenated with !!! using inner(). Go for it!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cb524391",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('a!!!', 'b!!!', 'c!!!')\n"
     ]
    }
   ],
   "source": [
    "# Define three_shouts\n",
    "def three_shouts(word1, word2, word3):\n",
    "    \"\"\"Returns a tuple of strings\n",
    "    concatenated with '!!!'.\"\"\"\n",
    "\n",
    "    # Define inner\n",
    "    def inner(word):\n",
    "        \"\"\"Returns a string concatenated with '!!!'.\"\"\"\n",
    "        return word + '!!!'\n",
    "\n",
    "    # Return a tuple of strings\n",
    "    return (inner(word1), inner(word2), inner(word3))\n",
    "\n",
    "# Call three_shouts() and print\n",
    "print(three_shouts('a', 'b', 'c'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e922b778",
   "metadata": {},
   "source": [
    "### Nested Functions II\n",
    "Great job, you've just nested a function within another function. One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when the outer function has finished execution.\n",
    "\n",
    "Let's move forward then! In this exercise, you will complete the definition of the inner function inner_echo() and then call echo() a couple of times, each with a different argument. Complete the exercise and see what the output will be!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a8d1f489",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hellohello hellohellohello\n"
     ]
    }
   ],
   "source": [
    "# Define echo\n",
    "def echo(n):\n",
    "    \"\"\"Return the inner_echo function.\"\"\"\n",
    "\n",
    "    # Define inner_echo\n",
    "    def inner_echo(word1):\n",
    "        \"\"\"Concatenate n copies of word1.\"\"\"\n",
    "        echo_word = word1 * n\n",
    "        return echo_word\n",
    "\n",
    "    # Return inner_echo\n",
    "    return inner_echo\n",
    "\n",
    "# Call echo: twice\n",
    "twice = echo(2)\n",
    "\n",
    "# Call echo: thrice\n",
    "thrice = echo(3)\n",
    "\n",
    "# Call twice() and thrice() then print\n",
    "print(twice('hello'), thrice('hello'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20cbf2e8",
   "metadata": {},
   "source": [
    "### The keyword nonlocal and nested functions\n",
    "Let's once again work further on your mastery of scope! In this exercise, you will use the keyword nonlocal within a nested function to alter the value of a variable defined in the enclosing scope."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "367d13e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hellohello\n",
      "hellohello!!!\n"
     ]
    }
   ],
   "source": [
    "# Define echo_shout()\n",
    "def echo_shout(word):\n",
    "    \"\"\"Change the value of a nonlocal variable\"\"\"\n",
    "    \n",
    "    # Concatenate word with itself: echo_word\n",
    "    echo_word = word + word\n",
    "    \n",
    "    # Print echo_word\n",
    "    print(echo_word)\n",
    "    \n",
    "    # Define inner function shout()\n",
    "    def shout():\n",
    "        \"\"\"Alter a variable in the enclosing scope\"\"\"    \n",
    "        # Use echo_word in nonlocal scope\n",
    "        nonlocal echo_word\n",
    "        \n",
    "        # Change echo_word to echo_word concatenated with '!!!'\n",
    "        echo_word = echo_word + '!!!'\n",
    "    \n",
    "    # Call function shout()\n",
    "    shout()\n",
    "    \n",
    "    # Print echo_word\n",
    "    print(echo_word)\n",
    "\n",
    "# Call function echo_shout() with argument 'hello'\n",
    "echo_shout('hello')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8285c12c",
   "metadata": {},
   "source": [
    "Quite something, that nonlocal keyword!\n",
    "\n",
    "### Functions with one default argument\n",
    "In the previous chapter, you've learned to define functions with more than one parameter and then calling those functions by passing the required number of arguments. In the last video, Hugo built on this idea by showing you how to define functions with default arguments. You will practice that skill in this exercise by writing a function that uses a default argument and then calling the function a couple of times."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "48c31c9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hey!!!\n",
      "HeyHeyHeyHeyHey!!!\n"
     ]
    }
   ],
   "source": [
    "# Define shout_echo\n",
    "def shout_echo(word1, echo = 1):\n",
    "    \"\"\"Concatenate echo copies of word1 and three\n",
    "     exclamation marks at the end of the string.\"\"\"\n",
    "\n",
    "    # Concatenate echo copies of word1 using *: echo_word\n",
    "    echo_word = echo*word1\n",
    "\n",
    "    # Concatenate '!!!' to echo_word: shout_word\n",
    "    shout_word = echo_word + '!!!'\n",
    "\n",
    "    # Return shout_word\n",
    "    return shout_word\n",
    "\n",
    "# Call shout_echo() with \"Hey\": no_echo\n",
    "no_echo = shout_echo('Hey')\n",
    "\n",
    "# Call shout_echo() with \"Hey\" and echo=5: with_echo\n",
    "with_echo = shout_echo('Hey', echo=5)\n",
    "\n",
    "# Print no_echo and with_echo\n",
    "print(no_echo)\n",
    "print(with_echo)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9276087",
   "metadata": {},
   "source": [
    "### Functions with multiple default arguments\n",
    "You've now defined a function that uses a default argument - don't stop there just yet! You will now try your hand at defining a function with more than one default argument and then calling this function in various ways.\n",
    "\n",
    "After defining the function, you will call it by supplying values to all the default arguments of the function. Additionally, you will call the function by not passing a value to one of the default arguments - see how that changes the output of your function!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b9dec6c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HEYHEYHEYHEYHEY!!!\n",
      "HEY!!!\n"
     ]
    }
   ],
   "source": [
    "# Define shout_echo\n",
    "def shout_echo(word1, echo = 1, intense = False):\n",
    "    \"\"\"Concatenate echo copies of word1 and three\n",
    "    exclamation marks at the end of the string.\"\"\"\n",
    "\n",
    "    # Concatenate echo copies of word1 using *: echo_word\n",
    "    echo_word = word1 * echo\n",
    "\n",
    "    # Capitalize echo_word if intense is True\n",
    "    if intense is True:\n",
    "        # Capitalize and concatenate '!!!': echo_word_new\n",
    "        echo_word_new = echo_word.upper() + '!!!'\n",
    "    else:\n",
    "        # Concatenate '!!!' to echo_word: echo_word_new\n",
    "        echo_word_new = echo_word + '!!!'\n",
    "\n",
    "    # Return echo_word_new\n",
    "    return echo_word_new\n",
    "\n",
    "# Call shout_echo() with \"Hey\", echo=5 and intense=True: with_big_echo\n",
    "with_big_echo = shout_echo(\"Hey\", 5, True)\n",
    "\n",
    "# Call shout_echo() with \"Hey\" and intense=True: big_no_echo\n",
    "big_no_echo = shout_echo(\"Hey\", intense = True)\n",
    "\n",
    "# Print values\n",
    "print(with_big_echo)\n",
    "print(big_no_echo)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22b7c5d7",
   "metadata": {},
   "source": [
    "### Functions with variable-length arguments (*args)\n",
    "Flexible arguments enable you to pass a variable number of arguments to a function. In this exercise, you will practice defining a function that accepts a variable number of string arguments.\n",
    "\n",
    "The function you will define is gibberish() which can accept a variable number of string values. Its return value is a single string composed of all the string arguments concatenated together in the order they were passed to the function call. You will call the function with a single string argument and see how the output changes with another call using more than one string argument.Within the function definition, args is a tuple."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cd65bc34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "luke\n",
      "lukeleiahanobidarth\n"
     ]
    }
   ],
   "source": [
    "# Define gibberish\n",
    "def gibberish(*args):\n",
    "    \"\"\"Concatenate strings in *args together.\"\"\"\n",
    "\n",
    "    # Initialize an empty string: hodgepodge\n",
    "    hodgepodge = \"\"\n",
    "\n",
    "    # Concatenate the strings in args\n",
    "    for word in args:\n",
    "        hodgepodge += word\n",
    "\n",
    "    # Return hodgepodge\n",
    "    return hodgepodge\n",
    "\n",
    "# Call gibberish() with one string: one_word\n",
    "one_word = gibberish(\"luke\")\n",
    "\n",
    "# Call gibberish() with five strings: many_words\n",
    "many_words = gibberish(\"luke\", \"leia\", \"han\", \"obi\", \"darth\")\n",
    "\n",
    "# Print one_word and many_words\n",
    "print(one_word)\n",
    "print(many_words)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "862208d7",
   "metadata": {},
   "source": [
    "### Functions with variable-length keyword arguments (**kwargs)\n",
    "Let's push further on what you've learned about flexible arguments - you've used *args, you're now going to use **kwargs! What makes **kwargs different is that it allows you to pass a variable number of keyword arguments to functions.Within the function definition, kwargs is a dictionary.\n",
    "\n",
    "To understand this idea better, you're going to use **kwargs in this exercise to define a function that accepts a variable number of keyword arguments. The function simulates a simple status report system that prints out the status of a character in a movie."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5efebbb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "BEGIN: REPORT\n",
      "\n",
      "name: luke\n",
      "affiliation: jedi\n",
      "status: missing\n",
      "\n",
      "END REPORT\n",
      "\n",
      "BEGIN: REPORT\n",
      "\n",
      "name: anakin\n",
      "affiliation: sith lord\n",
      "status: deceased\n",
      "\n",
      "END REPORT\n"
     ]
    }
   ],
   "source": [
    "# Define report_status\n",
    "def report_status(**kwargs):\n",
    "    \"\"\"Print out the status of a movie character.\"\"\"\n",
    "\n",
    "    print(\"\\nBEGIN: REPORT\\n\")\n",
    "\n",
    "    # Iterate over the key-value pairs of kwargs\n",
    "    for key, value in kwargs.items():\n",
    "        # Print out the keys and values, separated by a colon ':'\n",
    "        print(key + \": \" + value)\n",
    "\n",
    "    print(\"\\nEND REPORT\")\n",
    "\n",
    "# First call to report_status()\n",
    "report_status(name='luke', affiliation='jedi', status='missing')\n",
    "\n",
    "# Second call to report_status()\n",
    "report_status(name='anakin', affiliation='sith lord', status='deceased')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e262fe0",
   "metadata": {},
   "source": [
    "### Bringing it all together (1)\n",
    "Recall the Bringing it all together exercise in the previous chapter where you did a simple Twitter analysis by developing a function that counts how many tweets are in certain languages. The output of your function was a dictionary that had the language as the keys and the counts of tweets in that language as the value.\n",
    "\n",
    "In this exercise, we will generalize the Twitter language analysis that you did in the previous chapter. You will do that by including a default argument that takes a column name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7ce9082a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'en': 97, 'et': 1, 'und': 2}\n",
      "{'<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>': 24, '<a href=\"http://www.facebook.com/twitter\" rel=\"nofollow\">Facebook</a>': 1, '<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>': 26, '<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>': 33, '<a href=\"http://www.twitter.com\" rel=\"nofollow\">Twitter for BlackBerry</a>': 2, '<a href=\"http://www.google.com/\" rel=\"nofollow\">Google</a>': 2, '<a href=\"http://twitter.com/#!/download/ipad\" rel=\"nofollow\">Twitter for iPad</a>': 6, '<a href=\"http://linkis.com\" rel=\"nofollow\">Linkis.com</a>': 2, '<a href=\"http://rutracker.org/forum/viewforum.php?f=93\" rel=\"nofollow\">newzlasz</a>': 2, '<a href=\"http://ifttt.com\" rel=\"nofollow\">IFTTT</a>': 1, '<a href=\"http://www.myplume.com/\" rel=\"nofollow\">Plume\\xa0for\\xa0Android</a>': 1}\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Python Data Science Toolbox (Part 1)/datasets/tweets.csv')\n",
    "\n",
    "# Define count_entries()\n",
    "def count_entries(df, col_name = 'lang'):\n",
    "    \"\"\"Return a dictionary with counts of\n",
    "    occurrences as value for each key.\"\"\"\n",
    "\n",
    "    # Initialize an empty dictionary: cols_count\n",
    "    cols_count = {}\n",
    "\n",
    "    # Extract column from DataFrame: col\n",
    "    col = df[col_name]\n",
    "    \n",
    "    # Iterate over the column in DataFrame\n",
    "    for entry in col:\n",
    "\n",
    "        # If entry is in cols_count, add 1\n",
    "        if entry in cols_count.keys():\n",
    "            cols_count[entry] += 1\n",
    "\n",
    "        # Else add the entry to cols_count, set the value to 1\n",
    "        else:\n",
    "            cols_count[entry] = 1\n",
    "\n",
    "    # Return the cols_count dictionary\n",
    "    return cols_count\n",
    "\n",
    "# Call count_entries(): result1\n",
    "result1 =count_entries(df, 'lang')\n",
    "\n",
    "# Call count_entries(): result2\n",
    "result2 = count_entries(df, 'source')\n",
    "\n",
    "# Print result1 and result2\n",
    "print(result1)\n",
    "print(result2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d28fc755",
   "metadata": {},
   "source": [
    "### Bringing it all together (2)\n",
    "Wow, you've just generalized your Twitter language analysis that you did in the previous chapter to include a default argument for the column name. You're now going to generalize this function one step further by allowing the user to pass it a flexible argument, that is, in this case, as many column names as the user would like!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "79ca4927",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'en': 97, 'et': 1, 'und': 2}\n",
      "{'en': 97, 'et': 1, 'und': 2, '<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>': 24, '<a href=\"http://www.facebook.com/twitter\" rel=\"nofollow\">Facebook</a>': 1, '<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>': 26, '<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>': 33, '<a href=\"http://www.twitter.com\" rel=\"nofollow\">Twitter for BlackBerry</a>': 2, '<a href=\"http://www.google.com/\" rel=\"nofollow\">Google</a>': 2, '<a href=\"http://twitter.com/#!/download/ipad\" rel=\"nofollow\">Twitter for iPad</a>': 6, '<a href=\"http://linkis.com\" rel=\"nofollow\">Linkis.com</a>': 2, '<a href=\"http://rutracker.org/forum/viewforum.php?f=93\" rel=\"nofollow\">newzlasz</a>': 2, '<a href=\"http://ifttt.com\" rel=\"nofollow\">IFTTT</a>': 1, '<a href=\"http://www.myplume.com/\" rel=\"nofollow\">Plume\\xa0for\\xa0Android</a>': 1}\n"
     ]
    }
   ],
   "source": [
    "# Define count_entries()\n",
    "def count_entries(df, *args):\n",
    "    \"\"\"Return a dictionary with counts of\n",
    "    occurrences as value for each key.\"\"\"\n",
    "    \n",
    "    #Initialize an empty dictionary: cols_count\n",
    "    cols_count = {}\n",
    "    \n",
    "    # Iterate over column names in args\n",
    "    for col_name in args:\n",
    "    \n",
    "        # Extract column from DataFrame: col\n",
    "        col = df[col_name]\n",
    "    \n",
    "        # Iterate over the column in DataFrame\n",
    "        for entry in col:\n",
    "    \n",
    "            # If entry is in cols_count, add 1\n",
    "            if entry in cols_count.keys():\n",
    "                cols_count[entry] += 1\n",
    "    \n",
    "            # Else add the entry to cols_count, set the value to 1\n",
    "            else:\n",
    "                cols_count[entry] = 1\n",
    "\n",
    "    # Return the cols_count dictionary\n",
    "    return cols_count\n",
    "\n",
    "# Call count_entries(): result1\n",
    "result1 = count_entries(df, 'lang')\n",
    "\n",
    "# Call count_entries(): result2\n",
    "result2 = count_entries(df, 'lang', 'source')\n",
    "\n",
    "# Print result1 and result2\n",
    "print(result1)\n",
    "print(result2)"
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
