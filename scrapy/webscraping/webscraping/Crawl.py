import subprocess

def run_spiders():
    subprocess.call(['scrapy', 'crawl', 'dendscrape', '-O', 'scrape/DenOtevrenychDveri.json'])
    subprocess.call(['scrapy', 'crawl', 'prijmac', '-O', 'scrape/PrijimaciZkousky.json'])
    subprocess.call(['scrapy', 'crawl', 'obedovac', '-O', 'scrape/Jidelnicek.json'])

if __name__ == "__main__":
    run_spiders()