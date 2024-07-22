#!/usr/bin/env python3

import tkinter
from tkinter import *
from tkinter.ttk import *
from SwipeDown.SwipeDown.Inject import sql, css
from SwipeDown.SwipeDown.Parameter import httpPollute
from SwipeDown.SwipeDown.Disrupt.Deny import deface
from SwipeDown.SwipeDown.Scan import webscrape


class UI(tkinter.Frame):
    def __init__(self, master=None):

        tkinter.Frame.__init__(self, master, padx=150, pady=150)
        self.grid()
        self.createWidgets()

    def openNewWindow(self):

        newWindow = Toplevel(master=None)
        newWindow.title('Sub-Menu')
        newWindow.geometry('200x200')
        Label(newWindow, text='Sub-menu for widget').pack()

    def createWidgets(self):

        # Initialize the Menu
        SwipeDown = tkinter.LabelFrame(self, name='options')
        headerLabel = tkinter.Label(self, text='SwipeDown Options:')
        headerLabel.grid()
        SwipeDown.grid()

        # Web Scrape Option
        ScrapeLabel = tkinter.Label(self, name='_Web Scrape', text='Web Scraper')
        ScrapeLabel.grid()
        scrapeButton = tkinter.Button(self, text='Google Scrape', command=f'{webscrape}')

        if scrapeButton:
            while scrapeButton:
                tkinter.LabelFrame(self, name='_Scrape Log', text='Scrape Log')
            tkinter.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        scrapeButton.grid()

        # Sql Injection
        sqlLabel = tkinter.Label(self, name='_SQL Label', text='Sql Scan')
        sqlLabel.grid()
        sqlButton = tkinter.Button(self, text='Scan', command=f'{sql}')

        while sqlButton:
            tkinter.LabelFrame(self, name='_SQL Log', text='SQL Log')
            tkinter.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        sqlButton.grid()

        # HTTP Parameter Pollution
        httpPolluteLabel = tkinter.Label(self, name='_Nmap Label', text='Nmap Scan')
        httpPolluteLabel.grid()
        httpPolluteButton = tkinter.Button(self, text='HTTP Parameter Pollution Test', command=f'{httpPollute}')

        while httpPolluteButton:
            tkinter.LabelFrame(self, name='_Pollution Log', text='Parameter Pollution Log')
            tkinter.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        httpPolluteButton.grid()

        # CSS Injection
        cssLabel = tkinter.Label(self, name='_Nmap Label', text='Nmap Scan')
        cssLabel.grid()
        cssButton = tkinter.Button(self, text='Scan', command=f'{css}')

        while cssButton:
            tkinter.LabelFrame(self, name='_CSS Log', text='CSS Injection Log')
            tkinter.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        cssButton.grid()

        # Deface
        defaceLabel = tkinter.Label(self, name='_Nmap Label', text='Nmap Scan')
        defaceLabel.grid()
        defaceButton = tkinter.Button(self, text='Deface', command=f'{deface}')

        while defaceButton:
            tkinter.LabelFrame(self, name='_Deface Log', text='Deface Log')
            tkinter.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        defaceButton.grid()

        quitButton = tkinter.Button(self, text="Quit", command=self.quit)
        quitButton.grid()


ui = UI()
ui.master.title('SwipeDown')

ui.mainloop()
ui.pack()
