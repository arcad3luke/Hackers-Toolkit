# import SwipeDown.SwipeDown.swipedown as sd
import time
# from SwipeDown.JARVIS.functions.online_utility.ip import get_public_ip as ip


# @TODO
# 1.) Make the script search the page for a login form
# 2.) Make the script scan the login form for vuln(s)
# 3.) Make the script attempt to authenticate using forms
# 4.) Add JS login prompt() scanner to expand reach
# 5.) Integrate with SwipeDown


def sql():
    # requests.get(url, params={key: value}, args) # Basic get request syntax
    try:
        import requests
        from bs4 import BeautifulSoup

        def check_forms(url):
            # Send a GET request to the website
            response = requests.get(url)

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all form elements in the HTML
            forms = soup.find_all('form')

            if forms:
                print("Forms found on the website:")
                for form in forms:
                    # Extract form details
                    form_id = form.get('id')
                    form_action = form.get('action')
                    form_method = form.get('method')

                    def check_captcha(captcha_response):
                        from
                        from google.auth import compute_engine
                        check_url = "https://www.google.com/recaptcha/api/siteverify"
                        data = {
                            "response": captcha_response,
                            "remoteip": ip  # Replace with the user's IP address
                        }
                        headers = {
                            "Content-Type": "application/x-www-form-urlencoded"
                        }
                        check_response = requests.post(check_url, data=data, headers=headers)
                        return check_response.json()["success"]

                    user_captcha_response = "<div class='g-recaptcha' data-sitekey='6LfwuyUTAAAAAOAmoS0fdqijC2PbbdH4kjq62Y1b' data-callback='onSubmit' data-size='invisible'></div><script>grecaptcha.execute();</script>"
                    if check_captcha(user_captcha_response):
                        print("Captcha passed. Form submitted successfully!")
                    else:
                        print("Captcha failed. Please try again.")
                    print(f"Form ID: {form_id}")
                    print(f"Action URL: {form_action}")
                    if form_action == 'g-recaptcha':
                        check_captcha(captcha_response=user_captcha_response)
                    print(f"Method: {form_method}")
                    print("---------")

            else:
                print("No forms found on the website.")

        import re

        def check_strings_in_javascript(js_code, strings):
            for search_string in strings:
                pattern = re.compile(r'\b{}\b'.format(re.escape(search_string)), re.IGNORECASE)
                if re.search(pattern, js_code):
                    print(f"Found '{search_string}'.")
                else:
                    print(f"'{search_string}' not found.")

        # JavaScript code to search within
        javascript_code = '''
        apiKey
        username
        password
        captcha-form
        '''

        # Strings to search for in the JavaScript code
        search_strings = ['apiKey','username','password','captcha-form']

        # Check for the strings in the JavaScript code
        count = 0
        while count < 50:
            # Provide the URL of the website to check for forms
            with open('../scan/GoogleHackMasterList.csv','r') as f:
                for website_url in f:
                    print('form count: ', count)
                    time.sleep(2)
                    check_strings_in_javascript(javascript_code, search_strings)
                    check_forms(website_url)
                    count += 1
            f.close()
    except KeyboardInterrupt:
        print('Error!')

if __name__ == '__main__':
    sql()
