import log_decorator
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

    @log_decorator.log_decorator()
    def add(self, third=0, fourth=0):
        # writing custom logs specific to function, outside of log decorator, if needed
        self.logger_obj.info("Add function custom log, outside decorator")
        try:
            return self.first + self.second + third + fourth
        except:
            raise

    @log_decorator.log_decorator()
    def divide(self):
        self.logger_obj.info("Divide function custom log, outside decorator")
        try:
            return self.first / self.second
        except:
            raise

if __name__ == '__main__':
    calculator = Calculator(5, 0, 'calculator_file', 'calculator_dir')
    calculator.add(third=2,fourth=3)
    calculator.divide()
