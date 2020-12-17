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
    feature = 'Amazon DVDs'
    bar = create_plot(feature)
    return render_template('index.html', plot=bar)

def create_plot(feature):
    if feature == 'Amazon DVDs':
        x = DVDs
        y = Prices
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'], # assign x as the dataframe column 'x'
                y=df['y']

            )




        ]

        fig = go.Figure(data=[go.Bar(x=df['x'], y=df['y'],
                                     )])
        # Customize aspect
        fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                          marker_line_width=3.5, opacity=0.6)

        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_layout(title_text='DVDs sortis lors du dernier mois',
                yaxis=dict(
                    title='Prix (dollars)',
                    titlefont_size=16,
                    tickfont_size=14,
        ))
        fig.update_layout(
            autosize=False,
            width=1300,
            height=700,
        )






    elif feature=='IMDB movies':
        colors = ['lightslategray', ] * 5
        x = movies_name
        y = movies_rating
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'],  # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]

        fig = go.Figure(data=[go.Bar(x=df['x'], y=df['y'],
                                     )])
        # Customize aspect
        fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                          marker_line_width=3.5, opacity=0.6,),

        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_layout(title_text='TOP 10 films de 2019',
                          yaxis=dict(
                              title='Metascore',
                              titlefont_size=16,
                              tickfont_size=14,
                          ))
        fig.update_layout(
            autosize=False,
            width=1300,
            height=700,
        )

    elif feature == 'Amazon movies':
        x = prime_name
        y = prime_reviews
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
              go.Bar(
                    x=df['x'],  # assign x as the dataframe column 'x'
                    y=df['y']
                )
            ]

        fig = go.Figure(data=[go.Bar(x=df['x'], y=df['y'],
                                     )])
        # Customize aspect
        fig.update_traces(marker_color='lightslategray', marker_line_color='rgb(8,48,107)',
                          marker_line_width=3.5, opacity=0.6)

        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_layout(title_text='Films proposés par Amazon Prime',
                          yaxis=dict(
                              title='Nombre de reviews',
                              titlefont_size=16,
                              tickfont_size=14,
                          ))
        fig.update_layout(
            autosize=False,
            width=1300,
            height=700,
        )


    elif feature == 'Amazon VGs':
        x = editor_name
        y = editor_occurence
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
                go.Scatter(
                        x=df['x'],  # assign x as the dataframe column 'x'
                        y=df['y']
                    )
                ]

        fig = go.Figure(data=[go.Scatter(x=df['x'], y=df['y'],
                                     )])
        # Customize aspect
        fig.update_traces(marker_color='crimson', marker_line_color='rgb(8,48,107)',
                          marker_line_width=3.5, opacity=0.6)

        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_layout(title_text='Editeurs jeux videos dernier mois',
                          yaxis=dict(
                              title='Nombre de jeux sortis',
                              titlefont_size=16,
                              tickfont_size=14,
                          ))
        fig.update_layout(
            autosize=False,
            width=1300,
            height=700,
        )




    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/bar', methods=['GET', 'POST'])
def change_features():

    feature = request.args['selected']
    graphJSON= create_plot(feature)




    return graphJSON

if __name__ == '__main__':
    app.run()
