# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QGraphicsScene,QFileDialog,QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dia1 import Ui_Dialog
from cropper import QExampleLabel
import os
from imgtes import imgt
import pybrl as brl
import json
import get_path

global p
p=0
# g1
class Ui_MainWindow(object):
    # s=""
    # ctr=0
    # con_f = open('/Users/adityachandra/Environments/myocr/Gui/config.json')
    # config = json.load(con_f)
    # con_f.close()
    global fname
    fname=""
    global File_path
    File_path=""
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Win2()
        self.ui.setupUi(self.window)
        self.window.show()

    def newpro(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        # self.config=self.ui.get_stuff()
        self.Dialog.show()

    def loadpro(self):
        global fname
        fname=QFileDialog.getOpenFileName(None,'Open file',os.getenv('HOME'))[0]
        self.scene=QGraphicsScene()
        a=QPixmap(fname)
        self.scene.addPixmap(a.scaled(560,560))
        self.graphicsView.setScene(self.scene)

    def roi(self):
        self.wid = QtWidgets.QWidget()
        self.wid.setWindowModality(QtCore.Qt.ApplicationModal)
        self.wid.setGeometry(QtCore.QRect(290, 70, 691, 511))
        self.window = QtWidgets.QHBoxLayout(self.wid)
        self.lab = QtWidgets.QLabel()
        global fname
        self.ui = QExampleLabel(fname,self.lab)
        self.Done = QtWidgets.QPushButton()
        self.Done.setText("Done")
        self.Done.setGeometry(QtCore.QRect(900, 560, 60, 40))
        self.Done.setObjectName("Done")
        self.window.addWidget(self.ui)
        self.window.addWidget(self.Done)
        self.wid.show()
        self.Done.clicked.connect(self.clip)
        self.Done.clicked.connect(self.wid.close)

    def clip(self):
        self.listWidget = QtWidgets.QListWidget(self.columnView)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 211, 551))
        self.listWidget.show()
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(get_path.get_images()) ]
        # images=["/Users/adityachandra/clip/images/output1.jpg"]
        #ls = ['test', 'test2', 'test3']
        for i in range(len(onlyfiles)):
                label = QtWidgets.QLabel()
                pm = QtGui.QPixmap(join(get_path.get_images(), onlyfiles[i]))
                label.setPixmap(pm.scaled(150, 100,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.SmoothTransformation))
                item = QtWidgets.QListWidgetItem(str(i+1))
                # item = QtWidgets.QListWidgetItem()
                item.setSizeHint(QtCore.QSize(100,100))
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item,label)

    def appendPageNo(self):
        global p
        p=p+1
        pg="------------------------------------------- Page"+str(p)
        pgFile=open(get_path.get_english(),"a")
        pgFile.write("\n"+pg)
        pgFile.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 690)
        MainWindow.setMinimumSize(QtCore.QSize(1069, 690))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, 211, 551))
        self.scrollArea.setMinimumSize(QtCore.QSize(201, 481))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.columnView = QtWidgets.QColumnView(self.scrollAreaWidgetContents)
        self.columnView.setGeometry(QtCore.QRect(0, 0, 211, 551))
        self.columnView.setMinimumSize(QtCore.QSize(211, 551))
        self.columnView.setObjectName("columnView")
        # self.listWidget = QtWidgets.QListWidget(self.columnView)


        #List widget ends here

        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(189, 0, 21, 551))
        self.verticalScrollBar.setMinimumSize(QtCore.QSize(21, 551))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 91, 21))
        self.label.setMinimumSize(QtCore.QSize(91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        # self.mdiArea.setGeometry(QtCore.QRect(290, 70, 691, 511))
        # self.mdiArea.setObjectName("mdiArea")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(290, 70, 691, 511))
        self.graphicsView.setObjectName("graphicsView")
        self.scene=QGraphicsScene()
        global fname
        a=QPixmap(fname)
        self.scene.addPixmap(a.scaled(560,560))
        self.graphicsView.setScene(self.scene)


        self.Convert = QtWidgets.QPushButton(self.centralwidget)
        self.Convert.setEnabled(False)
        self.Convert.setGeometry(QtCore.QRect(680, 600, 113, 32))
        self.Convert.setObjectName("Convert")

        self.Sav = QtWidgets.QPushButton(self.centralwidget)
        self.Sav.setGeometry(QtCore.QRect(810, 600, 113, 32))
        self.Sav.setObjectName("Sav")
        self.Sav.clicked.connect(self.roi)

        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(950, 600, 113, 32))
        self.Next.setObjectName("Next")

        self.Next.clicked.connect(self.openWindow)
        self.Next.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # creates new project folder and all the required files
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionNew_Project.triggered.connect(self.newpro)

        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")

        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.triggered.connect(self.loadpro)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")

        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")

        self.actionWindow = QtWidgets.QAction(MainWindow)
        self.actionWindow.setObjectName("actionWindow")

        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)


        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)

        self.menuHelp.addAction(self.actionWindow)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Clipboard"))
        self.Convert.setText(_translate("MainWindow", "Convert"))
        self.Sav.setText(_translate("MainWindow", "Save"))
        self.Next.setText(_translate("MainWindow", "Next"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionWindow.setText(_translate("MainWindow", "Window"))
# g2
class Ui_Win2(Ui_MainWindow):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Ocr()
        self.ui.setupUi(self.window)
        self.window.show()

    def prevWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def addimage(self):
        fil=QFileDialog.getOpenFileName(None,'Open file',os.getenv('HOME'))[0]
        fi = open(fil,"r")
        contents=fi.read()
        fi.close()
        f=open(get_path.get_english(),'a+')
        f.write("\n"+"\n"+contents)
        self.textEdit.append(contents)
        f.close()

    def setupUi(self, Win2):
        Win2.setObjectName("Win2")
        Win2.resize(826, 667)
        Win2.setMinimumSize(QtCore.QSize(826, 667))
        self.centralwidget = QtWidgets.QWidget(Win2)
        self.centralwidget.setObjectName("centralwidget")
        # self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        # self.mdiArea.setGeometry(QtCore.QRect(20, 30, 381, 511))
        # self.mdiArea.setMinimumSize(QtCore.QSize(381, 511))
        # self.mdiArea.setObjectName("mdiArea")

        global fname
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 30, 381, 511))
        self.graphicsView.setObjectName("graphicsView")
        self.scene=QGraphicsScene()
        a=QPixmap(fname)
        self.scene.addPixmap(a.scaled(381,500))
        self.graphicsView.setScene(self.scene)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 30, 381, 511))
        self.textEdit.setMinimumSize(QtCore.QSize(381, 511))
        self.textEdit.setObjectName("textEdit")
        global text
        # rf = open("config.json")
        # config = json.load(rf)
        # rf.close()
        imgt_obj = imgt(fname)
        imgt_obj.imgtes()
        text=open(get_path.get_english(),'r+', encoding="utf8")
        # text = open(self.config["english"],"r")
        f=text.read()
        self.textEdit.setPlainText(f)
        # self.fs_watcher = QtCore.QFileSystemWatcher(/Users/adityachandra/test/eng.txt')
        # self.fs_watcher.fileChanged.connect(self.textEdit.setPlainText(f))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 0, 91, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 550, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.prevWindow)
        self.pushButton.clicked.connect(Win2.close)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 550, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton_2.clicked.connect(self.appendPageNo)
        self.pushButton_2.clicked.connect(Win2.close)

        Win2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Win2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Win2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Win2)
        self.statusbar.setObjectName("statusbar")
        Win2.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Win2)
        self.toolBar.setObjectName("toolBar")
        Win2.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionInsert = QtWidgets.QAction(Win2)
        self.actionInsert.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/adityachandra/Environments/myocr/Gui/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsert.setIcon(icon)
        self.actionInsert.setObjectName("actionInsert")
        self.actionInsert.triggered.connect(self.addimage)

        self.actionNew_Project = QtWidgets.QAction(Win2)
        self.actionNew_Project.setEnabled(False)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionOpen_Project = QtWidgets.QAction(Win2)
        self.actionOpen_Project.setEnabled(False)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionUndo = QtWidgets.QAction(Win2)
        self.actionUndo.setEnabled(False)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(Win2)
        self.actionRedo.setObjectName("actionRedo")
        self.actionUndo_2 = QtWidgets.QAction(Win2)
        self.actionUndo_2.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/adityachandra/Environments/myocr/Gui/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo_2.setIcon(icon1)
        self.actionUndo_2.setObjectName("actionUndo_2")
        self.actionRedo_2 = QtWidgets.QAction(Win2)
        self.actionRedo_2.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/adityachandra/Environments/myocr/Gui/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo_2.setIcon(icon2)
        self.actionRedo_2.setObjectName("actionRedo_2")
        self.actionQuit = QtWidgets.QAction(Win2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSave = QtWidgets.QAction(Win2)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionUndo)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionInsert)
        self.toolBar.addAction(self.actionUndo_2)
        self.toolBar.addAction(self.actionRedo_2)
        self.toolBar.addSeparator()

        self.retranslateUi(Win2)
        QtCore.QMetaObject.connectSlotsByName(Win2)

    def retranslateUi(self, Win2):
        _translate = QtCore.QCoreApplication.translate
        Win2.setWindowTitle(_translate("Win2", "Win2"))
        self.label.setText(_translate("Win2", "Image View"))
        self.label_2.setText(_translate("Win2", "NotePad"))
        self.pushButton.setText(_translate("Win2", "Back"))
        self.pushButton_2.setText(_translate("Win2", "Next"))
        self.menuFile.setTitle(_translate("Win2", "File "))
        self.menuEdit.setTitle(_translate("Win2", "Edit"))
        self.menuView.setTitle(_translate("Win2", "View"))
        self.menuAbout.setTitle(_translate("Win2", "About"))
        self.menuSettings.setTitle(_translate("Win2", "Settings"))
        self.menuHelp.setTitle(_translate("Win2", "Help"))
        self.toolBar.setWindowTitle(_translate("Win2", "toolBar"))
        self.actionInsert.setText(_translate("Win2", "insert"))
        self.actionInsert.setShortcut(_translate("Win2", "Ctrl+I"))
        self.actionNew_Project.setText(_translate("Win2", "New Project"))
        self.actionNew_Project.setShortcut(_translate("Win2", "Ctrl+N"))
        self.actionOpen_Project.setText(_translate("Win2", "Open Project"))
        self.actionOpen_Project.setShortcut(_translate("Win2", "Ctrl+O"))
        self.actionUndo.setText(_translate("Win2", "New Project"))
        self.actionRedo.setText(_translate("Win2", "redo"))
        self.actionUndo_2.setText(_translate("Win2", "undo"))
        self.actionUndo_2.setShortcut(_translate("Win2", "Ctrl+Z"))
        self.actionRedo_2.setText(_translate("Win2", "redo"))
        self.actionRedo_2.setShortcut(_translate("Win2", "Ctrl+Y"))
        self.actionQuit.setText(_translate("Win2", "Quit"))
        self.actionSave.setText(_translate("Win2", "Save"))

