{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "58543ae3",
   "metadata": {},
   "source": [
    "# More on Decorators\n",
    "\n",
    "## Print the return type\n",
    "You are debugging a package that you've been working on with your friends. Something weird is happening with the data being returned from one of your functions, but you're not even sure which function is causing the trouble. You know that sometimes bugs can sneak into your code when you are expecting a function to return one thing, and it returns something different. For instance, if you expect a function to return a numpy array, but it returns a list, you can get unexpected behavior. To ensure this is not what is causing the trouble, you decide to write a decorator, `print_return_type()`, that will print out the type of the variable that gets returned from every call of any function it is decorating.\n",
    "\n",
    "* Create a nested function, `wrapper()`, that will become the new decorated function.\n",
    "* Call the function being decorated.\n",
    "* Return the new decorated function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c33c6779",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "foo() returned type <class 'int'>\n",
      "42\n",
      "foo() returned type <class 'list'>\n",
      "[1, 2, 3]\n",
      "foo() returned type <class 'dict'>\n",
      "{'a': 42}\n"
     ]
    }
   ],
   "source": [
    "def print_return_type(func):\n",
    "    # Define wrapper(), the decorated function\n",
    "    def wrapper(*args, **kwargs):\n",
    "        # Call the function being decorated\n",
    "        result = func(*args, **kwargs)\n",
    "        print('{}() returned type {}'.format(\n",
    "            func.__name__, type(result)\n",
    "        ))\n",
    "        return result\n",
    "    # Return the decorated function\n",
    "    return wrapper\n",
    "   \n",
    "@print_return_type\n",
    "def foo(value):\n",
    "    return value\n",
    "  \n",
    "print(foo(42))\n",
    "print(foo([1, 2, 3]))\n",
    "print(foo({'a': 42}))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a8bd19c3",
   "metadata": {},
   "source": [
    "Righteous return types! Your new decorator helps you examine the results of your functions at runtime. Now you can apply this decorator to every function in the package you are developing and run your scripts. Being able to examine the types of your return values will help you understand what is happening and will hopefully help you find the bug.\n",
    "\n",
    "## Counter\n",
    "You're working on a new web app, and you are curious about how many times each of the functions in it gets called. So you decide to write a decorator that adds a counter to each function that you decorate. You could use this information in the future to determine whether there are sections of code that you could remove because they are no longer being used by the app.\n",
    "\n",
    "* Call the function being decorated and return the result.\n",
    "* Return the new decorated function.\n",
    "* Decorate `foo()` with the `counter()` decorator."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "74dba381",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "calling foo()\n",
      "calling foo()\n",
      "foo() was called 2 times.\n"
     ]
    }
   ],
   "source": [
    "def counter(func):\n",
    "    def wrapper(*args, **kwargs):\n",
    "        wrapper.count += 1\n",
    "        # Call the function being decorated and return the result\n",
    "        return func(*args, **kwargs)\n",
    "    wrapper.count = 0\n",
    "    # Return the new decorated function\n",
    "    return wrapper\n",
    "\n",
    "# Decorate foo() with the counter() decorator\n",
    "@counter\n",
    "def foo():\n",
    "    print('calling foo()')\n",
    "  \n",
    "foo()\n",
    "foo()\n",
    "\n",
    "print('foo() was called {} times.'.format(foo.count))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df74e51e",
   "metadata": {},
   "source": [
    "Cool counting! Now you can go decorate a bunch of functions with the counter() decorator, let your program run for a while, and then print out how many times each function was called.\n",
    "\n",
    "It seems a little magical that you can reference the wrapper() function from inside the definition of wrapper() as we do here on line 3. That's just one of the many neat things about functions in Python -- any function, not just decorators.\n",
    "\n",
    "## Preserving docstrings when decorating functions\n",
    "Your friend has come to you with a problem. They've written some nifty decorators and added them to the functions in the open-source library they've been working on. However, they were running some tests and discovered that all of the docstrings have mysteriously disappeared from their decorated functions. Show your friend how to preserve docstrings and other metadata when writing decorators.\n",
    "\n",
    "* Decorate `print_sum()` with the `add_hello()` decorator to replicate the issue that your friend saw - that the docstring disappears."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "81fb088a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "30\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def add_hello(func):\n",
    "    def wrapper(*args, **kwargs):\n",
    "        print('Hello')\n",
    "        return func(*args, **kwargs)\n",
    "    return wrapper\n",
    "\n",
    "# Decorate print_sum() with the add_hello() decorator\n",
    "@add_hello\n",
    "def print_sum(a, b):\n",
    "    \"\"\"Adds two numbers and prints the sum\"\"\"\n",
    "    print(a + b)\n",
    "  \n",
    "print_sum(10, 20)\n",
    "print_sum_docstring = print_sum.__doc__\n",
    "print(print_sum_docstring)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dae2a2dc",
   "metadata": {},
   "source": [
    "* To show your friend that they are printing the `wrapper()` function's docstring, not the `print_sum()` docstring, add the following docstring to `wrapper()`:\n",
    "```python\n",
    "\"\"\"Print 'hello' and then call the decorated function.\"\"\"\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "77f173ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "30\n",
      "Print 'hello' and then call the decorated function.\n"
     ]
    }
   ],
   "source": [
    "def add_hello(func):\n",
    "    # Add a docstring to wrapper\n",
    "    def wrapper(*args, **kwargs):\n",
    "        \"\"\"Print 'hello' and then call the decorated function.\"\"\"\n",
    "        print('Hello')\n",
    "        return func(*args, **kwargs)\n",
    "    return wrapper\n",
    "\n",
    "@add_hello\n",
    "def print_sum(a, b):\n",
    "    \"\"\"Adds two numbers and prints the sum\"\"\"\n",
    "    print(a + b)\n",
    "  \n",
    "print_sum(10, 20)\n",
    "print_sum_docstring = print_sum.__doc__\n",
    "print(print_sum_docstring)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "777c3636",
   "metadata": {},
   "source": [
    "* Import a function that will allow you to add the metadata from `print_sum()` to the decorated version of `print_sum()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e11b2038",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "30\n",
      "Print 'hello' and then call the decorated function.\n"
     ]
    }
   ],
   "source": [
    "# Import the function you need to fix the problem\n",
    "from functools import wraps\n",
    "\n",
    "def add_hello(func):\n",
    "    def wrapper(*args, **kwargs):\n",
    "        \"\"\"Print 'hello' and then call the decorated function.\"\"\"\n",
    "        print('Hello')\n",
    "        return func(*args, **kwargs)\n",
    "    return wrapper\n",
    "  \n",
    "@add_hello\n",
    "def print_sum(a, b):\n",
    "    \"\"\"Adds two numbers and prints the sum\"\"\"\n",
    "    print(a + b)\n",
    "  \n",
    "print_sum(10, 20)\n",
    "print_sum_docstring = print_sum.__doc__\n",
    "print(print_sum_docstring)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2870b0e",
   "metadata": {},
   "source": [
    "* Finally, decorate `wrapper()` so that the metadata from `func()` is preserved in the new decorated function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7914ccce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "30\n",
      "Adds two numbers and prints the sum\n"
     ]
    }
   ],
   "source": [
    "# Import the function you need to fix the problem\n",
    "from functools import wraps\n",
    "\n",
    "def add_hello(func):\n",
    "    # Decorate wrapper() so that it keeps func()'s metadata\n",
    "    @wraps(func)\n",
    "    def wrapper(*args, **kwargs):\n",
    "        \"\"\"Print 'hello' and then call the decorated function.\"\"\"\n",
    "        print('Hello')\n",
    "        return func(*args, **kwargs)\n",
    "    return wrapper\n",
    "  \n",
    "@add_hello\n",
    "def print_sum(a, b):\n",
    "    \"\"\"Adds two numbers and prints the sum\"\"\"\n",
    "    print(a + b)\n",
    "  \n",
    "print_sum(10, 20)\n",
    "print_sum_docstring = print_sum.__doc__\n",
    "print(print_sum_docstring)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3429e592",
   "metadata": {},
   "source": [
    "That's a wrap! Your friend was concerned that they couldn't print the docstrings of their functions. They now realize that the strange behavior they were seeing was caused by the fact that they were accidentally printing the wrapper() docstring instead of the docstring of the original function. After adding @wraps(func) to all of their decorators, they see that the docstrings are back where they expect them to be.\n",
    "\n",
    "## Measuring decorator overhead\n",
    "Your boss wrote a decorator called check_everything() that they think is amazing, and they are insisting you use it on your function. However, you've noticed that when you use it to decorate your functions, it makes them run much slower. You need to convince your boss that the decorator is adding too much processing time to your function. To do this, you are going to measure how long the decorated function takes to run and compare it to how long the undecorated function would have taken to run. This is the decorator in question:\n",
    "```python\n",
    "def check_everything(func):\n",
    "    @wraps(func)\n",
    "    def wrapper(*args, **kwargs):\n",
    "        check_inputs(*args, **kwargs)\n",
    "        result = func(*args, **kwargs)\n",
    "        check_outputs(result)\n",
    "        return result\n",
    "    return wrapper\n",
    "```\n",
    "\n",
    "* Call the original function instead of the decorated version by using an attribute of the function that the `wraps()` statement in your boss's decorator added to the decorated function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b337e3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "@check_everything\n",
    "def duplicate(my_list):\n",
    "    \"\"\"Return a new list that repeats the input twice\"\"\"\n",
    "    return my_list + my_list\n",
    "\n",
    "t_start = time.time()\n",
    "duplicated_list = duplicate(list(range(50)))\n",
    "t_end = time.time()\n",
    "decorated_time = t_end - t_start\n",
    "\n",
    "t_start = time.time()\n",
    "# Call the original function instead of the decorated one\n",
    "duplicated_list = duplicate.__wrapped__(list(range(50)))\n",
    "t_end = time.time()\n",
    "undecorated_time = t_end - t_start\n",
    "\n",
    "print('Decorated time: {:.5f}s'.format(decorated_time))\n",
    "print('Undecorated time: {:.5f}s'.format(undecorated_time))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb259748",
   "metadata": {},
   "source": [
    "Wow! Your function ran approximately 10,000 times faster without your boss's decorator. At least they were smart enough to add @wraps(func) to the nested wrapper() function so that you were able to access the original function. You should show them the results of this test. Be sure to ask for a raise while you're at it!\n",
    "\n",
    "## Run_n_times()\n",
    "In the video exercise, I showed you an example of a decorator that takes an argument: `run_n_times()`. The code for that decorator is repeated below to remind you how it works. Practice different ways of applying the decorator to the function `print_sum()`. Then I'll show you a funny prank you can play on your co-workers.\n",
    "```python\n",
    "def run_n_times(n):\n",
    "    \"\"\"Define and return a decorator\"\"\"\n",
    "    def decorator(func):\n",
    "        def wrapper(*args, **kwargs):\n",
    "            for i in range(n):\n",
    "                func(*args, **kwargs)\n",
    "        return wrapper\n",
    "    return decorator\n",
    "```\n",
    "* Add the `run_n_times()` decorator to `print_sum()` using decorator syntax so that `print_sum()` runs 10 times."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "76085d86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "35\n",
      "35\n",
      "35\n",
      "35\n",
      "35\n",
      "35\n",
      "35\n",
      "35\n",
      "35\n",
      "35\n"
     ]
    }
   ],
   "source": [
    "def run_n_times(n):\n",
    "    \"\"\"Define and return a decorator\"\"\"\n",
    "    def decorator(func):\n",
    "        def wrapper(*args, **kwargs):\n",
    "            for i in range(n):\n",
    "                func(*args, **kwargs)\n",
    "        return wrapper\n",
    "    return decorator\n",
    "\n",
    "# Make print_sum() run 10 times with the run_n_times() decorator\n",
    "@run_n_times(10)\n",
    "def print_sum(a, b):\n",
    "    print(a + b)\n",
    "  \n",
    "print_sum(15, 20)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "381eee82",
   "metadata": {},
   "source": [
    "* Use `run_n_times()` to create a decorator `run_five_times()` that will run any function five times."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4f0d9f17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "104\n",
      "104\n",
      "104\n",
      "104\n",
      "104\n"
     ]
    }
   ],
   "source": [
    "# Use run_n_times() to create the run_five_times() decorator\n",
    "run_five_times = run_n_times(5)\n",
    "\n",
    "@run_five_times\n",
    "def print_sum(a, b):\n",
    "    print(a + b)\n",
    "  \n",
    "print_sum(4, 100)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "549e5def",
   "metadata": {},
   "source": [
    "* Here's the prank: use `run_n_times()` to modify the built-in `print()` function so that it always prints 20 times!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "71cdf37a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n",
      "What is happening?!?!\n"
     ]
    }
   ],
   "source": [
    "# Modify the print() function to always run 20 times\n",
    "print = run_n_times(20)(print)\n",
    "\n",
    "print('What is happening?!?!')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f553b4d8",
   "metadata": {},
   "source": [
    "You've become an expert at using decorators. Notice how when you use decorator syntax for a decorator that takes arguments, you need to call the decorator by adding parentheses, but you don't add parenthesis for decorators that don't take arguments.\n",
    "\n",
    "Warning: overwriting commonly used functions is probably not a great idea, so think twice before using these powers for evil.\n",
    "\n",
    "## HTML Generator\n",
    "You are writing a script that generates HTML for a webpage on the fly. So far, you have written two decorators that will add bold or italics tags to any function that returns a string. You notice, however, that these two decorators look very similar. Instead of writing a bunch of other similar looking decorators, you want to create one decorator, `html()`, that can take any pair of opening and closing tags.\n",
    "```python\n",
    "def bold(func):\n",
    "    @wraps(func)\n",
    "    def wrapper(*args, **kwargs):\n",
    "        msg = func(*args, **kwargs)\n",
    "        return '<b>{}</b>'.format(msg)\n",
    "    return wrapper\n",
    "\n",
    "def italics(func):\n",
    "    @wraps(func)\n",
    "    def wrapper(*args, **kwargs):\n",
    "        msg = func(*args, **kwargs)\n",
    "        return '<i>{}</i>'.format(msg)\n",
    "    return wrapper\n",
    "```\n",
    "\n",
    "* Return the decorator and the decorated function from the correct places in the new `html()` decorator."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3b9bd8b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def bold(func):\n",
    "    @wraps(func)\n",
    "    def wrapper(*args, **kwargs):\n",
    "        msg = func(*args, **kwargs)\n",
    "        return '<b>{}</b>'.format(msg)\n",
    "    return wrapper\n",
    "\n",
    "def italics(func):\n",
    "    @wraps(func)\n",
    "    def wrapper(*args, **kwargs):\n",
    "        msg = func(*args, **kwargs)\n",
    "        return '<i>{}</i>'.format(msg)\n",
    "    return wrapper\n",
    "\n",
    "def html(open_tag, close_tag):\n",
    "    def decorator(func):\n",
    "        @wraps(func)\n",
    "        def wrapper(*args, **kwargs):\n",
    "            msg = func(*args, **kwargs)\n",
    "            return '{}{}{}'.format(open_tag, msg, close_tag)\n",
    "            # Return the decorated function\n",
    "        return wrapper\n",
    "    # Return the decorator\n",
    "    return decorator"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85eff605",
   "metadata": {},
   "source": [
    "* Use the `html()` decorator to wrap the return value of `hello()` in the strings < b > and < /b > (the HTML tags that mean \"bold\")."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "060ba726",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n",
      "<b>Hello Alice!</b>\n"
     ]
    }
   ],
   "source": [
    "# Make hello() return bolded text\n",
    "@html('<b>', '</b>')\n",
    "def hello(name):\n",
    "    return 'Hello {}!'.format(name)\n",
    "\n",
    "print(hello('Alice'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01cacee1",
   "metadata": {},
   "source": [
    "* Use `html()` to wrap the return value of `goodbye()` in the strings < i > and < /i > (the HTML tags that mean \"italics\")."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "66fae9d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n",
      "<i>Goodbye Alice.</i>\n"
     ]
    }
   ],
   "source": [
    "# Make goodbye() return italicized text\n",
    "@html('<i>', '</i>')\n",
    "def goodbye(name):\n",
    "    return 'Goodbye {}.'.format(name)\n",
    "  \n",
    "print(goodbye('Alice'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a8d9bb27",
   "metadata": {},
   "source": [
    "* Use `html()` to wrap `hello_goodbye()` in a DIV, which is done by adding the strings < div > and < /div > tags around a string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "14e4b50d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n",
      "<div>\n",
      "<b>Hello Alice!</b>\n",
      "<i>Goodbye Alice.</i>\n",
      "</div>\n"
     ]
    }
   ],
   "source": [
    "# Wrap the result of hello_goodbye() in <div> and </div>\n",
    "@html('<div>', '</div>')\n",
    "def hello_goodbye(name):\n",
    "    return '\\n{}\\n{}\\n'.format(hello(name), goodbye(name))\n",
    "  \n",
    "print(hello_goodbye('Alice'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a099f74",
   "metadata": {},
   "source": [
    "That's some HTML hotness! With the new html() decorator you can focus on writing simple functions that return the information you want to display on the webpage and let the decorator take care of wrapping them in the appropriate HTML tags.\n",
    "\n",
    "## Tag your functions\n",
    "Tagging something means that you have given that thing one or more strings that act as labels. For instance, we often tag emails or photos so that we can search for them later. You've decided to write a decorator that will let you tag your functions with an arbitrary list of tags. You could use these tags for many things:\n",
    "\n",
    "* Adding information about who has worked on the function, so a user can look up who to ask if they run into trouble using it.\n",
    "* Labeling functions as \"experimental\" so that users know that the inputs and outputs might change in the future.\n",
    "* Marking any functions that you plan to remove in a future version of the code.\n",
    "* Etc.\n",
    "--------\n",
    "* Define a new decorator, named `decorator()`, to return.\n",
    "* Ensure the decorated function keeps its metadata.\n",
    "* Call the function being decorated and return the result.\n",
    "* Return the new decorator."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "666f9d6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n",
      "('test', 'this is a tag')\n"
     ]
    }
   ],
   "source": [
    "def tag(*tags):\n",
    "    # Define a new decorator, named \"decorator\", to return\n",
    "    def decorator(func):\n",
    "        # Ensure the decorated function keeps its metadata\n",
    "        @wraps(func)\n",
    "        def wrapper(*args, **kwargs):\n",
    "            # Call the function being decorated and return the result\n",
    "            return func(*args, **kwargs)\n",
    "        wrapper.tags = tags\n",
    "        return wrapper\n",
    "    # Return the new decorator\n",
    "    return decorator\n",
    "\n",
    "@tag('test', 'this is a tag')\n",
    "def foo():\n",
    "    pass\n",
    "\n",
    "print(foo.tags)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "974bf886",
   "metadata": {},
   "source": [
    "Terrific tagging! With this new decorator, you can do some really interesting things. For instance, you could tag a bunch of image transforming functions, and then write code that searches for all of the functions that transform images and apply them, one after the other, on a given input image. What other neat uses can you come up with for this decorator?\n",
    "\n",
    "## Check the return type\n",
    "Python's flexibility around data types is usually cited as one of the benefits of the language. It can sometimes cause problems though if incorrect data types go unnoticed. You've decided that in order to ensure your code is doing exactly what you want it to do, you will explicitly check the return types in all of your functions and make sure they're returning what you expect. To do that, you are going to create a decorator that checks if the return type of the decorated function is correct.\n",
    "\n",
    "Note: assert is a keyword that you can use to test whether something is true. If you type assert condition and condition is True, this function doesn't do anything. If condition is False, this function raises an error. The type of error that it raises is called an AssertionError.\n",
    "\n",
    "* Start by completing the `returns_dict()` decorator so that it raises an AssertionError if the return type of the decorated function is not a dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "70bc81f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n"
     ]
    }
   ],
   "source": [
    "def returns_dict(func):\n",
    "    # Complete the returns_dict() decorator\n",
    "    def wrapper(*args, **kwargs):\n",
    "        result = func(*args, **kwargs)\n",
    "        assert type(result) == dict\n",
    "        return result\n",
    "    return wrapper\n",
    "\n",
    "@returns_dict\n",
    "def foo(value):\n",
    "    return value\n",
    "\n",
    "try:\n",
    "    print(foo([1,2,3]))\n",
    "except AssertionError:\n",
    "    print('foo() did not return a dict!')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4971c223",
   "metadata": {},
   "source": [
    "* Now complete the `returns()` decorator, which takes the expected return type as an argument."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9b68b4b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n",
      "foo() did not return a dict!\n"
     ]
    }
   ],
   "source": [
    "def returns(return_type):\n",
    "    # Write a decorator that raises an AssertionError if the\n",
    "    # decorated function returns a value that is not return_type\n",
    "    def decorator(func):\n",
    "        def wrapper(*args, **kwargs):\n",
    "            result = func(*args, **kwargs)\n",
    "            assert type(result) == return_type\n",
    "            return result\n",
    "        return wrapper\n",
    "    return decorator\n",
    "  \n",
    "@returns(dict)\n",
    "def foo(value):\n",
    "    return value\n",
    "\n",
    "try:\n",
    "    print(foo([1,2,3]))\n",
    "except AssertionError:\n",
    "    print('foo() did not return a dict!')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "671d1462",
   "metadata": {},
   "source": [
    "You did it! We took the training wheels off on this exercise, and you still did a great job. You know how to write your own decorators now, but even more importantly, you know why they work the way they do."
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
