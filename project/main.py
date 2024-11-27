__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st

# Página de Streamlit
st.title("IMPLEMENTACIÓN DE MODELO DE PROCESAMIENTO DE LENGUAJE NATURAL PARA PREDICCIÓN DE VIOLENCIA MEDIANTE SEGMENTACIÓN DE AUDIO STREAM")

st.write("""
En esta interfaz podrás cargar un archivo de audio y seleccionar un modelo de predicción para realizar un análisis de fragmentos de audio.
Este sistema está diseñado para detectar y clasificar eventos como llantos, disparos, vidrios rotos, entre otros.
""")

st.write("""
### ¿Cómo funciona?
1. **Subida de archivo de audio**: Puedes cargar un archivo de audio en formato WAV. El archivo será automáticamente dividido en fragmentos de 2 segundos para realizar las predicciones.
2. **Selección de modelo de predicción**: Luego podrás elegir el modelo de predicción que prefieras. Este modelo se encargará de identificar diferentes tipos de eventos, como gritos, disparos, llantos, etc.
3. **Análisis de fragmentos**: Una vez cargado el archivo y seleccionado el modelo, el sistema analizará cada fragmento de audio y presentará las predicciones correspondientes.
4. **Visualización de resultados**: Los resultados de las predicciones y la transcripción del audio se mostrarán en tablas y gráficos, lo que te permitirá obtener un análisis detallado de los eventos detectados.
5. **Descarga del histórico**: Finalmente, tendrás la opción de descargar un archivo histórico con todos los resultados y detalles de los fragmentos procesados.

### Objetivo
Este modelo de procesamiento de lenguaje natural está diseñado para analizar audios segmentados, identificar eventos violentos y proporcionar un puntaje de violencia basado en los datos obtenidos. Además, se integran características de transcripción de texto y búsqueda de similitudes mediante una base de datos de embeddings.

""")
