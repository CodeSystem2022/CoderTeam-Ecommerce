# CoderTeam-Ecommerce
# UTN/San Rafael   <img src="projectDocsFiles/logoUTN.png" width="20">
<img src="projectDocsFiles/coder.gif" width="150">

Este proyecto es parte de ... y tiene como objetivo ...

## Tabla de Contenidos

- [¿Cómo correr el proyecto?](#¿cómo-correr-el-proyecto?)
  - [Pasos generales](#pasos-generales)
    - [Instalación](#instalación)
  - [Entorno virtual default](#requisitos)
    - [Activación](#activación)
    - [Correr servidor](#correr-servidor)
  - [Nuevo entorno virtual](#nuevo-entorno-virtual)
    - [Creación](#creación)
    - [Requisitos](#requisitos)
    - [Instalación](#instalación)
    - [Correr servidor](#correr-servidor)
- [Contribución](#contribución)
- [Site Preview](#site-preview )

## ¿Cómo correr el proyecto?
### Pasos generales
###### Estos pasos aplican para cualquier forma en la que quiera correr el proyecto, aunque vale destacar que también podría instalar el repositorio de otras formas. En nuestro caso solo mostraremos este método (clonar desde consola). Puede consultar la [documentación de github](https://docs.github.com/repositories) para conocer otros métodos.

#### Instalación

1. Clonar este repositorio en tu máquina local.
```bash
git clone https://github.com/tu-usuario/tu-proyecto.git
```

2. Navega al directorio del proyecto.
```bash
cd tu-proyecto
```

3. Instalación de venv (si no está instalado):
En la mayoría de las instalaciones de Python, venv ya está incluido. Sin embargo, si estás usando una versión más antigua de Python o si por alguna razón no tienes venv instalado, puedes instalarlo usando el siguiente comando:
```bash
python3 -m pip install --user virtualenv
```

###### En esta instancia procederemos al segundo paso, donde mostraremos dos formas para trabajar (si bien existen otras formas nos centraremos en dos maneras unicamente):

### 1. Entorno virtual default _(enviromentEcommerce)_:
#### Activación
###### Desde el directorio principal del proyecto recientemente clonado ejecute el siguiente comando para activar el entorno virtual:
##### En sistemas Windows:
```bash
- enviromentEcommerce/Scripts/activate
```
##### En sistemas basados en Unix (Linux/Mac):
```bash
- source enviromentEcommerce/bin/activate

```
#### Correr servidor
###### Luego con el entorno activado -se puede dar cuenta que está activo porque al principio de la línea de comando debería figurar _(enviromentEcommerce)_: 
```bash
- python -m manage.py runserver
```

### 2. Nuevo Entorno virtual
#### Creación
###### Desde el directorio principal del proyecto recientemente clonado ejecute el siguiente comando para generar el nuevo entorno virtual:
```bash
- python -m venv nombre_del_entorno
```
#### Activación
###### Desde el directorio principal del proyecto recientemente clonado ejecute el siguiente comando para activar el entorno virtual:
##### En sistemas Windows:
```bash
- nombre_del_entorno/Scripts/activate
```
##### En sistemas basados en Unix (Linux/Mac):
```bash
- source nombre_del_entorno/bin/activate
```

#### Requisitos
###### En este punto será momento para instalar las dependencias:

Para ejecutar este proyecto, necesitas tener instalado Python 3 y las siguientes dependencias:
```bash
- Django (version 4.2.7)
- Pillow
```

Puedes instalar los requerimientos utilizando pip:

Opción 1:
```bash
pip install -r requirements.txt
```
Opción 2:
```bash
pip install django Pillow
```

#### Correr servidor
###### Luego, con las dependencias instaladas y el entorno activado -se puede dar cuenta que está activo porque al principio de la línea de comando deberá figurar '(nombre_del_entorno)' ejecutar: 
```bash
- python -m manage.py runserver
```

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios.
3. Realiza tus cambios y pruebas.
4. Envía una solicitud de extracción (Pull Request) describiendo tus cambios.




## Site Preview  
<img src="projectDocsFiles/Coder Team (1).gif" width="70">



<img src="projectDocsFiles/Coder Team.gif" width="100">
