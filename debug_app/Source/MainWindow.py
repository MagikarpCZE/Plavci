#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
import pandas
import PySide6
from typing import Any
from PySide6 import QtCharts, QtCore
from PySide6.QtCharts import QChartView
from PySide6.QtCore import QMargins, Qt
from PySide6.QtGui import QFont, QBrush, QColor, QPainter
from PySide6.QtWidgets import (QMainWindow, QTreeWidgetItem, 
							   QMessageBox, QToolTip, QFileDialog, QApplication)
from Source.__windows.main_window import Ui_MainWindow

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
		print('Add new motor')

	def delete_button_clicked(self) -> None:
		"""Delet last motor."""
		print('Delete motor')