import customtkinter
from tbrankovic import App

# set theme
customtkinter.set_default_color_theme("tbrankovic/gui/light_theme.json")

# run windowed app
if __name__ == '__main__':

    app = App()
    app.mainloop()