"""
ECB没有偏移量
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

import base64



class AES_ECB:
    def __init__(self,key):
        self.key = key.encode('utf8')
        self.mode = AES.MODE_ECB

        # 生成加密器，需要密匙和模式
        self.cryptor  = AES.new(self.key, self.mode)

    @staticmethod
    def add_to_16(text):
        pad = 16 - len(text.encode('utf-8')) % 16
        text = text + pad * chr(pad)
        return text.encode('utf-8')


    def encrypt(self,text):

        #预处理,填充明文为16的倍数
        text = self.add_to_16(text)

        #加密,输出bytes类型
        cipher_text = self.cryptor.encrypt(text)
        b,a =  base64.b64encode(cipher_text).decode('utf-8'),b2a_hex(cipher_text).decode('utf-8')
        return  b,a


    def decrypt(self,arr):

        text_a = a2b_hex(arr[1])
        text_b = base64.b64decode(arr[0])  # base64解码

        hex_text = self.cryptor.decrypt(text_a).decode('utf8')

        #剔除尾部
        hex_text = hex_text[0:-ord(hex_text[-1])]
        base64_text = self.cryptor.decrypt(text_b).decode('utf8')
        base64_text = base64_text[0:-ord(base64_text[-1])]

        print('解密16进制密文:',arr[1],'->',hex_text)
        print('解密base64密文:', arr[0],'->',base64_text)

def request_data():
    key = 'OPyZ03AgyxoJT1xM'
    text = '{}'
    aesor = AES_ECB(key)
    e = aesor.encrypt(text)
    #d = aesor.decrypt(e)
    return e



if __name__ == '__main__':
    key = 'OPyZ03AgyxoJT1xM'
    t = '{"events":"564308,564310,564514,564312,564315,564319,564321,564324,564526,564326,564328,564330,564541,564856,564646,564332,564333,564545,564290"}'
    ase = AES_ECB(key)
    print(ase.encrypt(t))
    print(ase.decrypt(ase.encrypt(t)))