import requests
import steam.steamid as steamid

class discord():
	base_url = 'https://discordapp.com/api'
	headers = {'User-Agent': 'DiscordBot ({}, {})', 'Authorization': 'Bot {}'}
	class oauth():
		def authorize(client_id, permissions):
			return f'{discord.base_url}/oauth2/authorize?client_id={client_id}&scope=bot&permissions={permissions}'

class steam():
	base_url = 'http://api.steampowered.com'
	class ISteamUserStats():
		class_url = 'ISteamUserStats'
		def GetUserStatsForGame(appid, key, steamid):
			method_url = f'{steam.base_url}/{steam.ISteamUserStats.class_url}/GetUserStatsForGame/v0002/?appid={appid}&key={key}&steamid={steamid}'
			request = requests.get(method_url)
			request = request.json()
			return request
	class ISteamUser():
		class_url = 'ISteamUser'
		def GetPlayerSummaries(key, steamid):
			method_url = f'{steam.base_url}/{steam.ISteamUser.class_url}/GetPlayerSummaries/v0002/?key={key}&steamids={steamid}'
			request = requests.get(method_url)
			request = request.json()
			return request
	class utils():
		def converter(id):
			sid = steamid(id=id)
			return sid
