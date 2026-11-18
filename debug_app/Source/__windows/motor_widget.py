# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'motor_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_MotorWidget(object):
    def setupUi(self, MotorWidget):
        if not MotorWidget.objectName():
            MotorWidget.setObjectName(u"MotorWidget")
        MotorWidget.resize(115, 107)
        self.gridLayout = QGridLayout(MotorWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.motor_spinbox = QSpinBox(MotorWidget)
        self.motor_spinbox.setObjectName(u"motor_spinbox")
        self.motor_spinbox.setMaximum(100)

        self.gridLayout.addWidget(self.motor_spinbox, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.motor_label = QLabel(MotorWidget)
        self.motor_label.setObjectName(u"motor_label")

        self.gridLayout.addWidget(self.motor_label, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(MotorWidget)

        QMetaObject.connectSlotsByName(MotorWidget)
    # setupUi

    def retranslateUi(self, MotorWidget):
        MotorWidget.setWindowTitle(QCoreApplication.translate("MotorWidget", u"Motor Settings", None))
        self.motor_spinbox.setSuffix(QCoreApplication.translate("MotorWidget", u"%", None))
        self.motor_label.setText(QCoreApplication.translate("MotorWidget", u"Motor", None))
    # retranslateUi

