{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "941caf22",
   "metadata": {},
   "source": [
    "# Using iterators in PythonLand\n",
    "\n",
    "### Here, you'll learn all about iterators and iterables, which you have already worked with before when writing for loops! You'll learn about some very useful functions that will allow you to effectively work with iterators and finish the chapter with a use case that is pertinent to the world of Data Science - dealing with large amounts of data - in this case, data from Twitter that you will load in chunks using iterators!\n",
    "\n",
    "### Iterators vs Iterables\n",
    "An iterable is an object that can return an iterator, while an iterator is an object that keeps state and produces the next value when you call next() on it.\n",
    "\n",
    "### Iterating over iterables (1)\n",
    "Great, you're familiar with what iterables and iterators are! In this exercise, you will reinforce your knowledge about these by iterating over and printing from iterables and iterators.\n",
    "\n",
    "You are provided with a list of strings flash. You will practice iterating over the list by using a for loop. You will also create an iterator for the list and access the values from the iterator.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fe2804d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "jay garrick\n",
      "barry allen\n",
      "wally west\n",
      "bart allen\n",
      "jay garrick\n",
      "barry allen\n",
      "wally west\n",
      "bart allen\n"
     ]
    }
   ],
   "source": [
    "# Create a list of strings: flash\n",
    "flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']\n",
    "\n",
    "# Print each list item in flash using a for loop\n",
    "for person in flash:\n",
    "    print(person)\n",
    "\n",
    "\n",
    "# Create an iterator for flash: superspeed\n",
    "superspeed = iter(flash)\n",
    "\n",
    "# Print each item from the iterator\n",
    "print(next(superspeed))\n",
    "print(next(superspeed))\n",
    "print(next(superspeed))\n",
    "print(next(superspeed))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c0b034e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<list_iterator at 0x2ecc7f2d6a0>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "superspeed"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f256462b",
   "metadata": {},
   "source": [
    "### Iterating over iterables (2)\n",
    "One of the things you learned about in this chapter is that not all iterables are actual lists. A couple of examples that we looked at are strings and the use of the range() function. In this exercise, we will focus on the range() function.\n",
    "\n",
    "You can use range() in a for loop as if it's a list to be iterated over:\n",
    "\n",
    "```python\n",
    "for i in range(5):\n",
    "    print(i)\n",
    "``` \n",
    "Recall that range() doesn't actually create the list; instead, it creates a range object with an iterator that produces the values until it reaches the limit (in the example, until the value 4). If range() created the actual list, calling it with a value of 10100 may not work, especially since a number as big as that may go over a regular computer's memory. The value 10100 is actually what's called a __Googol__ which is a 1 followed by a hundred 0s. That's a huge number!\n",
    "\n",
    "Your task for this exercise is to show that calling range() with 10100 won't actually pre-create the list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "89cf4856",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 3)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "44642c5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "0\n",
      "1\n",
      "2\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "# Create an iterator for range(3): small_value\n",
    "small_value = iter(range(3))\n",
    "\n",
    "# Print the values in small_value\n",
    "print(next(small_value))\n",
    "print(next(small_value))\n",
    "print(next(small_value))\n",
    "\n",
    "# Loop over range(3) and print the values\n",
    "for num in range(3):\n",
    "    print(num)\n",
    "\n",
    "\n",
    "# Create an iterator for range(10 ** 100): googol\n",
    "googol = iter(range(10**100))\n",
    "\n",
    "# Print the first 5 values from googol\n",
    "print(next(googol))\n",
    "print(next(googol))\n",
    "print(next(googol))\n",
    "print(next(googol))\n",
    "print(next(googol))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5265f5bb",
   "metadata": {},
   "source": [
    "### Iterators as function arguments\n",
    "You've been using the iter() function to get an iterator object, as well as the next() function to retrieve the values one by one from the iterator object.\n",
    "\n",
    "There are also functions that take iterators and iterables as arguments. For example, the list() and sum() functions return a list and the sum of elements, respectively.\n",
    "\n",
    "In this exercise, you will use these functions by passing an iterable from range() and then printing the results of the function calls."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bcd2d633",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "range(10, 21)\n",
      "[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\n",
      "165\n"
     ]
    }
   ],
   "source": [
    "# Create a range object: values\n",
    "values = range(10,21)\n",
    "\n",
    "# Print the range object\n",
    "print(values)\n",
    "\n",
    "# Create a list of integers: values_list\n",
    "values_list = list(values)\n",
    "\n",
    "# Print values_list\n",
    "print(values_list)\n",
    "\n",
    "# Get the sum of values: values_sum\n",
    "values_sum = sum(values)\n",
    "\n",
    "# Print values_sum\n",
    "print(values_sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3cce5502",
   "metadata": {},
   "source": [
    "### Using enumerate\n",
    "You're really getting the hang of using iterators, great job!\n",
    "\n",
    "You've just gained several new ideas on iterators and one of them is the `enumerate()` function. enumerate() returns an enumerate object that produces a sequence of tuples, and each of the tuples is an index-value pair.\n",
    "\n",
    "In this exercise, you are given a list of strings mutants and you will practice using enumerate() on it by printing out a list of tuples and unpacking the tuples using a for loop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "53d7843f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(0, 'charles xavier'), (1, 'bobby drake'), (2, 'kurt wagner'), (3, 'max eisenhardt'), (4, 'kitty pryde')]\n",
      "0 charles xavier\n",
      "1 bobby drake\n",
      "2 kurt wagner\n",
      "3 max eisenhardt\n",
      "4 kitty pryde\n",
      "1 charles xavier\n",
      "2 bobby drake\n",
      "3 kurt wagner\n",
      "4 max eisenhardt\n",
      "5 kitty pryde\n"
     ]
    }
   ],
   "source": [
    "# Create a list of strings: mutants\n",
    "mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']\n",
    "\n",
    "# Create a list of tuples: mutant_list\n",
    "mutant_list = list(enumerate(mutants))\n",
    "\n",
    "# Print the list of tuples\n",
    "print(mutant_list)\n",
    "\n",
    "# Unpack and print the tuple pairs\n",
    "for index1, value1 in  enumerate(mutants):\n",
    "    print(index1, value1)\n",
    "\n",
    "# Change the start index\n",
    "for index2, value2 in enumerate(mutants, start = 1):\n",
    "    print(index2, value2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19b67cad",
   "metadata": {},
   "source": [
    "### Using zip\n",
    "Another interesting function is `zip()`, which takes any number of iterables and returns a zip object that is an iterator of tuples. If you wanted to print the values of a zip object, you can convert it into a list and then print it. Printing just a zip object will not return the values unless you unpack it first. In this exercise, you will explore this for yourself.\n",
    "\n",
    "Three lists of strings are pre-loaded: mutants, aliases, and powers. First, you will use list() and zip() on these lists to generate a list of tuples. Then, you will create a zip object using zip(). Finally, you will unpack this zip object in a for loop to print the values in each tuple. Observe the different output generated by printing the list of tuples, then the zip object, and finally, the tuple values in the for loop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "73bb8a91",
   "metadata": {},
   "outputs": [],
   "source": [
    "aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']\n",
    "powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5ab278a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('charles xavier', 'prof x', 'telepathy'), ('bobby drake', 'iceman', 'thermokinesis'), ('kurt wagner', 'nightcrawler', 'teleportation'), ('max eisenhardt', 'magneto', 'magnetokinesis'), ('kitty pryde', 'shadowcat', 'intangibility')]\n",
      "<zip object at 0x000002ECC7F5A300>\n",
      "charles xavier prof x telepathy\n",
      "bobby drake iceman thermokinesis\n",
      "kurt wagner nightcrawler teleportation\n",
      "max eisenhardt magneto magnetokinesis\n",
      "kitty pryde shadowcat intangibility\n"
     ]
    }
   ],
   "source": [
    "# Create a list of tuples: mutant_data\n",
    "mutant_data = list(zip(mutants, aliases, powers))\n",
    "\n",
    "# Print the list of tuples\n",
    "print(mutant_data)\n",
    "\n",
    "# Create a zip object using the three lists: mutant_zip\n",
    "mutant_zip = zip(mutants, aliases, powers)\n",
    "\n",
    "# Print the zip object\n",
    "print(mutant_zip)\n",
    "\n",
    "# Unpack the zip object and print the tuple values\n",
    "for value1, value2, value3 in mutant_zip:\n",
    "    print(value1, value2, value3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b04d0b1",
   "metadata": {},
   "source": [
    "### Using * and zip to 'unzip'\n",
    "You know how to use zip() as well as how to print out values from a zip object. Excellent!\n",
    "\n",
    "Let's play around with zip() a little more. There is no unzip function for doing the reverse of what zip() does. We can, however, reverse what has been zipped together by using zip() with a little help from `*`. `*` unpacks an iterable such as a list or a tuple into positional arguments in a function call.\n",
    "\n",
    "In this exercise, you will use * in a call to zip() to unpack the tuples produced by zip().\n",
    "\n",
    "Two tuples of strings, mutants and powers have been pre-loaded."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a850c562",
   "metadata": {},
   "outputs": [],
   "source": [
    "mutants = tuple(mutants)\n",
    "powers = tuple(powers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d09a1ed2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('charles xavier', 'telepathy') ('bobby drake', 'thermokinesis') ('kurt wagner', 'teleportation') ('max eisenhardt', 'magnetokinesis') ('kitty pryde', 'intangibility')\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Create a zip object from mutants and powers: z1\n",
    "z1 = zip(mutants, powers)\n",
    "\n",
    "# Print the tuples in z1 by unpacking with *\n",
    "print(*z1)\n",
    "\n",
    "# Re-create a zip object from mutants and powers: z1\n",
    "z1 = zip(mutants, powers)\n",
    "\n",
    "# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2\n",
    "result1, result2 = zip(*z1)\n",
    "\n",
    "# Check if unpacked tuples are equivalent to original tuples\n",
    "print(result1 == mutants)\n",
    "print(result2 == powers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ba09dbe",
   "metadata": {},
   "source": [
    "### Processing large amounts of Twitter data\n",
    "Sometimes, the data we have to process reaches a size that is too much for a computer's memory to handle. This is a common problem faced by data scientists. A solution to this is to process an entire data source chunk by chunk, instead of a single go all at once.\n",
    "\n",
    "In this exercise, you will do just that. You will process a large csv file of Twitter data in the same way that you processed 'tweets.csv' in Bringing it all together exercises of the prequel course, but this time, working on it in chunks of 10 entries at a time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "775a0ed0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "16e4b3f8",
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
    "# Initialize an empty dictionary: counts_dict\n",
    "counts_dict = {}\n",
    "\n",
    "# Iterate over the file chunk by chunk\n",
    "for chunk in pd.read_csv('datasets/tweets.csv', chunksize=10):\n",
    "\n",
    "    # Iterate over the column in DataFrame\n",
    "    for entry in chunk['lang']:\n",
    "        if entry in counts_dict.keys():\n",
    "            counts_dict[entry] += 1\n",
    "        else:\n",
    "            counts_dict[entry] = 1\n",
    "\n",
    "# Print the populated dictionary\n",
    "print(counts_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da7334ee",
   "metadata": {},
   "source": [
    "### Extracting information for large amounts of Twitter data\n",
    "Great job chunking out that file in the previous exercise. You now know how to deal with situations where you need to process a very large file and that's a very useful skill to have!\n",
    "\n",
    "It's good to know how to process a file in smaller, more manageable chunks, but it can become very tedious having to write and rewrite the same code for the same task each time. In this exercise, you will be making your code more reusable by putting your work in the last exercise in a function definition."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f6788e6d",
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
    "def count_entries(csv_file, c_size, colname):\n",
    "    \"\"\"Return a dictionary with counts of\n",
    "    occurrences as value for each key.\"\"\"\n",
    "    \n",
    "    # Initialize an empty dictionary: counts_dict\n",
    "    counts_dict = {}\n",
    "\n",
    "    # Iterate over the file chunk by chunk\n",
    "    for chunk in pd.read_csv(csv_file, chunksize = c_size):\n",
    "\n",
    "        # Iterate over the column in DataFrame\n",
    "        for entry in chunk[colname]:\n",
    "            if entry in counts_dict.keys():\n",
    "                counts_dict[entry] += 1\n",
    "            else:\n",
    "                counts_dict[entry] = 1\n",
    "\n",
    "    # Return counts_dict\n",
    "    return counts_dict\n",
    "\n",
    "# Call count_entries(): result_counts\n",
    "result_counts = count_entries('datasets/tweets.csv', 10, 'lang')\n",
    "\n",
    "# Print result_counts\n",
    "print(result_counts)"
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
