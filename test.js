var i =  require("crypto-js");
var dic={
            getKey: function() {
                var t = "OPyZ03AgyxoJT1xM";
                return i.enc.Utf8.parse(t)
            },
            encryptASE: function(t) {
                var e = this.getKey()
                  , n = i.AES.encrypt(t, e, {
                    mode: i.mode.ECB,
                    padding: i.pad.Pkcs7
                });
                return n.ciphertext.toString()
            },
}
var   t = '{"events":"\'\'or age"}'



console.log(dic.encryptASE(t))