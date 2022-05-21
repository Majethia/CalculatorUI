from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Number_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_1.setGeometry(QtCore.QRect(0, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_1.setFont(font)
        self.Number_1.setObjectName("Number_1")
        self.Number_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_2.setGeometry(QtCore.QRect(100, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_2.setFont(font)
        self.Number_2.setObjectName("Number_2")
        self.Number_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_3.setGeometry(QtCore.QRect(200, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_3.setFont(font)
        self.Number_3.setObjectName("Number_3")
        self.Number_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_4.setGeometry(QtCore.QRect(0, 150, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_4.setFont(font)
        self.Number_4.setObjectName("Number_4")
        self.Number_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_5.setGeometry(QtCore.QRect(100, 150, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_5.setFont(font)
        self.Number_5.setObjectName("Number_5")
        self.Number_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_6.setGeometry(QtCore.QRect(200, 150, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_6.setFont(font)
        self.Number_6.setObjectName("Number_6")
        self.Number_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_7.setGeometry(QtCore.QRect(0, 250, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_7.setFont(font)
        self.Number_7.setObjectName("Number_7")
        self.Number_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_8.setGeometry(QtCore.QRect(100, 250, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_8.setFont(font)
        self.Number_8.setObjectName("Number_8")
        self.Number_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_9.setGeometry(QtCore.QRect(200, 250, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_9.setFont(font)
        self.Number_9.setObjectName("Number_9")
        self.Number_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_0.setGeometry(QtCore.QRect(0, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_0.setFont(font)
        self.Number_0.setObjectName("Number_0")
        self.Number_00 = QtWidgets.QPushButton(self.centralwidget)
        self.Number_00.setGeometry(QtCore.QRect(100, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Number_00.setFont(font)
        self.Number_00.setObjectName("Number_00")
        self.Dot = QtWidgets.QPushButton(self.centralwidget)
        self.Dot.setGeometry(QtCore.QRect(200, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Dot.setFont(font)
        self.Dot.setObjectName("Dot")
        self.Divide = QtWidgets.QPushButton(self.centralwidget)
        self.Divide.setGeometry(QtCore.QRect(300, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Divide.setFont(font)
        self.Divide.setObjectName("Divide")
        self.Multiply = QtWidgets.QPushButton(self.centralwidget)
        self.Multiply.setGeometry(QtCore.QRect(300, 150, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Multiply.setFont(font)
        self.Multiply.setObjectName("Multiply")
        self.Subtract = QtWidgets.QPushButton(self.centralwidget)
        self.Subtract.setGeometry(QtCore.QRect(300, 250, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Subtract.setFont(font)
        self.Subtract.setObjectName("Subtract")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(300, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Add.setFont(font)
        self.Add.setObjectName("Add")
        self.Button_Back = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Back.setGeometry(QtCore.QRect(400, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_Back.setFont(font)
        self.Button_Back.setObjectName("Button_Back")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(400, 150, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.Equals = QtWidgets.QPushButton(self.centralwidget)
        self.Equals.setGeometry(QtCore.QRect(400, 250, 100, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Equals.setFont(font)
        self.Equals.setObjectName("Equals")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", ""))
        self.Number_1.setText(_translate("MainWindow", "1"))
        self.Number_2.setText(_translate("MainWindow", "2"))
        self.Number_3.setText(_translate("MainWindow", "3"))
        self.Number_4.setText(_translate("MainWindow", "4"))
        self.Number_5.setText(_translate("MainWindow", "5"))
        self.Number_6.setText(_translate("MainWindow", "6"))
        self.Number_7.setText(_translate("MainWindow", "7"))
        self.Number_8.setText(_translate("MainWindow", "8"))
        self.Number_9.setText(_translate("MainWindow", "9"))
        self.Number_0.setText(_translate("MainWindow", "0"))
        self.Number_00.setText(_translate("MainWindow", "(-)"))
        self.Dot.setText(_translate("MainWindow", "."))
        self.Divide.setText(_translate("MainWindow", "/"))
        self.Multiply.setText(_translate("MainWindow", "*"))
        self.Subtract.setText(_translate("MainWindow", "-"))
        self.Add.setText(_translate("MainWindow", "+"))
        self.Button_Back.setText(_translate("MainWindow", "Back"))
        self.Clear.setText(_translate("MainWindow", "AC"))
        self.Equals.setText(_translate("MainWindow", "="))


        self.Number_1.clicked.connect(lambda: self.nums(1))
        self.Number_2.clicked.connect(lambda: self.nums(2))
        self.Number_3.clicked.connect(lambda: self.nums(3))
        self.Number_4.clicked.connect(lambda: self.nums(4))
        self.Number_5.clicked.connect(lambda: self.nums(5))
        self.Number_6.clicked.connect(lambda: self.nums(6))
        self.Number_7.clicked.connect(lambda: self.nums(7))
        self.Number_8.clicked.connect(lambda: self.nums(8))
        self.Number_9.clicked.connect(lambda: self.nums(9))
        self.Number_0.clicked.connect(lambda: self.nums(0))
        self.Number_00.clicked.connect(self.negative_sign)
        self.Add.clicked.connect(lambda: self.Opperation('+'))
        self.Subtract.clicked.connect(lambda: self.Opperation('-'))
        self.Multiply.clicked.connect(lambda: self.Opperation('*'))
        self.Divide.clicked.connect(lambda: self.Opperation('/'))
        self.Equals.clicked.connect(self.equals)
        self.Dot.clicked.connect(self.dot)
        self.Button_Back.clicked.connect(self.back)
        self.Clear.clicked.connect(self.clear)

    def negative_sign(self):
        currentnum = self.label.text()
        if currentnum == '' :
            self.label.setText(f'-')
        
        elif currentnum.endswith(' '):
            self.label.setText(f'{currentnum}-')

        else:
            pass

    def clear(self):
        self.label.setText('')

    def back(self):
        try:
            currentnum = self.label.text()
            newnum = currentnum[:-1]
            self.label.setText(newnum)
        
        except:
            pass
        
        if newnum.endswith(' '):
            newnum = newnum[:-1]
            self.label.setText(newnum)

    def nums(self, x):
        try:
            currentnum = self.label.text()
            if currentnum == 'Enter a number first':
                currentnum = ''
            
            elif currentnum == 'WTF is this':
                currentnum = ''

            elif currentnum == 'Cant Divide by 0 Dumbass':
                currentnum = ''

        except:
            currentnum = ''

        newnum = self.label.setText(f"{currentnum}{x}")
        currentnum = newnum

    def Opperation(self, operation):
        firstnum = self.label.text()

        if '*' in firstnum:
            return

        elif '/' in firstnum:
            return

        elif ' - ' in firstnum:
            return

        elif '+' in firstnum:
            return

        if firstnum == '':
            self.label.setText('Enter a number first')

        elif 'Enter a number first' in firstnum:
            pass
        
        elif 'WTF is this' in firstnum:
            pass

        elif 'Cant Divide by 0 Dumbass' in firstnum:
            pass
            
        else:
            self.label.setText(f'{firstnum} {operation} ')
    
    def equals(self):
        equation = self.label.text()
        if equation == '12345':
            self.new_window()
            return

        else:
            firstspace = equation.find(' ')
            firstnum = equation[:firstspace]
            secondspace = firstspace + 3
            secondnum = equation[secondspace:]
            operation = equation[firstspace + 1 :secondspace]

        if firstnum.startswith('.'):
            firstnum = f'0{firstnum}'
        
        elif secondnum.startswith('.'):
            secondnum = f'0{secondnum}'

        if '+' in equation:
            ans = float(firstnum) + float(secondnum)
            self.Process_Answer(ans)

        elif '-' in equation:
            ans = float(firstnum) - float(secondnum)
            self.Process_Answer(ans)

        elif '/' in equation:
            try:
                ans = float(firstnum) / float(secondnum)
                self.Process_Answer(ans)
            except:
                self.label.setText('Cant Divide by 0 Dumbass')

        elif '*' in equation:
            ans = float(firstnum) * float(secondnum)
            self.Process_Answer(ans)
            
        else:
            self.Process_Answer(equation)

    def dot(self):
        currentnum = self.label.text()
        
        if currentnum.endswith('.'):
            pass
        
        else:
            if currentnum == 'Enter a number first':
                currentnum = '0'
                
            elif currentnum == 'WTF is this':
                currentnum = '0'

            elif currentnum.endswith(' '):
                currentnum = currentnum + '0'

            self.label.setText(f'{currentnum}.')

    def Process_Answer(self, x):
        str_ans = str(x)
        decimal = str_ans.find('.')
        ans = str_ans[:decimal + 7]
        a = 0
        while a == 0:
            if '.' in ans and ans.endswith('0'):
                ans = ans[:-1]

            else:
                a = 1

        if ans.endswith('.'):
            ans = ans[:-1]

        self.label.setText(str(ans))
    
    def new_window(self):
       pass 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

