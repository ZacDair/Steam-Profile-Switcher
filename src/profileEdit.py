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
    print(content)

    # Define our pre and post needles for each piece of data we need
    preProfileData = "g_rgProfileData = "
    postProfileData = ";"
    preLocation = '.gif">'
    postLocation = '</div>'
    preName = '<bdi>'
    postName = '</bdi>'

    # Use our custom method to retrieve data in between the pre and post needles
    profileData = retrieveMiddleElement(preProfileData, postProfileData, content)
    location = retrieveMiddleElement(preLocation, postLocation, content)
    actualName = retrieveMiddleElement(preName, postName, html)

    # Convert our profileData string into a dict (as it shares the same structure)
    profileDataDict = json.loads(profileData)

    # Add actualName to the profileDataDict
    profileDataDict['real_name'] = actualName

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

    #

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
    print(req)
    print(responseContent)
    if responseContent.startswith('{"success":true'):
        print("Successful Edit...")
        return True
    elif responseContent.startswith('{"success":1'):
        print("Successful Edit...")
        return True
    else:
        print("Failed Edit...")
        return False


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


def uploadName(name):
    if configFileValidation.validateConfigFile():
        configs = configFileValidation.getConfigs()
        url = configs['customUrl'] + 'edit/'
        body = {'sessionID': configs['sessionid'], 'type': 'profileSave', 'weblink_1_title': '','weblink_1_url': '',
                'weblink_2_title': '', 'weblink_2_url': '', 'weblink_3_title': '', 'weblink_3_url': '',
                'personaName': name, 'real_name': '', 'customURL': '', 'country': 'IE',
                'state': '', 'city': '', 'summary': 'test bio', 'json': 1}
        cookies = getCookies()
        req = requests.post(url, data=body, cookies=cookies)
        res = validateResponse(req)
        if res:
            print("Named Changed")
            return True
        else:
            print("Name Change Request Failed...")
            return False
    else:
        print("Config file was deemed invalid")
        return False


def uploadBio(bio):
    if configFileValidation.validateConfigFile():
        configs = configFileValidation.getConfigs()
        url = configs['customUrl'] + 'edit/info'
        body = {'sessionID': configs['sessionid'], 'type': "profileSave", 'summary': bio}
        cookies = getCookies()
        req = requests.post(url, data=body, cookies=cookies)
        res = validateResponse(req)
        if res:
            print("Bio Changed")
            return True
        else:
            print("Bio Change Request Failed...")
            return False
    else:
        print("Config file was deemed invalid")
        return False

'''
sessionID:6a1914ebc5394ec1f01e23af
type:profileSave
weblink_1_title:
weblink_1_url:
weblink_2_title:
weblink_2_url:
weblink_3_title:
weblink_3_url:
personaName:Crimson Crisis 
real_name:Zac
customURL:crimsoncrisis2011
country:IE
state:
city:
summary:test bio
json:1

All of the above is needed in the body of the request - look into pulling current info before doing the change,
as if left blank they overwrite whats actually there
'''