import orm

from models import User, Blog, Comment

import asyncio


# async def test(loop):
#     await orm.create_pool(user='root', password='ling123', db='awesome', loop=loop)
#
#     u = User(name='zhang', email='zhang@153.com', passwd='1234567890', image='about:blank')
#
#     await u.save()
#
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.run_forever()
#
# for x in test(loop):
#     pass


# def test(loop):
#     yield from orm.create_pool(user='root', password='ling123', db='awesome', loop=loop)
#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#     yield from u.save()
#
#
# for x in test(loop):
#     pass

# users = User.findAll()
# print(users)
# async def test():


async def test(loop):
    await orm.create_pool(user='root', password='ling123', db='awesome', loop=loop)

    u = User()

    u.findAll()



loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()
