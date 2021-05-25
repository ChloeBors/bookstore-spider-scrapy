import scrapy

## Shows how to scrape with either xpath or css handling.
class MySpider(scrapy.Spider):
    name = 'bookstoscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    custom_settings = {

        'LOG_LEVEL': 'WARNING',

    }

    def parse(self, response):
        print(f'Current page {response.url}')

        ## Xpath
        for book in response.xpath('//article'):
            title = book.xpath('.//h3/a/@title').extract_first()
            price = book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()

            yield {
                "title": title,
                "price": price
            }

        ## Css handling + regular expression to only extract price in decimal
        for book in response.css('article.product_pod'):
            title_css = book.css('h3 a::text').get()
            price_css = book.css('.product_price p::text').re(r'(\d+).(\d+)')

            yield {
                "title": title_css,
                "price": price_css
            }

        try:
            next_page = response.css('.next a::attr(href)').extract()
            go_to_page = 'https://books.toscrape.com/catalogue/' + next_page[0]
            yield scrapy.Request(go_to_page, callback=self.parse)
        except IndexError:
            print(f'Scrape ended')
