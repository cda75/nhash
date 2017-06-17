import requests

url = 'https://api.nicehash.com/api'
method = 'stats.provider.workers'
btcAddr = '1LoLs9AQvYzccVbvifj5pCXhfcJZx8tXWB'
algos = {'Scrypt' : 0,
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

payload = {'method':method, 'addr':btcAddr, 'algo':algos['CryptoNight']}
req = requests.get(url, params=payload)
rez = req.json()['result']
workers = rez['workers']
total = 0.0
for w in workers:
    if w[1]:
        total = total + float(w[1]['a'])
        print w[0],'\t\t',w[1]['a']

print '\nTotal:\t\t', total



