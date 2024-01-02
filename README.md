# Challenge Xepelin

![python_version](https://img.shields.io/badge/python-3.11-blue)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Linter: flake8](https://img.shields.io/badge/linter-flake8-blue)](https://flake8.pycqa.org/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

<p align="center"><img src="./images/logo.png" alt=""></p>

## Descripción

Este repositorio tiene como objetivo desarrollar un modelo predictivo que intente resolver el caso de uso presentado por Xepelin como desafío técnico.

## Ejecución del código

Para poder replicar el código que resuelve el problema se proveen dos alternativas:

### requirements.txt

En la parte superior del proyecto se menciona que versión de python se utilizó para el desarrollo.
Se puede usar el gestor de ambiente que se prefiera.

```bash
pip install -r requirements.txt
```

### Docker

Como requisito tener docker instalado.

1 - Construir la imagen

```bash
docker build -t nombre-de-la-imagen .
```

2 - Ejecutar el contenedor

```bash
docker run -p 8888:8888 nombre-de-la-imagen
```

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
- **presentaciones**: Carpeta que contiene la presentación generada para los usuarios de negocio.
- **reports**: Carpeta para almacenar informes generados por el proyecto.
- **xepelin**: Distribución creada para reutilizar funciones.
  - *figures*: Módulo para generar gráficos utilizados en el desarrollo del modelo.
  - *evaluation*: Módulo para generar métricas utilizadas para el desarrollo del proyecto.
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

| Nombre del Documento                                  | Descripción                                                                                                                                           |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [01_caso_de_uso.md](./docs/01_caso_de_uso.md)         | Documento donde se explica el planteo inicial que se hizo y donde se encarma el problema a una resolución de machine learning.                        |
| [02_desarrollo.md](./docs/02_desarrollo.md)           | Documento que detalla el proceso de desarrollo del modelo, se responden las preguntas realizas en las consignas y se informan las decisiones tomadas. |
| [03_impacto_negocio.md](./docs/03_impacto_negocio.md) | Documento que analiza el impacto del modelo en el negocio.                                                                                            |

## Presentación

Se adjunta una presentación cuyo objetivo son los usuarios de negocio explicando los resultados del desarrollo realizado. La presentación se encuentra dentro del mismo repositorio en el siguiente directorio: [Presentación del modelo](./presentaciones/ppt_modelo_detector_mora.pdf).
