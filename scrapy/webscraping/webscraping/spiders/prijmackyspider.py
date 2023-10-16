import scrapy

class prijmackyspider(scrapy.Spider):
    name = 'prijmac'
    start_urls = ['https://prijimacky.cermat.cz/menu/jednotna-prijimaci-zkouska']

    def parse(self, response):
        data = {'PrijmaciRizeniSS':[]}
        element_1 = response.xpath('//*[@id="page-158"]/table[1]/tbody/tr[2]/td[2]')
        element_2 = response.xpath('//*[@id="page-158"]/table[1]/tbody/tr[2]/td[3]')

        if not element_1 or not element_2:
            data['PrijmaciRizeniSS'].append({
                'error': 'Structure of web has changed',
                'termin1': '',
                'termin2': '',
            })
        else:
            for terminy in response.xpath('//*[@id="page-158"]/table[1]/tbody/tr[2]') :
                data['PrijmaciRizeniSS'].append({
                    'error': '',
                    'termin1': ''.join(
                        terminy.xpath('//*[@id="page-158"]/table[1]/tbody/tr[2]/td[2]/text()').extract()).strip(),
                    'termin2': ''.join(
                        terminy.xpath('//*[@id="page-158"]/table[1]/tbody/tr[2]/td[3]/text()').extract()).strip(),
                })
        yield data