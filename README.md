# Minecraft-ft.-discord-bot-
This Discord bot is used to allow any privilaged person to manage your private Minecraft server.
This project is very specific and I could imagine no one ever uses it but.
For more infos on Discord bots see here:(https://discordpy.readthedocs.io/en/stable/) or here (https://pypi.org/project/discord.py/)
# How to use
1. Create a Bot accout in Discord. In order for you to  do that go to the developer portal (https://discord.com/developers/applications).
2. Follow some steps to setup yourbot with the right privilages. I used this video https://www.youtube.com/watch?v=SPTfmiYiuok&pp=ygUSY3JlYXRlIGRpc2NvcmQgYm90
3. with ethtools on your server type: sudo ethtool -s >INTERFACE< wol g
4. Change the variables in .env to match your server and other device.
5. Change line 27 and 28 in Bot.py to point to your Minecraft Server
6. Try running Bot.py
# What to install
You'll need: 
1. discord.py -->   pip install -U discord.py
2. paramiko -->     pip install -U paramiko
3. wakeonlan on your device --> sudo apt install wakeonlan
4. ehtool on your server --> sudo apt install ethtool
and that should be it.
