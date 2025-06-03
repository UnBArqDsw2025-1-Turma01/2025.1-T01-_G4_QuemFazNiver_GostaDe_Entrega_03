usuarios = [
    {"id": 1, "nome": "João", "preferencias": {}},
    {"id": 2, "nome": "Maria", "preferencias": {}},
    {"id": 3, "nome": "Ana", "preferencias": {}}
]

def buscar_usuario_por_id(id_usuario):
    for u in usuarios:
        if u["id"] == id_usuario:
            return u
    return None