import pandas as pd
import re
import os

# ==================== 配置文件路径 ====================
# 请确保这是你的实际文件路径
file_path = r'D:\邱维俊\潮汐模拟系统\模拟潮汐\SaveWindows2025_8_21_15-31-07.TXT'

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"❌ 文件未找到：{file_path}")
    print("请检查路径是否正确，或把文件放在脚本同一目录")
    exit()

# ==================== 尝试多种编码读取文件 ====================
def read_with_encoding(file_path):
    encodings = ['gbk', 'utf-8', 'latin1']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                content = f.read()
            print(f"✅ 使用编码 '{enc}' 成功读取文件")
            return content
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"❌ 读取失败：{e}")
            return None
    print("❌ 所有编码尝试失败")
    return None

content = read_with_encoding(file_path)
if content is None:
    exit()

# ==================== 解析时间和水位（关键修正）====================
data = []

# 按行处理
lines = content.split('\n')
for line in lines:
    line = line.strip()
    if not line or 'END' not in line:
        continue  # 跳过空行或无效行

    # 提取时间戳 [HH:MM:SS.fff]
    time_match = re.search(r'\[(\d{2}:\d{2}:\d{2}\.\d{3})\]', line)
    if not time_match:
        continue

    # 提取所有浮点数（支持负数）
    values = re.findall(r'-?\d+\.\d+', line)
    if len(values) < 2:
        continue  # 至少要有两个数值

    timestamp = time_match.group(1)

    # ✅ 修正：从数据分析，第3个数值（索引为2）才是水位！
    # 格式: [时间]设备,误差,水位,变化率,...
    # 示例: [15:30:35.577]...,3.16,3.17,3.13 → 水位是 3.17（即 values[1]）
    #
    # 但注意：在最后阶段，水位跳变到 66.45，且稳定不变
    # 所以我们确定：第2个浮点数（values[1]）是真实水位
    water_level = float(values[1])

    data.append([timestamp, water_level])

# ==================== 创建 DataFrame ====================
df = pd.DataFrame(data, columns=['时间', '水位'])

# ==================== 保存为 Excel 文件（同目录）====================
# 构造输出路径：原文件名 + “_水位数据.xlsx”
output_path = file_path.rsplit('.', 1)[0] + '_水位数据.xlsx'

try:
    df.to_excel(output_path, index=False, engine='openpyxl')
    print(f"\n🎉 数据已成功保存为 Excel 文件：")
    print(f"📄 {output_path}")
    print(f"📊 共 {len(df)} 行数据")
    print(f"📈 水位范围：{df['水位'].min():.2f} ~ {df['水位'].max():.2f}")
except Exception as e:
    print(f"❌ 保存 Excel 失败：{e}")