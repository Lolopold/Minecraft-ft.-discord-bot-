import os
import discord
import paramiko
import subprocess
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv
from paramiko import SSHClient

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def startup():
	sshclient = SSHClient()
	sshclient.load_system_host_keys()
	sshclient.connect(os.getenv("ssh_host"), username=os.getenv("ssh_user"), password=os.getenv("ssh_password"))
	
	stdin, stdout, stderr = sshclient.exec_command('php')
	print(type(stdin))  
	print(type(stdout))  
	print(type(stderr))  

	command = 'java -Xmx4096M -Xms4096M -jar minecraft_server.1.**.jar nogui'
	stdin.write('<?php chdir("/to/your/minecraft/server"); ?>')
	stdin.write('<?php exec("' + command + '"); ?>')
	stdin.channel.shutdown_write()
	
	print(f'STDOUT: {stdout.read().decode("utf8")}')
	print(f'STDERR: {stderr.read().decode("utf8")}')
	
	print(f'Return code: {stdout.channel.recv_exit_status()}')
	
	stdin.close()
	stdout.close()
	stderr.close()
	
	sshclient.close()
	
()

def sleep():
	sshclient = SSHClient()
	sshclient.load_system_host_keys()
	sshclient.connect(os.getenv("ssh_host"), username=os.getenv("ssh_user"), password=os.getenv("ssh_password"))
	
	stdin, stdout, stderr = sshclient.exec_command('php')
	print(type(stdin))  
	print(type(stdout))  
	print(type(stderr))  

	command = 'sudo systemctl suspend'
	password = os.getenv("sudo")
	stdin.write('<?php $command = "' + command + '"; $password = "' + password + '"; exec("echo $password | sudo -S $command"); ?>')
	stdin.channel.shutdown_write()
	
	print(f'STDOUT: {stdout.read().decode("utf8")}')
	print(f'STDERR: {stderr.read().decode("utf8")}')
	
	print(f'Return code: {stdout.channel.recv_exit_status()}')
	
	stdin.close()
	stdout.close()
	stderr.close()
	
	sshclient.close()
	
()
def wakeup():
	wol_host=os.getenv("wol_host")
	wol_mac=os.getenv("wol_mac")
	wol=["wakeonlan", "-n", wol_host, wol_mac]
	subprocess.run(wol)

()	
@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):

	if message.content.startswith("//up"):
		await message.channel.send("Yes! I'm up")
	if message.content.startswith("//start"):
		await message.channel.send("Minecraft server should be up any moment now.")
		startup()
		await message.channel.send("Minecraft server is now down.")
	if message.content.startswith("//sleep"):
		await message.channel.send(":yawning_face:")
		await message.channel.send("Okay. I'm gonna go to bed.")
		sleep()
		await message.channel.send(":zzz:")
	if message.content.startswith("//wake"):
		wakeup()
		await message.channel.send(":weary:")
		await message.channel.send("Good morning!")
client.run(os.getenv("TOKEN"))

