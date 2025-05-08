def process_numbers_file(input_path, output_path=None):
    # 读取输入文件
    with open(input_path, 'r') as f:
        # 读取所有行并去除空白字符
        lines = [line.strip() for line in f.readlines()]
    
    # 过滤掉非数字的行
    numbers = [line for line in lines if line.isdigit()]
    
    # 将数字用逗号连接成一行
    result = ','.join(numbers)
    
    # 如果指定了输出路径，则写入文件
    if output_path:
        with open(output_path, 'w') as f:
            f.write(result)
        print(f"结果已保存到 {output_path}")
    else:
        # 否则打印到控制台
        print(result)
    
    return result

# 指定文件路径
input_file = '/sharefiles3/heyuxuan/tmp/a.js'
# 可以选择性地指定输出文件路径
output_file = '/sharefiles3/heyuxuan/tmp/a_processed.js'

# 处理文件
process_numbers_file(input_file, output_file)