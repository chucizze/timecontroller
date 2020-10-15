# 用于处理mysql中文的存储
table_args = {
     'mysql_engine': 'InnoDB',
     'mysql_charset': 'utf8'
 }
# 用于测试的服务器和端口，注意这里不能用http://
httpserver = "127.0.0.1"
httpport = "5000"
bind_ip='0.0.0.0'
# 用于日志配置
formatstr = "%(asctime)s\t%(name)s\t%(pathname)s\t%(lineno)d\t%(message)s\t%(funcName)s\t%(levelname)s"
logdir = "log"
loggername = "timecontroller"