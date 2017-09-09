import config
import scrapy
from scrapy.crawler import CrawlerProcess
from song import Song
from author import Author

class AuthorScraper(scrapy.Spider):
    """ Allows gettin the authors' songs list """

    name = "AuthorScraper"
    authors = []

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        author_name = response.css('h1::text').extract_first()
        author = Author(name=author_name, songs=[])
        song_list = response.css('ul.cnt-list li a')
        for song in song_list:
            title = song.css('::text').extract_first()
            link = song.css('::attr(href)').extract_first()
            author.songs.append(
                    Song(author_name, title, config.page_url + link, None))
        self.authors.append(author)

    def run(self, urls):
        process = CrawlerProcess({
            'USER_AGENT': config.user_agent
        })
        process.crawl(AuthorScraper, urls=set(urls))
        process.start()
        return self.authors
