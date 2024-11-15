import json

# 类：json文件操作
class ProjectJson:
    def __init__(self, filepath: str = ""):
        try:
            with open(filepath, "a") as file:
                pass
        except Exception as e:
            pass
        self.filepath = filepath
        self.InitializationFile()

    # json文件初始化
    def InitializationFile(self):
        filepath = self.filepath
        lst_cn = [
            {
                "nickname": "vx名",
                "note": "备注",
                "goodName": "商品名称(相卡批次)",
                "goodType": "相卡分类(具体编号)",
                "goodNum": "数量",
                "isGet": False,
            }
        ]
        data = {"cn": lst_cn}
        data = {"data": data}
        self.data = data
        self.SaveDataToFile()

    # 添加数据
    def AddData(
        self,
        cn: str,
        nickname: str,
        note: str,
        goodName: str,
        goodType: str,
        goodNum: int,
        isGet: bool = False,
    ):
        dataAdd = {
            "nickname": nickname,
            "note": note,
            "goodName": goodName,
            "goodType": goodType,
            "goodNum": goodNum,
            "isGet": isGet,
        }
        data = self.data["data"]
        data_cn = data.get(cn)
        if data_cn:
            data_cn.append(dataAdd)
        else:
            dataAdd = [dataAdd]
            data[cn] = dataAdd

        self.data["data"] = data
        self.SaveDataToFile()

    # 修改cn
    def ChangeCn(self, cn_old: str, cn_new: str):
        data = self.data["data"]
        data_cn = data.get(cn_old)
        if data_cn:
            data[cn_new] = data.pop(cn_old)
        self.data["data"] = data
        self.SaveDataToFile()

    # 移动数据
    def MoveData(
        self,
        cn_old: str,
        cn_new: str,
        nickname: str,
        note: str,
        goodName: str,
        goodType: str,
        goodNum: int,
        isGet: bool,
    ):
        data = self.data["data"]
        data_cn_old = data.get(cn_old)
        if data_cn_old:
            for index, item in enumerate(data_cn_old):
                if (item['nickname'] == nickname and
                    item['note'] == note and
                    item['goodName'] == goodName and
                    item['goodType'] == goodType and
                    item['goodNum'] == goodNum and
                    item['isGet'] == isGet):
                    continue
            data_cn_old.pop(index)
            data[cn_old] = data_cn_old
            self.data["data"] = data
            self.AddData(cn = cn_new, **item)
            #AddData()中有同步数据的代码，因此这里不需要再重复同步一次

    # 保存到文件
    def SaveDataToFile(self):
        try:
            with open(self.filepath, "w", encoding="utf-8-sig") as file:
                json.dump(self.data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            pass