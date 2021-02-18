import wx

class MyApp(wx.App):
	def __init__(self):
		super().__init__(clearSigInt = True)
		frame = MyFrame()
		frame.Show()

class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent = None, title = "Image Processor", pos = (20, 20), size = (700, 700))
		self.OnInit()

	def OnInit(self):
		self.panel = MyPanel(self)

class MyPanel(wx.Panel):
	def __init__(self, parent):
		super().__init__(parent = parent)

if __name__ == "__main__":
	app = MyApp()
	app.MainLoop()	
