import os
from shutil import copy, rmtree

# List of accepted images formats
acceptedImageFormats = (".png", ".jpeg", ".jpg", ".gif", ".PNG", ".JPEG", ".JPG", ".GIF")
cwd = os.getcwd()
# Clean CWD path into our main projects path
mainDir = cwd[:-4]
profilesPath = os.path.join(mainDir, "Profiles")


# Function checks if a profiles directory exists if not it creates one
def checkProfilesDirExists():
    if os.path.exists(profilesPath) and os.path.isdir(profilesPath):
        print("Profiles Directory was found")
    else:
        print("Profiles Directory was missing, creating one now...")
        try:
            os.mkdir(profilesPath)
        except OSError as e:
            print("An Error Occurred...")
            print(e)


# Check that the Profiles folder contains sub directories containing an image, name.txt, bio.txt
def checkProfilesDirContents():
    profilesContents = os.listdir(profilesPath)
    validProfiles = []
    for entry in profilesContents:
        if os.path.isdir(os.path.join(profilesPath, entry)):
            entryContents = os.listdir(os.path.join(profilesPath, entry))
            containsProfileDetails = False
            containsImg = False
            for subEntry in entryContents:
                if subEntry == "profileDetails.txt":
                    containsProfileDetails = True
                elif subEntry.endswith(acceptedImageFormats):
                    containsImg = True
            if containsProfileDetails and containsImg:
                validProfiles.append(entry)
    return validProfiles


# Get Profiles contents
def getProfiles():
    checkProfilesDirExists()
    profiles = checkProfilesDirContents()
    return profiles


# Get actual profile details using a dict to store the values
def getProfileDetails(dirname):
    res = {"name": "None",
           "bio": "None",
           "img": "None"}
    dirContents = os.listdir(os.path.join(profilesPath, dirname))
    for entry in dirContents:
        if entry == "profileDetails.txt":
            file = open(os.path.join(profilesPath, dirname, entry), "r")
            lines = file.readlines()
            if len(lines) > 0:
                res["name"] = lines.pop(0)
                res["bio"] = lines
            else:
                print("profileDetails.txt is empty")
        elif entry.endswith(acceptedImageFormats):
            res["img"] = entry
    return res


# Create a new folder containing the profile details and image
def createNewProfile(profileDetails):
    try:
        newProfileDir = os.path.join(profilesPath, profileDetails[0])
        os.mkdir(newProfileDir)
        detailsFile = open(os.path.join(newProfileDir, "profileDetails.txt"), "w+")
        detailsFile.write(profileDetails[0]+"\n")
        detailsFile.write(profileDetails[1] + "\n")
        copy(profileDetails[2], newProfileDir)
        print("New Profile Created")
        return profileDetails[0]
    except OSError as e:
        print("OS error: ", e)
        return False
    except IndexError:
        print("There was no value found at index 0")
        return False


def deleteProfileFolder(profileName):
    try:
        rmtree(os.path.join(profilesPath, profileName))
        print("Deleted Profile: ", profileName)
        return True
    except OSError as e:
        print("OS Error: ", e)
        return False
