#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySide6
from PySide6.QtWidgets import QMainWindow, QApplication
from Source.__windows.main_window import Ui_MainWindow
from Source.MotorWidget import MotorWidget
import Source.TransmissionSettings as TransmissionSettings

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
		self.initialize_ui()

		self.motor_list = []
		self.transmission_settings = {
			'continuosly_data_transmission': False,
			'transmission_rate': 1,
			'port': 'COM1'
		}

	def initialize_ui(self) -> None:
		"""Initialize the basic functions and settings of the window."""
		self.ui.actionTransmission_Settings.triggered.connect(self.options_button_clicked)
		self.ui.actionCommunication_Send_Data.triggered.connect(self.send_data_button_clicked)

		self.ui.btn_add_motor.clicked.connect(self.add_button_clicked)
		self.ui.btn_delete_motor.clicked.connect(self.delete_button_clicked)

	def add_button_clicked(self) -> None:
		"""Add new motor."""
		motor = MotorWidget(1, len(self.motor_list)+1)
		layout = self.ui.motors_container.widget().layout()
		layout.addWidget(motor)
		self.motor_list.append(motor)

		self.log(f"[SYSTEM] Motor {len(self.motor_list)} was added.")

	def delete_button_clicked(self) -> None:
		"""Delete last motor."""
		if len(self.motor_list) > 0:
			motor = self.motor_list.pop(-1)
			self.ui.motors_container.widget().layout().removeWidget(motor)
			motor.deleteLater()

			self.log(f"[SYSTEM] Motor {len(self.motor_list)+1} was deleted.")

		else:
			self.log(f"[SYSTEM] Motor list is empty.")

	def options_button_clicked(self) -> None:
		"""Handle click on transmission settings button."""
		window = TransmissionSettings.TransmissionSettings(self.transmission_settings)
		if window.exec():
			self.transmission_settings = window.get_parameters()
			self.change_send_data_button_state()

		lines = "\n".join(f"\t{k}: {v}" for k, v in self.transmission_settings.items())
		self.log(f"[SYSTEM] Set settings:\n{lines}\n")

	def send_data_button_clicked(self) -> None:
		"""Handle click on send data button."""
		if len(self.motor_list) > 0:
			self.serial_communication()

			string_to_send = ''

			for motor in self.motor_list:
				string_to_send = f'{string_to_send}{motor.get_intensity()};' 

			self.log(f"[SYSTEM] Data just sended on port {self.transmission_settings['port']}")
			self.log(f"Sended data string: {string_to_send}\n")

		else:
			self.log("[SYSTEM] Data was not sended, motor list is empty.")

	def change_send_data_button_state(self) -> None:
		"""Check and change send data button enabled state."""
		self.ui.actionCommunication_Send_Data.setEnabled(True)
		if self.transmission_settings['continuosly_data_transmission']:
			self.ui.actionCommunication_Send_Data.setEnabled(False)

	def serial_communication(self) -> None:
		"""Function for future serial comunication."""
		pass

	def log(self, log: str) -> None:
		"""Write text in console."""
		self.ui.console_plain.appendPlainText(log)
