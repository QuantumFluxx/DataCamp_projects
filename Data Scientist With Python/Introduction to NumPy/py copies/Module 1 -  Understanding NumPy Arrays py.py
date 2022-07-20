{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c4959a02",
   "metadata": {},
   "source": [
    "# Introduction to NumPy\n",
    "\n",
    "## Understanding NumPy Arrays\n",
    "\n",
    "## Your first NumPy array\n",
    "Once you're comfortable with NumPy, you'll find yourself converting Python lists into NumPy arrays all the time for increased speed and access to NumPy's excellent array methods.\n",
    "\n",
    "sudoku_list is a Python list containing a sudoku game:\n",
    "```\n",
    "[[0, 0, 4, 3, 0, 0, 2, 0, 9],\n",
    " [0, 0, 5, 0, 0, 9, 0, 0, 1],\n",
    " [0, 7, 0, 0, 6, 0, 0, 4, 3],\n",
    " [0, 0, 6, 0, 0, 2, 0, 8, 7],\n",
    " [1, 9, 0, 0, 0, 7, 4, 0, 0],\n",
    " [0, 5, 0, 0, 8, 3, 0, 0, 0],\n",
    " [6, 0, 0, 0, 0, 0, 1, 0, 5],\n",
    " [0, 0, 3, 5, 0, 8, 6, 9, 0],\n",
    " [0, 4, 2, 9, 1, 0, 3, 0, 0]]\n",
    " ```\n",
    "You're going to change sudoku_list into a NumPy array so you can practice with it in later lessons, for example by creating a 4D array of sudoku games along with their solutions!\n",
    "\n",
    "* Import NumPy using its generally accepted alias.\n",
    "* Convert `sudoku_list` into a NumPy array called sudoku_array.\n",
    "* Print the class `type()` of sudoku_array to check that your code has worked properly."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "45699bbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "sudoku_list = \\\n",
    "[[0, 0, 4, 3, 0, 0, 2, 0, 9],\n",
    " [0, 0, 5, 0, 0, 9, 0, 0, 1],\n",
    " [0, 7, 0, 0, 6, 0, 0, 4, 3],\n",
    " [0, 0, 6, 0, 0, 2, 0, 8, 7],\n",
    " [1, 9, 0, 0, 0, 7, 4, 0, 0],\n",
    " [0, 5, 0, 0, 8, 3, 0, 0, 0],\n",
    " [6, 0, 0, 0, 0, 0, 1, 0, 5],\n",
    " [0, 0, 3, 5, 0, 8, 6, 9, 0],\n",
    " [0, 4, 2, 9, 1, 0, 3, 0, 0]]\n",
    "\n",
    "# Import NumPy\n",
    "import numpy as np\n",
    "\n",
    "# Convert sudoku_list into an array\n",
    "sudoku_array = np.array(sudoku_list)\n",
    "\n",
    "# Print the type of sudoku_array \n",
    "print(type(sudoku_array))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e5f63f7",
   "metadata": {},
   "source": [
    "Hip hip h-array! Notice that the class of sudoku_array is numpy.ndarray. ndarray is short for N-dimensional array, so-called because a NumPy array can have any number of dimensions.\n",
    "\n",
    "## Creating arrays from scratch\n",
    "It can be helpful to know how to create quick NumPy arrays from scratch in order to test your code. For example, when you are doing math with large multi-dimensional arrays, it's nice to check whether the math works as expected on small test arrays before applying your code to the larger arrays. NumPy has many options for creating smaller synthetic arrays.\n",
    "\n",
    "* Create and print an array filled with zeros called `zero_array`, which has two rows and four columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "18b501de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0. 0. 0.]\n",
      " [0. 0. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "# Create an array of zeros which has four columns and two rows\n",
    "zero_array = np.zeros((2, 4))\n",
    "print(zero_array)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4faea984",
   "metadata": {},
   "source": [
    "* Create and print an array of random floats between 0 and 1 called `random_array`, which has three rows and six columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "58d1fe4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[7.91294913e-01 2.58839120e-01 5.84162493e-01 6.05948635e-01\n",
      "  8.85801935e-01 9.46880696e-01]\n",
      " [8.07469983e-01 1.49634461e-01 6.91588918e-01 3.53815469e-01\n",
      "  8.50330797e-01 6.61150922e-01]\n",
      " [5.25474119e-01 8.99202827e-01 8.13043543e-02 4.29567089e-01\n",
      "  3.30435972e-01 1.98641082e-04]]\n"
     ]
    }
   ],
   "source": [
    "# Create an array of random floats which has six columns and three rows\n",
    "random_array = np.random.random((3, 6))\n",
    "print(random_array)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8820330",
   "metadata": {},
   "source": [
    "Looks like you had zero issues with these arrays! Well done. You also got some practice with array shapes, which are very important!\n",
    "\n",
    "## A range array\n",
    "np.arange() has especially useful applications in graphing. Your task is to create a scatter plot with the values from doubling_array on the y-axis.\n",
    "```python\n",
    "doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]\n",
    "```\n",
    "Recall that a scatter plot can be created using the following code:\n",
    "```\n",
    "plt.scatter(x_values, y_values)\n",
    "plt.show()\n",
    "```\n",
    "With doubling_array on the y-axis, you now need values for the x-axis, which you can create with np.arange()!\n",
    "\n",
    "* Using `np.arange()`, create a 1D array called one_to_ten which holds all integers from one to ten (inclusive).\n",
    "* Create a scatterplot with `doubling_array` as the y values and `one_to_ten` as the x values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "be539ab6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "22a2f9d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD4CAYAAAAXUaZHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAQyElEQVR4nO3dcahed33H8ffH26xedSMtTUtzU5YOQmZr0YxLcSsMZ91SppggFLKhhFHoP2WrQ+Ia/5H9USxkiP6xDoI6AzpL0JgGJ8aSKjIQ641xxLaGBqvtvcma6yTTjUtN43d/3JN6k9w0T3Kf5z5Pf/f9gnDO+T7nnOd7D7mfnPzOec6TqkKS1JY3DLsBSVL/Ge6S1CDDXZIaZLhLUoMMd0lq0DXDbgDghhtuqPXr1w+7DUl6XTl8+PDPq2rNYq+NRLivX7+eqampYbchSa8rSX52qdcclpGkBhnuktQgw12SGmS4S1KDDHdJatBI3C0jSSvN/iMz7Dp4jBOn51i7epwdmzeyddNE3/ZvuEvSMtt/ZIad+44yd+YsADOn59i57yhA3wLeYRlJWma7Dh57NdjPmTtzll0Hj/XtPQx3SVpmJ07PXVH9ahjukrTM1q4ev6L61egp3JP8NMnRJD9MMtXVrk/yRJLnuul1C9bfmeR4kmNJNvetW0lqwI7NGxlfNXZebXzVGDs2b+zbe1zJmfufVdU7qmqyW34IOFRVG4BD3TJJbgO2AbcD9wCPJhlbbIeStBJt3TTBJz5wBxOrxwkwsXqcT3zgjpG5W2YL8K5ufg/wbeAfuvpjVfUy8HyS48CdwHeX8F6S1JStmyb6GuYX6vXMvYBvJjmc5P6udlNVnQTopjd29QngxQXbTne18yS5P8lUkqnZ2dmr616StKhez9zvqqoTSW4Enkjy49dYN4vU6qJC1W5gN8Dk5ORFr0uSrl5PZ+5VdaKbngK+yvwwy0tJbgbopqe61aeBWxZsvg440a+GJUmXd9lwT/LmJL97bh74C+BHwAFge7faduDxbv4AsC3JtUluBTYAT/W7cUnSpfUyLHMT8NUk59b/t6r6RpLvA3uT3Ae8ANwLUFVPJ9kLPAO8AjxQVWcX37UkaRAuG+5V9RPg7YvU/xu4+xLbPAw8vOTuJElXxU+oSlKDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1qOdwTzKW5EiSr3XL1yd5Islz3fS6BevuTHI8ybEkmwfRuCTp0q7kzP1B4NkFyw8Bh6pqA3CoWybJbcA24HbgHuDRJGP9aVeS1Iuewj3JOuC9wGcWlLcAe7r5PcDWBfXHqurlqnoeOA7c2ZduJUk96fXM/VPAR4HfLKjdVFUnAbrpjV19AnhxwXrTXU2StEwuG+5J3gecqqrDPe4zi9Rqkf3en2QqydTs7GyPu5Yk9aKXM/e7gPcn+SnwGPDuJF8AXkpyM0A3PdWtPw3csmD7dcCJC3daVburarKqJtesWbOEH0GSdKHLhntV7ayqdVW1nvkLpU9W1QeBA8D2brXtwOPd/AFgW5Jrk9wKbACe6nvnkqRLumYJ2z4C7E1yH/ACcC9AVT2dZC/wDPAK8EBVnV1yp5KknqXqouHwZTc5OVlTU1PDbkOSXleSHK6qycVe8xOqktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGXDfckb0zyVJL/TPJ0kn/s6tcneSLJc930ugXb7ExyPMmxJJsH+QNIki7Wy5n7y8C7q+rtwDuAe5K8E3gIOFRVG4BD3TJJbgO2AbcD9wCPJhkbQO+SpEu4bLjXvP/tFld1fwrYAuzp6nuArd38FuCxqnq5qp4HjgN39rNpSdJr62nMPclYkh8Cp4Anqup7wE1VdRKgm97YrT4BvLhg8+muduE+708ylWRqdnZ2CT+CJOlCPYV7VZ2tqncA64A7k7ztNVbPYrtYZJ+7q2qyqibXrFnTU7OSpN5c0d0yVXUa+DbzY+kvJbkZoJue6labBm5ZsNk64MRSG5Uk9a6Xu2XWJFndzY8D7wF+DBwAtnerbQce7+YPANuSXJvkVmAD8FSf+5YkvYZreljnZmBPd8fLG4C9VfW1JN8F9ia5D3gBuBegqp5Oshd4BngFeKCqzg6mfUnSYlJ10XD4spucnKypqalhtyFJrytJDlfV5GKv+QlVSWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoN6+YSqJDVj/5EZdh08xonTc6xdPc6OzRvZuumiB9e+7hnuklaM/Udm2LnvKHNn5p+IMnN6jp37jgI0F/AOy0haMXYdPPZqsJ8zd+Ysuw4eG1JHg2O4S1oxTpyeu6L665nhLmnFWLt6/Irqr2eGu6QVY8fmjYyvGjuvNr5qjB2bNw6po8HxgqqkFePcRVPvlpGkxmzdNNFkmF/IYRlJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1KDLhnuSW5J8K8mzSZ5O8mBXvz7JE0me66bXLdhmZ5LjSY4l2TzIH0CSdLFeztxfAT5SVW8F3gk8kOQ24CHgUFVtAA51y3SvbQNuB+4BHk0ytuieJUkDcdlwr6qTVfWDbv5XwLPABLAF2NOttgfY2s1vAR6rqper6nngOHBnn/uWJL2GKxpzT7Ie2AR8D7ipqk7C/D8AwI3dahPAiws2m+5qF+7r/iRTSaZmZ2evonVJ0qX0HO5J3gJ8BfhwVf3ytVZdpFYXFap2V9VkVU2uWbOm1zYkST3oKdyTrGI+2L9YVfu68ktJbu5evxk41dWngVsWbL4OONGfdiVJvejlbpkAnwWerapPLnjpALC9m98OPL6gvi3JtUluBTYAT/WvZUnS5VzTwzp3AR8Cjib5YVf7GPAIsDfJfcALwL0AVfV0kr3AM8zfafNAVZ3td+OSpEu7bLhX1X+w+Dg6wN2X2OZh4OEl9CVJWgI/oSpJDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1qJcvyJakJdt/ZIZdB49x4vQca1ePs2PzRrZumhh2W80y3CUN3P4jM+zcd5S5M2cBmDk9x859RwEM+AFxWEbSwO06eOzVYD9n7sxZdh08NqSO2me4Sxq4E6fnrqiupTPcJQ3c2tXjV1TX0hnukgZux+aNjK8aO682vmqMHZs3Dqmj9nlBVdLAnbto6t0yy8dwl7Qstm6aMMyXkcMyktQgw12SGnTZcE/yuSSnkvxoQe36JE8kea6bXrfgtZ1Jjic5lmTzoBqXJF1aL2funwfuuaD2EHCoqjYAh7plktwGbANu77Z5NMkYkqRlddlwr6rvAL+4oLwF2NPN7wG2Lqg/VlUvV9XzwHHgzv60Kknq1dWOud9UVScBuumNXX0CeHHBetNdTZK0jPp9QTWL1GrRFZP7k0wlmZqdne1zG5K0sl1tuL+U5GaAbnqqq08DtyxYbx1wYrEdVNXuqpqsqsk1a9ZcZRuSpMVcbbgfALZ389uBxxfUtyW5NsmtwAbgqaW1KEm6Upf9hGqSLwHvAm5IMg18HHgE2JvkPuAF4F6Aqno6yV7gGeAV4IGqOrvojiVJA3PZcK+qv7rES3dfYv2HgYeX0pQkaWn8hKokNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkN/EJDVu/5EZv95uBTLcpYbtPzLDzn1HmTsz/1nCmdNz7Nx3FMCAb5zDMlLDdh089mqwnzN35iy7Dh4bUkdaLoa71LATp+euqK52GO5Sw9auHr+iutphuEsN27F5I+Orzv+my/FVY+zYvHFIHWm5eEFVati5i6beLbPyGO5S47ZumjDMVyCHZSSpQYa7JDXIcJekBhnuktQgL6hKA+RzXTQshrs0ID7XRcPksIw0ID7XRcNkuEsD4nNdNEyGuzQgPtdFw2S4SwPic100TF5QVZNG4S4Vn+uiYTLc1ZxRukvF57poWByWUXO8S0XyzF19NgrDId6lInnmrj46Nxwyc3qO4rfDIfuPzCxrH96lIhnuzdh/ZIa7HnmSWx/6d+565MllD1QYneEQ71KRBjgsk+Qe4NPAGPCZqnqk3+8xCkMAo9LDKFxAHJXhEO9SkQYU7knGgH8G/hyYBr6f5EBVPdOv9xiFQBuFHuC1z5iXs4+1q8eZWSTIhzEc4l0qWukGNSxzJ3C8qn5SVb8GHgO29PMNRmEIYBR6gNE5Y3Y4RBodgwr3CeDFBcvTXe1VSe5PMpVkanZ29orfYBQCbRR6gNG5gLh10wSf+MAdTKweJ8DE6nE+8YE7PIOWhmBQY+5ZpFbnLVTtBnYDTE5O1iLrv6ZRGAIYhR5g/ox54fAQDO+M2eEQaTQM6sx9GrhlwfI64EQ/32AUhgBGoQfwjFnSxQZ15v59YEOSW4EZYBvw1/18g1G4I2IUeljYi2Eu6ZxUXfGISG87Tv4S+BTzt0J+rqoevtS6k5OTNTU1NZA+JKlVSQ5X1eRirw3sPveq+jrw9UHtX5J0aX5CVZIaZLhLUoMMd0lqkOEuSQ0a2N0yV9REMgv8bNh9LNENwM+H3cQI8Xicz+PxWx6L8y3lePx+Va1Z7IWRCPcWJJm61C1JK5HH43wej9/yWJxvUMfDYRlJapDhLkkNMtz7Z/ewGxgxHo/zeTx+y2NxvoEcD8fcJalBnrlLUoMMd0lqkOG+REluSfKtJM8meTrJg8PuadiSjCU5kuRrw+5l2JKsTvLlJD/u/o788bB7GqYkf9/9nvwoyZeSvHHYPS2nJJ9LcirJjxbUrk/yRJLnuul1/Xgvw33pXgE+UlVvBd4JPJDktiH3NGwPAs8Ou4kR8WngG1X1h8DbWcHHJckE8HfAZFW9jfnHgW8bblfL7vPAPRfUHgIOVdUG4FC3vGSG+xJV1cmq+kE3/yvmf3lX7LdmJFkHvBf4zLB7GbYkvwf8KfBZgKr6dVWdHmpTw3cNMJ7kGuBN9Pkb2kZdVX0H+MUF5S3Anm5+D7C1H+9luPdRkvXAJuB7Q25lmD4FfBT4zZD7GAV/AMwC/9oNU30myZuH3dSwVNUM8E/AC8BJ4H+q6pvD7Wok3FRVJ2H+ZBG4sR87Ndz7JMlbgK8AH66qXw67n2FI8j7gVFUdHnYvI+Ia4I+Af6mqTcD/0af/cr8edWPJW4BbgbXAm5N8cLhdtctw74Mkq5gP9i9W1b5h9zNEdwHvT/JT4DHg3Um+MNyWhmoamK6qc/+T+zLzYb9SvQd4vqpmq+oMsA/4kyH3NApeSnIzQDc91Y+dGu5LlCTMj6k+W1WfHHY/w1RVO6tqXVWtZ/5C2ZNVtWLPzKrqv4AXk2zsSncDzwyxpWF7AXhnkjd1vzd3s4IvMC9wANjezW8HHu/HTgf2HaoryF3Ah4CjSX7Y1T7WfYes9LfAF5P8DvAT4G+G3M/QVNX3knwZ+AHzd5kdYYU9iiDJl4B3ATckmQY+DjwC7E1yH/P/AN7bl/fy8QOS1B6HZSSpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJatD/AxYFR8GUG9TkAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create an array of integers from one to ten\n",
    "one_to_ten = np.arange(1, 11)\n",
    "\n",
    "# Create your scatterplot\n",
    "plt.scatter(one_to_ten, doubling_array)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "508c5223",
   "metadata": {},
   "source": [
    "Awesome—now you know how to make quite a range of arrays! You've also discovered that Pyplot accepts arrays as inputs, which makes sense since Matplotlib is built on top of NumPy.\n",
    "\n",
    "## 3D array creation\n",
    "In the first lesson, you created a sudoku_game two-dimensional NumPy array. Perhaps you have hundreds of sudoku game arrays, and you'd like to save the solution for this one, sudoku_solution, as part of the same array as its corresponding game in order to organize your sudoku data better. You could accomplish this by stacking the two 2D arrays on top of each other to create a 3D array.\n",
    "\n",
    "* Create a 3D array called `game_and_solution` by stacking the two 2D arrays, `sudoku_game` and `sudoku_solution`, on top of one another; in the final array, `sudoku_game` should appear before `sudoku_solution`.\n",
    "* Print `game_and_solution`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "67e49d02",
   "metadata": {},
   "outputs": [],
   "source": [
    "sudoku_game = np.load('datasets/sudoku_game.npy')\n",
    "sudoku_solution = np.load('datasets/sudoku_solution.npy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "64d75836",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0 0 5 0 0 9 0 0 1]\n",
      "  [0 7 0 0 6 0 0 4 3]\n",
      "  [0 0 6 0 0 2 0 8 7]\n",
      "  [1 9 0 0 0 7 4 0 0]\n",
      "  [0 5 0 0 8 3 0 0 0]\n",
      "  [6 0 0 0 0 0 1 0 5]\n",
      "  [0 0 3 5 0 8 6 9 0]\n",
      "  [0 4 2 9 1 0 3 0 0]]\n",
      "\n",
      " [[3 2 5 8 4 9 7 6 1]\n",
      "  [9 7 1 2 6 5 8 4 3]\n",
      "  [4 3 6 1 9 2 5 8 7]\n",
      "  [1 9 8 6 5 7 4 3 2]\n",
      "  [2 5 7 4 8 3 9 1 6]\n",
      "  [6 8 9 7 3 4 1 2 5]\n",
      "  [7 1 3 5 2 8 6 9 4]\n",
      "  [5 4 2 9 1 6 3 7 8]]]\n"
     ]
    }
   ],
   "source": [
    "# Create the game_and_solution 3D array\n",
    "game_and_solution = np.array([sudoku_game, sudoku_solution])\n",
    "\n",
    "# Print game_and_solution\n",
    "print(game_and_solution) "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6f651c1",
   "metadata": {},
   "source": [
    "Nice work! Notice how storing sudoku_game and sudoku_solution in three dimensions makes more sense than adding the data from both to one 2D array.\n",
    "\n",
    "## The fourth dimension\n",
    "Printing arrays is a good way to check code output for small arrays like `sudoku_game_and_solution`, but it becomes unwieldy when dealing with bigger arrays and those with higher dimensions. Another important check is to look at the array's `.shape`.\n",
    "\n",
    "Now, you'll create a 4D array that contains two sudoku games and their solutions. numpy is loaded as np. The `game_and_solution` 3D array you created in the previous example is available, along with `new_sudoku_game` and `new_sudoku_solution`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "683906f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 2, 8, 9)\n"
     ]
    }
   ],
   "source": [
    "new_sudoku_game = np.load('datasets/sudoku_game.npy')\n",
    "new_sudoku_solution = np.load('datasets/sudoku_solution.npy')\n",
    "\n",
    "# Create a second 3D array of another game and its solution \n",
    "new_game_and_solution = np.array([new_sudoku_game, new_sudoku_solution])\n",
    "\n",
    "# Create a 4D array of both game and solution 3D arrays\n",
    "games_and_solutions = np.array([game_and_solution, new_game_and_solution])\n",
    "\n",
    "# Print the shape of your 4D array\n",
    "print(games_and_solutions.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "356c74f3",
   "metadata": {},
   "source": [
    "Fabulous 4D array! The .shape of (2, 2, 8, 9) means that there are two sets of game/solution pairs. Within each game/solution pair, all arrays have nine rows and nine columns. That's exactly right! If there were ten game/solution pairs, the .shape would be (10, 2, 9, 9).\n",
    "\n",
    "## Flattening and reshaping\n",
    "You've learned to change not only array shape but also the number of dimensions that an array has. To test these skills, you'll change sudoku_game from a 2D array to a 1D array and back again. Can we trust NumPy to keep the array elements in the same order after being flattened and reshaped? Time to find out.\n",
    "\n",
    "* Flatten `sudoku_game` so that it is a 1D array, and save it as `flattened_game`.\n",
    "* Print the `.shape` of flattened_game."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "db96331d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(72,)\n"
     ]
    }
   ],
   "source": [
    "# Flatten sudoku_game\n",
    "flattened_game = sudoku_game.flatten()\n",
    "\n",
    "# Print the shape of flattened_game\n",
    "print(flattened_game.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "829bdbe9",
   "metadata": {},
   "source": [
    "* Reshape the `flattened_game` back to its original shape of nine rows and nine columns; save the new array as `reshaped_game`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "3375115e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 0 5 0 0 9 0 0 1]\n",
      " [0 7 0 0 6 0 0 4 3]\n",
      " [0 0 6 0 0 2 0 8 7]\n",
      " [1 9 0 0 0 7 4 0 0]\n",
      " [0 5 0 0 8 3 0 0 0]\n",
      " [6 0 0 0 0 0 1 0 5]\n",
      " [0 0 3 5 0 8 6 9 0]\n",
      " [0 4 2 9 1 0 3 0 0]]\n",
      "[[0 0 5 0 0 9 0 0 1]\n",
      " [0 7 0 0 6 0 0 4 3]\n",
      " [0 0 6 0 0 2 0 8 7]\n",
      " [1 9 0 0 0 7 4 0 0]\n",
      " [0 5 0 0 8 3 0 0 0]\n",
      " [6 0 0 0 0 0 1 0 5]\n",
      " [0 0 3 5 0 8 6 9 0]\n",
      " [0 4 2 9 1 0 3 0 0]]\n"
     ]
    }
   ],
   "source": [
    "# Reshape flattened_game back to a nine by nine array\n",
    "reshaped_game = flattened_game.reshape((8, 9))\n",
    "\n",
    "# Print sudoku_game and reshaped_game\n",
    "print(sudoku_game)\n",
    "print(reshaped_game)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3661af1b",
   "metadata": {},
   "source": [
    "Phew! Nice work resurrecting that sudoku game. Notice that .flatten() preserves the order of array elements—when the array is reshaped back to its original shape, the numbers are in the exact same places as they were before flattening.\n",
    "\n",
    "## The dtype argument\n",
    "One way to control the data type of a NumPy array is to declare it when the array is created using the dtype keyword argument. Take a look at the data type NumPy uses by default when creating an array with `np.zeros()`. Could it be updated?\n",
    "\n",
    "* Using `np.zeros()`, create an array of zeros that has three rows and two columns; call it `zero_array`.\n",
    "* Print the data type of `zero_array`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "048f7ef9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "float64\n"
     ]
    }
   ],
   "source": [
    "# Create an array of zeros with three rows and two columns\n",
    "zero_array = np.zeros((3, 2))\n",
    "\n",
    "# Print the data type of zero_array\n",
    "print(zero_array.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "839581ba",
   "metadata": {},
   "source": [
    "* Create a new array of zeros called `zero_int_array`, which will also have three rows and two columns, but the data type should be `np.int32`.\n",
    "* Print the data type of `zero_int_array`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "6e39c7e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int32\n"
     ]
    }
   ],
   "source": [
    "# Create a new array of int32 zeros with three rows and two columns\n",
    "zero_int_array = np.zeros((3, 2), dtype=np.int32)\n",
    "\n",
    "# Print the data type of zero_int_array\n",
    "print(zero_int_array.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eaa35e65",
   "metadata": {},
   "source": [
    "Nice! Since your original zero_array did not have any information following the decimal places of the floats, it makes sense to change the array's data type to an integer with a smaller bitsize.\n",
    "\n",
    "## A smaller sudoku game\n",
    "NumPy data types, which emphasize speed, are more specific than Python data types, which emphasize flexibility. When working with large amounts of data in NumPy, it's good practice to check the data type and consider whether a smaller data type is large enough for your data, since smaller data types use less memory.\n",
    "\n",
    "- Print the data type of the elements in `sudoku_game`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "fc61af7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int64\n"
     ]
    }
   ],
   "source": [
    "# Print the data type of sudoku_game\n",
    "print(sudoku_game.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca90776f",
   "metadata": {},
   "source": [
    "The current data type of sudoku_game is int64. Which of the following NumPy integers is the smallest bitsize that is still large enough to hold the data in sudoku_game? If you have never played sudoku, know that sudoku games only ever store integers from one to nine.\n",
    "\n",
    "\n",
    "* np.int64\n",
    "\n",
    "* np.int32\n",
    "\n",
    "* np.int16\n",
    "\n",
    "* **np.int8**\n",
    "\n",
    "* Change the data type of sudoku_game to be int8, an 8-bit integer; name the new array `small_sudoku_game`.\n",
    "* Print the data type of `small_sudoku_game` to be sure that your change to int8 is reflected."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "f867c4c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int8\n"
     ]
    }
   ],
   "source": [
    "# Change the data type of sudoku_game to int8\n",
    "small_sudoku_game = sudoku_game.astype(np.int8)\n",
    "\n",
    "# Print the data type of small_sudoku_game\n",
    "print(small_sudoku_game.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38c4bb5b",
   "metadata": {},
   "source": [
    "Int-credible! Gr8 data type casting! int8 is one of the smallest data types in NumPy since 8 bits is only a single byte."
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
