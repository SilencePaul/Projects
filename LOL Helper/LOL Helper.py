################################################################################
# LOL Helper Code
#
# Purpose: To start the whole application
#
# Author: Yiming Liu
# Contact: liu1330@mcmaster.ca
#
################################################################################
from ProcessMVC import *


def startApplication():
    startAPP = controller(view(), model())
    startAPP.start()


startApplication()
