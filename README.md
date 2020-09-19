NYTBestSellerListGenerator

# ABOUT

This program was built to provide automated harvesting of 
best-seller information from the New York Times. 

It allows the user to generate text documents populated with 
information of their choice about the best-seller list(s) of 
their choice. 

This program is open source and open access. If you would like 
to modify this program, go nuts! If you want to distribute it, 
do your thang! I hope some of my work will help out.           


# REQUIREMENTS

This program was written in Python v3.8 and intended to be executed in that programming
language. However, these scripts may be run through most legacy python versions as long
as the following libraries have been installed:

- configparser
- json
- requests
- time

In order to function correctly, all files must stay in the same directory.

To install the latest version of python go to: https://www.python.org/.

These scripts require a nytimes.com developer api key which may be applied for here:
https://developer.nytimes.com/.


# Functionality

This collection of scripts uses the New York Times API in order to collect the latest
best-seller lists, and associated data, in a variety of mediums.*

Data collected includes:
- Title
- Author
- Isbn
- Cover Image Source
- Description
- Number of Weeks on the Bestseller List
- Link to Website Holdings of Item (Searched by ISBN)
- Etc. (See NYTBS.ini File for Full Fist)

Mediums Included:
- Graphic Novels and Manga
- Fiction (Hardcover and Paperback)
- Non-Fiction (Hardcover and Paperback)
- Picture Books
- Etc. (See NYTBS.ini File for Full Fist)

*Data accuracy is dependent on the updating and maintaining of the API.*


# What Exactly Do These Scripts Do

These scripts access a json file through the New York Times API, by using the python requests
library. 

That file is then parsed for information delineated in the NYTBS.ini file.

Then that data is then written to a text file for later use by the user.

These scripts produce multiple text files, one for each list in the NYTBS.ini file. These files
will show up in the source code directory.

These text files contain the best seller information. Data in these files can be written in html
for easy copy and paste website display.* These files are overwritten by default every time the
script is run.** 

*CSV format and basic formatted text files are currently under development.*

**An option to have previous files archived is currently under development.**


A simple log file is also created which includes information about the success of the query to the
API and a time stamp.***

***A more verbose logging system is currently under development.***
