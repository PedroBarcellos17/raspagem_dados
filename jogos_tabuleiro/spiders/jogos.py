import scrapy


class JogosSpider(scrapy.Spider):
    name = "jogos"
    start_urls = ["https://boardgamegeek.com/browse/boardgame"]

    def parse(self, response):
        for jogo in response.css('#row_'):
            yield {
                'Rank': jogo.css('.collection_rank a::attr(name)').get(),
                'Nome': jogo.css('.primary ::text').get(),
                'Nota': jogo.css('.collection_bggrating:nth-child(5)::text').get().split(),
            }

        prox_pag = response.xpath(
            '//*[@id="maincontent"]/p/a[5]').attrib['href']
        if prox_pag is not None:
            yield response.follow(prox_pag, callback=self.parse)
