# 执行cmd
import subprocess


def test_subprocess():
    result = subprocess.getstatusoutput("ls")
    print(result, type(result))


# 执行空串命令的结果：(0, '')
def test_execute_blank_cmd():
    result = subprocess.getstatusoutput('')
    print(result)


test_subprocess()
