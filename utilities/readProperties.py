import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('commen info', 'baseURL')
        return url

    @staticmethod
    def getApplicationUsername():
        uname = config.get('commen info', 'username')
        return uname


    @staticmethod
    def getApplicationpassword():
        pwd = config.get('commen info', 'password')
        return pwd

