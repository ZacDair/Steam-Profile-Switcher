import os

# Init variables
configFilename = "config.cfg"
configFilePath = "../"+configFilename


# Create the config file based on the requirements list
def createConfigFile():
    print("Creating file...")
    configFile = open(configFilePath, "w+")
    configFile.close()


# Validate the contents of the config file
def validateConfigFile():
    isValid = False
    if os.path.exists(configFilePath):
        contents = getConfigs()
        # Cycle through the file contents if its more than or equal to the requirements
        keys = contents.keys()
        for key in keys:
            try:
                if key == "steamLoginSecure" or key == "steamid" or key == "steamMachineAuth"+contents["steamid"]:
                    isValid = True
            except KeyError:
                print("Steam ID missing from the config.cfg")
        if isValid:
            print("Config file was valid...")
            return True
        else:
            print("Config file was invalid...")
            return False
    else:
        print("Config file was missing...")
        createConfigFile()
        return False


# Function to see if a config file exists
def findConfigFile():
    # Check if the config.cfg exists
    if os.path.exists(configFilePath):
        validateConfigFile()
        print("Config File is valid")
    else:
        print("Config file was missing, creating one now...")
        createConfigFile()


# Retrieve configuration data from the config file
def getConfigs():
    configFile = open(configFilePath, "r")
    lines = configFile.readlines()
    configFile.close()
    configs = {}
    for line in lines:
        temp = line.split("=")
        try:
            configs[temp[0]] = temp[1].strip("\n")
        except KeyError:
            print("Error " + temp[0] + " was not a key in the config dict")
    return configs


# Save request response as configs into the cfg file
def saveConfigListToFile(configList):
    configFile = open(configFilePath, "a")
    for x in configList:
        configFile.write(x + "\n")
    configFile.close()
    print("Saved new configurations to config.cfg")


# Store a single value into the config file
def saveSingleConfigToFile(configName, configValue):
    writeMode = "a"
    if configName == "sessionid":
        writeMode = "w+"
    configFile = open(configFilePath, writeMode)
    configString = configName + "=" + configValue
    configFile.write(configString + "\n")
    configFile.close()
    print("Saved " + configName + " to config.cfg")
