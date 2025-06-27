# IMPLEMENTACIÓN DE UN MODELO DE INTELIGENCIA ARTIFICIAL PARA LA DETECCIÓN DE VIOLENCIA EN AUDIO MEDIANTE ANÁLISIS ACÚSTICO Y PROCESAMIENTO DE LENGUAJE NATURAL

## Descripción del Proyecto

Este proyecto se centra en la **fragmentación de audio en texto y espectrogramas** para el análisis y predicción de violencia utilizando algoritmos de procesamiento de lenguaje natural (NLP). Combina modelos de aprendizaje profundo y técnicas de NLP para identificar eventos violentos en grabaciones de audio segmentadas.

---

## 📚 Contexto Académico

### FICHA RESUMEN

El presente trabajo de grado aborda el problema de identificación, clasificación y predicción de eventos violentos en registros de audio, mediante la implementación de un modelo basado en técnicas de procesamiento de lenguaje natural y aprendizaje profundo. El modelo desarrollado permite analizar fragmentos de audio segmentados, clasificando eventos en cinco categorías específicas: **disparos**, **gritos**, **conversaciones**, **llanto** y **rotura de vidrios**. A partir de esta clasificación, se calcula un grado de violencia asociado a cada fragmento.

La solución integra tres componentes principales:
- **Procesamiento de espectrogramas de audio** mediante redes neuronales profundas
- **Análisis del contenido textual** derivado de los audios utilizando representaciones vectoriales
- **Incremento del conjunto de datos** de entrenamiento mediante la incorporación de ruido gaussiano para mejorar la capacidad de generalización del modelo

La metodología empleada incluyó la recopilación y segmentación de audios en intervalos de dos segundos, seguidos por el entrenamiento de ocho modelos diferentes: cuatro con datos originales y cuatro con datos aumentados con ruido, utilizando distintos valores de épocas (20, 30, 40 y 100). La clasificación de violencia se organiza en tres niveles (**bajo**, **moderado** y **alto**), definidos según el peso asignado a los eventos críticos presentes en el audio.

Los resultados indican que los modelos entrenados con datos aumentados mostraron mejor capacidad de generalización en conjuntos de datos reducidos, especialmente en el experimento con 40 épocas. Asimismo, se verificó la eficacia del modelo en escenarios simulados mediante la utilización de ejemplos extraídos de películas, alcanzando una detección en tiempo casi real.

### ANTECEDENTES Y MOTIVACIÓN

El estudio y análisis de la voz humana constituye un campo ampliamente abordado dentro del ámbito de la inteligencia artificial y el procesamiento digital de señales. La violencia, en sus diversas manifestaciones, suele expresarse mediante indicadores acústicos tanto verbales como no verbales, los cuales evidencian estados de tensión, agresión o miedo.

**Aplicaciones Existentes:**
- **SoundThinking (2023)**: Solución ShotSpotter que analiza en tiempo real sonidos de disparos, geolocalizando su procedencia
- **Modelos híbridos**: Estudios como Trinh et al. (2020) han demostrado tasas de detección superiores al 85% integrando espectrogramas de audio con análisis semántico
- **Data augmentation**: Durães, Veloso y Novais (2023) evaluaron técnicas de aumento de datos para detectar eventos violentos

**Problemática Actual:**
En contextos urbanos de América Latina, como Bolivia, la proliferación de contenido violento en entornos digitales se ha intensificado de manera alarmante. La ausencia de mecanismos automatizados para detectar, clasificar y valorar la gravedad de episodios violentos en señales de audio limita la posibilidad de generar alertas tempranas y dificulta la intervención oportuna.

### OBJETIVOS DEL PROYECTO

#### Objetivo General
Implementar un modelo basado en procesamiento de lenguaje natural y aprendizaje profundo para analizar señales de audio mediante la segmentación y conversión a espectrogramas, con el fin de predecir y clasificar episodios de violencia.

#### Objetivos Específicos
- Segmentar las señales de audio para generar representaciones textuales y en espectrogramas
- Preparar el conjunto de datos mediante su identificación, limpieza y estructuración para el entrenamiento del modelo de audio
- Diseñar un modelo de aprendizaje profundo, entrenarlo y evaluarlo para la clasificación de contenido violento en señales de audio
- Analizar el texto transcrito a partir del audio para identificar expresiones asociadas a violencia, mediante representaciones vectoriales
- Integrar las representaciones de audio y texto para predecir el grado de violencia en fragmentos de audio

### METODOLOGÍA

#### Arquitectura del Sistema
El modelo implementa una arquitectura híbrida que combina:

