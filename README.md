# Webscraping football tickets
This program checks the contet of the HTML of the webpage with football tickets. 
If the ticket you want is there and is available to buy you will recieve a reminder on your email. 

## Installation of necessary packages and libraries

You need 2 libraries for this code to work: Requests_HTML and Beautiful Soup

(Use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.)
```bash
pip install requests-html
pip install bs4
```
from requests_html you need to import HTMLSession
from bs4 import Beautiful Soup


We also need to import smptlib module and time module
```python
import smptlib
import time
```

## Variables

There are 6 variables that must be stated in the beginning:
```python
# webpage that you want to scrape for the ticket info
url = "'https://tickets.example.com"

# name of the teams how they should be written on a ticket (not case sensitive)
TEAMS = "manchester united v west ham united"

# email FROM which the email would be send
sender = "Sender.example@gmail.com"

# email password from which the email would be send
password = "42069"

# to whom you want to send the message
receiver = "Receiver.example@gmail.com"

# text that will be send to the receiver
message = "Tickets are on sale, buy NOW!!!"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

