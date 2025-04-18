# interfaz.py (fragmento modificado)

import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from escena import Escena

class JuegoGUI:
    def __init__(self, root, escenas, id_escena_inicial):
        self.root = root
        self.escenas = escenas
        self.escena_actual = None
        self.historial = []
        self.estado_jugador = {"inventario": [], "salud": 100}
        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.imagen_label = ttk.Label(self.frame)
        self.imagen_label.pack(pady=10)

        self.titulo_label = ttk.Label(self.frame, font=("Helvetica", 16, "bold"), wraplength=600, justify="center")
        self.titulo_label.pack(pady=(10, 5))

        self.descripcion_label = ttk.Label(self.frame, font=("Helvetica", 12), wraplength=600, justify="left")
        self.descripcion_label.pack(pady=10)

        self.botones_frame = ttk.Frame(self.frame)
        self.botones_frame.pack(pady=10, fill="x")

        self.historial_button = ttk.Button(self.frame, text="Ver Historial", command=self.mostrar_historial)
        self.historial_button.pack(pady=10)
        self.historial_ventana = None

        self.mostrar_escena(id_escena_inicial)

    def mostrar_imagen(self, ruta_imagen):
        try:
            imagen = PhotoImage(file=ruta_imagen)
            self.imagen_label.config(image=imagen)
            self.imagen_label.image = imagen
        except:
            self.imagen_label.config(image="")
            self.imagen_label.image = None

    def mostrar_escena(self, escena_id):
        escena = self.escenas.get(escena_id)
        self.escena_actual = escena

        for widget in self.botones_frame.winfo_children():
            widget.destroy()

        if escena:
            self.mostrar_imagen(escena.imagen)
            self.titulo_label.config(text=escena.titulo)
            self.descripcion_label.config(text=escena.descripcion)

            for i, opcion in enumerate(escena.opciones):
                texto_boton = opcion["texto"]
                boton = ttk.Button(
                    self.botones_frame,
                    text=f"{i + 1}. {texto_boton}",
                    command=lambda i=i: self.seleccionar_opcion(i)
                )
                boton.pack(fill="x", padx=20, pady=5)

            for evento in escena.eventos:
                self.ejecutar_evento(evento)

            if not escena.opciones:
                self.root.after(2000, self.mostrar_arbol_decisiones)
        else:
            self.titulo_label.config(text="¡Fin de la historia!")
            self.descripcion_label.config(text="Has llegado al final de este camino.")
            self.mostrar_imagen(None)
            self.mostrar_arbol_decisiones() # Mostrar el árbol al final definitivo

    def ejecutar_evento(self, evento):
        tipo = evento["tipo"]
        if tipo == "mensaje":
            messagebox.showinfo("Mensaje", evento["texto"])
        elif tipo == "obtener_item":
            item = evento["item"]
            self.estado_jugador["inventario"].append(item)
            messagebox.showinfo("Objeto Encontrado", f"¡Has obtenido: {item}!")
        elif tipo == "dialogo":
            messagebox.showinfo(evento["personaje"], evento["texto"])
        elif tipo == "fin_juego":
            messagebox.showinfo("Fin del Juego", evento["mensaje"])
            self.root.quit()
        elif tipo == "combate":
            messagebox.showinfo("Combate", f"¡Te enfrentas a un {evento['enemigo']}!")
            self.estado_jugador["salud"] -= 20
            messagebox.showinfo("Combate", f"¡Has perdido 20 de salud! Salud actual: {self.estado_jugador['salud']}")
            if self.estado_jugador["salud"] <= 0:
                messagebox.showerror("Fin del Juego", "¡Has muerto!")
                self.root.quit()

    def seleccionar_opcion(self, indice):
        if self.escena_actual and 0 <= indice < len(self.escena_actual.opciones):
            opcion = self.escena_actual.opciones[indice]
            siguiente_id, nuevo_estado = self.escena_actual.elegir_opcion(indice, self.estado_jugador)
            texto = opcion["texto"]

            self.historial.append((texto, siguiente_id))
            self.estado_jugador = nuevo_estado

            if siguiente_id == "Escena_8_condicionada" and "mapa_refugio" in self.estado_jugador["inventario"]:
                self.mostrar_escena(siguiente_id)
            elif siguiente_id == "Escena_9_condicionada" and "mapa_refugio" not in self.estado_jugador["inventario"]:
                self.mostrar_escena(siguiente_id)
            else:
                self.mostrar_escena(siguiente_id)

    def mostrar_historial(self):
        if self.historial_ventana is None or not tk.Toplevel.winfo_exists(self.historial_ventana):
            self.historial_ventana = tk.Toplevel(self.root)
            self.historial_ventana.title("Historial de Decisiones")
            historial_frame = ttk.Frame(self.historial_ventana, padding=10)
            historial_frame.pack(fill="both", expand=True)

            ttk.Label(historial_frame, text="--- Historial de Decisiones ---", font=("Helvetica", 14, "bold")).pack(pady=5)

            for i, (opcion, escena_id) in enumerate(self.historial, 1):
                color = "green" if escena_id in self.escenas else "red"
                texto = f"{i}. {opcion} -> {escena_id}"
                ttk.Label(historial_frame, text=texto, font=("Helvetica", 12), foreground=color, anchor="w").pack(padx=5, pady=2)

            ttk.Label(historial_frame, text="\nFin del historial.", font=("Helvetica", 10, "italic")).pack(pady=10)
        else:
            self.historial_ventana.lift()

    def mostrar_arbol_decisiones(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        ttk.Label(
            self.frame,
            text="--- Árbol de Decisiones Final ---",
            font=("Helvetica", 16, "bold"),
            foreground="black"
        ).pack(pady=10)

        for i, (opcion, siguiente_id) in enumerate(self.historial, 1):
            color = "green"  # Todas las decisiones elegidas se mostrarán en verde
            texto = f"{i}. {opcion} -> {siguiente_id}"
            ttk.Label(
                self.frame,
                text=texto,
                font=("Helvetica", 12),
                foreground=color,
                anchor="w"
            ).pack(padx=10)

        ttk.Label(
            self.frame,
            text="\nFin del juego.",
            font=("Helvetica", 14, "italic")
        ).pack(pady=20)