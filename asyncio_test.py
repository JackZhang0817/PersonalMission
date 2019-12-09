import time


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            print('not')
            return
        print('[CONSUMER] Consuming %s ...' % n)
        r = '200 OK'
        time.sleep(1)


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


# c = consumer()
# produce(c)


# 基础实例

# def addlist(alist):
#     for i in alist:
#         yield i + 1
#
#
# alist = [1, 2, 3, 4]
#
# for x in addlist(alist):
#     print(x)

# def h():
#     print('To be brave')
#     yield 5
#     print('Fighting')
#
# c = h()
# c.__next__()
# c.send('Fighting')

def h():
    print('Xiao Fang')
    m = yield 5
    print(m)
    d = yield 12
    print(d)
    print('We are together')

c = h()
s = c.__next__()
print(s)
s = c.send('Fighting')
print(s)







































































































