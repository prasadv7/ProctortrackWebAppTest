import requests


def perform_login(username, password, csrf_token):
    login_url = "https://testing.verificient.com/"

    login_data = {
        'csrfmiddlewaretoken': csrf_token,
        'username': username,
        'password': password,
    }

    response = requests.post(login_url, data=login_data)

    # Check the response
    if response.status_code == 200:
        print("Login successful!")
    else:
        print(f"Login failed. Status code: {response.status_code}, Response: {response.text}")


# Example usage
username = "prasadvidhate@verificient.com"
password = "Vidhaterajendra7@"
# Replace 'get_csrf_token_url' with the actual endpoint that provides the CSRF token
csrf_token_response = requests.get('https://testing.verificient.com/')
csrf_token = csrf_token_response.json()["csrf_token"]

# Perform the login
perform_login(username, password, csrf_token)
