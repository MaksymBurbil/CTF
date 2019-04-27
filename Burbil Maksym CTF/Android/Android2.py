from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode

p = 256128251579833588962640669288236343457
q = 334659195040579408284360462422195488949
c = 4541193573047010079622862634544566667638995016075815652287123393675051074423
e = 65537
n = 85715674500858120010215671295511591797438474555497398310962747973700011956693

phi = (p-1)*(q-1)

def egcd(a, b):

    if a == 0:

        return (b, 0, 1)

    g, y, x = egcd(b%a,a)

    return (g, x - (b//a) * y, y)
def modinv(a, m):

    g, x, y = egcd(a, m)

    if g != 1:

        raise Exception('No modular inverse')

    return x%m

d = modinv(e, phi)

priv_key = RSA.construct((n,e,d))
print(bytearray.fromhex(str(hex(priv_key.decrypt(c)))[2:]))

