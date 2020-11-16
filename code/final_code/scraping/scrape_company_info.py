import scrape
import pandas
import numpy as np
import time
import random

def get_job_urls(raw_salaries_fp):
    df = pandas.read_csv(raw_salaries_fp)
    urls = df['url']
    return urls

def scrape_company_info_by_country(urls, country_code):
    for i in range(len(urls)):
        slp = random.uniform(1, 3) 
        page = i + 1
        print(urls[i])
        fp = './salaries_info_{country}/page{page}.html'.format(country=country_code, page=page)
        scrape.write_html_to_file(urls[i], scrape.HEADERS, fp)
        time.sleep(slp)

gd_url = 'https://www.glassdoor.com'

# CA
urls = np.array(get_job_urls('./raw_salaries/salaries_ca.csv'))
urls = list(map(lambda x: gd_url + x, urls))
scrape_company_info_by_country(urls, 'CA')

# US
urls = np.array(get_job_urls('./raw_salaries/salaries_us.csv'))
urls = list(map(lambda x: gd_url + x, urls))
scrape_company_info_by_country(urls, 'US')