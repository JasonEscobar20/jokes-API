# Jokes API
***
Herramienta que obtiene un objeto de un API de terceros y genera un endpoint con 25 objetos evitando que se repitan los ID

Tecnologías usadas en este proyecto:
* [Python](https://www.python.org): Version 3.8
* [Django](https://www.djangoproject.com): Version 3.2 
* [Django-Rest-Framework](https://www.django-rest-framework.org): Version 3.14

## Installation
***
Para realizar creación de imagen del proyecto en docker por medio del Dockerfile.
```
$ git clone https://github.com/JasonEscobar20/Jokes-API.git
$ cd Jokes-API
$ docker build . -t jokes_app_img
```

## FAQs
1. **Utilizar puerto 8080 para levantar la imagen en el contenedor de docker**