# Discord_Bot

[Where to create a Discord bot](https://discord.com/developers/applications)

1. Go to the link above to create a bot, copy the TOKEN and paste it into config.py.
- [MESSAGE CONTENT INTENT] 체크 필수! [참고](https://github.com/star14ms/Discord_Bot#privileged-gateway-intents)

2. Copy the bot's CLIENT ID and insert it in place of CLIENT_ID in the link below to connect.

https://discord.com/oauth2/authorize?permissions=8&scope=bot&client_id=CLIENT_ID

3. Invite your bot to your desired server

4. Run main.py

---

## File Description

`main.py` - Bot starts when run (bot TOKEN required)

`bot_base/command.py` - Where to set bot commands

`bot_base/event.py` - Where to set up bot events

`persona/__init__.py` - Where to apply the bot’s persona

`persona/*.py` - Bot personas

`utils.py` - Functions to use when needed

---

## Location of important information on bot creation page

### TOKEN
![](bot_base/img/token.png)

### CLIENT_ID
![](bot_base/img/client_id.png)

### Privileged Gateway Intents
- MESSAGE CONTENT INTENT check required to read chat

![](bot_base/img/privileged_gateway_intents.png)

---

## Reading Materials

### discord.py

[Home Page]()

[Quick Start](https://discordpy.readthedocs.io/en/stable/quickstart.html)

[discord.ext.commands.Bot](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#bots)


### Apply commands and general message processing simultaneously
[is-it-possible-to-use-on-message-and-client-command-in-the-same-code](https://stackoverflow.com/questions/62150817/is-it-possible-to-use-on-message-and-client-command-in-the-same-code)
