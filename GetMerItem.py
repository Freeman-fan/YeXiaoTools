import requests
import os

def save_image(photo_url, product_id, index):
    # 使用product_id和序号构建文件名
    photo_filename = f"{product_id}_{index}.jpg"
    
    # 发送GET请求获取图片内容
    photo_response = requests.get(photo_url)
    
    # 检查响应状态码
    if photo_response.status_code == 200:
        # 获取当前工作目录
        current_dir = os.getcwd()
        # 构建图片的绝对路径
        photo_abspath = os.path.join(current_dir, photo_filename)
        
        # 写入图片内容到文件
        with open(photo_abspath, 'wb') as f:
            f.write(photo_response.content)
        
        # 打印图片的绝对路径
        print(f"图片保存至：{photo_abspath}")
    else:
        print(f"Failed to retrieve image, status code: {photo_response.status_code}")

# # 请求URL
# product_id_input = input("请输入商品ID: ")
# api_url = 'https://www.maetown.cn/Mobile/Mercari/GoodsDetail?id=' + product_id_input

# # 发送GET请求
# response = requests.get(api_url)

# # 检查请求是否成功
# if response.status_code == 200:
#     # 解析响应内容
#     data = response.json()
    
#     # 提取你需要的信息
#     try:
#         product_id = data.get('data', {}).get('id')
#         product_name = data.get('data', {}).get('name')
#         product_description = data.get('data', {}).get('description')
#         product_price = data.get('data', {}).get('price')
#         product_price_cny = data.get('data', {}).get('priceCNY')
#         product_status = data.get('data', {}).get('status')
#         product_photos = data.get('data', {}).get('photos', [])
#         seller_name = data.get('data', {}).get('seller', {}).get('name')
#     except Exception as e:
#         print(e)
#         exit()
    
#     # 打印提取的信息
#     print(f"商品ID: {product_id}")
#     print(f"标题: {product_name}")
#     print(f"价格: {product_price}y, 约{product_price_cny}r")
#     print(f"商品状态: {'在售' if product_status == 'on_sale' else '已售出'}")
    
#     # 提取响应数据
#     product_id = data.get('data', {}).get('id')
#     product_photos = data.get('data', {}).get('photos', [])

#     # 循环遍历图片URL列表，并为每张图片使用序号
#     for index, photo_url in enumerate(product_photos, start=1):
#         save_image(photo_url, product_id, index)
        
# else:
#     print(f"Failed to retrieve data, status code: {response.status_code}")


def GetMer(mNum):
    api_url = 'https://www.maetown.cn/Mobile/Mercari/GoodsDetail?id=' + mNum

    # 发送GET请求
    response = requests.get(api_url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析响应内容
        data = response.json()
        
        # 提取你需要的信息
        try:
            product_id = data.get('data', {}).get('id')
            product_name = data.get('data', {}).get('name')
            product_description = data.get('data', {}).get('description')
            product_price = data.get('data', {}).get('price')
            product_price_cny = data.get('data', {}).get('priceCNY')
            product_status = data.get('data', {}).get('status')
            product_photos = data.get('data', {}).get('photos', [])
            seller_name = data.get('data', {}).get('seller', {}).get('name')
        except Exception as e:
            print(e)
            exit()
        
        # 打印提取的信息
        print(f"商品ID: {product_id}")
        print(f"标题: {product_name}")
        print(f"价格: {product_price}y, 约{product_price_cny}r")
        print(f"商品状态: {'在售' if product_status == 'on_sale' else '已售出'}")
        
        # 提取响应数据
        product_id = data.get('data', {}).get('id')
        product_photos = data.get('data', {}).get('photos', [])

        # 循环遍历图片URL列表，并为每张图片使用序号
        for index, photo_url in enumerate(product_photos, start=1):
            save_image(photo_url, product_id, index)
            
    else:
        print(f"Failed to retrieve data, status code: {response.status_code}")
        