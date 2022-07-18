{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "80e57401",
   "metadata": {},
   "source": [
    "# Advanced Merging and Concatenating\n",
    "\n",
    "## Steps of a semi join\n",
    "In the last video, you were shown how to perform a semi join with pandas. In this exercise, you'll solidify your understanding of the necessary steps. Recall that a semi join filters the left table to only the rows where a match exists in both the left and right tables.\n",
    "\n",
    "* Sort the steps in the correct order of the technique shown to perform a semi join in pandas.\n",
    "\n",
    "```\n",
    "Merge the left and right tables on key column using an inner join.\n",
    "\n",
    "Search if the key column in the left table is in the merged tables using the .isin() method creating a Boolean Series.\n",
    "\n",
    "Subset the rows of the left table\n",
    "```\n",
    "\n",
    "Congratulations! You have a sense of the steps in this technique. It first merges the tables, then searches it for which rows belong in the final result creating a filter and subsets the left table with that filter.\n",
    "\n",
    "## Performing an anti join\n",
    "In our music streaming company dataset, each customer is assigned an employee representative to assist them. In this exercise, filter the employee table by a table of top customers, returning only those employees who are not assigned to a customer. The results should resemble the results of an anti join. The company's leadership will assign these employees additional training so that they can work with high valued customers.\n",
    "\n",
    "* Merge employees and `top_cust` with a left join, setting indicator argument to True. Save the result to `empl_cust`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9b5ec9cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e50e4d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge employees and top_cust\n",
    "empl_cust = employees.merge(top_cust, on='srid', \n",
    "                            how='left', indicator=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "924c5bfd",
   "metadata": {},
   "source": [
    "* Select the `srid` column of `empl_cust` and the rows where `_merge` is 'left_only'. Save the result to `srid_list`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a333d52",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Select the srid column where _merge is left_only\n",
    "srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47fbc2bb",
   "metadata": {},
   "source": [
    "* Subset the employees table and select those rows where the srid is in the variable `srid_list` and print the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "905536a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get employees not working with top customers\n",
    "print(employees[employees['srid'].isin(srid_list)])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80b48fc3",
   "metadata": {},
   "source": [
    "Success! You performed an anti join by first merging the tables with a left join, selecting the ID of those employees who did not support a top customer, and then subsetting the original employee's table. From that, we can see that there are five employees not supporting top customers. Anti joins are a powerful tool to filter a main table (i.e. employees) by another (i.e. customers).\n",
    "\n",
    "## Performing a semi join\n",
    "Some of the tracks that have generated the most significant amount of revenue are from TV-shows or are other non-musical audio. You have been given a table of invoices that include top revenue-generating items. Additionally, you have a table of non-musical tracks from the streaming service. In this exercise, you'll use a semi join to find the top revenue-generating non-musical tracks..\n",
    "\n",
    "* Merge `non_mus_tcks` and `top_invoices` on tid using an inner join. Save the result as `tracks_invoices`.\n",
    "* Use `.isin()` to subset the rows of `non_mus_tck` where tid is in the tid column of `tracks_invoices`. Save the result as top_tracks.\n",
    "* Group `top_tracks` by gid and count the tid rows. Save the result to `cnt_by_gid`.\n",
    "* Merge `cnt_by_gid` with the genres table on gid and print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e5e854c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge the non_mus_tck and top_invoices tables on tid\n",
    "tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')\n",
    "\n",
    "# Use .isin() to subset non_mus_tcsk to rows with tid in tracks_invoices\n",
    "top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]\n",
    "\n",
    "# Group the top_tracks by gid and count the tid rows\n",
    "cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})\n",
    "\n",
    "# Merge the genres table to cnt_by_gid on gid and print\n",
    "print(cnt_by_gid.merge(genres, on='gid'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "001f8b2c",
   "metadata": {},
   "source": [
    "Nice job! In this exercise, you replicated a semi join to filter the table of tracks by the table of invoice items to find the top revenue non-musical tracks. With some additional data manipulation, you discovered that 'TV-shows' is the non-musical genre that has the most top revenue-generating tracks. Now that you've done both semi- and anti joins, it's time to move to the next topic.\n",
    "\n",
    "## Concatenation basics\n",
    "You have been given a few tables of data with musical track info for different albums from the metal band, Metallica. The track info comes from their Ride The Lightning, Master Of Puppets, and St. Anger albums. Try various features of the .concat() method by concatenating the tables vertically together in different ways.\n",
    "\n",
    "* Concatenate `tracks_master`, `tracks_ride`, and `tracks_st`, in that order, setting sort to True."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7261466",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate the tracks\n",
    "tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], \n",
    "                               sort=True)\n",
    "print(tracks_from_albums)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3a34b1a4",
   "metadata": {},
   "source": [
    "* Concatenate `tracks_master`, `tracks_ride`, and `tracks_st`, where the index goes from 0 to n-1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "529571c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate the tracks so the index goes from 0 to n-1\n",
    "tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],\n",
    "                               ignore_index=True,\n",
    "                               sort=True)\n",
    "print(tracks_from_albums)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9884cf6b",
   "metadata": {},
   "source": [
    "* Concatenate `tracks_master`, `tracks_ride`, and `tracks_st`, showing only columns that are in all tables."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a9349fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate the tracks, show only columns names that are in all tables\n",
    "tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],\n",
    "                               join='inner',\n",
    "                               sort=True)\n",
    "print(tracks_from_albums)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f6486985",
   "metadata": {},
   "source": [
    "Great job! You've concatenated your first set of tables, adjusted the index, and altered the columns shown in the output. The .concat() method is a very flexible tool that is useful for combining data into a new dataset.\n",
    "\n",
    "## Concatenating with keys\n",
    "The leadership of the music streaming company has come to you and asked you for assistance in analyzing sales for a recent business quarter. They would like to know which month in the quarter saw the highest average invoice total. You have been given three tables with invoice data named `inv_jul`, `inv_aug`, and `inv_sep`. Concatenate these tables into one to create a graph of the average monthly invoice total.\n",
    "\n",
    "* Concatenate the three tables together vertically in order with the oldest month first, adding '7Jul', '8Aug', and '9Sep' as keys for their respective months, and save to variable `avg_inv_by_month`.\n",
    "* Use the `.agg()` method to find the average of the total column from the grouped invoices.\n",
    "* Create a bar chart of `avg_inv_by_month`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "370e533d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate the tables and add keys\n",
    "inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], \n",
    "                            keys=['7Jul','8Aug','9Sep'])\n",
    "\n",
    "# Group the invoices by the index keys and find avg of the total column\n",
    "avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})\n",
    "\n",
    "# Bar plot of avg_inv_by_month\n",
    "avg_inv_by_month.plot(kind='bar')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7095221",
   "metadata": {},
   "source": [
    "![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIKICAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyBoZWlnaHQ9IjQyNnB0IiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCA1NjYgNDI2IiB3aWR0aD0iNTY2cHQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPgogPG1ldGFkYXRhPgogIDxyZGY6UkRGIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgPGNjOldvcms+CiAgICA8ZGM6dHlwZSByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIi8+CiAgICA8ZGM6ZGF0ZT4yMDIyLTA3LTE4VDIyOjA5OjEyLjk0MjM1MzwvZGM6ZGF0ZT4KICAgIDxkYzpmb3JtYXQ+aW1hZ2Uvc3ZnK3htbDwvZGM6Zm9ybWF0PgogICAgPGRjOmNyZWF0b3I+CiAgICAgPGNjOkFnZW50PgogICAgICA8ZGM6dGl0bGU+TWF0cGxvdGxpYiB2My40LjMsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvPC9kYzp0aXRsZT4KICAgICA8L2NjOkFnZW50PgogICAgPC9kYzpjcmVhdG9yPgogICA8L2NjOldvcms+CiAgPC9yZGY6UkRGPgogPC9tZXRhZGF0YT4KIDxkZWZzPgogIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+KntzdHJva2UtbGluZWNhcDpidXR0O3N0cm9rZS1saW5lam9pbjpyb3VuZDt9PC9zdHlsZT4KIDwvZGVmcz4KIDxnIGlkPSJmaWd1cmVfMSI+CiAgPGcgaWQ9InBhdGNoXzEiPgogICA8cGF0aCBkPSJNIDAgNDI2IApMIDU2NiA0MjYgCkwgNTY2IDAgCkwgMCAwIAp6CiIgc3R5bGU9ImZpbGw6I2ZmZmZmZjsiLz4KICA8L2c+CiAgPGcgaWQ9ImF4ZXNfMSI+CiAgIDxnIGlkPSJwYXRjaF8yIj4KICAgIDxwYXRoIGQ9Ik0gMjQuMTYyNSAzODIuMzEwOTM4IApMIDU1NS4yIDM4Mi4zMTA5MzggCkwgNTU1LjIgMTAuOCAKTCAyNC4xNjI1IDEwLjggCnoKIiBzdHlsZT0iZmlsbDojZmZmZmZmOyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF8zIj4KICAgIDxwYXRoIGNsaXAtcGF0aD0idXJsKCNwMDhlNWNmOTg1YikiIGQ9Ik0gNjguNDE1NjI1IDM4Mi4zMTA5MzggCkwgMTU2LjkyMTg3NSAzODIuMzEwOTM4IApMIDE1Ni45MjE4NzUgNTkuMDgxMTk2IApMIDY4LjQxNTYyNSA1OS4wODExOTYgCnoKIiBzdHlsZT0iZmlsbDojMWY3N2I0OyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF80Ij4KICAgIDxwYXRoIGNsaXAtcGF0aD0idXJsKCNwMDhlNWNmOTg1YikiIGQ9Ik0gMjQ1LjQyODEyNSAzODIuMzEwOTM4IApMIDMzMy45MzQzNzUgMzgyLjMxMDkzOCAKTCAzMzMuOTM0Mzc1IDQ1LjQ3ODY4MiAKTCAyNDUuNDI4MTI1IDQ1LjQ3ODY4MiAKegoiIHN0eWxlPSJmaWxsOiMxZjc3YjQ7Ii8+CiAgIDwvZz4KICAgPGcgaWQ9InBhdGNoXzUiPgogICAgPHBhdGggY2xpcC1wYXRoPSJ1cmwoI3AwOGU1Y2Y5ODViKSIgZD0iTSA0MjIuNDQwNjI1IDM4Mi4zMTA5MzggCkwgNTEwLjk0Njg3NSAzODIuMzEwOTM4IApMIDUxMC45NDY4NzUgMjguNDkwOTk3IApMIDQyMi40NDA2MjUgMjguNDkwOTk3IAp6CiIgc3R5bGU9ImZpbGw6IzFmNzdiNDsiLz4KICAgPC9nPgogICA8ZyBpZD0ibWF0cGxvdGxpYi5heGlzXzEiPgogICAgPGcgaWQ9Inh0aWNrXzEiPgogICAgIDxnIGlkPSJsaW5lMmRfMSI+CiAgICAgIDxkZWZzPgogICAgICAgPHBhdGggZD0iTSAwIDAgCkwgMCAzLjUgCiIgaWQ9Im1mYjBlZmI5NDhjIiBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiLz4KICAgICAgPC9kZWZzPgogICAgICA8Zz4KICAgICAgIDx1c2Ugc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjg7IiB4PSIxMTIuNjY4NzUiIHhsaW5rOmhyZWY9IiNtZmIwZWZiOTQ4YyIgeT0iMzgyLjMxMDkzOCIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzEiPgogICAgICA8IS0tIDdKdWwgLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDExNS40MjgxMjUgNDA3LjczOTA2Milyb3RhdGUoLTkwKXNjYWxlKDAuMSAtMC4xKSI+CiAgICAgICA8ZGVmcz4KICAgICAgICA8cGF0aCBkPSJNIDUyNSA0NjY2IApMIDM1MjUgNDY2NiAKTCAzNTI1IDQzOTcgCkwgMTgzMSAwIApMIDExNzIgMCAKTCAyNzY2IDQxMzQgCkwgNTI1IDQxMzQgCkwgNTI1IDQ2NjYgCnoKIiBpZD0iRGVqYVZ1U2Fucy0zNyIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgICA8cGF0aCBkPSJNIDYyOCA0NjY2IApMIDEyNTkgNDY2NiAKTCAxMjU5IDMyNSAKUSAxMjU5IC01MTkgOTM5IC05MDAgClEgNjE5IC0xMjgxIC05MSAtMTI4MSAKTCAtMzMxIC0xMjgxIApMIC0zMzEgLTc1MCAKTCAtMTM0IC03NTAgClEgMjg0IC03NTAgNDU2IC01MTUgClEgNjI4IC0yODEgNjI4IDMyNSAKTCA2MjggNDY2NiAKegoiIGlkPSJEZWphVnVTYW5zLTRhIiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgIDxwYXRoIGQ9Ik0gNTQ0IDEzODEgCkwgNTQ0IDM1MDAgCkwgMTExOSAzNTAwIApMIDExMTkgMTQwMyAKUSAxMTE5IDkwNiAxMzEyIDY1NyAKUSAxNTA2IDQwOSAxODk0IDQwOSAKUSAyMzU5IDQwOSAyNjI5IDcwNiAKUSAyOTAwIDEwMDMgMjkwMCAxNTE2IApMIDI5MDAgMzUwMCAKTCAzNDc1IDM1MDAgCkwgMzQ3NSAwIApMIDI5MDAgMCAKTCAyOTAwIDUzOCAKUSAyNjkxIDIxOSAyNDE0IDY0IApRIDIxMzggLTkxIDE3NzIgLTkxIApRIDExNjkgLTkxIDg1NiAyODQgClEgNTQ0IDY1OSA1NDQgMTM4MSAKegpNIDE5OTEgMzU4NCAKTCAxOTkxIDM1ODQgCnoKIiBpZD0iRGVqYVZ1U2Fucy03NSIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgICA8cGF0aCBkPSJNIDYwMyA0ODYzIApMIDExNzggNDg2MyAKTCAxMTc4IDAgCkwgNjAzIDAgCkwgNjAzIDQ4NjMgCnoKIiBpZD0iRGVqYVZ1U2Fucy02YyIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtMzciLz4KICAgICAgIDx1c2UgeD0iNjMuNjIzMDQ3IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy00YSIvPgogICAgICAgPHVzZSB4PSI5My4xMTUyMzQiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTc1Ii8+CiAgICAgICA8dXNlIHg9IjE1Ni40OTQxNDEiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTZjIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyBpZD0ieHRpY2tfMiI+CiAgICAgPGcgaWQ9ImxpbmUyZF8yIj4KICAgICAgPGc+CiAgICAgICA8dXNlIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIgeD0iMjg5LjY4MTI1IiB4bGluazpocmVmPSIjbWZiMGVmYjk0OGMiIHk9IjM4Mi4zMTA5MzgiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgICA8ZyBpZD0idGV4dF8yIj4KICAgICAgPCEtLSA4QXVnIC0tPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyOTIuNDQwNjI1IDQxNS4yKXJvdGF0ZSgtOTApc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgIDxkZWZzPgogICAgICAgIDxwYXRoIGQ9Ik0gMjAzNCAyMjE2IApRIDE1ODQgMjIxNiAxMzI2IDE5NzUgClEgMTA2OSAxNzM0IDEwNjkgMTMxMyAKUSAxMDY5IDg5MSAxMzI2IDY1MCAKUSAxNTg0IDQwOSAyMDM0IDQwOSAKUSAyNDg0IDQwOSAyNzQzIDY1MSAKUSAzMDAzIDg5NCAzMDAzIDEzMTMgClEgMzAwMyAxNzM0IDI3NDUgMTk3NSAKUSAyNDg4IDIyMTYgMjAzNCAyMjE2IAp6Ck0gMTQwMyAyNDg0IApRIDk5NyAyNTg0IDc3MCAyODYyIApRIDU0NCAzMTQxIDU0NCAzNTQxIApRIDU0NCA0MTAwIDk0MiA0NDI1IApRIDEzNDEgNDc1MCAyMDM0IDQ3NTAgClEgMjczMSA0NzUwIDMxMjggNDQyNSAKUSAzNTI1IDQxMDAgMzUyNSAzNTQxIApRIDM1MjUgMzE0MSAzMjk4IDI4NjIgClEgMzA3MiAyNTg0IDI2NjkgMjQ4NCAKUSAzMTI1IDIzNzggMzM3OSAyMDY4IApRIDM2MzQgMTc1OSAzNjM0IDEzMTMgClEgMzYzNCA2MzQgMzIyMCAyNzEgClEgMjgwNiAtOTEgMjAzNCAtOTEgClEgMTI2MyAtOTEgODQ4IDI3MSAKUSA0MzQgNjM0IDQzNCAxMzEzIApRIDQzNCAxNzU5IDY5MCAyMDY4IApRIDk0NyAyMzc4IDE0MDMgMjQ4NCAKegpNIDExNzIgMzQ4MSAKUSAxMTcyIDMxMTkgMTM5OCAyOTE2IApRIDE2MjUgMjcxMyAyMDM0IDI3MTMgClEgMjQ0MSAyNzEzIDI2NzAgMjkxNiAKUSAyOTAwIDMxMTkgMjkwMCAzNDgxIApRIDI5MDAgMzg0NCAyNjcwIDQwNDcgClEgMjQ0MSA0MjUwIDIwMzQgNDI1MCAKUSAxNjI1IDQyNTAgMTM5OCA0MDQ3IApRIDExNzIgMzg0NCAxMTcyIDM0ODEgCnoKIiBpZD0iRGVqYVZ1U2Fucy0zOCIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgICA8cGF0aCBkPSJNIDIxODggNDA0NCAKTCAxMzMxIDE3MjIgCkwgMzA0NyAxNzIyIApMIDIxODggNDA0NCAKegpNIDE4MzEgNDY2NiAKTCAyNTQ3IDQ2NjYgCkwgNDMyNSAwIApMIDM2NjkgMCAKTCAzMjQ0IDExOTcgCkwgMTE0MSAxMTk3IApMIDcxNiAwIApMIDUwIDAgCkwgMTgzMSA0NjY2IAp6CiIgaWQ9IkRlamFWdVNhbnMtNDEiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICAgPHBhdGggZD0iTSAyOTA2IDE3OTEgClEgMjkwNiAyNDE2IDI2NDggMjc1OSAKUSAyMzkxIDMxMDMgMTkyNSAzMTAzIApRIDE0NjMgMzEwMyAxMjA1IDI3NTkgClEgOTQ3IDI0MTYgOTQ3IDE3OTEgClEgOTQ3IDExNjkgMTIwNSA4MjUgClEgMTQ2MyA0ODEgMTkyNSA0ODEgClEgMjM5MSA0ODEgMjY0OCA4MjUgClEgMjkwNiAxMTY5IDI5MDYgMTc5MSAKegpNIDM0ODEgNDM0IApRIDM0ODEgLTQ1OSAzMDg0IC04OTUgClEgMjY4OCAtMTMzMSAxODY5IC0xMzMxIApRIDE1NjYgLTEzMzEgMTI5NyAtMTI4NiAKUSAxMDI4IC0xMjQxIDc3NSAtMTE0NyAKTCA3NzUgLTU4OCAKUSAxMDI4IC03MjUgMTI3NSAtNzkwIApRIDE1MjIgLTg1NiAxNzc4IC04NTYgClEgMjM0NCAtODU2IDI2MjUgLTU2MSAKUSAyOTA2IC0yNjYgMjkwNiAzMzEgCkwgMjkwNiA2MTYgClEgMjcyOCAzMDYgMjQ1MCAxNTMgClEgMjE3MiAwIDE3ODQgMCAKUSAxMTQxIDAgNzQ3IDQ5MCAKUSAzNTMgOTgxIDM1MyAxNzkxIApRIDM1MyAyNjAzIDc0NyAzMDkzIApRIDExNDEgMzU4NCAxNzg0IDM1ODQgClEgMjE3MiAzNTg0IDI0NTAgMzQzMSAKUSAyNzI4IDMyNzggMjkwNiAyOTY5IApMIDI5MDYgMzUwMCAKTCAzNDgxIDM1MDAgCkwgMzQ4MSA0MzQgCnoKIiBpZD0iRGVqYVZ1U2Fucy02NyIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtMzgiLz4KICAgICAgIDx1c2UgeD0iNjMuNjIzMDQ3IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy00MSIvPgogICAgICAgPHVzZSB4PSIxMzIuMDMxMjUiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTc1Ii8+CiAgICAgICA8dXNlIHg9IjE5NS40MTAxNTYiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTY3Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyBpZD0ieHRpY2tfMyI+CiAgICAgPGcgaWQ9ImxpbmUyZF8zIj4KICAgICAgPGc+CiAgICAgICA8dXNlIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIgeD0iNDY2LjY5Mzc1IiB4bGluazpocmVmPSIjbWZiMGVmYjk0OGMiIHk9IjM4Mi4zMTA5MzgiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgICA8ZyBpZD0idGV4dF8zIj4KICAgICAgPCEtLSA5U2VwIC0tPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0NjkuNDUzMTI1IDQxNC41MjM0Mzgpcm90YXRlKC05MClzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSA3MDMgOTcgCkwgNzAzIDY3MiAKUSA5NDEgNTU5IDExODQgNTAwIApRIDE0MjggNDQxIDE2NjMgNDQxIApRIDIyODggNDQxIDI2MTcgODYxIApRIDI5NDcgMTI4MSAyOTk0IDIxMzggClEgMjgxMyAxODY5IDI1MzQgMTcyNSAKUSAyMjU2IDE1ODEgMTkxOSAxNTgxIApRIDEyMTkgMTU4MSA4MTEgMjAwNCAKUSA0MDMgMjQyOCA0MDMgMzE2MyAKUSA0MDMgMzg4MSA4MjggNDMxNSAKUSAxMjUzIDQ3NTAgMTk1OSA0NzUwIApRIDI3NjkgNDc1MCAzMTk1IDQxMjkgClEgMzYyMiAzNTA5IDM2MjIgMjMyOCAKUSAzNjIyIDEyMjUgMzA5OCA1NjcgClEgMjU3NSAtOTEgMTY5MSAtOTEgClEgMTQ1MyAtOTEgMTIwOSAtNDQgClEgOTY2IDMgNzAzIDk3IAp6Ck0gMTk1OSAyMDc1IApRIDIzODQgMjA3NSAyNjMyIDIzNjUgClEgMjg4MSAyNjU2IDI4ODEgMzE2MyAKUSAyODgxIDM2NjYgMjYzMiAzOTU4IApRIDIzODQgNDI1MCAxOTU5IDQyNTAgClEgMTUzNCA0MjUwIDEyODYgMzk1OCAKUSAxMDM4IDM2NjYgMTAzOCAzMTYzIApRIDEwMzggMjY1NiAxMjg2IDIzNjUgClEgMTUzNCAyMDc1IDE5NTkgMjA3NSAKegoiIGlkPSJEZWphVnVTYW5zLTM5IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgIDxwYXRoIGQ9Ik0gMzQyNSA0NTEzIApMIDM0MjUgMzg5NyAKUSAzMDY2IDQwNjkgMjc0NyA0MTUzIApRIDI0MjggNDIzOCAyMTMxIDQyMzggClEgMTYxNiA0MjM4IDEzMzYgNDAzOCAKUSAxMDU2IDM4MzggMTA1NiAzNDY5IApRIDEwNTYgMzE1OSAxMjQyIDMwMDEgClEgMTQyOCAyODQ0IDE5NDcgMjc0NyAKTCAyMzI4IDI2NjkgClEgMzAzNCAyNTM0IDMzNzAgMjE5NSAKUSAzNzA2IDE4NTYgMzcwNiAxMjg4IApRIDM3MDYgNjA5IDMyNTEgMjU5IApRIDI3OTcgLTkxIDE5MTkgLTkxIApRIDE1ODggLTkxIDEyMTQgLTE2IApRIDg0MSA1OSA0NDEgMjA2IApMIDQ0MSA4NTYgClEgODI1IDY0MSAxMTk0IDUzMSAKUSAxNTYzIDQyMiAxOTE5IDQyMiAKUSAyNDU5IDQyMiAyNzUzIDYzNCAKUSAzMDQ3IDg0NyAzMDQ3IDEyNDEgClEgMzA0NyAxNTg0IDI4MzYgMTc3OCAKUSAyNjI1IDE5NzIgMjE0NCAyMDY5IApMIDE3NTkgMjE0NCAKUSAxMDUzIDIyODQgNzM3IDI1ODQgClEgNDIyIDI4ODQgNDIyIDM0MTkgClEgNDIyIDQwMzggODU4IDQzOTQgClEgMTI5NCA0NzUwIDIwNTkgNDc1MCAKUSAyMzg4IDQ3NTAgMjcyOCA0NjkwIApRIDMwNjkgNDYzMSAzNDI1IDQ1MTMgCnoKIiBpZD0iRGVqYVZ1U2Fucy01MyIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgICA8cGF0aCBkPSJNIDM1OTcgMTg5NCAKTCAzNTk3IDE2MTMgCkwgOTUzIDE2MTMgClEgOTkxIDEwMTkgMTMxMSA3MDggClEgMTYzMSAzOTcgMjIwMyAzOTcgClEgMjUzNCAzOTcgMjg0NSA0NzggClEgMzE1NiA1NTkgMzQ2MyA3MjIgCkwgMzQ2MyAxNzggClEgMzE1MyA0NyAyODI4IC0yMiAKUSAyNTAzIC05MSAyMTY5IC05MSAKUSAxMzMxIC05MSA4NDIgMzk2IApRIDM1MyA4ODQgMzUzIDE3MTYgClEgMzUzIDI1NzUgODE3IDMwNzkgClEgMTI4MSAzNTg0IDIwNjkgMzU4NCAKUSAyNzc1IDM1ODQgMzE4NiAzMTI5IApRIDM1OTcgMjY3NSAzNTk3IDE4OTQgCnoKTSAzMDIyIDIwNjMgClEgMzAxNiAyNTM0IDI3NTggMjgxNSAKUSAyNTAwIDMwOTcgMjA3NSAzMDk3IApRIDE1OTQgMzA5NyAxMzA1IDI4MjUgClEgMTAxNiAyNTUzIDk3MiAyMDU5IApMIDMwMjIgMjA2MyAKegoiIGlkPSJEZWphVnVTYW5zLTY1IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgIDxwYXRoIGQ9Ik0gMTE1OSA1MjUgCkwgMTE1OSAtMTMzMSAKTCA1ODEgLTEzMzEgCkwgNTgxIDM1MDAgCkwgMTE1OSAzNTAwIApMIDExNTkgMjk2OSAKUSAxMzQxIDMyODEgMTYxNyAzNDMyIApRIDE4OTQgMzU4NCAyMjc4IDM1ODQgClEgMjkxNiAzNTg0IDMzMTQgMzA3OCAKUSAzNzEzIDI1NzIgMzcxMyAxNzQ3IApRIDM3MTMgOTIyIDMzMTQgNDE1IApRIDI5MTYgLTkxIDIyNzggLTkxIApRIDE4OTQgLTkxIDE2MTcgNjEgClEgMTM0MSAyMTMgMTE1OSA1MjUgCnoKTSAzMTE2IDE3NDcgClEgMzExNiAyMzgxIDI4NTUgMjc0MiAKUSAyNTk0IDMxMDMgMjEzOCAzMTAzIApRIDE2ODEgMzEwMyAxNDIwIDI3NDIgClEgMTE1OSAyMzgxIDExNTkgMTc0NyAKUSAxMTU5IDExMTMgMTQyMCA3NTIgClEgMTY4MSAzOTEgMjEzOCAzOTEgClEgMjU5NCAzOTEgMjg1NSA3NTIgClEgMzExNiAxMTEzIDMxMTYgMTc0NyAKegoiIGlkPSJEZWphVnVTYW5zLTcwIiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgPC9kZWZzPgogICAgICAgPHVzZSB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy0zOSIvPgogICAgICAgPHVzZSB4PSI2My42MjMwNDciIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTUzIi8+CiAgICAgICA8dXNlIHg9IjEyNy4wOTk2MDkiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTY1Ii8+CiAgICAgICA8dXNlIHg9IjE4OC42MjMwNDciIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTcwIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgIDwvZz4KICAgPGcgaWQ9Im1hdHBsb3RsaWIuYXhpc18yIj4KICAgIDxnIGlkPSJ5dGlja18xIj4KICAgICA8ZyBpZD0ibGluZTJkXzQiPgogICAgICA8ZGVmcz4KICAgICAgIDxwYXRoIGQ9Ik0gMCAwIApMIC0zLjUgMCAKIiBpZD0ibWIwNGRlNWI1ZTciIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIvPgogICAgICA8L2RlZnM+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjI0LjE2MjUiIHhsaW5rOmhyZWY9IiNtYjA0ZGU1YjVlNyIgeT0iMzgyLjMxMDkzOCIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzQiPgogICAgICA8IS0tIDAgLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwLjggMzg2LjExMDE1NilzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSAyMDM0IDQyNTAgClEgMTU0NyA0MjUwIDEzMDEgMzc3MCAKUSAxMDU2IDMyOTEgMTA1NiAyMzI4IApRIDEwNTYgMTM2OSAxMzAxIDg4OSAKUSAxNTQ3IDQwOSAyMDM0IDQwOSAKUSAyNTI1IDQwOSAyNzcwIDg4OSAKUSAzMDE2IDEzNjkgMzAxNiAyMzI4IApRIDMwMTYgMzI5MSAyNzcwIDM3NzAgClEgMjUyNSA0MjUwIDIwMzQgNDI1MCAKegpNIDIwMzQgNDc1MCAKUSAyODE5IDQ3NTAgMzIzMyA0MTI5IApRIDM2NDcgMzUwOSAzNjQ3IDIzMjggClEgMzY0NyAxMTUwIDMyMzMgNTI5IApRIDI4MTkgLTkxIDIwMzQgLTkxIApRIDEyNTAgLTkxIDgzNiA1MjkgClEgNDIyIDExNTAgNDIyIDIzMjggClEgNDIyIDM1MDkgODM2IDQxMjkgClEgMTI1MCA0NzUwIDIwMzQgNDc1MCAKegoiIGlkPSJEZWphVnVTYW5zLTMwIiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgPC9kZWZzPgogICAgICAgPHVzZSB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy0zMCIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgPC9nPgogICAgPGcgaWQ9Inl0aWNrXzIiPgogICAgIDxnIGlkPSJsaW5lMmRfNSI+CiAgICAgIDxnPgogICAgICAgPHVzZSBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuODsiIHg9IjI0LjE2MjUiIHhsaW5rOmhyZWY9IiNtYjA0ZGU1YjVlNyIgeT0iMzIyLjc5OTkzOCIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzUiPgogICAgICA8IS0tIDEgLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwLjggMzI2LjU5OTE1NylzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSA3OTQgNTMxIApMIDE4MjUgNTMxIApMIDE4MjUgNDA5MSAKTCA3MDMgMzg2NiAKTCA3MDMgNDQ0MSAKTCAxODE5IDQ2NjYgCkwgMjQ1MCA0NjY2IApMIDI0NTAgNTMxIApMIDM0ODEgNTMxIApMIDM0ODEgMCAKTCA3OTQgMCAKTCA3OTQgNTMxIAp6CiIgaWQ9IkRlamFWdVNhbnMtMzEiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTMxIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyBpZD0ieXRpY2tfMyI+CiAgICAgPGcgaWQ9ImxpbmUyZF82Ij4KICAgICAgPGc+CiAgICAgICA8dXNlIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIgeD0iMjQuMTYyNSIgeGxpbms6aHJlZj0iI21iMDRkZTViNWU3IiB5PSIyNjMuMjg4OTM5Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICAgPGcgaWQ9InRleHRfNiI+CiAgICAgIDwhLS0gMiAtLT4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTAuOCAyNjcuMDg4MTU4KXNjYWxlKDAuMSAtMC4xKSI+CiAgICAgICA8ZGVmcz4KICAgICAgICA8cGF0aCBkPSJNIDEyMjggNTMxIApMIDM0MzEgNTMxIApMIDM0MzEgMCAKTCA0NjkgMCAKTCA0NjkgNTMxIApRIDgyOCA5MDMgMTQ0OCAxNTI5IApRIDIwNjkgMjE1NiAyMjI4IDIzMzggClEgMjUzMSAyNjc4IDI2NTEgMjkxNCAKUSAyNzcyIDMxNTAgMjc3MiAzMzc4IApRIDI3NzIgMzc1MCAyNTExIDM5ODQgClEgMjI1MCA0MjE5IDE4MzEgNDIxOSAKUSAxNTM0IDQyMTkgMTIwNCA0MTE2IApRIDg3NSA0MDEzIDUwMCAzODAzIApMIDUwMCA0NDQxIApRIDg4MSA0NTk0IDEyMTIgNDY3MiAKUSAxNTQ0IDQ3NTAgMTgxOSA0NzUwIApRIDI1NDQgNDc1MCAyOTc1IDQzODcgClEgMzQwNiA0MDI1IDM0MDYgMzQxOSAKUSAzNDA2IDMxMzEgMzI5OCAyODczIApRIDMxOTEgMjYxNiAyOTA2IDIyNjYgClEgMjgyOCAyMTc1IDI0MDkgMTc0MiAKUSAxOTkxIDEzMDkgMTIyOCA1MzEgCnoKIiBpZD0iRGVqYVZ1U2Fucy0zMiIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtMzIiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgIDwvZz4KICAgIDxnIGlkPSJ5dGlja180Ij4KICAgICA8ZyBpZD0ibGluZTJkXzciPgogICAgICA8Zz4KICAgICAgIDx1c2Ugc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjg7IiB4PSIyNC4xNjI1IiB4bGluazpocmVmPSIjbWIwNGRlNWI1ZTciIHk9IjIwMy43Nzc5NCIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzciPgogICAgICA8IS0tIDMgLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwLjggMjA3LjU3NzE1OSlzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSAyNTk3IDI1MTYgClEgMzA1MCAyNDE5IDMzMDQgMjExMiAKUSAzNTU5IDE4MDYgMzU1OSAxMzU2IApRIDM1NTkgNjY2IDMwODQgMjg3IApRIDI2MDkgLTkxIDE3MzQgLTkxIApRIDE0NDEgLTkxIDExMzAgLTMzIApRIDgxOSAyNSA0ODggMTQxIApMIDQ4OCA3NTAgClEgNzUwIDU5NyAxMDYyIDUxOSAKUSAxMzc1IDQ0MSAxNzE2IDQ0MSAKUSAyMzA5IDQ0MSAyNjIwIDY3NSAKUSAyOTMxIDkwOSAyOTMxIDEzNTYgClEgMjkzMSAxNzY5IDI2NDIgMjAwMSAKUSAyMzUzIDIyMzQgMTgzOCAyMjM0IApMIDEyOTQgMjIzNCAKTCAxMjk0IDI3NTMgCkwgMTg2MyAyNzUzIApRIDIzMjggMjc1MyAyNTc1IDI5MzkgClEgMjgyMiAzMTI1IDI4MjIgMzQ3NSAKUSAyODIyIDM4MzQgMjU2NyA0MDI2IApRIDIzMTMgNDIxOSAxODM4IDQyMTkgClEgMTU3OCA0MjE5IDEyODEgNDE2MiAKUSA5ODQgNDEwNiA2MjggMzk4OCAKTCA2MjggNDU1MCAKUSA5ODggNDY1MCAxMzAyIDQ3MDAgClEgMTYxNiA0NzUwIDE4OTQgNDc1MCAKUSAyNjEzIDQ3NTAgMzAzMSA0NDIzIApRIDM0NTAgNDA5NyAzNDUwIDM1NDEgClEgMzQ1MCAzMTUzIDMyMjggMjg4NiAKUSAzMDA2IDI2MTkgMjU5NyAyNTE2IAp6CiIgaWQ9IkRlamFWdVNhbnMtMzMiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTMzIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyBpZD0ieXRpY2tfNSI+CiAgICAgPGcgaWQ9ImxpbmUyZF84Ij4KICAgICAgPGc+CiAgICAgICA8dXNlIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC44OyIgeD0iMjQuMTYyNSIgeGxpbms6aHJlZj0iI21iMDRkZTViNWU3IiB5PSIxNDQuMjY2OTQxIi8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICAgPGcgaWQ9InRleHRfOCI+CiAgICAgIDwhLS0gNCAtLT4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTAuOCAxNDguMDY2MTYpc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgIDxkZWZzPgogICAgICAgIDxwYXRoIGQ9Ik0gMjQxOSA0MTE2IApMIDgyNSAxNjI1IApMIDI0MTkgMTYyNSAKTCAyNDE5IDQxMTYgCnoKTSAyMjUzIDQ2NjYgCkwgMzA0NyA0NjY2IApMIDMwNDcgMTYyNSAKTCAzNzEzIDE2MjUgCkwgMzcxMyAxMTAwIApMIDMwNDcgMTEwMCAKTCAzMDQ3IDAgCkwgMjQxOSAwIApMIDI0MTkgMTEwMCAKTCAzMTMgMTEwMCAKTCAzMTMgMTcwOSAKTCAyMjUzIDQ2NjYgCnoKIiBpZD0iRGVqYVZ1U2Fucy0zNCIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDwvZGVmcz4KICAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtMzQiLz4KICAgICAgPC9nPgogICAgIDwvZz4KICAgIDwvZz4KICAgIDxnIGlkPSJ5dGlja182Ij4KICAgICA8ZyBpZD0ibGluZTJkXzkiPgogICAgICA8Zz4KICAgICAgIDx1c2Ugc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjg7IiB4PSIyNC4xNjI1IiB4bGluazpocmVmPSIjbWIwNGRlNWI1ZTciIHk9Ijg0Ljc1NTk0MiIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzkiPgogICAgICA8IS0tIDUgLS0+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwLjggODguNTU1MTYpc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgIDxkZWZzPgogICAgICAgIDxwYXRoIGQ9Ik0gNjkxIDQ2NjYgCkwgMzE2OSA0NjY2IApMIDMxNjkgNDEzNCAKTCAxMjY5IDQxMzQgCkwgMTI2OSAyOTkxIApRIDE0MDYgMzAzOCAxNTQzIDMwNjEgClEgMTY4MSAzMDg0IDE4MTkgMzA4NCAKUSAyNjAwIDMwODQgMzA1NiAyNjU2IApRIDM1MTMgMjIyOCAzNTEzIDE0OTcgClEgMzUxMyA3NDQgMzA0NCAzMjYgClEgMjU3NSAtOTEgMTcyMiAtOTEgClEgMTQyOCAtOTEgMTEyMyAtNDEgClEgODE5IDkgNDk0IDEwOSAKTCA0OTQgNzQ0IApRIDc3NSA1OTEgMTA3NSA1MTYgClEgMTM3NSA0NDEgMTcwOSA0NDEgClEgMjI1MCA0NDEgMjU2NSA3MjUgClEgMjg4MSAxMDA5IDI4ODEgMTQ5NyAKUSAyODgxIDE5ODQgMjU2NSAyMjY4IApRIDIyNTAgMjU1MyAxNzA5IDI1NTMgClEgMTQ1NiAyNTUzIDEyMDQgMjQ5NyAKUSA5NTMgMjQ0MSA2OTEgMjMyMiAKTCA2OTEgNDY2NiAKegoiIGlkPSJEZWphVnVTYW5zLTM1IiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICAgPC9kZWZzPgogICAgICAgPHVzZSB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy0zNSIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgPC9nPgogICAgPGcgaWQ9Inl0aWNrXzciPgogICAgIDxnIGlkPSJsaW5lMmRfMTAiPgogICAgICA8Zz4KICAgICAgIDx1c2Ugc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjg7IiB4PSIyNC4xNjI1IiB4bGluazpocmVmPSIjbWIwNGRlNWI1ZTciIHk9IjI1LjI0NDk0MyIvPgogICAgICA8L2c+CiAgICAgPC9nPgogICAgIDxnIGlkPSJ0ZXh0XzEwIj4KICAgICAgPCEtLSA2IC0tPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMC44IDI5LjA0NDE2MSlzY2FsZSgwLjEgLTAuMSkiPgogICAgICAgPGRlZnM+CiAgICAgICAgPHBhdGggZD0iTSAyMTEzIDI1ODQgClEgMTY4OCAyNTg0IDE0MzkgMjI5MyAKUSAxMTkxIDIwMDMgMTE5MSAxNDk3IApRIDExOTEgOTk0IDE0MzkgNzAxIApRIDE2ODggNDA5IDIxMTMgNDA5IApRIDI1MzggNDA5IDI3ODYgNzAxIApRIDMwMzQgOTk0IDMwMzQgMTQ5NyAKUSAzMDM0IDIwMDMgMjc4NiAyMjkzIApRIDI1MzggMjU4NCAyMTEzIDI1ODQgCnoKTSAzMzY2IDQ1NjMgCkwgMzM2NiAzOTg4IApRIDMxMjggNDEwMCAyODg2IDQxNTkgClEgMjY0NCA0MjE5IDI0MDYgNDIxOSAKUSAxNzgxIDQyMTkgMTQ1MSAzNzk3IApRIDExMjIgMzM3NSAxMDc1IDI1MjIgClEgMTI1OSAyNzk0IDE1MzcgMjkzOSAKUSAxODE2IDMwODQgMjE1MCAzMDg0IApRIDI4NTMgMzA4NCAzMjYxIDI2NTcgClEgMzY2OSAyMjMxIDM2NjkgMTQ5NyAKUSAzNjY5IDc3OCAzMjQ0IDM0MyAKUSAyODE5IC05MSAyMTEzIC05MSAKUSAxMzAzIC05MSA4NzUgNTI5IApRIDQ0NyAxMTUwIDQ0NyAyMzI4IApRIDQ0NyAzNDM0IDk3MiA0MDkyIApRIDE0OTcgNDc1MCAyMzgxIDQ3NTAgClEgMjYxOSA0NzUwIDI4NjEgNDcwMyAKUSAzMTAzIDQ2NTYgMzM2NiA0NTYzIAp6CiIgaWQ9IkRlamFWdVNhbnMtMzYiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8L2RlZnM+CiAgICAgICA8dXNlIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTM2Ii8+CiAgICAgIDwvZz4KICAgICA8L2c+CiAgICA8L2c+CiAgIDwvZz4KICAgPGcgaWQ9InBhdGNoXzYiPgogICAgPHBhdGggZD0iTSAyNC4xNjI1IDM4Mi4zMTA5MzggCkwgMjQuMTYyNSAxMC44IAoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLWxpbmVjYXA6c3F1YXJlO3N0cm9rZS1saW5lam9pbjptaXRlcjtzdHJva2Utd2lkdGg6MC44OyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF83Ij4KICAgIDxwYXRoIGQ9Ik0gNTU1LjIgMzgyLjMxMDkzOCAKTCA1NTUuMiAxMC44IAoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLWxpbmVjYXA6c3F1YXJlO3N0cm9rZS1saW5lam9pbjptaXRlcjtzdHJva2Utd2lkdGg6MC44OyIvPgogICA8L2c+CiAgIDxnIGlkPSJwYXRjaF84Ij4KICAgIDxwYXRoIGQ9Ik0gMjQuMTYyNSAzODIuMzEwOTM4IApMIDU1NS4yIDM4Mi4zMTA5MzggCiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2U6IzAwMDAwMDtzdHJva2UtbGluZWNhcDpzcXVhcmU7c3Ryb2tlLWxpbmVqb2luOm1pdGVyO3N0cm9rZS13aWR0aDowLjg7Ii8+CiAgIDwvZz4KICAgPGcgaWQ9InBhdGNoXzkiPgogICAgPHBhdGggZD0iTSAyNC4xNjI1IDEwLjggCkwgNTU1LjIgMTAuOCAKIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZTojMDAwMDAwO3N0cm9rZS1saW5lY2FwOnNxdWFyZTtzdHJva2UtbGluZWpvaW46bWl0ZXI7c3Ryb2tlLXdpZHRoOjAuODsiLz4KICAgPC9nPgogICA8ZyBpZD0ibGVnZW5kXzEiPgogICAgPGcgaWQ9InBhdGNoXzEwIj4KICAgICA8cGF0aCBkPSJNIDMxLjE2MjUgMzMuNDc4MTI1IApMIDg2LjAyODEyNSAzMy40NzgxMjUgClEgODguMDI4MTI1IDMzLjQ3ODEyNSA4OC4wMjgxMjUgMzEuNDc4MTI1IApMIDg4LjAyODEyNSAxNy44IApRIDg4LjAyODEyNSAxNS44IDg2LjAyODEyNSAxNS44IApMIDMxLjE2MjUgMTUuOCAKUSAyOS4xNjI1IDE1LjggMjkuMTYyNSAxNy44IApMIDI5LjE2MjUgMzEuNDc4MTI1IApRIDI5LjE2MjUgMzMuNDc4MTI1IDMxLjE2MjUgMzMuNDc4MTI1IAp6CiIgc3R5bGU9ImZpbGw6I2ZmZmZmZjtvcGFjaXR5OjAuODtzdHJva2U6I2NjY2NjYztzdHJva2UtbGluZWpvaW46bWl0ZXI7Ii8+CiAgICA8L2c+CiAgICA8ZyBpZD0icGF0Y2hfMTEiPgogICAgIDxwYXRoIGQ9Ik0gMzMuMTYyNSAyNy4zOTg0MzggCkwgNTMuMTYyNSAyNy4zOTg0MzggCkwgNTMuMTYyNSAyMC4zOTg0MzggCkwgMzMuMTYyNSAyMC4zOTg0MzggCnoKIiBzdHlsZT0iZmlsbDojMWY3N2I0OyIvPgogICAgPC9nPgogICAgPGcgaWQ9InRleHRfMTEiPgogICAgIDwhLS0gdG90YWwgLS0+CiAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNjEuMTYyNSAyNy4zOTg0Mzgpc2NhbGUoMC4xIC0wLjEpIj4KICAgICAgPGRlZnM+CiAgICAgICA8cGF0aCBkPSJNIDExNzIgNDQ5NCAKTCAxMTcyIDM1MDAgCkwgMjM1NiAzNTAwIApMIDIzNTYgMzA1MyAKTCAxMTcyIDMwNTMgCkwgMTE3MiAxMTUzIApRIDExNzIgNzI1IDEyODkgNjAzIApRIDE0MDYgNDgxIDE3NjYgNDgxIApMIDIzNTYgNDgxIApMIDIzNTYgMCAKTCAxNzY2IDAgClEgMTEwMCAwIDg0NyAyNDggClEgNTk0IDQ5NyA1OTQgMTE1MyAKTCA1OTQgMzA1MyAKTCAxNzIgMzA1MyAKTCAxNzIgMzUwMCAKTCA1OTQgMzUwMCAKTCA1OTQgNDQ5NCAKTCAxMTcyIDQ0OTQgCnoKIiBpZD0iRGVqYVZ1U2Fucy03NCIgdHJhbnNmb3JtPSJzY2FsZSgwLjAxNTYyNSkiLz4KICAgICAgIDxwYXRoIGQ9Ik0gMTk1OSAzMDk3IApRIDE0OTcgMzA5NyAxMjI4IDI3MzYgClEgOTU5IDIzNzUgOTU5IDE3NDcgClEgOTU5IDExMTkgMTIyNiA3NTggClEgMTQ5NCAzOTcgMTk1OSAzOTcgClEgMjQxOSAzOTcgMjY4NyA3NTkgClEgMjk1NiAxMTIyIDI5NTYgMTc0NyAKUSAyOTU2IDIzNjkgMjY4NyAyNzMzIApRIDI0MTkgMzA5NyAxOTU5IDMwOTcgCnoKTSAxOTU5IDM1ODQgClEgMjcwOSAzNTg0IDMxMzcgMzA5NiAKUSAzNTY2IDI2MDkgMzU2NiAxNzQ3IApRIDM1NjYgODg4IDMxMzcgMzk4IApRIDI3MDkgLTkxIDE5NTkgLTkxIApRIDEyMDYgLTkxIDc3OSAzOTggClEgMzUzIDg4OCAzNTMgMTc0NyAKUSAzNTMgMjYwOSA3NzkgMzA5NiAKUSAxMjA2IDM1ODQgMTk1OSAzNTg0IAp6CiIgaWQ9IkRlamFWdVNhbnMtNmYiIHRyYW5zZm9ybT0ic2NhbGUoMC4wMTU2MjUpIi8+CiAgICAgICA8cGF0aCBkPSJNIDIxOTQgMTc1OSAKUSAxNDk3IDE3NTkgMTIyOCAxNjAwIApRIDk1OSAxNDQxIDk1OSAxMDU2IApRIDk1OSA3NTAgMTE2MSA1NzAgClEgMTM2MyAzOTEgMTcwOSAzOTEgClEgMjE4OCAzOTEgMjQ3NyA3MzAgClEgMjc2NiAxMDY5IDI3NjYgMTYzMSAKTCAyNzY2IDE3NTkgCkwgMjE5NCAxNzU5IAp6Ck0gMzM0MSAxOTk3IApMIDMzNDEgMCAKTCAyNzY2IDAgCkwgMjc2NiA1MzEgClEgMjU2OSAyMTMgMjI3NSA2MSAKUSAxOTgxIC05MSAxNTU2IC05MSAKUSAxMDE5IC05MSA3MDEgMjExIApRIDM4NCA1MTMgMzg0IDEwMTkgClEgMzg0IDE2MDkgNzc5IDE5MDkgClEgMTE3NSAyMjA5IDE5NTkgMjIwOSAKTCAyNzY2IDIyMDkgCkwgMjc2NiAyMjY2IApRIDI3NjYgMjY2MyAyNTA1IDI4ODAgClEgMjI0NCAzMDk3IDE3NzIgMzA5NyAKUSAxNDcyIDMwOTcgMTE4NyAzMDI1IApRIDkwMyAyOTUzIDY0MSAyODA5IApMIDY0MSAzMzQxIApRIDk1NiAzNDYzIDEyNTMgMzUyMyAKUSAxNTUwIDM1ODQgMTgzMSAzNTg0IApRIDI1OTEgMzU4NCAyOTY2IDMxOTAgClEgMzM0MSAyNzk3IDMzNDEgMTk5NyAKegoiIGlkPSJEZWphVnVTYW5zLTYxIiB0cmFuc2Zvcm09InNjYWxlKDAuMDE1NjI1KSIvPgogICAgICA8L2RlZnM+CiAgICAgIDx1c2UgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNzQiLz4KICAgICAgPHVzZSB4PSIzOS4yMDg5ODQiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTZmIi8+CiAgICAgIDx1c2UgeD0iMTAwLjM5MDYyNSIgeGxpbms6aHJlZj0iI0RlamFWdVNhbnMtNzQiLz4KICAgICAgPHVzZSB4PSIxMzkuNTk5NjA5IiB4bGluazpocmVmPSIjRGVqYVZ1U2Fucy02MSIvPgogICAgICA8dXNlIHg9IjIwMC44Nzg5MDYiIHhsaW5rOmhyZWY9IiNEZWphVnVTYW5zLTZjIi8+CiAgICAgPC9nPgogICAgPC9nPgogICA8L2c+CiAgPC9nPgogPC9nPgogPGRlZnM+CiAgPGNsaXBQYXRoIGlkPSJwMDhlNWNmOTg1YiI+CiAgIDxyZWN0IGhlaWdodD0iMzcxLjUxMDkzOCIgd2lkdGg9IjUzMS4wMzc1IiB4PSIyNC4xNjI1IiB5PSIxMC44Ii8+CiAgPC9jbGlwUGF0aD4KIDwvZGVmcz4KPC9zdmc+Cg==)\n",
    "\n",
    "Way to come through! There are many ways to write code for this task. However, concatenating the tables with a key provides a hierarchical index that can be used for grouping. Once grouped, you can average the groups and create plots. You were able to find out that September had the highest average invoice total.\n",
    "\n",
    "## Using the append method\n",
    "The `.concat()` method is excellent when you need a lot of control over how concatenation is performed. However, if you do not need as much control, then the .append() method is another option. You'll try this method out by appending the track lists together from different Metallica albums. From there, you will merge it with the invoice_items table to determine which track sold the most.\n",
    "\n",
    "* Use the `.append()` method to combine (in this order) `tracks_ride`, `tracks_master`, and `tracks_st` together vertically, and save to `metallica_tracks`.\n",
    "* Merge `metallica_tracks` and `invoice_items` on tid with an inner join, and save to `tracks_invoices`.\n",
    "* For each tid and name in `tracks_invoices`, sum the quantity sold column, and save as `tracks_sold`.\n",
    "* Sort `tracks_sold` in descending order by the quantity column, and print the table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f63a91e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the .append() method to combine the tracks tables\n",
    "metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)\n",
    "\n",
    "# Merge metallica_tracks and invoice_items\n",
    "tracks_invoices = metallica_tracks.merge(invoice_items, on='tid')\n",
    "\n",
    "# For each tid and name sum the quantity sold\n",
    "tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity':'sum'})\n",
    "\n",
    "# Sort in decending order by quantity and print the results\n",
    "print(tracks_sold.sort_values(['quantity'], ascending=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0aaacdef",
   "metadata": {},
   "source": [
    "Great work! Even though .append() is less flexible, it's also simpler than .concat(). It looks like Battery, and For Whom The Bell Tolls were the most sold tracks.\n",
    "\n",
    "## Validating a merge\n",
    "You have been given 2 tables, artists, and albums. Use the IPython shell to merge them using `artists.merge(albums, on='artid').head()`. Adjust the validate argument to answer which statement is False.\n",
    "\n",
    "* You can use 'many_to_many' without an error, since there is a duplicate key in one of the tables.\n",
    "\n",
    "* You can use 'one_to_many' without error, since there is a duplicate key in the right table.\n",
    "\n",
    "* **You can use 'many_to_one' without an error, since there is a duplicate key in the left table.**\n",
    "\n",
    "That's correct! This statement is false. There is a duplicate value in the artid column in the albums table, which is the right table in this merge. Therefore, setting validate equal to 'many_to_one' or 'one_to_one' will raise an error, making this statement false.\n",
    "\n",
    "## Concatenate and merge to find common songs\n",
    "The senior leadership of the streaming service is requesting your help again. You are given the historical files for a popular playlist in the classical music genre in 2018 and 2019. Additionally, you are given a similar set of files for the most popular pop music genre playlist on the streaming service in 2018 and 2019. Your goal is to concatenate the respective files to make a large classical playlist table and overall popular music table. Then filter the classical music table using a semi join to return only the most popular classical music tracks.\n",
    "\n",
    "* Concatenate the `classic_18` and `classic_19` tables vertically where the index goes from 0 to n-1, and save to `classic_18_19`.\n",
    "* Concatenate the `pop_18` and `pop_19` tables vertically where the index goes from 0 to n-1, and save to `pop_18_19`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db355ed8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate the classic tables vertically\n",
    "classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)\n",
    "\n",
    "# Concatenate the pop tables vertically\n",
    "pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22974c0b",
   "metadata": {},
   "source": [
    "* With `classic_18_19` on the left, merge it with `pop_18_19` on tid using an inner join.\n",
    "* Use `isin()` to filter `classic_18_19` where tid is in `classic_pop`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b1bd39b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge classic_18_19 with pop_18_19\n",
    "classic_pop = classic_18_19.merge(pop_18_19, on='tid')\n",
    "\n",
    "# Using .isin(), filter classic_18_19 rows where tid is in classic_pop\n",
    "popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]\n",
    "\n",
    "# Print popular chart\n",
    "print(popular_classic)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1c1b792",
   "metadata": {},
   "source": [
    "Excellent work! In this exercise, you demonstrated many of the concepts discussed in this chapter, including concatenation, and semi joins. You now have experience combining data vertically and using semi- and anti joins. Time to move on to the next chapter!"
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
