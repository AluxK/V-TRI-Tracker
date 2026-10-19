import requests

Client_ID = ' '
Client_Secret = ' '

request_token = "https://id.twitch.tv/oauth2/token?client_id=" + Client_ID + \
                "&client_secret=" + Client_Secret + \
                "&grant_type=client_credentials"

response = requests.post(request_token)
responseJSON = response.json()
print(responseJSON['access_token'])
print(responseJSON['expires_in'])
print(responseJSON['token_type'])
