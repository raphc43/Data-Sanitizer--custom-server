# Data-Sanitizer--custom-server
This is an updated version of Data Sanitizer repo which basically utilizes python's built-in server to serve the data in a chart representation through chart.js.

# Purpose of the program?
Suppose you want to send mass emails, but the data you have also contains some emails that repeat 2 or more times. The file contains 5000 emails. So will 
you manually remove the repeated ones? Doing it manually will take weeks to months. Hence this program solves the issue by taking the data and outputing it in a 
unique form with stats. 

# How to use the program?
The repo consist of 6 total files, in which the main file is data_sanitizer.py

1 - Open CMD, navigate to the repo and issue 'python custom_server.py' command to launch the server.

2 - Then execute data_sanitizer.py file either by running it through a text editor or by directly clicking it.

3 - After a few seconds the file will return chart.html and after some more seconds the page will render a pie chart. 

# Why use a server?
The chart.html uses fetch API to get the data from stats.json, and fetch does not directly work with local directories, hence it requires a server to fetch files. 
Since the host is only one, fetching encounters no CORS issues, but I modified the server in order to expand the scope of the project. For example even after implementing React, fetch will have no problem in bypassing CORS
