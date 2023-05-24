In Python, you can interact with various operating system (OS) services using built-in modules. These modules provide functions and classes to perform operations related to file system management, directory manipulation, environment variables, process management, and more. Here are some commonly used OS services in Python:

1. File and Directory Operations:
   - `os`: The `os` module provides functions for interacting with the operating system. It allows you to perform operations like file and directory manipulation, process management, environment variables, etc.
   - `os.path`: The `os.path` module provides functions for manipulating file paths. It allows you to perform operations like joining paths, checking file existence, getting file information, etc.

2. File I/O:
   - `open()`: The `open()` function is used to open files in Python. It allows you to read from or write to files by creating a file object.

3. Environment Variables:
   - `os.environ`: The `os.environ` dictionary provides access to the environment variables of the current process. You can read and modify environment variables using this dictionary.

4. Process Management:
   - `subprocess`: The `subprocess` module allows you to spawn new processes, connect to their input/output/error streams, and obtain their return codes. It provides functions to execute shell commands and external programs.
   - `os.system`: The `os.system()` function is used to execute shell commands. It runs the specified command in a subshell and returns the exit status of the command.

5. Command Line Arguments:
   - `sys.argv`: The `sys.argv` list contains the command-line arguments passed to a Python script. It allows you to access and process command-line arguments.

6. Date and Time:
   - `datetime`: The `datetime` module provides classes and functions for working with dates and times. It allows you to create, manipulate, and format dates and times.

7. Error Handling and Logging:
   - `try-except`: Python's `try-except` construct is used for error handling. It allows you to catch and handle exceptions that occur during the execution of code.
   - `logging`: The `logging` module provides a flexible framework for logging messages from Python programs. It allows you to log messages with different severity levels and store them in various outputs.

These are just a few examples of OS services available in Python. Python's standard library offers many more modules and functions for interacting with the operating system and performing various system-related tasks. Additionally, there are third-party libraries available that provide even more advanced capabilities for specific OS services and operations.