# Glassdoor Data Scientist Salary Prediction

## Team Members
Elisa Du, Jack Ellis, Sasha Nanda

## Project Introduction
The goal of this project is to predict the annual salary (in CAD) for data science job positions. Job description data (as of November 2020) and company-specific salary data, along with company information (e.g. type, location, sector), were scraped from the Glassdoor site for each of the 3 countries: Canada, U.K., and the U.S., using exhaustive keyword searches: 'Junior Data Scientist', 'Senior Data Scientist', and 'Data Scientist'.

The datasets were merged and cleaned. The top twenty 1-, 2-, and 3-gram word features were engineered from the job description corpus. Some other features used for prediction were: job location, type of position (i.e. senior, junior, lead, and general data scientist), cash/stock bonuses, as well as company sector, type, and size. Models fitted are: 1) lasso- and 2) ridge-regularized linear regression 3) linear regression with forward selection. Mean squared error was used to evaluate prediction accuracy, with ridge-regularized linear regression having the lowest MSE.


## Report and slides
- Report can be found in `products/writing/report.pdf`
- Presentation slides can be found [here](https://docs.google.com/presentation/d/12QJ5WKs255s-w3jR9nlIg5pBfg6PZkY6EKdJThlRlgM/edit?usp=sharing).

## How to use the repo
1. Clone the repo. If needed, instructions can be found [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).    

2. In cloned directory install required packages using
```
pip install -r requirements.txt
```

## Workflow
![Workflow](sta2453_workflow.png)

## File directory

1. Scraping Glassdoor data: [scraping ](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/scraping) and [parsing](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/parsing) code folders.
2. Cleaning and Merging Data: [cleaning](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/cleaning) and [merging](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/merging) code folders.
6. Exploratory data analysis: [raw code](https://github.com/sashananda/sta_project_1/tree/main/code/raw_code) and [exploration](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/exploration) code folders.
7. Feature Word Engineering: script [here](http://localhost:8889/notebooks/Desktop/STA2453_Fall2020/Project%201%20-%20Glassdoor%20web%20scraping/Github%20_project1_STA2453/sta_project_1/code/raw_code/NLP/DescriptionAnalysis.ipynb).
8. Model Training & Evaluation: [Preprocessing](https://github.com/sashananda/sta_project_1/tree/main/code/final_code/Preprocessing) code folder.


*More detailed scripts and data documentation see below.*

### 1. Scraping data

- Raw scraped data see `raw_data` folder

*Scripts:*

*Note: First 2 scripts require `Chromedriver.exe` (for dynamic web page) backed by `Selenium` library, found in repo. Rest of the scraping scripts use the `BeautifulSoup` library.*

- `elisa_scrape_us.ipynb`: scrape U.S. job listings
- `jack_scrape_canada.ipynb`, `jack_scrape_canada2.ipynb`: scrape Canada job listings
- `scrape.py`, `scrape_additional_company_info.py`, `scrape_company_info.py`, `scrape_salaries.py`: scrape salary (e.g. salary, base pay, cash/stock bonuses) and company data
- `parse_xx.py`: parsing html and getting info


### 2a. Cleaning data
- **Final cleaned dataset (with all features):** `salaries_descriptions_locations_gramcounts.csv`

- **Train and test data (with some features removed), normalized and unnormalized**
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

### 2b. Merging data

-`Merging_Company_Location.ipynb`: merge company location with rest of the data

-`merge_salaries_and_job_descriptions.ipynb`: merge company and salary data, with job descriptions and job position names

### 3. EDA
- `wordcloud_[job title].png`: wordclouds by job positions

*Scripts*:
- `correlation.ipynb`: correlation matrix between continuous variables and salary (response variable)
- `wordcloud.ipynb`: generate Wordclouds from job description corpus (by job position)


### 4. Analysis/NLP
- `Position_[..].pdf`: plots of salary by job titles

*Scripts:*
- `DescriptionAnalysis.ipynb`: generate N-gram features and append top 20 as 1-hot encoded vectors to data
- `Position_Exploratory_Analysis.ipynb`: analyze how salary differed by job titles

### 5. Fitting models and generating predictions
- `[Model name]_FeatureImportance.pdf`: feature importance plot from regression models
- `[Model name]_Predictions.pdf`: plot true vs. predicted salary

*Scripts:*
- `Preprocessing.ipynb`: getting data ready for model fitting (e.g. mapping job position to integers, removing missing values, normalizing data)
- `Training_Testing.ipynb`: fitting 3 models and generating predictions and feature weights, and feature importance plots
