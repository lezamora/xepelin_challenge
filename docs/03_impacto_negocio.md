## Impacto del modelo en el negocio

<p align="center"><img src="../images/producto.png" alt=""></p>

Es sumamente importante darle seguimiento a un modelo de machine learning con métricas de negocio para evaluar su impacto en términos financieros, operativos y de satisfacción, permitiendo ajustes continuos para optimizar la toma de decisiones y garantizar que el modelo contribuya efectivamente a los objetivos comerciales y estratégicos de la empresa.

Es por eso que las métricas seleccionadas para analizar el impacto del modelo en el negocio deben estar alineadas con estos últimos.

### Rentabilidad Neto o Margen del Financiamiento

Beneficio neto generado por las operaciones del financiamiento directo. Sería calculado como la diferencia generada por los ingresos de dar préstamos (intereses) y los costos asociados de dichas operaciones (el costo de oportunidad por no tener la devolución del financiamiento a la fecha establecida.)

Esto viene relacionado estrechamente con las métricas definidas para la selección del modelo. No seleccionamos ni el recall o precision para la evaluación dado que depende de las decisiones comerciales asociadas.

**Recall:** La capacidad del modelo para identificar correctamente todos los casos positivos. Este permitiría reducir la **tasa de incumplientos**, y en consecuencia, disminuir perdidas. Pero sin equilibrio justo podríamos estar negando financiación a operaciones que podrían no caer en mora y así perder ingresos por no financiar.

**Precision:** Mide la proporción de casos positivos predichos por el modelo que realmente son positivos. En este caso corremos el riesgo de financiar operaciones que pueden terminar en morosidad. Por lo que también aumentarían las pérdidas.

**Balance entre Recall y Precision:** Encontrar el equilibrio adecuado es fundamental. Un modelo que es demasiado conservador (alto recall pero baja precisión) puede rechazar préstamos potencialmente rentables. Por otro lado, un modelo demasiado permisivo (alta precisión pero bajo recall) puede aprobar préstamos de alto riesgo. En ambos casos, el margen de préstamo podría verse afectado negativamente.

### Otras métricas

Nuevamente como indicamos en el comienzo, el objetivo de la organización será la que le dé formas a los KPI. Otras métricas importantes podrían ser:

- Tasa de incumplimiento: cantidad de financiamientos no pagos a término sobre el total dado.
- Ingresos por financimienos aprobados y costos por incumplimiento: los que utilizaríamos para calcular el margen.
- Satisfacción del cliente: puede darse el caso que si negamos muchos financiamientos ocasione un mal estar en nuestros clientes y opten por utilizar otro servicio.
