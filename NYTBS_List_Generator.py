import time, requests, json, configparser


# This function takes a dictionary of display names and encoded names of the best sellers
# lists the user wants to access along with the api key and a list 
# of metadata tags delimitating what information should be returned. It then returns
# that information in a list of dictionaries.

def Query_NYT_BS(e_name, api_key, metadata):
    item_list = []
    
    # Send request to api, check if it is a valid query, and create a json object or write the
    # error to the log file.

    book_req = requests.get("https://api.nytimes.com/svc/books/v3/lists/currnet/" + e_name + '?api-key=' + api_key)
    if book_req.status_code == 200:
        book_req = book_req.json()

        # We loop through each of the items in the results and then loop through each metadata tag and add that
        # data to a dictionary which, once all the tags have been looped through, is added to a list of total
        # results and then reset. Once all the items in the results have been looped through, the completed
        # list is returned to the function call.
        
        for i in book_req["results"]:
            if i == "books":
                for item in book_req["results"]["books"]:
                    item_dict = {}
                    for data in metadata:
                        item_dict.update({data:item[data]})
                    item_list.append(item_dict)
        return item_list
    

    else:
        t = time.localtime()
        with open("NYTBS_log.txt", "a", encoding='utf-8') as file:
            file.write("Failed. Request status code: " + str(book_req.status_code) + ". " + e_name + ". \t\t\t TIME:" + str(time.strftime("%H:%M:%S", t)) + "\n")
            file.close()
    return item_list


# This function writes the data pertaining to a best seller list to a text file.
# It requires the list name, the format it should write in, and the metadata dictionary
# relating to that list name.
def write_to_file(list_of_metadata_dicts, list_name, data_key):

    # This empties the current files containing best_seller data
    if "save_past_lists" not in data_key:
        empty = open('%s.txt' %list_name, 'w')
        empty.close()
        empty = open('%s_html.txt' %list_name, 'w')
        empty.close()
        empty = open('%s_csv.txt' %list_name, 'w')
        empty.close()
    else:
        # Move content to legacy files.
        content = open('%s.txt' %list_name, 'r').read()
        move = open('%s_legacy.txt' %list_name, 'a')
        move.write(content)
        move.close()
        content.close()

        content = open('%s_html.txt' %list_name, 'r').read()
        move = open('%s_html_legacy.txt' %list_name, 'a')
        move.write(content)
        move.close()
        content.close()

        content = open('%s_csv.txt' %list_name, 'r').read()
        move = open('%s_csv_legacy.txt' %list_name, 'a')
        move.write(content)
        move.close()
        content.close()

        # Erase data in default files.
        empty = open('%s.txt' %list_name, 'w')
        empty.close()
        empty = open('%s_html.txt' %list_name, 'w')
        empty.close()
        empty = open('%s_csv.txt' %list_name, 'w')
        empty.close()

    
    # This loop goes through each dictionary in the list
    for dictionary in list_of_metadata_dicts:

        if "text" in data_key:

            # establish an empty list object to which each items information will be written in format
            list_info = []
        
            # This loop goes through all the values (data tags i.e. "author", "title", etc.) in the dictionary
            # and appends the data to a list.
            for key in dictionary:
                list_info.append(str(key) + ': ' + str(dictionary[key]) + '\n')
                
            # write the content of the list to a text file with the same name as the best seller list name.
            with open('%s.txt' %list_name, 'a', encoding='utf-8') as f:
                f.writelines(list_info)
                f.write('\n')
            f.close()

        if "html" in data_key:
            
            # establish an empty list object to which each items information will be written in format
            list_info = []

            # This loop goes through all the metadata tags and values and asigns them to variabels of the same
            # or similar name. They are then used to create an html <div> container populated with that
            # information which is appended to a list.
            for key in dictionary:
                if key == "title":
                    title = dictionary[key]
                if key == "author":
                    author = dictionary[key]
                if key == "publisher":
                    publisher = dictionary[key]
                if key == "weeks_on_list":
                    weeks_on_list = dictionary[key]
                if key == "price":
                    price = dictionary[key]
                if key == "description":
                    description = dictionary[key]
                if key == "book_image":
                    img = dictionary[key]
                    
            list_info.append("<div align=\"center\"><h3>" + title.upper() + "<br>by<br>" + author + "<br>Weeks on List: " + str(weeks_on_list) + "</h3><b>" + description + "</b><br><br><a href=\"https://sjcpl.bibliocommons.com/v2/search?query=" + title.replace(" ", "+").lower() + "&searchType=title\"><img type=\"image\" height=\"200\" width=\"150\" src=\"" + img + "\"</img></a></div>")
                
            # write the content of the list to a text file with the same name as the best seller list name.
            with open('%s_html.txt' %list_name, 'a', encoding='utf-8') as f:
                f.writelines(list_info)
                f.write('\n')
            f.close()

        if "csv" in data_key:

            # establish an empty list object to which each items information will be written in format
            list_info = []
            
            # This loop goes through all the metadata tags and values and appends it to a list in csv format.
            for key in dictionary:
                list_info.append(str(dictionary[key]) + ', ')
                
            # write the content of the list to a text file with the same name as the best seller list name.
            with open('%s_csv.txt' %list_name, 'a', encoding='utf-8') as f:
                f.writelines(list_info)
                f.write('\n')
            f.close()
        
          
#START HERE
    
# Initiate configparser and make a configparser file object from the .ini file located in
# the same directory as this script.
config = configparser.ConfigParser()
config.read("NYTBS.ini")



# Read and assign data from .ini file into relevant dictionaries.
for i in config.sections():
    if i == "API":
        api = dict(config.items(i))
    if i == "METADATA":
        metadata = dict(config.items(i))
    if i == "BS_LISTS":
        list_data = dict(config.items(i))
    if i == "DATA_STRUCTURE":
        data_form = dict(config.items(i))
    if i == "MISC":
        misc = dict(config.items(i))

        
# Loop through the metadata dictionary and append the True values to a list.
metadata_key = []
for key in metadata:
    if metadata[key] == "True":
      metadata_key.append(key)

data_key = []
for key in data_form:
    if data_form[key] == "True":
      data_key.append(key)


# Loop through the dictionary of best seller lists, passing each encoded name to Query_NYT_BS
# function and storing the data deliminated by the metadata dictionary in a dictionary.

for i in list_data:
	list_of_metadata_dicts = Query_NYT_BS(list_data[i], api['api key'], metadata_key)
	write_to_file(list_of_metadata_dicts, list_data[i], data_key)

        # In order to avoid 429 error codes NYT recommends a wait time of 6 secs between requests.
	time.sleep(6)


t = time.localtime()
with open("NYTBS_log.txt", "a", encoding='utf-8') as file:
    file.write("STATUS: Completed Requests\t\tTIME:" + time.strftime("%H:%M:%S", t) + "\n")
    file.close()

print("Done.")
