import csv
import sqlite3


# 初始化数据库
def CreateDB():
    conn = sqlite3.connect("FlowusCsvDataPreprocessing\data.db")
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS products (
        m_code TEXT PRIMARY KEY,
        main_spelling TEXT,
        participation_in_splicing TEXT,
        price REAL,
        status TEXT,
        weight TEXT
    )
    """
    )
    conn.commit()
    conn.close()


# 读取csv文件并写入数据库
def ReadCsvAndWriteToDB():
    conn = sqlite3.connect("FlowusCsvDataPreprocessing\data.db")
    cursor = conn.cursor()
    # 读取csv文件
    with open(
        "FlowusCsvDataPreprocessing\切煤记录表.csv", "r", encoding="utf-8-sig"
    ) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == "m码":
                continue
            m_code = row[0]
            main_spelling = row[12]
            participation_in_splicing = row[11]
            price = row[1]
            status = row[8]
            weight = row[9]
            # 检查数据库中是否存在对应m码数据
            cursor.execute("SELECT * FROM products WHERE m_code=?", (m_code,))
            result = cursor.fetchone()
            if result:
                print(m_code, "数据已存在，跳过")
                continue
            # 插入数据
            cursor.execute(
                "INSERT INTO products VALUES (?,?,?,?,?,?)",
                (
                    m_code,
                    main_spelling,
                    participation_in_splicing,
                    price,
                    status,
                    weight,
                ),
            )
            conn.commit()
            print(
                m_code,
                main_spelling,
                participation_in_splicing,
                price,
                status,
                weight,
                "写入成功",
            )
    conn.close()


# 主程序入口
if __name__ == "__main__":
    CreateDB()
    ReadCsvAndWriteToDB()
