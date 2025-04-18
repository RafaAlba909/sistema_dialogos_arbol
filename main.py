import tkinter as tk
from tkinter import ttk
from cargar_escenas import cargar_escenas
from interfaz import JuegoGUI

def main():
    escenas = cargar_escenas()
    escena_inicial = "Introducción"

    root = tk.Tk()
    root.title("The Last of Us - Sistema de Diálogos Avanzado")
    root.geometry("800x600")
    root.resizable(False, False)
    root.style = ttk.Style()
    root.style.theme_use('clam') # Un tema moderno

    app = JuegoGUI(root, escenas, escena_inicial)
    root.mainloop()

if __name__ == "__main__":
    main()