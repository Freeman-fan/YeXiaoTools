import csv
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from Ui_DataToTab import *
from Ui_DataToTab_ReSplitDialog import *


# 类：重新拆分对话框
class ResplitDialog(QDialog, Ui_Dialog):
    def __init__(self, rawdata):
        super().__init__()
        self.setupUi(self)
        self.rawdata = rawdata

        # 按钮事件
        self.btn_ReSplit.clicked.connect(self.ReSplit)
        self.btn_Confirm.clicked.connect(self.Confirm)

    def ReSplit(self):
        newSplit = self.lineEdit.text()
        try:
            newdata = self.rawdata.replace(newSplit, "，")
            self.textEdit.setText(newdata)
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))

    def Confirm(self):
        self.rawdata = self.textEdit.toPlainText()
        self.accept()


# 类：主窗口
class MainWindows(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        # 绑定按钮事件
        self.btn_GetCsv.clicked.connect(self.GetCsv)
        self.btn_CleanAll.clicked.connect(self.CleanAll)
        self.btn_AddLine.clicked.connect(self.AddLine)
        self.btn_DelLine.clicked.connect(self.DelLine)
        self.btn_ReSplit.clicked.connect(self.ReSplit)
        self.btn_Save.clicked.connect(self.SaveFile)

        # 初始化窗口

    # 处理文本
    def GetCsv(self):
        try:
            if self.textEdit.toPlainText() == "":
                QMessageBox.warning(self, "错误", "原始数据不能为空")
                return
            rawText = self.textEdit.toPlainText()
            lintText = rawText.split("\n")
            self.tableWidget.setRowCount(len(lintText))
            i = 0
            for text in lintText:
                item = text.split("\t")
                for j in range(4):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(item[j]))
                i += 1
            self.tableWidget.resizeColumnsToContents()
            self.tabWidget.setCurrentIndex(1)
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))

    # 清空数据
    def CleanAll(self):
        self.textEdit.clear()
        self.tableWidget.setRowCount(0)
        self.tabWidget.setCurrentIndex(0)

    # 添加一行
    def AddLine(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)

    # 删除一行
    def DelLine(self):
        row = self.tableWidget.currentRow()
        if row != -1:
            self.tableWidget.removeRow(row)

    # 重新拆分
    def ReSplit(self):
        rawitem = self.tableWidget.selectedItems()
        if rawitem:
            for item in rawitem:
                row = self.tableWidget.row(item)
                col = self.tableWidget.column(item)
                rawdata = item.text()
            resplitDialog = ResplitDialog(rawdata)
            if resplitDialog.exec():
                newdata = resplitDialog.rawdata
                self.tableWidget.setItem(row, col, QTableWidgetItem(newdata))
                self.tableWidget.resizeColumnsToContents()

    # 保存文件
    def SaveFile(self):
        file_path = None
        try:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("CSV文件(*.csv);;所有格式(*)")
            if file_dialog.exec():
                file_path = file_dialog.selectedFiles()[0]
                if not file_path.endswith(".csv"):
                    file_path += ".csv"
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))
        try:
            with open(file_path, "w", newline="", encoding="utf-8-sig") as csvfile:
                csvwriter = csv.writer(csvfile)
                for i in range(self.tableWidget.rowCount()):
                    csvwriter.writerow(
                        [
                            self.tableWidget.item(i, 0).text(),
                            self.tableWidget.item(i, 3).text(),
                        ]
                    )
                    csvwriter.writerow([self.tableWidget.item(i, 1).text()])
                    if self.tableWidget.item(i, 2).text() != "":
                        cn = self.tableWidget.item(i, 2).text()
                        cn_group = cn.split("，")
                        for cn in cn_group:
                            csvwriter.writerow([cn])
                    csvwriter.writerow(
                        [
                            "",
                        ]
                    )
        except Exception as e:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindows = MainWindows()
    mainWindows.show()
    sys.exit(app.exec())
