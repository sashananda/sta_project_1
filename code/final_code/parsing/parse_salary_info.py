from bs4 import BeautifulSoup
import pandas as pd

def get_soup(fp):
    soup = BeautifulSoup(open(fp), 'html.parser')
    return soup

def get_salary_info(soup):
    base_pay = ''
    bonus_pay = ''
    cash_bonus = ''
    stock_bonus = ''
    ring = soup.find_all('div', {'class': 'common__DonutTwoSegmentStyle__donut'})
    if ring:
        for bp in soup.find_all('div', {'class': 'salaryDetails__DonutAndDataStyle__basePay'}):
            base_pay_tag = bp.find_all('div', {'class': 'salaryDetails__SalaryWithRangeStyle__basePay '})
            if base_pay_tag:
                base_pay = base_pay_tag[0].text
            base_pay_range_tag = bp.find_all('div', {'class': 'salaryDetails__SalaryWithRangeStyle__basePay css-1w5ifpo salaryDetails__SalaryWithRangeStyle__range'})
            if base_pay_range_tag:
                base_pay = base_pay_range_tag[0].text
        for ap in soup.find_all('div', {'class': 'salaryDetails__DonutAndDataStyle__additionalPay'}):
            bonus_pay_tag = ap.find_all('div', {'class': 'salaryDetails__SalaryWithRangeStyle__basePay '})
            if bonus_pay_tag:
                bonus_pay = bonus_pay_tag[0].text
            bonus_pay_range_tag = bp.find_all('div', {'class': 'salaryDetails__SalaryWithRangeStyle__basePay css-1w5ifpo salaryDetails__SalaryWithRangeStyle__range'})
            if bonus_pay_range_tag:
                bonus_pay = base_pay_range_tag[0].text
    table = soup.find_all('div', {'class': 'salaryDetails__AdditionalCompTableStyle__additionalCompTable'})
    if table:
        rows = table[0].find_all('div', {'class': 'salaryDetails__AdditionalCompRowStyle__compRow'})
        for row in rows:
            bonus_tag = row.find_all('div', {'class': 'common__flex__container common__flex__vCenter common__flex__container'})
            is_cash = bonus_tag[0].text.startswith('Cash Bonus')
            strong_tag = bonus_tag[0].find_all('span', {'class': 'pr-lg'})
            if strong_tag:
                bonus = strong_tag[0].text
                if (is_cash):
                    cash_bonus = bonus
                else:
                    stock_bonus = bonus
            range_tag = bonus_tag[0].find_all('span', {'class': 'strong'})
            if range_tag:
                bonus = range_tag[0].text
                if (is_cash):
                    cash_bonus = bonus
                else:
                    stock_bonus = bonus
    return [base_pay, bonus_pay, cash_bonus, stock_bonus]

def get_salary_info_for_all_pages(fps):
    salary_info = []
    for fp in fps:
        soup = get_soup(fp)
        info = get_salary_info(soup)
        salary_info.append(info)
    return salary_info

# fp = './salaries_info_CA/page1.html'
# soup = get_soup(fp)
# info = get_salary_info(soup)
# print(info)

header = ['base_pay', 'bonus_pay', 'cash_bonus', 'stock_bonus']

# Scrape Canada
# pages = range(1, 401)
# fps_CA = ['./salaries_info_CA/page{page}.html'.format(page=page) for page in pages]
# info_CA = get_salary_info_for_all_pages(fps_CA)
# df = pd.DataFrame(info_CA, columns=header)
# print(df)

# df_csv = pd.read_csv('./raw_salaries/salaries_ca.csv')
# for i in range(len(header)):
#     df_csv[header[i]] = df[header[i]]

# df_csv = df_csv.drop(['url', 'Unnamed: 0'], axis=1)
# df_csv.to_csv('./raw_salaries/salaries_ca_info.csv')

# Scrape US
pages = range(1, 6960)
fps_US = ['./salaries_info_US/page{page}.html'.format(page=page) for page in pages]
info_US = get_salary_info_for_all_pages(fps_US)
df = pd.DataFrame(info_US, columns=header)

df_csv = pd.read_csv('./raw_salaries/salaries_us.csv')
for i in range(len(header)):
    df_csv[header[i]] = df[header[i]]

df_csv = df_csv.drop(['url', 'Unnamed: 0'], axis=1)
df_csv.to_csv('./raw_salaries/salaries_us_info.csv')