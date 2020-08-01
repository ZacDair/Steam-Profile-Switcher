from tkinter import TclError, END
import view
import model

# Create and store a reference to our application's main window and children
mainWindow = view.createMainWindow()
mainWindowChildren = mainWindow.children


# Ask model to find our profiles, then update our view accordingly
def updateProfileList():
    profiles, updateLabel = model.getProfiles()
    view.populateScrollBox(profiles, mainWindow)
    view.updateScrollBoxLabel(updateLabel, mainWindow)


# Store our scrollBox selection, get our profile details and get view to update the details
def triggerSelectionLogic(event):
    selection = view.processScrollBoxSelection(mainWindow, scrollBox)
    profileDetails = model.getProfileDetails(selection)
    if profileDetails:
        view.updateProfileDetails(mainWindow, profileDetails)
        view.selection = profileDetails["name"].strip("\n")


# Login logic TODO: implemented the commented functionality
def triggerLoginLogic(event):
    '''if model.isLoggedIn():
            view.updateStatusLabel("Logged in as ...")
        else:
            view.createLoginWindow'''
    label = view.getStatusLabel(mainWindow)
    label.configure(text="this should come up")


# Calls the model to delete the selected profile
def deleteProfile(window):
    selection = view.processScrollBoxSelection(mainWindow, scrollBox)
    if model.deleteProfile(selection):
        view.clearScrollBox(scrollBox)
        updateProfileList()
    else:
        view.createAlertWindow(mainWindow, "Unable to delete the profile")
    window.destroy()


# Calls the model to create the profile
def createProfile(window):
    newProfileData = []

    # Retrieve all of our frames and input elements
    inputFrame = window.children.get("inputFrame")
    avatarFrame = inputFrame.children.get("avatarFrame")
    bioFrame = inputFrame.children.get("!frame")
    nameInput = inputFrame.children.get("nameInput")
    imageInput = avatarFrame.children.get("imageInput")
    bioInput = bioFrame.children.get("bioInput")

    # Retrieve the data inputted
    newProfileData.append(nameInput.get())
    newProfileData.append(bioInput.get('1.0', END))
    newProfileData.append(imageInput.get())

    if model.saveProfile(newProfileData):
        view.clearScrollBox(scrollBox)
        updateProfileList()
    else:
        view.createAlertWindow(mainWindow, "Unable to create the profile")
    window.destroy()


# Function creates the delete window and stores a reference of it
def createDeleteProfileWindow():
    deleteWindow = view.createDeleteWindow(mainWindow)
    if deleteWindow:
        children = deleteWindow.children
        yesButton = children.get("yesButton")
        yesButton.configure(command=lambda: deleteProfile(deleteWindow))
    else:
        print("The delete window was not created...")


# Function creates the profile creation window
def createProfileCreateWindow():
    createWindow = view.createProfileCreateWindow(mainWindow)
    if createWindow:
        children = createWindow.children
        frame = children.get("controlFrame")
        saveButton = frame.children.get("saveButton")
        saveButton.configure(command=lambda: createProfile(createWindow))
    else:
        print("The create window was not created...")


# Event listener for the scrollBox
scrollBox = view.getScrollBoxItem(mainWindow, "scrollBox")
scrollBox.bind('<<ListboxSelect>>', triggerSelectionLogic)

# Event listener for the login status label
statusLabel = view.getStatusLabel(mainWindow)
statusLabel.bind('<Button-1>', triggerLoginLogic)


# Event listeners for the main screen TODO: potentially isolate the lamda functions into local calls
controlFrame = mainWindowChildren.get("controlFrame")
topFrame = mainWindowChildren.get("topFrame")

deleteProfileButton = controlFrame.children.get("deleteProfileButton")
createProfileButton = controlFrame.children.get("createProfileButton")
switchProfileButton = controlFrame.children.get("switchProfileButton")
helpButton = controlFrame.children.get("helpButton")
configButton = topFrame.children.get("configButton")

deleteProfileButton.configure(command=createDeleteProfileWindow)
createProfileButton.configure(command=createProfileCreateWindow)
helpButton.configure(command=lambda: view.createAlertWindow(mainWindow, "Help will go here...\n.\n.\nthis should be a good help notice"))
configButton.configure(command=lambda: view.createConfigWindow(mainWindow))


# Initial check for profiles, either populates the scrollBox, or will create an empty dir if needed
updateProfileList()

# Run our main application
mainWindow.mainloop()
