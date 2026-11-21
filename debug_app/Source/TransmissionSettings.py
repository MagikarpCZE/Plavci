#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySide6
from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtGui import QIntValidator
from Source.__windows.transmission_settings import Ui_Dialog

class TransmissionSettings(QDialog):
	"""The Transmission settings window."""
	def __init__(self, settings: dict) -> None:
		"""Class initialization."""
		super(TransmissionSettings, self).__init__()

		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.inicialize_ui(settings)

	def inicialize_ui(self, settings: dict) -> None:
		"""Initialize the basic functions and settings of the window."""
		self.ui.transmission_rate.setEnabled(False)	

		self.ui.save_button.clicked.connect(self.save_settings)
		self.ui.send_data_continuosly.stateChanged.connect(self.send_data_continuosly_state_changed)
		self.ui.transmission_rate.setValidator(QIntValidator(1, 2147483647, self))

		self.fill_combobox_with_com_ports()
		self.set_settings(settings)

	def get_parameters(self) -> dict[str: bool, str]:
		"""Return local settings to main window."""
		return {
			'continuosly_data_transmission': self.ui.send_data_continuosly.isChecked() == 1,
			'transmission_rate': self.ui.transmission_rate.text() or 1,
			'port': f'COM{self.ui.cmb_port.currentIndex() + 1}'
		}

	def send_data_continuosly_state_changed(self) -> dict:
		"""Handle continuosly data transmitting checkbox state changing."""
		self.ui.transmission_rate.setEnabled(False)	
		if self.ui.send_data_continuosly.isChecked():
			self.ui.transmission_rate.setEnabled(True)

	def fill_combobox_with_com_ports(self) -> dict:
		"""Fill combobox with COMx text."""
		self.ui.cmb_port.clear()
		for i in range(1, 11):
			self.ui.cmb_port.addItem(f'COM{i}', f'COM{i}')

	def save_settings(self) -> None:
		"""Save local settings."""
		if self.ui.send_data_continuosly.isChecked() and self.ui.transmission_rate.text() != '' and int(self.ui.transmission_rate.text()) > 0:
			self.accept()

		elif not(self.ui.send_data_continuosly.isChecked()):
			self.accept()

	def set_settings(self, settings: dict) -> None:
		"""Set actual settings of program."""
		self.ui.send_data_continuosly.setChecked(settings['continuosly_data_transmission'])
		if self.ui.send_data_continuosly.isChecked():
			self.ui.transmission_rate.setText(settings['transmission_rate'])

		port = int(settings['port'].replace('COM', ''))-1
		self.ui.cmb_port.setCurrentIndex(port)