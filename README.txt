Reto TAPPX 

Instalar las librerías necesarias: 
!pip install -U sentence-transformers 

!pip install termcolor 
!pip install spacy 
!pip install numpy 

Nota: Si se ejecuta localmente se debe correr este comando e instalar la versión en español. 
python3 -m spacy download es_core_news_md 

Importar las funciones de las librerías: 

from termcolor import colored #para utilizar las propiedades de color 
from tqdm import tqdm #bar 
import json # leer los Json. 
import pandas as pd # Generar el DataFrame. 
import numpy as np # realizar el cálculo del coseno. # para calcula el coseno 
from sentence_transformers import SentenceTransformer # se utiliza para implementar el modelo IA para comparar la similitud entre textos. 
import spacy # para extraer la keywords de los textos. # para implementar el modelo IA para extraer la Keywords. 

Nota: Si se ejecuta en un entorno como el google colab se debe poner en este orden no es necesario agregarlo cuando trabajas localmente. 
!python -m spacy download es_core_news_md #Descarga el modelo en español 

Cargar el Modelo IA para extraer la keywords 

nlp = spacy.load('es_core_news_md')# Cargar el modelo de lenguaje en español 

Cargar el Modelo IA para el análisis del texto 

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')  

Definición de la biblioteca más relevantes 

La biblioteca sentence_transformers es una biblioteca de procesamiento de lenguaje natural (PLN) de código abierto que proporciona una forma fácil de entrenar y utilizar modelos de representación de oraciones para tareas de clasificación de texto, agrupamiento y recuperación de información. 
La clase SentenceTransformer es una clase que se utiliza para cargar y utilizar modelos pre-entrenados de representación de oraciones. Estos modelos preentrenados son capaces de convertir frases y oraciones en vectores de alta dimensionalidad que pueden ser utilizados en varias tareas de PLN. 

Función para abrir Json 
	def read_json(filename) 

Estas dos funciones se encargar de agregar al diccionario otro diccionario que contiene el id del video y su score 
	def push_dic_dic(dic, id_article, id_video, score) 

     def push_dic(dic, id_article) 

Función para extraer las Keywords 
Esta función permite extraer las palabras claves de un texto. 
	def search_keywords(text) 

Funciones para analizar los textos y calcular el coseno: 
La función se encarga de calcular la similitud entre un artículo con respecto al archivo de videos. 
	def score(df, article) 

Esta función se encarga de hacer el análisis de todos los artículos que contiene el archivo.json 
	def analyze(df_video) 

Main: 

El main se encarga de hacer todos los procesos que son apertura de cada uno de los archivos, la extracción de palabras claves y la relación que tiene cada uno de los artículos con los videos su salida es un archivo data.json que su contenido es un diccionario con la relación de artículos y dos videos. 

 

La relación del articulo con respecto a los videos se hace a través de un sistema de puntuación que nos retorna la función score esta evalúa del 0 al 10 donde 10 es la máxima relación que puede tener un video con respecto al artículo.  

Autores del proyecto: 
María Yamileth Contreras Rivas 
Micaela Rollo 
Dannyel Humberto Cortés Romero 