import profileValidation
import configFileValidation
import steamLogin


# Validate and retrieve our profiles
def getProfiles():
    profilesList = profileValidation.getProfiles()
    profileCount = len(profilesList)
    newScrollBoxLabel = "Searching for profiles..."
    if profileCount != 0:
        newScrollBoxLabel = "Found " + str(profileCount) + " Profiles."
        # Cheeky way to remove the s from profiles, if there is only one found
        if profileCount == 1:
            newScrollBoxLabel = newScrollBoxLabel.replace("s.", ".")
    return profilesList, newScrollBoxLabel


# Validate and retrieve our saved configs
def getConfigs():
    return configFileValidation.getConfigs()


# Create and save a new profile
def saveProfile(profileData):
    return profileValidation.createNewProfile(profileData)


# Delete a profile folder
def deleteProfile(index):
    profiles = profileValidation.getProfiles()
    try:
        profile = profiles[index]
        return profileValidation.deleteProfileFolder(profile)
    except IndexError as e:
        print("Error has occurred ...")
        print(e)
        return False


# Find profile details by index, searches the profiles dir for the (index)-th profile returns correct details
def getProfileDetails(index):
    profiles = profileValidation.getProfiles()
    try:
        return profileValidation.getProfileDetails(profiles[index])
    except IndexError as e:
        print("Error has occurred ...")
        print(e)
        return False


# Check if we are logged into Steam, returns a string and a boolean
def checkLogin():
    response = steamLogin.checkLogin()
    if response:
        return "Logged in as " + response, True
    else:
        return "Please login", False


# Send our first login request to get the rsa key and check if we need a captcha
def captchaNeeded():
    return steamLogin.CaptchaRequired()


# Clean the response cookies and response content into a config dict
def cleanToList(cookies, content):
    configs = []
    for x in cookies:
        temp = str(x).split(" ")
        configs.append(temp[1])
    content = content.replace('"transfer_parameters":{"', '')
    contentList = str(content).split(",")
    # Ignore the first 5 elements grab 6th ie(transfer params)
    contentList = contentList[5:len(contentList)]
    for x in contentList:
        x = x.replace(':', '=')
        x = x.replace('"', '')
        x = x.replace('}}', '')
        configs.append(x)
    return configs


# Attempt to login with our given details, store and process our results
def tryToLogin(username, password, twoFA, captcha, gid, sessionID):
    rsaData = steamLogin.getRSAData(username)
    if rsaData['success'] == 'false':
        return "Username Error"
    else:
        doNotCache = steamLogin.getDoNotCache()
        timestamp = steamLogin.getTimestamp(rsaData)
        encryptedPass = steamLogin.getEncryptedPassword(rsaData, password)
        responseCookies, responseText = steamLogin.requestToDoLogin(doNotCache, encryptedPass, username, twoFA,
                                                                    gid, captcha, sessionID, timestamp)
        temp = responseText.split(",")
        responseLoginComplete = temp[2].replace(",", '')
        responseLoginComplete = responseLoginComplete.replace('"', "")
        if responseText.startswith('{"success":true') and responseLoginComplete == "login_complete:true":
            configList = cleanToList(responseCookies, responseText)
            configList.append("username="+username)
            configFileValidation.saveConfigListToFile(configList)
            return "Login Complete"
        else:
            if responseLoginComplete.startswith("message:"):
                return responseLoginComplete[8:len(responseLoginComplete)]
            return "Connection Error"