1. **Procesamiento Acústico**:
   - Segmentación de audio en fragmentos de 2 segundos
   - Conversión a espectrogramas Mel con 128 bandas de frecuencia
   - Frecuencia de muestreo objetivo: 16kHz
   - Frecuencia máxima: 8kHz

2. **Análisis de Texto**:
   - Transcripción de audio a texto mediante Whisper-1 (OpenAI)
   - Generación de embeddings vectoriales usando Sentence Transformers
   - Búsqueda de similitud semántica en base de datos ChromaDB

3. **Clasificación de Eventos**:
   - Redes neuronales convolucionales (CNN) para análisis espectral
   - Clasificación en 5 categorías: crying, glass_breaking, gun_shot, people_talking, screams
   - Cálculo de grados de violencia (bajo, moderado, alto)

#### Estrategia de Entrenamiento
- **8 modelos diferentes** entrenados con distintas configuraciones:
  - 4 modelos con dataset original (20, 30, 40, 100 épocas)
  - 4 modelos con data augmentation (ruido gaussiano + 20, 30, 40, 100 épocas)
- **Técnicas de data augmentation**: Ruido gaussiano para mejorar generalización
- **Validación cruzada** para evaluar robustez del modelo

### RESULTADOS Y CONTRIBUCIONES

#### Rendimiento del Modelo
- **Mejor generalización**: Modelos con data augmentation mostraron superior capacidad de adaptación
- **Punto óptimo**: Experimento con 40 épocas y ruido gaussiano
- **Detección en tiempo real**: Capacidad de procesamiento en tiempo casi real
- **Precisión**: Tasas de detección superiores al 85% en escenarios controlados

#### Innovaciones Técnicas
- **Integración multimodal**: Combinación de análisis acústico y semántico
- **Sistema de alertas**: Predicción de evolución de violencia basada en tendencias
- **Base de datos vectorial**: Almacenamiento y búsqueda eficiente de embeddings
- **Interfaz intuitiva**: Aplicación web con Streamlit para uso no técnico

#### Aplicaciones Prácticas
- **Monitoreo urbano**: Detección de eventos violentos en espacios públicos
- **Seguridad ciudadana**: Alertas tempranas para cuerpos de seguridad
- **Análisis forense**: Clasificación automática de evidencia de audio
- **Investigación social**: Estudios sobre patrones de violencia en contextos urbanos

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

---

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ViolenceDetectionInterface
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   # Crear entorno virtual
   python -m venv venv
   
   # Activar el entorno virtual
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar API Key de OpenAI (opcional)**
   
   Para usar la funcionalidad de transcripción de audio a texto, necesitas configurar tu API key de OpenAI:
   
   ```bash
   # En Windows:
   set OPENAI_API_KEY=tu_api_key_aqui
   
   # En macOS/Linux:
   export OPENAI_API_KEY=tu_api_key_aqui
   ```
   
   O crear un archivo `.env` en la raíz del proyecto:
   ```
   OPENAI_API_KEY=tu_api_key_aqui
   ```

---

## 🎯 Cómo Ejecutar la Aplicación

### Ejecución Principal

1. **Navegar al directorio del proyecto**
   ```bash
   cd project
   ```

2. **Ejecutar la aplicación Streamlit**
   ```bash
   streamlit run main.py
   ```

3. **Acceder a la aplicación**
   
   La aplicación se abrirá automáticamente en tu navegador web. Si no se abre automáticamente, ve a:
   ```
   http://localhost:8501
   ```

### Funcionalidades Disponibles

La aplicación tiene tres páginas principales:

#### 1. **Realizar Clasificación de Audio** (`1_Realizar_clasificacion_de_audio.py`)
- Subir archivos de audio en formato WAV
- Seleccionar entre 8 modelos preentrenados diferentes
- Analizar fragmentos de audio de 2 segundos
- Obtener predicciones de eventos (llanto, disparos, vidrios rotos, etc.)
- Transcripción de audio a texto (requiere API key de OpenAI)
- Búsqueda de similitudes en base de datos de embeddings
- Guardar resultados en archivo Excel

#### 2. **Ver Histórico** (`2_Ver_historico.py`)
- Visualizar archivos históricos guardados
- Analizar resultados anteriores
- Descargar archivos de histórico

#### 3. **Determinar Grado de Violencia** (`3_Determinar_grado_de_violencia.py`)
- Calcular evolución de violencia en el tiempo
- Análisis de tendencias de violencia
- Visualización de grados de violencia

---

## 📁 Estructura del Proyecto

