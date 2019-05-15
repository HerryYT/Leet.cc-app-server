# -*- coding:utf-8 -*-

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/api/system/version/get/<string:platform>', methods=['GET'])
def get_device(platform):
	print('[*] Got a message from client on route get device !')

	for key in request.form:
		print(f'{key}: {request.form[key]}')

	data = {
		"ForceUpdateVersion": 100
	}

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/server/get/<string:server_id>/<string:token>', methods=['GET'])
def some_unknown_data(server_id, token):

	print('GOT SERVER ID ON GET SERVER: ' + server_id + " TOKEN: " + token)

	data = {"rconpassword":"12M3BS","ID":1770637,"Credits":99999999999,"PriceDaily":10,"PriceMultiplier":1.0,"DockerName":"leetcc/leetv2-7","Status":True,"Domains":["ALTLIST_COAMING_:).pocket.pe"],"Port":43661,"UserRegistered":False,"UserEmail":None,"MapID":1,"Settings":{"Name":"A LEET Server","OPs":[],"Gamemode":"survival","MaxOnline":5,"ServerVersion":30,"PVP":True,"AlwaysDay":False,"AlwaysSpawn":False,"Ranks":False,"Monsters":True,"Animals":True,"Login":False,"Whitelist":False,"WhitelistPlayers":[],"SpawnProtection":0,"Weather":False},"Statistics":{"PlayersOnline":0,"Players":[],"LastOnlineTime":0,"TimeCreated":1551463580},"Plugins":[{"PluginID":8,"IsActive":False,"IsLocked":True},{"PluginID":9,"IsActive":False,"IsLocked":True},{"PluginID":10,"IsActive":False,"IsLocked":True},{"PluginID":11,"IsActive":False,"IsLocked":True},{"PluginID":12,"IsActive":False,"IsLocked":True},{"PluginID":13,"IsActive":False,"IsLocked":True},{"PluginID":14,"IsActive":False,"IsLocked":True},{"PluginID":15,"IsActive":False,"IsLocked":True},{"PluginID":16,"IsActive":False,"IsLocked":True},{"PluginID":17,"IsActive":False,"IsLocked":True},{"PluginID":18,"IsActive":False,"IsLocked":True},{"PluginID":19,"IsActive":False,"IsLocked":True},{"PluginID":20,"IsActive":False,"IsLocked":True},{"PluginID":21,"IsActive":False,"IsLocked":True},{"PluginID":22,"IsActive":False,"IsLocked":True},{"PluginID":23,"IsActive":False,"IsLocked":True},{"PluginID":25,"IsActive":False,"IsLocked":True},{"PluginID":26,"IsActive":False,"IsLocked":True},{"PluginID":27,"IsActive":False,"IsLocked":True},{"PluginID":28,"IsActive":False,"IsLocked":True},{"PluginID":29,"IsActive":False,"IsLocked":True},{"PluginID":30,"IsActive":False,"IsLocked":True},{"PluginID":32,"IsActive":False,"IsLocked":True},{"PluginID":33,"IsActive":False,"IsLocked":True},{"PluginID":34,"IsActive":False,"IsLocked":True},{"PluginID":35,"IsActive":False,"IsLocked":True},{"PluginID":36,"IsActive":False,"IsLocked":True},{"PluginID":37,"IsActive":False,"IsLocked":True},{"PluginID":38,"IsActive":False,"IsLocked":True},{"PluginID":39,"IsActive":False,"IsLocked":True},{"PluginID":40,"IsActive":False,"IsLocked":True},{"PluginID":41,"IsActive":False,"IsLocked":True},{"PluginID":42,"IsActive":False,"IsLocked":True},{"PluginID":43,"IsActive":False,"IsLocked":True},{"PluginID":46,"IsActive":False,"IsLocked":True},{"PluginID":48,"IsActive":False,"IsLocked":True},{"PluginID":49,"IsActive":False,"IsLocked":True},{"PluginID":50,"IsActive":False,"IsLocked":True},{"PluginID":51,"IsActive":False,"IsLocked":True},{"PluginID":52,"IsActive":False,"IsLocked":True},{"PluginID":53,"IsActive":False,"IsLocked":True},{"PluginID":54,"IsActive":False,"IsLocked":True},{"PluginID":55,"IsActive":False,"IsLocked":True},{"PluginID":56,"IsActive":False,"IsLocked":True},{"PluginID":57,"IsActive":False,"IsLocked":True},{"PluginID":58,"IsActive":False,"IsLocked":True},{"PluginID":59,"IsActive":False,"IsLocked":True},{"PluginID":60,"IsActive":False,"IsLocked":True},{"PluginID":61,"IsActive":False,"IsLocked":True},{"PluginID":62,"IsActive":False,"IsLocked":True},{"PluginID":63,"IsActive":False,"IsLocked":True},{"PluginID":64,"IsActive":False,"IsLocked":True},{"PluginID":65,"IsActive":False,"IsLocked":True},{"PluginID":66,"IsActive":False,"IsLocked":True},{"PluginID":67,"IsActive":False,"IsLocked":True},{"PluginID":68,"IsActive":False,"IsLocked":True},{"PluginID":69,"IsActive":False,"IsLocked":True},{"PluginID":70,"IsActive":False,"IsLocked":True},{"PluginID":73,"IsActive":False,"IsLocked":True},{"PluginID":74,"IsActive":False,"IsLocked":True},{"PluginID":75,"IsActive":False,"IsLocked":True},{"PluginID":76,"IsActive":False,"IsLocked":True},{"PluginID":77,"IsActive":False,"IsLocked":True},{"PluginID":79,"IsActive":False,"IsLocked":True},{"PluginID":80,"IsActive":False,"IsLocked":True},{"PluginID":81,"IsActive":False,"IsLocked":True},{"PluginID":82,"IsActive":False,"IsLocked":True},{"PluginID":83,"IsActive":False,"IsLocked":True},{"PluginID":84,"IsActive":False,"IsLocked":True},{"PluginID":85,"IsActive":False,"IsLocked":True},{"PluginID":86,"IsActive":False,"IsLocked":True},{"PluginID":87,"IsActive":False,"IsLocked":True},{"PluginID":93,"IsActive":False,"IsLocked":True},{"PluginID":94,"IsActive":False,"IsLocked":True},{"PluginID":103,"IsActive":False,"IsLocked":True},{"PluginID":106,"IsActive":False,"IsLocked":True},{"PluginID":107,"IsActive":False,"IsLocked":True},{"PluginID":110,"IsActive":False,"IsLocked":True},{"PluginID":112,"IsActive":False,"IsLocked":True},{"PluginID":113,"IsActive":False,"IsLocked":True},{"PluginID":126,"IsActive":False,"IsLocked":True},{"PluginID":130,"IsActive":False,"IsLocked":True},{"PluginID":135,"IsActive":False,"IsLocked":True},{"PluginID":137,"IsActive":False,"IsLocked":True},{"PluginID":140,"IsActive":False,"IsLocked":True},{"PluginID":141,"IsActive":False,"IsLocked":True},{"PluginID":142,"IsActive":False,"IsLocked":True},{"PluginID":143,"IsActive":False,"IsLocked":True},{"PluginID":144,"IsActive":False,"IsLocked":True},{"PluginID":145,"IsActive":False,"IsLocked":True},{"PluginID":146,"IsActive":False,"IsLocked":True},{"PluginID":148,"IsActive":False,"IsLocked":True},{"PluginID":149,"IsActive":False,"IsLocked":True},{"PluginID":150,"IsActive":False,"IsLocked":True},{"PluginID":151,"IsActive":False,"IsLocked":True},{"PluginID":152,"IsActive":False,"IsLocked":True},{"PluginID":153,"IsActive":False,"IsLocked":True},{"PluginID":154,"IsActive":False,"IsLocked":True},{"PluginID":155,"IsActive":False,"IsLocked":True},{"PluginID":156,"IsActive":False,"IsLocked":True},{"PluginID":157,"IsActive":False,"IsLocked":True},{"PluginID":158,"IsActive":False,"IsLocked":True},{"PluginID":159,"IsActive":False,"IsLocked":True},{"PluginID":160,"IsActive":False,"IsLocked":True},{"PluginID":161,"IsActive":False,"IsLocked":True},{"PluginID":162,"IsActive":False,"IsLocked":True},{"PluginID":163,"IsActive":False,"IsLocked":True}],"RCONPassword":"12M3BS","VotingSecret":None,"VotingIdentity":None,"GameID":0}

	dataold = {"rconpassword": "apassword",
	        "ID": "test",
	        "Credits": 9999999999,
	        "PriceDaily": 10,
	        "PriceMultiplier": 1.0,
	        "DockerName": "leet.cc/leetv2-7",
	        "Status": False,
	        "Domains": [
		        "BB43661.pocket.pe"
	        ],
	        "Port": 19132,
	        "UserRegistered": False,
	        "MapID": 1,
	        "Settings": {"Name": "a leet server",
	                     "OPs": [],
	                     "Gamemode": "survival",
	                     "MaxOnline": 5,
	                     "ServerVersion": 30,
	                     "PVP": True,
	                     "AlwaysDay": False,
	                     "AlwaysSpawn": False,
	                     "Ranks": False,
	                     "Monsters": True,
	                     "Animals": True,
	                     "Login": False,
	                     "Whitelist": False,
	                     "WhitelistPlayers": [],
	                     "SpawnProtection": 0,
	                     "Weather": False},
	        "Statistics": {"PlayersOnline": 0,
	                       "Players": [],
	                       "LastOnlineTime": 0,
	                       "TimeCreated": "15563424",
	                       },
	        "Plugins": [{"PluginID": 8,
	                     "IsActive": False,
	                     "IsLocked": True
	                     },
	                    {"PluginID": 9,
	                     "IsActive": False,
	                     "IsLocked": True}],
	        "RCONPassword": "12M3BS",
	        "GameID": 0}

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/setting/serverversion/get/<string:server_id>/<string:token>', methods=['GET'])
def get_versions(server_id, token):

	data = [{
		"ID": 6,
		"Name": "PocketMine 1.0.5",
		"DockerName": "leetcc/leetv2-pmmp-1.0.5",
		"GameID": 0
	}]

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/system/startup/get/<string:server_id>', methods=['GET'])
def get_rating(server_id):

	data = {
		"AskForRating": False
	}

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/system/broadcast/token/register/<string:platform>/<string:token_device>/<string:server_id>/<string:token>', methods=['GET'])
def get_brodacast(server_id, token_device, token, platform):

	print(server_id + ' ' + token_device + ' ' + token + ' ' + platform)

	data = {
		"Status": 0
	}

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/system/plugins/categories/get/<string:server_id>/<string:token>', methods=['GET'])
def get_plugins(server_id, token):

	data = [{"ID":1000,
	         "Name":"All Plugins",
	         "Description":"",
	         "PluginCount":104,
	         "PluginUnlockedCount":0},
	        {"ID":4,
	         "Name":"Admin",
	         "Description":"Plugins that help you administrate your server.",
	         "PluginCount":14,
	         "PluginUnlockedCount":0},
	        {"ID":10,"Name":"Communication",
	         "Description":"Plugins that affect the communication on your server.",
	         "PluginCount":2,
	         "PluginUnlockedCount":0},
	        {"ID":5,
	         "Name":"Cosmetic",
	         "Description":"Plugins that redesign the style of your server.",
	         "PluginCount":18,
	         "PluginUnlockedCount":0},
	        {"ID":8,
	         "Name":"Fun",
	         "Description":"Plugins that add a fun element to your server.",
	         "PluginCount":16,
	         "PluginUnlockedCount":0},
	        {"ID":6,"Name":"Gameplay",
	         "Description":"Plugins that change the gameplay mechanics of your server.",
	         "PluginCount":24,
	         "PluginUnlockedCount":0},
	        {"ID":12,"Name":"Informative",
	         "Description":"Plugins that help you inform players on your server.",
	         "PluginCount":7,
	         "PluginUnlockedCount":0},
	        {"ID":14,
	         "Name":"Misc.",
	         "Description":"Plugins that don't fit into any other category. :(",
	         "PluginCount":9,
	         "PluginUnlockedCount":0},
	        {"ID":16,
	         "Name":"New Plugins",
	         "Description":"Plugins that were recently added",
	         "PluginCount":3,
	         "PluginUnlockedCount":0},
	        {"ID":13,
	         "Name":"Role Play",
	         "Description":"Plugins that help your players role play on you server.",
	         "PluginCount":12,
	         "PluginUnlockedCount":0},
	        {"ID":11,
	         "Name":"Security",
	         "Description":"Plugins that help improve the security of your server.",
	         "PluginCount":9,
	         "PluginUnlockedCount":0},
	        {"ID":15,
	         "Name":"Utilities",
	         "Description":"Plugins that help keep the server running.",
	         "PluginCount":24,
	         "PluginUnlockedCount":0},
	        {"ID":7,
	         "Name":"World Management",
	         "Description":"Plugins that help you manage the worlds/maps of your server.",
	         "PluginCount":12,
	         "PluginUnlockedCount":0}]

	print(json.dumps(data))
	return json .dumps(data)


