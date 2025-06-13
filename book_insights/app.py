import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output
from flask import Flask, jsonify
from statsmodels.nonparametric.smoothers_lowess import lowess

# Load dataset
df = pd.read_csv("books_ascii_clean.csv")

# Flask for REST
server = Flask(__name__)

@server.route("/api/stats", methods=["GET"])
def get_stats():
    genre_price = df.groupby("genre")["price"].mean().to_dict()
    genre_rating = df.groupby("genre")["rating"].mean().to_dict()
    return jsonify({
        "avg_price_by_genre": genre_price,
        "avg_rating_by_genre": genre_rating
    })

# Dash app
app = Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("📚 Book Price Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(id='price-by-genre'),
    dcc.Graph(id='rating-by-genre'),
    dcc.Graph(id='price-vs-rating-trend'),  # Updated ID
    dcc.Graph(id='book-count-by-genre'),
    dcc.Graph(id='stock-by-genre')
])

@app.callback(
    Output('price-by-genre', 'figure'),
    Output('rating-by-genre', 'figure'),
    Output('price-vs-rating-trend', 'figure'),
    Output('book-count-by-genre', 'figure'),
    Output('stock-by-genre', 'figure'),
    Input('price-by-genre', 'id')  # dummy input
)
def update_graphs(_):
    # Box plot: Price by genre
    price_fig = px.box(df, x='genre', y='price', title='Price Distribution by Genre')

    # Bar plot: Average rating by genre
    rating_avg = df.groupby('genre')['rating'].mean().reset_index()
    rating_fig = px.bar(rating_avg, x='genre', y='rating', title='Average Rating by Genre')

    # LOWESS-smoothed trend: Rating vs Price
    df_sorted = df.sort_values("rating")
    lowess_result = lowess(df_sorted["price"], df_sorted["rating"], frac=0.3)

    trend_fig = go.Figure()

    # Smoothed line
    trend_fig.add_trace(go.Scatter(
        x=lowess_result[:, 0],
        y=lowess_result[:, 1],
        mode='lines',
        line=dict(color='firebrick', width=3),
        name='LOWESS Trend'
    ))

    # Raw data as faded dots
    trend_fig.add_trace(go.Scatter(
        x=df_sorted["rating"],
        y=df_sorted["price"],
        mode='markers',
        opacity=0.2,
        name='Raw Data',
        marker=dict(color='gray')
    ))

    trend_fig.update_layout(
        title='Smoothed Price Trend by Rating',
        xaxis_title='Rating',
        yaxis_title='Price',
        template='plotly_white'
    )

    # Bar: Book count by genre
    genre_counts = df['genre'].value_counts().reset_index()
    genre_counts.columns = ['genre', 'count']
    count_fig = px.bar(genre_counts, x='genre', y='count', title='Book Count by Genre')

    # Bar: Total stock by genre
    stock_sum = df.groupby('genre')['stock'].sum().reset_index()
    stock_fig = px.bar(stock_sum, x='genre', y='stock', title='Total Stock by Genre')

    return price_fig, rating_fig, trend_fig, count_fig, stock_fig

if __name__ == "__main__":
    app.run(debug=True)
