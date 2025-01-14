import requests
from bs4 import BeautifulSoup
import os
import re

# --- 1. Configuración general ---

# --- 2. Función para "limpiar" el nombre a fin de usarlo como archivo ---
def limpiar_nombre_archivo(nombre):
    """
    Reemplaza caracteres que no sean alfanuméricos, espacios o guiones
    por un guion bajo, evitando problemas al crear el archivo.
    """
    nombre_limpio = re.sub(r"[^\w\s-]", "_", nombre)  # Sustituye símbolos raros por "_"
    nombre_limpio = nombre_limpio.strip().replace(" ", "_")  # Cambia espacios por "_"
    return nombre_limpio

DIRECTORIO_SALIDA = "fotos_jugadores"
os.makedirs(DIRECTORIO_SALIDA, exist_ok=True)

clubs = [14,2,3,591,10,592,13,16,57,28,8,5,624,22,9,25,4,12]
for club in clubs:

    URL = f"https://acb.com/club/plantilla/id/{club}/temporada_id/2023"


    # --- 3. Descarga del contenido HTML ---
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"No se ha podido acceder a la página. Código de estado: {response.status_code}")
        exit()

    soup = BeautifulSoup(response.text, "html.parser")

    # --- 4. Localizamos los contenedores de los jugadores en la plantilla ---
    contenedores_jugadores = soup.find_all("article", class_="caja_miembro_plantilla caja_jugador_medio_cuerpo")

    # --- 5. Recorremos cada contenedor y extraemos el nombre y la URL de la imagen ---
    for contenedor in contenedores_jugadores:
        # 5.1. Extraemos la imagen del jugador
        img_tag = contenedor.find("img")
        if not img_tag:
            continue  # Si no hay imagen, saltamos
    
        imagen_url = img_tag.get("src")
    
        # 5.2. Extraemos el nombre del jugador
        # Dentro de ".datos .nombre" está el <a> con el nombre.
        datos_div = contenedor.find("div", class_="datos")
        if not datos_div:
            continue
    
        nombre_div = datos_div.find("div", class_="nombre")
        if not nombre_div:
            continue
    
        # El nombre real puede estar en el propio texto o dentro de <a>:
        nombre_jugador_tag = nombre_div.find("a")
        if nombre_jugador_tag and nombre_jugador_tag.text:
            nombre_jugador = nombre_jugador_tag.text.strip()
        else:
            # Si no hubiera <a>, intentamos con .text
            nombre_jugador = nombre_div.text.strip()
    
        # 5.3. Limpiamos el nombre para usarlo como archivo (evitamos caracteres problemáticos).
        nombre_archivo = limpiar_nombre_archivo(nombre_jugador)
        nombre_archivo += ".jpg"  # Extensión para la imagen
    
        # 5.4. Descargamos y guardamos la imagen
        if imagen_url.startswith("//"):
            # Si la URL es relativa tipo //static.acb..., agregamos https:
            imagen_url = "https:" + imagen_url
        try:
            img_resp = requests.get(imagen_url, stream=True)
            if img_resp.status_code == 200:
                ruta_fichero = os.path.join(DIRECTORIO_SALIDA, nombre_archivo)
                with open(ruta_fichero, "wb") as f:
                    f.write(img_resp.content)
                print(f"Guardada: {ruta_fichero}")
            else:
                print(f"No se pudo descargar {imagen_url} (status: {img_resp.status_code})")
        except Exception as e:
            print(f"Ocurrió un error al descargar {imagen_url}: {e}")

