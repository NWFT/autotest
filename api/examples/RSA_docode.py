import rsa
import base64
from time import time


def rsaEncrypt(msg):
    """
    :param msg:
    :type msg: str
    :return:
    """
    server_pub_key = """
    -----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
    O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
    tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
    kKlZFc8Br7SHtbL2tQIDAQAB
    -----END PUBLIC KEY-----
    """

    # encode the public_key string
    pub_key_byte = server_pub_key.encode("utf-8")
    # print(pub_key_byte)
    pub_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_byte)

    # encode msg
    content = msg.encode("utf-8")

    # encode msg and return
    cryto_msg = rsa.encrypt(content, pub_key_obj)
    # base64编码
    cipher_base64 = base64.b64encode(cryto_msg)
    # change to string
    return cipher_base64.decode()


def generator_sign(token):
    # token 50 characters
    token_50 = token[:50]
    # timestamp
    timestamp = int(time())
    # print(timestamp)
    # token + timestamp
    msg = token_50 + str(timestamp)
    # print(msg)
    # RSA encode
    sign = rsaEncrypt(msg)
    return sign, timestamp


if __name__ == '__main__':
    token = "YrRKzJfkJqIkqLAxd/U2IElBN64eVGD04isrx+vYy+iZmsomhC8c6WEaRSfY9gIdYRCVb3H/i11B2blQIvbIYjKhB3mavTJtTSVJiIH/b8lfsXVUDV7mS53j6SYrpZ0xqV4W2vFT/MhKSwFnemPPmudxQSD3DG0NRMpcqZx8sdX5GjxLVm/dPWmZw/fo5JFk7OqtdQxICedy+PA5HkBct+Hl0dzp7BnHxZlGLkFJTgHAkZVm/"
    sign_token, timestamp = generator_sign(token)
    print(sign_token)
    print(timestamp)
