import scrapy


class XpathSpider(scrapy.Spider):
        name = "toscrape-xpath"

        def start_requests(self):
            url = 'http://quotes.toscrape.com/'
            tag = getattr(self, 'tag', None)
            if tag is not None:
                url = url + 'tag/' + tag
            yield scrapy.Request(url, self.parse)

        def parse(self, response):
            for q in response.xpath('//div[@class="quote"]'):
                yield {
                    'text': q.xpath('./span[@class="text"]/text()').get()
                    ,
                    'author': q.xpath('.//small[@class="author"]/text()').get(),
                    'tags': q.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
                }

            next_page = response.xpath('//li[@class="next"]//@href').get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
