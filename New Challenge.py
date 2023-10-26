from bs4 import BeautifulSoup

import requests

html = requests.get("https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios")

soup =BeautifulSoup(html,'html.parser')

print(soup.prettify())


fec_alta = soup.find ("span, class_=block _margin-b-5 -gray")
print (fec_alta.string)

user_name = soup.find ("span, class_=block _margin-b-5 -gray")
print (user_name.string)

codigo_zip = soup.find ("span, class_=block _margin-b-5 -gray")
print (codigo_zip.string)

credit_card_num = soup.find ("span, class_=block _margin-b-5 -gray")
print (credit_card_num.string)

credit_card_ccv = soup.find ("span, class_=block _margin-b-5 -gray")
print (credit_card_ccv.string)

cuenta_numero = soup.find ("span, class_=block _margin-b-5 -gray")
print (cuenta_numero.string)

direccion = soup.find ("span, class_=block _margin-b-5 -gray")
print (direccion.string)

geo_latitud = soup.find ("span, class_=block _margin-b-5 -gray")
print (geo_latitud.string)

geo_longitud = soup.find ("span, class_=block _margin-b-5 -gray")
print (geo_longitud.string)

color_favorito = soup.find ("span, class_=block _margin-b-5 -gray")
print (color_favorito.string)

foto_dni = soup.find ("span, class_=block _margin-b-5 -gray")
print (foto_dni.string)

ip = soup.find ("span, class_=block _margin-b-5 -gray")
print (ip.string)

auto = soup.find ("span, class_=block _margin-b-5 -gray")
print (auto.string)

auto_modelo = soup.find ("span, class_=block _margin-b-5 -gray")
print (auto_modelo.string)

auto_tipo = soup.find ("span, class_=block _margin-b-5 -gray")
print (auto_tipo.string)

auto_color = soup.find ("span, class_=block _margin-b-5 -gray")
print (auto_color.string)

cantidad_compras_realizadas = soup.find ("span, class_=block _margin-b-5 -gray")
print (cantidad_compras_realizadas.string)

avatar = soup.find ("span, class_=block _margin-b-5 -gray")
print (avatar.string)

fec_birthday = soup.find ("span, class_=block _margin-b-5 -gray")
print (fec_birthday.string)

id = soup.find ("span, class_=block _margin-b-5 -gray")
print (id.string)


