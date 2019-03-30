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


@app.route('/api/server/get/-1/', methods=['GET'])
def some_unknown_data():

	data = {"rconpassword": "apassword",
	        "ID": "test",
	        "Credits": 100,
	        "PriceDaily": 10,
	        "PriceMultiplier": 1.0,
	        "DockerName": "leet.cc/leetv2-7",
	        "Status": False,
	        "Domains": ["BB43661.pocket.pe"],
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
	                    {"PluginID": 8,
	                     "IsActive": False,
	                     "IsLocked": True}]}
	print(json.dumps(data))
	return json.dumps(data)


if __name__ == '__main__':
	app.run(port=80, host='0.0.0.0', debug=False)
