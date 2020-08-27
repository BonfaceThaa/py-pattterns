class Logger(object):
    """
    A file-based message logger with the following properties:
    file_name: string representing full path to log file
    """

    def __init__(self, file_name):
        """
        Return a logger object whose file name is ***
        :param file_name:
        """
        self.file_name = file_name

    def write_log(self, level, msg):
        """
        writes a message to the file_name for a specific logger instance
        :param level:
        :param msg:
        :return:
        """
        with open(self.file_name, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def critical(self, msg):
        self.write_log("CRITICAL", msg)

    def error(self, msg):
        self.write_log("ERROR", msg)

    def warn(self, msg):
        self.write_log("WARNING", msg)

    def info(self, msg):
        self.write_log("INFO", msg)

    def debug(self, msg):
        self.write_log("DEBUG", msg)


logger_object = Logger("../../logs/test.log")

logger_object.info("This is an info message!")