import requests
import json
import configFileValidation


# Needle data finding code, splits the content by a pre and post string, in order to return the central string
def retrieveMiddleElement(preNeedle, postNeedle, content):
    try:
        firstHalf = content.split(preNeedle)
        secondHalf = firstHalf[1].split(postNeedle)
        return secondHalf[0]
    except IndexError:
        return "Not Found"


# returns the class corresponding to the class name given
def retrieveClass(className, content):
    divContent = retrieveMiddleElement('<div class="' + className + '">', "</div>", content)
    return divContent


# Cleans profile data such as custom url, name, bio and country from the profile html code
def getCurrentProfileData(customUrl):
    # Send a request to the profile page and decode and store the content
    req = requests.get(customUrl)
    html = str(req.content)
    content = req.content.decode('utf-8')

    # Define our pre and post needles for each piece of data we need
    profileDataClassName = "responsive_page_template_content"
    preProfileData = "g_rgProfileData = "
    postProfileData = ";"
    locationClassName = "header_real_name ellipsis"
    preLocation = '.gif">'
    postLocation = '</div>'
    preName = '<bdi>'
    postName = '</bdi>'
    preAvatar = 'https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/avatars/'
    postAvatar = '_full.jpg">'

    # Use our custom method to retrieve data in between the pre and post needles
    profileClass = retrieveClass(profileDataClassName, content)
    profileData = retrieveMiddleElement(preProfileData, postProfileData, profileClass)
    locationClass = retrieveClass(locationClassName, content)
    location = retrieveMiddleElement(preLocation, postLocation, locationClass)
    nameClass = retrieveClass(locationClassName, html)
    actualName = retrieveMiddleElement(preName, postName, nameClass)
    avatarCode = retrieveMiddleElement(preAvatar, postAvatar, content)

    # Convert our profileData string into a dict (as it shares the same structure)
    profileDataDict = json.loads(profileData)

    # Add actualName to the profileDataDict
    profileDataDict['real_name'] = actualName

    # Concatenate the avatar code and leading url into a full usable url, append the url to the profileDataDict
    profileDataDict['avatarURL'] = preAvatar+avatarCode

    # From the profileData get the custom url (trim un-needed data ie: HTTPS://Steam......"
    url = profileDataDict['url']
    idIndex = profileDataDict['url'].find('id')
    profileDataDict['url'] = url[idIndex + 3:len(url)-1]

    # Strip leading spaces from the location data split by comma and store each location section separately
    location = location.strip()
    location = location.split(",")
    # Reverse the location as its given by city, state, country if there is 3 values
    location.reverse()
    locationNames = ["country", "state", "city"]
    i = 0
    while i < len(location):
        profileDataDict[locationNames[i]] = location[i]
        i = i + 1
    return profileDataDict


# Compiles a cookie jar with the configs required for steam
def getCookies():
    configs = configFileValidation.getConfigs()
    try:
        sessionID = configs['sessionid']
        steamID = configs['steamid']
        smAuthName = 'steamMachineAuth' + steamID
        cookies = {smAuthName: configs[smAuthName], 'steamRememberLogin': configs['steamRememberLogin'],
                    'sessionid': sessionID, 'steamLoginSecure': configs['steamLoginSecure']}
        return cookies
    except KeyError:
        print("An error occurred, a required config was missing...")
        return False


# Validates an editing request (two types of success responses, one true, and one 1)
def validateResponse(req):
    responseContent = req.content.decode('utf-8')
    if responseContent.startswith('{"success":true'):
        print("Successful Edit...")
        return True
    elif responseContent.startswith('{"success":1'):
        print("Successful Edit...")
        return True
    else:
        print("Failed Edit...")
        print(responseContent)
        return False


# Function to hit the location urls, returning the code based on the location key and value
def getCodeFromString(locationKey, locationVal, codeName, url, cookies):
    resp = requests.get(url, cookies=cookies)
    content = json.loads(resp.content)
    resultCode = ''
    for x in content:
        if x[locationKey] == locationVal:
            resultCode = x[codeName]
    return resultCode


# Function that runs error checking on the profileData dict to find the location data
def convertLocationToCode(dataDict):
    country = ''
    state = ''
    city = ''

    # Try to retrieve the location data by key
    try:
        country = dataDict["country"].strip()
        state = dataDict["state"].strip()
        city = dataDict["city"].strip()
    except KeyError:
        print("One of the location keys was missing data...")
    if country != '':
        url = "https://steamcommunity.com/actions/QueryLocations/"
        cookies = getCookies()
        country = getCodeFromString("countryname", country, "countrycode", url, cookies)
        if state != '':
            state = getCodeFromString("statename", state, "statecode", url+country, cookies)
            if city != '':
                city = getCodeFromString("cityname", city, "citycode", url+country+"/"+state, cookies)
    return country, state, city


def uploadAvatar(imagePath):
    if configFileValidation.validateConfigFile():
        file = {'avatar': open(imagePath, 'rb')}
        configs = configFileValidation.getConfigs()
        cookies = getCookies()
        url = "https://steamcommunity.com/actions/FileUploader"
        body = {'type': 'player_avatar_image',
                'sId': configs['steamid'],
                'sessionid': configs['sessionid'],
                'doSub': 1,
                'json': 1,
                }
        req = requests.post(url, data=body, cookies=cookies, files=file)
        res = validateResponse(req)
        if res:
            print("Avatar Changed")
            return True
        else:
            print("Avatar Change Request Failed...")
            return False
    else:
        print("Config file was deemed invalid")
        return False


def updateProfileData(newName, newSummary):
    if configFileValidation.validateConfigFile():
        configs = configFileValidation.getConfigs()
        url = configs['customUrl'] + 'edit/'
        profileData = getCurrentProfileData(configs['customUrl'])
        country, state, city = convertLocationToCode(profileData)

        # Formulate our body with the data to update and old data to keep
        body = {'sessionID': configs['sessionid'], 'type': 'profileSave', 'weblink_1_title': '','weblink_1_url': '',
                'weblink_2_title': '', 'weblink_2_url': '', 'weblink_3_title': '', 'weblink_3_url': '',
                'personaName': newName, 'real_name': profileData['real_name'], 'customURL': profileData['url'],
                'country': country, 'state': state, 'city': city, 'summary': newSummary, 'json': 1}
        cookies = getCookies()
        req = requests.post(url, data=body, cookies=cookies)
        res = validateResponse(req)
        if res:
            print("Profile Updated")
            return True
        else:
            print("Profile Update Request Failed...")
            return False
    else:
        print("Config file was deemed invalid")
        return False