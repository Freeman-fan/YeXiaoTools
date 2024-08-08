import csv

# 自定义错误类


class Error(Exception):
    pass


def read_csv(row):  # 处理一行信息
    dataGroup = []  # 储存该行的信息，只取前两个，并返回
    dataGroup_raw = [item for item in row]
    dataGroup = dataGroup_raw[0:2:1]
    return dataGroup


def create_group(cn, gram, cn_group, gram_group):  # 建立每一单的cn和重量列表
    # 这里使用append或者下标修改列表，不需要return具体值
    try:
        # cn存在
        cn_index = cn_group.index(cn)
        gram_group[cn_index] += int(gram)
    except ValueError:
        # cn不存在
        cn_group.append(cn)
        gram_group.append(gram)
    return


def get_fina_gram(total_gram='', gram_group=[]):  # 获取目标重量
    fina_gram = 0  # 目标重量
    auto_gram = 0  # 自动求和重量
    # 对重量列表求和
    if gram_group != []:
        for item in gram_group:
            try:
                gram_item = float(item)
            except:
                gram_item = 0
            auto_gram += gram_item
    # 选择目标重量
    if total_gram == '' and auto_gram != []:
        fina_gram = auto_gram
    elif auto_gram == [] and total_gram != '':
        fina_gram = total_gram
    elif auto_gram != [] and total_gram != '':
        fina_gram = max(auto_gram, total_gram)
    else:
        return Error("No Gram.")
    return fina_gram


def count_total_price(fina_gram):  # 计算一单的总肾额
    total_price = 0  # 该单总肾额
    total_price = fina_gram * ppg + inLand_post
    return total_price


def count_price_group(gram_group=[], total_price=0, total_gram=0):  # 计算拼盘的邮费均摊
    price_group = []  # 邮费均摊列表
    for item in gram_group:
        if item == '':
            item = 0
        price_group.append(float(item)*total_price/total_gram)
    return price_group


def add_fina_group(cn_group=[], gram_group=[], price_group=[]):  # 写入总表
    # 这里使用append或者下标修改列表，不需要return具体值
    global fina_cn_group, fina_gram_group, fina_price_group
    for cn in cn_group:
        gram = gram_group.pop(0)
        price = price_group.pop(0)
        try:
            #cn已存在
            cn_index = fina_cn_group.index(cn)
            fina_gram_group[cn_index]+=float(gram)
            fina_price_group[cn_index]+=float(price)
        except ValueError:
            #cn不存在
            fina_cn_group.append(cn)
            fina_gram_group.append(float(gram))
            fina_price_group.append(float(price))
    return


if __name__ == "__main__":  # 主程序入口
    # 可变参数
    csv_filename = "D:\Onedrive\ACGN相关\切煤代购\夜宵称重表\国内17_output.csv"
    ppg = 0.12  # 单位克重
    inLand_post = 2  # 国内均摊

    # 定义空白参数
    empty_num = 0  # 当前累计空行数
    text_num = 0  # 当前累计非空行数
    cn_group = []  # 记录cn的列表
    gram_group = []  # 记录重量的列表（与cn索引对应）
    total_gram = 0  # 总重
    m_num = ''  # m码

    fina_cn_group = []  # 总表cn
    fina_gram_group = []  # 总表重量
    fina_price_group = []  # 总表肾额
    

    with open(csv_filename, newline='', encoding='utf-8')as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            row_data = read_csv(row=row)
            # 判断是否空行
            if row_data[0] == '':
                empty_num += 1
                text_num = 0
            else:
                empty_num = 0
                text_num += 1
            # 判断是否结束循环，或结束本单
            if empty_num == 1:  # 第一个空行
                # 本单读取结束，开始计算（需要判断本单信息是否存在）
                if m_num != '':  # 判断m码是否存在
                    try:
                        gram = get_fina_gram(
                            total_gram=total_gram, gram_group=gram_group)
                    except Error as e:
                        print(e)
                        continue
                    price = count_total_price(fina_gram=gram)
                    if len(cn_group) > 1:  # 如果cn列表大于1，则为拼盘，需要计算均摊
                        price_group = count_price_group(
                            gram_group=gram_group, total_price=price, total_gram=gram)
                    else:
                        price_group = []
                        price_group.append(price)
                    add_fina_group(
                        cn_group=cn_group, gram_group=gram_group, price_group=price_group)
            if empty_num == 2:
                # 结束循环
                break
            # 正常读取信息
            if text_num == 1:  # 是m码和总重
                m_num = row_data[0]
                try:
                    total_gram = round(float(row_data[1]), 2)
                except:
                    total_gram = 0
            if text_num > 1:  # 是cn和称重
                create_group(*row_data, cn_group=cn_group,
                             gram_group=gram_group)
