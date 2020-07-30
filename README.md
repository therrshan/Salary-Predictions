# Salary-Predictions

* Created a tool that estimates data science salaries using the data from the Glass Door website.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 

### Links 
Github for Selenium scraper : https://github.com/arapfaik/scraping-glassdoor-selenium  


## Web Scraping

Modified the web scraper github repo above to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
*	Job title, Salary estimate, Job Description, Rating
*	Company, Location, Company Headquarters, Company Size
*	Company Founded Date, Type of Ownership
*	Industry, Sector, Revenue, Competitiors

## Data Cleaning
After scraping the data, the data was cleaned considering below factors:

*	took only numeric data out of salary and removed missing values
*	Simplified salary depending on type
*	removed rating out of company text 
*	Made a new column for company location and job location
*	Transformed founded date into age of company 
*	Made columns for languages defined in Job Skills
    * Python, R, excel, AWS, Spark  
*	Column for simplified job title and Seniority 

## EDA
The plots for various columns were observed for relations between them. Below are a few of the important revelations. 

![alt text](https://github.com/therrshan/Salary-Predictions/blob/master/Salaries.PNG "Salary per Positions")
![alt text](https://github.com/therrshan/Salary-Predictions/blob/master/Locations.png "Job Opportunities versus Locations")
![alt text](https://github.com/therrshan/Salary-Predictions/blob/master/Relations.png "Relations between Columns")

## Model Building 

The categorical data was transformed into dummy data and the data set was split into Test data and train data.   

Models were chosen as per the walkdown through Ken Jee on his youtube channel. Mean Absolute Error (MAE) evaluation was chosen because the salary output is not correct or incorrect
It can be evaluated as to how much the predicted salary was off by the actual amount

Used models:
*	**Multiple Linear Regression**
*	**Lasso Regression**
*	**Random Forest** 

## Model performance
The Random Forest model was way too effective as compared to the regression models
*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67




