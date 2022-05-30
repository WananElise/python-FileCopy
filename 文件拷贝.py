"""

任何文件的底层都是二进制的 因此不管是音频 图片 通过编译器文件操作
二进制读取 可以进行拷贝

"""
# 1.获取文件对象,关联 数据源文件
src_name = str(input("请输入您要拷贝的文件路径"))
# 1.1 截取文件名 并判断是否合法
index = src_name.rfind('.')
if index == 0:
    print("录入的文件路径不合法")
else:
    try:
        src_f = open(src_name, 'rb')  # 以二进制方式读取
    except Exception as e:
        print(f"Find a BUG>>{e}")
    else:
        dest_name = src_name[:index] + "[备份]" + src_name[index:]
    # 2. 获取文件对象, 关联 目的地文件
        dest_f = open(dest_name, 'wb')  # 以二进制方式写入
    # 3.采用while循环一次读取1024个字节防止拓机 然后写入
        while True:
            buf = src_f.read(1024)
            if len(buf) == 0:
                break
            dest_f.write(buf)
            print("文件拷贝成功")
            # 4.释放资源
            src_f.close()
            dest_f.close()
