# 使用in判断键是否在字典中存在
d = {'1': 'one', '2': 'two', '3': 'three'}

print('-vf scale={}'.format(d.get('1')) if '1' in d else '')
print('#' + ('-vf scale={}'.format(d.get('0')) if '0' in d else ''))