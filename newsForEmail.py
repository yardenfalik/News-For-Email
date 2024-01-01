from bs4 import BeautifulSoup
import feedparser
import smtplib, ssl, email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

today = date.today()

sources = {"ynet":"https://www.ynet.co.il/Integration/StoryRss2.xml", "walla":"https://rss.walla.co.il/feed/1?type=main", "mako": "https://rcs.mako.co.il/rss/MainSliderRss.xml"}

url = sources["mako"]

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
    <title>Document</title>
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
</body>
</html>

"""

sender_email = "your gmail address"
receiver_email = email
password = "your gmail password"

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