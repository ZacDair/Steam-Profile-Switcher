# Import dependencies (TODO: possibly need a version check as python 2 is Tkinter, python 3 is tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename

from src import profileValidation, configFileValidation

# Create our applications main window
masterWindow = Tk()
masterWindow.title("Steam Profile Switcher")
masterWindow.geometry('700x700')

# Status label
statusLabel = Label(masterWindow, text="Status: Waiting....")
statusLabel.grid(row=0)

# ScrollBox label
scrollBoxLabel = Label(masterWindow, text="Searching for profiles...")
scrollBoxLabel.grid(column=1, row=1)

# Scroll box for profiles
scrollBox = Listbox(masterWindow, width=50, selectmode=SINGLE)
scrollBox.grid(column=1, row=2)

# Label for selected profile section and the details
selectedProfileLabel = Label(masterWindow, text="Selected Profile Details:")
selectedProfileLabel.grid(column=2, row=2)
profileNameLabel = Label(masterWindow, text="Profile Name: ")
profileNameLabel.grid(column=2, row=3)
profileImgLabel = Label(masterWindow, text="Profile Image: ")
profileImgLabel.grid(column=2, row=4)
profileBioLabel = Label(masterWindow, text="Profile Bio: ")
profileBioLabel.grid(column=2, row=5)


# Populate our scroll box with the valid profiles
def populateScrollBox():
    profilesList = profileValidation.getProfiles()
    newScrollBoxText = "Searching for profiles..."
    for profile in profilesList:
        scrollBox.insert(END, profile)
    profileCount = len(profilesList)
    if profileCount != 0:
        newScrollBoxText = "Found " + str(profileCount) + " Profiles."
        # Cheeky way to remove the s from profiles, if there is only one found
        if profileCount == 1:
            newScrollBoxText = newScrollBoxText.replace("s.", ".")
    scrollBoxLabel.configure(text=newScrollBoxText)
    return profilesList


profiles = populateScrollBox()
userConfigs = configFileValidation.getConfigs()


# Change our profiles section labels to represent the selected profile
def displaySelectedProfileDetails(event):
    # Get the listbox selection index (returned as tuple)
    selectedItem = scrollBox.curselection()
    if len(selectedItem) > 0:
        profileDetails = profileValidation.getProfileDetails(profiles[selectedItem[0]])
        try:
            profileNameLabel.configure(text="Profile Name: " + profileDetails["name"].replace("\n", ""))
            profileImgLabel.configure(text="Profile Image: " + profileDetails["img"])
            if profileDetails["bio"] != "None":
                miniBioList = profileDetails["bio"]
                profileBioLabel.configure(text="Profile Bio: " + miniBioList[0].replace("\n", "") + "...")
            else:
                profileBioLabel.configure(text="Profile Bio: " + profileDetails["name"])
        except KeyError:
            print("Key error was found in the profile details dict")
        except IndexError:
            print("Index error, check bio")
    else:
        print("Nothing selected to display")


# Update our configuration dict with the new values
def updateConfigDict(configInputBoxes, configWindow):
    i = 0
    for key in userConfigs:
        userConfigs[key] = configInputBoxes[i].get()
        i = i + 1
    configFileValidation.saveConfigsToFile(userConfigs)
    configWindow.destroy()


# Generate user input window for configs
def createConfigInputWindow():
    configInputWindow = Tk()
    configInputWindow.title("User Configurations")
    Label(configInputWindow, text="Current Configurations:").grid(row=1, column=1)

    Label(configInputWindow, text="Session ID: ").grid(row=2, column=1)
    Label(configInputWindow, text="Steam ID (64): ").grid(row=3, column=1)
    Label(configInputWindow, text="Auth Code: ").grid(row=4, column=1)
    Label(configInputWindow, text="Country Code: ").grid(row=5, column=1)

    sessionIDInput = Entry(configInputWindow)
    sessionIDInput.grid(row=2, column=2)
    sessionIDInput.insert(0, userConfigs["sessionID"])

    steamID64Input = Entry(configInputWindow)
    steamID64Input.grid(row=3, column=2)
    steamID64Input.insert(0, userConfigs["steamID64"])

    authCodeInput = Entry(configInputWindow)
    authCodeInput.grid(row=4, column=2)
    authCodeInput.insert(0, userConfigs["authCode"])

    countryCodeInput = Entry(configInputWindow)
    countryCodeInput.grid(row=5, column=2)
    countryCodeInput.insert(0, userConfigs["countryCode"])

    configInputBoxes = [sessionIDInput, steamID64Input, authCodeInput, countryCodeInput]

    saveConfigButton = Button(configInputWindow, text="Save", command=lambda: updateConfigDict(configInputBoxes, configInputWindow))
    saveConfigButton.grid(row=6, column=1)
    closeConfigButton = Button(configInputWindow, text="Close", command=configInputWindow.destroy)
    closeConfigButton.grid(row=6, column=2)

    mainloop()


