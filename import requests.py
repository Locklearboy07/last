import requests
import hashlib
import hmac
import time

api_key = '039C26C7F5316ab9891ed924b3A4885BF35C70FE'
secret_key = '866cee39cb5a66816c815ee46481530f4d6b984bcf8eb9f9676715ee46fe2e37'
base_url = 'https://api-cloud.bitmart.com'

# Create a nonce (a unique number)
nonce = int(time.time() * 1000)

# Create a message to sign
message = f'{api_key}{nonce}'
signature = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

# Prepare headers
headers = {
    'X-BM-Key': api_key,
    'X-BM-Signature': signature,
    'X-BM-Nonce': str(nonce),
}

# Make an API request (e.g., get account balances)
response = requests.get(f'{base_url}/v2/account', headers=headers)
print(response.json())