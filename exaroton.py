import aiohttp
import asyncio
import json

baseURL ="https://api.exaroton.com/v1"
optionID = input("Please enter the option: ")
def checkOptionID(optionID):
    intOptionID = int(optionID)
    if intOptionID > 14:
        return 404
    if intOptionID < 0: 
        return 404
        
check = checkOptionID(optionID)
if check == 404:
    print("Option ID not found") 
    exit()
    
exarotonToken = input("Please enter your exaroton API token: ")

def exaroton(optionID):
    optionID = int(optionID)
    if optionID == 0:
        print('Loading...')
        print('Option: 0')
        print('Description: Get account information')
        path = "/account/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 1:
        print('Loading...')
        print('Option: 1')
        print('Description: List servers')
        path ="/servers/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 2:
        print('Loading...')
        print('Option: 2')
        print('Description: Get a server')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 3:
        print('Loading...')
        print('Option: 3')
        print('Description: Get a server log')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/logs/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 4:
        print('Loading...')
        print('Option: 4')
        print('Description: Upload a server log to mclo.gs')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/logs/share/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 5:
        print('Loading...')
        print('Option: 5')
        print('Description: Get server RAM')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/options/ram/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 6:
        print('Loading...')
        print('Option: 6')
        print('Description: Change server RAM')
        serverID = input("Please enter the server ID: ")
        value = input("Please enter the new amount of RAM: ")
        path = f"/servers/{serverID}/options/ram/"
        HTTPSoption = "POST"
        value = {"ram": value}
        return path, HTTPSoption, value
    if optionID == 7:
        print('Loading...')
        print('Option: 7')
        print('Description: Get server MOTD')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/options/motd/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 8:
        print('Loading...')
        print('Option: 8')
        print('Description: Change server MOTD')
        serverID = input("Please enter the server ID: ")
        value = input("Please enter the new server MOTD: ")
        path = f"/servers/{serverID}/options/motd/"
        HTTPSoption = "POST"
        value = {"motd": value}
        return path, HTTPSoption, value
    if optionID == 9:
        print('Loading...')
        print('Option: 9')
        print('Description: Start a server')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/start/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 10:
        print('Loading...')
        print('Option: 10')
        print('Description: Stop a server')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/stop/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 11:
        print('Loading...')
        print('Option: 11')
        print('Description: Restart a server')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/restart/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 12:
        print('Loading...')
        print('Option: 12')
        print('Description: Execute a server command')
        serverID = input("Please enter the server ID: ")
        value = input("Please enter the command to execute: ")
        path = f"/servers/{serverID}/command/"
        HTTPSoption = "POST"
        value = {"command": value}
        return path, HTTPSoption, value
    if optionID == 13:
        print('Loading...')
        print('Option: 13')
        print('Description: Get available player lists')
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/playerlists/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 14:
        print('Loading...')
        print('Option: 14')
        print('Description: Get player list contents')
        serverID = input("Please enter the server ID: ")
        list = input("Please enter the list: ")
        path = f"/servers/{serverID}/playerlists/{list}"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
        

async def main():
    path, HTTPSoption, value = exaroton(optionID)
    resp = await api_request(baseURL + path, HTTPSoption, value)
    print(json.dumps(resp))

async def api_request(path, method, data):
    headers = {'Authorization': 'Bearer ' + exarotonToken}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=path, data=data) as response:
            return await response.json()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())