import requests
import json
import configFileValidation


# Needle data finding code, splits the content by a pre and post string, in order to return the central string
def retrieveMiddleElement(preNeedle, postNeedle, content):
    firstHalf = content.split(preNeedle)
    secondHalf = firstHalf[1].split(postNeedle)
    return secondHalf[0]


# Cleans profile data such as custom url, name, bio and country from the profile html code
def getCurrentProfileData(customUrl):
    # Send a request to the profile page and decode and store the content
    req = requests.get(customUrl)
    html = str(req.content)
    content = req.content.decode('utf-8')

    # Define our pre and post needles for each piece of data we need
    preProfileData = "g_rgProfileData = "
    postProfileData = ";"
    preLocation = '.gif">'
    postLocation = '</div>'
    preName = '<bdi>'
    postName = '</bdi>'
    preAvatar = 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/'
    postAvatar = '_full.jpg">'

    # Use our custom method to retrieve data in between the pre and post needles
    profileData = retrieveMiddleElement(preProfileData, postProfileData, content)
    location = retrieveMiddleElement(preLocation, postLocation, content)
    actualName = retrieveMiddleElement(preName, postName, html)
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

    # Replace all <br> tags with a \n in the bio
    # profileDataDict['summary'] = str(profileDataDict['summary']).replace("<br>", '\n')

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

    # print and return our profile data
    print(profileDataDict)
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


# Function that runs error checking on the profileData dict to find the location data
def checkLocationByKey(dataDict, key):
    try:
        return dataDict[key]
    except KeyError:
        return ''


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

        # Check which country data needs to be sent (improvement: if there is no country, there is no state etc)
        country = checkLocationByKey(profileData, 'country')
        state = checkLocationByKey(profileData, 'state')
        city = checkLocationByKey(profileData, 'city')

        # Formulate our body with the data to update and old data to keep
        body = {'sessionID': configs['sessionid'], 'type': 'profileSave', 'weblink_1_title': '','weblink_1_url': '',
                'weblink_2_title': '', 'weblink_2_url': '', 'weblink_3_title': '', 'weblink_3_url': '',
                'personaName': newName, 'real_name': profileData['real_name'], 'customURL': profileData['url'], 'country': country,
                'state': state, 'city': city, 'summary': newSummary, 'json': 1}
        cookies = getCookies()
        print(body)
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


'''
Getting a slight error when updating profile data as the country needs to be shorted (Ireland to IE)
And state and city values need to be integers instead of strings
'''