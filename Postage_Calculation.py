from Ui_Postage_Calculation import Ui_MainWindow as Ui_Postage_Calculation_MainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import sys
import os
import pandas as pd
import json
import csv


# 从csv中读取数据并写入json中
def GetFromCsv(csv_path, json_path):
    empty_num = 0
    text_num = 0
    m_num = None
    total_gram = None
    cn_group = []
    gram_group = []
    json_list = []
    with open(csv_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_list = [item for item in row]
            if row_list[0] != "":  # 不是空行
                text_num += 1
                empty_num = 0
                if text_num == 1:  # 读取m码和总重
                    m_num = row_list[0]
                    if row_list[1] == "":
                        total_gram = 0
                    else:
                        try:
                            total_gram = float(row_list[1])
                        except:
                            total_gram = 0
                elif text_num > 1:  # 读取cn和称重
                    cn_group.append(row_list[0])
                    if row_list[1] == "":
                        gram_group.append(0)
                    else:
                        try:
                            gram_group.append(float(row_list[1]))
                        except:
                            0
            elif row_list[0] == "" and empty_num != 1:  # 有空行
                empty_num = 1
                text_num = 0
                # 数据检查
                if m_num == None:
                    continue
                elif total_gram == 0:
                    total_gram = sum(gram_group)
                elif gram_group[0] == 0:
                    gram_group[0] = total_gram
                good_json = Goods_json(
                    mNum=m_num,
                    total_gram=total_gram,
                    cn_group=cn_group,
                    gram_group=gram_group,
                )
                json_list.append(good_json.info_json)
                # 清空列表
                m_num = None
                total_gram = None
                cn_group.clear()
                gram_group.clear()
    # 构建元数据
    file_name, _ = os.path.splitext(os.path.basename(csv_path))
    base_info = {
        "BoxID": f"{file_name}",
        "isCountPostage": False,
        "rpg": 0.12,
        "inlandPostage": 2.00,
    }
    json_list.insert(0, base_info)
    with open(json_path, "w", encoding="utf-8-sig") as jsonfile:
        json.dump(json_list, jsonfile, ensure_ascii=False, indent=4)


# 计算所有订单的邮费
def CountAll(json_path):
    with open(json_path, "r", encoding="utf-8-sig") as jsonfile:
        data = json.load(jsonfile)
    for item in data:
        if item.get("rpg"):
            rpg = item.get("rpg")
            inland_postage = item.get("inlandPostage")
            item["isCountPostage"] = True
        if item.get("goodID"):
            each_gram = item.get("eachGram", {})
            gram_price_group = []
            for gram_list in each_gram.values():
                if isinstance(gram_list, list) and len(gram_list) >= 1:
                    gram_price_group.append(gram_list)
            # 计算邮费
            total_gram = item.get("totalGram")
            each_gram_sum = 0
            for i, (gram, _) in enumerate(gram_price_group):
                each_gram_sum += gram
                # gram_price_group[i][1] = round(gram/each_gram_sum*rpg*total_gram, 2)
            total_gram = max(total_gram, each_gram_sum)
            # rpg_inland = inland_postage / total_gram
            total_price = total_gram * rpg + inland_postage
            for i, (gram, price) in enumerate(gram_price_group):
                gram_price_group[i][1] = round(gram / each_gram_sum * total_price, 2)
            # 更新到data中
            each_gram_updata = {}
            index = 0
            for key in each_gram.keys():
                each_gram_updata[key] = gram_price_group[index]
                index += 1
            item["eachGram"] = each_gram_updata
    # 写回json中
    with open(json_path, "w", encoding="utf-8-sig") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


# 类：主窗口
class Mainwindows(QMainWindow, Ui_Postage_Calculation_MainWindow):
    def __init__(self, parent=None):
        super(Mainwindows, self).__init__(parent)
        self.setupUi(self)

        # 绑定事件
        self.btn_NewProject.clicked.connect(self.NewProject)
        self.btn_LoadData.clicked.connect(self.LoadData)
        self.btn_PrintFinTab.clicked.connect(self.PrintFinTab)
        self.btn_ReCount.clicked.connect(self.ReCount)
        self.btn_Save.clicked.connect(self.SaveData)
        self.btn_ReCountAll.clicked.connect(self.ReCountAll)
        self.btn_NewGood.clicked.connect(self.NewGood)
        self.btn_DelGood.clicked.connect(self.DelGood)
        self.btn_AddLine.clicked.connect(self.AddLine)
        self.btn_DelLine.clicked.connect(self.DelLine)
        self.btn_CleanSearch.clicked.connect(self.CleanSearch)
        self.btn_SaveFinaTab.clicked.connect(self.SaveFinTab)
        self.list_mNum.itemDoubleClicked.connect(self.onItemDoubleClicked)
        self.list_mNum.itemClicked.connect(self.onItemDoubleClicked)
        self.edit_Search.setPlaceholderText("搜索内容...")
        self.edit_Search.textChanged.connect(self.Search)

        # 类变量
        self.file_path = None
        self.json_path = None
        self.goodID_list = []

    # 创建项目
    def NewProject(self):
        try:
            json_path, _ = QFileDialog.getSaveFileName(
                self, "选择路径", filter="Json文件(*.json)"
            )
            if json_path:
                if not json_path.endswith(".json"):
                    json_path += ".json"
                self.json_path = json_path
            else:
                return
        except Exception as e:
            QMessageBox.information(self, "警告", str(e))
        # 初始化json元数据
        base_info = {"isCountPostage": False, "rpg": 0.12, "inlandPostage": 2.00}
        json_list = []
        json_list.append(base_info)
        with open(self.json_path, "w", encoding="utf-8-sig") as jsonfile:
            json.dump(json_list, jsonfile, ensure_ascii=False, indent=4)

    # 导入数据
    def LoadData(self):
        self.list_mNum.clear()
        self.tab_Details.setRowCount(0)
        self.tab_FineTab.setRowCount(0)
        self.edit_InlandPost.clear()
        self.edit_rpg.clear()
        self.edit_TotalGram.clear()

        self.file_path = None
        self.json_path = None
        try:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter(
                "Excel文件(*.xlsx);;CSV文件(*.csv);;Json文件(*.json);;所有格式(*)"
            )
            if file_dialog.exec():
                self.file_path = file_dialog.selectedFiles()[0]
                name_filter = file_dialog.selectedNameFilter()
                if "Json" in name_filter:
                    # JSON项目
                    self.json_path = file_dialog.selectedFiles()[0]
                else:
                    # 创建json文件
                    base_name = os.path.basename(self.file_path)
                    file_name, _ = os.path.splitext(base_name)
                    json_path = os.path.join(
                        os.path.dirname(self.file_path), file_name + ".json"
                    )
                    self.json_path = json_path
                    if os.path.exists(json_path):
                        response = QMessageBox.question(
                            self,
                            "文件存在",
                            "当前目录下已存在项目文件，是否覆盖？",
                            QMessageBox.StandardButton.Yes
                            | QMessageBox.StandardButton.No,
                        )
                        if response == QMessageBox.StandardButton.Yes:
                            with open(json_path, "w") as json_file:
                                json_file.write("{}")
                        else:
                            return
                    else:
                        with open(json_path, "w") as json_file:
                            json_file.write("{}")
                    # 读取原数据
                    if "Excel" in name_filter:
                        # excel文件，转为csv
                        df = pd.read_excel(self.file_path)
                        csv_file_path = os.path.join(
                            os.path.dirname(self.file_path),
                            os.path.splitext(os.path.basename(self.file_path))[0]
                            + ".csv",
                        )
                        df.to_csv(csv_file_path, index=False, encoding="utf-8-sig")
                        self.file_path = csv_file_path
                    # 将csv数据转为json数据
                    GetFromCsv(self.file_path, self.json_path)
                # 从json文件中读取并写入控件
                with open(self.json_path, "r", encoding="utf-8-sig") as jsonfile:
                    data = json.load(jsonfile)
                    for item in data:
                        goodID = item.get("goodID")
                        if goodID:
                            self.list_mNum.addItem(goodID)
                            self.goodID_list.append(goodID)
                    self.edit_rpg.setText(str(data[0].get("rpg")))
                    self.edit_InlandPost.setText(str(data[0].get("inlandPostage")))
                    self.edit_BoxID.setText(str(data[0].get("BoxID")))
                    if data[0].get("isCountPostage") == False:
                        response = QMessageBox.question(
                            self,
                            "提示",
                            "邮费未计算，是否立刻进行计算？",
                            QMessageBox.StandardButton.Yes
                            | QMessageBox.StandardButton.No,
                        )
                        if response == QMessageBox.StandardButton.Yes:
                            # 重算所有
                            CountAll(self.json_path)
                        else:
                            QMessageBox.information(
                                self, "提示", "邮费未计算，请在生成总表前重新计算邮费"
                            )
                    QMessageBox.information(self, "提示", "导入完成")
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))

    # 另存为(未完成)
    def SaveData(self):
        file_path = None
        try:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("CSV文件(*.csv);;Excel文件(*.xlsx);;所有格式(*)")
            if file_dialog.exec():
                file_path = file_dialog.selectedFiles()[0]
                name_filter = file_dialog.selectedNameFilter()
                if "Excel" in name_filter:
                    # 保存为excel
                    pass
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))

    # 重算所有订单
    def ReCountAll(self):
        # 更新rpg和inlandPostage
        with open(self.json_path, "r", encoding="utf-8-sig") as jsonfile:
            data = json.load(jsonfile)
        for item in data:
            if item.get("rpg"):
                item["rpg"] = float(self.edit_rpg.text())
                item["inlandPostage"] = float(self.edit_InlandPost.text())
                item["BoxID"] = self.edit_BoxID.text()
        # 写回json中
        with open(self.json_path, "w", encoding="utf-8-sig") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        CountAll(self.json_path)
        QMessageBox.information(self, "提示", "邮费信息已更新")
        self.tab_Details.setRowCount(0)

    # 重算当前订单
    def ReCount(self):
        with open(self.json_path, "r", encoding="utf-8-sig") as jsonfile:
            data = json.load(jsonfile)
        for item in data:
            if item.get("rpg"):
                rpg = item.get("rpg")
                inland_postage = item.get("inlandPostage")
        # 重算
        total_gram = float(self.edit_TotalGram.text())
        each_gram_sum = 0
        for i in range(self.tab_Details.rowCount()):
            each_gram_sum += float(self.tab_Details.item(i, 1).text())
        total_gram = max(total_gram, each_gram_sum)
        total_price = total_gram * rpg + inland_postage
        for i in range(self.tab_Details.rowCount()):
            self.tab_Details.setItem(
                i,
                2,
                QTableWidgetItem(
                    f"{round(float(self.tab_Details.item(i, 1).text()) / each_gram_sum * total_price,2)}"
                ),
            )
        # 更新json
        goodID = self.list_mNum.selectedItems()[0].text()
        each_gram_list = {}
        for i in range(self.tab_Details.rowCount()):
            cn = self.tab_Details.item(i, 0).text()
            gram = float(self.tab_Details.item(i, 1).text())
            price = float(self.tab_Details.item(i, 2).text())
            gram_price_group = [gram, price]
            each_gram_list[cn] = gram_price_group
        for item in data:
            if item.get("goodID") == goodID:
                item["totalGram"] = round(float(total_gram), 2)
                item["eachGram"] = each_gram_list
        with open(self.json_path, "w", encoding="utf-8-sig") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        item = self.list_mNum.selectedItems()[0]
        self.onItemDoubleClicked(item)

    # 生成总表
    def PrintFinTab(self):
        self.tab_FineTab.setRowCount(0)
        with open(self.json_path, "r", encoding="utf-8-sig") as jsonfile:
            data = json.load(jsonfile)
        each_gram_group = []
        cn_group = []
        gram_group = []
        price_group = []
        for item in data:
            if item.get("goodID"):
                each_gram_group.append(item.get("eachGram"))
        for each_group in each_gram_group:
            for cn, gram_price_group in each_group.items():
                gram, price = gram_price_group
                try:
                    # cn存在
                    cn_index = cn_group.index(cn)
                    gram_group[cn_index] += gram
                    price_group[cn_index] += price
                except:
                    cn_group.append(cn)
                    gram_group.append(gram)
                    price_group.append(price)
        self.tabWidget.setCurrentIndex(1)
        tab_index = 0
        for cn, gram, price in zip(cn_group, gram_group, price_group):
            gram = f"{gram:.2f}"
            price = f"{price:.2f}"
            self.tab_FineTab.insertRow(self.tab_FineTab.rowCount())
            self.tab_FineTab.setItem(
                self.tab_FineTab.rowCount() - 1, 0, QTableWidgetItem(cn)
            )
            self.tab_FineTab.setItem(
                self.tab_FineTab.rowCount() - 1, 1, QTableWidgetItem(gram)
            )
            self.tab_FineTab.setItem(
                self.tab_FineTab.rowCount() - 1, 2, QTableWidgetItem(price)
            )

    # 导出总表
    def SaveFinTab(self):
        try:
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "选择路径",
                directory=f"{os.path.join(os.path.dirname(self.json_path),self.edit_BoxID.text())}总表.csv",
                filter="CSV文件(*.csv)",
            )
            if save_path:
                if not save_path.endswith(".csv"):
                    save_path += ".csv"
                with open(save_path, "w", newline="", encoding="utf-8-sig") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    for rowindex in range(self.tab_FineTab.rowCount() - 1):
                        csvwriter.writerow(
                            [
                                self.tab_FineTab.item(rowindex, 0).text(),
                                self.tab_FineTab.item(rowindex, 1).text(),
                                self.tab_FineTab.item(rowindex, 2).text(),
                            ]
                        )
        except Exception as e:
            QMessageBox.warning(self, "警告", f"保存失败。{str(e)}")

    # list双击事件
    def onItemDoubleClicked(self, item):
        with open(self.json_path, "r", encoding="utf-8-sig") as jsonfile:
            data = json.load(jsonfile)
        for jsonitem in data:
            if jsonitem.get("goodID") == item.text():
                gooditem = jsonitem
        self.edit_TotalGram.setText(str(gooditem["totalGram"]))
        self.tab_Details.setRowCount(0)
        each_gram = gooditem.get("eachGram", {})
        self.tab_Details.setRowCount(len(each_gram))
        for index, (key, value_price) in enumerate(each_gram.items()):
            self.tab_Details.setItem(index, 0, QTableWidgetItem(key))
            self.tab_Details.setItem(
                index, 1, QTableWidgetItem(f"{value_price[0]:.2f}")
            )
            self.tab_Details.setItem(
                index, 2, QTableWidgetItem(f"{value_price[1]:.2f}")
            )

    # 新建订单
    def NewGood(self):
        try:
            if self.json_path == None:
                return
            goodID, ok = QInputDialog.getText(
                self, "商品ID", "请输入ID", QLineEdit.EchoMode.Normal
            )
            if ok:
                good_json = Goods_json(mNum=goodID)
                with open(self.json_path, "r", encoding="utf-8-sig") as jsonfile:
                    data = json.load(jsonfile)
                data.append(good_json.info_json)
                with open(self.json_path, "w", encoding="utf-8-sig") as jsonfile:
                    json.dump(data, jsonfile, ensure_ascii=False, indent=4)
                self.list_mNum.addItem(goodID)
                self.goodID_list.append(goodID)
                items = self.list_mNum.findItems(goodID, Qt.MatchFlag.MatchExactly)
                if items:
                    current_item = self.list_mNum.currentItem()
                    if current_item:
                        current_item.setSelected(False)
                    items[0].setSelected(True)
                item = self.list_mNum.selectedItems()[0]
                self.list_mNum.scrollToItem(
                    item, QAbstractItemView.ScrollHint.EnsureVisible
                )
                self.onItemDoubleClicked(item)
                self.AddLine()
        except Exception as e:
            QMessageBox.warning(self, "警告", str(e))

    # 删除订单
    def DelGood(self):
        try:
            reponse = QMessageBox.question(
                self,
                "删除",
                "删除后不可恢复！确定要删除吗？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if reponse == QMessageBox.StandardButton.Yes:
                self.tab_Details.setRowCount(0)
                item = self.list_mNum.selectedItems()[0]
                goodID_Del = item.text()
                self.goodID_list.remove(goodID_Del)
                self.list_mNum.takeItem(self.list_mNum.row(item))
                with open(self.json_path, "r", encoding="utf-8-sig") as jsonfile:
                    data = json.load(jsonfile)
                data = [item for item in data if item.get("goodID") != goodID_Del]
                with open(self.json_path, "w", encoding="utf-8-sig") as jsonfile:
                    json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        except Exception as e:
            QMessageBox.warning(self, "警告", str(e))

    # 添加行
    def AddLine(self):
        if self.list_mNum.selectedItems():
            self.tab_Details.insertRow(self.tab_Details.rowCount())

    # 删除行
    def DelLine(self):
        if self.list_mNum.selectedItems():
            row = self.tab_Details.currentRow()
            if row == -1:
                row = self.tab_Details.rowCount() - 1
            if self.tab_Details.item(row, 0) != None:
                cn = self.tab_Details.item(row, 0).text()
                response = QMessageBox.question(
                    self,
                    "删除",
                    f"您即将删除cn为“{cn}”的行，删除后不可恢复！确定要删除吗？",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                )
                if response == QMessageBox.StandardButton.Yes:
                    self.tab_Details.removeRow(row)
            else:
                self.tab_Details.removeRow(row)

    # 清空搜索框
    def CleanSearch(self):
        self.edit_Search.clear()

    # 搜索
    def Search(self, text):
        self.list_mNum.clear()
        for item in self.goodID_list:
            if text in item:
                self.list_mNum.addItem(QListWidgetItem(item))


# 类：json格式化
class Goods_json:
    def __init__(self, mNum, total_gram=0, cn_group=[], gram_group=[]):
        self.info_json = None
        gram_group = [[weight, 0] for weight in gram_group]
        customer_prices = dict(zip(cn_group, gram_group))
        self.info_json = {
            "goodID": mNum,
            "totalGram": total_gram,
            "eachGram": customer_prices,
        }


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindows = Mainwindows()
    mainwindows.show()
    sys.exit(app.exec())
