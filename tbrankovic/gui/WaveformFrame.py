import os
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tbrankovic.utils.generate_awg_file import generate_awg_file
from tbrankovic.utils.generate_waveform import generate_waveform
from tbrankovic.utils.plot_waveform import plot_waveform


class WaveformFrame(customtkinter.CTkFrame):
    def __init__(self, master, pulse_frame, message_frame, **kwargs):
        super().__init__(master, **kwargs)

        # store references to PulseFrame and MessageFrame instances
        self.x = None
        self.y = None
        self.pulse_frame = pulse_frame
        self.message_frame = message_frame

        # add widgets onto the frame
        self.label = customtkinter.CTkLabel(self)
        self.label.configure(text="Waveform", font=('default', 24, 'bold'), anchor="w")
        self.label.grid(row=0, column=0, padx=24, pady=18, sticky="ew")

        # add button to generate the waveform
        self.button = customtkinter.CTkButton(self, text="Generate", command=self.update_waveform)
        self.button.grid(row=1, column=0, padx=24, pady=(0, 18), sticky="w")

        # add button to save waveform
        self.button = customtkinter.CTkButton(self, text="Save", command=self.save_waveform)
        self.button.grid(row=1, column=0, padx=196, pady=(0, 18), sticky="w")

        # add file path text extry
        self.save_file_path = customtkinter.StringVar(value="")
        self.file_path_entry = customtkinter.CTkEntry(self, placeholder_text="filename")
        self.file_path_entry.grid(row=1, column=0, padx=360, pady=(0, 18), sticky="w")
        # self.file_path_entry.bind("<Return>", self.hande_file_path_entry)  # Bind return key press event

        # initialize canvas
        self.canvas = None

    def update_waveform(self):
        print("Called update_waveform()")

        # fetch pulse_y and binary_message_stream variables from PulseFrame and MessageFrame instances
        pulse_y = self.pulse_frame.pulse_y
        binary_message_stream = self.message_frame.binary_message_stream

        # generate waveforms and display plot
        self.x, self.y = generate_waveform(pulse_y, binary_message_stream)
        self.update_canvas(self.x, self.y)

    def update_canvas(self, x, y):
        # clear previous plot
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # plot graph
        fig = plot_waveform(x, y)
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=2, column=0, padx=24, pady=0, sticky="nsew")

    def save_waveform(self):
        # check if entries are valid
        if self.y is None or self.file_path_entry.get() == '':
            return

        # ensure the waveform_out directory exists
        output_dir = os.path.join(os.getcwd(), 'waveform_out')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file_path = os.path.join(output_dir, self.file_path_entry.get() + '.txt')

        generate_awg_file(self.y, output_file_path)
