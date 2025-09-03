import tkinter as tk
from tkinter import ttk


class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Async Weather Dashboard")
        self._build_ui()

    def _build_ui(self):
        frm = ttk.Frame(self.root, padding=12)
        frm.pack(fill=tk.BOTH, expand=True)

        # City input
        self.city_var = tk.StringVar()
        ttk.Label(frm, text="City:").grid(row=0, column=0, sticky="w")
        ttk.Entry(frm, textvariable=self.city_var, width=24).grid(row=0, column=1, sticky="we")
        self.btn = ttk.Button(frm, text="Get Weather", command=self.on_get_weather)
        self.btn.grid(row=0, column=2, padx=6)

        # Status
        self.status = tk.StringVar(value="Ready")
        ttk.Label(frm, textvariable=self.status).grid(row=1, column=0, columnspan=3, sticky="w")

        # Weather placeholders
        self.temp = tk.StringVar()
        self.hum = tk.StringVar()
        self.desc = tk.StringVar()
        ttk.Label(frm, textvariable=self.temp, font=("", 14)).grid(row=2, column=0, columnspan=3, sticky="w")
        ttk.Label(frm, textvariable=self.hum).grid(row=3, column=0, columnspan=3, sticky="w")
        ttk.Label(frm, textvariable=self.desc).grid(row=4, column=0, columnspan=3, sticky="w")

        # Resize behavior
        frm.columnconfigure(1, weight=1)

    def on_get_weather(self):
        self.status.set("Fetching… (dummy)")
        self.temp.set("Temp: -- °C")
        self.hum.set("Humidity: --%")
        self.desc.set("Description: --")

    def run(self):
        self.root.mainloop()
 
