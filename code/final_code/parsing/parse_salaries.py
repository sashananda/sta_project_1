from bs4 import BeautifulSoup
import pandas as pd

def get_soup(fp):
    soup = BeautifulSoup(open(fp), 'html.parser')
    return soup

def get_salary_tag(row, company, start):
    """ Salary tag sometimes has an "about" section. Helper function to deal
        with this. """
    salary = False
    for row in company.find_all('div', {'class': 'col-2 d-none d-md-flex flex-row justify-content-end'}):
        salary = row.text
        return salary
    if not salary:
        for row in company.find_all('div', {'class': 'col-2 d-none d-md-flex flex-column align-items-end'}):
            salary = row.get_text()
            idx = salary.find(start)
            sal = salary[idx:]
            return sal

def get_companies_info(soup, info):
    for company in soup.find_all('div', {'data-test': 'salary-list-items'}):
        company_info = []

        # Get name and href link to more info to scrape later
        for row in company.find_all('div', {'data-test': 'job-info'}):
            url_tags = row.find_all('a')
            for url_tag in url_tags:
                if url_tag.text: 
                    company_info.append(url_tag['href'])
            for sibling in url_tags:
                position = sibling.next_element
                company_info.append(position)
                name_tag = position.next_element
                name = name_tag.text
                company_info.append(name)

        # Get salary
        salary = get_salary_tag(row, company, '$')
        company_info.append(salary)

        # Get range of salaries in company to calculate percentiles later
        for bar in company.find_all('div', {'class': 'common__RangeBarStyle__values common__flex__justifySpaceBetween common__flex__container '}):
            range_tag = bar.find_all('span')
            lower_range = range_tag[0].text
            upper_range = range_tag[1].text
            company_info.append(lower_range)
            company_info.append(upper_range)
        if (name in ['Rubikloud Technologies', 'I Don\'t Know', 'Me', 'g', 'Do not wish to disclose', 'Dane Street', 'YYZ Ventures']):
            continue
        info.append(company_info)
    return info

def get_all_companies_info(num_pages, country_code):
    info = []
    for page in range(1, num_pages + 1):
        fp = './data_science_salaries_{country}_html/page{page}.html'.format(country=country_code, page=page)
        soup = get_soup(fp)
        get_companies_info(soup, info)
    return info

header = ['url', 'position', 'company', 'salary', 'lower_bound_salary', 'upper_bound_salary']

# CA
num_pages_CA = 21
info_CA = get_all_companies_info(num_pages_CA, 'CA')
df = pd.DataFrame(info_CA, columns=header)
df = df[['company', 'position', 'salary', 'lower_bound_salary', 'upper_bound_salary', 'url']]
df.to_csv('./raw_salaries/salaries_ca.csv')

# US
num_pages_US = 348
info_US = get_all_companies_info(num_pages_US, 'US')
df = pd.DataFrame(info_US, columns=header)
df = df[['company', 'position', 'salary', 'lower_bound_salary', 'upper_bound_salary', 'url']]
df.to_csv('./salaries/salaries_us.csv')