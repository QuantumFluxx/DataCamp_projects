{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "70912b43",
   "metadata": {},
   "source": [
    "# Diving deep into the Twitter API\n",
    "\n",
    "## Streaming tweets\n",
    "It's time to stream some tweets! Your task is to create the Streamobject and to filter tweets according to particular keywords. tweepy has been imported for you.\n",
    "\n",
    "* Create your Stream object with the credentials given.\n",
    "* Filter your Stream variable for the keywords \"clinton\", \"trump\", \"sanders\", and \"cruz\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "827a9bbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tweepy\n",
    "\n",
    "# Store credentials in relevant variables\n",
    "consumer_key = \"nZ6EA0FxZ293SxGNg8g8aP0HM\"\n",
    "consumer_secret = \"fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i\"\n",
    "access_token = \"1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy\"\n",
    "access_token_secret = \"X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx\"\n",
    "\n",
    "# Create your Stream object with credentials\n",
    "stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)\n",
    "\n",
    "# Filter your Stream variable\n",
    "stream.filter(track=[\"clinton\", \"trump\", \"sanders\", \"cruz\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "194f745d",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Load and explore your Twitter data\n",
    "Now that you've got your Twitter data sitting locally in a text file, it's time to explore it! This is what you'll do in the next few interactive exercises. In this exercise, you'll read the Twitter data into a list: `tweets_data`.\n",
    "\n",
    "Be aware that this is real data from Twitter and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real Twitter data).\n",
    "\n",
    "* Assign the filename `'tweets.txt'` to the variable `tweets_data_path`.\n",
    "* Initialize `tweets_data` as an empty list to store the tweets in.\n",
    "* Within the for loop initiated by for line in tweets_file:, load each tweet into a variable, tweet, using `json.loads()`, then append tweet to tweets_data using the `append()` method.\n",
    "* Hit submit and check out the keys of the first tweet dictionary printed to the shell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "94c7e9ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['in_reply_to_user_id', 'created_at', 'filter_level', 'truncated', 'possibly_sensitive', 'timestamp_ms', 'user', 'text', 'extended_entities', 'in_reply_to_status_id', 'entities', 'favorited', 'retweeted', 'is_quote_status', 'id', 'favorite_count', 'retweeted_status', 'in_reply_to_status_id_str', 'in_reply_to_user_id_str', 'id_str', 'in_reply_to_screen_name', 'coordinates', 'lang', 'place', 'contributors', 'geo', 'retweet_count', 'source'])\n"
     ]
    }
   ],
   "source": [
    "# Import package\n",
    "import json\n",
    "\n",
    "# String of path to file: tweets_data_path\n",
    "tweets_data_path = 'datasets/tweets.txt'\n",
    "\n",
    "# Initialize empty list to store tweets: tweets_data\n",
    "tweets_data = []\n",
    "\n",
    "# Open connection to file\n",
    "tweets_file = open(tweets_data_path, \"r\")\n",
    "\n",
    "# Read in tweets and store in list: tweets_data\n",
    "for line in tweets_file:\n",
    "    tweet = json.loads(line)\n",
    "    tweets_data.append(tweet)\n",
    "\n",
    "# Close connection to file\n",
    "tweets_file.close()\n",
    "\n",
    "# Print the keys of the first tweet dict\n",
    "print(tweets_data[0].keys())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "416bf943",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Twitter data to DataFrame\n",
    "Now you have the Twitter data in a list of dictionaries, tweets_data, where each dictionary corresponds to a single tweet. Next, you're going to extract the text and language of each tweet. The text in a tweet, t1, is stored as the value `t1['text']`; similarly, the language is stored in `t1['lang']`. Your task is to build a DataFrame in which each row is a tweet and the columns are 'text' and 'lang'.\n",
    "\n",
    "* Use `pd.DataFrame()` to construct a DataFrame of tweet texts and languages; to do so, the first argument should be tweets_data, a list of dictionaries. The second argument to `pd.DataFrame()` is a list of the keys you wish to have as columns. Assign the result of the `pd.DataFrame()` call to df.\n",
    "* Print the head of the DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "12154423",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                text lang\n",
      "0  RT @bpolitics: .@krollbondrating's Christopher...   en\n",
      "1  RT @HeidiAlpine: @dmartosko Cruz video found.....   en\n",
      "2  Njihuni me Zonjën Trump !!! | Ekskluzive https...   et\n",
      "3  Your an idiot she shouldn't have tried to grab...   en\n",
      "4  RT @AlanLohner: The anti-American D.C. elites ...   en\n"
     ]
    }
   ],
   "source": [
    "# Import package\n",
    "import pandas as pd\n",
    "\n",
    "# Build DataFrame of tweet texts and languages\n",
    "df = pd.DataFrame(tweets_data, columns=['text', 'lang'])\n",
    "\n",
    "# Print head of DataFrame\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e4cfaa1",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## A little bit of Twitter text analysis\n",
    "Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis to count how many tweets contain the words 'clinton', 'trump', 'sanders' and 'cruz'. In the pre-exercise code, we have defined the following function `word_in_text()`, which will tell you whether the first argument (a word) occurs within the 2nd argument (a tweet).\n",
    "```python\n",
    "import re\n",
    "\n",
    "def word_in_text(word, text):\n",
    "    word = word.lower()\n",
    "    text = text.lower()\n",
    "    match = re.search(word, text)\n",
    "\n",
    "    if match:\n",
    "        return True\n",
    "    return False\n",
    "```\n",
    "You're going to iterate over the rows of the DataFrame and calculate how many tweets contain each of our keywords! The list of objects for each candidate has been initialized to 0.\n",
    "\n",
    "* Within the for loop for index, row in `df.iterrows()`:, the code currently increases the value of clinton by 1 each time a tweet (text row) mentioning 'Clinton' is encountered; complete the code so that the same happens for trump, sanders and cruz."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e0303674",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "def word_in_text(word, text):\n",
    "    word = word.lower()\n",
    "    text = text.lower()\n",
    "    match = re.search(word, text)\n",
    "\n",
    "    if match:\n",
    "        return True\n",
    "    return False\n",
    "\n",
    "# Initialize list to store tweet counts\n",
    "[clinton, trump, sanders, cruz] = [0, 0, 0, 0]\n",
    "\n",
    "# Iterate through df, counting the number of tweets in which\n",
    "# each candidate is mentioned\n",
    "for index, row in df.iterrows():\n",
    "    clinton += word_in_text('clinton', row['text'])\n",
    "    trump += word_in_text('trump', row['text'])\n",
    "    sanders += word_in_text('sanders', row['text'])\n",
    "    cruz += word_in_text('cruz', row['text'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ef841d0",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Plotting your Twitter data\n",
    "Now that you have the number of tweets that each candidate was mentioned in, you can plot a bar chart of this data. You'll use the statistical data visualization library seaborn, which you may not have seen before, but we'll guide you through. You'll first import seaborn as sns. You'll then construct a barplot of the data using sns.barplot, passing it two arguments:\n",
    "\n",
    "* a list of labels and\n",
    "* a list containing the variables you wish to plot (clinton, trump and so on.)\n",
    "\n",
    "Hopefully, you'll see that Trump was unreasonably represented! We have already run the previous exercise solutions in your environment.\n",
    "\n",
    "* Import both `matplotlib.pyplot` and `seaborn` using the aliases plt and sns, respectively.\n",
    "* Complete the arguments of `sns.barplot`:\n",
    "  + The first argument should be the list of labels to appear on the x-axis (created in the previous step).\n",
    "  + The second argument should be a list of the variables you wish to plot, as produced in the previous exercise (i.e. a list containing clinton, trump, etc)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "04b6ece3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import packages\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "# Set seaborn style\n",
    "sns.set(color_codes=True)\n",
    "\n",
    "# Create a list of labels:cd\n",
    "cd = ['clinton', 'trump', 'sanders', 'cruz']\n",
    "\n",
    "# Plot the bar chart\n",
    "ax = sns.barplot(cd, [clinton, trump, sanders, cruz])\n",
    "ax.set(ylabel=\"count\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "88a6c50d",
   "metadata": {},
   "source": [
    "Awesome!"
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
