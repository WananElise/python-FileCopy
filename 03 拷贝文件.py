"""
文件拷贝:
    所谓的拷贝指的就是备份文件或者拷贝文件
思路:
    1.获取文件对象 关联 数据源
    2.获取文件对象 关联 目的地文件
    3.具体实现过程
    4.释放资源


"""
# src_name = str(input("请输入您要备份的文件名"))
# index = src_name.rfind('.')
# dest_name = src_name[:index] + "[备份]" + src_name[index:]
# print(dest_name)

# 拷贝文件操作:
# 1.获取文件对象 关联 数据源
src_name = str(input("请输入您要备份的文件名"))
src_f = open(src_name,'r',encoding='utf-8')
# 2.获取文件对象 关联 目的地文件
index = src_name.rfind('.')
dest_name = src_name[:index] + "[备份]" + src_name[index:]
# 3.获取文件对象
dest_f = open(dest_name,'w',encoding='utf-8')
# 开始拷贝

# 方式1: 一次读取所有然后全部写入
# deta = src_f.read()
# len = dest_f.write(deta)

# 方式2: 读取所有行写入所有行
# lines = src_f.readlines()
# len = dest_f.writelines(lines)

# 方式3: 一次读取一定的长度然后写入
#因为上述方式都是一次性读取所有数据 如果文件内容过大
# 一次读取所有的数据容易造成宕机的风险
while True:
    # 一次读取1024个字符
    deta = src_f.read(1024)
    dest_f.write(deta)
    if len(deta) == 0:
        break





# 4.释放资源

print(f"备份成功,当前备份{len}个字节")
dest_f.close()
src_f.close()


