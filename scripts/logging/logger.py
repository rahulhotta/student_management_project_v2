# import logging
# import os
# from logging import StreamHandler
# from logging.handlers import RotatingFileHandler, SocketHandler

# import yaml

# # this method is to read the configuration from backup.conf
# # from scripts.config import Logging


# def read_configuration(file_name):
#     """
#     :param file_name:
#     :return: all the configuration constants
#     """
#     with open(file_name) as stream:
#         try:
#             return yaml.safe_load(stream)
#         except Exception as e:
#             print(f"Failed to load Configuration. Error: {e}")


# # config = read_configuration("scripts/logging/logger_conf.yml")



# def get_logger():
#     """
#     Creates a rotating log
#     """
#     __logger__ = logging.getLogger("")
#     __logger__.setLevel("info".upper())
#     log_formatter = "%(asctime)s - %(levelname)-6s - [%(threadName)5s:%(funcName)5s():" "" "%(lineno)s] - %(message)s"
#     time_format = "%Y-%m-%d %H:%M:%S"
#     formatter = logging.Formatter(log_formatter, time_format)


#     log_file = "logs/app.log"
#     temp_handler = RotatingFileHandler(
#         log_file, maxBytes=1000000, backupCount=5
#     )
#     temp_handler.setFormatter(formatter)
#     __logger__.addHandler(temp_handler)
#     __logger__.addHandler(StreamHandler().setFormatter(formatter))

#     return __logger__


# logger = get_logger()