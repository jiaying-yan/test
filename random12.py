import random

num = random.choices(1, 2)
if num == 1:
    payload = {"key1": "value1", "key2": "value2"}
    r = request.get("www.baidu.com", param=payload)
else:
    print("current num is 2")
