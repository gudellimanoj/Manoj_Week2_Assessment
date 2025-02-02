# •	11. Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`).
class Logger:
    def log(self, message, type="info"):
        if type=="error":
            return f"Error: {message}"
        elif type=="warning":
            return f"Warning: {message}"
        else:
            return f"Info: {message}"
obj = Logger()
print(obj.log("This is an error message", "error"))
print(obj.log("This is a warning message", "warning"))
print(obj.log("This is an info message"))

    