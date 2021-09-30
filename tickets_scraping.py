from requests_html import HTMLSession
from bs4 import BeautifulSoup
import smtplib
import time

"""----------------------------------------------------------------------------------
        !!! VARIABLES THAT HAS TO BE STATED BY THE USER !!! 
"""
# link to the website with tickets
url = 'https://tickets.manutd.com/en-GB/categories/home-tickets'

# Playing teams that we want to be on a ticket (not case sensitive)
TEAMS = "manchester united v west ham united (carabao cup)"

# Email FROM which the message will be sent
# HERE I USE GMAIL AS AN EXAMPLE, but in order to use it some account's setting must be changed. One way to do
# it is to allow your gmail account connect with less secure apps (it can be done by changing the button "off"
# to "on" at My account >>> Less secure app access.
# If you do have 2 factor authentication and would like to keep it that way, then you need to generate an app
# the password at My account >>> App passwords
sender = 'WhereToSend@gmail.com'
password = "PASSWORD42069"

# Receiver email
# if there are several receivers this should be changed to a list of strings
receiver = 'FromWhom@gmail.com'

# message that will be sent if the button says "Buy Tickets"
message = "Subject: Tickets are on sale! \n\nLink: {}\n{} are playing and the button is 'Buy Tickets'!".format(url, TEAMS)

"""---------------------------------------------------------------------------------
"""
# creating empty lists to store values in them in the for-loop
teams_list = []
button_container_list = []


def initiate_connection():
    # rendering HTML
    session = HTMLSession()
    resp = session.get(url)
    resp.html.render()
    html = resp.html.html

    # parsing through the html and getting raw data for each ticket
    page_soup = BeautifulSoup(html, 'html.parser')
    tickets_containers_raw = page_soup.find_all("div", class_="dataItem")

    # getting info from the data containers and checking if there is a ticket for teams we want
    for tickets in tickets_containers_raw:
        # getting the names of the 2 playing teams
        teams = tickets.find(class_="small_text_d").text.strip().lower()
        # store them in the list
        teams_list.append(teams)
        # find info in button containers
        button_container = tickets.find(class_="small_button_a").text.strip().lower()
        # store them in a list
        button_container_list.append(button_container)

    # using dictionary comprehension to convert lists to dictionary
    teams_and_buttons = dict(zip(teams_list, button_container_list))

    for key in teams_and_buttons:
        if TEAMS in key and teams_and_buttons[key] == "buy tickets":
            send_email()
        else:
            pass


def send_email():
    # the first value in the brackets is email provider of the sender
    # and the second is the port number
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        # identifying with the email server we are using
        smtp.ehlo()
        # encrypt the traffic
        smtp.starttls()
        # identifying as an encrypted connection
        smtp.ehlo()

        # login to the mail server, email of a sender is the first variable
        # and password for that email, remember to use created password
        # if you use 2 factor Identification
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, message)


while True:
    initiate_connection()
    time.sleep(60)
