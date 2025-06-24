import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# La ruta al chromedriver ya no es necesaria, Selenium la gestionará automáticamente
# CHROMEDRIVER_PATH = os.path.join('chromedriver-mac-x64', 'chromedriver')

# Leer contactos
contactos = pd.read_csv('contacts.csv', sep=';', header=None, names=['nombre', 'telefono'])
mensaje_base = "Hola {nombre}, este es un mensaje personalizado para ti."

# Configuración de Selenium
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=./chrome_selenium_profile')
# El Service ya no se pasa explícitamente
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com')

# Ya no es necesario el input si la sesión se guarda en el perfil
# input("Escanea el código QR en WhatsApp Web y presiona Enter aquí cuando estés listo...")

time.sleep(5)

for idx, row in contactos.iterrows():
    nombre = row['nombre']
    telefono = str(row['telefono'])
    if not telefono.startswith('+'):
        telefono = '+{}'.format(telefono)
    mensaje = mensaje_base.format(nombre=nombre)
    print(f"Enviando a {nombre} ({telefono}): {mensaje}")

    # Abrir chat con el número
    url = f'https://web.whatsapp.com/send?phone={telefono}&text={mensaje}'
    driver.get(url)
    time.sleep(10)  # Esperar a que cargue el chat

    # Esperar y buscar el botón de enviar y hacer click
    try:
        wait = WebDriverWait(driver, 15)
        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Enviar"]')))
        send_button.click()
        print(f"Mensaje enviado a {nombre}")
    except Exception as e:
        print(f"No se pudo enviar mensaje a {nombre}: {e}")
    time.sleep(5)  # Espera entre mensajes

print("Mensajes enviados.")
driver.quit() 