################################################################################
# Print Report Code
#
# Purpose: TO check the information that is available for the program to work.
#
# Author: Yiming Liu
# Contact: liu1330@mcmaster.ca
#
################################################################################

class report:
    # Generate a report to a text file
    @staticmethod
    def generateReport(reportName, information):
        f = open(reportName, 'w')
        f.write(information)
        f.close()
