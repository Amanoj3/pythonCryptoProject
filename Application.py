from tkinter import *
from tkinter.messagebox import showerror

from appOperations import *
import matplotlib.pyplot as plt
import csv

class Application(Frame):

    def showBarGraph(self,inputFile):
        # dataset from https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory
        dataX = []
        dataY = []
        rows = []
        with open(inputFile, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)

            for row in rows[1:50]:
                currentDate = row[3][:-9]
                currentHighPrice = row[4][:-9]
                dataX.append(currentDate)
                dataY.append(currentHighPrice)

            plt.bar(dataX,dataY)
            plt.xticks(rotation=45)
            plt.xlabel("Date")
            plt.ylabel("AAVE Crypto Price (Highest Daily Value)")
            plt.show()

    def parseFile(self):
        textInput = self.text_area.get("1.0", "end-1c")
        filename_valid = filenameValid(textInput)
        if not filename_valid:
            showerror("showerror", "Please enter the name of an EXISTING .csv file")
        else:
            print("good!")
            self.showBarGraph(textInput)

    def generateScene(self):
        # parse button and its necessary attributes
        self.parse = Button(self)
        self.parse["text"] = "Parse File"
        self.parse["command"] = self.parseFile

        # text area (where a user can type in the name of a file) and its necessary attributes
        self.text_area = Text(self, height=0.5,
                              width=20,
                              bg="light yellow")

        self.parse.pack(side=TOP, pady=10)
        self.text_area.pack(side=BOTTOM)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parse = None
        self.text_area = None
        self.pack(fill="both")
        self.generateScene()
