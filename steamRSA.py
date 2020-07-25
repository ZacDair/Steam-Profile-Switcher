# Reverse engineered RSA encryption/Decryption from Steam (originally JS)
import random
import jsbn
import decimal

# test function to attempt to replicate what we need
def run(modHex, expHex, password):
    rsa = RSA(modHex, expHex)
    return rsa.encrypt(password, rsa.pubKey)


def montgomery(m):
    z = {'m': m,
         'mp': '',
         'mp1': '',
         'mph': '',
         'um': '',
         'mt2': ''}
    return



def modPowInt(e, m):
    z = ''
    if e < 256 or (m % 2) == 0:
        z = "Classic(m)"
    else:
        z = "Montgomery(m)"


# Convert our RSA modulus and exponent to their numerical vales
class RSAPublicKey:
    def __init__(self, modHex, expHex):
        self.modulus = int(modHex, 16)
        self.encryptionExponent = int(expHex, 16)


def getPublicKey(modulusHex, exponentHex):
    return RSAPublicKey(modulusHex, exponentHex)


# Class for encoding and decoding using base64
class Base64:
    def __init__(self):
        self.base64 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4",
                       "5", "6", "7", "8", "9", "+", "/", "="]

    def encode(self, inputVal):
        if len(inputVal) == 0:
            return False

        output = ""
        chr1, chr2, chr3 = '', '', ''
        enc1, enc2, enc3, enc4 = '', '', '', ''
        i = 0
        while i < len(inputVal):
            try:
                chr1 = ord(inputVal[i])
                i = i + 1
                chr2 = ord(inputVal[i])
                i = i + 1
                chr3 = ord(inputVal[i])
                i = i + 1
                enc1 = chr1 >> 2
                enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
                enc3 = ((chr2 & 15) << 2) | (chr3 >> 6)
                enc4 = chr3 & 63

            except IndexError:
                if not isinstance(chr2, int):
                    enc3, enc4 = 64, 64
                elif not isinstance(chr3, int):
                    enc4 = 64
                elif isinstance(chr2, int):
                    enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
                enc1 = chr1 >> 2

            output = output + self.base64[enc1] + self.base64[enc2] + self.base64[enc3] + self.base64[enc4]

        print("Base64 encode: ", output)
        return output

    def decode(self, inputVal):
        if len(inputVal) == 0:
            return False

        output = ""
        enc1, enc2, enc3, enc4 = '', '', '', ''
        i = 0
        while i < len(inputVal):
            try:
                enc1 = self.base64.index(inputVal[i])
                i = i + 1
                enc2 = self.base64.index(inputVal[i])
                i = i + 1
                enc3 = self.base64.index(inputVal[i])
                i = i + 1
                enc4 = self.base64.index(inputVal[i])
                i = i + 1
                output = output + chr((enc1 << 2) | (enc2 >> 4))
                if enc3 != 64:
                    output = output + chr(((enc2 & 15) << 4) | (enc3 >> 2))
                if enc4 != 64:
                    output = output + chr(((enc3 & 3) << 6) | enc4)
            except IndexError:
                print("Index Error")

        # Quick fix for extra two chars that are always part of the original str, possibly enc1 & enc2
        output = output[0:len(output)-2]
        print("Base64 Decode: ", output)
        return output


# Class for hex encoding and decoding
class Hex:
    def __init__(self):
        self.hexList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

    def encode(self, inputVal):
        output = ''
        if len(inputVal) != 0:
            for char in inputVal:
                k = ord(char)
                output = output + self.hexList[((k >> 4) & 0xf)] + self.hexList[(k & 0xf)]
        print("Hex Encode: ", output)
        return output

    def decode(self, inputVal):
        output = ''
        if len(inputVal) != 0:
            # currently going to ignore this cleaning function $input = $input.replace( / [ ^ 0 - 9 abcdef] / g, "");
            i = 0
            while i < len(inputVal):
                try:
                    char1 = inputVal[i]
                    i = i + 1
                    char2 = inputVal[i]
                    output = output + chr(((self.hexList.index(char1) << 4) & 0xf0) | (self.hexList.index(char2) & 0xf))
                except IndexError as e:
                    print("At the end of the inputVal")

        res = output[::2]
        print("Hex Decode: ", res)
        return res


# Class for RSA
class RSA:
    def __init__(self, modHex, expHex):
        self.pubKey = getPublicKey(modHex, expHex)

    def pkcs1pad(self, data, keySize):
        if keySize < len(data) + 11:
            return ""
        buffer = [-1]*keySize
        i = len(data)-1
        while i >= 0 and keySize > 0:
            keySize = keySize - 1
            i = i - 1
            buffer[keySize] = ord(data[i])
            keySize = keySize - 1
        buffer[keySize] = 0
        while keySize > 2:
            keySize = keySize - 1
            buffer[keySize] = random.randint(0, 254)
            keySize = keySize - 1
            buffer[keySize] = 2
            keySize = keySize - 1
            buffer[keySize] = 0
        return buffer

    def encrypt(self, data, pubKey):
        if len(str(pubKey)) == 0:
            return False
        data = self.pkcs1pad(data, (self.pubKey.modulus.bit_length()+7) >> 3)
        if len(data) == 0:
            return False
        data = jsbn.run("password", pubKey.modulus, pubKey.encryptionExponent)
        if len(data) == 0:
            return False
        data = data.to_string(16)
        if len(data) & 1 == 1:
            data = "0" + data
        base64 = Base64()
        hexObj = Hex()
        return base64.encode(hexObj.decode(data))
'''

var RSA = {

	getPublicKey: function( $modulus_hex, $exponent_hex ) {
		return new RSAPublicKey( $modulus_hex, $exponent_hex );
	},
	
    pkcs1pad2: function($data, $keysize) {
		if($keysize < $data.length + 11)
			return null;
		var $buffer = [];
		var $i = $data.length - 1;
		while($i >= 0 && $keysize > 0)
			$buffer[--$keysize] = $data.charCodeAt($i--);
		$buffer[--$keysize] = 0;
		while($keysize > 2)
			$buffer[--$keysize] = Math.floor(Math.random()*254) + 1;
		$buffer[--$keysize] = 2;
		$buffer[--$keysize] = 0;
		return new BigInteger($buffer);
	}
	
	encrypt: function($data, $pubkey) {
		if (!$pubkey) return false;
		$data = this.pkcs1pad2($data,($pubkey.modulus.bitLength()+7)>>3);
		if(!$data) return false;
		$data = $data.modPowInt($pubkey.encryptionExponent, $pubkey.modulus);
		if(!$data) return false;
		$data = $data.toString(16);
		if(($data.length & 1) == 1)
			$data = "0" + $data;
		return Base64.encode(Hex.decode($data));
	},

	
};
'''