# WhatsApp Auto Messenger con Python y Selenium

Este proyecto permite enviar mensajes personalizados de WhatsApp a una lista de contactos almacenada en un archivo CSV, de forma completamente automática, utilizando Python y Selenium.

## Funcionalidad
- Lee una lista de contactos desde `contacts.csv` (nombre y número de teléfono).
- Personaliza el mensaje para cada contacto usando su nombre.
- Abre WhatsApp Web en una ventana de Chrome y envía los mensajes automáticamente.
- **Multiplataforma**: Funciona en macOS, Windows y Linux.
- **Gestión automática de ChromeDriver**: Selenium gestiona la descarga y el uso del driver automáticamente.
- Utiliza un perfil exclusivo de Chrome para Selenium, evitando interferencias con tu navegador habitual.

## Requisitos
- Python 3.8 o superior
- Google Chrome instalado

## Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/diegoreyesd/whatsappauto.git
    cd whatsappauto
    ```

2.  **Crea y activa un entorno virtual (recomendado):**

    - **En macOS/Linux:**
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```
    - **En Windows:**
      ```bash
      python -m venv .venv
      .venv\Scripts\activate
      ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepara tu archivo de contactos:**
    - Crea un archivo `contacts.csv` con el siguiente formato (separado por punto y coma):
      ```csv
      Nombre;Telefono
      Juan;+521234567890
      Ana;+521234567891
      ```

## Uso

1.  **Ejecuta el script principal:**
    ```bash
    # En Windows
    python enviar_mensajes_selenium.py

    # En macOS/Linux
    python3 enviar_mensajes_selenium.py
    ```
2.  **La primera vez**, se abrirá una ventana de Chrome y tendrás que escanear el código QR de WhatsApp Web con tu teléfono.
3.  El script enviará los mensajes personalizados automáticamente a cada contacto de la lista.
4.  La próxima vez que ejecutes el script, usará la sesión guardada y no te pedirá el QR.

## Notas
- El perfil de Chrome usado por Selenium se almacena en la carpeta `chrome_selenium_profile`.
- No es necesario iniciar sesión en Google, solo en WhatsApp Web.
- Si cambias de computadora o borras la carpeta de perfil, deberás escanear el QR nuevamente.

---

¡Listo! Ahora puedes automatizar el envío de mensajes de WhatsApp de forma sencilla y segura. 