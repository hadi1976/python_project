"""
Author: Viviana Eloisa Quezada Dominguez
The "config.py" file, is importing all the libraries and modules that are
required for the correct functionality of this code.As well as, the path
of the GUI inputs.

Also, in case one of the libraries or modules is not properly installed
or the path of the GUI cannot be found. The user will be able to realize
that is an ImportError with its respective message.
"""

try:
    import os
    import logging
    import math
except ImportError:
    logging.info("ERROR: Cannot import basic Python libraries.")

try:
    import numpy as np
    import pandas as pd
except ImportError:
    logging.info("ERROR: Cannot import SciPy libraries.")

try:
    import matplotlib.pyplot as plt
except ImportError:
    logging.info("ERROR: Cannot import Matplotlib libraries")

try:
    import tkinter as tk
    from tkinter.messagebox import showinfo
    from tkinter import ttk
except ImportError:
    logging.info("ERROR: Cannot import tkinter modules")

try:
    from openpyxl import load_workbook
except ImportError:
    logging.info("ERROR: Cannot import openpyxl libraries")

try:
    p = os.path.abspath("")
    country = p + "/inputs/country.txt"
    country_codes = p + "/Country_Codes_and_Names.xlsx"
    inhabitants = p + "/inputs/Input1.txt"
    user_elevation = p + "/inputs/Input2.txt"
    transmission_pipe_length = p + "/inputs/Input5.txt"
    distribution_pipe_length = p + "/inputs/Input6.txt"
except ImportError:
    logging.info("ERROR: Cannot import the input path")

# Creating the log file.
logging.basicConfig(filename="my-logfile.log",
                    format="%(asctime)s - %(message)s",
                    filemode="w", level=logging.DEBUG)
