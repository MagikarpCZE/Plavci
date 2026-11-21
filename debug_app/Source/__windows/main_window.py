# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        self.actionTransmission_Settings = QAction(MainWindow)
        self.actionTransmission_Settings.setObjectName(u"actionTransmission_Settings")
        self.actionCommunication_Send_Data = QAction(MainWindow)
        self.actionCommunication_Send_Data.setObjectName(u"actionCommunication_Send_Data")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.console_plain = QPlainTextEdit(self.centralwidget)
        self.console_plain.setObjectName(u"console_plain")
        self.console_plain.setReadOnly(True)

        self.gridLayout.addWidget(self.console_plain, 0, 1, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add_motor = QPushButton(self.centralwidget)
        self.btn_add_motor.setObjectName(u"btn_add_motor")

        self.horizontalLayout.addWidget(self.btn_add_motor)

        self.btn_delete_motor = QPushButton(self.centralwidget)
        self.btn_delete_motor.setObjectName(u"btn_delete_motor")

        self.horizontalLayout.addWidget(self.btn_delete_motor)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.motors_container = QScrollArea(self.centralwidget)
        self.motors_container.setObjectName(u"motors_container")
        self.motors_container.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 285, 503))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.widget)

        self.motors_container.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.motors_container, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.actionTransmission_Settings)
        self.menuMain.addAction(self.actionCommunication_Send_Data)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionTransmission_Settings.setText(QCoreApplication.translate("MainWindow", u"Signal Transmission Settings", None))
        self.actionCommunication_Send_Data.setText(QCoreApplication.translate("MainWindow", u"Send Data", None))
        self.btn_add_motor.setText(QCoreApplication.translate("MainWindow", u"Add Motor", None))
        self.btn_delete_motor.setText(QCoreApplication.translate("MainWindow", u"Delete Motor", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"Communication", None))
    # retranslateUi

