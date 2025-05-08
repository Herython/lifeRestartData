import time

# 获取当前时间戳（秒级）
timestamp_seconds = int(time.time())
print(timestamp_seconds)

# 获取毫秒级时间戳
timestamp_milliseconds = int(time.time() * 1000)
print(timestamp_milliseconds)