import view
import model

mainWindow = view.createMainWindow()


# Ask model to find our profiles, then update our view accordingly
def updateProfileList():
    profiles, updateLabel = model.getProfiles()
    view.populateScrollBox(profiles, mainWindow)
    view.updateScrollBoxLabel(updateLabel, mainWindow)


# Pass our scrollBox and mainWindow to the view
def triggerSelectionLogic(event):
    selection = view.processScrollBoxSelection(mainWindow, scrollBox)
    profileDetails = model.getProfileDetails(selection)
    view.updateProfileDetails(mainWindow, profileDetails)


# Event listener for the scrollBox
scrollBox = view.getScrollBoxItem(mainWindow, "scrollBox")
scrollBox.bind('<<ListboxSelect>>', triggerSelectionLogic)

# Initial check for profiles, either populates the scrollBox, or will create an empty dir if needed
updateProfileList()

# Run our main application
view.runWindow(mainWindow)
