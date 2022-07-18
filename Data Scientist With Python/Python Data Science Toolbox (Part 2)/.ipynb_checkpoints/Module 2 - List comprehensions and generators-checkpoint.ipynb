{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d616a333",
   "metadata": {},
   "source": [
    "# List comprehensions and generators\n",
    "\n",
    "### In this chapter, you'll build on your knowledge of iterators and be introduced to list comprehensions, which allow you to create complicated lists and lists of lists in one line of code! List comprehensions can dramatically simplify your code and make it more efficient, and will become a vital part of your Python Data Science toolbox. You'll then learn about generators, which are extremely helpful when working with large sequences of data that you may not want to store in memory but instead generate on the fly.\n",
    "\n",
    "### Writing list comprehensions\n",
    "Your job in this exercise is to write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d45c11c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create list comprehension: squares\n",
    "squares = [x**2 for x in range(0,10)]\n",
    "squares"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07beeff3",
   "metadata": {},
   "source": [
    "### Nested list comprehensions\n",
    "Great! At this point, you have a good grasp of the basic syntax of list comprehensions. Let's push your code-writing skills a little further. In this exercise, you will be writing a list comprehension within another list comprehension, or nested list comprehensions. It sounds a little tricky, but you can do it!\n",
    "\n",
    "Let's step aside for a while from strings. One of the ways in which lists can be used are in representing multi-dimension objects such as matrices. Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:\n",
    "\n",
    "```python\n",
    "matrix = [[0, 1, 2, 3, 4],\n",
    "          [0, 1, 2, 3, 4],\n",
    "          [0, 1, 2, 3, 4],\n",
    "          [0, 1, 2, 3, 4],\n",
    "          [0, 1, 2, 3, 4]]\n",
    "```  \n",
    "Your task is to recreate this matrix by using nested listed comprehensions. Recall that you can create one of the rows of the matrix with a single list comprehension. To create the list of lists, you simply have to supply the list comprehension as the output expression of the overall list comprehension:\n",
    "\n",
    "```python\n",
    "[[output expression] for iterator variable in iterable]\n",
    "```\n",
    "Note that here, the output expression is itself a list comprehension."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "213ee6e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[0, 1, 2, 3, 4],\n",
       " [0, 1, 2, 3, 4],\n",
       " [0, 1, 2, 3, 4],\n",
       " [0, 1, 2, 3, 4],\n",
       " [0, 1, 2, 3, 4]]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "matrix = [[x for x in range(5)] for x in range(5)]\n",
    "matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "064640d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4]\n",
      "[0, 1, 2, 3, 4]\n",
      "[0, 1, 2, 3, 4]\n",
      "[0, 1, 2, 3, 4]\n",
      "[0, 1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "# Create a 5 x 5 matrix using a list of lists: matrix\n",
    "matrix = [[col for col in range(0,5)] for row in range(0,5) ]\n",
    "\n",
    "# Print the matrix\n",
    "for row in matrix:\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe1d054e",
   "metadata": {},
   "source": [
    "### Using conditionals in comprehensions (1)\n",
    "You've been using list comprehensions to build lists of values, sometimes using operations to create these values.\n",
    "\n",
    "An interesting mechanism in list comprehensions is that you can also create lists with values that meet only a certain condition. One way of doing this is by using conditionals on iterator variables. In this exercise, you will do exactly that!\n",
    "\n",
    "You can apply a conditional statement to test the iterator variable by adding an if statement in the optional predicate expression part after the for statement in the comprehension:\n",
    "\n",
    "```python\n",
    "[ output expression for iterator variable in iterable if predicate expression ].\n",
    "```\n",
    "You will use this recipe to write a list comprehension for this exercise. You are given a list of strings fellowship and, using a list comprehension, you will create a list that only includes the members of fellowship that have 7 characters or more."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7f420dee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['samwise', 'aragorn', 'legolas', 'boromir']\n"
     ]
    }
   ],
   "source": [
    "# Create a list of strings: fellowship\n",
    "fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']\n",
    "\n",
    "# Create list comprehension: new_fellowship\n",
    "new_fellowship = [member for member in fellowship if len(member) >= 7]\n",
    "\n",
    "# Print the new list\n",
    "print(new_fellowship)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "033611df",
   "metadata": {},
   "source": [
    "### Using conditionals in comprehensions (2)\n",
    "In the previous exercise, you used an if conditional statement in the predicate expression part of a list comprehension to evaluate an iterator variable. In this exercise, you will use an if-else statement on the output expression of the list.\n",
    "\n",
    "You will work on the same list, fellowship and, using a list comprehension and an if-else conditional statement in the output expression, create a list that keeps members of fellowship with 7 or more characters and replaces others with an empty string. Use member as the iterator variable in the list comprehension."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6d73b2a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['', 'samwise', '', 'aragorn', 'legolas', 'boromir', '']\n"
     ]
    }
   ],
   "source": [
    "# Create list comprehension: new_fellowship\n",
    "new_fellowship = [member if len(member) >= 7 else \"\" for member in fellowship]\n",
    "\n",
    "# Print the new list\n",
    "print(new_fellowship)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9728d915",
   "metadata": {},
   "source": [
    "### Dict comprehensions\n",
    "Comprehensions aren't relegated merely to the world of lists. There are many other objects you can build using comprehensions, such as dictionaries, pervasive objects in Data Science. You will create a dictionary using the comprehension syntax for this exercise. In this case, the comprehension is called a `dict comprehension`.\n",
    "\n",
    "The main difference between a list comprehension and a dict comprehension is the use of curly braces {} instead of []. Additionally, members of the dictionary are created using a colon :, as in <key> : <value>.\n",
    "\n",
    "You are given a list of strings fellowship and, using a dict comprehension, create a dictionary with the members of the list as the keys and the length of each string as the corresponding values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "678b4277",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'frodo': 5, 'samwise': 7, 'merry': 5, 'aragorn': 7, 'legolas': 7, 'boromir': 7, 'gimli': 5}\n"
     ]
    }
   ],
   "source": [
    "# Create dict comprehension: new_fellowship\n",
    "new_fellowship = {member : len(member) for member in fellowship}\n",
    "\n",
    "# Print the new list\n",
    "print(new_fellowship)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf304842",
   "metadata": {},
   "source": [
    "### List comprehensions vs generators \n",
    "list comprehensions and generator expressions look very similar in their syntax, except for the use of parentheses () in generator expressions and brackets [] in list comprehensions.  \n",
    "```python\n",
    "# Generator expression\n",
    "fellow2 = (member for member in fellowship if len(member) >= 7)\n",
    "```  \n",
    "A list comprehension produces a list as output, a generator produces a generator object.\n",
    "\n",
    "### Write your own generator expressions\n",
    "You are familiar with what generators and generator expressions are, as well as its difference from list comprehensions. In this exercise, you will practice building generator expressions on your own.\n",
    "\n",
    "Recall that generator expressions basically have the same syntax as list comprehensions, except that it uses parentheses () instead of brackets []; this should make things feel familiar! Furthermore, if you have ever iterated over a dictionary with .items(), or used the range() function, for example, you have already encountered and used generators before, without knowing it! When you use these functions, Python creates generators for you behind the scenes.\n",
    "\n",
    "Now, you will start simple by creating a generator object that produces numeric values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b2d69e38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n",
      "21\n",
      "22\n",
      "23\n",
      "24\n",
      "25\n",
      "26\n",
      "27\n",
      "28\n",
      "29\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "# Create generator object: result\n",
    "result = ( num for num in range(0,31))\n",
    "\n",
    "# Print the first 5 values\n",
    "print(next(result))\n",
    "print(next(result))\n",
    "print(next(result))\n",
    "print(next(result))\n",
    "print(next(result))\n",
    "\n",
    "# Print the rest of the values\n",
    "for value in result:\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "14e7c68d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<generator object <genexpr> at 0x0000019C337B7190>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e05fa77",
   "metadata": {},
   "source": [
    "### Changing the output in generator expressions\n",
    "Great! At this point, you already know how to write a basic generator expression. In this exercise, you will push this idea a little further by adding to the output expression of a generator expression. Because generator expressions and list comprehensions are so alike in syntax, this should be a familiar task for you!\n",
    "\n",
    "You are given a list of strings lannister and, using a generator expression, create a generator object that you will iterate over to print its values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4983b590",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "5\n",
      "5\n",
      "6\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "# Create a list of strings: lannister\n",
    "lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']\n",
    "\n",
    "# Create a generator object: lengths\n",
    "lengths = (len(person) for person in lannister)\n",
    "\n",
    "# Iterate over and print the values in lengths\n",
    "for value in lengths:\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90f4da75",
   "metadata": {},
   "source": [
    "### Build a generator\n",
    "In previous exercises, you've dealt mainly with writing generator expressions, which uses comprehension syntax. Being able to use comprehension syntax for generator expressions made your work so much easier!\n",
    "\n",
    "Not only are there generator expressions, there are generator functions as well. Generator functions are functions that, like generator expressions, yield a series of values, instead of returning a single value. A generator function is defined as you do a regular function, but whenever it generates a value, it uses the keyword yield instead of return.\n",
    "\n",
    "In this exercise, you will create a generator function with a similar mechanism as the generator expression you defined in the previous exercise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "22ba8c44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "5\n",
      "5\n",
      "6\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "# Define generator function get_lengths\n",
    "def get_lengths(input_list):\n",
    "    \"\"\"Generator function that yields the\n",
    "    length of the strings in input_list.\"\"\"\n",
    "\n",
    "    # Yield the length of a string\n",
    "    for person in input_list:\n",
    "        yield len(person)\n",
    "\n",
    "# Print the values generated by get_lengths()\n",
    "for value in get_lengths(lannister):\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ecbfe4b",
   "metadata": {},
   "source": [
    "### List comprehensions for time-stamped data\n",
    "You will now make use of what you've learned from this chapter to solve a simple data extraction problem. You will also be introduced to a data structure, the pandas Series, in this exercise. We won't elaborate on it much here, but what you should know is that it is a data structure that you will be working with a lot of times when analyzing data from pandas DataFrames. You can think of DataFrame columns as single-dimension arrays called Series.\n",
    "\n",
    "In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b9d81ae1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>contributors</th>\n",
       "      <th>coordinates</th>\n",
       "      <th>created_at</th>\n",
       "      <th>entities</th>\n",
       "      <th>extended_entities</th>\n",
       "      <th>favorite_count</th>\n",
       "      <th>favorited</th>\n",
       "      <th>filter_level</th>\n",
       "      <th>geo</th>\n",
       "      <th>id</th>\n",
       "      <th>...</th>\n",
       "      <th>quoted_status_id</th>\n",
       "      <th>quoted_status_id_str</th>\n",
       "      <th>retweet_count</th>\n",
       "      <th>retweeted</th>\n",
       "      <th>retweeted_status</th>\n",
       "      <th>source</th>\n",
       "      <th>text</th>\n",
       "      <th>timestamp_ms</th>\n",
       "      <th>truncated</th>\n",
       "      <th>user</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tue Mar 29 23:40:17 +0000 2016</td>\n",
       "      <td>{'hashtags': [], 'user_mentions': [{'screen_na...</td>\n",
       "      <td>{'media': [{'sizes': {'large': {'w': 1024, 'h'...</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>low</td>\n",
       "      <td>NaN</td>\n",
       "      <td>714960401759387648</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>{'retweeted': False, 'text': \".@krollbondratin...</td>\n",
       "      <td>&lt;a href=\"http://twitter.com\" rel=\"nofollow\"&gt;Tw...</td>\n",
       "      <td>RT @bpolitics: .@krollbondrating's Christopher...</td>\n",
       "      <td>1459294817758</td>\n",
       "      <td>False</td>\n",
       "      <td>{'utc_offset': 3600, 'profile_image_url_https'...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tue Mar 29 23:40:17 +0000 2016</td>\n",
       "      <td>{'hashtags': [{'text': 'cruzsexscandal', 'indi...</td>\n",
       "      <td>{'media': [{'sizes': {'large': {'w': 500, 'h':...</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>low</td>\n",
       "      <td>NaN</td>\n",
       "      <td>714960401977319424</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>{'retweeted': False, 'text': '@dmartosko Cruz ...</td>\n",
       "      <td>&lt;a href=\"http://twitter.com\" rel=\"nofollow\"&gt;Tw...</td>\n",
       "      <td>RT @HeidiAlpine: @dmartosko Cruz video found.....</td>\n",
       "      <td>1459294817810</td>\n",
       "      <td>False</td>\n",
       "      <td>{'utc_offset': None, 'profile_image_url_https'...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tue Mar 29 23:40:17 +0000 2016</td>\n",
       "      <td>{'hashtags': [], 'user_mentions': [], 'symbols...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>low</td>\n",
       "      <td>NaN</td>\n",
       "      <td>714960402426236928</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>&lt;a href=\"http://www.facebook.com/twitter\" rel=...</td>\n",
       "      <td>Njihuni me Zonjën Trump !!! | Ekskluzive https...</td>\n",
       "      <td>1459294817917</td>\n",
       "      <td>False</td>\n",
       "      <td>{'utc_offset': 7200, 'profile_image_url_https'...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tue Mar 29 23:40:17 +0000 2016</td>\n",
       "      <td>{'hashtags': [], 'user_mentions': [], 'symbols...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>low</td>\n",
       "      <td>NaN</td>\n",
       "      <td>714960402367561730</td>\n",
       "      <td>...</td>\n",
       "      <td>7.149239e+17</td>\n",
       "      <td>7.149239e+17</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>&lt;a href=\"http://twitter.com/download/android\" ...</td>\n",
       "      <td>Your an idiot she shouldn't have tried to grab...</td>\n",
       "      <td>1459294817903</td>\n",
       "      <td>False</td>\n",
       "      <td>{'utc_offset': None, 'profile_image_url_https'...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tue Mar 29 23:40:17 +0000 2016</td>\n",
       "      <td>{'hashtags': [], 'user_mentions': [{'screen_na...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>low</td>\n",
       "      <td>NaN</td>\n",
       "      <td>714960402149416960</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>{'retweeted': False, 'text': 'The anti-America...</td>\n",
       "      <td>&lt;a href=\"http://twitter.com/download/iphone\" r...</td>\n",
       "      <td>RT @AlanLohner: The anti-American D.C. elites ...</td>\n",
       "      <td>1459294817851</td>\n",
       "      <td>False</td>\n",
       "      <td>{'utc_offset': -18000, 'profile_image_url_http...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 31 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   contributors  coordinates                      created_at  \\\n",
       "0           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   \n",
       "1           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   \n",
       "2           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   \n",
       "3           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   \n",
       "4           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   \n",
       "\n",
       "                                            entities  \\\n",
       "0  {'hashtags': [], 'user_mentions': [{'screen_na...   \n",
       "1  {'hashtags': [{'text': 'cruzsexscandal', 'indi...   \n",
       "2  {'hashtags': [], 'user_mentions': [], 'symbols...   \n",
       "3  {'hashtags': [], 'user_mentions': [], 'symbols...   \n",
       "4  {'hashtags': [], 'user_mentions': [{'screen_na...   \n",
       "\n",
       "                                   extended_entities  favorite_count  \\\n",
       "0  {'media': [{'sizes': {'large': {'w': 1024, 'h'...               0   \n",
       "1  {'media': [{'sizes': {'large': {'w': 500, 'h':...               0   \n",
       "2                                                NaN               0   \n",
       "3                                                NaN               0   \n",
       "4                                                NaN               0   \n",
       "\n",
       "   favorited filter_level  geo                  id  ...  quoted_status_id  \\\n",
       "0      False          low  NaN  714960401759387648  ...               NaN   \n",
       "1      False          low  NaN  714960401977319424  ...               NaN   \n",
       "2      False          low  NaN  714960402426236928  ...               NaN   \n",
       "3      False          low  NaN  714960402367561730  ...      7.149239e+17   \n",
       "4      False          low  NaN  714960402149416960  ...               NaN   \n",
       "\n",
       "  quoted_status_id_str  retweet_count  retweeted  \\\n",
       "0                  NaN              0      False   \n",
       "1                  NaN              0      False   \n",
       "2                  NaN              0      False   \n",
       "3         7.149239e+17              0      False   \n",
       "4                  NaN              0      False   \n",
       "\n",
       "                                    retweeted_status  \\\n",
       "0  {'retweeted': False, 'text': \".@krollbondratin...   \n",
       "1  {'retweeted': False, 'text': '@dmartosko Cruz ...   \n",
       "2                                                NaN   \n",
       "3                                                NaN   \n",
       "4  {'retweeted': False, 'text': 'The anti-America...   \n",
       "\n",
       "                                              source  \\\n",
       "0  <a href=\"http://twitter.com\" rel=\"nofollow\">Tw...   \n",
       "1  <a href=\"http://twitter.com\" rel=\"nofollow\">Tw...   \n",
       "2  <a href=\"http://www.facebook.com/twitter\" rel=...   \n",
       "3  <a href=\"http://twitter.com/download/android\" ...   \n",
       "4  <a href=\"http://twitter.com/download/iphone\" r...   \n",
       "\n",
       "                                                text   timestamp_ms truncated  \\\n",
       "0  RT @bpolitics: .@krollbondrating's Christopher...  1459294817758     False   \n",
       "1  RT @HeidiAlpine: @dmartosko Cruz video found.....  1459294817810     False   \n",
       "2  Njihuni me Zonjën Trump !!! | Ekskluzive https...  1459294817917     False   \n",
       "3  Your an idiot she shouldn't have tried to grab...  1459294817903     False   \n",
       "4  RT @AlanLohner: The anti-American D.C. elites ...  1459294817851     False   \n",
       "\n",
       "                                                user  \n",
       "0  {'utc_offset': 3600, 'profile_image_url_https'...  \n",
       "1  {'utc_offset': None, 'profile_image_url_https'...  \n",
       "2  {'utc_offset': 7200, 'profile_image_url_https'...  \n",
       "3  {'utc_offset': None, 'profile_image_url_https'...  \n",
       "4  {'utc_offset': -18000, 'profile_image_url_http...  \n",
       "\n",
       "[5 rows x 31 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('datasets/tweets.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c831aee2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['23:40:17', '23:40:17', '23:40:17', '23:40:17', '23:40:17', '23:40:17', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:19', '23:40:18', '23:40:18', '23:40:18', '23:40:19', '23:40:19', '23:40:19', '23:40:18', '23:40:19', '23:40:19', '23:40:19', '23:40:18', '23:40:19', '23:40:19', '23:40:19', '23:40:18', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19']\n"
     ]
    }
   ],
   "source": [
    "# Extract the created_at column from df: tweet_time\n",
    "tweet_time = df['created_at']\n",
    "\n",
    "# Extract the clock time: tweet_clock_time\n",
    "tweet_clock_time = [entry[11:19] for entry in tweet_time]\n",
    "\n",
    "# Print the extracted times\n",
    "print(tweet_clock_time)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5d257db",
   "metadata": {},
   "source": [
    "### Conditional list comprehensions for time-stamped data\n",
    "Great, you've successfully extracted the data of interest, the time, from a pandas DataFrame! Let's tweak your work further by adding a conditional that further specifies which entries to select.\n",
    "\n",
    "In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. You will add a conditional expression to the list comprehension so that you only select the times in which entry[17:19] is equal to '19'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a3e73f42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19']\n"
     ]
    }
   ],
   "source": [
    "# Extract the clock time: tweet_clock_time\n",
    "tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']\n",
    "\n",
    "# Print the extracted times\n",
    "print(tweet_clock_time)"
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
