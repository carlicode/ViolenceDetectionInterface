import numpy as np
import librosa
import os
from keras.models import load_model

# Configuración inicial para el procesamiento de audio
# Se definen los parámetros globales para la extracción de características
# target_sampling_rate: frecuencia de muestreo objetivo
# n_mels: número de bandas Mel
# fmax: frecuencia máxima para el espectrograma

target_sampling_rate = 16000
n_mels = 128
fmax = 8000

def load_audio_model(model_path):
    """
    Carga un modelo preentrenado de Keras para predicción de audio.
    Args:
        model_path (str): Ruta al archivo .h5 del modelo.
    Returns:
        keras.Model: Modelo cargado listo para predecir.
    Raises:
        FileNotFoundError: Si el archivo no existe en la ruta especificada.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"El modelo no se encuentra en la ruta especificada: {model_path}")
    return load_model(model_path)

def split_audio(audio, sr, duration=2):
    """
    Divide un array de audio en fragmentos de duración fija.
    Args:
        audio (np.ndarray): Señal de audio.
        sr (int): Frecuencia de muestreo.
        duration (int): Duración de cada fragmento en segundos.
    Returns:
        list: Lista de fragmentos de audio (np.ndarray).
    """
    fragment_length = duration * sr
    num_fragments = len(audio) // fragment_length
    # Se generan los fragmentos cortando el array de audio
    fragments = [audio[i * fragment_length: (i + 1) * fragment_length] for i in range(num_fragments)]
    return fragments

def process_fragment(fragment, sr, n_mels=n_mels, fmax=fmax):
    """
    Convierte un fragmento de audio en un Mel-espectrograma en escala logarítmica.
    Args:
        fragment (np.ndarray): Fragmento de audio.
        sr (int): Frecuencia de muestreo.
        n_mels (int): Número de bandas Mel.
        fmax (int): Frecuencia máxima.
    Returns:
        np.ndarray: Mel-espectrograma en dB.
    """
    # Se calcula el Mel-espectrograma
    spectrogram = librosa.feature.melspectrogram(y=fragment, sr=sr, n_mels=n_mels, fmax=fmax)
    # Se convierte a escala logarítmica (dB)
    spectrogram = librosa.power_to_db(spectrogram, ref=np.max)
    return spectrogram

def predict_episode(episodes, model):
    """
    Realiza predicciones sobre una lista de fragmentos de audio usando el modelo cargado.
    Args:
        episodes (list): Lista de fragmentos de audio (np.ndarray).
        model (keras.Model): Modelo de predicción.
    Returns:
        list: Lista de predicciones para cada fragmento.
    """
    predictions = []
    for episode in episodes:
        # Se procesa el fragmento a espectrograma
        spectrogram = process_fragment(episode, target_sampling_rate)
        # Se ajustan las dimensiones para el modelo (batch, alto, ancho, canales)
        spectrogram = np.expand_dims(spectrogram, axis=-1)  # Añade canal
        spectrogram = np.expand_dims(spectrogram, axis=0)   # Añade batch
        pred = model.predict(spectrogram)
        predictions.append(pred[0])  # Se guarda la predicción del fragmento
    return predictions
