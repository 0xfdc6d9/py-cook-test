# isblank的写法
def test_str_blank(a: str):
    print('yes' if a.isspace() or len(a) == 0 else 'no')


test_str_blank('')
test_str_blank('   ')
test_str_blank(' a')
