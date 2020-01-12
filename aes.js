var CryptoJS = require("crypto-js");

// 加密
var str = '{}';
var key = 'OPyZ03AgyxoJT1xM';

var str = CryptoJS.enc.Utf8.parse(str);
var key = CryptoJS.enc.Utf8.parse(key);
console.log(CryptoJS.enc.Hex.stringify(key));
function AES_encrypt(){
    var arr=[]
    var encryptor = CryptoJS.AES.encrypt(str, key,
            {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7

         });

     let hex_text = encryptor.ciphertext.toString().toUpperCase();
     let base64_text = encryptor.toString();

     arr.push(hex_text,base64_text)
     return arr

};

// 解密
function AES_dencrypt(arr){

    //解密器
    var base64_decryptor = CryptoJS.AES.decrypt(arr[1], key,
            {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7

         });
    console.log(base64_decryptor.toString());
    console.log('key:',key);
    let base64_text = base64_decryptor.toString(CryptoJS.enc.Utf8);
    console.log('base64解密:',arr[1],'->',base64_text)

    let bytes_obj = CryptoJS.enc.Hex.parse(arr[0]);
    let str = CryptoJS.enc.Base64.stringify(bytes_obj);
    //返回{'word':,sigBytes}
    let hex_decryptor = CryptoJS.AES.decrypt(str, key,
            {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7

         });


    let hex_text = hex_decryptor.toString(CryptoJS.enc.Utf8)
    console.log('hex解密:',arr[0],'->',hex_text)
}

e= AES_encrypt();
AES_dencrypt(e);