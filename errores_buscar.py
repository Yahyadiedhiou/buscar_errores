import os
import time

#se importa este modulo porq el sistema de archivos en el que navegaremos 
# es uno de los componentes de os

def buscar_errores(place_to_search):
    for errores in place_to_search:
        return errores
    with open ("//C:/Carpeta1/carpeta2/search_here/errores.txt","w",encoding="utf-8") as file:
     file.write(errores)

#lo de arriba es que una vez que los encuentre , que los escriba en un txt

#pero me falta definir que es un "error" que el script entienda que buscar

errores=input("aqui pones el error que quieras buscar: ")

#definido lo que es un error 

#ahora falta saber donde buscar el error o los errores

#debe buscarlo en los directorios, asi que debe navegar en el sistema operativo
# dentro del sistema de archivos, uno de los componentes de os

place_to_search=("//C:/Carpeta1/carpeta2/search_here/errores.txt":carpeta1/carpeta2/carpeta3/carpeta4)

place_to_search=os.walk

#os.walk te permite navegar en los directorios 

# los errores se han escrito, osea existen , ahora necesitan un prog 

# guardar los errores un un fichero txt que se cerrara en 10 minutos 
#import time 

def encontrar_errores():
   place_to_search=("//C:/Carpeta1/carpeta2/search_here/errores.txt":carpeta1/carpeta2/carpeta3/carpeta4)

   place_to_search=os.walk


def guardar_errores(errores):
   with open("errores.txt","a") as file:
      texto=file.write(errores.txt)



#---------------------------------------------------------------
#----------------------------------------------------------------


import os

def buscar_errores(place_to_search):
    for errores in place_to_search:
        return errores
    with open ("//C:/Carpeta1/carpeta2/search_here/errores.txt","w",encoding="utf-8") as file:
     file.write(errores)

    place_to_search=("//C:/Carpeta1/carpeta2/search_here/errores.txt":carpeta1/carpeta2/carpeta3/carpeta4)

    place_to_search=os.walk
    def encontrar_errores():
        place_to_search=("//C:/Carpeta1/carpeta2/search_here/errores.txt":carpeta1/carpeta2/carpeta3/carpeta4)

        place_to_search=os.walk


        def guardar_errores(errores):
         with open("errores.txt","a") as file:
          texto=file.write(errores.txt)



errores=input("aqui pones el error que quieras buscar: ")


