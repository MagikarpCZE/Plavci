#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySide6
from PySide6.QtWidgets import QWidget, QApplication
from Source.__windows.motor_widget import Ui_MotorWidget

class MotorWidget(QWidget):
	"""
	The motor widget.

	Attributes:
		app(QApplication): reference to an instance of the QApplication 
						   class for changing the application style.
		index(int): index of the motor.
	"""

	def __init__(self, app: QApplication, index: int) -> None:
		"""Class initialization."""
		super(MotorWidget, self).__init__()

		self.ui = Ui_MotorWidget()
		self.ui.setupUi(self)
		self.index = index
		self.ui.motor_label.setText(f"Motor {index} intesity")
		self.app = app

	def get_intensity(self) -> int:
		"""Return current motor intensity without percents."""
		return int(self.ui.motor_spinbox.text().replace('%', ''))