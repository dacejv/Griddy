import subprocess
import os

def run_spiders():
    relative_path = "webscraping\webscraping"
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, relative_path)
    subprocess.call(['scrapy', 'crawl', 'dendscrape', '-O', 'DenOtevrenychDveri.json'], cwd=full_path)
    subprocess.call(['scrapy', 'crawl', 'prijmac', '-O', 'PrijimaciZkousky.json'], cwd=full_path)
    subprocess.call(['scrapy', 'crawl', 'obedovac', '-O', 'Jidelnicek.json'], cwd=full_path)

if __name__ == "__main__":
    run_spiders()