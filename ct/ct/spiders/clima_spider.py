import scrapy
from datetime import datetime
import re
from ..items import CtItem


class ClimaTempo(scrapy.Spider):
    name = "climatempo"

    def start_requests(self):
        allowed_domains = ['climatempo.com.br']
        urls = [
            "https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/558/saopaulo-sp",
            "https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/321/riodejaneiro-rj"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_text)

    def parse_text(self, response):
        item = CtItem()

        city = str(''.join(response.xpath(
            '//*[@id="mainContent"]/ul/div/div[1]/ol/li[4]/span/text()').get().split()))

        weather_now_C = float(''.join(
            re.findall(
                '[\d]',
                str(
                    response.css(
                        'span.-bold.-gray-dark-2::text').get().split()))))

        felling = float(''.join(
            re.findall(
                '[\d]',
                str(
                    response.xpath(
                        '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[3]/span[2]/text()'
                    ).get().split()))))

        wind = str(''.join(
            response.xpath(
                '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/text()'
            ).getall()[1].split()))
        humidity = float(''.join(
            re.findall(
                '[\d]',
                str(
                    response.xpath(
                        '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/p/span/text()'
                    ).get().split()))))

        pressure = int(''.join(
            re.findall(
                '[\d]',
                str(
                    response.xpath(
                        '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[3]/div[2]/span/text()'
                    ).get().split()))))

        item['city'] = city
        item['weather_now_C'] = weather_now_C
        item['felling'] = felling
        item['wind'] = wind
        item['humidity'] = humidity
        item['url'] = response.url
        item['register_at'] = datetime.now().isoformat(timespec='minutes')

        yield item
