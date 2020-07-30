from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("/home/darshan/chromedriver")

url = "https://www.glassdoor.co.in/Job/data-scientist-jobs-SRCH_KO0,14.htm"

driver.get(url)
jobs = []

while len(jobs) < 1000:

    try:
        driver.find_element_by_class_name("selected").click()
    except ElementClickInterceptedException:
        pass

    time.sleep(.1)

    try:
        driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
        print(' x out worked')
    except NoSuchElementException:
        print(' x out failed')
        pass 

    job_buttons = driver.find_elements_by_class_name("jl")  #jl for Job Listing. These are the buttons we're going to click.
    for job_button in job_buttons:  

        print("Progress: {}".format("" + str(len(jobs)) + "/" + str(1000)))
        if len(jobs) >= 1000:
            break

        job_button.click()  #You might 
        time.sleep(1)
        collected_successfully = False
        
        while not collected_successfully:
            try:
                company_name = driver.find_element_by_xpath('.//div[@class="employerName"]').text
                location = driver.find_element_by_xpath('.//div[@class="location"]').text
                job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                collected_successfully = True
            except:
                time.sleep(5)

        try:
            salary_estimate = driver.find_element_by_xpath('.//span[@class="gray salary"]').text
        except NoSuchElementException:
            salary_estimate = -1 #You need to set a "not found value. It's important."
        
        try:
            rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
        except NoSuchElementException:
            rating = -1 #You need to set a "not found value. It's important."

        try:
            driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()

            try:
                #<div class="infoEntity">
                #    <label>Headquarters</label>
                #    <span class="value">San Francisco, CA</span>
                #</div>
                headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
            except NoSuchElementException:
                headquarters = -1

            try:
                size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
            except NoSuchElementException:
                size = -1

            try:
                founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
            except NoSuchElementException:
                founded = -1

            try:
                type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
            except NoSuchElementException:
                type_of_ownership = -1

            try:
                industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
            except NoSuchElementException:
                industry = -1

            try:
                sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
            except NoSuchElementException:
                sector = -1

            try:
                revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
            except NoSuchElementException:
                revenue = -1

            try:
                competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
            except NoSuchElementException:
                competitors = -1

        except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
            headquarters = -1
            size = -1
            founded = -1
            type_of_ownership = -1
            industry = -1
            sector = -1
            revenue = -1
            competitors = -1

        jobs.append({"Job Title" : job_title,
        "Salary Estimate" : salary_estimate,
        "Job Description" : job_description,
        "Rating" : rating,
        "Company Name" : company_name,
        "Location" : location,
        "Headquarters" : headquarters,
        "Size" : size,
        "Founded" : founded,
        "Type of ownership" : type_of_ownership,
        "Industry" : industry,
        "Sector" : sector,
        "Revenue" : revenue,
        "Competitors" : competitors})

    try:
        driver.find_element_by_xpath('.//li[@class="next"]//a').click()
    except NoSuchElementException:
        print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
        break


df = pd.DataFrame(jobs)
df.to_csv("data.csv", index = False)