import urllib.request
import rumps

def ping(url):
    try:
        urllib.request.urlopen(url, timeout=1)
        return True
    except urllib.error.URLError as err: 
        return False

class InternetStatusApp(rumps.App):
    def __init__(self):
        super(InternetStatusApp, self).__init__(self.getAppTitle())
    
    @rumps.timer(1)
    def updateTitle(self, sender):
        self.title = self.getAppTitle()

    def getStatus(self):
        return "🟢" if ping("http://www.google.com") else "🔴"
    
    def getAppTitle(self):
        return self.getStatus()

app = InternetStatusApp()
for timer in rumps.timers():
    timer.start()
app.run()