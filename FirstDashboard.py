import json

import pandas as pd
import plotly
import plotly.graph_objs as go
from flask import Flask, render_template, request

app = Flask(__name__)


data = pd.read_csv("items.csv")
data=data.drop([0,1,3,17,18],axis=0)
data=data.sort_values(by=['product_price'])
new_data=data[0:5]
DVDs=new_data.iloc[:,0]
Prices=new_data.iloc[:,1]

movies = pd.read_csv("movies.csv")
movies=movies.sort_values(by=['movie_rating'])
new_data=movies.drop([17,9,16,18,1,15,6,10,7,14],axis=0)
movies_name=new_data.iloc[:,0]
movies_rating=new_data.iloc[:,1]

prime = pd.read_csv("prime.csv")
prime=prime.drop([1,2,3,5,8,10,12,13],axis=0)
prime=prime.reindex([4, 15, 9, 6,11,0,14,7])
prime.index = range(8)
prime_name=prime.iloc[:,0]
prime_reviews=prime.iloc[:,1]

prime = pd.read_csv("editors.csv")
prime=prime.drop([3,6,12,15],axis=0)
df1=prime['Editor'].value_counts()
df2=pd.DataFrame(df1)
df2.reset_index(level=0, inplace=True)
editor_name=df2.iloc[:,0]
editor_occurence=df2.iloc[:,1]


@app.route('/')
def index():
    feature = 'Amazon plot'
    bar = create_plot(feature)
    return render_template('index.html', plot=bar)

def create_plot(feature):
    if feature == 'Amazon plot':
        x = DVDs
        y = Prices
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'], # assign x as the dataframe column 'x'
                y=df['y']

            )




        ]




    elif feature=='IMDB plot':
        x = movies_name
        y = movies_rating
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'],  # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]

    elif feature == 'Third plot':
        x = prime_name
        y = prime_reviews
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
              go.Bar(
                    x=df['x'],  # assign x as the dataframe column 'x'
                    y=df['y']
                )
            ]

    elif feature == 'Fourth plot':
        x = editor_name
        y = editor_occurence
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
                go.Bar(
                        x=df['x'],  # assign x as the dataframe column 'x'
                        y=df['y']
                    )
                ]




    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/bar', methods=['GET', 'POST'])
def change_features():

    feature = request.args['selected']
    graphJSON= create_plot(feature)




    return graphJSON

if __name__ == '__main__':
    app.run()
