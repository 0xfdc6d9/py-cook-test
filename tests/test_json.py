# json 序列化与反序列化
import json


def test_json():
    # info = "{'name': 'jack', 'age': 18}"
    info = '{"name": "jack", "age": 18}'

    json_info = json.loads(info)
    print(type(json_info))  # <class 'dict'>
    print(json_info.get('name'))
    print(json_info['name'])

    str_info = json.dumps(json_info)
    print(type(str_info))  # <class 'str'>


# 可以链式调用获取内层信息
def test_json2():
    info = '{"inputUrl":"inputUrl","taskId":18,"template":{"autoRotateScreen":true,' \
           '"createUserName":"Nepenthe8","videoWidth":"1280"}}'
    json_info = json.loads(info)
    print(json_info.get('template'))
    print(json_info.get('template').get('createUserName'))


test_json2()
