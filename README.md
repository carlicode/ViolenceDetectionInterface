# IMPLEMENTACIÓN DE MODELO DE PROCESAMIENTO DE LENGUAJE NATURAL PARA PREDICCIÓN DE VIOLENCIA MEDIANTE SEGMENTACIÓN DE AUDIO STREAM

## Descripción del Proyecto

Este proyecto se centra en la **fragmentación de audio en texto y espectrogramas** para el análisis y predicción de violencia utilizando algoritmos de procesamiento de lenguaje natural (NLP). Combina modelos de aprendizaje profundo y técnicas de NLP para identificar eventos violentos en grabaciones de audio segmentadas.

---

## Objetivo General

Fragmentación de audio en texto y espectrograma para el análisis y predicción de violencia mediante algoritmos de procesamiento de lenguaje natural.

---

## Objetivos Específicos

- Descomposición de audio en texto y señales de audio.
- Identificación de set de datos para el entrenamiento y evaluación del modelo de clasificación.
- Creación, entrenamiento y evaluación del modelo.
- Análisis de texto usando embeddings.
- Identificación de sonidos contextuales.
- Identificación de falsos positivos y falsos negativos.
- Plan de contingencia y mejora del modelo para casos no identificados por el modelo.

### Características:
- **Subida de archivos de audio**: Permite cargar archivos de audio en formato WAV.
- **Segmentación de audio**: Divide los archivos de audio en fragmentos de 2 segundos para su análisis.
- **Clasificación**: Detecta y clasifica eventos como llanto, vidrios rotos, disparos, gritos, y personas hablando.
- **Visualización**: Muestra gráficos de la distribución de las etiquetas y los eventos de alta probabilidad.
- **Histórico**: Los resultados de las predicciones se guardan en un archivo Excel para su posterior análisis.

# Estructura del proyecto
```
violencedetectioninterface/
│
├── models/                     # Ejemplos de resultados en .csv
├── models/                     # 8 modelos entrenados .h5
├── project/
│   ├── modules/                # Archivos con funciones auxiliares
│   │   ├── chroma_query.py     # Funciones para consultar la base de datos Chroma
│   │   └── audio_prediction.py # Funciones para la predicción de audio
│   │   └── violence_grade.py   # Funciones para calcular la evolución de la violencia 
│   ├── pages/
│   │   ├── 1_Realizar_clasificacion_de_audio.py
│   │   ├── 2_Ver_historico.py
│   │   └── 3_Determinar_grado_de_violencia.py
│   └── requirements.txt        # Dependencias del proyecto
├── README.md
└── requirements.txt
```

## Licencia

**Universidad Mayor de San Simón, Cochabamba, Bolivia**

El contenido de este proyecto es parte del trabajo de tesis titulado *"Implementación de Modelo de Procesamiento de Lenguaje Natural para Predicción de Violencia mediante Segmentación de Audio Stream"*, desarrollado por **Carla Marcela Florida Roman** bajo la supervisión del **Tutor Eduardo Di Santi Grönros, PhD**.