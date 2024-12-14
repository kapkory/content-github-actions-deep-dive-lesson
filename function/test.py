import requests

# Replace with your client ID and secret
client_id = "3kC8Q~5rf_xe7RoHFoiUG94NAoOpn0J8ymTCqazI"
client_secret = "35980a29-ce7e-4103-bfe2-4b253d37477c"
tenant_id = "6ada60ee-02fa-473d-8825-c9ae7a435bbb"  # Replace with your tenant ID (e.g., 'common' or specific tenant GUID)

# Microsoft OAuth token endpoint
url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# Request body
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default",
    "grant_type": "client_credentials"
}

# Make the request
response = requests.post(url, data=data)

# Check the response
if response.status_code == 200:
    print("Client ID and secret are valid!")
    print("Access Token:", response.json().get("access_token"))
else:
    print("Invalid client ID or secret.")
    print("Error:", response.json())
