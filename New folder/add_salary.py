
import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 260, 161, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.add_salary)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 130, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(139, 133, 81, 20))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(250, 210, 111, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 170, 111, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 210, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 20, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 92, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 90, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 101, 21))
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
        self.pushButton.setText(_translate("MainWindow", "ADD SALARY DETAILS"))
        self.label_3.setText(_translate("MainWindow", "Employee_ID"))
        self.label_5.setText(_translate("MainWindow", "salary_date"))
        self.label_8.setText(_translate("MainWindow", "ADD NEW SALARY DETAILS"))
        self.label.setText(_translate("MainWindow", "Salary ID"))
        self.label_2.setText(_translate("MainWindow", "SALARY AMOUNT"))

    def add_salary(self):
        # Get values from line edits
        id = self.lineEdit.text()
        employee_id = self.lineEdit_3.text()
        salary_amount = self.lineEdit_2.text()
        salary_date = self.dateEdit.date().toString("yyyy-MM-dd")

        # Data validation
        if not id.isnumeric():
            QtWidgets.QMessageBox.warning(self.centralwidget, "Invalid Salary ID", "Please enter a valid salary ID (numeric).")
            return
        if not employee_id.isnumeric():
            QtWidgets.QMessageBox.warning(self.centralwidget, "Invalid Employee ID", "Please enter a valid employee ID (numeric).")
            return
        if not salary_amount.isnumeric():
            QtWidgets.QMessageBox.warning(self.centralwidget, "Invalid Salary Amount", "Please enter a valid salary amount (numeric).")
            return

        # Check if salary ID already exists
        conn = mysql.connector.connect(user='root', password='piyush007Q#!', host='localhost', database='emoloyeedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salary WHERE id = %s", (id,))
        if cursor.fetchone():
            QtWidgets.QMessageBox.warning(self.centralwidget, "Salary ID already exists", "Please enter a unique salary ID.")
            cursor.close()
            conn.close()
            return

        # Check if employee ID exists in employee table
        cursor.execute("SELECT * FROM employee WHERE emp_id = %s", (employee_id,))
        if not cursor.fetchone():
            QtWidgets.QMessageBox.warning(self.centralwidget, "Employee ID not found", "Please enter a valid employee ID.")
            cursor.close()
            conn.close()
            return

        # Add salary to database
        try:
            cursor.execute("INSERT INTO salary (id, employee_id, salary_amount, salary_date) VALUES (%s, %s, %s, %s)", (id, employee_id, salary_amount, salary_date))
            conn.commit()
            QtWidgets.QMessageBox.information(self.centralwidget, "Salary added successfully", "Salary details added successfully.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error adding salary details", f"An error occurred while adding salary details:\n{str(e)}")
        finally:
            cursor.close()
            conn.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
