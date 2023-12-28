# Challenge Xepelin

![python_version](https://img.shields.io/badge/python-3.11-blue)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Linter: flake8](https://img.shields.io/badge/linter-flake8-blue)](https://flake8.pycqa.org/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Descripción

Descripción sobre el proyecto.

## Modelo seleccionado: nombre del modelo

Nombre del modelo seleccionado.

## Bibliografīa

En caso de que exista bibliografía al respecto listarla a continuación.

- Bibliografía 1.
- Bibliografía 2.
- Bibliografía 3.

## Fuentes de datos utilizadas

- Fuente 1
- Fuente 2

## Construcción del conjunto de entrenamiento, testeo y validación

- Período de los datos de entrenamiento: Septiembre del 2019 hasta Agosto del 2020.
- Estrategia de recolección: 30 días para generar las variables independientes y 15 días para generar el target.
- Estrategia de evaluación: Cross validation en dev. Se útilizaron los últimos 2 meses para validar la generalización.
- Selección del modelo:Se utilizó el **AUC** como métrica principal. En caso de empate, se evalua Precisión, Recall y F1.
- Umbral seleccionado para determinar clase: 0.1

## Variables seleccionadas

- frecuencia: frecuencia de navegación del usuario dada por el rfv de 3 meses.
- recencia: recencia del usuario dada por el rfv de 3 meses.
- volumen: cantidad de notas navegadas del usuario dada por el rfv de 3 meses.
- alta: el usuario es considerado una alta si en esos 15 dīas se suscribió.

## Resultados

| Stage | AUC  | Precision | Recall | F1   |
| ----- | ---- | --------- | ------ | ---- |
| DEV   | 0.75 | 0.01      | 0.69   | 0.01 |
| TEST  | 0.67 | 0.01      | 0.53   | 0.01 |

## Criterios de aceptación

Describir que criterios se tuvieron en cuenta para aceptar al modelo como productivo.

## Artefactos

La documentación del caso de uso se encuentra en la siguiente página de [CONFLUENCE](LINKPAGINACUCONFLUENCE). Ver [plantilla](https://agea.atlassian.net/wiki/spaces/BIGAA/pages/258212333/Casos+de+uso).

El código productivo se encuentra en el siguiente [REPOSITORIO](INSERTARLINKREPOBITBUCKET).
