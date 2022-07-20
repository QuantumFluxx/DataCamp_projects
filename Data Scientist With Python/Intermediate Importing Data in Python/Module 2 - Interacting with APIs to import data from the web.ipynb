{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e5dcf980",
   "metadata": {},
   "source": [
    "# Interacting with APIs to import data from the web\n",
    "\n",
    "## Pop quiz: What exactly is a JSON?\n",
    "Which of the following is NOT true of the JSON file format?\n",
    "\n",
    "\n",
    "* JSONs consist of key-value pairs.\n",
    "\n",
    "* JSONs are human-readable.\n",
    "\n",
    "* The JSON file format arose out of a growing need for real-time server-to-browser communication.\n",
    "\n",
    "* **The function json.load() will load the JSON into Python as a list.**\n",
    "\n",
    "* The function json.load() will load the JSON into Python as a dictionary.\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Loading and exploring a JSON\n",
    "Now that you know what a JSON is, you'll load one into your Python environment and explore it yourself. Here, you'll load the JSON `'a_movie.json'` into the variable json_data, which will be a dictionary. You'll then explore the JSON contents by printing the key-value pairs of json_data to the shell.\n",
    "\n",
    "* Load the JSON 'a_movie.json' into the variable `json_data` within the context provided by the with statement. To do so, use the function `json.load()` within the context manager.\n",
    "* Use a for loop to print all key-value pairs in the dictionary `json_data`. Recall that you can access a value in a dictionary using the syntax: `dictionary[key]`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9f7ee714",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title:  The Social Network\n",
      "Year:  2010\n",
      "Rated:  PG-13\n",
      "Released:  01 Oct 2010\n",
      "Runtime:  120 min\n",
      "Genre:  Biography, Drama\n",
      "Director:  David Fincher\n",
      "Writer:  Aaron Sorkin (screenplay), Ben Mezrich (book)\n",
      "Actors:  Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons\n",
      "Plot:  As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, he is sued by the twins who claimed he stole their idea, and by the co-founder who was later squeezed out of the business.\n",
      "Language:  English, French\n",
      "Country:  USA\n",
      "Awards:  Won 3 Oscars. Another 168 wins & 186 nominations.\n",
      "Poster:  https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg\n",
      "Ratings:  [{'Source': 'Internet Movie Database', 'Value': '7.7/10'}, {'Source': 'Rotten Tomatoes', 'Value': '96%'}, {'Source': 'Metacritic', 'Value': '95/100'}]\n",
      "Metascore:  95\n",
      "imdbRating:  7.7\n",
      "imdbVotes:  630,681\n",
      "imdbID:  tt1285016\n",
      "Type:  movie\n",
      "DVD:  05 Jun 2012\n",
      "BoxOffice:  $96,962,694\n",
      "Production:  Scott Rudin Productions, Michael De Luca, Trigger Street Productions\n",
      "Website:  N/A\n",
      "Response:  True\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "# Load JSON: json_data\n",
    "with open(\"datasets/a_movie.json\") as json_file:\n",
    "    json_data = json.load(json_file)\n",
    "\n",
    "# Print each key-value pair in json_data\n",
    "for k in json_data.keys():\n",
    "    print(k + ': ', json_data[k])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8e1e9d4",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Pop quiz: Exploring your JSON\n",
    "Load the JSON 'a_movie.json' into a variable, which will be a dictionary. Do so by copying, pasting and executing the following code in the IPython Shell:\n",
    "```python\n",
    "import json\n",
    "with open(\"a_movie.json\") as json_file:\n",
    "    json_data = json.load(json_file)\n",
    "```\n",
    "Print the values corresponding to the keys 'Title' and 'Year' and answer the following question about the movie that the JSON describes:\n",
    "\n",
    "Which of the following statements is true of the movie in question?\n",
    "\n",
    "* The title is 'Kung Fu Panda' and the year is 2010.\n",
    "\n",
    "* The title is 'Kung Fu Panda' and the year is 2008.\n",
    "\n",
    "* **The title is 'The Social Network' and the year is 2010.**\n",
    "\n",
    "* The title is 'The Social Network' and the year is 2008.\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Pop quiz: What's an API?\n",
    "Which of the following statements about APIs is NOT true?\n",
    "\n",
    "* An API is a set of protocols and routines for building and interacting with software applications.\n",
    "\n",
    "* API is an acronym and is short for Application Program interface.\n",
    "\n",
    "* It is common to pull data from APIs in the JSON file format.\n",
    "\n",
    "* **All APIs transmit data only in the JSON file format.**\n",
    "\n",
    "* An API is a bunch of code that allows two software programs to communicate with each other.\n",
    "\n",
    "Correct!\n",
    "\n",
    "## API requests\n",
    "Now it's your turn to pull some movie data down from the Open Movie Database (OMDB) using their API. The movie you'll query the API about is The Social Network. Recall that, in the video, to query the API about the movie Hackers, Hugo's query string was `'http://www.omdbapi.com/?t=hackers'` and had a single argument t=hackers.\n",
    "\n",
    "Note: recently, OMDB has changed their API: you now also have to specify an API key. This means you'll have to add another argument to the URL: apikey=72bc447a.\n",
    "\n",
    "* Import the `requests` package.\n",
    "* Assign to the variable url the URL of interest in order to query `'http://www.omdbapi.com'` for the data corresponding to the movie The Social Network. The query string should have two arguments: apikey=72bc447a and t=the+social+network. You can combine them as follows: `apikey=72bc447a&t=the+social+network`.\n",
    "* Print the text of the response object r by using its text attribute and passing the result to the `print()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1e2285af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\"Title\":\"The Social Network\",\"Year\":\"2010\",\"Rated\":\"PG-13\",\"Released\":\"01 Oct 2010\",\"Runtime\":\"120 min\",\"Genre\":\"Biography, Drama\",\"Director\":\"David Fincher\",\"Writer\":\"Aaron Sorkin, Ben Mezrich\",\"Actors\":\"Jesse Eisenberg, Andrew Garfield, Justin Timberlake\",\"Plot\":\"As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, he is sued by the twins who claimed he stole their idea, and by the co-founder who was later squeezed out of the business.\",\"Language\":\"English, French\",\"Country\":\"United States\",\"Awards\":\"Won 3 Oscars. 172 wins & 186 nominations total\",\"Poster\":\"https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg\",\"Ratings\":[{\"Source\":\"Internet Movie Database\",\"Value\":\"7.8/10\"},{\"Source\":\"Rotten Tomatoes\",\"Value\":\"96%\"},{\"Source\":\"Metacritic\",\"Value\":\"95/100\"}],\"Metascore\":\"95\",\"imdbRating\":\"7.8\",\"imdbVotes\":\"687,228\",\"imdbID\":\"tt1285016\",\"Type\":\"movie\",\"DVD\":\"11 Jan 2011\",\"BoxOffice\":\"$96,962,694\",\"Production\":\"N/A\",\"Website\":\"N/A\",\"Response\":\"True\"}\n"
     ]
    }
   ],
   "source": [
    "# Import requests package\n",
    "import requests\n",
    "\n",
    "# Assign URL to variable: url\n",
    "url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'\n",
    "\n",
    "# Package the request, send the request and catch the response: r\n",
    "r = requests.get(url)\n",
    "\n",
    "# Print the text of the response\n",
    "print(r.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06df0996",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## JSON–from the web to Python\n",
    "Wow, congrats! You've just queried your first API programmatically in Python and printed the text of the response to the shell. However, as you know, your response is actually a JSON, so you can do one step better and decode the JSON. You can then print the key-value pairs of the resulting dictionary. That's what you're going to do now!\n",
    "\n",
    "* Pass the variable url to the `requests.get()` function in order to send the relevant request and catch the response, assigning the resultant response message to the variable `r`.\n",
    "* Apply the `json()` method to the response object r and store the resulting dictionary in the variable json_data.\n",
    "* Hit submit to print the key-value pairs of the dictionary json_data to the shell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c2080c75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title:  The Social Network\n",
      "Year:  2010\n",
      "Rated:  PG-13\n",
      "Released:  01 Oct 2010\n",
      "Runtime:  120 min\n",
      "Genre:  Biography, Drama\n",
      "Director:  David Fincher\n",
      "Writer:  Aaron Sorkin, Ben Mezrich\n",
      "Actors:  Jesse Eisenberg, Andrew Garfield, Justin Timberlake\n",
      "Plot:  As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, he is sued by the twins who claimed he stole their idea, and by the co-founder who was later squeezed out of the business.\n",
      "Language:  English, French\n",
      "Country:  United States\n",
      "Awards:  Won 3 Oscars. 172 wins & 186 nominations total\n",
      "Poster:  https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg\n",
      "Ratings:  [{'Source': 'Internet Movie Database', 'Value': '7.8/10'}, {'Source': 'Rotten Tomatoes', 'Value': '96%'}, {'Source': 'Metacritic', 'Value': '95/100'}]\n",
      "Metascore:  95\n",
      "imdbRating:  7.8\n",
      "imdbVotes:  687,228\n",
      "imdbID:  tt1285016\n",
      "Type:  movie\n",
      "DVD:  11 Jan 2011\n",
      "BoxOffice:  $96,962,694\n",
      "Production:  N/A\n",
      "Website:  N/A\n",
      "Response:  True\n"
     ]
    }
   ],
   "source": [
    "# Assign URL to variable: url\n",
    "url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'\n",
    "\n",
    "# Package the request, send the request and catch the response: r\n",
    "r = requests.get(url)\n",
    "\n",
    "# Decode the JSON data into a dictionary: json_data\n",
    "json_data = r.json()\n",
    "\n",
    "# Print each key-value pair in json_data\n",
    "for k in json_data.keys():\n",
    "    print(k + ': ', json_data[k])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d16865aa",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Checking out the Wikipedia API\n",
    "You're doing so well and having so much fun that we're going to throw one more API at you: the Wikipedia API (documented here). You'll figure out how to find and extract information from the Wikipedia page for Pizza. What gets a bit wild here is that your query will return nested JSONs, that is, JSONs with JSONs, but Python can handle that because it will translate them into dictionaries within dictionaries.\n",
    "\n",
    "The URL that requests the relevant query from the Wikipedia API is\n",
    "```\n",
    "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza\n",
    "```\n",
    "\n",
    "* Assign the relevant URL to the variable url.\n",
    "* Apply the `json()` method to the response object r and store the resulting dictionary in the variable `json_data`.\n",
    "* The variable `pizza_extract` holds the HTML of an extract from Wikipedia's Pizza page as a string; use the function `print()` to print this string to the shell.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c5107393",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<link rel=\"mw-deduplicated-inline-style\" href=\"mw-data:TemplateStyles:r1033289096\">\n",
      "<p class=\"mw-empty-elt\">\n",
      "</p>\n",
      "<p><b>Pizza</b> (<small>Italian: </small><span title=\"Representation in the International Phonetic Alphabet (IPA)\" lang=\"it-Latn-fonipa\">[ˈpittsa]</span>, <small>Neapolitan: </small><span title=\"Representation in the International Phonetic Alphabet (IPA)\" lang=\"nap-Latn-fonipa\">[ˈpittsə]</span>) is a dish of  Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients (such as various types of sausage, anchovies, mushrooms, onions, olives, vegetables, meat, ham, etc.), which is then baked at a high temperature, traditionally in a wood-fired oven. A small pizza is sometimes called a pizzetta. A person who makes pizza is known as a <b>pizzaiolo</b>.\n",
      "</p><p>In Italy, pizza served in a restaurant is presented unsliced, and is eaten with the use of a knife and fork. In casual settings, however, it is cut into wedges to be eaten while held in the hand.\n",
      "</p><p>The term <i>pizza</i> was first recorded in the 10th century in a Latin manuscript from the Southern Italian town of Gaeta in Lazio, on the border with Campania. Modern pizza was invented in Naples, and the dish and its variants have since become popular in many countries. It has become one of the most popular foods in the world and a common fast food item in Europe, North America and Australasia; available at pizzerias (restaurants specializing in pizza),  restaurants offering Mediterranean cuisine, via pizza delivery, and as street food. Various food companies sell ready-baked pizzas, which may be frozen, in grocery stores, to be reheated in a home oven.\n",
      "</p><p>In 2017, the world pizza market was US$128 billion, and in the US it was $44 billion spread over 76,000 pizzerias.  Overall, 13% of the U.S. population aged 2 years and over consumed pizza on any given day.</p><p>The <i>Associazione Verace Pizza Napoletana</i> (lit. True Neapolitan Pizza Association) is a non-profit organization founded in 1984 with headquarters in Naples that aims to promote traditional Neapolitan pizza. In 2009, upon Italy's request, Neapolitan pizza was registered with the European Union as a Traditional Speciality Guaranteed dish, and in 2017 the art of its making was included on UNESCO's list of intangible cultural heritage.</p><p>Raffaele Esposito is often considered to be the father of modern pizza.</p>\n"
     ]
    }
   ],
   "source": [
    "# Assign URL to variable: url\n",
    "url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'\n",
    "\n",
    "# Package the request, send the request and catch the response: r\n",
    "r = requests.get(url)\n",
    "\n",
    "# Decode the JSON data into a dictionary: json_data\n",
    "json_data = r.json()\n",
    "\n",
    "# Print the Wikipedia page extract\n",
    "pizza_extract = json_data['query']['pages']['24768']['extract']\n",
    "print(pizza_extract)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2c8cb17",
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
