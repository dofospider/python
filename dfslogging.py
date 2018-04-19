import os
import logging
import datetime

try:
    if not os.path.exists('log'):
        raise IOError("no have dir")
except IOError:
    os.mkdir('log')
log_file = './log/%s.log ' % datetime.date.today()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # datefmt='%a, %d %b %Y %H:%M:%S',
                    datefmt='%Y %b %d %H:%M:%S',
                    filename=log_file,
                    filemode='a+',)

logger = logging.getLogger(__name__)

#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################
