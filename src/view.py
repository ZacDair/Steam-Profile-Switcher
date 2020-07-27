from tkinter import Tk, Label, Listbox, SINGLE, scrolledtext, Button, Frame, BOTH, RAISED, NW, RIGHT, LEFT, TOP, FLAT, BOTTOM, X, Y, PhotoImage, Entry, Toplevel, END
import time

# Init variables
from tkinter.filedialog import askopenfilename

profiles = []
statusString = "Status: Waiting..."


# Class to contain the layout of our main screen
class MainLayout(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.selectedItem = ""

    def initUI(self):
        self.master.title("Steam Profile Switcher")

        # Initialize our frame layout (two bars spanning the width and 50 high, two columns in between the bars)
        topFrame = Frame(self, name="topFrame", relief=FLAT, borderwidth=1)
        topFrame.pack(side=TOP, fill=BOTH)

        controlFrame = Frame(self, name="controlFrame", relief=FLAT, borderwidth=1, height=50)
        controlFrame.pack(side=BOTTOM, fill=BOTH)

        scrollBoxFrame = Frame(self, name="scrollBoxFrame", relief=RAISED, borderwidth=1)
        scrollBoxFrame.pack(side=LEFT, fill=BOTH, expand=True)

        profileDetailsFrame = Frame(self, name="profileDetailsFrame", relief=FLAT, borderwidth=1)
        profileDetailsFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Add our topFrame elements (status label, config button)
        statusLabel = Label(topFrame, name="statusLabel", text=statusString)
        statusLabel.pack(side=LEFT, padx=5, pady=5)
        configButton = Button(topFrame, name="configButton", text="Configs")
        configButton.pack(side=RIGHT, padx=5, pady=5)

        # Add our listbox label, and listbox to the correct frame
        scrollBoxLabel = Label(scrollBoxFrame, name="scrollBoxLabel", text="Searching for Profiles...")
        scrollBoxLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)
        scrollBox = Listbox(scrollBoxFrame, name="scrollBox", selectmode=SINGLE, height=100)
        scrollBox.pack(side=TOP, anchor=NW, fill=BOTH, padx=5, pady=5)

        # Add our profile details labels to the right frame
        selectedProfileLabel = Label(profileDetailsFrame, name="selectedProfileLabel", text="Selected Profile Details:")
        selectedProfileLabel.pack(side=TOP, anchor=NW, padx=5, pady=5)
        profileNameLabel = Label(profileDetailsFrame, name="profileNameLabel", text="Profile Name: ")
        profileNameLabel.pack(side=TOP, anchor=NW, padx=5, pady=10)
        profileImgLabel = Label(profileDetailsFrame, name="profileImgLabel", text="Profile Avatar: ")
        profileImgLabel.pack(side=TOP, anchor=NW, padx=5, pady=10)
        profileBioLabel = Label(profileDetailsFrame, name="profileBioLabel", text="Profile Bio: ", height=20)
        profileBioLabel.pack(side=BOTTOM, anchor=NW, padx=5, pady=10)

        # Add our various buttons, create, delete and switch profile
        helpButton = Button(controlFrame, name="helpButton", text="Help")
        helpButton.pack(side=LEFT, padx=5, pady=5)
        deleteProfileButton = Button(controlFrame, name="deleteProfileButton", text="Delete Profile")
        deleteProfileButton.pack(side=RIGHT, padx=5, pady=5)
        switchProfileButton = Button(controlFrame, name="switchProfileButton", text="Switch Profile")
        switchProfileButton.pack(side=RIGHT, padx=5, pady=5)
        createProfileButton = Button(controlFrame, name="createProfileButton", text="Create Profile")
        createProfileButton.pack(side=RIGHT, padx=5, pady=5)

        # Add our commands to our buttons
        deleteProfileButton.configure(command=lambda: createDeleteWindow(self))
        createProfileButton.configure(command=lambda: createProfileCreateWindow(self))
        configButton.configure(command=lambda: createConfigWindow(self))
        # switchProfileButton.configure(command="")

        self.pack(fill=BOTH, expand=True)


