from ast import Assert
from colorama import Back, Fore, Style


def check_for_assertion_error(func):
    """Adds a decorator to check to see if the code has been completed instead of returning unhelpful exception"""
    def wrapper_check_for_assertion_error(*args, **kwargs):
        self = args[0]
        try:
            func(*args, **kwargs)
            return func(*args, **kwargs)
        except TypeError as ex:
            if "NoneType" in ex.args[0]:
                return self.fail(format_message(f"HINT: Complete the {func.__doc__} sql for this test"))
            return func(*args, **kwargs)
        except AssertionError as ex:
            if "500 != 200" in ex.args[0]:
                return self.fail(format_message(f"HINT: Check your {func.__doc__} sql for errors"))

    return wrapper_check_for_assertion_error


def format_message(message):
    """Make it easy to see hints in the terminal"""
    return Fore.BLACK + Back.LIGHTRED_EX + message + Style.RESET_ALL
