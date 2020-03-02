import os
from pathlib import Path
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Driver a utilizar
driver = webdriver.Chrome(ChromeDriverManager().install())

# Cantidad de páginas a recorrer
pages = 2

for page in range(1, pages):
  url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"
  # Abro la URL
  driver.get(url)

  # Cantidad de elementos
  items = len(driver.find_elements_by_class_name("quote"))
  data = []
  for item in range(items):
    # Obtengo las frases
    quotes = driver.find_elements_by_class_name("quote")
    for quote in quotes:
      # Extraigo frase y autor
      quote_text = quote.find_element_by_class_name('text').text
      author = quote.find_element_by_class_name('author').text

      # Agrego info al array
      data.append([quote_text, author])

  # Convierto array a dataframe con Pandas
  df = pd.DataFrame(data, columns=['quote','author'])
  # Almaceno el dataframe como csv
  df.to_csv(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data.csv')

# Cierro el driver
driver.close()