# Class containing the layout of the delete profile window
class DeleteProfileLayout(Frame):
    def __init__(self, deleteWindow):
        super().__init__()
        self.initUI(deleteWindow)

    def initUI(self, deleteWindow):
        deleteWindow.title("Delete Profile")

        warningLabel = Label(deleteWindow, name="warningLabel", text="Are you sure you want to delete this profile: ")
        warningLabel.pack(side=TOP, padx=5, pady=5)
        selectedItemLabel = Label(deleteWindow, name="selectedItemLabel", text="Profile Name")
        selectedItemLabel.pack(side=TOP, padx=5, pady=5)
        yesButton = Button(deleteWindow, name="yesButton", text="Yes")
        yesButton.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)
        noButton = Button(deleteWindow, name="noButton", text="No")
        noButton.pack(side=RIGHT, padx=5, pady=5, expand=True, fill=X)

        self.pack(fill=BOTH, expand=True)


# Class containing the layout for the config window
class ConfigLayout(Frame):
    def __init__(self, configWindow):
        super().__init__()
        self.initUI(configWindow)

    def initUI(self, configWindow):
        configWindow.title("Configurations")

        usernameLabel = Label(configWindow, name="usernameLabel", text="Username: ")
        usernameLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)
        sessionIDLabel = Label(configWindow, name="sessionIDLabel", text="Session ID: ")
        sessionIDLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)
        steamIDLabel = Label(configWindow, name="steamIDLabel", text="Steam ID (64): ")
        steamIDLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)
        authCodeLabel = Label(configWindow, name="authCodeLabel", text="Auth Code: ")
        authCodeLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)
        countryCodeLabel = Label(configWindow, name="countryCodeLabel", text="Country Code: ")
        countryCodeLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)

        self.pack(fill=BOTH, expand=True)


# Class containing the layout for the create profile window
class CreateProfileLayout(Frame):

    def __init__(self, profileWindow):
        super().__init__()
        self.initUI(profileWindow)

    def initUI(self, profileWindow):
        profileWindow.title("Create Profile")

        # Left and right frames to contain Labels and Inputs
        guideLabel = Label(profileWindow, name="guideLabel", text="Please enter the following: ")
        guideLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)

        controlFrame = Frame(profileWindow, name="controlFrame")
        controlFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        labelFrame = Frame(profileWindow, name="labelFrame")
        labelFrame.pack(side=LEFT, fill=BOTH, expand=True)

        inputFrame = Frame(profileWindow, name="inputFrame")
        inputFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        nameLabel = Label(labelFrame, name="nameLabel", text="Steam Name: ")
        nameLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)
        imageLabel = Label(labelFrame, name="imageLabel", text="Steam Avatar: ")
        imageLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)
        bioLabel = Label(labelFrame, name="bioLabel", text="Steam Bio: ")
        bioLabel.pack(side=TOP, padx=5, pady=5, anchor=NW)

        nameInput = Entry(inputFrame, name="nameInput")
        nameInput.pack(side=TOP, padx=5, pady=5, anchor=NW)
        avatarFrame = Frame(inputFrame, name="avatarFrame")
        avatarFrame.pack(side=TOP, padx=5, pady=5, anchor=NW)
        imageInput = Entry(avatarFrame, name="imageInput")
        imageInput.pack(side=LEFT, pady=5, anchor=NW)

        # Open file browser to select an image
        def findImageFile():
            acceptedFileTypes = [('image files', '.png'),
                                 ('image files', '.jpg'),
                                 ('image files', '.jpeg'),
                                 ('image files', '.gif')]
            selectedFilePath = askopenfilename(filetypes=acceptedFileTypes, title='Choose a file')
            imageInput.insert(0, selectedFilePath)

        browseButton = Button(avatarFrame, name="browseButton", text="Browse", command=findImageFile)
        browseButton.pack(side=LEFT, anchor=NW)

        bioInput = scrolledtext.ScrolledText(inputFrame, name="bioInput")
        bioInput.pack(side=TOP, padx=5, pady=5, anchor=NW)

        saveButton = Button(controlFrame, name="saveButton", text="Save")
        saveButton.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)

        exitButton = Button(controlFrame, name="exitButton", text="Exit")
        exitButton.pack(side=RIGHT, padx=5, pady=5, expand=True, fill=X)

        self.pack(fill=BOTH, expand=True)


