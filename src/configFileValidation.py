import os

# Init variables
configFilename = "config.cfg"
configFileRequirements = ["sessionID:", "steamID64:", "authCode:", "countryCode:"]
requirementCount = len(configFileRequirements)


# Create the config file based on the requirements list
def createConfigFile():
    print("Creating file...")
    configFile = open(configFilename, "w+")
    for x in configFileRequirements:
        configFile.write(x + "\n")
    configFile.close()


# Validate the contents of the config file
def validateConfigFile():
    configFile = open(configFilename, "r")
    lines = configFile.readlines()
    configFile.close()
    isValid = True

    # Cycle through the file contents if its more than or equal to the requirements
    if len(lines) >= requirementCount:
        i = 0
        while i < requirementCount:

            # Check our lines start with the requirements
            if not lines[i].startswith(configFileRequirements[i]):
                isValid = False
            i = i + 1
    else:
        isValid = False

    # If the file was not valid, recreate a valid version
    if not isValid:
        createConfigFile()


# Function to see if a config file exists
def findConfigFile():
    # Check if the config.cfg exists
    if os.path.exists(configFilename):
        validateConfigFile()
        print("Config File is ok...")
    else:
        print("Config file was missing, creating one now...")
        createConfigFile()


# Retrieve configuration data from the config file
def getConfigs():
    validateConfigFile()
    configFile = open(configFilename, "r")
    lines = configFile.readlines()
    configFile.close()
    configDict = {"sessionID": "None",
                  "steamID64": "None",
                  "authCode": "None",
                  "countryCode": "None"}
    for line in lines:
        temp = line.split(":")
        try:
            configDict[temp[0]] = temp[1].strip("\n")
        except KeyError:
            print("Error " + temp[0] + " was not a key in the config dict")
    return configDict


# Save the configs to the config.cfg file
def saveConfigsToFile(configDict):
    configFile = open(configFilename, "w+")
    for x in configFileRequirements:
        configFile.write(x + configDict[x.strip(":")] + "\n")
    configFile.close()
    print("Saved new configurations to config.cfg")


# Save request response as configs
def saveConfigListToFile(configList):
    configFile = open(("../"+configFilename), "w+")
    for x in configList:
        configFile.write(x + "\n")
    configFile.close()
    print("Saved new configurations to config.cfg")