# Open file browser to select an image
def findImageFile(imageInput):
    acceptedFileTypes = [('image files', '.png'),
                         ('image files', '.jpg'),
                         ('image files', '.jpeg'),
                         ('image files', '.gif')]
    selectedFilePath = askopenfilename(filetypes=acceptedFileTypes, title='Choose a file')
    imageInput.insert(0, selectedFilePath)


# Save new profile details
def saveNewProfileDetails(inputBoxes, profileWindow):
    newProfileData = []
    for x in inputBoxes:
        try:
            newProfileData.append(x.get('1.0', END))
        except TypeError:
            newProfileData.append(x.get())
    if profileValidation.createNewProfile(newProfileData):
        scrollBox.insert(END, newProfileData[0])
        profiles.append(newProfileData[0])
    profileWindow.destroy()


# Function to create a profile
def createNewProfileWindow():
    newProfileWindow = Tk()
    newProfileWindow.title("New Profile")
    Label(newProfileWindow, text="Please enter the following:").grid(row=1, column=1)

    Label(newProfileWindow, text="New Steam Name: ").grid(row=2, column=1)

    profileNameInput = Entry(newProfileWindow)
    profileNameInput.grid(row=2, column=2)

    Label(newProfileWindow, text="New Steam Bio: ").grid(row=3, column=1)

    profileBioInput = scrolledtext.ScrolledText(newProfileWindow, height=10, width=15)
    profileBioInput.grid(row=3, column=2)

    Label(newProfileWindow, text="New Steam Avatar: ").grid(row=4, column=1)

    profileImageInput = Entry(newProfileWindow)
    profileImageInput.grid(row=4, column=2)
    browseButton = Button(newProfileWindow, text="Browse", command=lambda: findImageFile(profileImageInput))
    browseButton.grid(row=4, column=3)

    inputBoxes = [profileNameInput, profileBioInput, profileImageInput]
    saveProfileButton = Button(newProfileWindow, text="Save", command=lambda: saveNewProfileDetails(inputBoxes, newProfileWindow))
    saveProfileButton.grid(row=5, column=1)
    closeProfileButton = Button(newProfileWindow, text="Close", command=newProfileWindow.destroy)
    closeProfileButton.grid(row=5, column=2)

    mainloop()


def deleteProfile(selectedIndex, deleteProfileWindow):
    profileValidation.deleteProfileFolder(profiles[selectedIndex])
    scrollBox.delete(0, END)
    populateScrollBox()
    profiles.pop(selectedIndex)
    deleteProfileWindow.destroy()


# Delete a selected profile
def createDeleteProfileWindow():
    selectedItem = scrollBox.curselection()
    if len(selectedItem) > 0:
        deleteAlertWindow = Tk()
        deleteAlertWindow.title("Deleting Profile")
        Label(deleteAlertWindow, text="You are about to delete this profile: ").grid(row=1, column=1)
        Label(deleteAlertWindow, text="Profile Name: " + profiles[selectedItem[0]]).grid(row=2, column=2)
        Label(deleteAlertWindow, text="Are you sure ?").grid(row=3, column=1)
        Button(deleteAlertWindow, text="Yes", command=lambda: deleteProfile(selectedItem[0], deleteAlertWindow)).grid(row=4, column=1)
        Button(deleteAlertWindow, text="No", command=deleteAlertWindow.destroy).grid(row=4, column=2)
    else:
        print("Select a profile first")


# Config button
configButton = Button(masterWindow, text="Configs", command=createConfigInputWindow)
configButton.grid(row=0, column=4)

# Main Control buttons
switchProfileButton = Button(masterWindow, text="Switch Active Profile")
switchProfileButton.grid(row=6, column=2)
createProfileButton = Button(masterWindow, text="Create Profile", command=createNewProfileWindow)
createProfileButton.grid(row=7, column=2)
deleteProfileButton = Button(masterWindow, text="Delete Profile", command=createDeleteProfileWindow)
deleteProfileButton.grid(row=7, column=3)

# Testing generating events
scrollBox.bind('<<ListboxSelect>>', displaySelectedProfileDetails)

# Run our main window
masterWindow.mainloop()
