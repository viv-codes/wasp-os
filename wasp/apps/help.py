import wasp

class HelpApp():
    """A demo application for wasp-os that helps display the capabilities of the watch such as touch gestures, etc."""
    NAME = "Help"
    
    def __init__(self,msg="Welcome to wasp-os!"):
        self.msg = msg

    def foreground(self):
        self.draw()

    def _draw(self):
        draw = wasp.watch.drawable
        draw.fill()
        draw.string(self.msg,0,108,width=240)