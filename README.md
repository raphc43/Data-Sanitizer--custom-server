# Data-Sanitizer--custom-server
This is an updated version of Data Sanitizer repo which basically utilizes python's built-in server to serve the data in a chart representation through chart.js.

How to use the program?
The repo consist of 5 total files, in which the main file is data_sanitizer.py

1 - Open CMD and issue 'python -m http.server' command to launch the server.

2 - Then execute data_sanitizer.py file either by running it through a text editor or by directly clicking it.

3 - After a few seconds the file will return chart.html and after some more seconds the page will render a pie chart. 

Why use a server?
The chart.html uses fetch API to get the data from stats.json, and fetch does not directly work with local directories, hence it requires a server to fetch files. 
And since the host is only one, fetching encounters no CORS issues.
