from django.shortcuts import render
from .machine_learning import train_linear_regression_model
import pandas as pd
from django import template
from django.shortcuts import HttpResponse
import pandas as pd
import json
import streamlit as st
from datetime import time
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objs  as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_diabetes
from math import sqrt
import plotly.express as px
from PIL import Image
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import numpy as np

def predict_view(request):
    if request.method == 'POST':
        # Get input data from user
        x = request.POST.get('x')
        
        # Load the dataset
        data = pd.read_csv('Database.csv')

        print(data)

        # Split the data into training and testing sets
        X_train = data[['x']]
        y_train = data['y']

        # Train the model
        model = train_linear_regression_model(X_train, y_train)

        # Make a prediction on the input data
        new_data_point = [[x]]
        predicted_value = model.predict(new_data_point)

        # Render the result
        return render(request, 'machine/result.html', {'predicted_value': predicted_value})
    else:
        # Render the input form
        return render(request, 'machine/result.html')

def Table(request):
    df = pd.read_csv("Database.csv")
  
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'machine/table.html', context)

import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)
        
        print(df.head())
        
        # Process the dataframe and generate the graph
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['DATE'], y=df['EF'], name='stock_open'))
        fig.add_trace(go.Scatter(x=df['DATE'], y=df['AvgTemp'], name='stock_close'))
        fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
        
        # Save the HTML table to a variable
        df_table = df.to_html(index=False)
        
        # Return the rendered template with the graph and HTML table
        return render(request, 'graph.html', {'graph': fig.to_html(), 'df_table': df_table})
    return render(request, 'upload.html')
