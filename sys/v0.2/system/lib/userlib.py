from clilib import cli
from ppsysutils import file_exists
from guilib import ask
import json
cUser = "sysUser"
cli.printl("checking /system/user.json")
if file_exists("/system/user.json"):
    with open("/system/user.json") as file:
        userData = file.read()
    userJson = json.loads(userData)
else:
    cli.printl("unable to find file!")
    userExists = False
    username = "ERROR"
class user:
    def __init__(self,user):
        self.userd = userJson[user]
        print(self.userd)
        self.name = self.userd["name"]
    def getDir(self):
        return self.userd["dir"]
    def getName(self):
        return self.userd["name"]
    def getPass(self):
        if self.userd["password"] == "":
            return ""
        else:
            if ask("program wants password data.","give password?"):
                return self.userd["password"]
            else:
                return False