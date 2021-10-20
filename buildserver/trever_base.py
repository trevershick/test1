from pyjenkins import *

class MyBuildClass(PyJenkinsBuild):
    def __init__(self):
        pass

    def run(self):
        logger.println("Running My Build (using str.format): {}".format(self.get_name()))
        return Result.SUCCESS
