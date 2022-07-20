{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a913c3e4",
   "metadata": {},
   "source": [
    "# Array Mathematics!\n",
    "\n",
    "## Sales totals\n",
    "The dataset you'll be working with during this chapter is one year's sales data by month for three different industries. Each row in this `monthly_sales` array represents a month from January to December. The first column has monthly sales data for liquor stores, the second column has data for restaurants, and the last column tracks sales for department stores.\n",
    "```\n",
    "array([[ 4134, 23925,  8657],\n",
    "       [ 4116, 23875,  9142],\n",
    "       [ 4673, 27197, 10645],\n",
    "       [ 4580, 25637, 10456],\n",
    "       [ 5109, 27995, 11299],\n",
    "       [ 5011, 27419, 10625],\n",
    "       [ 5245, 27305, 10630],\n",
    "       [ 5270, 27760, 11550],\n",
    "       [ 4680, 24988,  9762],\n",
    "       [ 4913, 25802, 10456],\n",
    "       [ 5312, 25405, 13401],\n",
    "       [ 6630, 27797, 18403]])\n",
    "```\n",
    "\n",
    "Your task is to create an array with all the information from `monthly_sales` as well as a fourth column which totals the monthly sales across industries for each month.\n",
    "\n",
    "* Create a 2D array which contains a single column of total monthly sales across industries; call it `monthly_industry_sales`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e49bb03e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[36716]\n",
      " [37133]\n",
      " [42515]\n",
      " [40673]\n",
      " [44403]\n",
      " [43055]\n",
      " [43180]\n",
      " [44580]\n",
      " [39430]\n",
      " [41171]\n",
      " [44118]\n",
      " [52830]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "monthly_sales = np.load('datasets/monthly_sales.npy')\n",
    "\n",
    "# Create a 2D array of total monthly sales across industries\n",
    "monthly_industry_sales = monthly_sales.sum(axis=1, keepdims=True)\n",
    "print(monthly_industry_sales)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f567da81",
   "metadata": {},
   "source": [
    "* Concatenate `monthly_industry_sales` with `monthly_sales` into a new array called `monthly_sales_with_total`, with the monthly cross-industry sales information in the final column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5efc29dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 4134 23925  8657 36716]\n",
      " [ 4116 23875  9142 37133]\n",
      " [ 4673 27197 10645 42515]\n",
      " [ 4580 25637 10456 40673]\n",
      " [ 5109 27995 11299 44403]\n",
      " [ 5011 27419 10625 43055]\n",
      " [ 5245 27305 10630 43180]\n",
      " [ 5270 27760 11550 44580]\n",
      " [ 4680 24988  9762 39430]\n",
      " [ 4913 25802 10456 41171]\n",
      " [ 5312 25405 13401 44118]\n",
      " [ 6630 27797 18403 52830]]\n"
     ]
    }
   ],
   "source": [
    "# Add this column as the last column in monthly_sales\n",
    "monthly_sales_with_total = np.concatenate((monthly_sales, monthly_industry_sales), axis=1)\n",
    "print(monthly_sales_with_total)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4294db68",
   "metadata": {},
   "source": [
    "Those are sum good-looking arrays! Notice how using the keepdims keyword is helpful not only for dimension compatibility but also for visualizing which axis your aggregating data originates from!\n",
    "\n",
    "## Plotting averages\n",
    "Perhaps you have a hunch that department stores see greater increased sales than average during the end of the year as people rush to buy gifts. You'd like to test this theory by comparing monthly department store sales to average sales across all three industries.\n",
    "\n",
    "* Create a 1D array called `avg_monthly_sales`, which contains an average sales amount for each month across the three industries."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e8416e5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12238.66666667 12377.66666667 14171.66666667 13557.66666667\n",
      " 14801.         14351.66666667 14393.33333333 14860.\n",
      " 13143.33333333 13723.66666667 14706.         17610.        ]\n"
     ]
    }
   ],
   "source": [
    "# Create the 1D array avg_monthly_sales\n",
    "avg_monthly_sales = monthly_sales.mean(axis=1)\n",
    "print(avg_monthly_sales)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8c6d542",
   "metadata": {},
   "source": [
    "* Plot an array of the numbers one through twelve (representing each month) on the x-axis and `avg_monthly_sales` on the y-axis.\n",
    "* Plot an array of the numbers one through twelve on the x-axis and the department store sales column of `monthly_sales` on the y-axis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7ff10c98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
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
    "# Plot avg_monthly_sales by month\n",
    "plt.plot(np.arange(1, 13), avg_monthly_sales, label=\"Average sales across industries\")\n",
    "\n",
    "# Plot department store sales by month\n",
    "plt.plot(np.arange(1, 13), monthly_sales[:, 2], label=\"Department store sales\")\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14a27077",
   "metadata": {},
   "source": [
    "Great plot! Based on your work, it does look like department store sales are even greater than the average sales across three industries with heavy end-of-year sales—at least in December!\n",
    "\n",
    "## Cumulative sales\n",
    "In the last exercise, you established that December is a big month for department stores. Are there other months where sales increase or decrease significantly?\n",
    "\n",
    "Your task now is to look at monthly cumulative sales for each industry. The slope of the cumulative sales line will explain a lot about how steady sales are over time: a straight line will indicate steady growth, and changes in slope will indicate relative increases or decreases in sales.\n",
    "\n",
    "- Find cumulative monthly sales for each industry, saving this data in an array called `cumulative_monthly_industry_sales`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0b749646",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  4134  23925   8657]\n",
      " [  8250  47800  17799]\n",
      " [ 12923  74997  28444]\n",
      " [ 17503 100634  38900]\n",
      " [ 22612 128629  50199]\n",
      " [ 27623 156048  60824]\n",
      " [ 32868 183353  71454]\n",
      " [ 38138 211113  83004]\n",
      " [ 42818 236101  92766]\n",
      " [ 47731 261903 103222]\n",
      " [ 53043 287308 116623]\n",
      " [ 59673 315105 135026]]\n"
     ]
    }
   ],
   "source": [
    "# Find cumulative monthly sales for each industry\n",
    "cumulative_monthly_industry_sales = monthly_sales.cumsum(axis=0)\n",
    "print(cumulative_monthly_industry_sales)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17bf9669",
   "metadata": {},
   "source": [
    "* Plot each industry's cumulative sales by month as separate lines, with cumulative sales on the y-axis and month number on the x-axis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "37298efd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
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
    "# Plot each industry's cumulative sales by month as separate lines\n",
    "plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 0], label=\"Liquor Stores\")\n",
    "plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 1], label=\"Restaurants\")\n",
    "plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 2], label=\"Department stores\")\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e62c4bf",
   "metadata": {},
   "source": [
    "Nice work! Your graph indicates that sales for both restaurants and liquor stores are fairly steady throughout the year. The biggest sales growth is the growth you identified in the previous task: department store sales increase towards the end of the year.\n",
    "\n",
    "## Tax calculations\n",
    "It's possible to use vectorized operations to calculate taxes for the liquor, restaurant, and department store industries! We'll simplify the tax calculation process here and assume that government collects 5% of all sales across these industries as tax revenue.\n",
    "\n",
    "* Create an array called `tax_collected` which calculates tax collected by industry and month by multiplying each element in `monthly_sales` by 0.05.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "113251c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 206.7  1196.25  432.85]\n",
      " [ 205.8  1193.75  457.1 ]\n",
      " [ 233.65 1359.85  532.25]\n",
      " [ 229.   1281.85  522.8 ]\n",
      " [ 255.45 1399.75  564.95]\n",
      " [ 250.55 1370.95  531.25]\n",
      " [ 262.25 1365.25  531.5 ]\n",
      " [ 263.5  1388.    577.5 ]\n",
      " [ 234.   1249.4   488.1 ]\n",
      " [ 245.65 1290.1   522.8 ]\n",
      " [ 265.6  1270.25  670.05]\n",
      " [ 331.5  1389.85  920.15]]\n"
     ]
    }
   ],
   "source": [
    "# Create an array of tax collected by industry and month\n",
    "tax_collected = monthly_sales * 0.05\n",
    "print(tax_collected)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6fb2e035",
   "metadata": {},
   "source": [
    "* Create an array that keeps track of `total_tax_and_revenue` collected by each industry and month by adding each element in `tax_collected` with its corresponding element in `monthly_sales`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4506dd7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 4340.7  25121.25  9089.85]\n",
      " [ 4321.8  25068.75  9599.1 ]\n",
      " [ 4906.65 28556.85 11177.25]\n",
      " [ 4809.   26918.85 10978.8 ]\n",
      " [ 5364.45 29394.75 11863.95]\n",
      " [ 5261.55 28789.95 11156.25]\n",
      " [ 5507.25 28670.25 11161.5 ]\n",
      " [ 5533.5  29148.   12127.5 ]\n",
      " [ 4914.   26237.4  10250.1 ]\n",
      " [ 5158.65 27092.1  10978.8 ]\n",
      " [ 5577.6  26675.25 14071.05]\n",
      " [ 6961.5  29186.85 19323.15]]\n"
     ]
    }
   ],
   "source": [
    "# Create an array of sales revenue plus tax collected by industry and month\n",
    "total_tax_and_revenue = tax_collected + monthly_sales\n",
    "print(total_tax_and_revenue)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "475a3b3c",
   "metadata": {},
   "source": [
    "Hope that wasn't too taxing! Your code looks great, and you've probably noticed that doing mathematical operations with scalars or arrays of the same shape is pretty straightforward. We'll build on this in the next chapter when we explore how NumPy approaches math between two arrays of different shapes!\n",
    "\n",
    "## Projecting sales\n",
    "You'd like to be able to plan for next year's operations by projecting what sales will be, and you've gathered multipliers specific to each month and industry. These multipliers are saved in an array called monthly_industry_multipliers. For example, the multiplier at monthly_industry_multipliers[0, 0] of 0.98 means that the liquor store industry is projected to have 98% of this January's sales in January of next year.\n",
    "```\n",
    "array([[0.98, 1.02, 1.  ],\n",
    "       [1.00, 1.01, 0.97],\n",
    "       [1.06, 1.03, 0.98],\n",
    "       [1.08, 1.01, 0.98],\n",
    "       [1.08, 0.98, 0.98],\n",
    "       [1.1 , 0.99, 0.99],\n",
    "       [1.12, 1.01, 1.  ],\n",
    "       [1.1 , 1.02, 1.  ],\n",
    "       [1.11, 1.01, 1.01],\n",
    "       [1.08, 0.99, 0.97],\n",
    "       [1.09, 1.  , 1.02],\n",
    "       [1.13, 1.03, 1.02]])\n",
    "```\n",
    "\n",
    "* Create an array called `projected_monthly_sales` which contains projected sales for all three industries based on the multipliers you have gathered."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "66f28572",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 4051.32 23446.5   8483.86]\n",
      " [ 4033.68 23397.5   8959.16]\n",
      " [ 4579.54 26653.06 10432.1 ]\n",
      " [ 4488.4  25124.26 10246.88]\n",
      " [ 5006.82 27435.1  11073.02]\n",
      " [ 4910.78 26870.62 10412.5 ]\n",
      " [ 5140.1  26758.9  10417.4 ]\n",
      " [ 5164.6  27204.8  11319.  ]\n",
      " [ 4586.4  24488.24  9566.76]\n",
      " [ 4814.74 25285.96 10246.88]\n",
      " [ 5205.76 24896.9  13132.98]\n",
      " [ 6497.4  27241.06 18034.94]]\n"
     ]
    }
   ],
   "source": [
    "monthly_industry_multipliers = 0.98\n",
    "\n",
    "# Create an array of monthly projected sales for all industries\n",
    "projected_monthly_sales = monthly_sales * monthly_industry_multipliers\n",
    "print(projected_monthly_sales)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e3da870",
   "metadata": {},
   "source": [
    "* Create a graph that plots two lines: current liquor store sales by month and projected liquor store sales by month; months will be represented by an array of the numbers one through twelve."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ed2d34ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAD4CAYAAAAAczaOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAABGU0lEQVR4nO3deVxU1fvA8c9hFxQXwH0BFTUFREXFXdNcytQ0yzYzLduz+lVafetbtlnfVls0K7PFzHIpSy3DDdzFcpcABRVXUEH2Zeb8/rgDgiwiDgzL8369eM3MmXvvnIv43DvPPfc5SmuNEEKImsHO1h0QQghRcSToCyFEDSJBXwghahAJ+kIIUYNI0BdCiBrEwdYduBJPT0/t7e1t624IIUSVsmvXrgSttdfl7ZU+6Ht7exMeHm7rbgghRJWilDpaVLukd4QQogaRoC+EEDWIBH0hhKhBKn1OvyjZ2dnExcWRkZFh664IUSwXFxeaN2+Oo6OjrbsiRJ4qGfTj4uKoU6cO3t7eKKVs3R0hCtFac+7cOeLi4vDx8bF1d4TIUyXTOxkZGXh4eEjAF5WWUgoPDw/5NioqnSoZ9AEJ+KLSk79RURlV2aAvhBDV1a6jF/h0fTTJGdlW37YE/TI6ffo0EyZMoE2bNnTs2JEbb7yRyMjICu3Dhg0b2LJlS5HvLViwgMceewyAuXPn8u2331Zk14pUUn8rWu3atW3dBSGK9duek3y8LgpHe+uH6Cp5IdfWtNbccsst3Hvvvfz4448A7N69mzNnztCuXbtSbcNkMmFvb1/s69LYsGEDtWvXpnfv3iUu99BDD13VdsuiNP0vbX/zy8nJwcFB/kxFzRIaGU9waw9cHK8uJpSGnOmXwfr163F0dCwQTAMDA+nXrx8bNmxg5MiRee2PPfYYCxYsAIySEjNnzqRv3778/PPPhV6vWbOGXr160bVrV8aPH09KSkreev/973/p2rUr/v7+REREEBsby9y5c/nggw8IDAwkLCys2P6+8sorvPvuuwDs2rWLzp0706tXL5599ln8/PyAgt8MAEaOHMmGDRsAWLRoEf7+/vj5+TF9+vS8ZWrXrs3LL79Mz5492bp1a4HPnD17Nh07diQgIIAJEyYU2d+jR48yePBgAgICGDx4MMeOHQNg0qRJPP300wwaNIjp06dz+PBhhg8fTrdu3ejXrx8RERGF9nHjxo0EBgYSGBhIly5dSE5OJiUlhcGDB+f93n799dcifz//+9//6N69OwEBAfz3v/8FIDU1lZtuuonOnTvj5+fH4sWLi/39CmFNx8+ncSQhlf6+hcrmWEWVP4V69bcDHDx50arb7NjUnf/e3KnY9/fv30+3bt3KtG0XFxc2bdoEwIwZM/JeJyQkMHbsWEJCQnBzc+Ptt9/m/fff5+WXXwbA09OTv//+m88++4x3332XL7/8koceeojatWvzzDPPlPrz77vvPj7++GMGDBjAs88+e8XlT548yfTp09m1axf169dn6NCh/PLLL4wZM4bU1FT8/PyYOXNmofVmzZpFTEwMzs7OJCYmUq9evUL9vfnmm5k4cSL33nsv8+fP54knnuCXX34BIDIykpCQEOzt7Rk8eDBz587F19eX7du388gjj7Bu3boCn/fuu+/y6aef0qdPH1JSUnBxcQFg+fLluLu7k5CQQHBwMKNGjSpwgXXNmjVERUWxY8cOtNaMGjWK0NBQ4uPjadq0KStXrgQgKSmp1L9jIa5FWFQCAP3beZbL9uVMv4LdfvvtRb7etm0bBw8epE+fPgQGBvLNN99w9Oilekljx44FoFu3bsTGxpbps5OSkkhMTGTAgAEA3HPPPVdcZ+fOnQwcOBAvLy8cHBy46667CA0NBcDe3p5x48YVuV5AQAB33XUX33//fbHpma1bt3LnnXfm9SX3YAgwfvx47O3tSUlJYcuWLYwfP57AwEAefPBBTp06VWhbffr04emnn2b27NkkJibi4OCA1poXXniBgIAAhgwZwokTJzhz5kyB9dasWcOaNWvo0qULXbt2JSIigqioKPz9/QkJCWH69OmEhYVRt27dK/6uhLCGsKh4mtZ1oY1X+Vx3qvJn+iWdkZeXTp06sWTJkiLfc3BwwGw2572+fJy2m5tbka+11txwww0sWrSoyO06OzsDRqDNyckpU7+11sUOIyyu31rrYrfn4uJSbB5/5cqVhIaGsmLFCl577TUOHDhwxf7l71vu78VsNlOvXj12795d4rozZszgpptuYtWqVQQHBxMSEsK2bduIj49n165dODo64u3tXejfQ2vN888/z4MPPlhom7t27WLVqlU8//zzDB06NO9blxDlJcdkZlN0Ajf6NSm3Ib9ypl8G119/PZmZmXzxxRd5bTt37mTjxo20atWKgwcP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\n",
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
    "# Graph current liquor store sales and projected liquor store sales by month\n",
    "plt.plot(np.arange(1, 13), monthly_sales[:, 0], label=\"Current liquor store sales\")\n",
    "plt.plot(np.arange(1, 13), projected_monthly_sales[:, 0], label=\"Projected liquor store sales\")\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c0cbf59",
   "metadata": {},
   "source": [
    "Well done! It looks like the liquor industry is projected to have a tough January next year. After that, though, projected sales are looking just fine.\n",
    "\n",
    "## Vectorizing .upper()\n",
    "There are many situations where you might want to use Python methods and functions on array elements in NumPy. You can always write a for loop to do this, but vectorized operations are much faster and more efficient, so consider using `np.vectorize()`!\n",
    "\n",
    "You've got an array called names which contains first and last names:\n",
    "```python\n",
    "names = np.array([[\"Izzy\", \"Monica\", \"Marvin\"],\n",
    "                  [\"Weber\", \"Patel\", \"Hernandez\"]])\n",
    "```\n",
    "You'd like to use one of the Python methods you learned on DataCamp, .upper(), to make all the letters of every name in the array uppercase. As a reminder, `.upper()` is a string method, meaning that it must be called on an instance of a string: `str.upper()`.\n",
    "\n",
    "* Create a vectorized function called `vectorized_upper` from the Python `.upper()` string method.\n",
    "* Apply `vectorized_upper()` to the names array and save the resulting array as `uppercase_names`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "98a8de59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['IZZY' 'MONICA' 'MARVIN']\n",
      " ['WEBER' 'PATEL' 'HERNANDEZ']]\n"
     ]
    }
   ],
   "source": [
    "names = np.array([[\"Izzy\", \"Monica\", \"Marvin\"],\n",
    "                  [\"Weber\", \"Patel\", \"Hernandez\"]])\n",
    "\n",
    "# Vectorize the .upper() string method\n",
    "vectorized_upper = np.vectorize(str.upper)\n",
    "\n",
    "# Apply vectorized_upper to the names array\n",
    "uppercase_names = vectorized_upper(names)\n",
    "print(uppercase_names)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb606ab8",
   "metadata": {},
   "source": [
    "Awesome—you can now brag to your friends about how you can vectorize Python functions! You also just harnessed the power of C in your Python code to make it more efficient. Don't forget about np.vectorize() once you've learned to write your own Python functions—you can vectorize those, too!\n",
    "\n",
    "## Broadcasting across columns\n",
    "Recall that when broadcasting across columns, NumPy requires you to be explicit that it should broadcast a vertical array, and horizontal and vertical 1D arrays do not exist in NumPy. Instead, you must first create a 2D array to declare that you have vertical data. Then, NumPy creates a copy of this 2D vertical array for each column and applies the desired operation.\n",
    "\n",
    "A Python list called `monthly_growth`_rate with `len()` of 12 is available. This list represents monthly year-over-year expected growth for the economy; your task is to use broadcasting to multiply this list by each column in the `monthly_sales` array. The `monthly_sales` array is loaded, along with numpy as np.\n",
    "\n",
    "* Convert `monthly_growth_rate`, currently a Python list, into a one-dimensional NumPy array called `monthly_growth_1D`.\n",
    "* Reshape `monthly_growth_1D` so that it is broadcastable column-wise across monthly_sales; call the new array `monthly_growth_2D`.\n",
    "* Using broadcasting, multiply each column in `monthly_sales` by `monthly_growth_2D`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d62c314",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert monthly_growth_rate into a NumPy array\n",
    "monthly_growth_1D = np.array(monthly_growth_rate)\n",
    "\n",
    "# Reshape monthly_growth_1D\n",
    "monthly_growth_2D = monthly_growth_1D.reshape((12, 1))\n",
    "\n",
    "# Multiply each column in monthly_sales by monthly_growth_2D\n",
    "print(monthly_growth_2D * monthly_sales)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3bc91acb",
   "metadata": {},
   "source": [
    "You've now harnessed the power of broadcasting! Notice how .reshape() was critical here for helping NumPy understand what you wanted it to do. We don't just reshape data for the sake of it!\n",
    "\n",
    "## Broadcasting across rows\n",
    "In the last set of exercises, you used `monthly_industry_multipliers`, to create sales predictions. Recall that `monthly_industry_multipliers` looks like this:\n",
    "```\n",
    "array([[0.98, 1.02, 1.  ],\n",
    "       [1.00, 1.01, 0.97],\n",
    "       [1.06, 1.03, 0.98],\n",
    "       [1.08, 1.01, 0.98],\n",
    "       [1.08, 0.98, 0.98],\n",
    "       [1.1 , 0.99, 0.99],\n",
    "       [1.12, 1.01, 1.  ],\n",
    "       [1.1 , 1.02, 1.  ],\n",
    "       [1.11, 1.01, 1.01],\n",
    "       [1.08, 0.99, 0.97],\n",
    "       [1.09, 1.  , 1.02],\n",
    "       [1.13, 1.03, 1.02]])\n",
    "```       \n",
    "Assume you're not comfortable being so specific with your estimates. Rather, you'd like to use `monthly_industry_multipliers` to find a single average multiplier for each industry. Then you'll use that multiplier to project next year's sales.\n",
    "\n",
    "* Find the mean sales projection multiplier for each industry; save in an array `called mean_multipliers`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "2c3d6fef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.0775     1.00833333 0.99333333]\n"
     ]
    }
   ],
   "source": [
    "monthly_industry_multipliers = np.array \\\n",
    "      ([[0.98, 1.02, 1.  ],\n",
    "       [1.00, 1.01, 0.97],\n",
    "       [1.06, 1.03, 0.98],\n",
    "       [1.08, 1.01, 0.98],\n",
    "       [1.08, 0.98, 0.98],\n",
    "       [1.1 , 0.99, 0.99],\n",
    "       [1.12, 1.01, 1.  ],\n",
    "       [1.1 , 1.02, 1.  ],\n",
    "       [1.11, 1.01, 1.01],\n",
    "       [1.08, 0.99, 0.97],\n",
    "       [1.09, 1.  , 1.02],\n",
    "       [1.13, 1.03, 1.02]])\n",
    "\n",
    "# Find the mean sales projection multiplier for each industry\n",
    "mean_multipliers = monthly_industry_multipliers.mean(axis=0)\n",
    "print(mean_multipliers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1619b51",
   "metadata": {},
   "source": [
    "* Print the shapes of `mean_multipliers` and `monthly_sales` to ensure they are suitable for broadcasting."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "94a5c2ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3,) (12, 3)\n"
     ]
    }
   ],
   "source": [
    "# Print the shapes of mean_multipliers and monthly_sales\n",
    "print(mean_multipliers.shape, monthly_sales.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5b881510",
   "metadata": {},
   "source": [
    "* Multiply each monthly sales value by the mean multiplier you found for that industry; save in an array called `projected_sales`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b3144064",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 4454.385      24124.375       8599.28666667]\n",
      " [ 4434.99       24073.95833333  9081.05333333]\n",
      " [ 5035.1575     27423.64166667 10574.03333333]\n",
      " [ 4934.95       25850.64166667 10386.29333333]\n",
      " [ 5504.9475     28228.29166667 11223.67333333]\n",
      " [ 5399.3525     27647.49166667 10554.16666667]\n",
      " [ 5651.4875     27532.54166667 10559.13333333]\n",
      " [ 5678.425      27991.33333333 11473.        ]\n",
      " [ 5042.7        25196.23333333  9696.92      ]\n",
      " [ 5293.7575     26017.01666667 10386.29333333]\n",
      " [ 5723.68       25616.70833333 13311.66      ]\n",
      " [ 7143.825      28028.64166667 18280.31333333]]\n"
     ]
    }
   ],
   "source": [
    "# Multiply each value by the multiplier for that industry\n",
    "projected_sales = monthly_sales * mean_multipliers\n",
    "print(projected_sales)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37be907d",
   "metadata": {},
   "source": [
    "Stellar work! Think about how much code you'd have had to write to perform the same operations on a Python list! Broadcasting is a huge advantage of working with NumPy."
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
