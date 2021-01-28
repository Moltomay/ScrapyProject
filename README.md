# Flask application to visualise scrapped data with scrapy

## Table of contents
* [General info](#general-info)

* [Technologies](#Technologies)

* [Setup](#setup)

* [Heroku](#Heroku)

* [Demo](#Demo)

## General info
The idea behind the project is to scrape data from IMDB and Amazon websites and then store this data in CSV files, on which we will apply some visualisations with the help of the plotly library. Then we will deploy a FLASK application with our visualisations on Heroku.

So to summarize, the steps are as follow : 

1- Scrap data with Scrapy.

2- Store data in CSV files.

3- Clean the CSV files and apply visualisations with Plotly.

4- Deploy Flask application with the visualisations.

This guideline is about how to run the Flask application locally as well as deploying it to Heroku.

## Technologies

Project is created with:
* Python version: 3 or more
* PyCharm : community edition
* Scrapy
* Plotly
* Flask

## Setup 

To run this project locally follow the steps below : 

1- Clone the repo.

2- Open the project in PyCharm.

3- Install the required libraries from the PyCharm terminal : ``` $ pip install -r requirements.txt ```

4- Run FirstDashboard.py

## Heroku

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
## Demo

[Project link](https://web-semantique.herokuapp.com)

![alt text](https://user-images.githubusercontent.com/16072777/104095678-81231a00-5298-11eb-8d3f-82fa1544a715.png)



