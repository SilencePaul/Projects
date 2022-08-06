################################################################################
# Config information Code
#
# Purpose: Access the information in the config code.
#
# Author: Yiming Liu
# Contact: liu1330@mcmaster.ca
#
################################################################################
import configparser


class configInfo:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        self.apikey = config['RiotAPI']['api_key']
        self.version = config['Version']['version']
        self.language = config['Languages']['code']
        self.host = config['Database']['host']
        self.user = config['Database']['user']
        self.password = config['Database']['password']
        self.database = config['Database']['database']
