{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "040d7e18",
   "metadata": {},
   "source": [
    "# Context Managers\n",
    "\n",
    "## The number of cats\n",
    "You are working on a natural language processing project to determine what makes great writers so great. Your current hypothesis is that great writers talk about cats a lot. To prove it, you want to count the number of times the word \"cat\" appears in \"Alice's Adventures in Wonderland\" by Lewis Carroll. You have already downloaded a text file, alice.txt, with the entire contents of this great book.\n",
    "\n",
    "* Use the `open()` context manager to open alice.txt and assign the file to the file variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "173f3ac3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Open \"alice.txt\" and assign the file to \"file\"\n",
    "with open('alice.txt') as file:\n",
    "    text = file.read()\n",
    "\n",
    "n = 0\n",
    "for word in text.split():\n",
    "    if word.lower() in ['cat', 'cats']:\n",
    "        n += 1\n",
    "\n",
    "print('Lewis Carroll uses the word \"cat\" {} times'.format(n))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f68dbf86",
   "metadata": {},
   "source": [
    "Cool cat counting! By opening the file using the with open() statement, you were able to read in the text of the file. More importantly, when you were done reading the text, the context manager closed the file for you.\n",
    "\n",
    "## The speed of cats\n",
    "You're working on a new web service that processes Instagram feeds to identify which pictures contain cats (don't ask why -- it's the internet). The code that processes the data is slower than you would like it to be, so you are working on tuning it up to run faster. Given an image, image, you have two functions that can process it:\n",
    "\n",
    "* process_with_numpy(image)\n",
    "* process_with_pytorch(image)\n",
    "\n",
    "Your colleague wrote a context manager, `timer()`, that will print out how long the code inside the context block takes to run. She is suggesting you use it to see which of the two options is faster. Time each function to determine which one to use in your web service.\n",
    "\n",
    "* Use the `timer()` context manager to time how long process_with_numpy(image) takes to run.\n",
    "* Use the `timer()` context manager to time how long process_with_pytorch(image) takes to run."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5244563",
   "metadata": {},
   "outputs": [],
   "source": [
    "image = get_image_from_instagram()\n",
    "\n",
    "# Time how long process_with_numpy(image) takes to run\n",
    "with timer():\n",
    "    print('Numpy version')\n",
    "    process_with_numpy(image)\n",
    "\n",
    "# Time how long process_with_pytorch(image) takes to run\n",
    "with timer():\n",
    "    print('Pytorch version')\n",
    "    process_with_pytorch(image)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a2b9570",
   "metadata": {},
   "source": [
    "Terrific timing! Now that you know the pytorch version is faster, you can use it in your web service to ensure your users get the rapid response time they expect.\n",
    "\n",
    "You may have noticed there was no as <variable name> at the end of the with statement in timer() context manager. That is because timer() is a context manager that does not return a value, so the as <variable name> at the end of the with statement isn't necessary. In the next lesson, you'll learn how to write your own context managers like timer().\n",
    "    \n",
    "## The timer() context manager\n",
    "A colleague of yours is working on a web service that processes Instagram photos. Customers are complaining that the service takes too long to identify whether or not an image has a cat in it, so your colleague has come to you for help. You decide to write a context manager that they can use to time how long their functions take to run.\n",
    "\n",
    "* Add a decorator from the contextlib module to the `timer()` function that will make it act like a context manager.\n",
    "* Send control from the `timer()` function to the context block."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2779192e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import contextlib\n",
    "\n",
    "# Add a decorator that will make timer() a context manager\n",
    "@contextlib.contextmanager\n",
    "def timer():\n",
    "    \"\"\"Time the execution of a context block.\n",
    "\n",
    "    Yields:\n",
    "        None\n",
    "    \"\"\"\n",
    "    start = time.time()\n",
    "    # Send control back to the context block\n",
    "    yield\n",
    "    end = time.time()\n",
    "    print('Elapsed: {:.2f}s'.format(end - start))\n",
    "\n",
    "with timer():\n",
    "    print('This should take approximately 0.25 seconds')\n",
    "    time.sleep(0.25)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "603735ed",
   "metadata": {},
   "source": [
    "You're managing context like a boss! And your colleague can now use your timer() context manager to figure out which of their functions is running too slow. Notice that the three elements of a context manager are all here: a function definition, a yield statement, and the @contextlib.contextmanager decorator. It's also worth noticing that timer() is a context manager that does not return an explicit value, so yield is written by itself without specifying anything to return.\n",
    "\n",
    "## A read-only open() context manager\n",
    "You have a bunch of data files for your next deep learning project that took you months to collect and clean. It would be terrible if you accidentally overwrote one of those files when trying to read it in for training, so you decide to create a read-only version of the open() context manager to use in your project.\n",
    "\n",
    "The regular `open()` context manager:\n",
    "\n",
    "* takes a filename and a mode ('r' for read, 'w' for write, or 'a' for append)\n",
    "* opens the file for reading, writing, or appending\n",
    "* yields control back to the context, along with a reference to the file\n",
    "* waits for the context to finish\n",
    "* and then closes the file before exiting\n",
    "\n",
    "Your context manager will do the same thing, except it will only take the filename as an argument and it will only open the file for reading.\n",
    "\n",
    "* Yield control from `open_read_only()` to the context block, ensuring that the `read_only_file` object gets assigned to my_file.\n",
    "* Use `read_only_file's` `.close()` method to ensure that you don't leave open files lying around."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fdac3dbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "@contextlib.contextmanager\n",
    "def open_read_only(filename):\n",
    "    \"\"\"Open a file in read-only mode.\n",
    " \n",
    "    Args:\n",
    "        filename (str): The location of the file to read\n",
    "\n",
    "    Yields:\n",
    "        file object\n",
    "    \"\"\"\n",
    "    read_only_file = open(filename, mode='r')\n",
    "    # Yield read_only_file so it can be assigned to my_file\n",
    "    yield read_only_file\n",
    "    # Close read_only_file\n",
    "    read_only_file.close()\n",
    "\n",
    "with open_read_only('my_file.txt') as my_file:\n",
    "    print(my_file.read())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2874428",
   "metadata": {},
   "source": [
    "That is a radical read-only context manager! Now you can relax, knowing that every time you use with open_read_only() your files are safe from being accidentally overwritten. This function is an example of a context manager that does return a value, so we write yield read_only_file instead of just yield. Then the read_only_file object gets assigned to my_file in the with statement so that whoever is using your context can call its .read() method in the context block.\n",
    "\n",
    "## Context manager use cases\n",
    "Which of the following would NOT be a good opportunity to use a context manager?\n",
    "\n",
    "\n",
    "* A function that starts a timer that keeps track of how long some block of code takes to run.\n",
    "\n",
    "* **A function that prints all of the prime numbers between 2 and some value n.**\n",
    "\n",
    "* A function that connects to a smart thermostat so that it can be programmed remotely.\n",
    "\n",
    "* A function that prevents multiple users from updating an online spreadsheet at the same time by locking access to the spreadsheet before every operation.\n",
    "\n",
    "Correct! While you might be able to do this with a context manager, it would make much more sense just to do it with a normal function.\n",
    "\n",
    "## Scraping the NASDAQ\n",
    "Training deep neural nets is expensive! You might as well invest in NVIDIA stock since you're spending so much on GPUs. To pick the best time to invest, you are going to collect and analyze some data on how their stock is doing. The context manager stock('NVDA') will connect to the NASDAQ and return an object that you can use to get the latest price by calling its .price() method.\n",
    "\n",
    "You want to connect to stock('NVDA') and record 10 timesteps of price data by writing it to the file NVDA.txt.\n",
    "\n",
    "You will notice the use of an underscore when iterating over the for loop. If this is confusing to you, don't worry. It could easily be replaced with i, if we planned to do something with it, like use it as an index. Since we won't be using it, we can use a dummy operator, _, which doesn't use any additional memory.\n",
    "\n",
    "* Use the stock('NVDA') context manager and assign the result to nvda.\n",
    "* Open a file for writing with open('NVDA.txt', 'w') and assign the file object to `f_out` so you can record the price over time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70f80047",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the \"stock('NVDA')\" context manager\n",
    "# and assign the result to the variable \"nvda\"\n",
    "with stock('NVDA') as nvda:\n",
    "    # Open 'NVDA.txt' for writing as f_out\n",
    "    with open('NVDA.txt', 'w') as f_out:\n",
    "    for _ in range(10):\n",
    "        value = nvda.price()\n",
    "        print('Logging ${:.2f} for NVDA'.format(value))\n",
    "        f_out.write('{:.2f}\\n'.format(value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03304038",
   "metadata": {},
   "source": [
    "Super stock scraping! Now you can monitor the NVIDIA stock price and decide when is the exact right time to buy. Nesting context managers like this allows you to connect to the stock market (the CONNECT/DISCONNECT pattern) and write to a file (the OPEN/CLOSE pattern) at the same time.\n",
    "\n",
    "## Changing the working directory\n",
    "You are using an open-source library that lets you train deep neural networks on your data. Unfortunately, during training, this library writes out checkpoint models (i.e., models that have been trained on a portion of the data) to the current working directory. You find that behavior frustrating because you don't want to have to launch the script from the directory where the models will be saved.\n",
    "\n",
    "You decide that one way to fix this is to write a context manager that changes the current working directory, lets you build your models, and then resets the working directory to its original location. You'll want to be sure that any errors that occur during model training don't prevent you from resetting the working directory to its original location.\n",
    "\n",
    "* Add a statement that lets you handle any errors that might occur inside the context.\n",
    "* Add a statement that ensures `os.chdir(current_dir)` will be called, whether there was an error or not."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6de85b51",
   "metadata": {},
   "outputs": [],
   "source": [
    "def in_dir(directory):\n",
    "    \"\"\"Change current working directory to `directory`,\n",
    "    allow the user to run some code, and change back.\n",
    "\n",
    "    Args:\n",
    "        directory (str): The path to a directory to work in.\n",
    "    \"\"\"\n",
    "    current_dir = os.getcwd()\n",
    "    os.chdir(directory)\n",
    "\n",
    "    # Add code that lets you handle errors\n",
    "    try:\n",
    "        yield\n",
    "    # Ensure the directory is reset,\n",
    "    # whether there was an error or not\n",
    "    finally:\n",
    "        os.chdir(current_dir)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3fe719b3",
   "metadata": {},
   "source": [
    "Excellent error handling! Now, even if someone writes buggy code when using your context manager, you will be sure to change the current working directory back to what it was when they called in_dir(). This is important to do because your users might be relying on their working directory being what it was when they started the script. in_dir() is a great example of the CHANGE/RESET pattern that indicates you should use a context manager."
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
