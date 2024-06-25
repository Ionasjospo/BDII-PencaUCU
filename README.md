# BDII-PencaUCU
Este repositorio contiene el proyecto PencaUCU, desarrollado como parte de la asignatura Bases de Datos II en la Universidad Católica del Uruguay. El objetivo del proyecto es crear una aplicación para gestionar una penca de la Copa America 2024, permitiendo a los usuarios predecir los resultados de los partidos y competir por puntos.

## Descripción
PencaUCU es una aplicación web que permite a los usuarios registrarse, iniciar sesión, realizar predicciones sobre eventos deportivos y ver los resultados y clasificaciones. El sistema incluye un backend en python para gestionar los datos de los usuarios y las predicciones, así como un frontend en VUEjs intuitivo y fácil de usar.

## Características
Registro e inicio de sesión de usuarios.
Predicción de resultados de eventos deportivos.
Visualización de resultados y clasificación de usuarios.

## Tecnologías Utilizadas
- Frontend: Vue.js
- Backend: Python, Flask
- Base de Datos: MySQL
- Otros: Docker

## Requisitos
- Python 3.8+
- Node.js
- VUE.js 
- Docker

## Instalación
### Clona este repositorio:

```
git clone https://github.com/Ionasjospo/BDII-PencaUCU.git
cd BDII-PencaUCU
cd Back
pip install -r requirements.txt
cd docker
docker-compose up
```

### Inicia el servidor backend:
```
python main.py
```
### Instala las dependencias del frontend e inicia el servidor de desarrollo:
```
cd Front
npm install
npm run serve
```
#### Uso
Abre tu navegador web y navega a http://localhost:8080 para acceder a la aplicación.
Regístrate o inicia sesión para comenzar a hacer predicciones.
Explora y realiza tus predicciones.
Consulta la clasificación para ver cómo te comparas con otros usuarios.

