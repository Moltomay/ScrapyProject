# Web scrapping project with scrapy

## Table of contents
* [General info](#general-info)

* [Technologies](#Technologies)

* [Setup](#setup)

* [Heroku](#Heroku)

* [Result](#Result)

## General info
The idea behind the project is to scrape data from IMDB and Amazon websites and then store this data in CSV files, on which we will apply some visualisations. Then we will deploy a FLASK application with our visualisations on Heroku. This guideline is about how to run the Flask application as well as deploying it to Heroku. 

## Technologies

Project is created with:
* Python version: 3 or more
* PyCharm : community edition
* Scrapy

## Setup 

To run this project locally follow the steps below : 

1- Clone the repo.

2- Open the project in PyCharm.

3- Install the required libraries from the PyCharm terminal : ``` $ pip install -r requirements.txt ```

4- Run FirstDashboard.py

## Heroku Deployment

To deploy this project on Heroku follow the steps below : 

1- Create a Heroku account if you don't have one.

2- Create a new application.

3- Choose Heroku Git as the deployment method.

4- Install Heroku CLI.

5- Inside the PyCharm terminal enter the following commands : 

``` 
$ heroku login 
$ git init 
$ heroku git:remote -a yourAppName
$ git add .
$ git commit -am "commit message"
$ git push heroku master

```
## Result 

![Result Heroku](https://ibb.co/RB7n322)



