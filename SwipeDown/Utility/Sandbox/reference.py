casc = '''All this was just a test of a pyhcarm feature:\n
                Ctrl+Alt+Shift+C creates a reference to a line of code within a file.\n
                I thought that this would copy/paste the line itself, but this simply\n
                puts a reference to the line number associated with the code.\n
                SwipeDown/SwipeDown/Utility/shell_server.py:9\n'''

page = '''
The following snippet is a template for adding the option of a log to the UI menu.
        while < menu item >:
            tk.LabelFrame(self, name='_< item name >', text='< insert text here >')
            tk.Button(self, text="Back", command=f'{self.tk_focusPrev()}')\n
'''

match_case = '''
    match <something>:
        case 'whatever':
            command
            return whatever_it_is
'''








# help_me = input("which example would you like? (1, 2, or 3)")

ref_menu = {
    1: print(casc),
    2: print(page),
    3: print(match_case)
}