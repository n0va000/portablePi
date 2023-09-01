from ppsysutils import wlan
import urequests
from guilib import ask
if ask("mode","fsaveun","wrun"):
    data = urequests.get("https://raw.githubusercontent.com/n0va000/wrun/main/run.py")
    with open("/rbd/wrun.py","w") as f:
        f.write(str(data.text))
else:
    data = urequests.get("https://raw.githubusercontent.com/n0va000/wrun/main/run.py")
    exec(str(data.text))