from functools import wraps
# Notes and code on decorators

# Wrappers are functions that take functions as inputs
# Interally the function is called to obtain outputs


def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return 'a {} wrapped up box of {}'.format(style, str(item()))
        return wrapped_item  # Careful that it returns a function
    return add_wrapping
# The output of the original function is fed into the wrapper


def repeat_call(f):
    def repeat():
        print(f())
        print(f())
    return repeat


# @add_wrapping_with_style('beautifully')
@repeat_call
def new_gpu():
    return 'a new Tesla GPU'


new_gpu()  # If @wraps(item) is used the original function name is returned
