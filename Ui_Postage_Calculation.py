# Form implementation generated from reading ui file 'd:\Onedrive\CodeS\Python\YeXiao\Postage_Calculation.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 703)
        MainWindow.setMinimumSize(QtCore.QSize(906, 703))
        MainWindow.setMaximumSize(QtCore.QSize(906, 703))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list_mNum = QtWidgets.QListWidget(parent=self.tab)
        self.list_mNum.setMinimumSize(QtCore.QSize(200, 0))
        self.list_mNum.setMaximumSize(QtCore.QSize(150, 16777215))
        self.list_mNum.setObjectName("list_mNum")
        self.horizontalLayout.addWidget(self.list_mNum)
        self.tab_Details = QtWidgets.QTableWidget(parent=self.tab)
        self.tab_Details.setMinimumSize(QtCore.QSize(550, 0))
        self.tab_Details.setObjectName("tab_Details")
        self.tab_Details.setColumnCount(3)
        self.tab_Details.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_Details.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_Details.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_Details.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tab_Details)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_NewProject = QtWidgets.QPushButton(parent=self.tab)
        self.btn_NewProject.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_NewProject.setObjectName("btn_NewProject")
        self.verticalLayout_3.addWidget(self.btn_NewProject)
        self.btn_LoadData = QtWidgets.QPushButton(parent=self.tab)
        self.btn_LoadData.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_LoadData.setObjectName("btn_LoadData")
        self.verticalLayout_3.addWidget(self.btn_LoadData)
        self.btn_Save = QtWidgets.QPushButton(parent=self.tab)
        self.btn_Save.setEnabled(False)
        self.btn_Save.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_Save.setObjectName("btn_Save")
        self.verticalLayout_3.addWidget(self.btn_Save)
        self.line_4 = QtWidgets.QFrame(parent=self.tab)
        self.line_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.edit_rpg = QtWidgets.QLineEdit(parent=self.tab)
        self.edit_rpg.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edit_rpg.setObjectName("edit_rpg")
        self.verticalLayout_3.addWidget(self.edit_rpg)
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.edit_InlandPost = QtWidgets.QLineEdit(parent=self.tab)
        self.edit_InlandPost.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edit_InlandPost.setObjectName("edit_InlandPost")
        self.verticalLayout_3.addWidget(self.edit_InlandPost)
        self.btn_ReCountAll = QtWidgets.QPushButton(parent=self.tab)
        self.btn_ReCountAll.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_ReCountAll.setObjectName("btn_ReCountAll")
        self.verticalLayout_3.addWidget(self.btn_ReCountAll)
        self.line_2 = QtWidgets.QFrame(parent=self.tab)
        self.line_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.btn_NewGood = QtWidgets.QPushButton(parent=self.tab)
        self.btn_NewGood.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_NewGood.setObjectName("btn_NewGood")
        self.verticalLayout_3.addWidget(self.btn_NewGood)
        self.btn_DelGood = QtWidgets.QPushButton(parent=self.tab)
        self.btn_DelGood.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_DelGood.setObjectName("btn_DelGood")
        self.verticalLayout_3.addWidget(self.btn_DelGood)
        self.line = QtWidgets.QFrame(parent=self.tab)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(parent=self.tab)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.edit_TotalGram = QtWidgets.QLineEdit(parent=self.tab)
        self.edit_TotalGram.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edit_TotalGram.setObjectName("edit_TotalGram")
        self.verticalLayout_3.addWidget(self.edit_TotalGram)
        self.btn_AddLine = QtWidgets.QPushButton(parent=self.tab)
        self.btn_AddLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_AddLine.setObjectName("btn_AddLine")
        self.verticalLayout_3.addWidget(self.btn_AddLine)
        self.btn_DelLine = QtWidgets.QPushButton(parent=self.tab)
        self.btn_DelLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_DelLine.setObjectName("btn_DelLine")
        self.verticalLayout_3.addWidget(self.btn_DelLine)
        self.btn_ReCount = QtWidgets.QPushButton(parent=self.tab)
        self.btn_ReCount.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_ReCount.setObjectName("btn_ReCount")
        self.verticalLayout_3.addWidget(self.btn_ReCount)
        self.line_3 = QtWidgets.QFrame(parent=self.tab)
        self.line_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.btn_PrintFinTab = QtWidgets.QPushButton(parent=self.tab)
        self.btn_PrintFinTab.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_PrintFinTab.setObjectName("btn_PrintFinTab")
        self.verticalLayout_3.addWidget(self.btn_PrintFinTab)
        spacerItem = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab_FineTab = QtWidgets.QTableWidget(parent=self.tab_2)
        self.tab_FineTab.setObjectName("tab_FineTab")
        self.tab_FineTab.setColumnCount(3)
        self.tab_FineTab.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_FineTab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_FineTab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_FineTab.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_2.addWidget(self.tab_FineTab)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_SaveFinaTab = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_SaveFinaTab.setObjectName("btn_SaveFinaTab")
        self.verticalLayout.addWidget(self.btn_SaveFinaTab)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "国际表"))
        item = self.tab_Details.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "cn"))
        item = self.tab_Details.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "重量"))
        item = self.tab_Details.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "肾额"))
        self.btn_NewProject.setText(_translate("MainWindow", "创建项目"))
        self.btn_LoadData.setText(_translate("MainWindow", "导入数据"))
        self.btn_Save.setText(_translate("MainWindow", "另存为"))
        self.label.setText(_translate("MainWindow", "克重单价(r/g)"))
        self.edit_rpg.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "国内均摊(r)"))
        self.edit_InlandPost.setText(_translate("MainWindow", "0"))
        self.btn_ReCountAll.setText(_translate("MainWindow", "重算所有"))
        self.btn_NewGood.setText(_translate("MainWindow", "新建订单"))
        self.btn_DelGood.setText(_translate("MainWindow", "删除订单"))
        self.label_3.setText(_translate("MainWindow", "本单总重"))
        self.edit_TotalGram.setText(_translate("MainWindow", "0"))
        self.btn_AddLine.setText(_translate("MainWindow", "添加行"))
        self.btn_DelLine.setText(_translate("MainWindow", "删除行"))
        self.btn_ReCount.setText(_translate("MainWindow", "重算订单"))
        self.btn_PrintFinTab.setText(_translate("MainWindow", "生成总表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "分表"))
        item = self.tab_FineTab.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "cn"))
        item = self.tab_FineTab.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "重量"))
        item = self.tab_FineTab.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "肾额"))
        self.btn_SaveFinaTab.setText(_translate("MainWindow", "导出总表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "整箱总表"))
