"""
文件操作:
    读文件




"""
# 参数1: 数据源文件路径    参数2: 模式 r(只读)     参数3: 采用什么码表
f = open('qix.txt','r',encoding='utf-8')

# 方式1:读取单个字符
# buf = f.read(1)
# buf = f.read() # 不填参数默认读取全部
# print(buf)

# 方式2: 读取一行字符
# line = f.readline()
# print(line,end='')

# 方式3: 读取所有行
lines = f.readlines()
print(lines)
for line in lines:
    print(line,end="")
f.close()
