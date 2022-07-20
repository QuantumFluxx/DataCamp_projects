{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Lambda functions and error-handling"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Herein, you'll learn about lambda functions, which allow you to write functions quickly and on-the-fly. You'll also get practice at handling errors that your functions, at some point, will inevitably throw. You'll wrap up once again applying these skills to Data Science questions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Pop quiz on lambda functions\n",
    "In this exercise, you will practice writing a simple lambda function and calling this function. Recall what you know about lambda functions and answer the following questions:\n",
    "\n",
    "How would you write a lambda function add_bangs that adds three exclamation points '!!!' to the end of a string a?\n",
    "How would you call add_bangs with the argument 'hello'?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "add_bangs = lambda a : a + '!!!'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello!!!'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add_bangs('hello')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing a lambda function you already know\n",
    "Some function definitions are simple enough that they can be converted to a lambda function. By doing this, you write less lines of code, which is pretty awesome and will come in handy, especially when you're writing and maintaining big programs. In this exercise, you will use what you know about lambda functions to convert a function that does a simple task into a lambda function. Take a look at this function definition:\n",
    "\n",
    "```python\n",
    "def echo_word(word1, echo):\n",
    "    \"\"\"Concatenate echo copies of word1.\"\"\"\n",
    "    words = word1 * echo\n",
    "    return words\n",
    "```\n",
    "The function echo_word takes 2 parameters: a string value, word1 and an integer value, echo. It returns a string that is a concatenation of echo copies of word1. Your task is to convert this simple function into a lambda function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "heyheyheyheyhey\n"
     ]
    }
   ],
   "source": [
    "# Define echo_word as a lambda function: echo_word\n",
    "echo_word = (lambda word1, echo : echo*word1)\n",
    "\n",
    "# Call echo_word: result\n",
    "result = echo_word('hey', 5)\n",
    "\n",
    "# Print result\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Map() and lambda functions\n",
    "So far, you've used lambda functions to write short, simple functions as well as to redefine functions with simple functionality. The best use case for lambda functions, however, are for when you want these simple functionalities to be anonymously embedded within larger expressions. What that means is that the functionality is not stored in the environment, unlike a function defined with def. To understand this idea better, you will use a lambda function in the context of the map() function.\n",
    "\n",
    "map() applies a function over an object, such as a list. Here, you can use lambda functions to define the function that map() will use to process the object. For example:\n",
    "\n",
    "```python\n",
    "nums = [2, 4, 6, 8, 10]  \n",
    "\n",
    "result = map(lambda a: a ** 2, nums)  \n",
    "```\n",
    "You can see here that a lambda function, which raises a value a to the power of 2, is passed to map() alongside a list of numbers, nums. The map object that results from the call to map() is stored in result. You will now practice the use of lambda functions with map(). For this exercise, you will map the functionality of the add_bangs() function you defined in previous exercises over a list of strings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['protego!!!', 'accio!!!', 'expecto patronum!!!', 'legilimens!!!']\n"
     ]
    }
   ],
   "source": [
    "# Create a list of strings: spells\n",
    "spells = [\"protego\", \"accio\", \"expecto patronum\", \"legilimens\"]\n",
    "\n",
    "# Use map() to apply a lambda function over spells: shout_spells\n",
    "shout_spells = map(lambda item : item + '!!!', spells)\n",
    "\n",
    "# Convert shout_spells to a list: shout_spells_list\n",
    "shout_spells_list = list(shout_spells)\n",
    "\n",
    "# Convert shout_spells into a list and print it\n",
    "print(shout_spells_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Filter() and lambda functions\n",
    "In the previous exercise, you used lambda functions to anonymously embed an operation within map(). You will practice this again in this exercise by using a lambda function with filter(), which may be new to you! The function filter() offers a way to filter out elements from a list that don't satisfy certain criteria.\n",
    "\n",
    "Your goal in this exercise is to use filter() to create, from an input list of strings, a new list that contains only strings that have more than 6 characters."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['samwise', 'aragorn', 'boromir', 'legolas', 'gandalf']\n"
     ]
    }
   ],
   "source": [
    "# Create a list of strings: fellowship\n",
    "fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']\n",
    "\n",
    "# Use filter() to apply a lambda function over fellowship: result\n",
    "result = filter(lambda member: len(member) > 6, fellowship)\n",
    "\n",
    "# Convert result to a list: result_list\n",
    "result_list = list(result)\n",
    "\n",
    "# Convert result into a list and print it\n",
    "print(result_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Reduce() and lambda functions\n",
    "You're getting very good at using lambda functions! Here's one more function to add to your repertoire of skills. The reduce() function is useful for performing some computation on a list and, unlike map() and filter(), returns a single value as a result. To use reduce(), you must import it from the functools module.\n",
    "\n",
    "Remember gibberish() from a few exercises back?\n",
    "\n",
    "```python\n",
    "# Define gibberish\n",
    "def gibberish(*args):\n",
    "    \"\"\"Concatenate strings in *args together.\"\"\"\n",
    "    hodgepodge = ''\n",
    "    for word in args:\n",
    "        hodgepodge += word\n",
    "    return hodgepodge\n",
    "```\n",
    "gibberish() simply takes a list of strings as an argument and returns, as a single-value result, the concatenation of all of these strings. In this exercise, you will replicate this functionality by using reduce() and a lambda function that concatenates strings together."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "robbsansaaryabrandonrickon\n"
     ]
    }
   ],
   "source": [
    "# Import reduce from functools\n",
    "from functools import reduce\n",
    "\n",
    "# Create a list of strings: stark\n",
    "stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']\n",
    "\n",
    "# Use reduce() to apply a lambda function over stark: result\n",
    "result = reduce(lambda item1, item2 : item1 + item2, stark)\n",
    "\n",
    "# Print the result\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Error handling with try-except\n",
    "A good practice in writing your own functions is also anticipating the ways in which other people (or yourself, if you accidentally misuse your own function) might use the function you defined.\n",
    "\n",
    "As in the previous exercise, you saw that the len() function is able to handle input arguments such as strings, lists, and tuples, but not int type ones and raises an appropriate error and error message when it encounters invalid input arguments. One way of doing this is through exception handling with the try-except block.\n",
    "\n",
    "In this exercise, you will define a function as well as use a try-except block for handling cases when incorrect input arguments are passed to the function.\n",
    "\n",
    "Recall the shout_echo() function you defined in previous exercises; parts of the function definition are provided in the sample code. Your goal is to complete the exception handling code in the function definition and provide an appropriate error message when raising an error."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "word1 must be a string and echo must be an integer.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define shout_echo\n",
    "def shout_echo(word1, echo=1):\n",
    "    \"\"\"Concatenate echo copies of word1 and three\n",
    "    exclamation marks at the end of the string.\"\"\"\n",
    "\n",
    "    # Initialize empty strings: echo_word, shout_words\n",
    "    echo_word = \"\"\n",
    "    shout_words = \"\"\n",
    "    \n",
    "\n",
    "    # Add exception handling with try-except\n",
    "    try:\n",
    "        # Concatenate echo copies of word1 using *: echo_word\n",
    "        echo_word = echo * word1\n",
    "\n",
    "        # Concatenate '!!!' to echo_word: shout_words\n",
    "        shout_words = echo_word + '!!!'\n",
    "    except:\n",
    "        # Print error message\n",
    "        print(\"word1 must be a string and echo must be an integer.\")\n",
    "\n",
    "    # Return shout_words\n",
    "    return shout_words\n",
    "\n",
    "# Call shout_echo\n",
    "shout_echo(\"particle\", echo=\"accelerator\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Error handling by raising an error\n",
    "Another way to raise an error is by using raise. In this exercise, you will add a raise statement to the shout_echo() function you defined before to raise an error message when the value supplied by the user to the echo argument is less than 0.\n",
    "\n",
    "The call to shout_echo() uses valid argument values. To test and see how the raise statement works, simply change the value for the echo argument to a negative value. Don't forget to change it back to valid values to move on to the next exercise!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'particleparticleparticleparticleparticle!!!'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define shout_echo\n",
    "def shout_echo(word1, echo=1):\n",
    "    \"\"\"Concatenate echo copies of word1 and three\n",
    "    exclamation marks at the end of the string.\"\"\"\n",
    "\n",
    "    # Raise an error with raise\n",
    "    if echo < 0:\n",
    "        raise ValueError('echo must be greater than 0')\n",
    "\n",
    "    # Concatenate echo copies of word1 using *: echo_word\n",
    "    echo_word = word1 * echo\n",
    "\n",
    "    # Concatenate '!!!' to echo_word: shout_word\n",
    "    shout_word = echo_word + '!!!'\n",
    "\n",
    "    # Return shout_word\n",
    "    return shout_word\n",
    "\n",
    "# Call shout_echo\n",
    "shout_echo(\"particle\", echo=5)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Bringing it all together (1)\n",
    "This is awesome! You have now learned how to write anonymous functions using lambda, how to pass lambda functions as arguments to other functions such as map(), filter(), and reduce(), as well as how to write errors and output custom error messages within your functions. You will now put together these learnings to good use by working with a Twitter dataset. Before practicing your new error handling skills,in this exercise, you will write a lambda function and use filter() to select retweets, that is, tweets that begin with the string 'RT'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RT @bpolitics: .@krollbondrating's Christopher Whalen says Clinton is the weakest Dem candidate in 50 years https://t.co/pLk7rvoRSn https:/…\n",
      "RT @HeidiAlpine: @dmartosko Cruz video found.....racing from the scene.... #cruzsexscandal https://t.co/zuAPZfQDk3\n",
      "RT @AlanLohner: The anti-American D.C. elites despise Trump for his America-first foreign policy. Trump threatens their gravy train. https:…\n",
      "RT @BIackPplTweets: Young Donald trump meets his neighbor  https://t.co/RFlu17Z1eE\n",
      "RT @trumpresearch: @WaitingInBagdad @thehill Trump supporters have selective amnisia.\n",
      "RT @HouseCracka: 29,000+ PEOPLE WATCHING TRUMP LIVE ON ONE STREAM!!!\n",
      "\n",
      "https://t.co/7QCFz9ehNe\n",
      "RT @urfavandtrump: RT for Brendon Urie\n",
      "Fav for Donald Trump https://t.co/PZ5vS94lOg\n",
      "RT @trapgrampa: This is how I see #Trump every time he speaks. https://t.co/fYSiHNS0nT\n",
      "RT @trumpresearch: @WaitingInBagdad @thehill Trump supporters have selective amnisia.\n",
      "RT @Pjw20161951: NO KIDDING: #SleazyDonald just attacked Scott Walker for NOT RAISING TAXES in WI! #LyinTrump\n",
      "#NeverTrump  #CruzCrew  https…\n",
      "RT @urfavandtrump: RT for Brendon Urie\n",
      "Fav for Donald Trump https://t.co/PZ5vS94lOg\n",
      "RT @ggreenwald: The media spent all day claiming @SusanSarandon said she might vote for Trump. A total fabrication, but whatever... https:/…\n",
      "RT @Pjw20161951: NO KIDDING: #SleazyDonald just attacked Scott Walker for NOT RAISING TAXES in WI! #LyinTrump\n",
      "#NeverTrump  #CruzCrew  https…\n",
      "RT @trapgrampa: This is how I see #Trump every time he speaks. https://t.co/fYSiHNS0nT\n",
      "RT @mitchellvii: So let me get this straight.  Any reporter can assault Mr Trump at any time and Corey can do nothing?  Michelle is clearly…\n",
      "RT @paulbenedict7: How #Trump Sacks RINO Strongholds by Hitting Positions Held by Dems and GOP https://t.co/D7ulnAJhis   #tcot #PJNET https…\n",
      "RT @DRUDGE_REPORT: VIDEO:  Trump emotional moment with Former Miss Wisconsin who has terminal illness... https://t.co/qt06aG9inT\n",
      "RT @ggreenwald: The media spent all day claiming @SusanSarandon said she might vote for Trump. A total fabrication, but whatever... https:/…\n",
      "RT @DennisApgar: Thank God I seen Trump at first stop in Wisconsin media doesn't know how great he is, advice watch live streaming https://…\n",
      "RT @paulbenedict7: How #Trump Sacks RINO Strongholds by Hitting Positions Held by Dems and GOP https://t.co/D7ulnAJhis   #tcot #PJNET https…\n",
      "RT @DRUDGE_REPORT: VIDEO:  Trump emotional moment with Former Miss Wisconsin who has terminal illness... https://t.co/qt06aG9inT\n",
      "RT @DennisApgar: Thank God I seen Trump at first stop in Wisconsin media doesn't know how great he is, advice watch live streaming https://…\n",
      "RT @mitchellvii: So let me get this straight.  Any reporter can assault Mr Trump at any time and Corey can do nothing?  Michelle is clearly…\n",
      "RT @sciam: Trump's idiosyncratic patterns of speech are why people tend either to love or hate him https://t.co/QXwquVgs3c https://t.co/P9N…\n",
      "RT @Norsu2: Nightmare WI poll for Ted Cruz has Kasich surging: Trump 29, Kasich 27, Cruz 25. https://t.co/lJsgbLYY1P #NeverTrump\n",
      "RT @thehill: WATCH: Protester pepper-sprayed point blank at Trump rally https://t.co/B5f65Al9ld https://t.co/skAfByXuQc\n",
      "RT @sciam: Trump's idiosyncratic patterns of speech are why people tend either to love or hate him https://t.co/QXwquVgs3c https://t.co/P9N…\n",
      "RT @ggreenwald: The media spent all day claiming @SusanSarandon said she might vote for Trump. A total fabrication, but whatever... https:/…\n",
      "RT @DebbieStout5: Wow! Last I checked it was just 12 points &amp; that wasn't more than a day ago. Oh boy Trump ppl might want to rethink🤔 http…\n",
      "RT @tyleroakley: i'm a messy bitch, but at least i'm not voting for trump\n",
      "RT @vandives: Trump supporters r tired of justice NOT being served. There's no justice anymore. Hardworking Americans get screwed. That's n…\n",
      "RT @AP: BREAKING: Trump vows to stand by campaign manager charged with battery, says he does not discard people.\n",
      "RT @AP: BREAKING: Trump vows to stand by campaign manager charged with battery, says he does not discard people.\n",
      "RT @urfavandtrump: RT for Jerrie (Little Mix)\n",
      "Fav for Donald Trump https://t.co/nEVxElW6iG\n",
      "RT @urfavandtrump: RT for Jerrie (Little Mix)\n",
      "Fav for Donald Trump https://t.co/nEVxElW6iG\n",
      "RT @NoahCRothman: When Walker was fighting for reforms, Trump was defending unions and collective bargaining privileges https://t.co/e1UWNN…\n",
      "RT @RedheadAndRight: Report: Secret Service Says Michelle Fields Touched Trump https://t.co/c5c2sD8VO2\n",
      "\n",
      "This is the only article you will n…\n",
      "RT @AIIAmericanGirI: VIDEO=&gt; Anti-Trump Protester SLUGS Elderly Trump Supporter in the Face\n",
      "https://t.co/GeEryMDuDY\n",
      "RT @NoahCRothman: When Walker was fighting for reforms, Trump was defending unions and collective bargaining privileges https://t.co/e1UWNN…\n",
      "RT @JusticeRanger1: @realDonaldTrump @Pudingtane @DanScavino @GOP @infowars @EricTrump \n",
      "URGENT PUBLIC TRUMP ALERT:\n",
      "COVERT KILL MEANS https:…\n",
      "RT @AIIAmericanGirI: VIDEO=&gt; Anti-Trump Protester SLUGS Elderly Trump Supporter in the Face\n",
      "https://t.co/GeEryMDuDY\n",
      "RT @RedheadAndRight: Report: Secret Service Says Michelle Fields Touched Trump https://t.co/c5c2sD8VO2\n",
      "\n",
      "This is the only article you will n…\n",
      "RT @JusticeRanger1: @realDonaldTrump @Pudingtane @DanScavino @GOP @infowars @EricTrump \n",
      "URGENT PUBLIC TRUMP ALERT:\n",
      "COVERT KILL MEANS https:…\n",
      "RT @Schneider_CM: Trump says nobody had ever heard of executive orders before Obama started signing them. Never heard of the Emancipation P…\n",
      "RT @RonBasler1: @DavidWhitDennis @realDonaldTrump @tedcruz \n",
      "\n",
      "CRUZ SCREWS HOOKERS\n",
      "\n",
      "CRUZ / CLINTON\n",
      "RT @DonaldsAngel: Former Ms. WI just said that she is terminally ill but because of Trump pageant, her 7 yr. old son has his college educat…\n",
      "RT @Schneider_CM: Trump says nobody had ever heard of executive orders before Obama started signing them. Never heard of the Emancipation P…\n",
      "RT @DonaldsAngel: Former Ms. WI just said that she is terminally ill but because of Trump pageant, her 7 yr. old son has his college educat…\n",
      "RT @Dodarey: @DR8801 @SykesCharlie Charlie, let's see you get a straight \"yes\" or \"no\" answer from Cruz a/b being unfaithful to his wife @T…\n",
      "RT @RonBasler1: @DavidWhitDennis @realDonaldTrump @tedcruz \n",
      "\n",
      "CRUZ SCREWS HOOKERS\n",
      "\n",
      "CRUZ / CLINTON\n",
      "RT @RockCliffOne: Remember when the idea of a diabolical moron holding the world hostage was an idea for a funny movie? #Trump #GOP https:/…\n",
      "RT @HillaryClinton: \"Every day, another Republican bemoans the rise of Donald Trump... but [he] didn’t come out of nowhere.\" —Hillary\n",
      "https…\n",
      "RT @Dodarey: @DR8801 @SykesCharlie Charlie, let's see you get a straight \"yes\" or \"no\" answer from Cruz a/b being unfaithful to his wife @T…\n",
      "RT @HillaryClinton: \"Every day, another Republican bemoans the rise of Donald Trump... but [he] didn’t come out of nowhere.\" —Hillary\n",
      "https…\n",
      "RT @RockCliffOne: Remember when the idea of a diabolical moron holding the world hostage was an idea for a funny movie? #Trump #GOP https:/…\n",
      "RT @immigrant4trump: @immigrant4trump msm, cable news attacking trump all day, from 8am to 10pm today, then the reruns come on, repeating t…\n",
      "RT @immigrant4trump: @immigrant4trump msm, cable news attacking trump all day, from 8am to 10pm today, then the reruns come on, repeating t…\n",
      "RT @GlendaJazzey: Donald Trump’s Campaign Financing Dodge, @rrotunda https://t.co/L8flI4lswG via @VerdictJustia\n",
      "RT @TUSK81: LOUDER FOR THE PEOPLE IN THE BACK https://t.co/hlPVyNLXzx\n",
      "RT @loopzoop: Well...put it back https://t.co/8Yb7BDT5VM\n",
      "RT @claytoncubitt: Stop asking Bernie supporters if they’ll vote for Hillary against Trump. We got a plan to beat Trump already. Called Ber…\n",
      "RT @akaMaude13: Seriously can't make this up. What a joke. #NeverTrump  https://t.co/JkTx6mdRgC\n"
     ]
    }
   ],
   "source": [
    "# Select retweets from the Twitter DataFrame: result\n",
    "result = filter(lambda x: x[0:2] == 'RT', df['text'])\n",
    "\n",
    "# Create list from filter object result: res_list\n",
    "res_list = list(result)\n",
    "\n",
    "# Print all retweets in res_list\n",
    "for tweet in res_list:\n",
    "    print(tweet)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Bringing it all together (2)\n",
    "Sometimes, we make mistakes when calling functions - even ones you made yourself. But don't fret! In this exercise, you will improve on your previous work with the count_entries() function in the last chapter by adding a try-except block to it. This will allow your function to provide a helpful message when the user calls your count_entries() function but provides a column name that isn't in the DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
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
    "def count_entries(df, col_name='lang'):\n",
    "    \"\"\"Return a dictionary with counts of\n",
    "    occurrences as value for each key.\"\"\"\n",
    "\n",
    "    # Initialize an empty dictionary: cols_count\n",
    "    cols_count = {}\n",
    "\n",
    "    # Add try block\n",
    "    try:\n",
    "        # Extract column from DataFrame: col\n",
    "        col = df[col_name]\n",
    "        \n",
    "        # Iterate over the column in dataframe\n",
    "        for entry in col:\n",
    "    \n",
    "            # If entry is in cols_count, add 1\n",
    "            if entry in cols_count.keys():\n",
    "                cols_count[entry] += 1\n",
    "            # Else add the entry to cols_count, set the value to 1\n",
    "            else:\n",
    "                cols_count[entry] = 1\n",
    "    \n",
    "        # Return the cols_count dictionary\n",
    "        return cols_count\n",
    "\n",
    "    # Add except block\n",
    "    except:\n",
    "        print(\"The DataFrame does not have a \" + col_name + 'column')\n",
    "\n",
    "# Call count_entries(): result1\n",
    "result1 = count_entries(df, 'lang')\n",
    "\n",
    "# Print result1\n",
    "print(result1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Bringing it all together (3)\n",
    "In the previous exercise, you built on your function count_entries() to add a try-except block. This was so that users would get helpful messages when calling your count_entries() function and providing a column name that isn't in the DataFrame. In this exercise, you'll instead raise a ValueError in the case that the user provides a column name that isn't in the DataFrame.\n",
    "\n",
    "Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
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
    "def count_entries(df, col_name='lang'):\n",
    "    \"\"\"Return a dictionary with counts of\n",
    "    occurrences as value for each key.\"\"\"\n",
    "    \n",
    "    # Raise a ValueError if col_name is NOT in DataFrame\n",
    "    if col_name not in df.columns:\n",
    "        raise ValueError('The DataFrame does not have a '+col_name+' column.')\n",
    "\n",
    "    # Initialize an empty dictionary: cols_count\n",
    "    cols_count = {}\n",
    "    \n",
    "    # Extract column from DataFrame: col\n",
    "    col = df[col_name]\n",
    "    \n",
    "    # Iterate over the column in DataFrame\n",
    "    for entry in col:\n",
    "\n",
    "        # If entry is in cols_count, add 1\n",
    "        if entry in cols_count.keys():\n",
    "            cols_count[entry] += 1\n",
    "            # Else add the entry to cols_count, set the value to 1\n",
    "        else:\n",
    "            cols_count[entry] = 1\n",
    "        \n",
    "        # Return the cols_count dictionary\n",
    "    return cols_count\n",
    "\n",
    "# Call count_entries(): result1\n",
    "result1 = count_entries(df)\n",
    "\n",
    "# Print result1\n",
    "print(result1)"
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
 "nbformat_minor": 2
}
