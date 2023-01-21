from urllib.parse import urlencode
import webbrowser

# Set the client ID and redirect URI
client_id = "your_client_id"
redirect_uri = "your_redirect_uri"

# Set the scope of access
scope = "https://www.googleapis.com/auth/blogger"

# Build the authorization URL
query_params = {
    "response_type": "code",
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "scope": scope
}

url = f"https://accounts.google.com/o/oauth2/auth?{urlencode(query_params)}"

# Open the authorization URL in the user's web browser
webbrowser.open(url)


#This open the browser and gives us
#http://localhost/?code='CODE'&scope=https://www.googleapis.com/auth/blogger
