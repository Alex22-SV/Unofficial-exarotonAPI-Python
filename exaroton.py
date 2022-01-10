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
        path = "/account/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 1:
        path ="/servers/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 2:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 3:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/logs/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 4:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/logs/share/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 5:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/options/ram/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 6:
        serverID = input("Please enter the server ID: ")
        value = input("Please enter the new amount of RAM: ")
        path = f"/servers/{serverID}/options/ram/"
        HTTPSoption = "POST"
        value = {"ram": value}
        return path, HTTPSoption, value
    if optionID == 7:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/options/motd/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 8:
        serverID = input("Please enter the server ID: ")
        value = input("Please enter the new server MOTD: ")
        path = f"/servers/{serverID}/options/motd/"
        HTTPSoption = "POST"
        value = {"motd": value}
        return path, HTTPSoption, value
    if optionID == 9:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/start/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 10:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/stop/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 11:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/restart/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 12:
        serverID = input("Please enter the server ID: ")
        value = input("Please enter the command to execute: ")
        path = f"/servers/{serverID}/command/"
        HTTPSoption = "POST"
        value = {"command": value}
        return path, HTTPSoption, value
    if optionID == 13:
        serverID = input("Please enter the server ID: ")
        path = f"/servers/{serverID}/playerlists/"
        HTTPSoption = "GET"
        value = {}
        return path, HTTPSoption, value
    if optionID == 14:
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