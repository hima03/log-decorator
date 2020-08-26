import logDecorator
import log


class Calculator():
    def __init__(self, first=0, second=0, log_file_name='', log_file_dir=''):
        self.first = first
        self.second = second
        #log file name and directory which we want to keep
        self.log_file_name = log_file_name
        self.log_file_dir = log_file_dir
        # Initializing logger object to write custom logs
        self.logger_obj = log.get_logger(log_file_name=self.log_file_name, log_sub_dir=self.log_file_dir)

    @logDecorator.log_decorator()
    def add(self, third=0, fourth=0):
        # writing custom logs specific to function, outside of log decorator, if needed
        self.logger_obj.info("Add function custom log, outside decorator")
        try:
            return self.first + self.second + third + fourth
        except:
            raise

    @logDecorator.log_decorator()
    def subtract(self):
        self.logger_obj.info("Add function custom log, outside decorator")
        try:
            return self.first - self.second
        except:
            raise

    @logDecorator.log_decorator()
    def multiply(self):
        self.logger_obj.info("Add function custom log, outside decorator")
        try:
            return self.first * self.second
        except:
            raise

    @logDecorator.log_decorator()
    def divide(self):
        self.logger_obj.info("Add function custom log, outside decorator")
        try:
            return self.first / self.second
        except:
            raise


if __name__ == '__main__':
    obj = Calculator(5, 0, 'calculator_file', 'calculator_dir')
    obj.add(2,3)
    obj.divide()
