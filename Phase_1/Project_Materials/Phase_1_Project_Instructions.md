# Yelp API - Lab

## Objectives

You will be able to:
* Utilize Github to save your code
* Create a SQLite instance of a DB to store information from Yelp about businesses
* Create HTTP requests to get data from Yelp API
* Parse HTTP responses and insert the information into your DB
* Perform pagination to retrieve troves of data
* Write SQL queries to answer questions about your data 
* Use descriptive statistic to find any insights in your data about 

## Introduction 

Now that we've seen how the Yelp API works, it's time to put those API and SQL skills to work in order to do some basic business analysis! Taking things a step further, you'll also independently explore how to perform pagination in order to retrieve a full results set from the Yelp API!

## Problem Statement

You and your partner are looking to open a new business and trying to decide where is the best geographical area for it. You will to do some research to learn more about the potential markets you are about to enter. The data for your analysis will come primarily from Yelp's API, but you are able to bring in data from any source to augment your analysis. The business and potential markets for your business are to open to your chooisng. You must look at at least two geographical areas and compare which one you deem a better opportunity. The geographical areas that you are comparing can be two cities/towns or, for large cities, it can be two separate parts of that city (Queens vs. BK). You and your partner will decide the criteria for selecting the area to open your business, but it must be based in your data analysis.  






## Process 

A separate notebook is included to hgive you a step by step guide to complete the project.  


0. Create a Github repo to track and maintain an updated version of your code.

1. Read through the SQL questions and the API documentation to determine which pieces of information you need to pull from the Yelp API.

2. Create a DB schema with 2 tables. One for the businesses and one for the reviews.

3. Create code to:
  - Perform a search of businesses using pagination
  - Parse the API response for specific data points
  - Insert the data into your AWS DB

4. Use the functions above in a loop that will paginate over the results to retrieve all of the results. 

5. Create functions to:
  - Retrieve the reviews data of one business
  - Parse the reviews response for specific review data
  - Insert the review data into the DB

6. Using SQL, query all of the business IDs. Using the 3 Python functions you've created, run your business IDs through a loop to get the reviews for each business and insert them into your DB.

7. Write SQL queries to answer the following questions about your data.

8. Bring your data from your SQLite db into a python environment to perform futher analysis.

9. Create at least 4 data visualizations to help communicate key insights from from your analysis. 

10. Create a presentation (PowerPoint or Slideshow) that communicates your process and the findings of your analysis.

11. Clean up your code and your Github repo to clearly display the work of your project. 



Bonus Steps:  
- Place your helper functions in a package so that your final notebook only has the major steps listed.
- Rewrite your business search functions to be able take an argument for the type of business you are searching for.


 
## SQL Questions

As a itermediary step in the process, you will need to be able to write SQL queries to answer the questions below. Each group will meet with the instructor Thursday morning to review your SQL statements.  

- Which are the 5 most reviewed businesses?
- What is the highest rating recieved in your data set and how many businesses have that rating?
- What percentage of businesses have a rating greater than or  4.5?
- What percentage of businesses have a rating less than 3?
- What is the average rating of businesses that have a price label of one dollar sign? Two dollar signs? Three dollar signs? 
- Return the text of the reviews for the most reviewed business. 
- Return the name of the business with the most recent review. 
- Find the highest rated business and return text of the most recent review. If multiple business have the same rating, select the business with the most reviews. 
- Find the lowest rated business and return text of the most recent review.  If multiple business have the same rating, select the business with the least reviews. 

