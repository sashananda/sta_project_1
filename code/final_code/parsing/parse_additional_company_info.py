from bs4 import BeautifulSoup
import pandas as pd
import os.path
from os import path
import numpy as np

def get_soup(fp):
    soup = BeautifulSoup(open(fp), 'html.parser')
    return soup

def get_overview_text(overview_block, data_test):
    txt = ''
    if overview_block:
        tag = overview_block[0].find_all('div', {'data-test': data_test})
        if tag:
            txt = tag[0].text
    return txt

def get_overview(fp):
    soup = get_soup(fp)
    overview_block = soup.find_all('div', {'data-test': 'employerOverviewModule'})
    size = get_overview_text(overview_block, 'employer-size')
    founded = get_overview_text(overview_block, 'employer-founded')
    company_type = get_overview_text(overview_block, 'employer-type')
    industry = get_overview_text(overview_block, 'employer-industry')
    revenue = get_overview_text(overview_block, 'employer-revenue')
    return [size, founded, company_type, industry, revenue]

def get_review(fp):
    soup = get_soup(fp)
    review = ''
    review_block = soup.find_all('div', {'class': 'v2__EIReviewsRatingsStylesV2__ratingInfoWrapper'})
    if review_block:
        review_tag = review_block[0].find_all('div', {'class': 'v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__large'})
        if review_tag:
            review = review_tag[0].text
    return review
        
def get_interview_difficulty(fp):
    soup = get_soup(fp)
    difficulty = ''
    interview_block = soup.find_all('div', {'class': 'd-flex justify-content-between flex-wrap'})
    if interview_block:
        difficulty_block = soup.find_all('div', {'class': 'd-flex flex-column '})
        if difficulty_block:
            difficulty_tag = difficulty_block[2].find_all('div', {'class': 'align-self-center'})
            if difficulty_tag:
                difficulty = difficulty_tag[0].contents[-2].text
    return difficulty

def get_benefits(fp):
    soup = get_soup(fp)
    benefits = ''
    benefits_block = soup.find_all('div', {'class': 'd-flex align-items-center mb-0 mb-sm-sm'})
    if benefits_block:
        benefits_tag = benefits_block[0].find_all('div', {'class': 'mr css-b63kyi css-16iqw5x'})
        if benefits_tag:
            benefits = benefits_tag[0].text
    return benefits

def get_info(func, country_code, company_name, inf):
    if func == get_overview:
        info = ['', '', '', '', '']
    else:
        info = ''
    fp = './companies_{country_code}/{company_name}/{inf}.html'\
        .format(country_code=country_code, company_name=company_name, inf=inf)
    if path.exists(fp):
        info = func(fp)
    return info

def get_additional_info(country_code, company_name):
    overview = get_info(get_overview, country_code, company_name, 'overview')
    review = get_info(get_review, country_code, company_name, 'review')
    interview = get_info(get_interview_difficulty, country_code, company_name, 'interview')
    benefits = get_info(get_benefits, country_code, company_name, 'benefits')
    return [overview[0], overview[1], overview[2], overview[3], overview[4], review, interview, benefits]

def get_all_additional_company_info(country_code, company_names):
    info = []
    for company_name in company_names:
        print(company_name)
        company_info = get_additional_info(country_code, company_name)
        info.append(company_info)
    return info

header = ['company_size', 'company_year_founded', 'company_type', 'company_industry', 'company_revenue', \
          'company_review', 'company_interview_difficulty', 'company_benefits']

# CA
# fp = './companies_{country_code}/{company_name}/benefits.html'
# country_code = 'CA'
# df_csv = pd.read_csv('./raw_companies/companies_ca_urls.csv')
# names = df_csv['company']

# info_CA = get_all_additional_company_info(country_code, names)
# df = pd.DataFrame(info_CA, columns=header)

# for i in range(len(header)):
#     df_csv[header[i]] = df[header[i]]

# df_csv = df_csv.drop(['url_overview', 'url_review', 'url_interview', 'url_benefits', 'Unnamed: 0'], axis=1)
# df_csv.to_csv('./raw_companies/companies_ca_info.csv')

# US
country_code = 'US'
df_csv = pd.read_csv('./raw_companies/companies_us_urls.csv')
names = df_csv['company']

info_US = get_all_additional_company_info(country_code, names)
df = pd.DataFrame(info_US, columns=header)

for i in range(len(header)):
    df_csv[header[i]] = df[header[i]]

df_csv = df_csv.drop(['url_overview', 'url_review', 'url_interview', 'url_benefits', 'Unnamed: 0'], axis=1)
df_csv.to_csv('./raw_companies/companies_us_info.csv')