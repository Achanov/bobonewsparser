# bobonewsparser
Feel free to receive financial news from Russian market in some clicks. And some waiting. And some libs installed.

Download the latest ChromeDriver from here https://googlechromelabs.github.io/chrome-for-testing/#stable

Make sure all files and the Chromedriver are in the same folder. Install necessary libraries.

The siteconfig file contains site configs. Parser reads the config file and starts the browser in NON-headless mode. JS is allowed!

Websites scraping is performed in a gentle way.

Generator addresses the database and provides the HTML file with the news parsed within the last 24 hours. 
