# _*_ coding: utf-8 _*_
# @Time : 2022/09/16 10:50 AM
# @Author : Coding with cat
# @File : async_await_simple_example
# @Project : SHPythonCode

import asyncio
import time

from framewrok.utility.log_utility import ILog


# 一个真实的耗时操作，可以比如去爬取网页
def my_sleep(x):
    time.sleep(x)


async def my_task(task_name):
    ILog.debug(__file__, f'{task_name} start')
    # r = asyncio.sleep(1) # 好多教程的做法
    r = await asyncio.get_event_loop().run_in_executor(None, my_sleep, 3)
    ILog.debug(__file__, f'{task_name} end')


if __name__ == '__main__':

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = [my_task('task1'), my_task('task2')]

    loop.run_until_complete(asyncio.wait(tasks))

    loop.close()
