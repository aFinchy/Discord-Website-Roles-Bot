import requests
import time
from config import WEBSITE_API_KEY, WEBSITE_API_URL

def get_website_roles():
    headers = {
        'Authorization': f'Bearer {WEBSITE_API_KEY}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(WEBSITE_API_URL, headers=headers)
        if response.status_code == 200:
            website_roles = response.json()
            return website_roles
        else:
            print(f"Failed to fetch website roles. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching website roles: {e}")

    return {}

def check_website_roles():
    while True:
        website_roles = get_website_roles()

        # Perform role synchronization logic here
        # Compare website roles with Discord server roles
        # Assign or remove roles based on the criteria

        print("Website roles checked. Synchronization completed.")

        # Sleep for a week (adjust the interval as needed)
        time.sleep(7 * 24 * 60 * 60)

# Other functions for interacting with the website's API can be added here

