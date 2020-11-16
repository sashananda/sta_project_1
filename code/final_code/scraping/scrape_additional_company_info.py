import scrape
import re
import urllib.parse as urlparse
import pandas
import numpy as np
import time
import random
import math

def to_ascii(url):
    url = urlparse.urlsplit(url)
    url = list(url)
    url[2] = urlparse.quote(url[2])
    url = urlparse.urlunsplit(url)
    return url

def map_to_valid_url(urls, base_url):
    urls = urls.map(lambda x: base_url + x, na_action='ignore')
    return urls

def get_job_urls(raw_salaries_fp, base_url):
    df = pandas.read_csv(raw_salaries_fp)
    df = df[2949:]
    company_names = df['company']
    urls_overview = map_to_valid_url(df['url_overview'], base_url)
    urls_review = map_to_valid_url(df['url_review'], base_url)
    urls_interview = map_to_valid_url(df['url_interview'], base_url)
    urls_benefits = map_to_valid_url(df['url_benefits'], base_url)
    return [company_names, urls_overview, urls_review, urls_interview, urls_benefits]

def scrape_job_information(company_name, url_overview, url_review, url_interview, url_benefits, country_code):
    print(company_name)
    if type(url_overview) != float:
        fp = './companies_{country_code}/{company_name}/overview.html'\
            .format(country_code=country_code, company_name=company_name)
        scrape.write_html_to_file(to_ascii(url_overview), scrape.HEADERS, fp)

    if type(url_review) != float:
        fp = './companies_{country_code}/{company_name}/review.html'\
            .format(country_code=country_code, company_name=company_name)
        scrape.write_html_to_file(to_ascii(url_review), scrape.HEADERS, fp)

    if type(url_interview) != float:
        fp = './companies_{country_code}/{company_name}/interview.html'\
            .format(country_code=country_code, company_name=company_name)
        scrape.write_html_to_file(to_ascii(url_interview), scrape.HEADERS, fp)

    if type(url_benefits) != float:
        fp = './companies_{country_code}/{company_name}/benefits.html'\
            .format(country_code=country_code, company_name=company_name)
        scrape.write_html_to_file(to_ascii(url_benefits), scrape.HEADERS, fp)

def scrape_all_companies(company_names, urls_overview, urls_review, urls_interview, urls_benefits, country_code):
    for i in range(2949, len(company_names) + 2949):
        slp = random.uniform(1, 4)
        scrape_job_information(company_names[i], 
                               urls_overview[i],
                               urls_review[i],
                               urls_interview[i],
                               urls_benefits[i],
                               country_code)
        time.sleep(slp)

# CA
# fp_ca = './raw_companies/companies_ca_urls.csv'
# gd_url = 'https://www.glassdoor.com'
# company_names, urls_overview, urls_review, urls_interview, urls_benefits = get_job_urls(fp_ca, gd_url)
# scrape_all_companies(company_names, urls_overview, urls_review, urls_interview, urls_benefits, 'CA')



# US
fp_us = './raw_companies/companies_us_urls.csv'
gd_url = 'https://www.glassdoor.com'
company_names, urls_overview, urls_review, urls_interview, urls_benefits = get_job_urls(fp_us, gd_url)
scrape_all_companies(company_names, urls_overview, urls_review, urls_interview, urls_benefits, 'US')