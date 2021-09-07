import sys, re
from pyjenkins import *
from pyjenkins_smb import *

class TheBuild(PyJenkinsBuild):
    def run(self):
        print("Running My Build")
        return Result.SUCCESS


register_pybuild( TheBuild() )
