from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['sha256_crypt'])

password = ''

print(pwd_context.hash(password)
