import json
import urequests as urq
import guilib as gui
import userlib
import prc
class RobloxApp:
    def __init__(self):
        self.gui = gui
        self.userlib = userlib
        
    def run(self):
        sel = self.gui.menu("roblox", "your account", "users")
        
        if sel == 1:
            self.account()
        elif sel == 2:
            self.users()
    
    def account(self):
        if self.gui.ask("login how?", "json file", "typing"):
            temp = self.userlib.user(self.userlib.cUser)
            quizlist = self.gui.file("pick user json", temp.getDir())
            del temp
    
    def users(self):
        username = self.gui.osk("roblox username", "abcdefghijklmnopqrstuvwxyz0123456789_")
        data = {
            "usernames": [username],
            "excludeBannedUsers": True
        }

        response = urq.post("https://roblox.com/v1/usernames/users", json=data)
        response_data = response.json()
        
        if "data" in response_data and len(response_data["data"]) > 0:
            user_id = response_data["data"][0]["id"]
            display_name = response_data["data"][0]["displayName"]
            self.gui.splash("Welcome " + display_name, 1)
        else:
            self.gui.splash("User not found!")

if prc.sysprc == "home":
    app = RobloxApp()
    app.run()