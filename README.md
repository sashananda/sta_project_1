# Glassdoor Data Scientist Salary Prediction

## Team Members
Elisa Du, Jack Ellis, Sasha Nanda

## Project Introduction
The goal of this project is to predict the annual salary (in Canadian dollars) for a data science role. Job description data (as of November 2020) and company-specific salary data, along with company information, were scraped from the Glassdoor site for each of the 3 countries: Canada, U.K., and the U.S., using exhaustive keyword searches: 'Junior Data Scientist', 'Senior Data Scientist', and 'Data Scientist'. The datasets are merged and cleaned. N-gram word features were engineered from the job description data. Some other features used for prediction were: job location, type of position (e.g. senior, junior, lead), cash/stock bonuses, as well as company sector, type, and size. Models fitted include lasso and ridge regression, as well as linear regression with forward selection.

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

## Getting and cleaning datasets

Raw data containing salary information
Final cleaned dataset is ...

## Fitting and saving models


## Report and slides
- Report can be found in `products/writing/report.pdf`
- Presentation slides can be found [here](https://docs.google.com/presentation/d/12QJ5WKs255s-w3jR9nlIg5pBfg6PZkY6EKdJThlRlgM/edit?usp=sharing).
