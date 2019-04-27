import requests
url = 'http://134.209.95.120:1819'
headers = {'user-agent': 'martin-1981clark'}
r = requests.get(url, headers=headers)
f = open('index.html', 'w+')
f.write(r.text)
f.close()