# import insert_rc
# g3
class CustomLineEdit(QtWidgets.QTextEdit):
    def __init__(self, parent = None):
        super(CustomLineEdit, self).__init__()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__contextMenu)

    def __contextMenu(self):
        self._normalMenu = self.createStandardContextMenu()
        self._addCustomMenuItems(self._normalMenu)
        self._normalMenu.exec_(QtGui.QCursor.pos())

    def _addCustomMenuItems(self, menu):
        menu.addSeparator()
        menu.addAction(u'Test', self.testFunc)

    def testFunc(self):
        print ("Call")

class Ui_Ocr(Ui_Win2):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Nem()
        self.ui.setupUi(self.window)
        self.window.show()

    def prevWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Win2()
        self.ui.setupUi(self.window)
        self.window.show()

    def open2Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def mytext(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        example=brl.translate(textSelected)
        s = brl.toUnicodeSymbols(example, flatten=True)
        cursor.insertText(s)


    def setupUi(self, Ocr):
        Ocr.setObjectName("Ocr")
        Ocr.resize(801, 669)
        self.centralwidget = QtWidgets.QWidget(Ocr)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 60, 501, 511))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setObjectName("textEdit")
        global text
        text=open(get_path.get_english(),'r+', encoding="utf8")
        f=text.read()
        self.textEdit.setPlainText(f)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 121, 21))
        self.label.setObjectName("label")
        self.nem = QtWidgets.QPushButton(self.centralwidget)
        self.nem.setGeometry(QtCore.QRect(630, 10, 161, 61))
        self.nem.setObjectName("nem")

        # self.nem.clicked.connect(self.openWindow)
        self.nem.clicked.connect(self.mytext)



        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 580, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.prevWindow)
        self.pushButton.clicked.connect(Ocr.close)


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(622, 580, 141, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.open2Window)
        self.pushButton_2.clicked.connect(Ocr.close)

        Ocr.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ocr)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setEnabled(False)
        self.menuFile.setObjectName("menuFile")
        Ocr.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ocr)
        self.statusbar.setObjectName("statusbar")
        Ocr.setStatusBar(self.statusbar)
        self.actionPrint_preview = QtWidgets.QAction(Ocr)
        self.actionPrint_preview.setObjectName("actionPrint_preview")
        self.actionUndo = QtWidgets.QAction(Ocr)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(Ocr)
        self.actionRedo.setObjectName("actionRedo")
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(Ocr)
        QtCore.QMetaObject.connectSlotsByName(Ocr)

    def retranslateUi(self, Ocr):
        _translate = QtCore.QCoreApplication.translate
        Ocr.setWindowTitle(_translate("Ocr", "Ocr"))
        self.label.setText(_translate("Ocr", "TextEditor"))
        self.nem.setText(_translate("Ocr", "Convert to Nemeth"))
        self.pushButton.setText(_translate("Ocr", "Go back"))
        self.pushButton_2.setText(_translate("Ocr", "Preview in Braille"))
        self.menuEdit.setTitle(_translate("Ocr", "Edit"))
        self.menuFile.setTitle(_translate("Ocr", "File"))
        self.actionPrint_preview.setText(_translate("Ocr", "Print preview"))
        self.actionUndo.setText(_translate("Ocr", "undo"))
        self.actionRedo.setText(_translate("Ocr", "redo"))

