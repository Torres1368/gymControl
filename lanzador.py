import subprocess
import os
import threading
import webbrowser
from filelock import FileLock, Timeout
from tkinter import Tk, messagebox
import sys

# Ruta al archivo de bloqueo
lock_path = os.path.abspath("clientes.lock")
lock = FileLock(lock_path, timeout=1)

try:
    with lock:
        ruta_manage = os.path.abspath("C:/Users/Dash-J/Desktop/GYM/gym/manage.py")

        def iniciar_django():
            subprocess.Popen(
                ['python', ruta_manage, 'runserver', '0.0.0.0:8000'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

        threading.Thread(target=iniciar_django, daemon=True).start()

        # Abrir navegador predeterminado
        webbrowser.open("http://127.0.0.1:8000")

        # Esto mantiene el script vivo mientras el navegador está abierto
        root = Tk()
        root.withdraw()
        messagebox.showinfo("Iron Fit", "✅ Servidor iniciado.\n\nPuedes cerrar esta ventana cuando termines.")

except Timeout:
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Iron Fit", "⚠️ La aplicación ya está en ejecución.")
    sys.exit()
