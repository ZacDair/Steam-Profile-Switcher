import time
from tkinter import END
import view
import model
import threading

# Create and store a reference to our application's main window and children
mainWindow = view.createMainWindow()
mainWindowChildren = mainWindow.children


# Check to see if we are logged in update label accordingly using a thread
def updateStatusLabel():
    label = view.getStatusLabel(mainWindow)
    loginStatus, loggedIn = model.checkLogin()
    label.configure(fg="blue", text=loginStatus)


updateStatusLabelThread = threading.Thread(target=updateStatusLabel)
updateStatusLabelThread.daemon = True
updateStatusLabelThread.start()


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


# Event triggered by login button, attempts a login
def triggerLoginLogic(event):
    loginStatusString, loginStatusBool = model.checkLogin()
    if not loginStatusBool:
        # Create our login window
        loginWindow = view.createLoginWindow(mainWindow)

        # Get our login window elements
        inputFrame = loginWindow.children.get("inputFrame")
        labelFrame = loginWindow.children.get("labelFrame")
        buttonFrame = loginWindow.children.get("controlFrame")
        progressFrame = loginWindow.children.get("progressFrame")
        usernameInput = inputFrame.children.get("usernameInput")
        passwordInput = inputFrame.children.get("passwordInput")
        twoFAInput = inputFrame.children.get("twoFAInput")
        captchaInput = inputFrame.children.get("captchaInput")
        captchaImageLabel = labelFrame.children.get("captchaImageLabel")
        loginButton = buttonFrame.children.get("loginButton")
        progressBar = progressFrame.children.get("progressBar")
        responseLabel = progressFrame.children.get("loginResponseLabel")

        # Check if we need a captcha
        captchaNeeded, sessionID, gid = model.captchaNeeded()
        if captchaNeeded:
            # Set captcha image label to the stored image
            view.setCaptchaImage(captchaImageLabel)

        # function to update our progress bar when called - conditional check to see if a thread gets stopped
        def updateProgressBar():
            activeThreads = threading.activeCount()
            progressBar['value'] = 0
            while progressBar['value'] <= 100 and activeThreads >= 3:
                activeThreads = threading.activeCount()
                progressBar['value'] = progressBar['value'] + 0.7325
                time.sleep(0.18)

        # Retrieve data from our input fields and attempt to login using a thread
        def doLogin():
            responseLabel.configure(fg="black", text="")
            username = usernameInput.get()
            password = passwordInput.get()
            twoFA = twoFAInput.get()
            captchaCode = captchaInput.get()
            if len(password) != 0:
                loginResponse = model.tryToLogin(username, password, twoFA, captchaCode, gid, sessionID)
                # Update our label according to our login response
                if loginResponse == "Username Error":
                    responseLabel.configure(fg="red", text="An error occurred please check your username...")
                elif loginResponse == "Connection Error":
                    responseLabel.configure(fg="red", text="An connection error occurred...")
                elif loginResponse == "Login Complete":
                    responseLabel.configure(fg="green", text="Successfully Logged in...")
                else:
                    responseLabel.configure(fg="red", text=loginResponse)
            else:
                responseLabel.configure(fg="red", text="Please enter a password...")

        # Function creates a thread and runs the doLogin
        def callDoLogin():
            loginThread = threading.Thread(target=doLogin, args=())
            loginThread.daemon = True
            loginThread.start()

            # Update the progress bar while function runs
            progressBarThread = threading.Thread(target=updateProgressBar, args=())
            progressBarThread.daemon = True
            progressBarThread.start()

        # Set loginButton event to run the doLogin function above
        loginButton.configure(command=callDoLogin)

    # Edit our main window label
    mainWindowLabel = view.getStatusLabel(mainWindow)
    mainWindowLabel.configure(fg="blue", text=loginStatusString)


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

    # If a new profile was saved, clear and repopulate the scrollBox else generate an alert
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


# Event listeners for the main screen TODO: potentially isolate the lambda functions into local calls
controlFrame = mainWindowChildren.get("controlFrame")
topFrame = mainWindowChildren.get("topFrame")

deleteProfileButton = controlFrame.children.get("deleteProfileButton")
createProfileButton = controlFrame.children.get("createProfileButton")
switchProfileButton = controlFrame.children.get("switchProfileButton")
helpButton = controlFrame.children.get("helpButton")
configButton = topFrame.children.get("configButton")

deleteProfileButton.configure(command=createDeleteProfileWindow)
createProfileButton.configure(command=createProfileCreateWindow)
helpButton.configure(command=lambda: view.createAlertWindow(mainWindow, "Help will go here..."))
configButton.configure(command=lambda: view.createConfigWindow(mainWindow))

# Initial check for profiles, either populates the scrollBox, or will create an empty dir if needed
updateProfileList()

# Run our main application
mainWindow.mainloop()
