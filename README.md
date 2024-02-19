# bobonewsparser
Feel free to receive financial news from the Russian market with some clicks. And some waiting. And some libs installed.

Make sure all files and the Chromedriver are in the same folder. Install necessary libraries, these are jinja2 and selenium.

The siteconfig.py file contains site configs. The parser reads the config file and starts the browser in NON-headless mode. JS is allowed!

Website scraping is made in a gentle way. The generator addresses the database and provides the HTML file with the news parsed within the last 24 hours.

After the first run, you will see many unnecessary links, which is fine. You need to run the parser in 24 hours to see these gone.

Automatization is up to you, sorry. 
