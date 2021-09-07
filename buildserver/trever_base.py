from pyjenkins import *

def MyBuildClass(PyJenkinsBuild):
    def run(self):

        print("Running My Build: ", self.get_name())
        return Result.SUCCESS
