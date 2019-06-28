import json
import os
import codecs
import configparser

proDir = os.path.split(os.path.abspath(__file__))[0]
configPath = os.path.join(proDir, 'testFile', "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        # 实例化configParser对象
        self.cf = configparser.ConfigParser()
        # 读取config.ini文件
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
    
    def read_json(self, num, url):
        jsonDir = os.path.join(proDir, 'login_url.json')
        with open(jsonDir) as file:
            jsonData = file.read()
            dictData = json.loads(jsonData)
            return dictData[num][url]

    def file_path(self, *loc):
        target_path = os.path.join(proDir, *loc)
        return target_path
