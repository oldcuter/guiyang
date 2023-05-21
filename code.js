var CryptoJS = require('crypto-js')

function s(e) {
    var t = CryptoJS.enc.Utf8.parse("s%kld*spECslDa#a")
        , n = CryptoJS.enc.Utf8.parse("03Q22$9V0(92&3*0")
        , i = CryptoJS.enc.Base64.parse(e)
        , s = CryptoJS.enc.Base64.stringify(i)
        , o = CryptoJS.AES.decrypt(s, t, {
        iv: n,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
        , c = o.toString(CryptoJS.enc.Utf8);
    return c
}

function o(e) {
    var t = CryptoJS.enc.Utf8.parse("s%kld*spECslDa#a")
        , n = CryptoJS.enc.Utf8.parse("03Q22$9V0(92&3*0")
        , i = CryptoJS.AES.encrypt(e, t, {
        iv: n,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return i.toString()
}

console.log(s('cz5F+NPy9o+w+TOp7kSfkA=='))