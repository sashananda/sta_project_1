import scrape

def make_url_str(page, country_code):
    if (country_code == 'CA'):
        url = 'https://www.glassdoor.com/Salaries/canada-data-scientist-salary-SRCH_IL.0,6_IN3_KO7,21_IP{page}.htm?clickSource=searchBtn'.format(page=page)
    else:
        url = 'https://www.glassdoor.com/Salaries/us-data-scientist-salary-SRCH_IL.0,2_IN1_KO3,17_IP{page}.htm?clickSource=searchBtn'.format(page=page)
    return url

def scrape_all_pages(base_url, urls, country_code):
    fp = './data_science_salaries_{country}/page1.html'.format(country=country_code)
    scrape.write_html_to_file(base_url, scrape.HEADERS, fp)
    for url in urls:
        fp = './data_science_salaries_{country}/page{num}.html'.format(country=country_code, num=url[0])
        scrape.write_html_to_file(url[1], scrape.HEADERS, fp)

# Scrape Canada
base_url_CA = 'https://www.glassdoor.com/Salaries/canada-data-scientist-salary-SRCH_IL.0,6_IN3_KO7,21.htm?clickSource=searchBtn'
pages = range(2, 22)
urls_CA = [[page, make_url_str(page, 'CA')] for page in pages]
scrape_all_pages(base_url_CA, urls_CA, 'CA')

# Scrape US
base_url_US = 'https://www.glassdoor.com/Salaries/us-data-scientist-salary-SRCH_IL.0,2_IN1_KO3,17.htm?clickSource=searchBtn'
pages = range(2, 348)
urls_US = [[page, make_url_str(page, 'US')] for page in pages]
scrape_all_pages(base_url_US, urls_US, 'US')