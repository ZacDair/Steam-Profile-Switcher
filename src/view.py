from tkinter import Tk, Label, Listbox, SINGLE, scrolledtext, Button, Frame, BOTH, N, E, S, W

# Init variables
profiles = []
statusString = "Status: Waiting..."


# Class for window objects (such as main screen and popups)
class MainWindow(Frame):

    def __init__(self):
        super().__init__()

    def initUI(self):
        # Create our applications main window
        self.master.title("Steam Profile Switcher")
        self.pack(fill=BOTH, expand=True)

        # Configure our rows and columns accordingly
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        # Status label
        statusLabel = Label(self, text=statusString)
        statusLabel.grid(sticky=W, pady=4, padx=5)

        # ScrollBox label
        scrollBoxLabel = Label(self, text="Searching for profiles...")
        scrollBoxLabel.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

        # Scroll box for profiles
        scrollBox = Listbox(self, selectmode=SINGLE)
        scrollBox.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

        # Label for selected profile section and the details
        selectedProfileLabel = Label(masterWindow, text="Selected Profile Details:")
        selectedProfileLabel.grid(column=2, row=2)
        profileNameLabel = Label(masterWindow, text="Profile Name: ")
        profileNameLabel.grid(column=2, row=3)
        profileImgLabel = Label(masterWindow, text="Profile Image: ")
        profileImgLabel.grid(column=2, row=4)
        profileBioLabel = Label(masterWindow, text="Profile Bio: ")
        profileBioLabel.grid(column=2, row=5)

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


# Initialize and return our application's main window
def createMainWindow():
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
    return masterWindow

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