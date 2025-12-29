from rich.console import Console
from rich.table import Table
import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Cargamos variables de entorno si existen
load_dotenv()

console = Console()

def mostrar_demo():
    console.print("[bold blue]¡Librerías instaladas con éxito![/bold blue]\n")
    
    # Ejemplo de Tabla con Rich
    table = Table(title="Librerías Recomendadas por Antigravity")
    table.add_column("Librería", style="cyan", no_wrap=True)
    table.add_column("Propósito", style="magenta")
    table.add_column("Estado", justify="right", style="green")

    librerias = [
        ("requests", "Peticiones HTTP / APIs", "Instalado"),
        ("pandas", "Análisis de Datos", "Instalado"),
        ("python-dotenv", "Variables de Entorno", "Instalado"),
        ("rich", "Interfaces de Terminal Pro", "Instalado"),
        ("pytest", "Pruebas de Software", "Instalado")
    ]

    for lib, prop, status in librerias:
        table.add_row(lib, prop, status)

    console.print(table)
    
    # Pequeña prueba de Pandas
    data = {"Proyecto": ["Prueba", "Cloud", "AI"], "Versión": [1.0, 2.1, 0.5]}
    df = pd.DataFrame(data)
    console.print("\n[bold yellow]Vista previa de datos (Pandas):[/bold yellow]")
    console.print(df)

if __name__ == "__main__":
    mostrar_demo()
