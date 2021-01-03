import configparser

config = configparser.RawConfigParser()
config.read(".\\Configaurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserename():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'Password')
        return password







