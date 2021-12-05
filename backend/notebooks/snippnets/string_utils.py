def trim(s):
    if len(s) == 0:
        return s
    for i in range(len(s)):
        if s[i] != ' ':
            break
    for j in range(len(s)):
        if s[-1-j] != ' ':
            break
    # print(s[i:len(s)-j])
    # print(len(s[i:len(s)-j]))
    return s[i:len(s)-j]


if __name__ == "__main__":
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')