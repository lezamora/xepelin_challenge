# Challenge Xepelin

![python_version](https://img.shields.io/badge/python-3.11-blue)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Linter: flake8](https://img.shields.io/badge/linter-flake8-blue)](https://flake8.pycqa.org/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Descripción

Este repositorio tiene como objetivo desarrollar un modelo predictivo que intente resolver el caso de uso presentado por Xepelin como desafío técnico.

## Utilización del proyecto

Para poder replicar el código que resuelve el problema se proveen dos alternativas:

### Virtualenvs

### Docker

## Estructura del proyecto

- **data**
  - *raw*: Datos sin procesar sin modificaciones.
  - *intermediate*: Datos intermedios generados durante el procesamiento.
  - *processed*: Datos procesados y listos para el entrenamiento del modelo.
- **docs**: Carpeta para almacenar documentación relacionadas con el proyecto.
- **images**: Carpeta para almacenar imágenes relacionadas a la documentación.
- **metrics**: Carpeta para almacenar métricas y medidas de evaluación del modelo.
- **models**: Carpeta para almacenar modelos entrenados.
- **notebooks**: Carpeta que contiene Jupyter Notebooks utilizados para análisis y desarrollo.
- **reports**: Carpeta para almacenar informes generados por el proyecto.
- **xepelin**
  - *figures*: Módulo para generar gráficos utilizados en el desarrollo del modelo.
  - *evaluation*: Módulo para generar métricas utilizadas para el desarrollo del proyecto.
- *.editorconfig*: Configuración del editor para mantener la consistencia del estilo de código.
- *.gitignore*: Archivo de configuración Git para ignorar archivos y carpetas específicos.
- *.pre-commit-config.yaml*: Configuración para pre-commit hooks que se ejecutan antes de confirmar cambios en Git.
- *pyproject.toml*: Archivo de configuración para proyectos Python, utilizado para especificar dependencias y configuraciones del proyecto.
- *requirements.txt*: Lista de dependencias del proyecto en formato de archivo de texto.
- *setup.cfg*: Configuración adicional para el sistema de distribución de Python.
- *setup.py*: Archivo de configuración para la distribución del proyecto.
- *.dockerignore*: Archivo de configuración para Docker, especifica qué archivos y carpetas deben ser ignorados al construir imágenes Docker.
- *Dockerfile*: Archivo de configuración para construir una imagen Docker del proyecto.

## Documentación

Toda la documentación relacionada a la resolución del problema se encontrará divida en secciones para proveer mayor simplicidad en la lectura:
