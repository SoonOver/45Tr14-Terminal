import urllib.request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://safebooru.org/index.php?page=dapi&s=post&q=index&tags=yae_miko+%28genshin_impact%29+1girl+solo+rating:safe&json=1&limit=1"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode('utf-8'))
    if len(data) > 0:
        img_url = "https://safebooru.org/images/" + data[0]['directory'] + "/" + data[0]['image']
        urllib.request.urlretrieve(img_url, "app/src/main/res/drawable/bg_anime.jpg")
        print("Downloaded:", img_url)
    else:
        print("No image found for Yae Miko")
except Exception as e:
    print("Error:", e)
