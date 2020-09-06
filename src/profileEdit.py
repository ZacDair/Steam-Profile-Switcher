import requests
import configFileValidation


def uploadAvatar(imagePath):
    file = {'avatar': open(imagePath, 'rb')}
    if configFileValidation.validateConfigFile():
        configs = configFileValidation.getConfigs()
        steamID = configs['steamid']
        sessionID = configs['sessionid']
        smAuthName = 'steamMachineAuth' + steamID
        url = "https://steamcommunity.com/actions/FileUploader"
        body = {'type': 'player_avatar_image',
                'sId': configs['steamid'],
                'sessionid': configs['sessionid'],
                'doSub': 1,
                'json': 1,
                }
        cookies = {smAuthName: configs[smAuthName], 'steamRememberLogin': configs['steamRememberLogin'],
                   'sessionid': sessionID, 'steamLoginSecure': configs['steamLoginSecure']}
        req = requests.post(url, data=body, cookies=cookies, files=file)
        responseContent = req.content.decode('utf-8')
        if responseContent.startswith('{"success":true'):
            print("File was uploaded...")
            return True
        else:
            print("File was not uploaded...")
            return False

def uploadName(name):
    pass
