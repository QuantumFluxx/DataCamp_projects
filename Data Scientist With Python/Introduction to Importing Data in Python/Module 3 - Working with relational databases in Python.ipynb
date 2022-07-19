{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "68717bd2",
   "metadata": {},
   "source": [
    "# Working with relational databases in Python\n",
    "\n",
    "## Pop quiz: The relational model\n",
    "Which of the following is not part of the relational model?\n",
    "\n",
    "* Each row or record in a table represents an instance of an entity type.\n",
    "\n",
    "* Each column in a table represents an attribute or feature of an instance.\n",
    "\n",
    "* Every table contains a primary key column, which has a unique entry for each row.\n",
    "\n",
    "* **A database consists of at least 3 tables.**\n",
    "\n",
    "* There are relations between tables.\n",
    "\n",
    "Correct!\n",
    "\n",
    "## Creating a database engine\n",
    "Here, you're going to fire up your very first SQL engine. You'll create an engine to connect to the SQLite database 'Chinook.sqlite', which is in your working directory. Remember that to create an engine to connect to 'Northwind.sqlite', Hugo executed the command\n",
    "```sql\n",
    "engine = create_engine('sqlite:///Northwind.sqlite')\n",
    "```\n",
    "Here, 'sqlite:///Northwind.sqlite' is called the connection string to the SQLite database Northwind.sqlite. A little bit of background on the Chinook database: the Chinook database contains information about a semi-fictional digital media store in which media data is real and customer, employee and sales data has been manually created.\n",
    "\n",
    "Why the name Chinook, you ask? According to their website,\n",
    "\n",
    "The name of this sample database was based on the Northwind database. Chinooks are winds in the interior West of North America, where the Canadian Prairies and Great Plains meet various mountain ranges. Chinooks are most prevalent over southern Alberta in Canada. Chinook is a good name choice for a database that intends to be an alternative to Northwind.\n",
    "\n",
    "* Import the function create_engine from the module `sqlalchemy`.\n",
    "* Create an engine to connect to the SQLite database `'Chinook.sqlite'` and assign it to engine."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "08f0c499",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import necessary module\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "# Create engine: engine\n",
    "engine = create_engine('sqlite:///Chinook.sqlite')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "771f3a05",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## What are the tables in the database?\n",
    "In this exercise, you'll once again create an engine to connect to `'Chinook.sqlite'`. Before you can get any data out of the database, however, you'll need to know what tables it contains!\n",
    "\n",
    "To this end, you'll save the table names to a list using the method `table_names()` on the engine and then you will print the list.\n",
    "\n",
    "* Import the function `create_engine` from the module `sqlalchemy`.\n",
    "* Create an engine to connect to the SQLite database `'Chinook.sqlite'` and assign it to engine.\n",
    "* Using the method `table_names()` on the engine engine, assign the table names of `'Chinook.sqlite'` to the variable `table_names`.\n",
    "* Print the object `table_names` to the shell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6c538507",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "# Import necessary module\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "# Create engine: engine\n",
    "engine = create_engine('sqlite:///Chinook.sqlite')\n",
    "\n",
    "# Save the table names to a list: table_names\n",
    "table_names = engine.table_names()\n",
    "\n",
    "# Print the table names to the shell\n",
    "print(table_names)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37bdcabd",
   "metadata": {},
   "source": [
    "Great job!\n",
    "\n",
    "## The Hello World of SQL Queries!\n",
    "Now, it's time for liftoff! In this exercise, you'll perform the Hello World of SQL queries, SELECT, in order to retrieve all columns of the table Album in the Chinook database. Recall that the query `SELECT *` selects all columns.\n",
    "\n",
    "* Open the engine connection as con using the method `connect()` on the engine.\n",
    "* Execute the query that selects ALL columns from the Album table. Store the results in rs.\n",
    "* Store all of your query results in the DataFrame df by applying the `fetchall()` method to the results rs.\n",
    "* Close the connection!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8c8d7019",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   AlbumId                                  Title  ArtistId\n",
      "0        1  For Those About To Rock We Salute You         1\n",
      "1        2                      Balls to the Wall         2\n",
      "2        3                      Restless and Wild         2\n",
      "3        4                      Let There Be Rock         1\n",
      "4        5                               Big Ones         3\n"
     ]
    }
   ],
   "source": [
    "# Import packages\n",
    "from sqlalchemy import create_engine\n",
    "import pandas as pd\n",
    "\n",
    "# Create engine: engine\n",
    "engine = create_engine('sqlite:///datasets/Chinook.sqlite')\n",
    "\n",
    "# Open engine connection\n",
    "con = engine.connect()\n",
    "\n",
    "# Perform query: rs\n",
    "rs = con.execute(\"SELECT * FROM Album\")\n",
    "\n",
    "# Save results of the query to DataFrame: df\n",
    "df = pd.DataFrame(rs.fetchall())\n",
    "\n",
    "# Close connection\n",
    "con.close()\n",
    "\n",
    "# Print head of DataFrame df\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35cccb85",
   "metadata": {},
   "source": [
    "Good job!\n",
    "\n",
    "## Customizing the Hello World of SQL Queries\n",
    "Congratulations on executing your first SQL query! Now you're going to figure out how to customize your query in order to:\n",
    "\n",
    "* Select specified columns from a table;\n",
    "* Select a specified number of rows;\n",
    "* Import column names from the database table.\n",
    "\n",
    "Recall that Hugo performed a very similar query customization in the video:\n",
    "```sql\n",
    "engine = create_engine('sqlite:///Northwind.sqlite')\n",
    "\n",
    "with engine.connect() as con:\n",
    "    rs = con.execute(\"SELECT OrderID, OrderDate, ShipName FROM Orders\")\n",
    "    df = pd.DataFrame(rs.fetchmany(size=5))\n",
    "    df.columns = rs.keys()\n",
    "```\n",
    "\n",
    "Packages have already been imported as follows:\n",
    "```python\n",
    "from sqlalchemy import create_engine\n",
    "import pandas as pd\n",
    "```\n",
    "\n",
    "The engine has also already been created:\n",
    "```sql\n",
    "engine = create_engine('sqlite:///Chinook.sqlite')\n",
    "```\n",
    "The engine connection is already open with the statement\n",
    "```python\n",
    "with engine.connect() as con:\n",
    "```\n",
    "All the code you need to complete is within this context.\n",
    "\n",
    "* Execute the SQL query that selects the columns LastName and Title from the Employee table. Store the results in the variable rs.\n",
    "* Apply the method `fetchmany()` to rs in order to retrieve 3 of the records. Store them in the DataFrame df.\n",
    "* Using the rs object, set the DataFrame's column names to the corresponding names of the table columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "20408bc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "  LastName                Title\n",
      "0    Adams      General Manager\n",
      "1  Edwards        Sales Manager\n",
      "2  Peacock  Sales Support Agent\n"
     ]
    }
   ],
   "source": [
    "# Open engine in context manager\n",
    "# Perform query and save results to DataFrame: df\n",
    "with engine.connect() as con:\n",
    "    rs = con.execute(\"SELECT LastName, Title FROM Employee\")\n",
    "    df = pd.DataFrame(rs.fetchmany(size=3))\n",
    "    df.columns = rs.keys()\n",
    "\n",
    "# Print the length of the DataFrame df\n",
    "print(len(df))\n",
    "\n",
    "# Print the head of the DataFrame df\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c32b9c2",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Filtering your database records using SQL's WHERE\n",
    "You can now execute a basic SQL query to select records from any table in your database and you can also perform simple query customizations to select particular columns and numbers of rows.\n",
    "\n",
    "There are a couple more standard SQL query chops that will aid you in your journey to becoming an SQL ninja.\n",
    "\n",
    "Let's say, for example that you wanted to get all records from the Customer table of the Chinook database for which the Country is 'Canada'. You can do this very easily in SQL using a SELECT statement followed by a WHERE clause as follows:\n",
    "```sql\n",
    "SELECT * FROM Customer WHERE Country = 'Canada'\n",
    "```\n",
    "\n",
    "In fact, you can filter any SELECT statement by any condition using a WHERE clause. This is called filtering your records.\n",
    "\n",
    "In this interactive exercise, you'll select all records of the Employee table for which 'EmployeeId' is greater than or equal to 6.\n",
    "\n",
    "Packages are already imported as follows:\n",
    "```python\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "```\n",
    "Query away!\n",
    "\n",
    "* Complete the argument of `create_engine()` so that the engine for the SQLite database `'Chinook.sqlite'` is created.\n",
    "* Execute the query that selects all records from the Employee table where 'EmployeeId' is greater than or equal to 6. Use the >= operator and assign the results to rs.\n",
    "* Apply the method `fetchall()` to rs in order to fetch all records in rs. Store them in the DataFrame df.\n",
    "* Using the rs object, set the DataFrame's column names to the corresponding names of the table columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d2fb1137",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeId  LastName FirstName       Title  ReportsTo            BirthDate  \\\n",
      "0           6  Mitchell   Michael  IT Manager          1  1973-07-01 00:00:00   \n",
      "1           7      King    Robert    IT Staff          6  1970-05-29 00:00:00   \n",
      "2           8  Callahan     Laura    IT Staff          6  1968-01-09 00:00:00   \n",
      "\n",
      "              HireDate                      Address        City State Country  \\\n",
      "0  2003-10-17 00:00:00         5827 Bowness Road NW     Calgary    AB  Canada   \n",
      "1  2004-01-02 00:00:00  590 Columbia Boulevard West  Lethbridge    AB  Canada   \n",
      "2  2004-03-04 00:00:00                  923 7 ST NW  Lethbridge    AB  Canada   \n",
      "\n",
      "  PostalCode              Phone                Fax                    Email  \n",
      "0    T3B 0C5  +1 (403) 246-9887  +1 (403) 246-9899  michael@chinookcorp.com  \n",
      "1    T1K 5N8  +1 (403) 456-9986  +1 (403) 456-8485   robert@chinookcorp.com  \n",
      "2    T1H 1Y8  +1 (403) 467-3351  +1 (403) 467-8772    laura@chinookcorp.com  \n"
     ]
    }
   ],
   "source": [
    "# Create engine: engine\n",
    "engine = create_engine('sqlite:///datasets/Chinook.sqlite')\n",
    "\n",
    "# Open engine in context manager\n",
    "# Perform query and save results to DataFrame: df\n",
    "with engine.connect() as con:\n",
    "    rs = con.execute(\"SELECT * FROM Employee WHERE EmployeeId >= 6\")\n",
    "    df = pd.DataFrame(rs.fetchall())\n",
    "    df.columns = rs.keys()\n",
    "\n",
    "# Print the head of the DataFrame df\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d74b6a14",
   "metadata": {},
   "source": [
    "Good job!\n",
    "\n",
    "## Ordering your SQL records with ORDER BY\n",
    "You can also order your SQL query results. For example, if you wanted to get all records from the Customer table of the Chinook database and order them in increasing order by the column SupportRepId, you could do so with the following query:\n",
    "```sql\n",
    "\"SELECT * FROM Customer ORDER BY SupportRepId\"\n",
    "In fact, you can order any SELECT statement by any column.\n",
    "```\n",
    "In this interactive exercise, you'll select all records of the Employee table and order them in increasing order by the column BirthDate.\n",
    "\n",
    "Packages are already imported as follows:\n",
    "```python\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "```\n",
    "Get querying!\n",
    "\n",
    "* Using the function `create_engine()`, create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.\n",
    "* In the context manager, execute the query that selects all records from the Employee table and orders them in increasing order by the column BirthDate. Assign the result to rs.\n",
    "* In a call to `pd.DataFrame(`), apply the method `fetchall()` to rs in order to fetch all records in rs. Store them in the DataFrame df.\n",
    "* Set the DataFrame's column names to the corresponding names of the table columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2dfebcf3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeId  LastName FirstName                Title  ReportsTo  \\\n",
      "0           4      Park  Margaret  Sales Support Agent        2.0   \n",
      "1           2   Edwards     Nancy        Sales Manager        1.0   \n",
      "2           1     Adams    Andrew      General Manager        NaN   \n",
      "3           5   Johnson     Steve  Sales Support Agent        2.0   \n",
      "4           8  Callahan     Laura             IT Staff        6.0   \n",
      "\n",
      "             BirthDate             HireDate              Address        City  \\\n",
      "0  1947-09-19 00:00:00  2003-05-03 00:00:00     683 10 Street SW     Calgary   \n",
      "1  1958-12-08 00:00:00  2002-05-01 00:00:00         825 8 Ave SW     Calgary   \n",
      "2  1962-02-18 00:00:00  2002-08-14 00:00:00  11120 Jasper Ave NW    Edmonton   \n",
      "3  1965-03-03 00:00:00  2003-10-17 00:00:00         7727B 41 Ave     Calgary   \n",
      "4  1968-01-09 00:00:00  2004-03-04 00:00:00          923 7 ST NW  Lethbridge   \n",
      "\n",
      "  State Country PostalCode              Phone                Fax  \\\n",
      "0    AB  Canada    T2P 5G3  +1 (403) 263-4423  +1 (403) 263-4289   \n",
      "1    AB  Canada    T2P 2T3  +1 (403) 262-3443  +1 (403) 262-3322   \n",
      "2    AB  Canada    T5K 2N1  +1 (780) 428-9482  +1 (780) 428-3457   \n",
      "3    AB  Canada    T3B 1Y7   1 (780) 836-9987   1 (780) 836-9543   \n",
      "4    AB  Canada    T1H 1Y8  +1 (403) 467-3351  +1 (403) 467-8772   \n",
      "\n",
      "                      Email  \n",
      "0  margaret@chinookcorp.com  \n",
      "1     nancy@chinookcorp.com  \n",
      "2    andrew@chinookcorp.com  \n",
      "3     steve@chinookcorp.com  \n",
      "4     laura@chinookcorp.com  \n"
     ]
    }
   ],
   "source": [
    "# Create engine: engine\n",
    "engine = create_engine('sqlite:///datasets/Chinook.sqlite')\n",
    "\n",
    "# Open engine in context manager\n",
    "with engine.connect() as con:\n",
    "    rs = con.execute(\"SELECT * FROM Employee ORDER BY BirthDate\")\n",
    "    df = pd.DataFrame(rs.fetchall())\n",
    "\n",
    "    # Set the DataFrame's column names\n",
    "    df.columns = rs.keys()\n",
    "\n",
    "# Print head of DataFrame\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56fc33e3",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## Pandas and The Hello World of SQL Queries!\n",
    "Here, you'll take advantage of the power of pandas to write the results of your SQL query to a DataFrame in one swift line of Python code!\n",
    "\n",
    "You'll first import pandas and create the SQLite `'Chinook.sqlite'` engine. Then you'll query the database to select all records from the Album table.\n",
    "\n",
    "Recall that to select all records from the Orders table in the Northwind database, Hugo executed the following command:\n",
    "```python\n",
    "df = pd.read_sql_query(\"SELECT * FROM Orders\", engine)\n",
    "```\n",
    "* Import the pandas package using the alias pd.\n",
    "* Using the function `create_engine()`, create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.\n",
    "* Use the pandas function `read_sql_query()` to assign to the variable df the DataFrame of results from the following query: select all records from the table Album.\n",
    "* The remainder of the code is included to confirm that the DataFrame created by this method is equal to that created by the previous method that you learned."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4ee1ff21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   AlbumId                                  Title  ArtistId\n",
      "0        1  For Those About To Rock We Salute You         1\n",
      "1        2                      Balls to the Wall         2\n",
      "2        3                      Restless and Wild         2\n",
      "3        4                      Let There Be Rock         1\n",
      "4        5                               Big Ones         3\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Import packages\n",
    "from sqlalchemy import create_engine\n",
    "import pandas as pd\n",
    "\n",
    "# Create engine: engine\n",
    "engine = create_engine('sqlite:///datasets/Chinook.sqlite')\n",
    "\n",
    "# Execute query and store records in DataFrame: df\n",
    "df = pd.read_sql_query(\"SELECT * FROM Album\", engine)\n",
    "\n",
    "# Print head of DataFrame\n",
    "print(df.head())\n",
    "\n",
    "# Open engine in context manager and store query result in df1\n",
    "with engine.connect() as con:\n",
    "    rs = con.execute(\"SELECT * FROM Album\")\n",
    "    df1 = pd.DataFrame(rs.fetchall())\n",
    "    df1.columns = rs.keys()\n",
    "\n",
    "# Confirm that both methods yield the same result\n",
    "print(df.equals(df1))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ac5ab45",
   "metadata": {},
   "source": [
    "Excellent!\n",
    "\n",
    "## Pandas for more complex querying\n",
    "Here, you'll become more familiar with the pandas function `read_sql_query()` by using it to execute a more complex query: a `SELECT` statement followed by both a `WHERE` clause `AND` an `ORDER BY` clause.\n",
    "\n",
    "You'll build a DataFrame that contains the rows of the Employee table for which the EmployeeId is greater than or equal to 6 and you'll order these entries by BirthDate.\n",
    "\n",
    "* Using the function `create_engine()`, create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.\n",
    "* Use the pandas function `read_sql_query()` to assign to the variable df the DataFrame of results from the following query: select all records from the Employee table where the EmployeeId is greater than or equal to 6 and ordered by BirthDate (make sure to use WHERE and ORDER BY in this precise order)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "da0a4f1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeId  LastName FirstName       Title  ReportsTo            BirthDate  \\\n",
      "0           8  Callahan     Laura    IT Staff          6  1968-01-09 00:00:00   \n",
      "1           7      King    Robert    IT Staff          6  1970-05-29 00:00:00   \n",
      "2           6  Mitchell   Michael  IT Manager          1  1973-07-01 00:00:00   \n",
      "\n",
      "              HireDate                      Address        City State Country  \\\n",
      "0  2004-03-04 00:00:00                  923 7 ST NW  Lethbridge    AB  Canada   \n",
      "1  2004-01-02 00:00:00  590 Columbia Boulevard West  Lethbridge    AB  Canada   \n",
      "2  2003-10-17 00:00:00         5827 Bowness Road NW     Calgary    AB  Canada   \n",
      "\n",
      "  PostalCode              Phone                Fax                    Email  \n",
      "0    T1H 1Y8  +1 (403) 467-3351  +1 (403) 467-8772    laura@chinookcorp.com  \n",
      "1    T1K 5N8  +1 (403) 456-9986  +1 (403) 456-8485   robert@chinookcorp.com  \n",
      "2    T3B 0C5  +1 (403) 246-9887  +1 (403) 246-9899  michael@chinookcorp.com  \n"
     ]
    }
   ],
   "source": [
    "# Import packages\n",
    "from sqlalchemy import create_engine\n",
    "import pandas as pd\n",
    "\n",
    "# Create engine: engine\n",
    "engine = create_engine('sqlite:///datasets/Chinook.sqlite')\n",
    "\n",
    "# Execute query and store records in DataFrame: df\n",
    "df = pd.read_sql_query(\n",
    "    \"SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate\",\n",
    "    engine\n",
    ")\n",
    "\n",
    "# Print head of DataFrame\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00d15b85",
   "metadata": {},
   "source": [
    "Awesome!\n",
    "\n",
    "## The power of SQL lies in relationships between tables: INNER JOIN\n",
    "Here, you'll perform your first INNER JOIN! You'll be working with your favourite SQLite database, Chinook.sqlite. For each record in the Album table, you'll extract the Title along with the Name of the Artist. The latter will come from the Artist table and so you will need to INNER JOIN these two tables on the ArtistID column of both.\n",
    "\n",
    "Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:\n",
    "```sql\n",
    "SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID\n",
    "```\n",
    "\n",
    "* Assign to rs the results from the following query: select all the records, extracting the Title of the record and Name of the artist of each record from the Album table and the Artist table, respectively. To do so, `INNER JOIN` these two tables on the ArtistID column of both.\n",
    "* In a call to `pd.DataFrame()`, apply the method `fetchall()` to rs in order to fetch all records in rs. Store them in the DataFrame df.\n",
    "* Set the DataFrame's column names to the corresponding names of the table columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1fa60f6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                   Title       Name\n",
      "0  For Those About To Rock We Salute You      AC/DC\n",
      "1                      Balls to the Wall     Accept\n",
      "2                      Restless and Wild     Accept\n",
      "3                      Let There Be Rock      AC/DC\n",
      "4                               Big Ones  Aerosmith\n"
     ]
    }
   ],
   "source": [
    "# Open engine in context manager\n",
    "# Perform query and save results to DataFrame: df\n",
    "with engine.connect() as con:\n",
    "    rs = con.execute(\"SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID\")\n",
    "    df = pd.DataFrame(rs.fetchall())\n",
    "    df.columns = rs.keys()\n",
    "\n",
    "# Print head of DataFrame df\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3a52d938",
   "metadata": {},
   "source": [
    "Good job!\n",
    "\n",
    "Filtering your INNER JOIN\n",
    "Congrats on performing your first INNER JOIN! You're now going to finish this chapter with one final exercise in which you perform an INNER JOIN and filter the result using a WHERE clause.\n",
    "\n",
    "Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:\n",
    "```sql\n",
    "SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID\n",
    "```\n",
    "\n",
    "* Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from PlaylistTrack `INNER JOIN` Track on PlaylistTrack.TrackId = Track.TrackId that satisfy the condition Milliseconds < 250000."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f2c861d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   PlaylistId  TrackId  TrackId              Name  AlbumId  MediaTypeId  \\\n",
      "0           1     3390     3390  One and the Same      271            2   \n",
      "1           1     3392     3392     Until We Fall      271            2   \n",
      "2           1     3393     3393     Original Fire      271            2   \n",
      "3           1     3394     3394       Broken City      271            2   \n",
      "4           1     3395     3395          Somedays      271            2   \n",
      "\n",
      "   GenreId Composer  Milliseconds    Bytes  UnitPrice  \n",
      "0       23     None        217732  3559040       0.99  \n",
      "1       23     None        230758  3766605       0.99  \n",
      "2       23     None        218916  3577821       0.99  \n",
      "3       23     None        228366  3728955       0.99  \n",
      "4       23     None        213831  3497176       0.99  \n"
     ]
    }
   ],
   "source": [
    "# Execute query and store records in DataFrame: df\n",
    "df = pd.read_sql_query(\n",
    "    \"SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000\",\n",
    "    engine\n",
    ")\n",
    "\n",
    "# Print head of DataFrame\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4bec4d95",
   "metadata": {},
   "source": [
    "Great work!"
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
