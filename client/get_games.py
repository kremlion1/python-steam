import csv
import requests
import json
from multiprocessing import Pool
from time import sleep
from lxml import html
import re
import HTMLParser
import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)


root = 'http://www.metacritic.com/'
SLOW_DOWN = False

def get_html(url):
    start_time=time.time()
    headers = {"User-Agent": "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101"}
    html = requests.get(url, headers=headers).content.decode('utf-8')
    wait =1.3-(time.time()-start_time)
    if (wait>0):
        sleep(wait)



def get_pages(genre):
    def scrape():
        page_content = get_html(genre)
        return page_content
        document = json.loads(page_content).values()[0]
        """
        match1 = re.findall("<a class=\"market_listing_row_link\" [\s\S]*?</a>", document)
        for m in match1:
            lpn_text = re.findall("<span class=\"normal_price\">([\s\S]*?)</span>", m)
            print lpn_text[0]
        print lpn_text

        match = re.search("var g_rgFilterData = (.*);", page_content)
        js_var = match.group().encode("cp1251")
        js_var = js_var[js_var.find("{"):len(js_var)-1:]
        dict =json.loads(js_var)
        games =[]
        for d in dict.values()[0].values()[1].values():
            games.append(d.values()[1])
        i=0

"""
    return scrape()

def main():
    with Profiler() as p:
        for i in range(0,51):
            p=get_pages("http://steamcommunity.com/market/search/render/?query=&start=40&count=200&search_descriptions=0&sort_column=name&sort_dir=asc&appid=753&category_753_Game%5B%5D=any&category_753_item_class%5B%5D=tag_item_class_2&category_753_item_class%5B%5D=tag_item_class_5&currency=5")
            if p=="null":
                print i
                break
    sleep(1)
    """dict = json.load(open('genres.json', 'r'))
    p = Pool(4)
    p.map(get_pages, [dict[key] for key in dict.keys()])
    print('Over')"""

if __name__ == "__main__":
    main()