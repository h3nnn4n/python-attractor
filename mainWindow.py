# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Wed Jun 18 17:09:32 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(551, 317)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frameMaster = QtGui.QFrame(self.centralwidget)
        self.frameMaster.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.frameMaster.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameMaster.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMaster.setObjectName(_fromUtf8("frameMaster"))
        self.frameImage = QtGui.QFrame(self.frameMaster)
        self.frameImage.setGeometry(QtCore.QRect(10, 150, 351, 80))
        self.frameImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameImage.setFrameShadow(QtGui.QFrame.Raised)
        self.frameImage.setObjectName(_fromUtf8("frameImage"))
        self.txtBoxSens = QtGui.QLineEdit(self.frameImage)
        self.txtBoxSens.setGeometry(QtCore.QRect(270, 10, 61, 22))
        self.txtBoxSens.setObjectName(_fromUtf8("txtBoxSens"))
        self.txtBoxFrames = QtGui.QLineEdit(self.frameImage)
        self.txtBoxFrames.setGeometry(QtCore.QRect(170, 10, 61, 22))
        self.txtBoxFrames.setObjectName(_fromUtf8("txtBoxFrames"))
        self.txtBoxHeight = QtGui.QLineEdit(self.frameImage)
        self.txtBoxHeight.setGeometry(QtCore.QRect(50, 40, 61, 22))
        self.txtBoxHeight.setObjectName(_fromUtf8("txtBoxHeight"))
        self.label_17 = QtGui.QLabel(self.frameImage)
        self.label_17.setGeometry(QtCore.QRect(120, 10, 41, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_16 = QtGui.QLabel(self.frameImage)
        self.label_16.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_18 = QtGui.QLabel(self.frameImage)
        self.label_18.setGeometry(QtCore.QRect(120, 40, 51, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.txtBoxIters = QtGui.QLineEdit(self.frameImage)
        self.txtBoxIters.setGeometry(QtCore.QRect(170, 40, 61, 22))
        self.txtBoxIters.setObjectName(_fromUtf8("txtBoxIters"))
        self.label_19 = QtGui.QLabel(self.frameImage)
        self.label_19.setGeometry(QtCore.QRect(240, 10, 41, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_15 = QtGui.QLabel(self.frameImage)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.txtBoxWidth = QtGui.QLineEdit(self.frameImage)
        self.txtBoxWidth.setGeometry(QtCore.QRect(50, 10, 61, 22))
        self.txtBoxWidth.setObjectName(_fromUtf8("txtBoxWidth"))
        self.frameParameter = QtGui.QFrame(self.frameMaster)
        self.frameParameter.setGeometry(QtCore.QRect(10, 10, 171, 131))
        self.frameParameter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameParameter.setFrameShadow(QtGui.QFrame.Raised)
        self.frameParameter.setObjectName(_fromUtf8("frameParameter"))
        self.txtBoxDD = QtGui.QLineEdit(self.frameParameter)
        self.txtBoxDD.setGeometry(QtCore.QRect(100, 100, 61, 22))
        self.txtBoxDD.setObjectName(_fromUtf8("txtBoxDD"))
        self.label = QtGui.QLabel(self.frameParameter)
        self.label.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_12 = QtGui.QLabel(self.frameParameter)
        self.label_12.setGeometry(QtCore.QRect(83, 40, 20, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.txtBoxBB = QtGui.QLineEdit(self.frameParameter)
        self.txtBoxBB.setGeometry(QtCore.QRect(100, 40, 61, 22))
        self.txtBoxBB.setObjectName(_fromUtf8("txtBoxBB"))
        self.label_2 = QtGui.QLabel(self.frameParameter)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 16, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frameParameter)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 16, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_13 = QtGui.QLabel(self.frameParameter)
        self.label_13.setGeometry(QtCore.QRect(83, 70, 20, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_4 = QtGui.QLabel(self.frameParameter)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 16, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtBoxA = QtGui.QLineEdit(self.frameParameter)
        self.txtBoxA.setGeometry(QtCore.QRect(20, 10, 61, 22))
        self.txtBoxA.setObjectName(_fromUtf8("txtBoxA"))
        self.txtBoxD = QtGui.QLineEdit(self.frameParameter)
        self.txtBoxD.setGeometry(QtCore.QRect(20, 100, 61, 22))
        self.txtBoxD.setObjectName(_fromUtf8("txtBoxD"))
        self.txtBoxAA = QtGui.QLineEdit(self.frameParameter)
        self.txtBoxAA.setGeometry(QtCore.QRect(100, 10, 61, 22))
        self.txtBoxAA.setObjectName(_fromUtf8("txtBoxAA"))
        self.txtBoxB = QtGui.QLineEdit(self.frameParameter)
        self.txtBoxB.setGeometry(QtCore.QRect(20, 40, 61, 22))
        self.txtBoxB.setObjectName(_fromUtf8("txtBoxB"))
        self.label_14 = QtGui.QLabel(self.frameParameter)
        self.label_14.setGeometry(QtCore.QRect(83, 102, 20, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.txtBoxC = QtGui.QLineEdit(self.frameParameter)
        self.txtBoxC.setGeometry(QtCore.QRect(20, 70, 61, 22))
        self.txtBoxC.setObjectName(_fromUtf8("txtBoxC"))
        self.label_11 = QtGui.QLabel(self.frameParameter)
        self.label_11.setGeometry(QtCore.QRect(83, 12, 20, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.txtBoxCC = QtGui.QLineEdit(self.frameParameter)
        self.txtBoxCC.setGeometry(QtCore.QRect(100, 70, 61, 22))
        self.txtBoxCC.setObjectName(_fromUtf8("txtBoxCC"))
        self.frameColor = QtGui.QFrame(self.frameMaster)
        self.frameColor.setGeometry(QtCore.QRect(190, 10, 221, 131))
        self.frameColor.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameColor.setFrameShadow(QtGui.QFrame.Raised)
        self.frameColor.setObjectName(_fromUtf8("frameColor"))
        self.label_6 = QtGui.QLabel(self.frameColor)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 31, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtBoxGreen = QtGui.QLineEdit(self.frameColor)
        self.txtBoxGreen.setGeometry(QtCore.QRect(90, 70, 50, 22))
        self.txtBoxGreen.setObjectName(_fromUtf8("txtBoxGreen"))
        self.label_8 = QtGui.QLabel(self.frameColor)
        self.label_8.setGeometry(QtCore.QRect(50, 50, 31, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.txtBoxBlue = QtGui.QLineEdit(self.frameColor)
        self.txtBoxBlue.setGeometry(QtCore.QRect(140, 70, 50, 22))
        self.txtBoxBlue.setObjectName(_fromUtf8("txtBoxBlue"))
        self.txtBoxBlue2 = QtGui.QLineEdit(self.frameColor)
        self.txtBoxBlue2.setGeometry(QtCore.QRect(140, 100, 50, 22))
        self.txtBoxBlue2.setObjectName(_fromUtf8("txtBoxBlue2"))
        self.txtBoxRed2 = QtGui.QLineEdit(self.frameColor)
        self.txtBoxRed2.setGeometry(QtCore.QRect(40, 100, 50, 22))
        self.txtBoxRed2.setObjectName(_fromUtf8("txtBoxRed2"))
        self.label_9 = QtGui.QLabel(self.frameColor)
        self.label_9.setGeometry(QtCore.QRect(100, 50, 31, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.txtBoxRed = QtGui.QLineEdit(self.frameColor)
        self.txtBoxRed.setGeometry(QtCore.QRect(40, 70, 50, 22))
        self.txtBoxRed.setObjectName(_fromUtf8("txtBoxRed"))
        self.label_10 = QtGui.QLabel(self.frameColor)
        self.label_10.setGeometry(QtCore.QRect(150, 50, 31, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_7 = QtGui.QLabel(self.frameColor)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 31, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.txtBoxGreen2 = QtGui.QLineEdit(self.frameColor)
        self.txtBoxGreen2.setGeometry(QtCore.QRect(90, 100, 50, 22))
        self.txtBoxGreen2.setObjectName(_fromUtf8("txtBoxGreen2"))
        self.comboBox = QtGui.QComboBox(self.frameColor)
        self.comboBox.setGeometry(QtCore.QRect(100, 10, 91, 24))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.frameColor)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.frameButton = QtGui.QFrame(self.frameMaster)
        self.frameButton.setGeometry(QtCore.QRect(420, 10, 120, 131))
        self.frameButton.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameButton.setFrameShadow(QtGui.QFrame.Raised)
        self.frameButton.setObjectName(_fromUtf8("frameButton"))
        self.pushButton = QtGui.QPushButton(self.frameButton)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 101, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.buttonRender = QtGui.QPushButton(self.frameButton)
        self.buttonRender.setGeometry(QtCore.QRect(10, 10, 101, 27))
        self.buttonRender.setObjectName(_fromUtf8("buttonRender"))
        self.buttonClose = QtGui.QPushButton(self.frameButton)
        self.buttonClose.setGeometry(QtCore.QRect(10, 40, 101, 27))
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.progressBar = QtGui.QProgressBar(self.frameMaster)
        self.progressBar.setGeometry(QtCore.QRect(10, 240, 531, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.textEdit = QtGui.QTextEdit(self.frameMaster)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(370, 150, 171, 81))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuQuit = QtGui.QMenu(self.menubar)
        self.menuQuit.setObjectName(_fromUtf8("menuQuit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionYep_quit_now = QtGui.QAction(MainWindow)
        self.actionYep_quit_now.setObjectName(_fromUtf8("actionYep_quit_now"))
        self.menuQuit.addAction(self.actionYep_quit_now)
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtBoxA, self.txtBoxAA)
        MainWindow.setTabOrder(self.txtBoxAA, self.txtBoxB)
        MainWindow.setTabOrder(self.txtBoxB, self.txtBoxBB)
        MainWindow.setTabOrder(self.txtBoxBB, self.txtBoxC)
        MainWindow.setTabOrder(self.txtBoxC, self.txtBoxCC)
        MainWindow.setTabOrder(self.txtBoxCC, self.txtBoxD)
        MainWindow.setTabOrder(self.txtBoxD, self.txtBoxDD)
        MainWindow.setTabOrder(self.txtBoxDD, self.txtBoxRed)
        MainWindow.setTabOrder(self.txtBoxRed, self.txtBoxGreen)
        MainWindow.setTabOrder(self.txtBoxGreen, self.txtBoxBlue)
        MainWindow.setTabOrder(self.txtBoxBlue, self.txtBoxRed2)
        MainWindow.setTabOrder(self.txtBoxRed2, self.txtBoxGreen2)
        MainWindow.setTabOrder(self.txtBoxGreen2, self.txtBoxBlue2)
        MainWindow.setTabOrder(self.txtBoxBlue2, self.txtBoxWidth)
        MainWindow.setTabOrder(self.txtBoxWidth, self.txtBoxHeight)
        MainWindow.setTabOrder(self.txtBoxHeight, self.txtBoxFrames)
        MainWindow.setTabOrder(self.txtBoxFrames, self.txtBoxIters)
        MainWindow.setTabOrder(self.txtBoxIters, self.txtBoxSens)
        MainWindow.setTabOrder(self.txtBoxSens, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.buttonRender)
        MainWindow.setTabOrder(self.buttonRender, self.buttonClose)
        MainWindow.setTabOrder(self.buttonClose, self.pushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.txtBoxSens.setText(_translate("MainWindow", "0.025", None))
        self.txtBoxFrames.setText(_translate("MainWindow", "1000", None))
        self.txtBoxHeight.setText(_translate("MainWindow", "600", None))
        self.label_17.setText(_translate("MainWindow", "Frames:", None))
        self.label_16.setText(_translate("MainWindow", "Height:", None))
        self.label_18.setText(_translate("MainWindow", "Iterations:", None))
        self.txtBoxIters.setText(_translate("MainWindow", "5000", None))
        self.label_19.setText(_translate("MainWindow", "Sens:", None))
        self.label_15.setText(_translate("MainWindow", "Width:", None))
        self.txtBoxWidth.setText(_translate("MainWindow", "800", None))
        self.txtBoxDD.setText(_translate("MainWindow", "1.2", None))
        self.label.setText(_translate("MainWindow", "A:", None))
        self.label_12.setText(_translate("MainWindow", "to", None))
        self.txtBoxBB.setText(_translate("MainWindow", "1.9", None))
        self.label_2.setText(_translate("MainWindow", "B:", None))
        self.label_3.setText(_translate("MainWindow", "C:", None))
        self.label_13.setText(_translate("MainWindow", "to", None))
        self.label_4.setText(_translate("MainWindow", "D:", None))
        self.txtBoxA.setText(_translate("MainWindow", "-1.7", None))
        self.txtBoxD.setText(_translate("MainWindow", "-0.8", None))
        self.txtBoxAA.setText(_translate("MainWindow", "-0.6", None))
        self.txtBoxB.setText(_translate("MainWindow", "1.2", None))
        self.label_14.setText(_translate("MainWindow", "to", None))
        self.txtBoxC.setText(_translate("MainWindow", "0.9", None))
        self.label_11.setText(_translate("MainWindow", "to", None))
        self.txtBoxCC.setText(_translate("MainWindow", "1.8", None))
        self.label_6.setText(_translate("MainWindow", "From:", None))
        self.txtBoxGreen.setText(_translate("MainWindow", "255", None))
        self.label_8.setText(_translate("MainWindow", "Red", None))
        self.txtBoxBlue.setText(_translate("MainWindow", "0", None))
        self.txtBoxBlue2.setText(_translate("MainWindow", "200", None))
        self.txtBoxRed2.setText(_translate("MainWindow", "255", None))
        self.label_9.setText(_translate("MainWindow", "Green", None))
        self.txtBoxRed.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "Blue", None))
        self.label_7.setText(_translate("MainWindow", "To:", None))
        self.txtBoxGreen2.setText(_translate("MainWindow", "125", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "HUE shift", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "2color grad", None))
        self.label_5.setText(_translate("MainWindow", "Coloring mode:", None))
        self.pushButton.setText(_translate("MainWindow", "Useless big button", None))
        self.buttonRender.setText(_translate("MainWindow", "Render", None))
        self.buttonClose.setText(_translate("MainWindow", "Close!", None))
        self.menuQuit.setTitle(_translate("MainWindow", "Quit", None))
        self.actionYep_quit_now.setText(_translate("MainWindow", "Yep, quit now!", None))

