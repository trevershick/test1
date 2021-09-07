from pyjenkins import *

class MyBuildClass(PyJenkinsBuild):
    def __init__(self):
        pass

    def run(self):
        print("Running My Build: " + self.get_name())
        return Result.SUCCESS
