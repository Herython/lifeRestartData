import json
import random
import time
from datetime import datetime

def process_file(input_path, output_path, reference_path):
    # 读取输入文件中的数字
    with open(input_path, 'r') as f:
        numbers = [line.strip() for line in f.readlines()]
    
    # 过滤掉非数字的行
    numbers = [int(line) for line in numbers if line.isdigit()]
    print(f"输入文件中的数字总数: {len(numbers)}")
    
    # 读取参考文件以获取已使用的编号
    with open(reference_path, 'r') as f:
        data = json.load(f)
    
    # 提取已经使用过的编号
    used_ids = []
    if 'ACHV' in data:
        achievement_data = data['ACHV']
        # 提取已使用的编号（第一个元素）
        if isinstance(achievement_data, list):
            used_ids = [pair[0] for pair in achievement_data if isinstance(pair, list) and len(pair) >= 2]
    
    print(f"已使用的编号数量: {len(used_ids)}")
    
    # 过滤掉已使用的编号
    available_numbers = [num for num in numbers if int(num) not in used_ids]
    print(f"可用的编号数量: {len(available_numbers)}")
    
    # 随机打乱可用编号的顺序，但使用所有编号
    random.shuffle(available_numbers)
    selected_numbers = available_numbers
    
    # 获取当前时间戳作为基础
    current_timestamp = int(time.time() * 1000)
    
    # 生成时间戳递增的对，每对之间随机间隔
    result = []
    for num in selected_numbers:
        # 随机间隔1-10秒 (1000-10000毫秒)
        random_interval = random.randint(12000, 1000000)
        current_timestamp += random_interval
        result.append([int(num), current_timestamp])
    
    # 将结果格式化为字符串
    formatted_result = ','.join([f"[{pair[0]},{pair[1]}]" for pair in result])
    
    # 输出结果
    with open(output_path, 'w') as f:
        f.write(formatted_result)
    
    human_readable_time = datetime.fromtimestamp(current_timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')
    print(f"处理完成! 已生成 {len(result)} 对数据")
    print(f"最后一个时间戳: {current_timestamp} ({human_readable_time})")
    print(f"结果已保存到 {output_path}")
    
    return formatted_result

# 指定文件路径
input_file = '/sharefiles3/heyuxuan/tmp/a.js'
output_file = '/sharefiles3/heyuxuan/tmp/result.js'
reference_file = '/sharefiles3/heyuxuan/tmp/data.js'

# 处理文件
result = process_file(input_file, output_file, reference_file)
print("\n生成的部分结果预览:")
print(result[:200] + "..." if len(result) > 200 else result)