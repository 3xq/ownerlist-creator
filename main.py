import requests, threading

Owners   =  []
Friends  =  []
Threads  =  []

Asset = 134683641

def To_UserID(Username):
	return requests.get(f'https://api.roblox.com/users/get-by-username?username={Username}').json()['Id']

def Check_Ownership(Username):
	try:
		Request = requests.get('http://api.roblox.com/Ownership/HasAsset?userId='+str(To_UserID(Username))+'&assetId='+str(Asset)).text
		print(f'| CHECKING | '+Username+str(' '*int(27-len(Username)))+' |')
		if Request == 'true':
			Owners.append(Username)
	except:
		eval('0')

def Ownerlist(Owners_Table):
	for Owner in list(set(Owners_Table)):
		CurrentFriends = requests.get(f'https://friends.roblox.com/v1/users/{To_UserID(str(Owner))}/friends').json()
		print(f'| FRIENDS  | '+Owner+str(' '*int(27-len(Owner)))+' |')
		if 'data' in CurrentFriends:
			for UserData in CurrentFriends['data']:
				Friends.append(UserData['name'])

	try:
		Threads.clear()
	except:
		Threads = []

	for Username in Friends:
		Thread = threading.Thread(target=Check_Ownership, args=(Username,))
		Threads.append(Thread)

	for Thread in Threads:
		Thread.start()

	for Thread in Threads:
		Thread.join()

	BoolInput = input('\nFinished! C/V: ')

	if BoolInput.lower() == 'c':
		Ownerlist(list(set(Owners)))
	elif BoolInput.lower() == 'v':
		print()
		print(list(set(Owners)))
		print(len(list(set(Owners))))

Ownerlist(['table','of','people'])
