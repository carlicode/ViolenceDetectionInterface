from chroma_query import load_chroma_db

# Lista de textos de referencia (puedes modificar o ampliar esta lista)
textos = [
    "¡Auxilio, me están atacando!",
    "¿Qué es esto? ¡Él trajo a la policía!",
    "¡No me pegues!",
    "¡Disparos en la calle!",
    "Se escuchan gritos y vidrios rotos.",
    "Por favor, no me hagas daño.",
    "Llama a la policía, hay violencia.",
    "¡Socorro!",
    "Alguien está gritando muy fuerte.",
    "Se oyen disparos y gritos de miedo.",
    # ... agrega más frases relevantes ...
]

def poblar_chroma_db(db, textos):
    for i, texto in enumerate(textos):
        db.add(
            documents=[texto],
            ids=[f"doc_{i}"]
        )
    print(f"Se agregaron {len(textos)} documentos a la colección.")

if __name__ == "__main__":
    db = load_chroma_db()
    poblar_chroma_db(db, textos) 