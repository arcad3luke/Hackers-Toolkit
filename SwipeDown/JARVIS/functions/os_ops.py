import os

def find_in_linux():
    import subprocess

    def search_application(application_name):
        try:
            result = subprocess.check_output(["which", application_name])
            if result:
                return result.decode('utf-8').strip()
            else:
                return f"{application_name} not found."
        except subprocess.CalledProcessError:
            return f"Error searching for {application_name}"

    # Example usage:
    app_name = "geany"
    result = search_application(app_name)
    print(result)
    
def find_in_macos():
    import subprocess

    def search_application_macos(application_name):
        try:
            result = subprocess.check_output(["mdfind", f"kMDItemDisplayName == '{application_name}'"])
            if result:
                return result.decode('utf-8').strip()
            else:
                return f"{application_name} not found."
        except subprocess.CalledProcessError:
            return f"Error searching for {application_name}"

    # Example usage:
    app_name = "TextEdit"
    result = search_application_macos(app_name)
    print(result)

paths = {
    'notepad': {
        'windows' : "C:\\Windows\\notepad.exe",
        'linux' : find_in_linux(),
        'macosx' : find_in_macos()
                },
    'discord': {
        'windows' : f"C:\\Users\\{os.getenv('username')}\\AppData\\Local\\Discord\\app-1.0.9013\\Discord.exe",
        'linux' : '/usr/bin/discord',
        'macosx' : '~/Library/Application Support/Discord'
                },
    'calculator': "C:\\Windows\\System32\\calc.exe"
}