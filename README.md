# Glassdoor Data Scientist Salary Prediction

## Team Members
Elisa Du, Jack Ellis, Sasha Nanda

## Project Introduction
The goal of this project is to predict the annual salary (in Canadian dollars) for data science job positions. Job description data (as of November 2020) and company-specific salary data, along with company information (e.g. type, location, sector), were scraped from the Glassdoor site for each of the 3 countries: Canada, U.K., and the U.S., using exhaustive keyword searches: 'Junior Data Scientist', 'Senior Data Scientist', and 'Data Scientist'. The datasets were merged and cleaned. N-gram word features were engineered from the job description data. Some other features used for prediction were: job location, type of position (i.e. senior, junior, lead, and general data scientist), cash/stock bonuses, as well as company sector, type, and size. Models fitted are: lasso and ridge regression, as well as linear regression with forward selection.

## How to use the repo
1. Clone the repo. If needed, instructions can be found [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).    

2. In cloned directory install required packages using
```
pip install -r requirements.txt
```

## Workflow
![Workflow](sta2453_workflow.png)

## File structure
Where to find scripts:
1. Scraping Glassdoor data: [scraping ](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/scraping) and [parsing](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/parsing) code folders.
2. Cleaning and Merging Data: [cleaning](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/cleaning) and [merging](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/merging) code folders.
6. Exploratory data analysis: [raw code](https://github.com/sashananda/sta_project_1/tree/main/code/raw_code) and [exploration](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/exploration) code folders.
7. Feature Word Engineering: script [here](http://localhost:8889/notebooks/Desktop/STA2453_Fall2020/Project%201%20-%20Glassdoor%20web%20scraping/Github%20_project1_STA2453/sta_project_1/code/raw_code/NLP/DescriptionAnalysis.ipynb).
8. Model Training & Evaluation: [Preprocessing](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/Preprocessing) code folder.


More detailed scripts and data documentation see below.

### Scraping data
SCRAPING
scrapesalaries: basepay, upper bound pay
scrapeadditionlinfo: benefits, headquarters,
scrape scrape company info_additional_company_info.py : get all urLS to scrape ratings, beenfits, etc.


Chromedriver.exe?

Raw data containing salary information
Final cleaned dataset is ...

### Cleaning data
- **Final cleaned dataset (with all features):** `salaries_descriptions_locations_gramcounts.csv`

- **Train and test data (with some features with NaN removed), normalized and unnormalized**
     - `train.csv`, `test.csv`
     - `train_normalized.csv`, `test_normalized.csv`

*Scripts*:
- `add_location_info.ipynb` : add location (latitude/longitude) for companies
- `add_uk_salary_col.ipynb` : debug U.K. salary column
- `check_salary_col_cleaning.ipynb`: debug salary columns for special cases (e.g. positions with hourly/monthly/yearly pay -> convert all to yearly pay)
- `clean_company_cols.ipynb`: clean company info columns
- `clean_position_canada/us/uk.ipynb`: standarize job position column for job description data - so only have 5 positions: Data Scientist Intern, Junior Data Scientist, Senior Data Scientist, Lead Data Scientist, and (general) Data Scientist.
- `clean_position_forSalaryDF.ipynb`: same as above, but for salary data
- `clean_salary_cols.ipynb`: clean all columns (other than job position)
- `final_salary_remove_outliers.ipynb`: remove salary outliers


### EDA


### Analysis/NLP

### Fitting models and generating predictions



parsing : all scripts are parsing html and grabbing the info

EXPLORATION
Position_Exploratory_Analysis.ipynb - histogramsfor positionand Salary
Untitled - DELETE

Merging
-Merging_Company_Location.ipynb - merged location w everything else
merge_salaries_and_job_descriptions.ipynb -
delete other one

Preprocessing
- see chat

Training testing
-


## Report and slides
- Report can be found in `products/writing/report.pdf`
- Presentation slides can be found [here](https://docs.google.com/presentation/d/12QJ5WKs255s-w3jR9nlIg5pBfg6PZkY6EKdJThlRlgM/edit?usp=sharing).
