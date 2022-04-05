import ctypes
import os

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.path.abspath("images/mortal_kombat.jpg").encode(), 0)