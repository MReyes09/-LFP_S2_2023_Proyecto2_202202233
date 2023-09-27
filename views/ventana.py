import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import json

class Ventana_Principal(tk.Tk):
    def __init__(self):

        super().__init__() # HEREDA DE TKINTER

        self.geometry("1400x600")
        self.title("Proyecto 2 - 202202233")
        self.navbar = tk.Frame(self, bg="#FFB38B")
        self.btnAbrir = ttk.Button(self.navbar, text="Abrir")
        self.btnAnalizar = ttk.Button(self.navbar, text="Analizar")
        self.cmbReportes = ttk.Combobox(self.navbar, state="readonly", values=[
            "Reportes", "Tokens", "Errores", "Árbol de derivación"
        ])
        self.txtContainer = tk.Frame(self)
        self.txtArea = tk.Text(self.txtContainer, width=105, height=50, bg="#BEFACB")
        self.txtConsola = tk.Text(self.txtContainer, width=100, height=100, bg="#F2DCC1", state="disabled")
        self.file_Path = None

        self.build_Componentes()

        self.btnAbrir.bind("<Button-1>", self.open_File)

    def build_Componentes(self):

        self.navbar.pack(fill=tk.X)
        self.cmbReportes.set("Reportes")
        self.cmbReportes.pack(side=tk.RIGHT, padx=5, pady=10)
        self.btnAnalizar.pack(side=tk.RIGHT, padx=5, pady=10)
        self.btnAbrir.pack(side=tk.RIGHT, padx=5, pady=10)

        self.txtContainer.pack(padx=10, pady=10)
        self.txtArea.pack(side=tk.LEFT, padx=5, pady=10)
        self.txtConsola.pack(side=tk.RIGHT, padx=5, pady=10)

    def open_File(self, event):

        try:

            self.file_Path = filedialog.askopenfilename(filetypes=[("Archivos BIZDATA", "*.bizdata")])
            file_path = self.file_Path

            if file_path:
                with open(file_path, 'r') as file:
                    content = file.read()  # Transforma el contenido del archivo en un Str

                self.txtArea.delete(1.0, tk.END)
                self.txtArea.insert(tk.END, content)

        except Exception as e:

            print(f"Error: {e}")
