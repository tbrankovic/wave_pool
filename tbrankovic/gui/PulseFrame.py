import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tbrankovic.filters.pulse_shape import pulse_shape
from tbrankovic.utils.plot_graph import plot_graph


class PulseFrame(customtkinter.CTkFrame):

    periods = 10
    taps = 201
    pulse_x, pulse_y = None, None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add title
        self.label = customtkinter.CTkLabel(self)
        self.label.configure(text="Pulse", font=('default', 24, 'bold'), anchor="w")
        self.label.grid(row=0, column=0, padx=24, pady=18, sticky="ew")

        # initialize option menu
        self.optionmenu_var = customtkinter.StringVar(value="Square")
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Square", "Raised cosine"],
                                                      command=self.optionmenu_callback,
                                                      variable=self.optionmenu_var,
                                                      state="normal")
        self.optionmenu.grid(row=1, column=0, padx=24, pady=(0, 8), sticky="w")

        # initialize canvas
        self.canvas = None

        # plot initial graph
        self.pulse_x, self.pulse_y = pulse_shape(PulseFrame.periods, PulseFrame.taps, self.optionmenu_var.get())
        self.update_canvas(self.pulse_x, self.pulse_y)

        # initialize custom taps entry
        self.taps_entry_label = customtkinter.CTkLabel(self, text="Taps/points:")
        self.taps_entry_label.grid(row=2, column=0, padx=24, pady=8, sticky="w")

        self.taps_entry = customtkinter.CTkEntry(self, placeholder_text=str(PulseFrame.taps))
        self.taps_entry.grid(row=2, column=0, padx=128, pady=8, sticky="w")
        self.taps_entry.bind("<Return>", self.taps_entry_submit_handler)  # Bind return key press event

        # initialize custom periods entry
        self.periods_entry_label = customtkinter.CTkLabel(self, text="Periods:")
        self.periods_entry_label.grid(row=3, column=0, padx=24, pady=0, sticky="w")

        self.periods_entry = customtkinter.CTkEntry(self, placeholder_text=str(PulseFrame.periods))
        self.periods_entry.grid(row=3, column=0, padx=128, pady=0, sticky="w")
        self.periods_entry.bind("<Return>", self.periods_entry_submit_handler)  # Bind return key press event

    def update_canvas(self, x, y):
        # clear previous plot
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # plot graph
        fig = plot_graph(x, y)
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=4, column=0, padx=24, pady=0, sticky="nsew")

    def optionmenu_callback(self, choice):
        # plot graph based on selected choice
        self.pulse_x, self.pulse_y = pulse_shape(PulseFrame.periods, PulseFrame.taps, choice)
        self.update_canvas(self.pulse_x, self.pulse_y)

    def taps_entry_submit_handler(self, event):
        # get text from the entry
        entry_text = self.taps_entry.get()
        try:
            # try converting taps entry to integer
            taps = int(entry_text)

            # call pulse_shape with the taps and update the plot
            PulseFrame.taps = taps
            x, y = pulse_shape(PulseFrame.periods, PulseFrame.taps, self.optionmenu_var.get())
            self.update_canvas(x, y)
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    def periods_entry_submit_handler(self, event):
        entry_text = self.periods_entry.get()
        try:
            # try converting periods entry to integer
            periods = int(entry_text)

            # call pulse_shape with the periods and update the plot
            PulseFrame.periods = periods
            x, y = pulse_shape(PulseFrame.periods, PulseFrame.taps, self.optionmenu_var.get())
            self.update_canvas(x, y)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
