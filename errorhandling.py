# Figure out how to show line numbers which caused errors
import sys
import logging

def error_handling():
    return 'Error Type: {}. Description: {}, line: {}'.format(sys.exc_info()[0],
                                    sys.exc_info()[1],
                                    sys.exc_info()[2].tb_lineno)

try:
    a+b
except Exception as e:
    # print(sys.exc_info()[0]) # sys.exc_info() returns a tuple of info
    # print(sys.exc_info()[0])
    # print(sys.exc_info()[1])
    # print(sys.exc_info()[2].tb_lineno) # Print the line number of failure
    logging.error(error_handling())
