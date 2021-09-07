import sys, re
from pyjenkins import *

from trever_base import *

class TheBuild(MyBuildClass):
    def __init__(self):
        pass

    def get_name(self):
        return "Trever"

register_pybuild( TheBuild() )
