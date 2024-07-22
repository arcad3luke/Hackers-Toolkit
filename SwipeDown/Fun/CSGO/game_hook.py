import win32con
import win32gui


def game_hook(hwnd, msg, wparam, lparam):
    # Check if the game window is active
    if win32gui.GetForegroundWindow() == hwnd:
        # Check for specific game events and modify them
        if msg == win32con.WM_KEYDOWN:
            # Intercept keydown events
            if wparam == win32con.VK_SPACE:
                # Modify the behavior of the space key
                print("Space key pressed!")
                return True

    # Call the original game procedure
    return win32gui.CallWindowProc(game_hook, hwnd, msg, wparam, lparam)

# Get the handle of the League of Legends game window
game_window = win32gui.FindWindow(None, "League of Legends")

# Set the hook procedure for the game window
original_proc = win32gui.SetWindowLong(game_window, win32con.GWL_WNDPROC, game_hook)

# Start the message loop to receive and process messages
while True:
    # Process pending messages
    win32gui.PumpWaitingMessages()
