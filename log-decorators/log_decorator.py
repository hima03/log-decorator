import sys, os, functools
import log

def log_decorator(_func=None):
    def log_decorator_info(func):
        @functools.wraps(func)
        def log_decorator_wrapper(self, *args, **kwargs):
            # Build logger object
            logger_obj = log.get_logger(log_file_name=self.log_file_name, log_sub_dir=self.log_file_dir)

            """ Create a list of the positional arguments passed to function.
            - Using repr() for string representation for each argument. repr() is similar to str() only difference being
             it prints with a pair of quotes and if we calculate a value we get more precise value than str(). """
            args_passed_in_function = [repr(a) for a in args]
            """ Create a list of the keyword arguments. The f-string formats each argument as key=value, where the !r 
                specifier means that repr() is used to represent the value. """
            kwargs_passed_in_function = [f"{k}={v!r}" for k, v in kwargs.items()]

            """ The lists of positional and keyword arguments is joined together to form final string """
            formatted_arguments = ", ".join(args_passed_in_function + kwargs_passed_in_function)

            """ Generate file name and function name for calling function. __func.name__ will give the name of the 
                caller function ie. wrapper_log_info and caller file name ie log-decorator.py
            - In order to get actual function and file name we will use 'extra' parameter.
            - To get the file name we are using in-built module inspect.getframeinfo which returns calling file name """
            extra_args = { 'func_name_override': func.__name__,
                           'file_name_override': os.path.basename(func.__globals__['__file__']) }

            """ Before to the function execution, log function details."""
            logger_obj.info(f"Arguments: {formatted_arguments} - Begin function", extra=extra_args)
            try:
                """ log return value from the function """
                value = func(self, *args, **kwargs)
                logger_obj.info(f"Returned: - End function {value!r}", extra=extra_args)
            except:
                """log exception if occurs in function"""
                logger_obj.error(f"Exception: {str(sys.exc_info()[1])}", extra=extra_args)
                raise
            # Return function value
            return value
        # Return the pointer to the function
        return log_decorator_wrapper
    # Decorator was called with arguments, so return a decorator function that can read and return a function
    if _func is None:
        return log_decorator_info
    # Decorator was called without arguments, so apply the decorator to the function immediately
    else:
        return log_decorator_info(_func)