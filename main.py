# -------------------------
# Made by qf
# 2025-08-21
# -------------------------

import os  # 导入os模块
from datetime import datetime  # 导入datetime模块

def rename_files_in_directory(directory, filter_names, mode='independent'):
    """文件重命名核心函数
    参数：
    directory - 目标目录路径
    filter_names - 需要过滤的文件名列表
    mode - 处理模式（independent/merged/sequential）
    """
    # 获取目录中所有文件的列表，排除过滤文件名
    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f not in filter_names]
    
    if mode == 'independent':
        # 独立模式：按文件类型分组后分别处理
        extensions = sorted(set(f.split('.')[-1] for f in all_files))  # 获取不重复的扩展名列表
        for extension in extensions:
            files = [f for f in all_files if f.split('.')[-1] == extension]  # 按扩展名过滤文件
            file_timestamps = {}
            for file in files:
                timestamp_str = '.'.join(file.split('.')[:-1])  # 提取文件名中的时间戳部分
                try:
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H-%M-%S')  # 解析时间戳
                    file_timestamps[file] = timestamp
                except ValueError:
                    print(f"文件名格式错误: {file}")  # 时间戳格式异常处理
            sorted_files = sorted(file_timestamps, key=file_timestamps.get)  # 按时间排序文件
            for index, file in enumerate(sorted_files, start=1):
                new_file_name = f"{extension}_{index}.{extension}"  # 生成新文件名（类型_序号.扩展名）
                old_file_path = os.path.join(directory, file)
                new_file_path = os.path.join(directory, new_file_name)
                os.rename(old_file_path, new_file_path)  # 执行文件重命名
                print(f"已重命名: {old_file_path} -> {new_file_path}")
    
    elif mode == 'merged':
        # 合并所有文件并按时间戳排序
        file_timestamps = {}
        for file in all_files:
            timestamp_str = '.'.join(file.split('.')[:-1])
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H-%M-%S')
                file_timestamps[file] = timestamp
            except ValueError:
                print(f"文件名格式错误: {file}")
        sorted_files = sorted(file_timestamps, key=file_timestamps.get)
        for index, file in enumerate(sorted_files, start=1):
            extension = file.split('.')[-1]
            new_file_name = f"{extension}_{index}.{extension}"
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"已重命名: {old_file_path} -> {new_file_path}")
    
    elif mode == 'sequential':
        # 按文件后缀排序，再按时间戳排序，并为每种文件类型分配独立的编号序列
        extensions = sorted(set(f.split('.')[-1] for f in all_files))
        for extension in extensions:
            files = [f for f in all_files if f.split('.')[-1] == extension]
            file_timestamps = {}
            for file in files:
                timestamp_str = '.'.join(file.split('.')[:-1])
                try:
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H-%M-%S')
                    file_timestamps[file] = timestamp
                except ValueError:
                    print(f"文件名格式错误: {file}")
            sorted_files = sorted(file_timestamps, key=file_timestamps.get)
            for index, file in enumerate(sorted_files, start=1):
                new_file_name = f"{extension}_{index}.{extension}"
                old_file_path = os.path.join(directory, file)
                new_file_path = os.path.join(directory, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"已重命名: {old_file_path} -> {new_file_path}")

directory_path = r'j:\Files\Video\服务器生存' # 目录路径
filter_names = ['process.py', 'start.bat'] # 过滤文件名

mode_id = 'sequential' # 模式标识

rename_files_in_directory(directory_path, filter_names, mode=mode_id) # 文件处理

#rename_files_in_directory(directory_path, filter_names, mode='independent') # 独立文件处理
#rename_files_in_directory(directory_path, filter_names, mode='merged') # 合并文件处理
#rename_files_in_directory(directory_path, filter_names, mode='sequential') # 顺并文件处理