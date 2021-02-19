import wx

class MyApp(wx.App):
	def __init__(self):
		super().__init__(clearSigInt = True)
		frame = MyFrame()
		frame.Show()

class FileMenu(wx.Menu):
	def __init__(self, parentFrame):
		super().__init__()
		self.OnInit()
		self.parentFrame = parentFrame

	def OnInit(self):
		aboutItem = wx.MenuItem(parentMenu = self, id = wx.ID_ANY, text="&About")
		self.Append(aboutItem)
		self.Bind(wx.EVT_MENU, handler = self.onAbout, source = aboutItem)
	
	def onAbout(self, event):
		aboutFrame = AboutFrame()
		aboutFrame.show()	

class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent = None, title = "Image Processor", pos = (20, 20), size = (700, 700))
		self.OnInit()

	def OnInit(self):
		self.panel = MyPanel(self)
		menuBar = wx.MenuBar()
		fileMenu = FileMenu(parentFrame = self)
		menuBar.Append(fileMenu, '&File')
		self.SetMenuBar(menuBar)
class MyPanel(wx.Panel):
	def __init__(self, parent):
		super().__init__(parent = parent)

if __name__ == "__main__":
	app = MyApp()
	app.MainLoop()	
