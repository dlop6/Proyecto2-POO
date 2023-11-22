import tkinter as tk
from  tkcalendar import Calendar

def on_select_date(date):
    print("Fecha seleccionada:", date)

root = tk.Tk()
root.title("Calendario de Ejemplo")

cal = Calendar(root, selectmode="day", year=2023, month=11, day=7)
cal.pack(pady=20)

btn = tk.Button(root, text="Seleccionar Fecha", command=lambda: on_select_date(cal.get_date()))
btn.pack(pady=20)

root.mainloop()