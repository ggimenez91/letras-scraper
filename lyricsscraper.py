import config
import scrapy
from scrapy.crawler import CrawlerProcess
from song import Song

class LyricsScraper(scrapy.Spider):
    """ Allows getting the detailed info of each song """
    name = "Letras.com"
    songs = []

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        author = response.css('h2 a::text').extract_first()
        title =  response.css('h1::text').extract_first()
        stanzas = list(map(lambda x: x.css('p::text').extract(),
            response.css('article p')))
        self.songs.append(Song(author, title, response.url, stanzas))

    def run(self, urls):
        process = CrawlerProcess({
            'USER_AGENT': config.user_agent
        })
        process.crawl(LyricsScraper, urls=set(urls))
        process.start()
        return self.songs
