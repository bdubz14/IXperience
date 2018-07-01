# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import requests
from parsel import Selector


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        book_urls = [response.urljoin(url) for url in response.css("div.image_container>a::attr(href)").extract()]
        for book in book_urls:
            yield scrapy.Request(book, callback=self.parse_book)
        next_page_url = 'http://books.toscrape.com/catalogue/' + response.css("li.next>a::attr(href)").extract_first()
        if next_page_url:  # the last page wont have next button
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_book(self, response):
        link = response._get_url()
        r = requests.get(link)
        sel = Selector(r.text)
        book_data = {}
        title = sel.css('div.col-sm-6.product_main>h1')[0].extract().replace('<h1>', '').replace('</h1>', '')
        df = pd.read_html(link)[0]
        
        book_data['category'] = sel.css('ul li')[2].extract().split('</a>')[0].split('>')[2]
        book_data['title'] = title
        book_data['price'] = df[1][3]
        book_data['units left'] = int(df[1][5].replace('In stock (', '').replace(' available)', ''))
        book_data['UPC'] = df[1][0]
        book_data['url'] = link
        book_data['description'] = sel.css('p')[3].extract().replace('<p>', '').replace('</p>', '')
        book_data['rating'] = sel.css('p')[2].extract().split('\n')[0].replace('<p class="star-rating ', '').replace('">', '')
        yield book_data
