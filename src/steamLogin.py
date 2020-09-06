import requests
import configFileValidation
from urllib import request
import re
import time
import encryption


# Function does a get request to steam's url
def checkConnectionToSteam():
    response = requests.get("https://steamcommunity.com")
    if response.status_code == 200:
        print("Steam is up and working...")
    else:
        print("Steam might be down...")


# Convert headers from getrsakey to a dict
def headersToDict(headersAsString):
    resDict = {}
    # Remove excess brackets
    headersAsString = headersAsString[1:len(headersAsString)-1]

    # Remove and quotation marks and split by commas
    headersAsString = headersAsString.replace('"', '')
    temp = headersAsString.split(',')

    # Cycle through our new list of strings, splitting by : and using the values as keys and values
    for x in temp:
        headerVals = x.split(":")
        resDict[headerVals[0]] = headerVals[1]
    return resDict


# Hit getrsakey in an attempt to get the values needed to encrypt our password
def requestToGetRsaKey(username):
    url = "https://steamcommunity.com/login/getrsakey"
    body = {'username': username}
    req = requests.post(url, data=body)
    if req.status_code == 200:
        headers = headersToDict(req.text)
        return headers
    else:
        print("Error connecting to: ", url)
        print("Error Code: ", req.status_code)


# Function sends a post request to the doLogin with our required details
def requestToDoLogin(donotcache, password, username, twoFactorCode, gid, captcha, sessionID, timeStamp):
    url = "https://steamcommunity.com/login/dologin"
    body = {'donotcache': donotcache,
            'password': password,
            'username': username,
            'twofactorcode': twoFactorCode,
            'emailauth': '',
            'loginfriendlyname': '',
            'captchagid': gid,
            'captcha_text': captcha,
            'emailsteamid': '',
            'rsatimestamp':  timeStamp,
            'remember_login': 'true',
            }
    cookies = {"sessionid": sessionID}
    req = requests.post(url, data=body, cookies=cookies)
    return req.cookies, req.text


# Check are we required to input a captcha by getting the html, checking to find a captcha id -1 means none needed
def CaptchaRequired():
    captchaNeedle = "tgidCaptcha: "
    gid = "unset"
    captchaURL = "https://steamcommunity.com/login/rendercaptcha/?gid="
    resp = request.urlopen("https://steamcommunity.com/login/home/?goto=")
    info = resp.info()
    cookie = str(info["Set-Cookie"]).replace("; Path=/; Secure; SameSite=None", '')
    sessionID = cookie.strip("sessionid=")
    configFileValidation.saveSingleConfigToFile("sessionid", sessionID)
    html = str(resp.read())
    splitHtml = html.split(captchaNeedle)
    try:
        postNeedle = splitHtml[1]
        gid = postNeedle[0:postNeedle.index(",")].strip('"')
    except IndexError as e:
        print("Index Error:", e)
    except ValueError as e:
        print("Value Error:", e)
    if gid != "unset":
        if gid != "-1":
            print("Captcha should be required, gid: ", gid)
            r = request.urlopen(captchaURL+gid)
            output = open("../captcha.jpg", "wb")
            output.write(r.read())
            output.close()
            return True, sessionID, gid
        else:
            print("Captcha should not be required, gid: ", gid)
            return False, sessionID, gid


# Main function to call to mimic the login functions of Steam, including captcha, 2fa and encryption
def login(username, password):

    # Get public key modulus and exponent from getrsakey XML request
    rsaData = requestToGetRsaKey(username)

    # donocache is a formatted timestamp
    donotcache = re.sub(r'\.', '', str(time.time()))[:-4]

    # Get our public key using modulus and exponent, encrypt the password using the rsa code
    password = encryption.runStuff(encryption.setVar(rsaData["publickey_mod"], rsaData["publickey_exp"], password))
    # password = steamRSA.run(rsaData["publickey_mod"], rsaData["publickey_exp"], "password") (OLD METHOD)

    captcha = ''
    # Check if we need to enter a captcha (also returns our sessionID and gid for the captcha as well as boolean)
    captchaRequired, sessionID, gid = CaptchaRequired()

    # Pull timestamp from the data retrieved from the getrsakey page request
    timeStamp = rsaData["timestamp"]

    # Ask for captcha input (TODO: needs a popup to display the captcha image)
    if captchaRequired:
        captcha = input("Enter the captcha from the image: ")

    # Enter two factor code from mobile app or email (TODO: checking if the code is required before asking for it)
    twoFA = input("Enter the 2FA code: ")

    # Run our dologin request with all our required data (TODO: check into the changes in requests when you save login)
    requestToDoLogin(donotcache, password, username, twoFA, gid, captcha, sessionID, timeStamp)


# Function sends a request to steams url if the cookies contains a secure id we can say we are logged in
def checkLogin():
    if configFileValidation.validateConfigFile():
        configs = configFileValidation.getConfigs()
        steamID = configs['steamid']
        try:
            customUrl = configs["customUrl"]
        except KeyError:
            print("Custom Url was not in the config file...")
            url = "https://steamcommunity.com/profiles/" + steamID
            req = requests.get(url)
            customUrl = req.url
            configFileValidation.saveSingleConfigToFile("customUrl", customUrl)
        cookies = {"steamMachineAuth" + steamID: configs["steamMachineAuth" + steamID],
                   "steamLoginSecure": configs["steamLoginSecure"]}
        editInfoReq = requests.get(customUrl + "edit/info", cookies=cookies)
        if editInfoReq.url == customUrl + "edit/info":
            return configs["username"]
        elif str(editInfoReq.url).startswith("https://steamcommunity.com/login"):
            return False
    else:
        return False


# Get RSA Data
def getRSAData(username):
    return requestToGetRsaKey(username)


# Get DoNotCache
def getDoNotCache():
    return re.sub(r'\.', '', str(time.time()))[:-4]


# Get Timestamp
def getTimestamp(rsaData):
    return rsaData["timestamp"]


# Get encrypted password
def getEncryptedPassword(rsaData, password):
    return encryption.runStuff(encryption.setVar(rsaData["publickey_mod"], rsaData["publickey_exp"], password))
