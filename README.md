# 视频素材预处理工具

## 简介

该项目是一个纯Python编写的视频素材预处理工具，主要功能是根据文件名中的时间戳（格式：YYYY-MM-DD HH-MM-SS）对文件进行排序并重命名，帮助用户快速整理视频素材文件。

## 适用人群

刚开始用 OBS 直接用时间戳保存录制素材而且还录一大堆的视频文件的人 & 在剪映(或其他剪辑软件)中看见一大堆素材不知道录制顺序的人 & 我

## 特性

- 自动提取文件名中的时间戳信息
- 支持三种处理模式：
  - 🗂 独立模式（independent）：按文件类型分组独立编号
  - 🔀 合并模式（merged）：所有文件统一编号
  - ➡️ 顺序模式（sequential）：按类型分组后顺序编号
- 批量重命名为统一格式：`扩展名_序号.扩展名`
- 支持排除指定文件（如脚本文件本身）
- 仅依赖Python标准库，无需额外安装依赖

## 安装

1. 确保已安装Python环境
2. 克隆或下载本项目到本地

## 使用方法

1. 打开main.py文件，修改以下参数：
   - `directory_path`：设置需要处理的文件目录
   - `filter_names`：设置需要排除的文件名列表（必须包含main.py、README.md等关键文件）
   - `mode_id`：选择处理模式（independent/merged/sequential）
2. 运行脚本：

   ```bash
   python main.py  # 更新命令
   ```

或双击运行start.bat批处理文件

## 使用示例

原文件列表：

```plainText
2025-08-21 10-30-45.mp4
2025-08-22 09-15-22.mp4
2025-08-21 14-20-10.jpg
2025-08-22 11-25-30.png
2025-08-22 11-25-30.jpg
main.py
start.bat
README.md
```

处理后文件列表(independent)：
**按时间戳排序**

```plainText
mp4_1.mp4
mp4_2.mp4
jpg_1.jpg
png_1.png
jpg_2.jpg
main.py
start.bat
README.md
```

处理后文件列表(merged)：
**按时间戳排序 按首字母排序**

```plainText
mp4_1.mp4
mp4_2.mp4
jpg_3.jpg
jpg_4.jpg
png_5.png
main.py
start.bat
README.md
```

处理后文件列表(sequential)：
**按首字母排序并按文件类型排序 按时间戳排序**

```plainText
jpg_1.jpg
jpg_2.jpg
mp4_3.mp4
mp4_4.mp4
png_5.png
main.py
start.bat
README.md
```

## 联系信息

- 项目作者：qf
- QQ：2128627267
