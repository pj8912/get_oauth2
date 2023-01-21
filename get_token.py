import requests
token_endpoint = "https://oauth2.googleapis.com/token"

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
code = "YOUR_CODE"

redirect_uri = "http://localhost"

data  = {

        "grant_type" : "authorization_code",
        "code" : code,
        "redirect_uri" : redirect_uri,
        "client_id" : client_id,
        "client_secret" : client_secret,
        "scope" : "https://www.googleapis.com/auth/blogger"
}

response = requests.post(token_endpoint, data =data)
token = response.json()["access_token"]
print(token)

