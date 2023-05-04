
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from add_employee import Ui_MainWindow as AddEmployeeWindow
from update_employee import Ui_MainWindow as UpdateEmployeeWindow
from delete_employee import Ui_MainWindow as DeleteEmployeeWindow
from add_department import Ui_MainWindow as AddDepartmentWindow
from update_department import Ui_MainWindow as UpdateDepartmentWindow
from delete_department import Ui_MainWindow as DeleteDepartmentWindow
from add_salary import Ui_MainWindow as AddSalaryWindow
from update_salary import Ui_MainWindow as UpdatesalaryWindow
from delete_salary import Ui_MainWindow as DeleteSalaryWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 784)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 360, 1201, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 200, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 150, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 200, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 100, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1080, 150, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1080, 200, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1080, 100, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(13, 50, 131, 151))
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(210, 70, 221, 121))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(480, 0, 20, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 50, 71, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 50, 51, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(830, 50, 81, 41))
        self.label_3.setObjectName("label_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(520, 250, 211, 61))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(760, 250, 211, 61))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(1000, 250, 211, 61))
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setObjectName("pushButton_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton.clicked.connect(self.show_add_department_window)
        self.pushButton_2.setText(_translate("MainWindow", "UPDATE"))
        self.pushButton_2.clicked.connect(self.show_update_department_window)
        self.pushButton_3.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_3.clicked.connect(self.show_delete_department_window)
        self.pushButton_4.setText(_translate("MainWindow", "UPDATE"))
        self.pushButton_4.clicked.connect(self.show_update_employee_window)
        self.pushButton_5.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_5.clicked.connect(self.show_delete_employee_window)
        self.pushButton_6.setText(_translate("MainWindow", "ADD"))
        self.pushButton_6.clicked.connect(self.show_add_employee_window)
        self.pushButton_7.setText(_translate("MainWindow", "UPDATE"))
        self.pushButton_7.clicked.connect(self.show_update_Salary_window)
        self.pushButton_8.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_8.clicked.connect(self.show_delete_Salary_window)
        self.pushButton_9.setText(_translate("MainWindow", "ADD"))
        self.pushButton_9.clicked.connect(self.show_add_Salary_window)
        self.label.setText(_translate("MainWindow", "EMPLOYEE"))
        self.label_2.setText(_translate("MainWindow", "SALARY"))
        self.label_3.setText(_translate("MainWindow", "DEPARTMENT"))
        self.pushButton_10.setText(_translate("MainWindow", "SHOW ALL / UPDATE"))
        self.pushButton_11.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_12.setText(_translate("MainWindow", "GENERATE A PAYMENT SLIP"))

    def show_add_employee_window(self):
        self.add_employee_window = QtWidgets.QMainWindow()
        self.ui_add_employee = AddEmployeeWindow()
        self.ui_add_employee.setupUi(self.add_employee_window)
        self.add_employee_window.show()

    def show_update_employee_window(self):
        self.update_employee_window = QtWidgets.QMainWindow()
        self.ui_update_employee = UpdateEmployeeWindow()
        self.ui_update_employee.setupUi(self.update_employee_window)
        self.update_employee_window.show()

    def show_delete_employee_window(self):
        self.delete_employee_window = QtWidgets.QMainWindow()
        self.ui_delete_employee = DeleteEmployeeWindow()
        self.ui_delete_employee.setupUi(self.delete_employee_window)
        self.delete_employee_window.show()


    def show_add_department_window(self):
        self.add_Department_window = QtWidgets.QMainWindow()
        self.ui_add_Department = AddDepartmentWindow()
        self.ui_add_Department.setupUi(self.add_Department_window)
        self.add_Department_window.show()

    def show_update_department_window(self):
        self.update_Department_window = QtWidgets.QMainWindow()
        self.ui_update_Department = UpdateDepartmentWindow()
        self.ui_update_Department.setupUi(self.update_Department_window)
        self.update_Department_window.show()

    def show_delete_department_window(self):
        self.delete_department_window = QtWidgets.QMainWindow()
        self.ui_delete_Department = DeleteDepartmentWindow()
        self.ui_delete_Department.setupUi(self.delete_department_window)
        self.delete_department_window.show()
        
    def show_add_Salary_window(self):
        self.add_Salary_window = QtWidgets.QMainWindow()
        self.ui_add_Salary = AddSalaryWindow()
        self.ui_add_Salary.setupUi(self.add_Salary_window)
        self.add_Salary_window.show()

    def show_update_Salary_window(self):
        self.update_Salary_window = QtWidgets.QMainWindow()
        self.ui_update_Salary = UpdatesalaryWindow()
        self.ui_update_Salary.setupUi(self.update_Salary_window)
        self.update_Salary_window.show()

    def show_delete_Salary_window(self):
        self.delete_Salary_window = QtWidgets.QMainWindow()
        self.ui_delete_Salary = DeleteSalaryWindow()
        self.ui_delete_Salary.setupUi(self.delete_Salary_window)
        self.delete_Salary_window.show()
    
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
