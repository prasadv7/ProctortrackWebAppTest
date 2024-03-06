import configparser
import os

config = configparser.RawConfigParser()
config.read(r"C:\Users\GOD\PycharmProjects\ProctortrackWebAppTest\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password

    # D2l instructor creds
    @staticmethod
    def getD2LAppURL():
        d2lurl = config.get('D2L info', 'baseURL_D2L')
        return d2lurl

    @staticmethod
    def getD2LUserEmail():
        d2lusername = config.get('D2L info', 'username_D2L')
        return d2lusername

    @staticmethod
    def getD2LPassword():
        d2lpassword = config.get('D2L info', 'password_D2L')
        return d2lpassword

    # Canvas instructor creds
    @staticmethod
    def getCanvasAppURL():
        canvasurl = config.get('Canvas info', 'baseURL_Canvas')
        return canvasurl

    @staticmethod
    def getCanvasUserEmail():
        canvasusername = config.get('Canvas info', 'username_Canvas')
        return canvasusername

    @staticmethod
    def getCanvasPassword():
        canvaspassword = config.get('Canvas info', 'password_Canvas')
        return canvaspassword



