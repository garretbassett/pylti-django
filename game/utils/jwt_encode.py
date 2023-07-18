import jwt
from datetime import datetime, timedelta

with open("../../configs/private.key", "r") as f:
    private_key = f.read()

client_secret = "H3RL521W5g4gbvUgmTJbpJrE2lRwBqyQ0pGAGbUTKL2lqRT6knlPLde4dKyRQ3pQ"
payload = {
    "iss": "10000000000004",  # Replace with your client ID
    "sub": "10000000000004",  # Replace with the user ID or unique identifier
    "aud": "http://canvas.docker",
    "exp": datetime.utcnow() + timedelta(minutes=5),  # expiration time
    "iat": datetime.utcnow(),  # issued at now
    # Add any additional claims as required
}

access_token = jwt.encode(payload, client_secret, algorithm="HS256")
print("TOKEN: ", access_token)