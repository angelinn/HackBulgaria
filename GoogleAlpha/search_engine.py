from connection import Base
from connection import engine
from sqlalchemy.orm import Session
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import sys
from website import Website
from page import Page


class SearchEngine:
    worked_links = []

    def __init__(self, site):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)

        self.pages_count = 0
        self.site = site

    def get_page_links(self, site):
        html = requests.get(site).text
        soup = BeautifulSoup(html)

        links = []

        for a_href in soup.find_all('a'):
            try:
                link = a_href.get('href')

                if self.is_link_valid(link) is False:
                    continue

                try:
                    title = soup.title.string
                except Exception:
                    title = ''

                try:
                    desc = soup.title.description
                except Exception:
                    desc = ''

                links.append({'link': link, 'title': title, 'desc': desc})

            except TypeError:
                continue
            except UserWarning:
                continue

        return links

    def work_pages(self, page):
        links = self.get_page_links(page)

        i = 0
        while links != []:
            self.pages_count += 1
            self.read_page(links[i], links)
            i += 1

        self.pages_count = len(links)

    def read_page(self, link, links):
        if link['link'] not in self.worked_links:
            self.worked_links.append(link['link'])
        else:
            return

        res = urljoin(self.site, link['link'])
        print(res)

        links += self.get_page_links(res)

        self.session.add(Page(website=self.site, url=res, title=link['title'],
                              description=link['desc'],
                              ads=0, SSL=True, multi_lang=None, points=None))
        self.session.commit()
        links = links[1:]

    def is_link_valid(self, link):
        inside_http_correct = True

        if self.site not in link:
            if 'http' in link:
                inside_http_correct = False

        elif link.count('http') > 1:
            inside_http_correct = False

        return (not (link in self.worked_links or
                     '#' in link or
                     '..' in link or ':' in link)) and inside_http_correct

    def go(self):
        self.work_pages(self.site)

        self.session.add(Website(url=self.site, title='', domain=self.site,
                                 pages_count=self.pages_count, HTML_version=0.0))

        self.session.commit()


def main():
    search = SearchEngine(sys.argv[1])
    search.go()

if __name__ == '__main__':
    main()
