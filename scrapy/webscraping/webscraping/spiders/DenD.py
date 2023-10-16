import scrapy


class DenDspider(scrapy.Spider):
    name = 'dendscrape'
    start_urls = ['https://www.spseplzen.cz/dny-otevrenych-dveri/']

    def parse(self, response):
        data = {'DenOtevrenychDveri':[]}
        element = response.xpath('//*[@id="post-20390"]/div[2]/div[4]/div[1]/div/div/div/div/h2/span/strong/text()')
        if not element:
            data['DenOtevrenychDveri'].append({
                'error': 'Structure of web has changed',
                'termin1': '',
            })
        else:
            for termin in response.xpath('//*[@id="post-20390"]/div[2]/div[4]/div[1]/div/div'):
                data['DenOtevrenychDveri'].append({
                    'error': '',
                    'termin1': ''.join(termin.xpath('/html/body/div[1]/div[3]/div/div/div/main/article/div[2]/div[4]/div[1]/div/div/div/div/h2/span/strong/text()').extract()).strip(),
                })
        yield data