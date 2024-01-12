import configparser
import os

config = configparser.RawConfigParser()
config.read("C:\\Users\\prasa\\PycharmProjects\\ProctortrackWebAppTest\\Configurations\\config.ini")


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
