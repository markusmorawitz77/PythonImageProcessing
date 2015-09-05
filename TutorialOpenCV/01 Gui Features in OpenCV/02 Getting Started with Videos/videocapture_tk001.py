import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk


class Application(tk.Frame, object):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.title('OpenCV video capture using tkinter')
        self.createFrames()

    def quit(self):
        super(Application, self).quit()     # stops mainloop
        self.destroy()                      # this is necessary on Windows to prevent
                                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def createFrames(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(0, minsize=200, weight=1)
        self.rowconfigure(1, minsize=200, weight=1)
        self.columnconfigure(0, minsize=10,  weight=0)
        self.columnconfigure(1, minsize=400, weight=1)

        self.toolbarFrame   = tk.LabelFrame(self, text='Toolbar')
        self.originalFrame  = tk.LabelFrame(self, text='Original')
        self.processedFrame = tk.LabelFrame(self, text='Processed')

        self.toolbarFrame.grid  (row=0, column=0, rowspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.originalFrame.grid (row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.processedFrame.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        self.createToolbar(self.toolbarFrame)


    def createToolbar(self, parentFrame):
        self.quitButton = tk.Button(parentFrame, text='Quit', command=self.quit)
        self.startButton = tk.Button(parentFrame, text='Start capture')
        self.stopButton = tk.Button(parentFrame, text='Stop capture')

        self.startButton.grid(row=0,sticky=tk.N+tk.S+tk.E+tk.W)
        self.stopButton.grid (row=1,sticky=tk.N+tk.S+tk.E+tk.W)
        self.quitButton.grid (row=2,sticky=tk.S+tk.E+tk.W)

        parentFrame.rowconfigure(2, weight=1)


app = Application()
app.mainloop()