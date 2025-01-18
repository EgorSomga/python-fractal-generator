


class fractalgenerator(tk.Tk):
    def __init__():
        super().init()



        self.title("Fractal Generator")
        self.geometry("800x600")

        self.size = 400 
        self.max_iter = 100
        self.julia_c = complex(-0.4,0.6)
        self.anfle = 0.5
        self.tree_ratio =0.7
        def.setup_ui(self):

    def setup_ui(self):
        control_frame == ttk.Frame(self)
        control_frame.pack(sede=tk.LEFT, fill = tk.Y, padx = 5, pady=5)

        ttk.Label(control_frame,text="Тип фракталу:").pack(pady=5)
        self.fractal_type = ttk.Combobox(control_frame, value = ["Мандельборна",\
            "Жюлія","Серпінського","Дерево"])
        self.fractal_type.set("Мальдельборна")
        self.fractal_type.pack(pady = 5)
        self.fractal_type.bind('<<ComboboxSelecte>>',self.on_fractal_change)

        ttk.Label(control_frame, text="Кількість ітерацій").pack(pady=5)
        self.iter_slider = ttk.Scale(control_frame, from_=10, to=200,\
            orient=tk.HORIZONTAL, value=100, command=self.on_param_change)
        self.iter_slider.pack(pady=5)

        self.julia_frame = ttk.LabelFrame(control_frame, text="Параметри Жюлія")
        ttk.Label(self.julia_frame,text="Реальна частина с:").pack()
        self.julia_real = ttk.Scale(self.julia_frame,from_=-2,to = 2,\
                                    )
