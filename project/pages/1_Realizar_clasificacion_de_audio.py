import streamlit as st
import librosa
import soundfile as sf
import os
import pandas as pd
from openai import OpenAI
from modules.chroma_query import load_chroma_db, query_chroma_db
from modules.audio_prediction import load_audio_model, split_audio, predict_episode

# Configuración del directorio para guardar el histórico
HISTORIC_DIR = 'histórico/'
os.makedirs(HISTORIC_DIR, exist_ok=True)

# Initialize OpenAI client with proper error handling
try:
    # Check if API key is set in environment
    import os
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        # Initialize without API key (will fail gracefully when used)
        client = OpenAI()
except Exception as e:
    st.error(f"Error initializing OpenAI client: {e}")
    client = None

# Etiquetas para las predicciones
labels = ["crying", "glass_breaking", "gun_shot", "people_talking", "screams"]

# Opciones de modelos disponibles
models = {
    "Audios originales con 20 epochs": "models/original_dataset_20.h5",
    "Audios originales con 30 epochs": "models/original_dataset_30.h5",
    "Audios originales con 40 epochs": "models/original_dataset_40.h5",
    "Audios originales con 100 epochs": "models/original_dataset_100.h5",
    "Gaussian Noise con 20 epochs": "models/gaussian noise_20.h5",
    "Gaussian Noise con 30 epochs": "models/gaussian noise_30.h5",
    "Gaussian Noise con 40 epochs": "models/gaussian noise_40.h5",
    "Gaussian Noise con 100 epochs": "models/gaussian_noise_100.h5"
}

# Cargar la base vectorial de ChromaDB
db = load_chroma_db()

# Página de Streamlit
st.title("Clasificador de Fragmentos de Audio")

# Selector de modelo
model_choice = st.selectbox("Selecciona el modelo de predicción:", list(models.keys()))
model = load_audio_model(models[model_choice])
st.write(f"Modelo seleccionado: **{model_choice}**")

# Función para convertir audio a texto usando openAI
def audio_to_text(audio_path):
    if client is None:
        st.warning("OpenAI client not available. Skipping audio transcription.")
        return ""
    
    try:
        audio_file = open(audio_path, "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file)
        return transcription.text  # Devolver el texto transcrito
    except Exception as e:
        st.error(f"Error transcribing audio: {e}")
        return ""

# Subir archivo de audio
uploaded_file = st.file_uploader("Sube un archivo de audio", type=["wav"])

if uploaded_file:
    audio, sr = librosa.load(uploaded_file, sr=16000, mono=True)
    episodes = split_audio(audio, sr)
    historical_data = []

    st.write(f"Se detectaron {len(episodes)} fragmentos de 2 segundos.")

    predictions = predict_episode(episodes, model)
    for i, (episode, pred) in enumerate(zip(episodes, predictions)):
        fragment_filename = f"fragment_{i + 1}.wav"
        sf.write(fragment_filename, episode, 16000)

        st.audio(fragment_filename, format="audio/wav")

        recognized_text = audio_to_text(fragment_filename)  
        document, distance = query_chroma_db(db, recognized_text) if recognized_text else (None, None)

        pred_percentage = [round(p * 100, 2) for p in pred]
        fragment_time = f"{i * 2},{(i + 1) * 2}"
        historical_data.append({
            'Número de Fragmento': i + 1,
            'Tiempo del Fragmento': fragment_time,
            'Texto': recognized_text or "",
            'Embedding Asociado': document or "",
            'Distancia': f"{distance:.4f}" if distance else "",
            **{label: percentage for label, percentage in zip(labels, pred_percentage)}
        })

        st.write(f"Fragmento {i + 1}: Probabilidades")
        st.table(pd.DataFrame({'Label': labels, 'Probabilidad (%)': pred_percentage}))

        st.write(f"Fragmento {i + 1}: Texto Identificado")
        st.table(pd.DataFrame({
            'Texto': [recognized_text or ""],
            'Embedding Asociado': [document or ""],
            'Distancia': [f"{distance:.4f}" if distance else ""]
        }))

        os.remove(fragment_filename)

    # Aquí se realiza el cambio para que el archivo se guarde con el nombre del dataset y el modelo seleccionado
    dataset_name = os.path.splitext(uploaded_file.name)[0]  # El nombre base del archivo de audio
    model_name = model_choice.replace(" ", "_").replace("con", "").lower()  # Formatear el nombre del modelo
    output_filename = f"{dataset_name}_{model_name}_historico.xlsx"  # Crear el nombre del archivo
    output_path = os.path.join(HISTORIC_DIR, output_filename)
    
    pd.DataFrame(historical_data).to_excel(output_path, index=False)
    st.success(f"Histórico guardado en: {output_path}")