class AlertLayout(Frame):
    def __init__(self, alertWindow, message):
        super().__init__()
        self.initUI(alertWindow, message)

    def initUI(self, alertWindow, message):
        alertWindow.title("Alert")
        Label(alertWindow, text=message).pack(side=TOP, padx=5, pady=5)
        Button(alertWindow, text="OK", command=alertWindow.destroy).pack(side=TOP, padx=5, pady=5)

        self.pack(fill=BOTH, expand=True)


# Function that will create the main application window
def createMainWindow():
    mainWindow = Tk()
    mainWindow.geometry("550x500+300+300")
    appMain = MainLayout()
    return appMain


# Function that will create the delete application window
def createDeleteWindow(mainWindow):
    if type(mainWindow.selectedItem) == int:
        deleteWindow = Toplevel(mainWindow)
        deleteWindow.geometry("250x200+300+300")
        DeleteProfileLayout(deleteWindow)
        deleteWindow.grab_set()
    else:
        createAlertWindow(mainWindow, "Please select a profile to delete")


# Function that will create the config application window
def createConfigWindow(mainWindow):
    configWindow = Toplevel(mainWindow)
    ConfigLayout(configWindow)
    configWindow.geometry("300x200+300+300")
    configWindow.grab_set()


# Function that will create the create profile application window
def createProfileCreateWindow(mainWindow):
    createWindow = Toplevel(mainWindow)
    createWindow.geometry("450x400+300+300")
    CreateProfileLayout(createWindow)
    createWindow.grab_set()


# Function that will create an alert window
def createAlertWindow(mainWindow, message):
    alertWindow = Toplevel(mainWindow)
    alertWindow.geometry("250x80+450+450")
    AlertLayout(alertWindow, message)
    alertWindow.grab_set()


# Function triggered by an element of the scrollBox being clicked
def processScrollBoxSelection(mainWindow, scrollBox):
    selection = scrollBox.curselection()
    if len(selection) > 0:
        mainWindow.selectedItem = selection[0]
        return selection[0]
    else:
        return False


# Main loop function
def runWindow(mainWindow):
    mainWindow.mainloop()


# Populate our scrollBox based on the profiles list passed in args
def populateScrollBox(profileList, mainWindow):
    scrollBox = getScrollBoxItem(mainWindow, "scrollBox")
    for profile in profileList:
        scrollBox.insert(END, profile)


# Retrieve and update our scroll box status label
def updateScrollBoxLabel(updateLabel, mainWindow):
    scrollBoxLabel = getScrollBoxItem(mainWindow, "scrollBoxLabel")
    scrollBoxLabel.configure(text=updateLabel)


# Use our window and a key to retrieve an element from the scrollBox frame
def getScrollBoxItem(mainWindow, key):
    scrollBoxFrame = mainWindow.children.get("scrollBoxFrame")
    return scrollBoxFrame.children.get(key)


def updateProfileDetails(mainWindow, profileDetails):
    profileDetailsFrame = mainWindow.children.get("profileDetailsFrame")
    NameLabel = profileDetailsFrame.children.get("profileNameLabel")
    imgLabel = profileDetailsFrame.children.get("profileImgLabel")
    bioLabel = profileDetailsFrame.children.get("profileBioLabel")
    try:
        NameLabel.configure(text="Profile Name: " + profileDetails["name"].replace("\n", ""))
        imgLabel.configure(text="Profile Image: " + profileDetails["img"])
        if profileDetails["bio"] != "None":
            miniBioList = profileDetails["bio"]
            bioLabel.configure(text="Profile Bio: " + miniBioList[0].replace("\n", "") + "...")
        else:
            bioLabel.configure(text="Profile Bio: " + profileDetails["name"])
    except KeyError:
        print("Key error was found in the profile details dict")
    except IndexError:
        print("Index error, check bio")