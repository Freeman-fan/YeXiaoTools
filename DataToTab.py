import csv
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from Ui_DataToTab import *


class MainWindows(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        # 绑定按钮事件
        self.btn_ChooseFile.clicked.connect(self.ChooseFilePath)
        self.btn_GetCsv.clicked.connect(self.GetCsv)
        self.btn_CleanAll.clicked.connect(self.CleanAll)
        self.btn_Save.clicked.connect(self.SaveFile)

        # 类参数
        self.file_path = None
        self.raw_data = None

        # 初始化窗口

    # 选择路径
    def ChooseFilePath(self):
        self.file_path = None
        try:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("CSV文件(*.csv);;所有格式(*)")
            if file_dialog.exec():
                file_path = file_dialog.selectedFiles()[0]
                if not file_path.endswith(".csv"):
                    file_path += ".csv"
                self.file_path = file_path
                self.edit_FilePath.setText(file_path)
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))

    # 处理文本
    def GetCsv(self):
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

    # 清空数据
    def CleanAll(self):
        self.edit_FilePath.clear()
        self.file_path = None
        self.textEdit.clear()
        self.tableWidget.setRowCount(0)
        self.tabWidget.setCurrentIndex(0)

    # 保存文件
    def SaveFile(self):
        try:
            with open(self.file_path, "w", newline="", encoding="utf-8-sig") as csvfile:
                csvwriter = csv.writer(csvfile)
                for i in range(self.tableWidget.rowCount()):
                    csvwriter.writerow(
                        [
                            self.tableWidget.item(i, 0).text(),
                            self.tableWidget.item(i, 3).text(),
                        ]
                    )
                    csvwriter.writerow([self.tableWidget.item(i, 1).text()])
                    if self.tableWidget.item(i, 2).text() != '':
                        cn = self.tableWidget.item(i, 2).text()
                        cn_group = cn.split('，')
                        for cn in cn_group:
                            csvwriter.writerow([cn])
                    csvwriter.writerow(['',])
        except Exception as e:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindows = MainWindows()
    mainWindows.show()
    sys.exit(app.exec())
