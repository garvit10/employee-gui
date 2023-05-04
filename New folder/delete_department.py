import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 211)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.delete_department)
        self.pushButton.setGeometry(QtCore.QRect(131, 150, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(217, 98, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(51, 30, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(81, 100, 91, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "DELETE DEPARTMENT"))
        self.label_8.setText(_translate("MainWindow", "DELETE DEPARTMENT"))
        self.label.setText(_translate("MainWindow", "Department ID"))

    def delete_department(self):
        # Get the department ID from the line edit
        id = self.lineEdit.text()

        # Open a connection to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="piyush007Q#!",
            database="emoloyeedb"
        )

        # Create a cursor object
        mycursor = mydb.cursor()

        # Execute the SQL DELETE statement
        mycursor.execute("DELETE FROM departments WHERE id = %s", (id,))

        # Check how many rows were affected
        num_rows_deleted = mycursor.rowcount

        # Commit the changes to the database
        mydb.commit()

        # Close the cursor and database connection
        mycursor.close()
        mydb.close()

        # Show a message box to inform the user
        if num_rows_deleted == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Department ID not found.")
            msg.setWindowTitle("Error")
            msg.exec_()
            self.lineEdit.clear()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"DELTED")
            msg.setWindowTitle("Success")
            msg.exec_()
            self.lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