```
ViolenceDetectionInterface/
│
├── models/                     # Modelos entrenados (.h5)
│   ├── original_dataset_20.h5
│   ├── original_dataset_30.h5
│   ├── original_dataset_40.h5
│   ├── original_dataset_100.h5
│   ├── gaussian noise_20.h5
│   ├── gaussian noise_30.h5
│   ├── gaussian noise_40.h5
│   └── gaussian_noise_100.h5
│
├── project/
│   ├── modules/                # Módulos auxiliares
│   │   ├── chroma_query.py     # Consultas a base de datos Chroma
│   │   ├── audio_prediction.py # Predicción de audio
│   │   └── violence_grade.py   # Cálculo de grado de violencia
│   │
│   ├── pages/                  # Páginas de la aplicación
│   │   ├── 1_Realizar_clasificacion_de_audio.py
│   │   ├── 2_Ver_historico.py
│   │   └── 3_Determinar_grado_de_violencia.py
│   │
│   └── main.py                 # Archivo principal de Streamlit
│
├── histórico/                  # Archivos de resultados (.xlsx)
├── data_embeddings/           # Base de datos de embeddings
├── requirements.txt           # Dependencias del proyecto
└── README.md
```

---

## 🔧 Uso de la Aplicación

### Paso a Paso para Clasificación de Audio

1. **Abrir la aplicación**
   - Ejecutar `streamlit run main.py` desde el directorio `project/`
   - Navegar a la página "Realizar Clasificación de Audio"

2. **Seleccionar modelo**
   - Elegir entre los 8 modelos disponibles:
     - 4 modelos con audios originales (20, 30, 40, 100 epochs)
     - 4 modelos con ruido gaussiano (20, 30, 40, 100 epochs)

3. **Subir archivo de audio**
   - Hacer clic en "Browse files" o arrastrar archivo WAV
   - El sistema automáticamente dividirá el audio en fragmentos de 2 segundos

4. **Analizar resultados**
   - Ver predicciones para cada fragmento
   - Escuchar fragmentos individuales
   - Revisar transcripción de texto (si está configurada la API)
   - Ver embeddings asociados y distancias

5. **Descargar histórico**
   - Los resultados se guardan automáticamente en formato Excel
   - El archivo se nombra según el dataset y modelo seleccionado

### Modelos Disponibles

| Modelo | Descripción | Épocas |
|--------|-------------|--------|
| Audios originales | Entrenado con dataset original | 20, 30, 40, 100 |
| Gaussian Noise | Entrenado con ruido gaussiano | 20, 30, 40, 100 |

---

## 🐛 Solución de Problemas

### Errores Comunes

1. **Error de dependencias**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

2. **Error de memoria con archivos grandes**
   - Usar archivos de audio más pequeños
   - Aumentar la memoria disponible

3. **Error de API de OpenAI**
   - Verificar que la API key esté configurada correctamente
   - La funcionalidad de transcripción es opcional

4. **Error de puerto ocupado**
   ```bash
   streamlit run main.py --server.port 8502
   ```

### Requisitos del Sistema

- **RAM**: Mínimo 4GB, recomendado 8GB
- **Almacenamiento**: 2GB de espacio libre
- **Sistema Operativo**: Windows, macOS, o Linux

---

## 📊 Formato de Salida

Los archivos de histórico se guardan en formato Excel (.xlsx) con las siguientes columnas:

- **Número de Fragmento**: Identificador del fragmento
- **Tiempo del Fragmento**: Rango de tiempo (ej: "0,2")
- **Texto**: Transcripción del audio (si está disponible)
- **Embedding Asociado**: Texto más similar encontrado
- **Distancia**: Distancia de similitud
- **crying**: Probabilidad de llanto (%)
- **glass_breaking**: Probabilidad de vidrios rotos (%)
- **gun_shot**: Probabilidad de disparos (%)
- **people_talking**: Probabilidad de personas hablando (%)
- **screams**: Probabilidad de gritos (%)

---

## 📝 Notas Importantes

- Los archivos de audio deben estar en formato WAV
- La transcripción de audio requiere una API key válida de OpenAI
- Los modelos están preentrenados y listos para usar
- Los resultados se guardan automáticamente en la carpeta `histórico/`
- La aplicación funciona mejor con archivos de audio de buena calidad

---

## Licencia

**Universidad Mayor de San Simón, Cochabamba, Bolivia**

El contenido de este proyecto es parte del trabajo de tesis titulado *"IMPLEMENTACIÓN DE UN MODELO DE INTELIGENCIA ARTIFICIAL PARA LA DETECCIÓN DE VIOLENCIA EN AUDIO MEDIANTE ANÁLISIS ACÚSTICO Y PROCESAMIENTO DE LENGUAJE NATURAL"*, desarrollado por **Carla Marcela Florida Roman** bajo la supervisión del **Tutor Eduardo Di Santi Grönros, PhD**.