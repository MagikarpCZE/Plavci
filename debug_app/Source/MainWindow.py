#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySide6
from PySide6.QtWidgets import QMainWindow, QApplication
from Source.__windows.main_window import Ui_MainWindow
from .MotorWidget import MotorWidget

class MainWindow(QMainWindow):
	"""
	The main window of the program.

	Attributes:
		app(QApplication): reference to an instance of the QApplication 
						   class for changing the application style.
	"""

	def __init__(self, app: QApplication) -> None:
		"""Class initialization."""
		super(MainWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.app = app

		self.motor_list = []
		self.initialize_ui()

	def initialize_ui(self) -> None:
		"""Initialize the basic functions and settings of the window."""
		self.ui.btn_add_motor.clicked.connect(self.add_button_clicked)
		self.ui.btn_delete_motor.clicked.connect(self.delete_button_clicked)

	def add_button_clicked(self) -> None:
		"""Add new motor."""
		motor = MotorWidget(1, len(self.motor_list)+1)
		layout = self.ui.motors_container.widget().layout()
		layout.addWidget(motor)
		self.motor_list.append(motor)

		self.log(f"Motor {len(self.motor_list)} was added.")

	def delete_button_clicked(self) -> None:
		"""Delete last motor."""
		if len(self.motor_list) > 0:
			motor = self.motor_list.pop(-1)
			self.ui.motors_container.widget().layout().removeWidget(motor)
			motor.deleteLater()

			self.log(f"Motor {len(self.motor_list)+1} was deleted.")

		else:
			self.log(f"Motor list is empty.")


	def log(self, log: str) -> None:
		"""Write text in console."""
		self.ui.console_plain.appendPlainText(log)
