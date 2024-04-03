import requests
from fake_useragent import UserAgent
from lxml import etree
import re


def _get_job_description(html):
    descriptions = html.xpath('//div[@class="vacancy-description"]//div[@data-qa="vacancy-description"]//text()')
    if descriptions:
        descrip = ''.join(descriptions)
        pattern = r'(?i)(django|flask)'
        if re.compile(pattern=pattern).search(descrip):
            return descrip
    return None


def get_job_information(link):
    headers = {'User-Agent': UserAgent().chrome}
    response = requests.get(link, headers=headers)
    html = etree.HTML(response.text)
    descripton = _get_job_description(html=html)
    if descripton:
        title = ''.join(html.xpath('//div[@class="vacancy-title"]//h1//text()'))
        print(title)
        salary = html.xpath('//div[@class="vacancy-title"]//div[@data-qa="vacancy-salary"]//text()')
        if salary:
            for i in salary:
                print(i)


def get_job_links(qty_pages = 1):
    ua = UserAgent()
    for i in range(qty_pages):
        url = f'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page={i}'
        page = requests.get(url, headers={'User-Agent': ua.chrome})
        html = etree.HTML(page.content.decode('utf-8'))
        links = html.xpath('//div[@class="serp-item serp-item_link"]//h3//a[@class="bloko-link"]/@href')
        yield from links if links else None


if __name__ == '__main__':
    # for link in get_job_links(2):
        # print(link)
    # print(get_job_information(link='https://spb.hh.ru/vacancy/96074104?query=python&hhtmFrom=vacancy_search_list'))
    # print(get_job_information(link='https://spb.hh.ru/vacancy/94623534?query=python&hhtmFrom=vacancy_search_list'))
    print(get_job_information(link='https://spb.hh.ru/vacancy/96002765?query=python&hhtmFrom=vacancy_search_list'))
                