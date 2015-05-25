# ![](https://rawgithub.com/rcotrina94/citasalud/master/docs/images/icon.png) CitaSalud: Gestión de citas y diagnósticos


## Descripción:
CitaSalud, es un sistema de gestión de citas y diagnóstico. El proyecto se realiza en base a una tarea para el curso de Sistemas de Información I.
Consiste de un Sistema de Información Web para optimizacion de tiempos y costos en la administración de citas y diagnóstico de un hospital.

> **Enunciado**: [Práctica 02](./docs/README.md)
>
> **Integrantes**:
> - Cotrina Alvitres, Richard
> - Carmona Chavez, Jossy
> - Asmat Velásquez, Desiré
> - Vasquez Muñoz, Brenda
> - Polo Zavala, Nick

![](https://rawgithub.com/rcotrina94/citasalud/master/docs/images/model.png)

## Arquitectura del SI
El sistema consta de un servidor escrito en Python y su framework Django, y dos interfaces: Una interfaz web usada por los Pacientes, Doctores, Administradores, y una interfaz de escritorio que es usada por únicamente por Personal del Hospital (Administradores, Supervisores, Gerencia, Doctores, etc).

### Backend
- **Aplicación Web:** Django(Python)
	- **API REST:** Django REST Framework
	
- **Motor de Base de Datos:** SQLite / MySQL / PostgreSQL

- **Servidor de Aplicaciones:** Nginx / Apache

### Frontend
- **Interfaz Web Escritorio/Móvil**: HTML5 + CSS3
	- **Diseño:** Material Design 
	- **Programación:** jQuery (Javascript)
	
- **Interfaz de Escritorio:** Electron (Packaged Webkit Browser + io.js)
	- **Diseño:** Material Design (Angular Material Design) 
	- **Programación:** AngularJS+io.js (Javascript)
		
## [Implementación](http://i.imgur.com/Wuuw4N9.gifv)


### Entorno de desarrollo

Se deben instalar los siguientes requerimientos:
```js
Django==1.8
django-extensions==1.5.5
django-localflavor==1.1
djangorestframework==3.1.1
Markdown==2.6.2
MySQL-python==1.2.5
Pillow==2.8.1
pygraphviz==1.2
six==1.9.0
```

### Producción
[...]

## Capturas
![](https://raw.github.com/rcotrina94/citasalud/master/docs/images/001.png)
![](https://raw.github.com/rcotrina94/citasalud/master/docs/images/002.png)
![](https://raw.github.com/rcotrina94/citasalud/master/docs/images/003.png)
