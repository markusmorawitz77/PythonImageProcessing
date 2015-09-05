import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

import cv2
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt




class Application(tk.Frame, object):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.master.title('OpenCV video capture using tkinter')
        self.createFrames()
        self.initOpenCV()

    def quit(self):
        self.stop()

        super(Application, self).quit()     # stops mainloop
        self.destroy()                      # this is necessary on Windows to prevent
                                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    

    def initOpenCV(self):
        self.cap = None
        self.currentFrame = 0


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
        self.createOriginalFrame(self.originalFrame)
        self.createProcessedFrame(self.processedFrame)


    def createToolbar(self, parentFrame):
        self.quitButton  = tk.Button(parentFrame, text='Quit',          command=self.quit)
        self.startButton = tk.Button(parentFrame, text='Start capture', command=self.start)
        self.stopButton  = tk.Button(parentFrame, text='Stop capture',  command=self.stop)

        self.startButton.grid(row=0,sticky=tk.N+tk.S+tk.E+tk.W)
        self.stopButton.grid (row=1,sticky=tk.N+tk.S+tk.E+tk.W)
        self.quitButton.grid (row=2,sticky=tk.S+tk.E+tk.W)

        parentFrame.rowconfigure(2, weight=1)

    def createOriginalFrame(self, parentFrame):
        self.originalFigure = plt.figure(figsize=(5,3))
        self.originalAxes = self.originalFigure.add_subplot(111)
        self.originalAxes.set_xticklabels([])
        self.originalAxes.set_yticklabels([])
        self.originalCanvas = FigureCanvasTkAgg(self.originalFigure, master=parentFrame)
        self.originalCanvas.show()
        self.originalCanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        

    def createProcessedFrame(self, parentFrame):
        self.processedFigure = plt.figure(figsize=(5,3))
        self.processedAxes = self.processedFigure.add_subplot(111)
        self.processedAxes.set_xticklabels([])
        self.processedAxes.set_yticklabels([])
        self.processedCanvas = FigureCanvasTkAgg(self.processedFigure, master=parentFrame)
        self.processedCanvas.show()
        self.processedCanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        

    def start(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            print 'created video capture object'
            self.currentFrame = 0
            self.processVideo()

    def stop(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            print 'released video capture object'

    def processVideo(self):
        if self.cap is not None:
            #print 'process video frame %d' % self.currentFrame

            _, image_original_bgr = self.cap.read()

            b,g,r = cv2.split(image_original_bgr)
            image_original_rgb = cv2.merge([r,g,b])

            if self.currentFrame == 0:
                self.originalImageAxes = self.originalAxes.imshow(image_original_rgb)
            else:
                self.originalImageAxes.set_data(image_original_rgb)

            if self.currentFrame == 0:
                self.processedImageAxes = self.processedAxes.imshow(image_original_rgb)
            else:
                self.processedImageAxes.set_data(image_original_rgb)

            self.updateFigures()

            self.currentFrame = self.currentFrame + 1
            self.after(1, self.processVideo)
    
    def updateFigures(self):
        self.originalCanvas.draw()
        self.originalCanvas.flush_events()

        self.processedCanvas.draw()
        self.processedCanvas.flush_events()




app = Application()
app.mainloop()