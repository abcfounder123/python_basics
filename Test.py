

class FunctionTester:
    def __init__(self):
        self.__error = 0
        self.__total = 0
        print("Testing\n")

    def check(self, msg, true_value, func, *args):
        print(" ", msg, " : ", end="")
        self.__total += 1
        calc_value = func(*args)  # Apply function to arguments
        if calc_value == true_value:
            print("\033[1;32m" + "OK" + "\033[0m")
        else:
            self.__error += 1  # Count this failed test
            print("\033[1;31m" + "Failed! >> true value:", true_value, "calculated value:", calc_value, "\033[0m")

    def report_results(self):
        print(self.__total, "tests run")
        print(self.__total - self.__error, "\033[1;32m" + "passed" + "\033[0m")
        print(self.__error, "\033[1;31m" + "failed" + "\033[0m")
