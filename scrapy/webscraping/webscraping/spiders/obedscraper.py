import scrapy

class obedyspider(scrapy.Spider):
    name = 'obedovac'
    start_urls = ['https://strava.spseplzen.cz']

    def parse(self, response):
        for obed in response.css('div.jidelnicekDen'):
                    main_context_div = "//*[@id='mainContextDiv']"
        div1 = main_context_div + "/div[2]/div[1]/div[2]"
        div2 = main_context_div + "/div[2]/div[2]/div[2]"
        div3 = main_context_div + "/div[2]/div[3]/div[2]"
        div4 = main_context_div + "/div[2]/div[4]/div[2]"
        yield {
            'datum1': obed.xpath("/html/body/div[1]/div[2]/div[1]/div[1]/strong/span[1]").get().replace(" ", "").replace("\n","").replace("<spanclass=\"important\">", "").replace("</span>", ""),
            'obed1-1': obed.xpath(div1 + "/div[4]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'obed2-1': obed.xpath(div1 + "/div[5]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'obed3-1': obed.xpath(div1 + "/div[6]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'datum2': obed.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/strong/span[1]").get().replace(" ", "").replace("\n","").replace("<spanclass=\"important\">", "").replace("</span>", ""),
            'obed1-2': obed.xpath(div2 + "/div[4]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'obed2-2': obed.xpath(div2 + "/div[5]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'obed3-2': obed.xpath(div2 + "/div[6]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'datum3': obed.xpath("/html/body/div[1]/div[2]/div[3]/div[1]/strong/span[1]").get().replace(" ", "").replace("\n","").replace("<spanclass=\"important\">", "").replace("</span>", ""),
             'obed1-3': obed.xpath(div3 + "/div[4]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'obed2-3': obed.xpath(div3 + "/div[5]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'obed3-3': obed.xpath(div3 + "/div[6]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'datum4': obed.xpath("/html/body/div[1]/div[2]/div[4]/div[1]/strong/span[1]").get().replace(" ", "").replace("\n","").replace("<spanclass=\"important\">", "").replace("</span>", ""),
            'obed1-4': obed.xpath(div4 + "/div[4]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'obed2-4': obed.xpath(div4 + "/div[5]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
            'obed3-4': obed.xpath(div4 + "/div[6]/text()[3]").extract_first().replace("--", "").strip().replace("\n", ""),
        }