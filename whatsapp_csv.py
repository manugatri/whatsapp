import pandas as pd
import webbrowser
import time
import urllib.parse
import pyautogui

# Importar Lista de nombres y números de un csv
df = pd.read_csv('/ruta/al/archivo/archivo.csv')
nombres = df['Nombre'].tolist()
numeros = df['Telefono'].tolist()


# Mensaje a enviar
mensaje = "Hola {nombre}, le recordamos que esta disponible el recibo anual de la Associación de vecinos. Por favor, pase a recogerlo por la oficina."

# Iterar sobre cada número
for i, numero in enumerate(numeros):
    # Convertir el número a string si es necesario
    numero = str(numero)
    # si el numero no empiza por cero 0 o + agregar +34
    if not (numero.startswith("0") or numero.startswith("+")):
        numero = "+34" + numero
    print(f"📨 Enviando a {numero}...")

    # Personalizar el mensaje con el nombre
    mensaje_personalizado = mensaje.format(nombre=nombres[i])
    # Codificar el mensaje para la URL
    mensaje_encoded = urllib.parse.quote(mensaje_personalizado)
    url = f"https://wa.me/{numero}?text={mensaje_encoded}"

    # Abre WhatsApp con el mensaje
    webbrowser.open(url)

    # Esperar a que se cargue WhatsApp
    time.sleep(10)

    # Pulsar enter para enviar
    pyautogui.press('enter')
    print(f"✅ Mensaje enviado a {nombres[i]} {numero}.")

    # Esperar antes de pasar al siguiente (cerrar pestaña, o dejarla activa)
    time.sleep(5)
