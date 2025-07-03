# Remove the pysqlite3 import and use standard sqlite3
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st

# Título y presentación
st.title("Sistema Inteligente de Detección y Clasificación de Violencia en Audio")

st.markdown("""
**Desarrollado por:** Carla Marcela Florida Roman  
**Tutor:** Eduardo Di Santi Grönros, PhD  
**Universidad Mayor de San Simón, Cochabamba, Bolivia**
""")

st.write("""
Este sistema utiliza inteligencia artificial avanzada para analizar archivos de audio, identificar y clasificar eventos violentos, y calcular el grado de violencia presente en grabaciones. La arquitectura integra modelos de aprendizaje profundo, procesamiento de lenguaje natural y búsqueda semántica para ofrecer un análisis detallado y visualmente intuitivo.
""")

st.markdown("""
### ¿Qué puedes hacer con esta interfaz?
- **Subir archivos de audio** en formatos WAV, MP3, M4A o FLAC.
- **Seleccionar el modelo de predicción** más adecuado para tu análisis.
- **Fragmentar automáticamente** el audio en segmentos de 2 segundos para un análisis granular.
- **Detectar y clasificar eventos** como gritos, disparos, llantos, vidrios rotos y conversaciones.
- **Transcribir el audio** usando modelos de OpenAI (requiere API Key).
- **Buscar similitud semántica** con una base de datos de embeddings para contextualizar los resultados.
- **Visualizar resultados** en tablas y gráficos interactivos.
- **Descargar el histórico** de análisis en formato Excel para documentación o investigación.
- **Calcular y visualizar el grado de violencia** y su evolución a lo largo del tiempo.
""")

st.markdown("""
### Arquitectura y Flujo de Trabajo
1. **Carga y segmentación de audio**: El usuario sube un archivo, que se divide automáticamente en fragmentos de 2 segundos.
2. **Predicción de eventos**: Cada fragmento es analizado por un modelo de IA entrenado para identificar eventos violentos.
3. **Transcripción y embeddings**: Opcionalmente, cada fragmento se transcribe y se consulta su similitud semántica en una base vectorial.
4. **Visualización y análisis**: Los resultados se muestran en tablas, gráficos y se calculan métricas de violencia y su tendencia.
5. **Exportación**: El usuario puede descargar el histórico completo del análisis realizado.
""")

st.info("Para comenzar, selecciona una de las opciones en el menú de la izquierda.")
