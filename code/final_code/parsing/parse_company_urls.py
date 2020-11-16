from bs4 import BeautifulSoup
import pandas as pd

def get_soup(fp):
    soup = BeautifulSoup(open(fp), 'html.parser')
    return soup

def get_overview_url(soup):
    ov = soup.find_all('span', {'class': 'eiCell cell overviews switchLogo '})
    if ov:
        url_tags = ov[0].find_all('a')
        if url_tags:
            overview = url_tags[0]['href']
        else:
            overview = ''
    else:
        overview = ''
    return overview

def get_review_tag(soup):
    re = soup.find_all('a', {'data-label': 'Reviews'})
    if re:
        review_tag = re[0]['href']
    else:
        review_tag = ''
    return review_tag

def get_interview_tag(soup):
    re = soup.find_all('a', {'class': 'eiCell cell interviews '})
    if re:
        interview_tag = re[0]['href']
    else:
        interview_tag = ''
    return interview_tag

def get_benefits_tag(soup):
    re = soup.find_all('a', {'class': 'eiCell cell benefits '})
    if re:
        benefits_tag = re[0]['href']
    else:
        benefits_tag = ''
    return benefits_tag

def get_next_urls(soup):
    overview = get_overview_url(soup)
    review = get_review_tag(soup)
    interview = get_interview_tag(soup)
    benefits = get_benefits_tag(soup)
    return [overview, review, interview, benefits]

def get_next_urls_companies(company_fps):
    urls = []
    count = 1
    for fp in company_fps:
        print(count)
        soup = get_soup(fp)
        url = get_next_urls(soup)
        urls.append(url)
        count += 1
    return urls

# fp = './salaries_info_CA/page1.html'
# soup = get_soup(fp)
# info = get_next_urls(soup)

header = ['url_overview', 'url_review', 'url_interview', 'url_benefits']

# CA
# pages = range(1, 401)
# fps_CA = ['./salaries_info_CA/page{page}.html'.format(page=page) for page in pages]
# urls_CA = get_next_urls_companies(fps_CA)
# df = pd.DataFrame(urls_CA, columns=header)

# df_csv = pd.read_csv('./raw_salaries/salaries_ca_info.csv')

# # Get company names.
# df['company'] = df_csv['company']

# # # Get unique companies and drop the rest
# df = df.drop_duplicates(subset='company')

# df = df[['company', 'url_overview', 'url_review', 'url_interview', 'url_benefits']]
# df.to_csv('./raw_salaries/companies_ca_info.csv')

# US
pages = range(1, 6960)
fps_US = ['./salaries_info_US/page{page}.html'.format(page=page) for page in pages]
urls_CA = get_next_urls_companies(fps_US)
df = pd.DataFrame(urls_CA, columns=header)

df_csv = pd.read_csv('./raw_salaries/salaries_us_info.csv')

# Get company names.
df['company'] = df_csv['company']

# # Get unique companies and drop the rest
df_new = df.drop_duplicates(subset='company', keep='first')

df_new = df_new[['company', 'url_overview', 'url_review', 'url_interview', 'url_benefits']]
df_new.to_csv('./raw_companies/companies_us_urls.csv')
