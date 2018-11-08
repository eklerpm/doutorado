
import gpxpy
import matplotlib.pyplot as plt
import datetime
from geopy import distance
from math import sqrt, floor
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import haversine

# classe responsavel por abrir arquivos em formato gpx e importar para pandas DataFrame
class GerenciadorArquivos:
    def __init__(self):
    	print("Construtor")
     


    def abrirArquivo(self):
        print("Abrir arquivo")
        gpx_file = open('0.gpx.res.gpx', 'r')
        gpx = gpxpy.parse(gpx_file)
        tracks = len(gpx.tracks)
        segments = len(gpx.tracks[0].segments)
        points = len(gpx.tracks[0].segments[0].points)
        data = gpx.tracks[0].segments[0].points

        print(tracks)
        print(segments)
        print(points)

        i = 0;

        df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])

        for point in data:
        	i = i + 1
        	print("entrou")
        	df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation, 'time' : point.time}, ignore_index=True)
        	#df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : i, 'time' : point.time}, ignore_index=True)

        
        print(df)
        plt.plot(df['lon'], df['lat'])
        #plt.show()
       # plt.plot(df['time'], df['alt'])
        #plt.show()

        print("terminou")

#        _data = [go.Scatter3d(x=df['lon'], 
#        y=df['lat'], z=df['alt'], mode='lines')]
#        py.iplot(_data)

g = GerenciadorArquivos()

g.abrirArquivo()