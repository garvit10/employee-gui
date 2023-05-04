
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 206)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 88, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 30, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 90, 55, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.delete_employee)
        self.pushButton.setGeometry(QtCore.QRect(210, 140, 151, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "DELETE AN EXISTING  EMPLOYEE"))
        self.label.setText(_translate("MainWindow", "EmpID"))
        self.pushButton.setText(_translate("MainWindow", "DELETE EMPLOYEE"))

    def delete_employee(self):
        widget = QtWidgets.QWidget()
        emp_id = self.lineEdit.text()
        
        # validate that the employee ID is not empty and is a valid integer
        if not emp_id:
            QMessageBox.warning(widget, "Empty Field", "Please enter an Employee ID")
            return
        try:
            emp_id = int(emp_id)
        except ValueError:
            QMessageBox.warning(widget, "Invalid Employee ID", "Please enter a valid Employee ID")
            return
        
        # check if the employee exists in the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="piyush007Q#!",
            database="emoloyeedb"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM employee WHERE emp_id = %s"
        values = (emp_id,)
        cursor.execute(query, values)
        employee = cursor.fetchone()
        
        if not employee:
            QMessageBox.warning(widget, "Employee Not Found", "The specified Employee ID does not exist in the database")
            return
        
        # if the employee exists, delete it from the database
        query = "DELETE FROM employee WHERE emp_id = %s"
        cursor.execute(query, values)
        connection.commit()
        
        # display a message box to confirm that the employee was deleted
        QMessageBox.information(widget, "Employee Deleted", "Employee {} has been deleted".format(emp_id))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
