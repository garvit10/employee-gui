import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 240, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_department)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 140, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 142, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 180, 111, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(42, 20, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 100, 101, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 100, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 180, 81, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ADD DEPARTMENT"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_8.setText(_translate("MainWindow", "ADD A NEW DEPARTMENT"))
        self.label.setText(_translate("MainWindow", "DEPARTMENT ID"))
        self.label_2.setText(_translate("MainWindow", "DESCRIPTION"))
    def add_department(self):
    # retrieve the data from the text boxes
        id = self.lineEdit.text()
        name = self.lineEdit_3.text()
        description = self.lineEdit_2.text()
        
        # validate the data
        if not id or not name:
            msg = QMessageBox()
            msg.setWindowTitle("Validation Error")
            msg.setText("Department ID and Name cannot be empty.")
            msg.exec_()
            return

        # check if the department already exists
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="piyush007Q#!",
            database="emoloyeedb"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM departments WHERE id = %s"
        cursor.execute(query, (id,))
        existing_department = cursor.fetchone()
        if existing_department:
            msg = QMessageBox()
            msg.setWindowTitle("Validation Error")
            msg.setText("Department ID {} already exists.".format(id))
            msg.exec_()
            return
        if not id.isdigit():
            
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Department ID must be an integer.")
            msg.exec_()
            return
        # add the department to the database
        query = "INSERT INTO departments (id, name, description) VALUES (%s, %s, %s)"
        values = (id, name, description)
        cursor.execute(query, values)
        connection.commit()

        # display a message box to confirm that the department was added
        msg = QMessageBox()
        msg.setWindowTitle("Department Added")
        msg.setText("Department {} has been added".format(name))
        msg.exec_()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
