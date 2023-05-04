import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 150, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 152, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 20, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 190, 81, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 190, 111, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update_department)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 101, 20))
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 120, 151, 16))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_8.setText(_translate("MainWindow", "UPDATE DEPARTMENT"))
        self.label_2.setText(_translate("MainWindow", "DESCRIPTION"))
        self.pushButton.setText(_translate("MainWindow", "UPDATE"))
        self.label.setText(_translate("MainWindow", "DEPARTMENT ID"))
        self.label_7.setText(_translate("MainWindow", "ENTER THE NEW DETAILS"))

    def update_department(self):
        id = self.lineEdit.text()
        name = self.lineEdit_3.text()
        description = self.lineEdit_2.text()

        if not id.isdigit():
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Department ID should be a number")
            return

        if not name or not description:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Please enter department name and description")
            return

        id = int(id)

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="piyush007Q#!",
            database="emoloyeedb"
        )

        cursor = connection.cursor()
        query = "UPDATE departments SET name = %s, description = %s WHERE id = %s"
        values = (name, description, id)
        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount == 0:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", f"Department ID {id} does not exist")
        else:
            QtWidgets.QMessageBox.information(self.centralwidget, "Success", f"Department {id} updated successfully")
        
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        cursor.close()
        connection.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
