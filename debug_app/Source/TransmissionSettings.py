#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySide6
from PySide6.QtWidgets import QDialog, QApplication
from Source.__windows.transmission_settings import Ui_Dialog

class TransmissionSettings(QDialog):
	"""
	The main window of the program.
	"""

	def __init__(self) -> None:
		"""Class initialization."""
		super(TransmissionSettings, self).__init__()

		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
