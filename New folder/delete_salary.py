
import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 221)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(226, 108, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(99, 109, 91, 20))
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 30, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 160, 161, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.delete_salary)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SALARY ID"))
        self.label_8.setText(_translate("MainWindow", "DELETE SALARY DETAIL"))
        self.pushButton.setText(_translate("MainWindow", "DELETE SALARY DETAILS"))

    def delete_salary(self):
        salary_id = self.lineEdit.text()

        if not salary_id:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Please enter a salary ID.')
            return

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='piyush007Q#!',
            database='emoloyeedb'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM salary WHERE id = %s", (salary_id,))
        data = cursor.fetchone()
        if data is None:
            QtWidgets.QMessageBox.warning(None, "Error", "Salary_id not found in the database.")
            return
        
        

        try:
            cursor.execute("DELETE FROM salary WHERE id = %s", (salary_id,))
            connection.commit()
            QtWidgets.QMessageBox.information(self.centralwidget, 'Success', 'Salary details deleted successfully.')
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.critical(self.centralwidget, 'Error', f"Error while deleting salary details: {error}")
        finally:
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
