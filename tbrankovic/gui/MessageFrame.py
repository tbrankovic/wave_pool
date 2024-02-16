import customtkinter
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tbrankovic.utils.generate_stream import generate_stream
from tbrankovic.utils.plot_binary_graph import plot_binary_graph


class MessageFrame(customtkinter.CTkFrame):
    binary_message_stream = None
    size = 50

    def __init__(self, master, pulse_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.pulse_frame = pulse_frame

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self)
        self.label.configure(text="Message", font=('default', 24, 'bold'), anchor="w")
        self.label.grid(row=0, column=0, padx=24, pady=18, sticky="ew")

        # initialize option menu
        self.message_type = customtkinter.StringVar(value="Random")
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Random", "Alternating", "Custom"],
                                                      command=self.optionmenu_callback,
                                                      variable=self.message_type,
                                                      state="normal")
        self.optionmenu.grid(row=1, column=0, padx=24, pady=(0, 8), sticky="w")

        # entry for custom input
        self.message = customtkinter.StringVar(value="")
        self.message_entry = customtkinter.CTkEntry(self, placeholder_text="Message")
        self.message_entry.bind("<Return>", self.message_entry_return_handler)  # Bind return key press event

        # label for custom size
        self.size_entry_label = customtkinter.CTkLabel(self, text="Size:")
        self.size_entry_label.grid(row=2, column=0, padx=24, pady=0, sticky="w")

        # entry for custom size
        self.size_entry = customtkinter.CTkEntry(self, placeholder_text=str(self.size))
        self.size_entry.grid(row=2, column=0, padx=80, pady=0, sticky="w")
        self.size_entry.bind("<Return>", self.size_entry_return_handler)  # Bind return key press event

        # initialize canvas
        self.canvas = None

        # plot initial graph
        self.update_message_stream()  # plotting is contained in the update function

    def optionmenu_callback(self, choice):
        print("Selected", choice)

        if choice == "Custom":
            # show custom entry with placeholder text
            self.message_entry.grid(row=1, column=0, padx=196, pady=(0, 8), sticky="w")
        else:
            # hide custom entry if another option is selected
            self.message_entry.grid_forget()

        # update stream
        self.update_message_stream()

    def update_canvas(self, stream):
        # clear previous plot
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # plot graph
        fig = plot_binary_graph(stream)
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=4, column=0, padx=24, pady=0, sticky="nsew")

    def message_entry_return_handler(self, event):
        self.update_message_stream()

    def size_entry_return_handler(self, event):
        entered_size = self.size_entry.get()
        if entered_size.isdigit():
            self.size = int(entered_size)
            self.update_message_stream()
        else:
            print("Size must be an integer value.")

    def update_message_stream(self):
        self.binary_message_stream = generate_stream(self.message_type.get(), self.size, self.message_entry.get())
        self.update_canvas(self.binary_message_stream)