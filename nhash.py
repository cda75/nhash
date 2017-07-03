import requests
import csv
from datetime import datetime
import os
from statsd import StatsClient

API_URL = 'https://api.nicehash.com/api'
method = 'stats.provider.workers'
BTC = '1LoLs9AQvYzccVbvifj5pCXhfcJZx8tXWB'
APP_DIR = '/usr/local/nhash'
DATA_DIR = '/usr/local/nhash/data'
ALGOS = {'Scrypt' : 0,
        'SHA256' : 1,
        'ScryptNf' : 2,
        'X11' : 3,
        'X13' : 4,
        'Keccak' : 5,
        'X15' : 6,
        'Nist5' : 7,
        'NeoScrypt' : 8,
        'Lyra2RE' : 9,
        'WhirlpoolX' : 10,
        'Qubit' : 11, 
        'Quark' : 12,
        'Axiom' : 13,
        'Lyra2REv2' : 14,
        'ScryptJaneNf16' : 15,
        'Blake256r8' : 16,
        'Blake256r14' : 17, 
        'Blake256r8vnl' : 18,
        'Hodl' : 19,
        'DaggerHashimoto' : 20,
        'Decred' : 21,
        'CryptoNight' : 22,
        'Lbry' : 23,
        'Equihash' : 24,
        'Pascal' : 25,
        'X11Gost' : 26,
        'Sia' : 27 }


def collect_data(btcAddr):
    payload = {'method':method, 'addr':btcAddr, 'algo':ALGOS['CryptoNight']}
    req = requests.get(API_URL, params=payload)
    reqResult = req.json()['result']
    workers = reqResult['workers']
    totalHash = 0.0
    checkDate = datetime.now().strftime('%d.%m %H:%M')
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    for w in workers:
        if w[1]:
    	    workerName = w[0]
    	    workerHash = float(w[1]['a'])
            stats = StatsClient(prefix='nhash', port=8125)
            stats.gauge(workerName, workerHash)
            totalHash += workerHash
            workerFile = workerName + '.csv'
            with open(os.path.join(DATA_DIR, workerFile), 'a') as f:
        	writer = csv.writer(f)
        	writer.writerow((workerHash, checkDate))
            print workerName,'\t', workerHash
    print '\nTotal: %s H/s' %totalHash
    stats.gauge('Total', totalHash)
    with open(os.path.join(DATA_DIR, 'total.csv'), 'a') as f:
       writer = csv.writer(f)
       writer.writerow((totalHash, checkDate))


if __name__ == '__main__':
    collect_data(BTC)