# g4
class Ui_Nem(Ui_Ocr):
    def setupUi(self, Nem):
        Nem.setObjectName("Nem")
        Nem.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Nem)
        self.textEdit.setGeometry(QtCore.QRect(40, 50, 321, 71))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Nem)
        self.label.setGeometry(QtCore.QRect(40, 20, 241, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Nem)
        QtCore.QMetaObject.connectSlotsByName(Nem)

    def retranslateUi(self, Nem):
        _translate = QtCore.QCoreApplication.translate
        Nem.setWindowTitle(_translate("Nem", "Nem"))
        self.label.setText(_translate("Nem", "Nemeth braille equivlent in text form"))
# g5
class Ui_Form(Ui_Ocr):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(611, 617)
        Form.setMinimumSize(QtCore.QSize(611, 617))
        Form.setMaximumSize(QtCore.QSize(611, 617))
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 391, 521))
        self.textEdit.setMinimumSize(QtCore.QSize(391, 521))
        self.textEdit.setObjectName("textEdit")

        eng=" A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)="
        braille="⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
        transtab = str.maketrans(eng, braille)
        # transtab = str.maketrans(braille, eng)
        f1=open(get_path.get_english(),'r')
        contents=f1.read().upper()
        b1=open(get_path.get_braille(),'a')
        b1.write(contents.translate(transtab))
        f1.close()
        b1.close()
        # print(s.translate(transtab))


        b=open(get_path.get_braille(),'r+', encoding="utf8")
        f=b.read()
        self.textEdit.setPlainText(f)

        self.Finish = QtWidgets.QPushButton(Form)
        self.Finish.setGeometry(QtCore.QRect(420, 570, 113, 32))
        self.Finish.setMinimumSize(QtCore.QSize(113, 32))
        self.Finish.setObjectName("Finish")

        self.Finish.clicked.connect(self.openWindow)
        self.Finish.clicked.connect(Form.close)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 570, 113, 32))
        self.pushButton_2.setMinimumSize(QtCore.QSize(113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.dockWidget = QtWidgets.QDockWidget(Form)
        self.dockWidget.setGeometry(QtCore.QRect(480, 30, 131, 531))
        self.dockWidget.setMinimumSize(QtCore.QSize(131, 531))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(480, 10, 111, 16))
        self.label.setMinimumSize(QtCore.QSize(111, 16))
        self.label.setObjectName("label")
        self.dockWidget.raise_()
        self.textEdit.raise_()
        self.Finish.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Finish.setText(_translate("Form", "Finish"))
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.label.setText(_translate("Form", "Braille KeyBoard"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