@app.route('/api/system/purchase/get/<string:server_id>/<string:token>', methods=['GET'])
def get_purchases(server_id, token):

	data = []

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/setting/maxOnline/get/<string:server_id>/<string:token>', methods=['GET'])
def get_credits(server_id, token):

	data = [{
		"MaxOnline": 2,
		"PriceDaily": 5
	}, {
		"MaxOnline": 5,
		"PriceDaily": 10
	}, {
		"MaxOnline": 10,
		"PriceDaily": 29
	}, {
		"MaxOnline": 15,
		"PriceDaily": 49
	}, {
		"MaxOnline": 20,
		"PriceDaily": 79
	}, {
		"MaxOnline": 25,
		"PriceDaily": 229
	}, {
		"MaxOnline": 30,
		"PriceDaily": 159
	}, {
		"MaxOnline": 35,
		"PriceDaily": 229
	}]

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/authorization/exists/<string:key>', methods=['GET'])
def get_auth(key):
	print('GOT KEY ON AUTH: ' + key)

	data = {
		"Status": 0,
		"Token": "RG3DG400GA9G",
		"ServerId": 1770637,
		"ServerID": 1770637
	}

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/system/domain/get/<string:server_id>/<string:token>', methods=['GET'])
def get_domain(server_id, token):

	print('GOT SERVER ID ON DOMAIN: ' + server_id + " TOKEN: " + token)

	data = [{
		"Domain": "honza.pe",
		"PriceUnlock": 499
	}, {
		"Domain": "herry.pe",
		"PriceUnlock": 499
	}]

	print(json.dumps(data))
	return json.dumps(data)


@app.route('/api/system/maps/get/<string:server_id>/<string:token>', methods=['GET'])
def get_maps(server_id, token):

	print('GOT SERVER ID ON MAPS: ' + server_id + " TOKEN: " + token)

	data = [{
		"ID": 1,
		"SysName": "standard",
		"Name": "Standard",
		"Description": "Just a plain old regular map like in single player!",
		"NumImages": 3,
		"ImagesMaxAge": 39038979,
		"UnlockPrice": 0,
		"AverageRating": 4.5,
		"Locked": True
	}, {
		"ID": 2,
		"SysName": "cave",
		"Name": "Big natural cave",
		"Description": "Its underground, and its really big. Maybe even a bit scary...?",
		"NumImages": 2,
		"ImagesMaxAge": 39038975,
		"UnlockPrice": 0,
		"AverageRating": 3.5,
		"Locked": True
	}]

	print(json.dumps(data))
	return json.dumps(data)


if __name__ == '__main__':
	app.run(port=80, host='0.0.0.0', debug=False)
