
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200 ,1080, 720)
    win.setWindowTitle("Test Run")

    label = QtWidgets.QLabel(win)
    label.setText("Hello World")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec())



window()
"""
from PyQt5 import QtCore, QtGui, QtWidgets

from typing import List
from weighted_assignment import weighted_assignment
from Points_assignment import points_assignment





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 562) #1023
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1023, 562))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(290, 90, 471, 335))  #adjust size of the table
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.GradCalcLabel = QtWidgets.QLabel(self.splitter)    
        self.GradCalcLabel.setObjectName("GradCalcLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(151)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.addColumn = QtWidgets.QPushButton(self.splitter)
        self.addColumn.setObjectName("addColumn")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(890, 400, 112, 101))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1023, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave_2)
        self.menuBar.addAction(self.menuFile.menuAction())
        
        self.delete_row = QtWidgets.QPushButton(self.splitter)
        self.delete_row.setObjectName("deleteColumn")
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addColumn.clicked.connect(self.added_column)
        self.delete_row.clicked.connect(self.deleted_row)
        
        



        self.pushButton_2.clicked.connect(self.calculate_overall_grade)


        #self.tableWidget.cellChanged.connect(self.get_row)
      
        

        #self.tableWidget.cellChanged.connect(self.cell_access) #sets up a way to get user data 
        #self.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("100")) #sets up a way to output data to GUI

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GradCalcLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Grade Calculator</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Points Earned"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Points Total"))
        self.addColumn.setText(_translate("MainWindow", "Add Column"))
        self.delete_row.setText(_translate("MainWindow", "Delete Column"))
        
        

        self.label.setText(_translate("MainWindow", "Overall Grade"))
        self.pushButton_2.setText(_translate("MainWindow", "Click to calculate"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionSave_2.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave_2.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def get_row(self,row,column):
        cell_content = self.tableWidget.item(row,column)
        
        if cell_content:
            print(f"Content on cell: {cell_content.text()}")
            #print(f"({row}, {column}) is currently selected")


    """
    def cell_access(self):
        cell_content = self.tableWidget.itemAt(self.tableWidget.rowCount() - 1,)
        if cell_content:
            print(cell_content.text())
    """


    def added_column(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem("0"))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem("0"))

    def deleted_row(self):
        rowPosition = self.tableWidget.rowCount() - 1
        self.tableWidget.removeRow(rowPosition)


    def calculate_overall_grade(self):
        points_earned = 0
        points_total = 0
        for x in range(self.tableWidget.rowCount()):
            cell_content_earned = self.tableWidget.item(x,1)
            cell_content_total = self.tableWidget.item(x,2)

            if ((len(cell_content_earned.text()) > 0) and (len(cell_content_total.text()) > 0)):
                points_earned = points_earned + float(cell_content_earned.text())
                points_total = points_total + float(cell_content_total.text())   


  
                
        
        overall = (points_earned / points_total) * 100
        overall = round(overall,2)

        self.lcdNumber.display(overall)


        
    

    

        


if __name__ == "__main__":

    def calc_weighted_grade(list_of_weighted_asms: List[weighted_assignment]):
        score = 0
        for asm in list_of_weighted_asms:
            score += asm.calc_weight_grade()
        return score
    
    def calc_points_grade(list_of_points_asms: List[points_assignment]):
        score = 0
        tot_points_earned = 0
        tot_points_total = 0
        for asm in list_of_points_asms:
            tot_points_earned += asm.get_points_earned()
            tot_points_total += asm.get_points_total()

        score = (tot_points_earned / tot_points_total) * 100
        return score
    
    def add_assignment_points(list_of_asm: List, name, points_earned, points_total):  # Man
        asm = points_assignment(name, points_earned, points_total)
        list_of_asm.append(asm)
        print("Added Successfully")
        return True
    
    def remove_assignment(list_of_asm: List, name):  # Man
        for asm in list_of_asm:
            if(asm.get_name() == name):
                list_of_asm.remove(asm)
                return True
        print("Assignment not found.")
        return False
    
    def overall_grade_assignment(list_of_asm: List, asm_type):  # Man
        if (asm_type == 'W'):
            print(f"{calc_weighted_grade(list_of_asm): .2f}%")
            return True
        elif (asm_type == 'P'):
            print(f"{calc_points_grade(list_of_asm): .2f}%")
            return True
        else:
            return False
    
    import sys
    #asm_type = input("W or P\n")

    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    #stylesheet = "QWidget {background-color: qlineargradient(x1: 0, x2: 1, stop: 0 lightgray, stop: 1 lightgray)}"
    MainWindow.setStyleSheet("background-color: lightgray;")
    
        
    MainWindow.show()       
    sys.exit(app.exec_()) 
        
           
        


    
    
    

    