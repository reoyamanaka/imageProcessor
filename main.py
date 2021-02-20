import wx, sys

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
                aboutFrame.Show()	

class MyFrame(wx.Frame):
        def __init__(self):
                super().__init__(parent = None, title = "Image Processor", pos = (20, 30), size = (900, 700))
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
                hSizer = wx.BoxSizer(wx.HORIZONTAL)
                mainSizer = wx.BoxSizer(wx.VERTICAL)

                quitButton = wx.Button(self, label = "Quit")
                quitButton.Bind(wx.EVT_BUTTON, self.onQuit)
                
                hSizer.Add(quitButton, 0, wx.CENTER)
                mainSizer.Add((0,0), 3, wx.EXPAND)
                mainSizer.Add(hSizer, 0, wx.CENTER)
                mainSizer.Add((0,0), 1, wx.EXPAND)
                self.SetSizer(mainSizer)
        def onQuit(self, event):
                sys.exit()
                
                

if __name__ == "__main__":
        
        app = MyApp()
        app.MainLoop()	
