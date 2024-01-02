# News-For-Email 📬
A Python script that will send to your email 5 news articles so you don't miss anything.

## Introduction
This Python script will retrieve news articles from a specified source. It will select 5 articles to send to your email address. The script allows you to customize which news source it pulls articles.

## Requirements
1. To run the code `Python 3.12.1v` or above.
2. you will need these python libraries:
    * feedparser - `pip install feedparser`
    * beautifulsoup4 - `pip install beautifulsoup4`
## Getting Started
To get started with this script follow these steps:
1. Clone the repository: `git clone https://github.com/yardenfalik/News-For-Email.git`
2. Create a file in the project directory called `emailData.json`.
3. Copy the following code into the `emailData.json` file:
```
{
    "address": "your-mail@gmail.com",
    "password": "your password"
}
```
4. Change the address to your email address and the password to your Gmail password.
   if you don't know how to generate passwords for 3rd party apps on Gmail I've linked a video (not mine!)
   [here](https://www.youtube.com/watch?v=lSURGX0JHbA).
6. Run the main file with `Python 3.12.1v` or above.
