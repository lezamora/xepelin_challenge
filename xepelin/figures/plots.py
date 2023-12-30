import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve


def plot_confusion_matrix(cm: np.ndarray, classes: list, ax=None):
    """
    Grafica una matriz de confusión.

    Args:
        cm (np.ndarray): La matriz de confusión.
        classes (list): Las etiquetas de clase.
        ax: El objeto de eje para dibujar el gráfico (por defecto: None).

    Returns:
        None
    """
    if ax is None:
        ax = plt.gca()  # Obtener el eje actual si no se proporciona uno

    im = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    ax.set_title("Matriz de Confusión")
    plt.colorbar(im, ax=ax)
    tick_marks = np.arange(len(classes))
    ax.set_xticks(tick_marks)
    ax.set_xticklabels(classes, rotation=45)
    ax.set_yticks(tick_marks)
    ax.set_yticklabels(classes)

    fmt = ".2f"
    thresh = cm.max() / 2.0
    for i, j in np.ndindex(cm.shape):
        ax.text(
            j,
            i,
            format(cm[i, j], fmt),
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black",
        )

    ax.set_ylabel("Etiqueta Real")
    ax.set_xlabel("Etiqueta Predicha")


def plot_roc_curve(y_test: np.ndarray, y_proba: np.ndarray, ax=None):
    """
    Grafica la curva ROC.

    Args:
        y_test (np.ndarray): Las etiquetas reales.
        y_proba (np.ndarray): Las probabilidades predichas.
        ax: El objeto de eje para dibujar el gráfico (por defecto: None).

    Returns:
        None
    """
    if ax is None:
        ax = plt.gca()  # Obtiene el eje actual si no se proporciona uno

    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = roc_auc_score(y_test, y_proba)

    ax.plot(fpr, tpr, label="Curva ROC (AUC = %0.2f)" % roc_auc)
    ax.plot([0, 1], [0, 1], "k--")
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel("Tasa de Falsos Positivos")
    ax.set_ylabel("Tasa de Verdaderos Positivos")
    ax.set_title("Curva ROC")
    ax.legend(loc="lower right")
