
from escena import Escena

def cargar_escenas():
    escenas = {
        "Introducción": Escena(
            "Introducción",
            "El Inicio",
            "Una vieja casa abandonada. Joel se detiene en seco, escucha algo.\nEllie: Joel... ¿escuchaste eso?",
            [
                {"texto": "Sí. Quédate atrás.", "siguiente_id": "Escena_2", "efecto": lambda estado: estado},
                {"texto": "No es nada. Vamos.", "siguiente_id": "Escena_3", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/casa_abandonada.png"
        ),
        "Escena_2": Escena(
            "Escena_2",
            "Sospecha",
            "Joel observa una figura en la oscuridad.",
            [
                {"texto": "Hablar.", "siguiente_id": "Escena_4", "efecto": lambda estado: estado},
                {"texto": "Ignorar.", "siguiente_id": "Escena_5", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/silueta.png"
        ),
        "Escena_3": Escena(
            "Escena_3",
            "Caída",
            "Ignoras el sonido y caes en un sótano.",
            [
                {"texto": "Buscar salida.", "siguiente_id": "Escena_6", "efecto": lambda estado: estado},
                {"texto": "Llamar a Ellie.", "siguiente_id": "Escena_7", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/sotano.png"
        ),
        "Escena_4": Escena(
            "Escena_4",
            "Encuentro",
            "Hablas con Silas, un superviviente.",
            [
                {"texto": "Ayuda.", "siguiente_id": "Escena_8", "efecto": lambda estado: estado},
                {"texto": "Solo.", "siguiente_id": "Escena_9", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/silas.png"
        ),
        "Escena_5": Escena(
            "Escena_5",
            "Bloqueo",
            "El camino está bloqueado.",
            [
                {"texto": "Volver.", "siguiente_id": "Introducción", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/bloqueo.png"
        ),
        "Escena_6": Escena(
            "Escena_6",
            "Salida?",
            "Buscas una forma de salir del sótano.",
            [
                {"texto": "Puerta.", "siguiente_id": "Escena_10", "efecto": lambda estado: estado},
                {"texto": "Escalar.", "siguiente_id": "Escena_11", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/sotano_salida.png"
        ),
        "Escena_7": Escena(
            "Escena_7",
            "Respuesta?",
            "Llamas a Ellie.",
            [
                {"texto": "Espera.", "siguiente_id": "Escena_12", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/llamando.png"
        ),
        "Escena_8": Escena(
            "Escena_8",
            "Con Silas",
            "Silas se une a vosotros.",
            [
                {"texto": "Ruta?", "siguiente_id": "Escena_13", "efecto": lambda estado: estado},
                {"texto": "Cuidado.", "siguiente_id": "Escena_14", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/con_silas.png"
        ),
        "Escena_9": Escena(
            "Escena_9",
            "Solos",
            "Seguís solos.",
            [
                {"texto": "Pueblo.", "siguiente_id": "Escena_15", "efecto": lambda estado: estado},
                {"texto": "Bosque.", "siguiente_id": "Escena_16", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/solos.png"
        ),
        "Escena_10": Escena(
            "Escena_10",
            "Puerta Sótano",
            "La puerta está cerrada.",
            [
                {"texto": "Forzar.", "siguiente_id": "Escena_17", "efecto": lambda estado: estado},
                {"texto": "Buscar llave.", "siguiente_id": "Escena_18", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/puerta_sotano.png"
        ),
        "Escena_11": Escena(
            "Escena_11",
            "Escalar Sótano",
            "Intentas escalar.",
            [
                {"texto": "Éxito.", "siguiente_id": "Escena_19", "efecto": lambda estado: estado},
                {"texto": "Fallo.", "siguiente_id": "Escena_7", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/escalar.png"
        ),
        "Escena_12": Escena(
            "Escena_12",
            "Silencio Ellie",
            "No hay respuesta.",
            [
                {"texto": "Reintentar.", "siguiente_id": "Escena_7", "efecto": lambda estado: estado},
                {"texto": "Buscar otra salida.", "siguiente_id": "Escena_6", "efecto": lambda estado: estado},
            ],
            imagen="imagenes/silencio.png"
        ),
        "Escena_13": Escena(
            "Escena_13",
            "Ruta Silas",
            "Preguntas sobre la ruta.",
            [],
            imagen="imagenes/ruta_silas.png"
        ),
        "Escena_14": Escena(
            "Escena_14",
            "Cuidado Silas",
            "Estás cauteloso con Silas.",
            [],
            imagen="imagenes/cuidado_silas.png"
        ),
        "Escena_15": Escena(
            "Escena_15",
            "Pueblo Solos",
            "Llegas a un pueblo.",
            [],
            imagen="imagenes/pueblo_solos.png"
        ),
        "Escena_16": Escena(
            "Escena_16",
            "Bosque Solos",
            "Entras en el bosque.",
            [],
            imagen="imagenes/bosque_solos.png"
        ),
        "Escena_17": Escena(
            "Escena_17",
            "Forzar Puerta",
            "Intentas forzar la puerta.",
            [],
            imagen="imagenes/forzar_puerta.png"
        ),
        "Escena_18": Escena(
            "Escena_18",
            "Buscar Llave",
            "Buscas la llave en el sótano.",
            [],
            imagen="imagenes/buscar_llave.png"
        ),
        "Escena_19": Escena(
            "Escena_19",
            "Fuera Sótano",
            "Logras salir del sótano.",
            [],
            imagen="imagenes/fuera_sotano.png"
        ),
    }
    return escenas