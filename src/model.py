import profileValidation
import configFileValidation


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
        profileValidation.deleteProfileFolder(profile[0])
        return True
    except IndexError as e:
        print("Error has occurred ...")
        print(e)
        return False


def getProfileDetails(index):
    profiles = profileValidation.getProfiles()
    try:
        return profileValidation.getProfileDetails(profiles[0])
    except IndexError as e:
        print("Error has occurred ...")
        print(e)
        return False
