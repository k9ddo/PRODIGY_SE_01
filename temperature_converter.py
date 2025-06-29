import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        value = float(entry.get())
        unit = unit_var.get()
        if unit == 'C':
            f = (value * 9/5) + 32
            k = value + 273.15
            result_label.config(text=f"Fahrenheit: {f:.2f}, Kelvin: {k:.2f}")
        elif unit == 'F':
            c = (value - 32) * 5/9
            k = c + 273.15
            result_label.config(text=f"Celsius: {c:.2f}, Kelvin: {k:.2f}")
        elif unit == 'K':
            c = value - 273.15
            f = (c * 9/5) + 32
            result_label.config(text=f"Celsius: {c:.2f}, Fahrenheit: {f:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x150")

entry = tk.Entry(window)
entry.pack(pady=5)

unit_var = tk.StringVar(value='C')
unit_menu = tk.OptionMenu(window, unit_var, 'C', 'F', 'K')
unit_menu.pack()

tk.Button(window, text="Convert", command=convert_temperature).pack(pady=5)
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
