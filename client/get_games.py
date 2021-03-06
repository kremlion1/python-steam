import csv
import requests
import json
from multiprocessing import Process
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


class Client(object):
    block_date = time.time()

    def get_html(self, url):
        if time.time() < self.block_date:
            sleep(self.block_date - time.time())
        headers = {"User-Agent": "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101"}
        proxies = {
            'http': 'http://120.132.52.218:8888'
        }
        html_request = requests.get(url, headers=headers, proxies=proxies).content.decode('utf-8')
        return html_request

    def get_games(self, html_request):
        page_content = self.get_html(html_request)
        self.block_date = time.time() + (300 if "null" == page_content else 15)
        return page_content
        document = json.loads(page_content).values()[0]
        cards = []
        match1 = re.findall("<a class=\"market_listing_row_link\" [\s\S]*?</a>", document)
        for m in match1:
            href = re.findall("<a class=\"market_listing_row_link\" href=\"([\s\S]*?)\" id=\"resultlink_\d+\">", m)[0]
            img_src = re.findall("<img id=\"result_\d+_image\" src=\"([\s\S]*?)\" style=\"\"", m)[0]
            num_listings_qty = re.findall("<span class=\"market_listing_num_listings_qty\">([\s\S]*?)</span>", m)[0]
            price = re.findall("<span class=\"normal_price\">([\s\S]*?)</span>", m)[0]
            item_name = re.findall("class=\"market_listing_item_name\".*>([\s\S]*?)</span>\s*<br/>", m)[0]
            game_name = re.findall("<span class=\"market_listing_game_name\">([\s\S]*?)</span>", m)[0]
            cards.append(
                {'href': href, 'img_src': img_src, 'num_listings_qty': num_listings_qty, 'item_name': item_name,
                 'game_name': game_name, 'price': price})
            print cards
        return cards

    def start(self):
        for i in range(0, 151):
            page = self.get_games("http://steamcommunity.com/market/search/render/?query=&start=" + str(i)
                                  + "0&count=10&search_descriptions=0&sort_column=name&sort_dir=asc&appid=753"
                                    "&category_753_Game%5B%5D=any&category_753_item_class%5B%5D=tag_item_class_2"
                                    "&category_753_item_class%5B%5D=tag_item_class_")
            if page == "null":
                print i

def main():
    client = Client()
    p = Process(target=client.start())
    p.start()
    p.join()
    """
        dict = json.load(open('genres.json', 'r'))
        p = Pool(4)
        p.map(get_pages, [dict[key] for key in dict.keys()])
        print('Over')
    """


if __name__ == "__main__":
    main()
