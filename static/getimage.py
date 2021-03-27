# -*- coding: utf-8 -*- 
import os

from icrawler.builtin import BingImageCrawler

def main(w):
    os.remove('static/tmp/000001.jpg')
    
    print('run')
    crawler = BingImageCrawler(storage={"root_dir": "static/tmp"})
    crawler.crawl(keyword=w, max_num=1)
