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


# Save the configurations stored in the dict passed as an argument
def saveConfigs(configs):
    configFileValidation.saveConfigsToFile(configs)


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
    if response == "No Connection":
        return "Please check Steam server status...", False
    elif response:
        return "Logged in to Steam", True
    else:
        return "Please click here to login", False


# Send our first login request to get the rsa key and check if we need a captcha
def captchaNeeded():
    return steamLogin.CaptchaRequired()


def tryToLogin(username, password, twoFA, captcha, gid, sessionID):
    rsaData = steamLogin.getRSAData(username)
    doNotCache = steamLogin.getDoNotCache()
    timestamp = steamLogin.getTimestamp(rsaData)
    encryptedPass = steamLogin.getEncryptedPassword(rsaData, password)
    loginResponse = steamLogin.requestToDoLogin(doNotCache, encryptedPass, username, twoFA,
                                                gid, captcha, sessionID, timestamp)
    return loginResponse
