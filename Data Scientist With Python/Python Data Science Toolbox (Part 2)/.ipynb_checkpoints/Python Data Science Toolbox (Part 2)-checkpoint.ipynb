{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Bringing it all together!\n",
    "\n",
    "### This chapter will allow you to apply your newly acquired skills towards wrangling and extracting meaningful information from a real-world dataset - the World Bank's World Development Indicators dataset! You'll have the chance to write your own functions and list comprehensions as you work with iterators and generators and solidify your Python Data Science chops. Enjoy!\n",
    "\n",
    "### Dictionaries for data science\n",
    "For this exercise, you'll use what you've learned about the zip() function and combine two lists into a dictionary.\n",
    "\n",
    "These lists are actually extracted from a bigger dataset file of world development indicators from the World Bank. For pedagogical purposes, we have pre-processed this dataset into the lists that you'll be working with.\n",
    "\n",
    "The first list feature_names contains header names of the dataset and the second list row_vals contains actual values of a row from the dataset, corresponding to each of the header names."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "row_vals = ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']\n",
    "feature_names = ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Arab World': 'Arab World', 'ARB': 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT': 'SP.ADO.TFRT', '1960': '1960', '133.56090740552298': '133.56090740552298'}\n"
     ]
    }
   ],
   "source": [
    "# Zip lists: zipped_lists\n",
    "zipped_lists = zip(feature_names, row_vals)\n",
    "\n",
    "# Create a dictionary: rs_dict\n",
    "rs_dict = dict(zipped_lists)\n",
    "\n",
    "# Print the dictionary\n",
    "print(rs_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing a function to help you\n",
    "Suppose you needed to repeat the same process done in the previous exercise to many, many rows of data. Rewriting your code again and again could become very tedious, repetitive, and unmaintainable.\n",
    "\n",
    "In this exercise, you will create a function to house the code you wrote earlier to make things easier and much more concise. Why? This way, you only need to call the function and supply the appropriate lists to create your dictionaries!"
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
      "{'Arab World': 'Arab World', 'ARB': 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT': 'SP.ADO.TFRT', '1960': '1960', '133.56090740552298': '133.56090740552298'}\n"
     ]
    }
   ],
   "source": [
    "# Define lists2dict()\n",
    "def lists2dict(list1, list2):\n",
    "    \"\"\"Return a dictionary where list1 provides\n",
    "    the keys and list2 provides the values.\"\"\"\n",
    "\n",
    "    # Zip lists: zipped_lists\n",
    "    zipped_lists = zip(list1, list2)\n",
    "\n",
    "    # Create a dictionary: rs_dict\n",
    "    rs_dict = dict(zipped_lists)\n",
    "\n",
    "    # Return the dictionary\n",
    "    return rs_dict\n",
    "\n",
    "# Call lists2dict: rs_fxn\n",
    "rs_fxn = lists2dict(feature_names, row_vals)\n",
    "\n",
    "# Print rs_fxn\n",
    "print(rs_fxn)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Using a list comprehension\n",
    "This time, you're going to use the lists2dict() function you defined in the last exercise to turn a bunch of lists into a list of dictionaries with the help of a list comprehension.\n",
    "\n",
    "The lists2dict() function has already been preloaded, together with a couple of lists, feature_names and row_lists. feature_names contains the header names of the World Bank dataset and row_lists is a list of lists, where each sublist is a list of actual values of a row from the dataset.\n",
    "\n",
    "Your goal is to use a list comprehension to generate a list of dicts, where the keys are the header names and the values are the row entries."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "row_lists = [['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298'], ['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547'], ['Arab World', 'ARB', 'Age dependency ratio, old (% of working-age population)', 'SP.POP.DPND.OL', '1960', '6.634579191565161'], ['Arab World', 'ARB', 'Age dependency ratio, young (% of working-age population)', 'SP.POP.DPND.YG', '1960', '81.02332950839141'], ['Arab World', 'ARB', 'Arms exports (SIPRI trend indicator values)', 'MS.MIL.XPRT.KD', '1960', '3000000.0'], ['Arab World', 'ARB', 'Arms imports (SIPRI trend indicator values)', 'MS.MIL.MPRT.KD', '1960', '538000000.0'], ['Arab World', 'ARB', 'Birth rate, crude (per 1,000 people)', 'SP.DYN.CBRT.IN', '1960', '47.697888095096395'], ['Arab World', 'ARB', 'CO2 emissions (kt)', 'EN.ATM.CO2E.KT', '1960', '59563.9892169935'], ['Arab World', 'ARB', 'CO2 emissions (metric tons per capita)', 'EN.ATM.CO2E.PC', '1960', '0.6439635478877049'], ['Arab World', 'ARB', 'CO2 emissions from gaseous fuel consumption (% of total)', 'EN.ATM.CO2E.GF.ZS', '1960', '5.041291753975099'], ['Arab World', 'ARB', 'CO2 emissions from liquid fuel consumption (% of total)', 'EN.ATM.CO2E.LF.ZS', '1960', '84.8514729446567'], ['Arab World', 'ARB', 'CO2 emissions from liquid fuel consumption (kt)', 'EN.ATM.CO2E.LF.KT', '1960', '49541.707291032304'], ['Arab World', 'ARB', 'CO2 emissions from solid fuel consumption (% of total)', 'EN.ATM.CO2E.SF.ZS', '1960', '4.72698138789597'], ['Arab World', 'ARB', 'Death rate, crude (per 1,000 people)', 'SP.DYN.CDRT.IN', '1960', '19.7544519237187'], ['Arab World', 'ARB', 'Fertility rate, total (births per woman)', 'SP.DYN.TFRT.IN', '1960', '6.92402738655897'], ['Arab World', 'ARB', 'Fixed telephone subscriptions', 'IT.MLT.MAIN', '1960', '406833.0'], ['Arab World', 'ARB', 'Fixed telephone subscriptions (per 100 people)', 'IT.MLT.MAIN.P2', '1960', '0.6167005703199'], ['Arab World', 'ARB', 'Hospital beds (per 1,000 people)', 'SH.MED.BEDS.ZS', '1960', '1.9296220724398703'], ['Arab World', 'ARB', 'International migrant stock (% of population)', 'SM.POP.TOTL.ZS', '1960', '2.9906371279862403'], ['Arab World', 'ARB', 'International migrant stock, total', 'SM.POP.TOTL', '1960', '3324685.0']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']\n",
      "['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547']\n",
      "{'Arab World': 'Arab World', 'ARB': 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT': 'SP.ADO.TFRT', '1960': '1960', '133.56090740552298': '133.56090740552298'}\n",
      "{'Arab World': 'Arab World', 'ARB': 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)': 'Age dependency ratio (% of working-age population)', 'SP.ADO.TFRT': 'SP.POP.DPND', '1960': '1960', '133.56090740552298': '87.7976011532547'}\n"
     ]
    }
   ],
   "source": [
    "# Print the first two lists in row_lists\n",
    "print(row_lists[0])\n",
    "print(row_lists[1])\n",
    "\n",
    "# Turn list of lists into list of dicts: list_of_dicts\n",
    "list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]\n",
    "\n",
    "# Print the first two dictionaries in list_of_dicts\n",
    "print(list_of_dicts[0])\n",
    "print(list_of_dicts[1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Turning this all into a DataFrame\n",
    "You've zipped lists together, created a function to house your code, and even used the function in a list comprehension to generate a list of dictionaries. That was a lot of work and you did a great job!\n",
    "\n",
    "You will now use of all these to convert the list of dictionaries into a pandas DataFrame. You will see how convenient it is to generate a DataFrame from dictionaries with the `DataFrame()` function from the pandas package."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
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
       "      <th>133.56090740552298</th>\n",
       "      <th>1960</th>\n",
       "      <th>ARB</th>\n",
       "      <th>Adolescent fertility rate (births per 1,000 women ages 15-19)</th>\n",
       "      <th>Arab World</th>\n",
       "      <th>SP.ADO.TFRT</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>133.56090740552298</td>\n",
       "      <td>1960</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Adolescent fertility rate (births per 1,000 wo...</td>\n",
       "      <td>Arab World</td>\n",
       "      <td>SP.ADO.TFRT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>87.7976011532547</td>\n",
       "      <td>1960</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Age dependency ratio (% of working-age populat...</td>\n",
       "      <td>Arab World</td>\n",
       "      <td>SP.POP.DPND</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>6.634579191565161</td>\n",
       "      <td>1960</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Age dependency ratio, old (% of working-age po...</td>\n",
       "      <td>Arab World</td>\n",
       "      <td>SP.POP.DPND.OL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>81.02332950839141</td>\n",
       "      <td>1960</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Age dependency ratio, young (% of working-age ...</td>\n",
       "      <td>Arab World</td>\n",
       "      <td>SP.POP.DPND.YG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3000000.0</td>\n",
       "      <td>1960</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Arms exports (SIPRI trend indicator values)</td>\n",
       "      <td>Arab World</td>\n",
       "      <td>MS.MIL.XPRT.KD</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   133.56090740552298  1960  ARB  \\\n",
       "0  133.56090740552298  1960  ARB   \n",
       "1    87.7976011532547  1960  ARB   \n",
       "2   6.634579191565161  1960  ARB   \n",
       "3   81.02332950839141  1960  ARB   \n",
       "4           3000000.0  1960  ARB   \n",
       "\n",
       "  Adolescent fertility rate (births per 1,000 women ages 15-19)  Arab World  \\\n",
       "0  Adolescent fertility rate (births per 1,000 wo...             Arab World   \n",
       "1  Age dependency ratio (% of working-age populat...             Arab World   \n",
       "2  Age dependency ratio, old (% of working-age po...             Arab World   \n",
       "3  Age dependency ratio, young (% of working-age ...             Arab World   \n",
       "4        Arms exports (SIPRI trend indicator values)             Arab World   \n",
       "\n",
       "      SP.ADO.TFRT  \n",
       "0     SP.ADO.TFRT  \n",
       "1     SP.POP.DPND  \n",
       "2  SP.POP.DPND.OL  \n",
       "3  SP.POP.DPND.YG  \n",
       "4  MS.MIL.XPRT.KD  "
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Turn list of lists into list of dicts: list_of_dicts\n",
    "list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]\n",
    "\n",
    "# Turn list of dicts into a DataFrame: df\n",
    "df = pd.DataFrame(list_of_dicts)\n",
    "\n",
    "# Print the head of the DataFrame\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Processing data in chunks (1)\n",
    "Sometimes, data sources can be so large in size that storing the entire dataset in memory becomes too resource-intensive. In this exercise, you will process the first 1000 rows of a file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset.\n",
    "\n",
    "The csv file 'world_ind_pop_data.csv' is in your current directory for your use. To begin, you need to open a connection to this file using what is known as a context manager. For example, the command with open('datacamp.csv') as datacamp binds the csv file 'datacamp.csv' as datacamp in the context manager. Here, the with statement is the context manager, and its purpose is to ensure that resources are efficiently allocated when opening a connection to a file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Arab World': 5, 'Caribbean small states': 5, 'Central Europe and the Baltics': 5, 'East Asia & Pacific (all income levels)': 5, 'East Asia & Pacific (developing only)': 5, 'Euro area': 5, 'Europe & Central Asia (all income levels)': 5, 'Europe & Central Asia (developing only)': 5, 'European Union': 5, 'Fragile and conflict affected situations': 5, 'Heavily indebted poor countries (HIPC)': 5, 'High income': 5, 'High income: nonOECD': 5, 'High income: OECD': 5, 'Latin America & Caribbean (all income levels)': 5, 'Latin America & Caribbean (developing only)': 5, 'Least developed countries: UN classification': 5, 'Low & middle income': 5, 'Low income': 5, 'Lower middle income': 5, 'Middle East & North Africa (all income levels)': 5, 'Middle East & North Africa (developing only)': 5, 'Middle income': 5, 'North America': 5, 'OECD members': 5, 'Other small states': 5, 'Pacific island small states': 5, 'Small states': 5, 'South Asia': 5, 'Sub-Saharan Africa (all income levels)': 5, 'Sub-Saharan Africa (developing only)': 5, 'Upper middle income': 5, 'World': 4, 'Afghanistan': 4, 'Albania': 4, 'Algeria': 4, 'American Samoa': 4, 'Andorra': 4, 'Angola': 4, 'Antigua and Barbuda': 4, 'Argentina': 4, 'Armenia': 4, 'Aruba': 4, 'Australia': 4, 'Austria': 4, 'Azerbaijan': 4, '\"Bahamas': 4, 'Bahrain': 4, 'Bangladesh': 4, 'Barbados': 4, 'Belarus': 4, 'Belgium': 4, 'Belize': 4, 'Benin': 4, 'Bermuda': 4, 'Bhutan': 4, 'Bolivia': 4, 'Bosnia and Herzegovina': 4, 'Botswana': 4, 'Brazil': 4, 'Brunei Darussalam': 4, 'Bulgaria': 4, 'Burkina Faso': 4, 'Burundi': 4, 'Cabo Verde': 4, 'Cambodia': 4, 'Cameroon': 4, 'Canada': 4, 'Cayman Islands': 4, 'Central African Republic': 4, 'Chad': 4, 'Channel Islands': 4, 'Chile': 4, 'China': 4, 'Colombia': 4, 'Comoros': 4, '\"Congo': 8, 'Costa Rica': 4, \"Cote d'Ivoire\": 4, 'Croatia': 4, 'Cuba': 4, 'Curacao': 4, 'Cyprus': 4, 'Czech Republic': 4, 'Denmark': 4, 'Djibouti': 4, 'Dominica': 4, 'Dominican Republic': 4, 'Ecuador': 4, '\"Egypt': 4, 'El Salvador': 4, 'Equatorial Guinea': 4, 'Eritrea': 4, 'Estonia': 4, 'Ethiopia': 4, 'Faeroe Islands': 4, 'Fiji': 4, 'Finland': 4, 'France': 4, 'French Polynesia': 4, 'Gabon': 4, '\"Gambia': 4, 'Georgia': 4, 'Germany': 4, 'Ghana': 4, 'Greece': 4, 'Greenland': 4, 'Grenada': 4, 'Guam': 4, 'Guatemala': 4, 'Guinea': 4, 'Guinea-Bissau': 4, 'Guyana': 4, 'Haiti': 4, 'Honduras': 4, '\"Hong Kong SAR': 4, 'Hungary': 4, 'Iceland': 4, 'India': 4, 'Indonesia': 4, '\"Iran': 4, 'Iraq': 4, 'Ireland': 4, 'Isle of Man': 4, 'Israel': 4, 'Italy': 4, 'Jamaica': 4, 'Japan': 4, 'Jordan': 4, 'Kazakhstan': 4, 'Kenya': 4, 'Kiribati': 4, '\"Korea': 8, 'Kuwait': 4, 'Kyrgyz Republic': 4, 'Lao PDR': 4, 'Latvia': 4, 'Lebanon': 4, 'Lesotho': 4, 'Liberia': 4, 'Libya': 4, 'Liechtenstein': 4, 'Lithuania': 4, 'Luxembourg': 4, '\"Macao SAR': 4, '\"Macedonia': 4, 'Madagascar': 4, 'Malawi': 4, 'Malaysia': 4, 'Maldives': 4, 'Mali': 4, 'Malta': 4, 'Marshall Islands': 4, 'Mauritania': 4, 'Mauritius': 4, 'Mexico': 4, '\"Micronesia': 4, 'Moldova': 4, 'Monaco': 4, 'Mongolia': 4, 'Montenegro': 4, 'Morocco': 4, 'Mozambique': 4, 'Myanmar': 4, 'Namibia': 4, 'Nepal': 4, 'Netherlands': 4, 'New Caledonia': 4, 'New Zealand': 4, 'Nicaragua': 4, 'Niger': 4, 'Nigeria': 4, 'Northern Mariana Islands': 4, 'Norway': 4, 'Oman': 4, 'Pakistan': 4, 'Palau': 4, 'Panama': 4, 'Papua New Guinea': 4, 'Paraguay': 4, 'Peru': 4, 'Philippines': 4, 'Poland': 4, 'Portugal': 4, 'Puerto Rico': 4, 'Qatar': 4, 'Romania': 4, 'Russian Federation': 4, 'Rwanda': 4, 'Samoa': 4, 'San Marino': 4, 'Sao Tome and Principe': 4, 'Saudi Arabia': 4, 'Senegal': 4, 'Seychelles': 4, 'Sierra Leone': 4, 'Singapore': 4, 'Slovak Republic': 4, 'Slovenia': 4, 'Solomon Islands': 4, 'Somalia': 4, 'South Africa': 4, 'South Sudan': 4, 'Spain': 4, 'Sri Lanka': 4, 'St. Kitts and Nevis': 4, 'St. Lucia': 4, 'St. Vincent and the Grenadines': 4, 'Sudan': 4, 'Suriname': 4, 'Swaziland': 4, 'Sweden': 4, 'Switzerland': 4, 'Syrian Arab Republic': 4, 'Tajikistan': 4, 'Tanzania': 4, 'Thailand': 4, 'Timor-Leste': 4, 'Togo': 4, 'Tonga': 4, 'Trinidad and Tobago': 4, 'Tunisia': 4, 'Turkey': 4, 'Turkmenistan': 4, 'Turks and Caicos Islands': 4, 'Tuvalu': 4, 'Uganda': 4, 'Ukraine': 4, 'United Arab Emirates': 4, 'United Kingdom': 4, 'United States': 4, 'Uruguay': 4, 'Uzbekistan': 4, 'Vanuatu': 4, '\"Venezuela': 4, 'Vietnam': 4, 'Virgin Islands (U.S.)': 4, '\"Yemen': 4, 'Zambia': 4, 'Zimbabwe': 4}\n"
     ]
    }
   ],
   "source": [
    "# Open a connection to the file\n",
    "with open('world_ind_pop_data.csv') as file:\n",
    "\n",
    "    # Skip the column names\n",
    "    file.readline()\n",
    "\n",
    "    # Initialize an empty dictionary: counts_dict\n",
    "    counts_dict = {}\n",
    "\n",
    "    # Process only the first 1000 rows\n",
    "    for j in range(0,1000):\n",
    "\n",
    "        # Split the current line into a list: line\n",
    "        line = file.readline().split(',')\n",
    "\n",
    "        # Get the value for the first column: first_col\n",
    "        first_col = line[0]\n",
    "\n",
    "        # If the column value is in the dict, increment its value\n",
    "        if first_col in counts_dict.keys():\n",
    "            counts_dict[first_col] += 1\n",
    "\n",
    "        # Else, add to the dict and set value to 1\n",
    "        else:\n",
    "            counts_dict[first_col] = 1\n",
    "\n",
    "# Print the resulting dictionary\n",
    "print(counts_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing a generator to load data in chunks (2)\n",
    "In the previous exercise, you processed a file line by line for a given number of lines. What if, however, you want to do this for the entire file?\n",
    "\n",
    "In this case, it would be useful to use generators. Generators allow users to lazily evaluate data. This concept of lazy evaluation is useful when you have to deal with very large datasets because it lets you generate values in an efficient manner by yielding only chunks of data at a time instead of the whole thing at once.\n",
    "\n",
    "In this exercise, you will define a generator function read_large_file() that produces a generator object which yields a single line from a file each time next() is called on it. The csv file 'world_ind_pop_data.csv' is in your current directory for your use.\n",
    "\n",
    "Note that when you open a connection to a file, the resulting file object is already a generator! So out in the wild, you won't have to explicitly create generator objects in cases such as this. However, for pedagogical reasons, we are having you practice how to do this here with the read_large_file() function. Go for it!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CountryName,CountryCode,Year,Total Population,Urban population (% of total)\n",
      "\n",
      "Arab World,ARB,1960,92495902.0,31.285384211605397\n",
      "\n",
      "Caribbean small states,CSS,1960,4190810.0,31.5974898513652\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Define read_large_file()\n",
    "def read_large_file(file_object):\n",
    "    \"\"\"A generator function to read a large file lazily.\"\"\"\n",
    "\n",
    "    # Loop indefinitely until the end of the file\n",
    "    while True:\n",
    "\n",
    "        # Read a line from the file: data\n",
    "        data = file_object.readline()\n",
    "\n",
    "        # Break if this is the end of the file\n",
    "        if not data:\n",
    "            break\n",
    "\n",
    "        # Yield the line of data\n",
    "        yield data\n",
    "\n",
    "# Open a connection to the file\n",
    "with open('world_ind_pop_data.csv') as file:\n",
    "\n",
    "    # Create a generator object for the file: gen_file\n",
    "    gen_file = read_large_file(file)\n",
    "\n",
    "    # Print the first three lines of the file\n",
    "    print(next(gen_file))\n",
    "    print(next(gen_file))\n",
    "    print(next(gen_file))"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "Wonderful work! Note that since a file object is already a generator, you don't have to explicitly create a generator object with your read_large_file() function. However, it is still good to practice how to create generators - well done!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing a generator to load data in chunks (3)\n",
    "Great! You've just created a generator function that you can use to help you process large files.\n",
    "\n",
    "Now let's use your generator function to process the World Bank dataset like you did previously. You will process the file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset. For this exercise, however, you won't process just 1000 rows of data, you'll process the entire dataset!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'CountryName': 1, 'Arab World': 55, 'Caribbean small states': 55, 'Central Europe and the Baltics': 55, 'East Asia & Pacific (all income levels)': 55, 'East Asia & Pacific (developing only)': 55, 'Euro area': 55, 'Europe & Central Asia (all income levels)': 55, 'Europe & Central Asia (developing only)': 55, 'European Union': 55, 'Fragile and conflict affected situations': 55, 'Heavily indebted poor countries (HIPC)': 55, 'High income': 55, 'High income: nonOECD': 55, 'High income: OECD': 55, 'Latin America & Caribbean (all income levels)': 55, 'Latin America & Caribbean (developing only)': 55, 'Least developed countries: UN classification': 55, 'Low & middle income': 55, 'Low income': 55, 'Lower middle income': 55, 'Middle East & North Africa (all income levels)': 55, 'Middle East & North Africa (developing only)': 55, 'Middle income': 55, 'North America': 55, 'OECD members': 55, 'Other small states': 55, 'Pacific island small states': 55, 'Small states': 55, 'South Asia': 55, 'Sub-Saharan Africa (all income levels)': 55, 'Sub-Saharan Africa (developing only)': 55, 'Upper middle income': 55, 'World': 55, 'Afghanistan': 55, 'Albania': 55, 'Algeria': 55, 'American Samoa': 55, 'Andorra': 55, 'Angola': 55, 'Antigua and Barbuda': 55, 'Argentina': 55, 'Armenia': 55, 'Aruba': 55, 'Australia': 55, 'Austria': 55, 'Azerbaijan': 55, '\"Bahamas': 55, 'Bahrain': 55, 'Bangladesh': 55, 'Barbados': 55, 'Belarus': 55, 'Belgium': 55, 'Belize': 55, 'Benin': 55, 'Bermuda': 55, 'Bhutan': 55, 'Bolivia': 55, 'Bosnia and Herzegovina': 55, 'Botswana': 55, 'Brazil': 55, 'Brunei Darussalam': 55, 'Bulgaria': 55, 'Burkina Faso': 55, 'Burundi': 55, 'Cabo Verde': 55, 'Cambodia': 55, 'Cameroon': 55, 'Canada': 55, 'Cayman Islands': 55, 'Central African Republic': 55, 'Chad': 55, 'Channel Islands': 55, 'Chile': 55, 'China': 55, 'Colombia': 55, 'Comoros': 55, '\"Congo': 110, 'Costa Rica': 55, \"Cote d'Ivoire\": 55, 'Croatia': 55, 'Cuba': 55, 'Curacao': 55, 'Cyprus': 55, 'Czech Republic': 55, 'Denmark': 55, 'Djibouti': 55, 'Dominica': 55, 'Dominican Republic': 55, 'Ecuador': 55, '\"Egypt': 55, 'El Salvador': 55, 'Equatorial Guinea': 55, 'Eritrea': 55, 'Estonia': 55, 'Ethiopia': 55, 'Faeroe Islands': 55, 'Fiji': 55, 'Finland': 55, 'France': 55, 'French Polynesia': 55, 'Gabon': 55, '\"Gambia': 55, 'Georgia': 55, 'Germany': 55, 'Ghana': 55, 'Greece': 55, 'Greenland': 55, 'Grenada': 55, 'Guam': 55, 'Guatemala': 55, 'Guinea': 55, 'Guinea-Bissau': 55, 'Guyana': 55, 'Haiti': 55, 'Honduras': 55, '\"Hong Kong SAR': 55, 'Hungary': 55, 'Iceland': 55, 'India': 55, 'Indonesia': 55, '\"Iran': 55, 'Iraq': 55, 'Ireland': 55, 'Isle of Man': 55, 'Israel': 55, 'Italy': 55, 'Jamaica': 55, 'Japan': 55, 'Jordan': 55, 'Kazakhstan': 55, 'Kenya': 55, 'Kiribati': 55, '\"Korea': 110, 'Kuwait': 52, 'Kyrgyz Republic': 55, 'Lao PDR': 55, 'Latvia': 55, 'Lebanon': 55, 'Lesotho': 55, 'Liberia': 55, 'Libya': 55, 'Liechtenstein': 55, 'Lithuania': 55, 'Luxembourg': 55, '\"Macao SAR': 55, '\"Macedonia': 55, 'Madagascar': 55, 'Malawi': 55, 'Malaysia': 55, 'Maldives': 55, 'Mali': 55, 'Malta': 55, 'Marshall Islands': 55, 'Mauritania': 55, 'Mauritius': 55, 'Mexico': 55, '\"Micronesia': 55, 'Moldova': 55, 'Monaco': 55, 'Mongolia': 55, 'Montenegro': 55, 'Morocco': 55, 'Mozambique': 55, 'Myanmar': 55, 'Namibia': 55, 'Nepal': 55, 'Netherlands': 55, 'New Caledonia': 55, 'New Zealand': 55, 'Nicaragua': 55, 'Niger': 55, 'Nigeria': 55, 'Northern Mariana Islands': 55, 'Norway': 55, 'Oman': 55, 'Pakistan': 55, 'Palau': 55, 'Panama': 55, 'Papua New Guinea': 55, 'Paraguay': 55, 'Peru': 55, 'Philippines': 55, 'Poland': 55, 'Portugal': 55, 'Puerto Rico': 55, 'Qatar': 55, 'Romania': 55, 'Russian Federation': 55, 'Rwanda': 55, 'Samoa': 55, 'San Marino': 55, 'Sao Tome and Principe': 55, 'Saudi Arabia': 55, 'Senegal': 55, 'Seychelles': 55, 'Sierra Leone': 55, 'Singapore': 55, 'Slovak Republic': 55, 'Slovenia': 55, 'Solomon Islands': 55, 'Somalia': 55, 'South Africa': 55, 'South Sudan': 55, 'Spain': 55, 'Sri Lanka': 55, 'St. Kitts and Nevis': 55, 'St. Lucia': 55, 'St. Vincent and the Grenadines': 55, 'Sudan': 55, 'Suriname': 55, 'Swaziland': 55, 'Sweden': 55, 'Switzerland': 55, 'Syrian Arab Republic': 55, 'Tajikistan': 55, 'Tanzania': 55, 'Thailand': 55, 'Timor-Leste': 55, 'Togo': 55, 'Tonga': 55, 'Trinidad and Tobago': 55, 'Tunisia': 55, 'Turkey': 55, 'Turkmenistan': 55, 'Turks and Caicos Islands': 55, 'Tuvalu': 55, 'Uganda': 55, 'Ukraine': 55, 'United Arab Emirates': 55, 'United Kingdom': 55, 'United States': 55, 'Uruguay': 55, 'Uzbekistan': 55, 'Vanuatu': 55, '\"Venezuela': 55, 'Vietnam': 55, 'Virgin Islands (U.S.)': 55, '\"Yemen': 55, 'Zambia': 55, 'Zimbabwe': 55, 'Serbia': 25, 'West Bank and Gaza': 25, 'Sint Maarten (Dutch part)': 17}\n"
     ]
    }
   ],
   "source": [
    "# Initialize an empty dictionary: counts_dict\n",
    "counts_dict = {}\n",
    "\n",
    "# Open a connection to the file\n",
    "with open('world_ind_pop_data.csv') as file:\n",
    "\n",
    "    # Iterate over the generator from read_large_file()\n",
    "    for line in read_large_file(file):\n",
    "\n",
    "        row = line.split(',')\n",
    "        first_col = row[0]\n",
    "\n",
    "        if first_col in counts_dict.keys():\n",
    "            counts_dict[first_col] += 1\n",
    "        else:\n",
    "            counts_dict[first_col] = 1\n",
    "\n",
    "# Print            \n",
    "print(counts_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing an iterator to load data in chunks (1)\n",
    "Another way to read data too large to store in memory in chunks is to read the file in as DataFrames of a certain length, say, 100. For example, with the pandas package (imported as pd), you can do pd.read_csv(filename, chunksize=100). This creates an iterable reader object, which means that you can use next() on it.\n",
    "\n",
    "In this exercise, you will read a file in small DataFrame chunks with read_csv(). You're going to use the World Bank Indicators data 'ind_pop.csv', available in your current directory, to look at the urban population indicator for numerous countries and years."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                 CountryName CountryCode  Year  \\\n",
      "0                                 Arab World         ARB  1960   \n",
      "1                     Caribbean small states         CSS  1960   \n",
      "2             Central Europe and the Baltics         CEB  1960   \n",
      "3    East Asia & Pacific (all income levels)         EAS  1960   \n",
      "4      East Asia & Pacific (developing only)         EAP  1960   \n",
      "5                                  Euro area         EMU  1960   \n",
      "6  Europe & Central Asia (all income levels)         ECS  1960   \n",
      "7    Europe & Central Asia (developing only)         ECA  1960   \n",
      "8                             European Union         EUU  1960   \n",
      "9   Fragile and conflict affected situations         FCS  1960   \n",
      "\n",
      "   Total Population  Urban population (% of total)  \n",
      "0      9.249590e+07                      31.285384  \n",
      "1      4.190810e+06                      31.597490  \n",
      "2      9.140158e+07                      44.507921  \n",
      "3      1.042475e+09                      22.471132  \n",
      "4      8.964930e+08                      16.917679  \n",
      "5      2.653965e+08                      62.096947  \n",
      "6      6.674890e+08                      55.378977  \n",
      "7      1.553174e+08                      38.066129  \n",
      "8      4.094985e+08                      61.212898  \n",
      "9      1.203546e+08                      17.891972  \n",
      "                                      CountryName CountryCode  Year  \\\n",
      "10         Heavily indebted poor countries (HIPC)         HPC  1960   \n",
      "11                                    High income         HIC  1960   \n",
      "12                           High income: nonOECD         NOC  1960   \n",
      "13                              High income: OECD         OEC  1960   \n",
      "14  Latin America & Caribbean (all income levels)         LCN  1960   \n",
      "15    Latin America & Caribbean (developing only)         LAC  1960   \n",
      "16   Least developed countries: UN classification         LDC  1960   \n",
      "17                            Low & middle income         LMY  1960   \n",
      "18                                     Low income         LIC  1960   \n",
      "19                            Lower middle income         LMC  1960   \n",
      "\n",
      "    Total Population  Urban population (% of total)  \n",
      "10      1.624912e+08                      12.236046  \n",
      "11      9.075975e+08                      62.680332  \n",
      "12      1.866767e+08                      56.107863  \n",
      "13      7.209208e+08                      64.285435  \n",
      "14      2.205642e+08                      49.284688  \n",
      "15      1.776822e+08                      44.863308  \n",
      "16      2.410728e+08                       9.616261  \n",
      "17      2.127373e+09                      21.272894  \n",
      "18      1.571884e+08                      11.498396  \n",
      "19      9.429116e+08                      19.810513  \n"
     ]
    }
   ],
   "source": [
    "# Initialize reader object: df_reader\n",
    "df_reader = pd.read_csv('world_ind_pop_data.csv', chunksize = 10)\n",
    "\n",
    "# Print two chunks\n",
    "print(next(df_reader))\n",
    "print(next(df_reader))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing an iterator to load data in chunks (2)\n",
    "In the previous exercise, you used read_csv() to read in DataFrame chunks from a large dataset. In this exercise, you will read in a file using a bigger DataFrame chunk size and then process the data from the first chunk.\n",
    "\n",
    "To process the data, you will create another DataFrame composed of only the rows from a specific country. You will then zip together two of the columns from the new DataFrame, 'Total Population' and 'Urban population (% of total)'. Finally, you will create a list of tuples from the zip object, where each tuple is composed of a value from each of the two columns mentioned."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               CountryName CountryCode  Year  \\\n",
      "0                               Arab World         ARB  1960   \n",
      "1                   Caribbean small states         CSS  1960   \n",
      "2           Central Europe and the Baltics         CEB  1960   \n",
      "3  East Asia & Pacific (all income levels)         EAS  1960   \n",
      "4    East Asia & Pacific (developing only)         EAP  1960   \n",
      "\n",
      "   Total Population  Urban population (% of total)  \n",
      "0      9.249590e+07                      31.285384  \n",
      "1      4.190810e+06                      31.597490  \n",
      "2      9.140158e+07                      44.507921  \n",
      "3      1.042475e+09                      22.471132  \n",
      "4      8.964930e+08                      16.917679  \n",
      "[(91401583.0, 44.5079211390026), (92237118.0, 45.206665319194), (93014890.0, 45.866564696018), (93845749.0, 46.5340927663649), (94722599.0, 47.2087429803526)]\n"
     ]
    }
   ],
   "source": [
    "# Initialize reader object: urb_pop_reader\n",
    "urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=1000)\n",
    "\n",
    "# Get the first DataFrame chunk: df_urb_pop\n",
    "df_urb_pop = next(urb_pop_reader)\n",
    "\n",
    "# Check out the head of the DataFrame\n",
    "print(df_urb_pop.head())\n",
    "\n",
    "# Check out specific country: df_pop_ceb\n",
    "df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']\n",
    "\n",
    "# Zip DataFrame columns of interest: pops\n",
    "pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])\n",
    "\n",
    "# Turn zip object into list: pops_list\n",
    "pops_list = list(pops)\n",
    "\n",
    "# Print pops_list\n",
    "print(pops_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing an iterator to load data in chunks (3)\n",
    "You're getting used to reading and processing data in chunks by now. Let's push your skills a little further by adding a column to a DataFrame.\n",
    "\n",
    "Starting from the code of the previous exercise, you will be using a list comprehension to create the values for a new column 'Total Urban Population' from the list of tuples that you generated earlier. Recall from the previous exercise that the first and second elements of each tuple consist of, respectively, values from the columns 'Total Population' and 'Urban population (% of total)'. The values in this new column 'Total Urban Population', therefore, are the product of the first and second element in each tuple. Furthermore, because the 2nd element is a percentage, you need to divide the entire result by 100, or alternatively, multiply it by 0.01.\n",
    "\n",
    "You will also plot the data from this new column to create a visualization of the urban population data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
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
    "# Code from previous exercise\n",
    "urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=1000)\n",
    "df_urb_pop = next(urb_pop_reader)\n",
    "df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']\n",
    "pops = zip(df_pop_ceb['Total Population'], \n",
    "           df_pop_ceb['Urban population (% of total)'])\n",
    "pops_list = list(pops)\n",
    "\n",
    "# Use list comprehension to create new DataFrame column 'Total Urban Population'\n",
    "df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]\n",
    "\n",
    "# Plot urban population data\n",
    "df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing an iterator to load data in chunks (4)\n",
    "In the previous exercises, you've only processed the data from the first DataFrame chunk. This time, you will aggregate the results over all the DataFrame chunks in the dataset. This basically means you will be processing the entire dataset now. This is neat because you're going to be able to process the entire large dataset by just working on smaller pieces of it!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
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
    "# Initialize reader object: urb_pop_reader\n",
    "urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=1000)\n",
    "\n",
    "# Initialize empty DataFrame: data\n",
    "data = pd.DataFrame()\n",
    "\n",
    "# Iterate over each DataFrame chunk\n",
    "for df_urb_pop in urb_pop_reader:\n",
    "\n",
    "    # Check out specific country: df_pop_ceb\n",
    "    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']\n",
    "\n",
    "    # Zip DataFrame columns of interest: pops\n",
    "    pops = zip(df_pop_ceb['Total Population'],\n",
    "                df_pop_ceb['Urban population (% of total)'])\n",
    "\n",
    "    # Turn zip object into list: pops_list\n",
    "    pops_list = list(pops)\n",
    "\n",
    "    # Use list comprehension to create new DataFrame column 'Total Urban Population'\n",
    "    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]\n",
    "    \n",
    "    # Append DataFrame chunk to data: data\n",
    "    data = data.append(df_pop_ceb)\n",
    "\n",
    "# Plot urban population data\n",
    "data.plot(kind='scatter', x='Year', y='Total Urban Population')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Writing an iterator to load data in chunks (5)\n",
    "This is the last leg. You've learned a lot about processing a large dataset in chunks. In this last exercise, you will put all the code for processing the data into a single function so that you can reuse the code without having to rewrite the same things all over again.\n",
    "\n",
    "You're going to define the function plot_pop() which takes two arguments: the filename of the file to be processed, and the country code of the rows you want to process in the dataset.\n",
    "\n",
    "Because all of the previous code you've written in the previous exercises will be housed in plot_pop(), calling the function already does the following:\n",
    "\n",
    "- Loading of the file chunk by chunk,\n",
    "- Creating the new column of urban population values, and\n",
    "- Plotting the urban population data.  \n",
    "\n",
    "That's a lot of work, but the function now makes it convenient to repeat the same process for whatever file and country code you want to process and visualize!.\n",
    "\n",
    "After you are done, take a moment to look at the plots and reflect on the new skills you have acquired. The journey doesn't end here! If you have enjoyed working with this data, you can continue exploring it using the pre-processed version available on [Kaggle](https://www.kaggle.com/worldbank/world-development-indicators)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
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
    },
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
    "# Define plot_pop()\n",
    "def plot_pop(filename, country_code):\n",
    "\n",
    "    # Initialize reader object: urb_pop_reader\n",
    "    urb_pop_reader = pd.read_csv(filename, chunksize=1000)\n",
    "\n",
    "    # Initialize empty DataFrame: data\n",
    "    data = pd.DataFrame()\n",
    "    \n",
    "    # Iterate over each DataFrame chunk\n",
    "    for df_urb_pop in urb_pop_reader:\n",
    "        # Check out specific country: df_pop_ceb\n",
    "        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]\n",
    "\n",
    "        # Zip DataFrame columns of interest: pops\n",
    "        pops = zip(df_pop_ceb['Total Population'],\n",
    "                    df_pop_ceb['Urban population (% of total)'])\n",
    "\n",
    "        # Turn zip object into list: pops_list\n",
    "        pops_list = list(pops)\n",
    "\n",
    "        # Use list comprehension to create new DataFrame column 'Total Urban Population'\n",
    "        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]\n",
    "    \n",
    "        # Append DataFrame chunk to data: data\n",
    "        data = data.append(df_pop_ceb)\n",
    "\n",
    "    # Plot urban population data\n",
    "    data.plot(kind='scatter', x='Year', y='Total Urban Population')\n",
    "    plt.show()\n",
    "\n",
    "# Set the filename: fn\n",
    "fn = 'world_ind_pop_data.csv'\n",
    "\n",
    "# Call plot_pop for country code 'CEB'\n",
    "plot_pop(fn, 'CEB')\n",
    "\n",
    "# Call plot_pop for country code 'ARB'\n",
    "plot_pop(fn, 'ARB')"
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
