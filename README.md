# WhatsApp Auto Messenger con Python y Selenium

Este proyecto permite enviar mensajes personalizados de WhatsApp a una lista de contactos almacenada en un archivo CSV, de forma completamente automática, utilizando Python y Selenium.

## Funcionalidad
- Lee una lista de contactos desde `contacts.csv` (nombre y número de teléfono).
- Personaliza el mensaje para cada contacto usando su nombre.
- Abre WhatsApp Web en una ventana de Chrome y envía los mensajes automáticamente.
- Utiliza un perfil exclusivo de Chrome para Selenium, evitando interferencias con tu navegador habitual.

## Requisitos
- Python 3.8 o superior
- Google Chrome instalado
- ChromeDriver compatible con tu versión de Chrome

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd whatsappauto
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Descarga ChromeDriver:**
   - Descarga la versión de ChromeDriver que coincida con tu versión de Google Chrome desde:
     https://googlechromelabs.github.io/chrome-for-testing/
   - Descomprime el archivo y coloca el ejecutable en la carpeta `chromedriver-mac-x64/` (o ajusta la ruta en el script si usas otra carpeta).

5. **Prepara tu archivo de contactos:**
   - Crea un archivo `contacts.csv` con el siguiente formato (separado por punto y coma):
     ```csv
     Nombre;Telefono
     Juan;+521234567890
     Ana;+521234567891
     Pedro;+521234567892
     ```

## Uso

1. Ejecuta el script principal:
   ```bash
   python3 enviar_mensajes_selenium.py
   ```
2. La primera vez, escanea el código QR de WhatsApp Web con tu teléfono.
3. El script enviará los mensajes personalizados automáticamente a cada contacto de la lista.
4. La próxima vez que ejecutes el script, usará la sesión guardada y no pedirá el QR.

## Notas
- El perfil de Chrome usado por Selenium se almacena en la carpeta `chrome_selenium_profile`.
- No es necesario iniciar sesión en Google, solo en WhatsApp Web.
- Si cambias de computadora o borras la carpeta de perfil, deberás escanear el QR nuevamente.

---

¡Listo! Ahora puedes automatizar el envío de mensajes de WhatsApp de forma sencilla y segura. 