#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):
    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/*'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):

        res_data = {'url': page_url}

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node is not None:
            res_data['summary'] = summary_node.get_text()
        else:
            res_data['summary'] = 'None'

        return res_data

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data