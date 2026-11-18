#!/usr/bin/env python3`
# -*- coding: utf-8 -*-

import os
import sys
import PySide6
from PySide6.QtWidgets import QApplication
from PySide6 import QtGui
import Source.MainWindow as MainWindow

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('icon.ico'))

	window = MainWindow.MainWindow(app)
	window.show()

	sys.exit(app.exec())