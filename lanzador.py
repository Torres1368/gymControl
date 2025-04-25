import webview
import subprocess
import os
import threading
from filelock import FileLock, Timeout
from tkinter import Tk, messagebox

# Ruta al archivo de bloqueo
lock_path = os.path.abspath("clientes.lock")
lock = FileLock(lock_path, timeout=1)

try:
    with lock:
        # Ruta absoluta al manage.py de tu proyecto
        ruta_manage = os.path.abspath("C:/Users/Dash-J/Desktop/CLIENTES/clienteApp/manage.py")

        # Función para iniciar Django
        def iniciar_django():
            subprocess.Popen(['python', ruta_manage, 'runserver'])

        # Iniciar Django en un hilo separado
        threading.Thread(target=iniciar_django, daemon=True).start()

        # Abrir la ventana web
        webview.create_window("Iron Fit", "http://0.0.0.0:8000")
        webview.start()

except Timeout:
    # Mostrar ventana emergente si ya está en ejecución
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Iron Fit", "⚠️ La aplicación ya está en ejecución.")
