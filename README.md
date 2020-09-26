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
best-seller lists, and associated data, in a variety of mediums.

Data collected includes:
- Title
- Author
- Isbn
- Cover Image Source
- Description
- Number of Weeks on the Bestseller List
- Etc. (See NYTBS.ini File for Full Fist)

Mediums Included:
- Graphic Novels and Manga
- Fiction (Hardcover and Paperback)
- Non-Fiction (Hardcover and Paperback)
- Picture Books
- Etc. (See NYTBS.ini File for Full Fist)

        Note: Data accuracy is dependent on the updating and maintaining of the API.


# What Exactly Do These Scripts Do

These scripts access a json file through the New York Times API, by using the python requests
library. 

That file is then parsed for information delineated in the NYTBS.ini file.

Then that data is then written to a text file for later use by the user.

These scripts produce multiple text files, one for each list in the NYTBS.ini file. These files
will show up in the source code directory.

These text files contain the best seller information. Data in these files can be written in html
for easy copy and paste website display. These files are overwritten by default every time the
script is run.

A simple log file is also created which includes information about the success of the query to the
API and a time stamp.

        Note: A more verbose logging system is currently under development.


# Set Up

In order for this script to work properly, you must complete the setup process.

Step 1 : Download the complete directory containing files:
    - LICENSE 
    - NYTBS.ini
    - README.dm
    - NYTBS_List_Generator.py

Step 2 : Open NYTBS.ini in a text editor and enter in your New York Times Developer API Key
         by replacing the 'your-api-key' value.
          
Step 3 : Go to the [METADATA] section and comment out (place the '#' symbol at the beginning
         of the line) any metadata you do not wish to capture.
         
Step 4 : Go to the [BS_LISTS] section and comment out any best seller lists you do not wish to
         capture.
         DO NOT CHANGE ANYTHING ELSE IN THIS SECTION.
         
Step 5 : Go to the [DATA_STRUCTURE] section and comment out the formats you do not wish to
         generate. The script will create a separate file for each format uncommented.
         
         Note: One the initial running of the script, the 'SAVE_PAST_LISTS' line must be
               commented out or set to False or a 'file not found' error will occur. After the
               initial running of the program this may be uncommented and set to True in order
               to save past lists.

Step 6 : Run the script 'NYTBS_List_Generatory.py'.
     
          Note: If the script executes successfully, a file for each of the lists uncommented
                in the NYTBS.ini file will be written in the directory.
                
# Contact
For any questions/concerns contact:

Sardinedude1dev@gmail.com

Please be patient as I am a human being with other things that occupy my time occasionally.
