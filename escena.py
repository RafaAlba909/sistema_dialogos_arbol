
class Escena:
    def __init__(self, id, titulo, descripcion, opciones, imagen=None, eventos=None):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.opciones = opciones
        self.imagen = imagen  
        self.eventos = eventos if eventos else [] 

    def elegir_opcion(self, indice, estado_jugador):
        if 0 <= indice < len(self.opciones):
            opcion = self.opciones[indice]
            
            if "condicion" not in opcion or opcion["condicion"](estado_jugador):
                return opcion["siguiente_id"], opcion.get("efecto", lambda x: x)(estado_jugador)
        return None, estado_jugador

