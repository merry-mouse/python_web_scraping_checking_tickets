# python_web_scraping_checking_tickets
This program checks the contrnt of the HTML of the webpage with football tickets 
and if the ticket you want is there and is available to buy you will recieve a reminder on your email. 
## Installation of necessary packages and libraries
You need 2 libraries for this code to work: Requests_HTML and Beautiful Soup
-requests_html
-bs4
(can be installed using "$ pipenv install requests-html" and "$ pipenv install bs4")
```bash
pip install requests-html
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
1. url = webpage that you want to scrape for the ticket info
2. TEAMS = name of the teams how they should be written on a ticket (not case sensitive)
3. sender = email FROM which the email would be send
4. password = email password from which the email would be send
5. receiver = to whom you want to send the message
6. message = text that will be send to the receiver

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

