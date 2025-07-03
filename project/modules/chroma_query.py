__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


from chromadb import PersistentClient
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

# Configuración global para ChromaDB
CHROMA_PATH = 'data_embeddings/'
COLLECTION_NAME = 'violence_embeddings_DB'
MODEL_NAME = "all-mpnet-base-v2"

def load_chroma_db(chroma_path=CHROMA_PATH, collection_name=COLLECTION_NAME):
    """
    Carga o conecta a una colección existente en ChromaDB.
    Si la colección no existe, la crea con la función de embeddings adecuada.
    Args:
        chroma_path (str): Ruta donde se almacenan los datos de ChromaDB.
        collection_name (str): Nombre de la colección a cargar o crear.
    Returns:
        Collection: Colección de ChromaDB lista para consultas.
    """
    client_persistent = PersistentClient(path=chroma_path)
    try:
        db = client_persistent.get_collection(name=collection_name)
        print(f"Colección '{collection_name}' cargada exitosamente.")
    except Exception as e:
        # Si la colección no existe, se crea con la función de embeddings
        embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)
        db = client_persistent.create_collection(
            name=collection_name,
            embedding_function=embedding_function,
            metadata={"hnsw:space": "cosine"}  # Configurar distancia cosine
        )
        print(f"Colección '{collection_name}' creada exitosamente.")
    return db

def query_chroma_db(db, input_text, model_name=MODEL_NAME, n_results=1):
    """
    Realiza una consulta semántica en la base vectorial de ChromaDB usando embeddings.
    Args:
        db (Collection): Colección de ChromaDB.
        input_text (str): Texto a consultar.
        model_name (str): Nombre del modelo de embeddings.
        n_results (int): Número de resultados a retornar.
    Returns:
        tuple: (documento más similar, distancia de similitud) o (None, None) si no hay resultados.
    """
    # Se genera el embedding del texto de entrada
    model = SentenceTransformer(model_name)
    query_embedding = model.encode(input_text).tolist()
    # Se consulta la base vectorial
    results = db.query(query_embeddings=[query_embedding], n_results=n_results)

    if results['documents'] and results['distances']:
        document = results['documents'][0][0]
        distance = results['distances'][0][0]
        return document, distance
    return None, None