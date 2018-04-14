# coding='utf-8'
# 导入定时任务模块
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from datetime import datetime
import pytz


# 导入自己的log模块
import dfslogging
# 导入os路径模块
import os.path


def print_info():
    dfslogging.logger.info('clock is ring')
    print("hello i'm clock")


def print_in_second():
    dfslogging.logger.info('dida')
    print('dida')


def clock_to_get_item():
    timez = pytz.timezone('Asia/Shanghai')
    # scheduler = BackgroundScheduler()
    scheduler = BlockingScheduler()
    scheduler.add_job(print_info, 'cron', hour=10, minute=57, )
    scheduler.add_job(print_info, 'date',
                      run_date=datetime(2018, 4, 7, 11, 44, 10),)
    # scheduler.add_job(print_in_second, 'interval', minutes=1)
    dfslogging.logger.info('strat scheduler')
    scheduler.start()
    scheduler.print_jobs()

    print(time.localtime())


if __name__ == '__main__':
    dfslogging.logging.getLogger('apscheduler.executors.default')
    clock_to_get_item()
