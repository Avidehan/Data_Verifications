In this task I was asked to perform web scraping from "zillow.com" using selenium, from a URL of an apartment at a specific address.
The specific requirement is to take the data from the graph and not from other objects on the web-page*

The challenges posed by this task definition were as follows:

The graph size was different for each address.
* the site blocked access by selenium. in any access the site would not have raised the graph
* The structure of the web page itself has changed depending on the status of the apartment, whether it has been “sold” or is “for sale”.
* The key of the requested data within the DOM was an unknown variable

In order to solve these problems I have adopted the following strategies:
 * Check the graph at regular intervals and remove duplicates
* Sending various arguments in headers and using a user agent
* Building various functions that correspond to both the status of "for sale" and the status of "sold"
* Using parent-child tags.
* When the site does manage to identify the access as a robot, a blockage appeared and I replaced the IP with a plugin that I installed locally on the computer.
* In case of blockage by captcha, a message will be issued, and an ip must be replaced
* I added options that simulate as close as possible to a normal person.




In addition, I performed parallel tests using the python library to directly run the GUI



* The complete task definition is in the file… ..
