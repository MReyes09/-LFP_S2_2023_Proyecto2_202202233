import copy
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from controller.analyst import Analyst
from controller.sintactico import Sintactico


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
        self.analyst = None
        self.list_error = []

        self.build_Componentes()

        self.btnAbrir.bind("<Button-1>", self.open_File)
        self.btnAnalizar.bind("<Button-1>", self.analyst_Data)
        self.cmbReportes.bind("<<ComboboxSelected>>", self.accion_cmb)

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

    def analyst_Data(self, event):

        if self.file_Path:

            try:

                text = self.txtArea.get(1.0, tk.END)
                self.analyst = Analyst(text)
                self.analyst.analyst_Data()
                sintactico = Sintactico(copy.copy(self.analyst.tokens))
                sintactico.analyst_Syntactic()

                if len(self.analyst.errores_Lex_List) != 0 or len(sintactico.errores_Sintacticos) != 0:

                    self.list_error = []

                    for er_lexico in self.analyst.errores_Lex_List:
                        self.list_error.append(er_lexico)

                    for er_sin in sintactico.errores_Sintacticos:
                        self.list_error.append(er_sin)

                    messagebox.showwarning("Errores detectados", "Se han detectado errores en el archivo, puedes consultar \n"
                         "el reporte de errores para mayor información.")

                else:

                    self.list_error = []

                    if len(sintactico.results) > 0:

                        self.txtConsola.config(state="normal")

                        for res in sintactico.results:

                            if res.r is not None:

                                self.txtConsola.insert('end', str(res.r) + '\n')

                                if res.f == "exportarReporte":

                                    messagebox.showinfo("Reporte html", f"Tu archivo html ha sido creado con exito")

                        self.txtConsola.config(state="disabled")

                    messagebox.showinfo("Análisis completado", "El archivo se ha analisado correctamente")

            except Exception as e:

                print(f"Error: {e}")
                messagebox.showwarning("Errores critico",
                                       "Se han detectado errores en el archivo, puedes consultar \n"
                                       "el reporte de errores para mayor información.")

        else:

            messagebox.showwarning("Cuidado", "Aun no has abierto ningun archivo bizdata")

    def accion_cmb(self, event):

        """
        Esta funcion controla los posibles resultados ya definidos en el cmb, el cual ejecutara una accion
        dependiendo de cual se escoja
        """

        selected_option = self.cmbReportes.get()  # Se obtiene el valor actual del cmb

        if selected_option == "Errores":

            self.report_Error(True)
            messagebox.showinfo("Reporte de Errores", "El reporte se ha creado correctamente, puedes verlo en la carpeta de reportes")

        elif selected_option == "Tokens":

            self.report_Error(False)
            messagebox.showinfo("Reporte De Tokens",
                                "El reporte se ha creado correctamente, puedes verlo en la carpeta de reportes")

    def report_Error(self, errores):

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        </head>
        <body>"""
        filepath = ""
        if errores:
            html += "<h1>Errores Encontrados</h1>"
            filepath = "reportes/reporte_Errores.html"
        elif errores is False:
            html += "<h1>Tokens Obtenidos</h1>"
            filepath = "reportes/reporte_Tokens.html"

        html += """<table class="w3-table w3-striped">
                <tr>
                    <th>TIPO</th>
                    <th>CARACTER</th>
                    <th>FILA</th>
                    <th>COLUMNA</th>
                </tr>
        """
        if errores:

            for er in self.list_error:

                fila = f"""
                <tr>
                    <td>{er.tipo}</td>
                    <td>{er.lexema}</td>
                    <td>{er.fila}</td>
                    <td>{er.columna}</td>
                </tr>
                """
                html += fila

        elif errores is False:

            for er in self.analyst.tokens:
                fila = f"""
                <tr>
                    <td>{er.nombre}</td>
                    <td>{er.lexema}</td>
                    <td>{er.fila}</td>
                    <td>{er.columna}</td>
                </tr>
                """
                html += fila

        # Cierre del documento HTML
        html += """
        </table>
        </body>
        </html>
        """

        with open(filepath, "w", encoding="utf-8") as archivo:
            archivo.write(html)