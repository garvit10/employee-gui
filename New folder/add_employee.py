import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate


class MySQLDatabase:
    def __init__(self):
        self.database_name = 'emoloyeedb'
        self.table_name = 'employee'
        self.column_names = "emp_id, name, address, phone, dob, department_id, salary_id"
        self.connect()

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="piyush007Q#!",
            database=self.database_name
        )
        print("Connected to MySQL Database")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from MySQL Database")

    def insert_employee(self, emp_id, name, address, phone, dob, department_id, salary_id):
        cursor = self.connection.cursor()
        query = f"INSERT INTO {self.table_name} ({self.column_names}) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (emp_id, name, address, phone, dob, department_id, salary_id)
        cursor.execute(query, values)
        self.connection.commit()
        
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 443)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(191, 370, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_employee)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 82, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 160, 131, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 160, 111, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 122, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 120, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 198, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 200, 91, 20))
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(230, 240, 111, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 240, 41, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 282, 101, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 280, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 318, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(114, 320, 71, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 20, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ADD EMPLOYEE"))
        self.label.setText(_translate("MainWindow", "EmpID"))
        self.label_2.setText(_translate("MainWindow", "Address(STATE ONLY)"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "PHONE NUMBER"))
        self.label_5.setText(_translate("MainWindow", "DOB"))
        self.label_6.setText(_translate("MainWindow", "DEPARTMENT ID"))
        self.label_7.setText(_translate("MainWindow", "SALARY_ID"))
        self.label_8.setText(_translate("MainWindow", "ADD A NEW EMPLOYEE"))

    def add_employee(self):
    
        emp_id = self.lineEdit.text()
        name = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()
        address = self.lineEdit_2.text()
        dob = self.dateEdit.date().toString("yyyy-MM-dd")
        department_id = self.lineEdit_5.text()
        salary_id = self.lineEdit_6.text()
        
        widget = QtWidgets.QWidget()
        if emp_id == "" or name == "" or phone == "" or address == "" or dob == "" or department_id == "" or salary_id == "":
            QMessageBox.warning(widget, "Error", "All fields are required.")
            return
        if not phone.isdigit():
            
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Phone number must be an integer.")
            msg.exec_()
            return
        try:
            int(emp_id)
            int(department_id)
            int(salary_id)
        except ValueError:
            QMessageBox.warning(widget, "Error", "Employee ID, Department ID and Salary ID must be integers.")
            return

        
        db = MySQLDatabase()
        db.insert_employee(emp_id, name, address, phone, dob, department_id, salary_id)

        
        QMessageBox.information(widget, "Success", "Employee added successfully.")
        
        
        self.lineEdit.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_2.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.dateEdit.setDate(QDate.currentDate())

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
