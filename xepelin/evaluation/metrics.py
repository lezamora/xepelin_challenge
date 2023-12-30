from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)

from xepelin.figures import plot_confusion_matrix, plot_roc_curve


def track_metrics(
    pipeline,
    x: np.ndarray,
    y: np.ndarray,
    threshold: float = 0.5,
):
    """
    Registra métricas para un pipeline de clasificación.

    Args:
        pipeline: El pipeline de clasificación.
        x (np.ndarray): Las características de entrada.
        y (np.ndarray): Las etiquetas reales.
        set_name (str): El nombre del conjunto de datos (por defecto: "test").
        threshold (float): El umbral de predicción (por defecto: 0.5).

    Returns:
        None
    """
    # Predecir probabilidades
    y_proba = pipeline.predict_proba(x)[:, 1]

    # Aplicar el umbral
    y_pred = (y_proba >= threshold).astype(int)

    # Calcular la precisión
    accuracy = accuracy_score(y, y_pred)

    # Calcular métricas
    cm = confusion_matrix(y, y_pred)

    # Imprimir el informe de clasificación
    report = classification_report(y, y_pred, target_names=["Negativo", "Positivo"])
    print(f"Informe de Clasificación:\n{report}")

    # Calcular precision, recall, f1-score y support para cada clase utilizando output_dict
    metrics_dict = precision_recall_fscore_support(
        y, y_pred, average=None, labels=[0, 1]
    )

    # Crear una figura con dos subgráficos en la misma fila
    fig, axes = plt.subplots(1, 2, figsize=(12, 3))

    # Graficar la matriz de confusión en el primer subgráfico
    plot_confusion_matrix(cm, classes=["Negativo", "Positivo"], ax=axes[0])
    axes[0].set_title("Matriz de Confusión")

    # Graficar la curva ROC en el segundo subgráfico
    plot_roc_curve(y, y_proba, ax=axes[1])
    axes[1].set_title("Curva ROC")
    plt.show()

    # Devolver métricas como un diccionario
    metrics = {
        "Precisión (Negativo)": round(metrics_dict[0][0], 2),
        "Precisión (Positivo)": round(metrics_dict[0][1], 2),
        "Recall (Negativo)": round(metrics_dict[1][0], 2),
        "Recall (Positivo)": round(metrics_dict[1][1], 2),
        "F1-Score (Negativo)": round(metrics_dict[2][0], 2),
        "F1-Score (Positivo)": round(metrics_dict[2][1], 2),
        "Accuracy": round(accuracy, 2),
    }

    return metrics


def save_metrics_to_csv(metrics_test: dict, params: dict, model_name: str) -> None:
    """
    Agrega las métricas de un experimento a un archivo CSV existente o crea uno nuevo.

    Parameters:
        metrics_test (dict): Métricas del conjunto de prueba.
        params (dict): Parámetros del modelo y del experimento.
        model_name (str): Nombre del modelo.

    Returns:
        None
    """
    # Obtén el timestamp actual como parte del nombre del archivo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Definir el nombre del archivo CSV con el timestamp
    csv_filename = "../metrics/experiments.csv"

    try:
        # Intenta cargar el archivo CSV existente
        df_existing = pd.read_csv(csv_filename)

    except FileNotFoundError:
        # Si el archivo no existe, crea un DataFrame vacío
        df_existing = pd.DataFrame()

    # Crea DataFrames de pandas con las métricas de test y validación
    df_test = pd.DataFrame([metrics_test])
    df_params = pd.DataFrame([params])

    # Combina los DataFrames en uno solo
    df_combined = pd.concat([df_params, df_test], axis=1)

    # Agrega columnas adicionales para timestamp y nombre del modelo
    df_combined["run_timestamp"] = timestamp
    df_combined["model"] = model_name

    # Combina el DataFrame existente con los DataFrames de test y validación
    df_existing = pd.concat([df_existing, df_combined], axis=0)

    # Guarda el DataFrame actualizado como un archivo CSV
    df_existing.to_csv(csv_filename, index=False)
    print(f"Métricas agregadas y guardadas en {csv_filename}")
