# Vura: The Health App

Vura es una aplicación móvil desarrollada con Python y Flet diseñada para ayudar a los usuarios a llevar una gestión eficiente y sencilla de su salud.

## Características Principales
- **Autenticación Segura:** Inicio de sesión y registro integrados con Firebase Authentication.
- **Gestión de Salud:** Seguimiento en tiempo real de:
  - Consumo diario de agua.
  - Pasos realizados.
  - Horas de sueño.
- **Persistencia en la nube:** Tus datos de salud se sincronizan automáticamente con Firebase Realtime Database.
- **Multiplataforma:** Desarrollado con Flet para ejecutarse de manera fluida.

## Estructura del Proyecto
- `views/`: Pantallas de la aplicación (Welcome, Login, Register, Home).
- `utils/`: Lógica de conexión con servicios externos (Firebase).
- `assets/`: Recursos multimedia (iconos, imágenes).
- `main.py`: Punto de entrada de la aplicación.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/vura-health-app.git
   cd vura-health-app
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configura tus variables de entorno:
   Crea un archivo `.env` en la raíz con tus credenciales de Firebase:
   ```
   API_KEY=...
   AUTH_DOMAIN=...
   PROJECT_ID=...
   STORAGE_BUCKET=...
   MESSAGING_SENDER_ID=...
   APP_ID=...
   DATABASE_URL=...
   ```

4. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

## Licencia
Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.
