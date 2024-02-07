import bs4
import requests

#URL sin numero de pag
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

#lista de libros con 4 o 5 estrellas
titulos_rating_alto = []

#iterar paginas
for pag in range(1, 51):
    #Crear sopa de cada pag
    url_de_pag = url_base.format(pag)

    resultado = requests.get(url_de_pag)
    sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

    #Seleccionar datos de libros

    libros = sopa.select(".product_pod")

    #iterar en libros

    for libro in libros:

        #Checar si tiene 4 o 5 estrellas

        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            #Guardar titulo en variable
            titulo_libro = libro.select("a")[1]["title"]


            #agregar libro a lista

            titulos_rating_alto.append(titulo_libro)


#Ver libros de rating alto
            
for t in titulos_rating_alto:
    print(t)