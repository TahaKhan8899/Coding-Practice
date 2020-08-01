def reverseString(str):

    return ' '.join([word[::-1] for word in str.split()])


def test1():
    str = "hello"

    print(reverseString(str))


test1()
