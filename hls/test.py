import requests
url = 'https://papi.barryblueice.top/hls_count.php'
resp = requests.get(url = url)
html = resp.text
print(html)
