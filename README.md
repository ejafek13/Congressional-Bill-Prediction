# Congressional-Bill-Prediction

# Overview

An analysis 20 years of bills introduced across 10 Congresses (1997-2017). Only 3.4% of the 108,000 bills in the dataset became law, and only 18% of the bills in the dataset recieved any action besides getting referred to committee.

The project involved scraping and engineering 20 years of Congressional data in an attempt to predict whether a bill will make it out of committee, and whether a bill will become a law. Assigned each bill to one of five "final status" categories based on the final action on each bill included in the dataset. Predicted if a bill would make it out of committee with 77% recall using a Random Forest Classifier. Built various other models included in this repo with varying levels of success -- overall most outcomes are hard to predict and recall rates are low while accuracy rates are high (decievingly so) because of the unbalanced classes inherent in the dataset.

# Process
I used the ProPublica API to scrape congressional bills from 1997 to 2017, or Congresses 105-115. This data was combined with MIT researcher Christ Stewart's congressional committee data to create the final dataset. 

This blog describes the data gathering, cleaning, and engineering process: (https://medium.com/@elizabethjafek/scraping-and-wrangling-congressional-bill-data-bddc53b5cc93)

This blog describes the modeling process: (https://medium.com/@elizabethjafek/predicting-the-path-of-congressional-bills-cf1105f7c6c8)

# Directory 
Data Scrape Function

Data Combining Function

EDA and Data Wrangling

Statistics -- correlation/association scores and p-values for many variables

Adding Additional Features (majority/minority in each Congress analyzed)

Models -- Jupyter Notebooks with various models
  1) Modeling if bill becomes law
  2) Modeling if any action taken on bill besides being referred to committee -- includes second stage model
  3) Modeling which of the five categories a bill will end up in
  4) Modeling which of three categories a bill will end up in (referred to committee, action taken, law)

Presentation


# Resources
Link to Propublica API (https://projects.propublica.org/api-docs/congress-api/)

Link to MIT dataset (http://web.mit.edu/cstewart/www/data/data_page.html)
