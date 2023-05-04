import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 230, 91, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 400, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update_employee)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 150, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 152, 55, 16))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(310, 270, 111, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 190, 111, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 228, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 348, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 270, 41, 20))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 10, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 72, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 70, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 190, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 312, 101, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 310, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 350, 71, 20))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 110, 151, 16))
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
        self.label_4.setText(_translate("MainWindow", "PHONE NUMBER"))
        self.pushButton.setText(_translate("MainWindow", "UPDATE EMPLOYEE"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "DOB"))
        self.label_8.setText(_translate("MainWindow", "UPDATE AN EXISTING  EMPLOYEE"))
        self.label.setText(_translate("MainWindow", "EmpID"))
        self.label_2.setText(_translate("MainWindow", "Address(STATE ONLY)"))
        self.label_6.setText(_translate("MainWindow", "DEPARTMENT ID"))
        self.label_9.setText(_translate("MainWindow", "SALARY_ID"))
        self.label_7.setText(_translate("MainWindow", "ENTER THE NEW DETAILS"))
    
    def update_employee(self):
        
        emp_id = self.lineEdit.text()
        name = self.lineEdit_3.text()
        address = self.lineEdit_2.text()
        phone = self.lineEdit_4.text()
        dob = self.dateEdit.date().toString("yyyy-MM-dd")
        department_id = self.lineEdit_5.text()
        salary_id = self.lineEdit_6.text()
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="piyush007Q#!",
            database="emoloyeedb"
        )
        
        cursor = connection.cursor()
        query = "SELECT emp_id FROM employee WHERE emp_id=%s"
        values = (emp_id,)
        cursor.execute(query, values)
        employee = cursor.fetchone()
        if employee is None:
            
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Employee with ID {} does not exist in the database".format(emp_id))
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
            
        if not all([emp_id, name, address, phone, dob, department_id, salary_id]):
             
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Please fill in all fields.")
                msg.exec_()
                return

        if not emp_id.isdigit():
            
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Employee ID must be an integer.")
            msg.exec_()
            return

        if not phone.isdigit():
            
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Phone number must be an integer.")
            msg.exec_()
            return

        if not department_id.isdigit():
            
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Department ID must be an integer.")
            msg.exec_()
            return

        if not salary_id.isdigit():
            
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Salary ID must be an integer.")
            msg.exec_()
            return

        
        
        query = "UPDATE employee SET name=%s, address=%s, phone=%s, dob=%s, department_id=%s, salary_id=%s WHERE emp_id=%s"
        values = (name, address, phone, dob, department_id, salary_id, emp_id)
        cursor.execute(query, values)
        connection.commit()

        
        msg = QMessageBox()
        msg.setWindowTitle("Employee Updated")
        msg.setText("Employee {} has been updated".format(emp_id))
        self.lineEdit.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_2.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
