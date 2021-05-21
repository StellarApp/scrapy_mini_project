import scrapy


class googleStorefrontSpider(scrapy.Spider):
    name = "google-storefront"
    start_urls = [
        'https://www.google.com/search?q=storefront&tbm=isch',
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
            }