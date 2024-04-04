import requests
from fake_useragent import UserAgent
from lxml import etree
import re
import json

XPATH_LINKS = '//div[@class="serp-item serp-item_link"]//h3//a[@class="bloko-link"]/@href'
XPATH_DESCRIPT = '//div[@class="bloko-text" or @class="vacancy-section"]//div[@data-qa="vacancy-description"]//text()'
XPATH_TITLE = '//div[@class="vacancy-title"]//h1//text()'
XPATH_SALARY = '//div[@class="vacancy-title"]//div[@data-qa="vacancy-salary"]//text()'
XPATH_COMPANY = '(//span[@class="vacancy-company-name"])[1]//text()'
XPATH_ADDRESS = '(//a[@data-qa="vacancy-view-link-location"]//span/text())'
XPATH_CITY = '(//p[@data-qa="vacancy-view-location"])[2]/text()'


def _get_job_description(html):
    descriptions = html.xpath(XPATH_DESCRIPT)
    if descriptions:
        descrip = ''.join(descriptions)
        pattern = r'(?i)(django|flask)'
        if re.compile(pattern=pattern).search(descrip):
            return True
    return False


def get_job_information(link, salary_in_usd=False):
    headers = {'User-Agent': UserAgent().chrome}
    response = requests.get(link, headers=headers)
    html = etree.HTML(response.text)
    salary_text = html.xpath(XPATH_SALARY)

    if salary_text:
        salary = ''.join(salary_text).strip().replace(u'\xa0', u' ')
    else:
        salary = 'Зарплата не указана'
        
    if salary_in_usd and '$' not in salary:
        return None

    if not _get_job_description(html=html):
        return None

    title = ''.join(html.xpath(XPATH_TITLE))

    company = ''.join(html.xpath(XPATH_COMPANY)).strip().replace(u'\xa0', u' ')

    address = html.xpath(XPATH_CITY)
    if address:
        city = address[0]
    else:
        address = html.xpath(XPATH_ADDRESS)
        if address:
            city = address[0] + address[-1]
        else:
            city = 'Город не указан'

    return {
        'link': link,
        'title': title,
        'salary': salary,
        'company': company,
        'city': city,
    }


def get_job_links(qty_pages=1):
    ua = UserAgent()
    for i in range(qty_pages):
        url = f'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page={i}'
        page = requests.get(url, headers={'User-Agent': ua.chrome})
        html = etree.HTML(page.content.decode('utf-8'))
        links = html.xpath(XPATH_LINKS)
        yield from links if links else ''


def save_jobs_to_json(qty_pages=1, salary_in_usd=False):
    jobs = []
    for id, link in enumerate(get_job_links(qty_pages=qty_pages)):
        if link:
            # print(id, link)
            job = get_job_information(link, salary_in_usd=salary_in_usd)
            if job:
                jobs.append(job)
    if jobs:    
        file = f'jobs_{"USD" if salary_in_usd else "RUR"}.json'
        with open(file=file, mode='w', encoding='utf-8') as f:
            json.dump(jobs, f, ensure_ascii=False, indent=4)
    else:
        print('Не найдено подходящих вакансий')
                


if __name__ == '__main__':
    # save_jobs_to_json(qty_pages=5)
    save_jobs_to_json(qty_pages=15, salary_in_usd=True)
