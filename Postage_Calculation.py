from Ui_Postage_Calculation import Ui_MainWindow as Ui_Postage_Calculation_MainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class Mainwindows(QMainWindow, Ui_Postage_Calculation_MainWindow):
    def __init__(self, parent = None):
        super(Mainwindows, self).__init__(parent)
        self.setupUi(self)

        #绑定事件
        self.btn_LoadData.clicked.connect(self.LoadData)
        self.btn_PrintFinTab.clicked.connect(self.PrintFinTab)
        self.btn_ReCount.clicked.connect(self.ReCount)
        self.btn_Save.clicked.connect(self.SaveData)
        self.btn_SaveAndClose.clicked.connect(self.CloseData)

        #类变量
        self.file_path = None


    # 导入数据
    def LoadData(self):
        self.file_path = None
        try:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter('CSV文件(*.csv);;所有格式(*)')
            if file_dialog.exec():
                self.file_path = file_dialog.selectedFiles()[0]
                if self.file_path.endswith('.csv'):
                    #解析csv
                    pass
        except Exception as e:
            QMessageBox.warning(self, '错误', str(e))

    
    # 保存
    def SaveData(self):
        pass


    # 关闭
    def CloseData(self):
        pass


    # 重算本单
    def ReCount(self):
        pass


    # 生成总表
    def PrintFinTab(self):
        pass