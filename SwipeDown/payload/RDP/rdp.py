from pywinauto import Application

# Launch the Remote Desktop Connection application
app = Application().start("mstsc.exe")

# Connect to the Remote Desktop
dlg = app.window(title="Remote Desktop Connection")
dlg.wait("ready")
dlg.type_keys("address_to_connect")  # Replace with the actual IP or hostname
dlg.type_keys("{TAB}")
dlg.type_keys("{TAB}")
dlg.type_keys("{ENTER}")

# Wait for the Remote Desktop session to establish
rdp_window = app.window(title="Desktop Connection")
rdp_window.wait("ready")

# You can perform actions within the Remote Desktop session here
# For example, send keyboard input, interact with the GUI, etc.

# Close the Remote Desktop session
rdp_window.close()
