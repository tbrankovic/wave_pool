import customtkinter
from tbrankovic.gui.PulseFrame import PulseFrame
from tbrankovic.gui.MessageFrame import MessageFrame
from tbrankovic.gui.WaveformFrame import WaveformFrame
from tbrankovic.utils.generate_waveform import generate_waveform


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Waveform Generator")
        self.geometry("1280x720")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1, minsize=600)
        self.grid_columnconfigure(1, weight=1, minsize=600)  # ensure equal width for both columns
        self.grid_rowconfigure(1, weight=1, minsize=250)  # Set minsize for the additional frame

        self.pulse_frame = PulseFrame(master=self)
        self.pulse_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")

        self.message_frame = MessageFrame(master=self, pulse_frame=self.pulse_frame)
        self.message_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew")

        self.waveform_frame = WaveformFrame(master=self, pulse_frame=self.pulse_frame, message_frame=self.message_frame)
        self.waveform_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")

