
import json
import requests


print("Welcome User!")
print("The program retrieve any unsspent outouts on Blockchain.info API for a bitcoin address")

#bitcoin address
btc_address = input("Please enter the BTC addres you want to verify: ")

#call  blockchain.info APIs , will return a JSON document with all the transactions
resp = requests.get('https://blockchain.info/unspent?active=%s' % btc_address)


#load the list into utxo_list
try:
	utxo_list = json.loads(resp.text)["unspent_outputs"]


	print(" ")
	print("FORMAT:") , ("  [ Transaction ID : Index Number - Balance available to spend (in BTC)  ]")
	print(" ")

	total = 0
	total = int(total)
	#for each json object in the list of json objects
	for utxo in utxo_list:
		#print transactions ID : index number - balance available to spend
		print("%s:%d - %f BTC" % (utxo['tx_hash'], utxo['tx_output_n'], float(utxo['value']) / 100000000))
		print(" ")
		total = total + utxo['value'] + 0

	print("BTC available top1nd"
          " spend: %f" % (float(total) / 100000000) )
	print("------")


except:
	print ("No free outputs to spend")


print("Finish")