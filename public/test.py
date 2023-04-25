import jwt
import datetime

CONNECT_SECRET = "POw5BVJh81SMN3z//oeqdYUYfZNSlrjgfO6hbi1BE2w="

payload = {
  'sub': '119654d4-f86f-498a-8537-6f87a63ee88f',
  'iat': datetime.datetime.utcnow(),
  'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=500),
  'attributes': {"name": "Mark", "memberID": "123456789", "email": "Jane@example.com", "isPremiumUser": "true", "age": "45"}
}

header = {
  'typ': "JWT",
  'alg': 'HS256'
}

encoded_token = jwt.encode((payload), CONNECT_SECRET, algorithm="HS256", headers=header)
print(encoded_token)