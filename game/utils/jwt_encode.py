import jwt
from datetime import datetime, timedelta

with open("../../configs/private.key", "r") as f:
    private_key = f.read()

client_secret = "H3RL521W5g4gbvUgmTJbpJrE2lRwBqyQ0pGAGbUTKL2lqRT6knlPLde4dKyRQ3pQ"
client_secret_2 = "7RQ8I4Eu0QIm4V9cSIgWCobu5kzZ2PI6VBHEae1bpUenGtidazbWGmtW0HAfYPDW"

payload = {
    "iss": "10000000000004",  # Replace with your client ID
    "sub": "10000000000004",  # Replace with the user ID or unique identifier
    "aud": "http://canvas.docker/accounts/site_admin/authorize",
    "exp": datetime.utcnow() + timedelta(minutes=5),  # expiration time
    "iat": datetime.utcnow(),  # issued at now
    "jti": "ce31ce8d-dcc7-440b-94e4-4a3b0a4410e4"
    # Add any additional claims as required
}

access_token = jwt.encode(payload, client_secret)
print("\nTOKEN with client secret: ", access_token)

access_token = jwt.encode(payload, client_secret_2, algorithm="HS256")
print("\nTOKEN with client secret 2: ", access_token)

# access_token_2 = jwt.encode(payload, private_key)
# print("\nTOKEN with private key: ", access_token_2)