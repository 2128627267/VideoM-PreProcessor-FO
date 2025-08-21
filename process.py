# -------------------------
# Made by qf
# 2025-08-21
# -------------------------

import os  # 导入os模块
from datetime import datetime  # 导入datetime模块

def rename_files_in_directory(directory, filter_names):  # 定义函数，接受目录路径和脚本文件名作为参数
    # 获取目录中所有文件的列表，排除过滤文件名
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f not in filter_names]  # 获取所有文件
    
    # 创建一个字典来存储文件名及其时间戳
    file_timestamps = {}  # 初始化字典
    
    for file in files:  # 遍历文件列表
        # 提取文件后缀
        extension = file.split('.')[-1]  # 提取文件后缀
        # 从文件名中提取时间戳
        timestamp_str = file.split('.')[0]  # 提取时间戳字符串
        try:
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H-%M-%S')  # 将时间戳字符串转换为datetime对象
            file_timestamps[file] = timestamp  # 存储文件名和时间戳
        except ValueError:
            print(f"文件名格式错误: {file}")  # 处理时间戳格式错误的情况
    
    # 按照时间戳排序
    sorted_files = sorted(file_timestamps, key=file_timestamps.get)  # 根据时间戳排序文件
    
    # 重命名文件
    for index, file in enumerate(sorted_files, start=1):  # 遍历排序后的文件列表
        # 提取文件后缀
        extension = file.split('.')[-1]  # 提取文件后缀
        # 创建新的文件名
        new_file_name = f"{extension}_{index}.{extension}"  # 生成新的文件名
        # 拼接完整路径
        old_file_path = os.path.join(directory, file)  # 生成旧文件的完整路径
        new_file_path = os.path.join(directory, new_file_name)  # 生成新文件的完整路径
        # 重命名文件
        os.rename(old_file_path, new_file_path)  # 重命名文件
        print(f"已重命名: {old_file_path} -> {new_file_path}")  # 打印重命名信息

# 使用示例，替换为你自己的目录路径
directory_path = r'j:\Files\Video\服务器生存'  # 重命名路径
filter_names = ['process.py', 'start.bat']  # 过滤文件名列表
rename_files_in_directory(directory_path, filter_names)  # 调用函数进行重命名操作
