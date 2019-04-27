from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode

p = 1680613444652105838344133706142211604381500993652031705380909307238347587888162431490921255465344239
q = 2143532995881162829855694296384103840144300960388531553947710050014176459461784664429637761367242287
c = 1921902980210977295270519710634709719343372281625129194637780159651252905527903923450045434239794433327822136581724693103107581315471305119544244907185643235873825200596556268483571243342863955690176
e = 65537


n = p*q
phi = (p-1)*(q-1)

# f = open('encryptedtext.txt', 'r')
# message = f.read()



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


