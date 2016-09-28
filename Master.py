ver = (5.2)
global debug
debug = False
import discord
import asyncio
import random
import logging
import sys
import ctypes
import os
import pymysql.cursors
import urllib
from mal import findString
import threading
import urllib.request
from threading import Timer

from imgurpython import ImgurClient
imgur = ImgurClient(client_id, client_secret)
import feedparser
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import aiohttp
import regex
from array import array
re = regex
from google import search
from cleverbot import Cleverbot
import PIL
from PIL import Image
from time import gmtime, strftime
client = discord.Client()
import os.path
cb = Cleverbot()
counter = (0)
from io import BytesIO
client = discord.Client()
connection = pymysql.connect()
############################SYSTEM FUNCTIONS############################
async def say(dest,input,message):
    if dest == ('pm'):
        dest = message.author
    elif dest == ('ch'):
        dest = message.channel
    elif dest == ('log'):
        dest = cLog
    try:
        await client.send_message(dest,input)
    except discord.Forbidden:
        x = "I cannot talk in channel: "+message.channel.name+" In server: "+message.server.name
        await client.send_message(message.author,x)
async def role_modrole(message):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `admin_role` FROM `Servers` WHERE id=%s"
            cursor.execute(sql, (message.server.id))
            check = cursor.fetchone()['admin_role']
    except TypeError:
        bC = discord.utils.get(message.author.roles, name='Bot Commander')
        print('Falling back to failsafe role.')
        if bC != None:
            return False
        else: 
            return True
    else:
        bC = discord.utils.get(message.author.roles, id=check)
        if bC != None:
            return False
        else: 
            return True
#func to allow me to delete messages safe without having to deal with errors
async def delete_message(message):
    try:
	    return await client.delete_message(message)
    except discord.Forbidden:
        x = "I cannot delete message in channel: "+message.channel.name+" In server: "+message.server.name+" The message: \n"+message.clean_content
        await client.send_message(cLog,x)
def get_owner():
    for server in client.servers:
        for channel in server.channels:
            for m in channel.voice_members:
                if m.id == '190092287722651648':
                    return m
    else:
        return discord.utils.find(lambda m: m.id == '190092287722651648', client.get_all_members())
############################COMMANDS############################
helpmessage = '```fix\n'
helpmessage += '\nMH: for a chat bot that will respond with the flair: GH.'
helpmessage += '\n[>8ball] for 8 ball predictions'
helpmessage += '\n[>g] for a google search, any length works'
helpmessage += '\n[>y] for youtube search, now returns faster than 42'
helpmessage += '\n[>tc] allows you to create a tag'
helpmessage += '\n[>tt] allows you to call a tag, remember its case sensitive!'
helpmessage += '\n[>r34] searches for rule34 images PM cerulean for PM porn access'
helpmessage += '\n[>fp] searches the imgur front page. add a number after >fp for an image number'
helpmessage += '\n[>news [any number]] Searches the bbc for news. Do >news 0 for the latest'
helpmessage += '\n[>pet-c [Name] creates a pet cat for you to look after'
helpmessage += '\n[>pet-s] returns your pets details'
helpmessage += "\n For more information: PM @Cerulean#7014```"
helpmessage += "\nAdd this bot to your server! https://discordapp.com/oauth2/authorize?client_id=211994441106325504&scope=bot&permissions=0"
############################TAGGING SYSTEM############################

############################INTERNET BASED FUNCTIONS##########################

############################USER BASED COMMANDS##########################
async def user_info(message):
    input = message.content.split(None,1)
    print(input)
    try:
        user = discord.utils.get(message.server.members, id=input[1])
    except IndexError:
        user = message.author
    roles = []
    for role in user.roles:
        roles.append(role.name)
    del roles[0]
    roles = ", ".join(roles)
    join_date = user.joined_at
    made_at = user.created_at
    status = user.status
    if status.online:
        status = 'Online'
    elif status.offline:
        status = 'Offline'
    elif status.idle:
        status = "Idle"
    user_list = "**User information:**\n➠User name: "+user.display_name+" #"+user.discriminator
    sec_line = "\n➠ID: "+user.id+"\n➠Roles: "+roles+"\n➠Status: "+str(user.status)
    try:
        thir_line = "\n➠Now playing: "+user.game.name
    except AttributeError:
        thir_line = "\n➠Now playing: "+"No game."
    for_line = "\n➠Avatar: "+user.avatar_url
    dates = "\n➠Created at: "+user.created_at.strftime("%d-%m-%Y %H:%M:%S")+"\n➠Joined at: "+user.joined_at.strftime("%d-%m-%Y %H:%M:%S")
    lines = user_list + sec_line + thir_line +dates+ for_line
    await say("ch",lines,message)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.user.created_at)
    print('Version: V', ver, ' OPlIOS')
    print('-----Justice Rains From Above----')
    global globalLog
    globalLog = discord.utils.get(client.get_all_channels(), id='219209469714890754')
    global spoopyChannel
    spoopyChannel = discord.utils.get(client.get_all_channels(), id='193720384409960448')
    global log_check
    log_check = False
    global log_chan
    log_chan = {}
    global mod_roles
    mod_roles = {'213048814632828928':'bot-commander'}
@client.event
async def on_message(message):
    input = message.content.split(None,1)
    if message.author != client.user:
        return
    if input[0] == ('>purge') and message.author.id in ['190092287722651648','165568912564420608']:
        limit1 = message.content.split(None, 1)
        async for message in client.logs_from(message.channel, limit=1000):
            if message.author == client.user:
                await client.delete_message(message)
    ###TAGS###
    if input[0] == ('>tt'):
        await tag_tag(message)
    if input[0] == ('>tc'):
        await tag_create(message)
    if input[0] == ('>te'):
        await tag_edit(message)
    if input[0] == ('>td'):
        if await role_modrole(message):
            await tag_del_mod(message)
        else:
            await tag_del(message)
    ###INTERNET BASED FUNCTIONS###
    if input[0] == ('>g'):
        await google(message)
    if input[0] == ('>news'):
        await news(message)
    if input[0] == ('>r34'):
        await rule34_search(message)
    if input[0] == ('>y'):
        await youtube_search(message)
    ###USER BASED COMMANDS###
    if input[0] == ('>info'):
        await user_info(message)
    ###MISC##
    if input[0] == ('>eval') and message.author.id == "190092287722651648":
        await eval_async(message)
    if input[0] == ('>dice'):
        input1 = message.content.strip('>dice')
        dice = re.compile("\d+?(?:\+\-\d*)?")
        dice = re.search(dice,input1)
        print(dice)
        final = str(dick) + "d"+str(dicks[1])+str(addons)
        print(final)
        dice1 = dice.roll(final)
        await client.send_message(message.channel,dice1)
client.run("Token")
