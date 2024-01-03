from bs4 import BeautifulSoup
import feedparser
import smtplib, ssl, email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
import json


f = open('emailData.json')
emaiData = json.load(f)

sources = open('newsSources.json')
sources = json.load(sources)

today = date.today()

print("Available sources:")
for source in sources.keys():
    print(source)

#aveilable sources: ynet, walla, mako, nytimes.
source = input("Select your news source: ")

url = sources[source]

email = input("Enter your email: ")

print("Hold on, we're gathering your news...")

feed = feedparser.parse(url)

articles = []

for item in feed.entries:
    soup = BeautifulSoup(item.summary, 'html.parser')
    img = soup.find_all('img')

    if(len(img) == 0):
        article = f"""
        <div class="article">
            <h1>{item.title}</h1>
            <p>{item.published}</p>
            <p>{soup.get_text()}</p>
            <a href="{item.link}">Read More</a>
        </div>
        <hr>
        """
    else:
        article = f"""
        <div class="article">
            <h1>{item.title}</h1>
            <p>{item.published}</p>
            <img src="{img[0]['src']}">
            <p>{soup.get_text()}</p>
            <a href="{item.link}">Read More</a>
        </div>
        <hr>
        """

    articles.append(article)

    if len(articles) == 5:
        break


html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }
        img{
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <main>
    """+ "".join(articles) +"""
    </main>
    <p>News from """ + source + """</p>
</body>
</html>

"""

sender_email = emaiData["address"]
receiver_email = email
password = emaiData["password"]

#Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "your news for " + str(today)
msg["From"] = sender_email
msg["To"] = receiver_email

part = MIMEText(html, "html")
msg.attach(part)

# Create secure SMTP connection and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("your news are waiting for you in your email inbox!")