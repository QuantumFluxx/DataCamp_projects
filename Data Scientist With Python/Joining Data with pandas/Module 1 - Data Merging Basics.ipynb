{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "03ec4b67",
   "metadata": {},
   "source": [
    "# Data Merging Basics\n",
    "\n",
    "## What column to merge on?\n",
    "Chicago provides a list of taxicab owners and vehicles licensed to operate within the city, for public safety. Your goal is to merge two tables together. One table is called `taxi_owners`, with info about the taxi cab company owners, and one is called `taxi_veh`, with info about each taxi cab vehicle. Both the `taxi_owners` and `taxi_veh` tables have been loaded for you and you can explore them in the IPython shell.\n",
    "\n",
    "Choose the column you would use to merge the two tables on using the `.merge()` method.\n",
    "\n",
    "\n",
    "* on='rid'\n",
    "\n",
    "* **on='vid'**\n",
    "\n",
    "* on='year'\n",
    "\n",
    "* on='zip'\n",
    "\n",
    "\n",
    "Yes, great job! Both DataFrames contained the column vid. Now continue on to the next exercise where you will using this information to merge the tables.\n",
    "\n",
    "## Your first inner join\n",
    "You have been tasked with figuring out what the most popular types of fuel used in Chicago taxis are. To complete the analysis, you need to merge the `taxi_owners` and `taxi_veh` tables together on the vid column. You can then use the merged table along with the `.value_counts()` method to find the most common `fuel_type`.\n",
    "\n",
    "Since you'll be working with pandas throughout the course, the package will be preloaded for you as pd in each exercise in this course. Also the taxi_owners and `taxi_veh` DataFrames are loaded for you.\n",
    "\n",
    "Merge `taxi_owners` with `taxi_veh` on the column vid, and save the result to `taxi_own_veh`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ad90046b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "taxi_owners = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/taxi_owners.p')\n",
    "\n",
    "taxi_veh = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/taxi_vehicles.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "01d6215b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['rid', 'vid', 'owner_x', 'address', 'zip', 'make', 'model', 'year',\n",
      "       'fuel_type', 'owner_y'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Merge the taxi_owners and taxi_veh tables\n",
    "taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', how='left')\n",
    "\n",
    "# Print the column names of the taxi_own_veh\n",
    "print(taxi_own_veh.columns)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba103f50",
   "metadata": {},
   "source": [
    "* Set the left and right table suffixes for overlapping columns of the merge to `_own` and `_veh`, respectively."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c8aa92a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['rid', 'vid', 'owner_own', 'address', 'zip', 'make', 'model', 'year',\n",
      "       'fuel_type', 'owner_veh'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Merge the taxi_owners and taxi_veh tables setting a suffix\n",
    "taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))\n",
    "\n",
    "# Print the column names of taxi_own_veh\n",
    "print(taxi_own_veh.columns)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "933b7a2c",
   "metadata": {},
   "source": [
    "* Select the `fuel_type` column from `taxi_own_veh` and print the `value_counts()` to find the most popular `fuel_types` used."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5cbedda6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HYBRID                    2792\n",
      "GASOLINE                   611\n",
      "FLEX FUEL                   89\n",
      "COMPRESSED NATURAL GAS      27\n",
      "Name: fuel_type, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Print the value_counts to find the most popular fuel_type\n",
    "print(taxi_own_veh['fuel_type'].value_counts())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58ad29ce",
   "metadata": {},
   "source": [
    "Bravo! You correctly merged the two tables together and found out that the most common fuel type for taxis in Chicago are hybrids.\n",
    "\n",
    "## Inner joins and number of rows returned\n",
    "All of the merges you have studied to this point are called inner joins. It is necessary to understand that inner joins only return the rows with matching values in both tables. You will explore this further by reviewing the merge between the wards and census tables, then comparing it to merges of copies of these tables that are slightly altered, named `wards_altered`, and `census_altered`. The first row of the wards column has been changed in the altered tables. You will examine how this affects the merge between them. The tables have been loaded for you.\n",
    "\n",
    "For this exercise, it is important to know that the `wards` and `census` tables start with 50 rows.\n",
    "\n",
    "* Merge wards and census on the ward column and save result to `wards_census`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "aac4d48f",
   "metadata": {},
   "outputs": [],
   "source": [
    "wards = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/ward.p')\n",
    "census = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/census.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "860f5877",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "wards_census table shape: (50, 9)\n"
     ]
    }
   ],
   "source": [
    "# Merge the wards and census tables on the ward column\n",
    "wards_census = wards.merge(census, on='ward', how='inner')\n",
    "\n",
    "# Print the shape of wards_census\n",
    "print('wards_census table shape:', wards_census.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64abdea4",
   "metadata": {},
   "source": [
    "* Merge the `wards_altered` and `census` tables on the ward column, and notice the difference in returned rows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "599e94bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  ward\n",
      "0    1\n",
      "1    2\n",
      "2    3\n",
      "3    4\n",
      "4    5\n",
      "wards_altered_census table shape: (50, 9)\n"
     ]
    }
   ],
   "source": [
    "# Print the first few rows of the wards_altered table to view the change \n",
    "print(wards_altered[['ward']].head())\n",
    "\n",
    "# Merge the wards_altered and census tables on the ward column\n",
    "wards_altered_census = wards_altered.merge(census, on='ward')\n",
    "\n",
    "# Print the shape of wards_altered_census\n",
    "print('wards_altered_census table shape:', wards_altered_census.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6dce098b",
   "metadata": {},
   "source": [
    "* Merge the `wards` and `census_altered` tables on the ward column, and notice the difference in returned rows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "504c3261",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  ward\n",
      "0    1\n",
      "1    2\n",
      "2    3\n",
      "3    4\n",
      "4    5\n",
      "wards_census_altered table shape: (50, 9)\n"
     ]
    }
   ],
   "source": [
    "# Print the first few rows of the census_altered table to view the change \n",
    "print(census_altered[['ward']].head())\n",
    "\n",
    "# Merge the wards and census_altered tables on the ward column\n",
    "wards_census_altered = wards.merge(census_altered, on='ward')\n",
    "\n",
    "# Print the shape of wards_census_altered\n",
    "print('wards_census_altered table shape:', wards_census_altered.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b57e865d",
   "metadata": {},
   "source": [
    "Great job! In step 1, the .merge() returned a table with the same number of rows as the original wards table. However, in steps 2 and 3, using the altered tables with the altered first row of the ward column, the number of returned rows was fewer. There was not a matching value in the ward column of the other table. Remember that .merge() only returns rows where the values match in both tables.\n",
    "\n",
    "## One-to-many merge\n",
    "A business may have one or multiple owners. In this exercise, you will continue to gain experience with one-to-many merges by merging a table of business owners, called `biz_owners`, to the `licenses` table. Recall from the video lesson, with a one-to-many relationship, a row in the left table may be repeated if it is related to multiple rows in the right table. In this lesson, you will explore this further by finding out what is the most common business owner title. (i.e., secretary, CEO, or vice president)\n",
    "\n",
    "The `licenses` and `biz_owners` DataFrames are loaded for you.\n",
    "\n",
    "* Starting with the licenses table on the left, merge it to the `biz_owners` table on the column account, and save the results to a variable named `licenses_owners`.\n",
    "* Group licenses_owners by title and count the number of accounts for each title. Save the result as `counted_df`\n",
    "* Sort `counted_df` by the number of accounts in descending order, and save this as a variable named `sorted_df`.\n",
    "* Use the `.head()` method to print the first few rows of the `sorted_df`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f1aa481d",
   "metadata": {},
   "outputs": [],
   "source": [
    "biz_owners = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/business_owners.p')\n",
    "licenses = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/licenses.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "21f32b68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                 account\n",
      "title                   \n",
      "PRESIDENT           6259\n",
      "SECRETARY           5205\n",
      "SOLE PROPRIETOR     1658\n",
      "OTHER               1200\n",
      "VICE PRESIDENT       970\n"
     ]
    }
   ],
   "source": [
    "# Merge the licenses and biz_owners table on account\n",
    "licenses_owners = licenses.merge(biz_owners, on='account')\n",
    "\n",
    "# Group the results by title then count the number of accounts\n",
    "counted_df = licenses_owners.groupby('title').agg({'account':'count'})\n",
    "\n",
    "# Sort the counted_df in desending order\n",
    "sorted_df = counted_df.sort_values(by='account', ascending=False)\n",
    "\n",
    "# Use .head() method to print the first few rows of sorted_df\n",
    "print(sorted_df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4240e90b",
   "metadata": {},
   "source": [
    "Wonderful! After merging the tables together, you counted the number of repeated rows with the combination of .groupby() and .agg() statements. You see that president, followed by secretary, are the most common business owner titles.\n",
    "\n",
    "## Total riders in a month\n",
    "Your goal is to find the total number of rides provided to passengers passing through the Wilson station (station_name == 'Wilson') when riding Chicago's public transportation system on weekdays (day_type == 'Weekday') in July (month == 7). Luckily, Chicago provides this detailed data, but it is in three different tables. You will work on merging these tables together to answer the question. This data is different from the business related data you have seen so far, but all the information you need to answer the question is provided.\n",
    "\n",
    "The `cal`, `ridership`, and `stations` DataFrames have been loaded for you. The relationship between the tables can be seen in the diagram below.\n",
    "![](https://assets.datacamp.com/production/repositories/5486/datasets/56b5ecb2edcdc896c69effdf05ef65e5454ff996/cta_L_diagram.png)\n",
    "\n",
    "* Merge the ridership and cal tables together, starting with the ridership table on the left and save the result to the variable `ridership_cal`. If you code takes too long to run, your merge conditions might be incorrect."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a77d0408",
   "metadata": {},
   "outputs": [],
   "source": [
    "stations = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/stations.p')\n",
    "ridership = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/cta_ridership.p')\n",
    "cal = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/cta_calendar.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8d2f6331",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge the ridership and cal tables\n",
    "ridership_cal = ridership.merge(cal, on=['year','month','day'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2133f6a3",
   "metadata": {},
   "source": [
    "* Extend the previous merge to three tables by also merging the stations table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "88490406",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge the ridership, cal, and stations tables\n",
    "ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \\\n",
    "                                  .merge(stations, on='station_id')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80ef9452",
   "metadata": {},
   "source": [
    "* Create a variable called `filter_criteria` to select the appropriate rows from the merged table so that you can sum the rides column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "561301f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "140005\n"
     ]
    }
   ],
   "source": [
    "# Merge the ridership, cal, and stations tables\n",
    "ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \\\n",
    "                                  .merge(stations, on='station_id')\n",
    "\n",
    "# Create a filter to filter ridership_cal_stations\n",
    "filter_criteria = ((ridership_cal_stations['month'] == 7) \n",
    "                   & (ridership_cal_stations['day_type'] == 'Weekday') \n",
    "                   & (ridership_cal_stations['station_name'] == 'Wilson'))\n",
    "\n",
    "# Use .loc and the filter to select for rides\n",
    "print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6625749",
   "metadata": {},
   "source": [
    "Awesome work! You merged three DataFrames together, including merging two tables on multiple columns. Once the tables were merged, you filtered and selected just like any other DataFrame. Finally, you found out that the Wilson station had 140,005 riders during weekdays in July.\n",
    "\n",
    "## Three table merge\n",
    "To solidify the concept of a three DataFrame merge, practice another exercise. A reasonable extension of our review of Chicago business data would include looking at demographics information about the neighborhoods where the businesses are. A table with the median income by zip code has been provided to you. You will merge the licenses and wards tables with this new income-by-zip-code table called `zip_demo`.\n",
    "\n",
    "* Starting with the licenses table, merge to it the `zip_demo` table on the zip column. Then merge the resulting table to the wards table on the ward column. Save result of the three merged tables to a variable named `licenses_zip_ward`.\n",
    "* Group the results of the three merged tables by the column alderman and find the median income."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "f4c5361a",
   "metadata": {},
   "outputs": [],
   "source": [
    "zip_demo = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/zip_demo.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "2a360035",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                             income\n",
      "alderman                           \n",
      "Ameya Pawar                 66246.0\n",
      "Anthony A. Beale            38206.0\n",
      "Anthony V. Napolitano       82226.0\n",
      "Ariel E. Reyboras           41307.0\n",
      "Brendan Reilly             110215.0\n",
      "Brian Hopkins               87143.0\n",
      "Carlos Ramirez-Rosa         66246.0\n",
      "Carrie M. Austin            38206.0\n",
      "Chris Taliaferro            55566.0\n",
      "Daniel \"Danny\" Solis        41226.0\n",
      "David H. Moore              33304.0\n",
      "Deborah Mell                66246.0\n",
      "Debra L. Silverstein        50554.0\n",
      "Derrick G. Curtis           65770.0\n",
      "Edward M. Burke             42335.0\n",
      "Emma M. Mitts               36283.0\n",
      "George Cardenas             33959.0\n",
      "Gilbert Villegas            41307.0\n",
      "Gregory I. Mitchell         24941.0\n",
      "Harry Osterman              45442.0\n",
      "Howard B. Brookins, Jr.     33304.0\n",
      "James Cappleman             79565.0\n",
      "Jason C. Ervin              41226.0\n",
      "Joe Moore                   39163.0\n",
      "John S. Arena               70122.0\n",
      "Leslie A. Hairston          28024.0\n",
      "Margaret Laurino            70122.0\n",
      "Marty Quinn                 67045.0\n",
      "Matthew J. O'Shea           59488.0\n",
      "Michael R. Zalewski         42335.0\n",
      "Michael Scott, Jr.          31445.0\n",
      "Michelle A. Harris          32558.0\n",
      "Michelle Smith             100116.0\n",
      "Milagros \"Milly\" Santiago   41307.0\n",
      "Nicholas Sposato            62223.0\n",
      "Pat Dowell                  46340.0\n",
      "Patrick Daley Thompson      41226.0\n",
      "Patrick J. O'Connor         50554.0\n",
      "Proco \"Joe\" Moreno          87143.0\n",
      "Raymond A. Lopez            33959.0\n",
      "Ricardo Munoz               31445.0\n",
      "Roberto Maldonado           68223.0\n",
      "Roderick T. Sawyer          32558.0\n",
      "Scott Waguespack            68223.0\n",
      "Susan Sadlowski Garza       38417.0\n",
      "Tom Tunney                  88708.0\n",
      "Toni L. Foulkes             27573.0\n",
      "Walter Burnett, Jr.         87143.0\n",
      "William D. Burns           107811.0\n",
      "Willie B. Cochran           28024.0\n"
     ]
    }
   ],
   "source": [
    "# Merge licenses and zip_demo, on zip; and merge the wards on ward\n",
    "licenses_zip_ward = licenses.merge(zip_demo, on='zip') \\\n",
    "                            .merge(wards, on='ward')\n",
    "\n",
    "# Print the results by alderman and show median income\n",
    "print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8add4a64",
   "metadata": {},
   "source": [
    "Nice work! You successfully merged three tables together. With the merged data, you can complete your income analysis. You see that only a few aldermen represent businesses in areas where the median income is greater than $62,000, which is the median income for the state of Illinois.\n",
    "\n",
    "## One-to-many merge with multiple tables\n",
    "In this exercise, assume that you are looking to start a business in the city of Chicago. Your perfect idea is to start a company that uses goats to mow the lawn for other businesses. However, you have to choose a location in the city to put your goat farm. You need a location with a great deal of space and relatively few businesses and people around to avoid complaints about the smell. You will need to merge three tables to help you choose your location. The land_use table has info on the percentage of vacant land by city ward. The census table has population by ward, and the licenses table lists businesses by ward.\n",
    "\n",
    "* Merge land_use and census on the ward column. Merge the result of this with licenses on the ward column, using the suffix `_cen` for the left table and `_lic` for the right table. Save this to the variable `land_cen_lic`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "676be56a",
   "metadata": {},
   "outputs": [],
   "source": [
    "land_use = pd.read_pickle('C:/Users/Александр/pj/DataCamp_projects/Data Scientist With Python/Joining Data with pandas/datasets/land_use.p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "b96942a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge land_use and census and merge result with licenses including suffixes\n",
    "land_cen_lic = land_use.merge(census, on='ward') \\\n",
    "                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64630bfa",
   "metadata": {},
   "source": [
    "* Group land_cen_lic by ward,` pop_2010` (the population in 2010), and vacant, then count the number of accounts. Save the results to `pop_vac_lic`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f41b07e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Group by ward, pop_2010, and vacant, then count the # of accounts\n",
    "pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], \n",
    "                                   as_index=False).agg({'account':'count'})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea2b2dad",
   "metadata": {},
   "source": [
    "* Sort `pop_vac_lic` by vacant, account, `andpop_2010` in descending, ascending, and ascending order respectively. Save it as `sorted_pop_vac_lic`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "6910c60b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   ward  pop_2010  vacant  account\n",
      "47    7     51581      19       80\n",
      "12   20     52372      15      123\n",
      "1    10     51535      14      130\n",
      "16   24     54909      13       98\n",
      "7    16     51954      13      156\n"
     ]
    }
   ],
   "source": [
    "# Sort pop_vac_lic and print the results\n",
    "sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'], \n",
    "                                             ascending=[False, True, True])\n",
    "\n",
    "# Print the top few rows of sorted_pop_vac_lic\n",
    "print(sorted_pop_vac_lic.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ee37b33",
   "metadata": {},
   "source": [
    "Great job putting your new skills into action. You merged multiple tables with varying relationships and added suffixes to make your column names clearer. Using your skills, you were able to pull together information from different tables to see that the 7th ward would be a good place to build your goat farm!"
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
