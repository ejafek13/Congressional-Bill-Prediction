# Congressional-Bill-Prediction

# Overview

An analysis 20 years of bills introduced across 10 Congresses (1997-2017).

Scraped and engineered 20 years of Congressional data in an attempt to predict whether a bill will make it out of committee, and whether a bill will become a law. Predicted if a bill would make it out of committee with 77% recall. 

# Process
I used the ProPublica API to scrape congressional bills from 1997 to 2017, or Congresses 105-115. This data was combined with MIT researcher Christ Stewart's congressional committee data to create the final dataset. 

This blog describes the data gathering, cleaning, and enginnering process: (https://medium.com/@elizabethjafek/scraping-and-wrangling-congressional-bill-data-bddc53b5cc93)

This blog describes the modeling process: (https://medium.com/@elizabethjafek/predicting-the-path-of-congressional-bills-cf1105f7c6c8)

# Directory 
Data Scrape Function

Data Combining Function

EDA and Data Wrangling

Adding Additional Features (majority/minority in each Congress analyzed)

Models -- Jupyter Notebooks with various models

Presentation


# Resources
Link to Propublica API (https://projects.propublica.org/api-docs/congress-api/)

Link to MIT dataset (http://web.mit.edu/cstewart/www/data/data_page.html)
