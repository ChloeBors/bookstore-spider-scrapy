This python file shows how to make a spider/scrape bot using scrapy.

In the example I scrape books.toscrape.com since it is made for scraping.

The example shows how to use either Xpath or CSS (+ regular expression) handling.
# Comment the one you don't want to use.

Output to a CSV by running: 
scrapy runspider bookstore.py -s USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36" -s ROBOTSTXT_OBEY=False -o books.csv
