
import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 320, 201, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update_salary)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(139, 193, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 30, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(250, 270, 111, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 230, 111, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 190, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 270, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 230, 101, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 98, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 100, 55, 16))
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 150, 151, 16))
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
        self.pushButton.setText(_translate("MainWindow", "UPDATE SALARY DETAILS"))
        self.label_3.setText(_translate("MainWindow", "Employee_ID"))
        self.label_8.setText(_translate("MainWindow", "UPDATE SALARY DETAILS"))
        self.label_5.setText(_translate("MainWindow", "salary_date"))
        self.label_2.setText(_translate("MainWindow", "SALARY AMOUNT"))
        self.label.setText(_translate("MainWindow", "Salary ID"))
        self.label_7.setText(_translate("MainWindow", "ENTER THE NEW DETAILS"))

    def update_salary(self):
        # get the user input from the UI
        id = ui.lineEdit.text()
        salary_amount = ui.lineEdit_2.text()
        employee_id = ui.lineEdit_3.text()
        salary_date = ui.dateEdit.date().toString("yyyy-MM-dd")
        
        # Check if all fields are filled
        if not id or not salary_amount or not employee_id:
            QtWidgets.QMessageBox.warning(None, "Error", "Please fill all fields.")
            return
        
        try:
            id = int(id)
            salary_amount = int(salary_amount)
            employee_id = int(employee_id)
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Error", "Invalid input.")
            return
        
        conn = mysql.connector.connect(user='root', password='piyush007Q#!', host='localhost', database='emoloyeedb')
        cursor = conn.cursor()
        
        # Check if employee exists in the employee table
        cursor.execute("SELECT * FROM employee WHERE emp_id = %s", (employee_id,))
        data = cursor.fetchone()
        if data is None:
            QtWidgets.QMessageBox.warning(None, "Error", "Employee ID not found in the database.")
            return

        # check if the salary ID exists in the database
        cursor.execute("SELECT * FROM salary WHERE id = %s", (id,))
        data = cursor.fetchone()
        if data is None:
            QtWidgets.QMessageBox.warning(None, "Error", "Salary ID not found in the database.")
            return

        # update the salary record in the database
        cursor.execute("UPDATE salary SET Salary_Amount = %s, Employee_ID = %s, Salary_Date = %s WHERE id = %s",
                    (salary_amount, employee_id, salary_date, id))
        conn.commit()

        # show a success message to the user
        QtWidgets.QMessageBox.information(None, "Success", "Salary details updated successfully.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
