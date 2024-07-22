import pyautogui

# Read the RDP script file
with open('rdp_script.txt', 'r') as file:
    rdp_script = file.read()

# Split the script into individual lines
script_lines = rdp_script.splitlines()

# Reverse the lines
reversed_lines = script_lines[::-1]

# Execute the reversed script
for line in reversed_lines:
    # Perform actions based on the script line
    # For example, if the line starts with "click", you can simulate a mouse click
    if line.startswith('click'):
        # Extract the coordinates from the line (assuming format: "click x y")
        _, x, y = line.split()
        # Simulate a mouse click at the specified coordinates
        pyautogui.click(int(x), int(y))
    # Add more conditions for different actions as needed

# Save the reversed script to a file
with open('reversed_rdp_script.txt', 'w') as file:
    file.write('\n'.join(reversed_lines))
