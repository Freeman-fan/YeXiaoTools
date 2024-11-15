from Ui_photo import Ui_mainWindow as Ui_photo_mainWindow
from ProjectJson import ProjectJson

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

import sys
import os
import csv
import json
import pandas as pd


# 类：主窗体
class MainWindows(QMainWindow, Ui_photo_mainWindow):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        # 绑定事件
        self.btn_addFile.clicked.connect(self.BtnClick_AddFile)
        self.btn_clear.clicked.connect(self.BtnClick_Clear)
        self.btn_addOneGood.clicked.connect(self.BtnClick_AddOneGood)
        self.btn_addAllGood.clicked.connect(self.BtnClick_AddAllGood)
        self.btn_delOneGood.clicked.connect(self.BtnClick_DelOneGood)
        self.btn_delAllGood.clicked.connect(self.BtnClick_DelAllGood)
        self.btn_OK.clicked.connect(self.BtnClick_OK)

    ###
    # TAB1：数据选择
    ###

    # 按钮单击：导入数据
    def BtnClick_AddFile(self):
        lst_goodName = []
        try:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("支持的文件格式(*.csv *.xlsx);;所有格式(*)")
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
            if file_dialog.exec():
                selectFiles = file_dialog.selectedFiles()
                self.lst_filePath.addItems(selectFiles)
                for filepath in selectFiles:
                    filename, formate = os.path.splitext(filepath)
                    # 将xlxs文件转为csv方便处理
                    if formate == ".xlsx":
                        df = pd.read_excel(filepath, sheet_name=2)
                        csv_filepath = filename + ".csv"
                        df.to_csv(csv_filepath, index=False, encoding="utf-8-sig")
                        filepath = csv_filepath
                    with open(
                        filepath, "r", newline="", encoding="utf-8-sig"
                    ) as csvfile:
                        csvreader = csv.reader(csvfile)
                        for row in csvreader:
                            if row[0] == "昵称":
                                continue
                            goodName = row[7] if row[7] != "" else None
                            if goodName not in lst_goodName:
                                lst_goodName.append(goodName)
                    if formate == ".xlsx":
                        os.remove(filepath)
            self.lst_goodNoChoose.addItems(lst_goodName)
        except Exception as e:
            pass

    # 按钮单击：清空全部
    def BtnClick_Clear(self):
        response = QMessageBox.question(
            self,
            "删除确认",
            "将清空所有数据，且无法恢复(除非已经另存)",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if response == QMessageBox.StandardButton.Yes:
            self.ClearAllData()

    # 按钮单击：添加一个
    def BtnClick_AddOneGood(self):
        selectItems = self.lst_goodNoChoose.selectedItems()
        for item in selectItems:
            item_move = self.lst_goodNoChoose.takeItem(self.lst_goodNoChoose.row(item))
            self.lst_goodChoose.addItem(item_move)

    # 按钮单击：添加全部
    def BtnClick_AddAllGood(self):
        lst_count = self.lst_goodNoChoose.count()
        for index in range(lst_count - 1, -1, -1):
            text = self.lst_goodNoChoose.item(index)
            self.lst_goodNoChoose.takeItem(index)
            self.lst_goodChoose.addItem(text)

    # 按钮单击：移除一个
    def BtnClick_DelOneGood(self):
        selectItems = self.lst_goodChoose.selectedItems()
        for item in selectItems:
            item_move = self.lst_goodChoose.takeItem(self.lst_goodChoose.row(item))
            self.lst_goodNoChoose.addItem(item_move)

    # 按钮单击：移除全部
    def BtnClick_DelAllGood(self):
        lst_count = self.lst_goodChoose.count()
        for index in range(lst_count - 1, -1, -1):
            text = self.lst_goodChoose.item(index)
            self.lst_goodChoose.takeItem(index)
            self.lst_goodNoChoose.addItem(text)

    # 按钮单击：确定
    def BtnClick_OK(self):
        pass

    # 清除所有
    def ClearAllData(self):
        self.lst_filePath.clear()
        self.lst_goodChoose.clear()
        self.lst_goodNoChoose.clear()
        self.lst_cn.clear()
        self.lst_good.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindows()
    mainwindow.show()
    sys.exit(app.exec())
