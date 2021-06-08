from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(password: str):
        return pwd_ctx.hash(password)

    def verify(plainPassword, hashedPassword):
        return pwd_ctx.verify(plainPassword,hashedPassword)