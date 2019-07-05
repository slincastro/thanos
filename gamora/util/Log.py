

class Log:
    def __init__(self):
        pass

    def write_log(self, message):
        f = open("log.txt", "a")
        f.write(message + " \n")
        f.close()
