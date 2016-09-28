ver = (2.1)
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
#IMGUR CLIENT ID:
#da792af99ce069d
#IMGUR SECRET ID:
#caf7821a4bf2f41f14cd3d397f4cdf0fa429a9fa
#-----
#Dont forget list:
#Talons b day 31st aug. Make song!
#
#
#
#
from threading import Timer

from imgurpython import ImgurClient
client_id = 'da792af99ce069d'
client_secret = 'caf7821a4bf2f41f14cd3d397f4cdf0fa429a9fa'
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
import validators
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
#import images2gif
#Artemis "Cerulean" DeLaney
from midiutil.MidiFile3 import MIDIFile
Online = ('1')
helpmessage = '```fix\n'
helpmessage += '\nMH: for a chat bot that will respond with the flair: GH.'
helpmessage += '\n[>8ball] for 8 ball predictions'
helpmessage += '\n[>g] for a google search, any length works'
helpmessage += '\n[>y] for youtube search, now returns faster than 42'
helpmessage += '\n[>d] for definitions of a word[REMOVED IN NEXT UPDATE]'
helpmessage += '\n[>tc] allows you to create a tag'
helpmessage += '\n[>tt] allows you to call a tag, remember its case sensitive!'
helpmessage += '\n[>r34] searches for rule34 images PM cerulean for PM porn access'
helpmessage += '\n[>fp] searches the imgur front page. add a number after >fp for an image number'
helpmessage += '\n[>news [any number]] Searches the bbc for news. Do >news 0 for the latest'
helpmessage += '\n[>pet-c [Name] creates a pet cat for you to look after'
helpmessage += '\n[>pet-s] returns your pets details'
helpmessage += "\n For more information: PM @Cerulean#7014```"
helpmessage += "\nAdd this bot to your server! https://discordapp.com/oauth2/authorize?client_id=211994441106325504&scope=bot&permissions=0"
EIGHT_BALL_OPTIONS = ["It is certain", "It is decidedly so", "Without a doubt",
                      "Yes definitely", "You may rely on it", "As I see it yes",
                      "Most likely", "Outlook good", "Yes",
                      "Signs point to yes", "Reply hazy try again",
                      "Ask again later", "Better not tell you now",
                      "Cannot predict now", "Concentrate and ask again",
                      "Don't count on it", "My reply is no",
                      "My sources say no", "Eh~",
                      "Very doubtful"]
global connection

global b_a
global b_b
global b_bs
global gChannels
async def bot(input):
    return
async def fuck(message):
    fuck = message.content.split(None,1)
    filename = fuck[1]
    f = open(filename, 'rb')
    await client.edit_profile(avatar=f.read())
async def add_admin(message):
    query = message.content.split(None, 1)
    with connection.cursor() as cursor:
    # Create a new record
        sql = "INSERT INTO `BotMods` (`ID`) VALUES (%s)"
        cursor.execute(sql, (query[1]))
    connection.commit()
async def banned_word(message):
    Str = message.content.split(None, 1)
    splitMod = ';'
    Str2 = Str[1] + splitMod
    with open("Banned Words.txt", "a") as myfile:
        myfile.write(Str2)
    print ("Added Blocked Word: ", Str[1])


#TO BE REMOVED
async def update_lists(message):
    print ("UPDATING LIST'S")
    with open('Banned Words.txt') as banned_words:
        b_b = banned_words.read().split(';')
        print ('Blocked Words: ', b_b)
    with open('Admins.txt') as b_admin:
        b_a = b_admin.read().split(';')
        print ('Admins: ', b_a)
    with open('Blacklist.txt') as b_bs:
        b_bs = b_bs.read().split(';')
        print ('Blacklisted Channels: ', b_bs)

async def reset():
    asyncio.sleep(1)
    client.close()
    os.system('Start.bat 1')
    asyncio.sleep(2)
    sys.exit(0)
#####################################################################################################################################################
async def pet_create(message):
    declass = message.content.split(None, 1)
    declass = declass[1].replace("''","")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `owner` FROM `Pets` WHERE `owner`=%s"
            cursor.execute(sql, (message.author.id))
            check = cursor.fetchone()['owner']
    except TypeError:
        cat = random.randint(100,300)
        kitten = 'https://placekitten.com/200/' + str(cat)
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `Pets` (`Owner`, `Name`,`Hunger`,`Happy`,`illness`,`img`,`lvl`) VALUES (%s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(sql, (message.author.id, declass, 100,100,'None',kitten,0))
        connection.commit()
        ext = 'Congrats you now have a pet called: ' + declass + '\nThe image for your pet is:\n' + kitten
        await client.send_message(message.channel, ext)
        return
    else:
        await client.send_message(message.channel, 'Sorry, you already have a pet.')
async def pet_re(message):
    input = message.content.split(None,1)
    with connection.cursor() as cursor:
        # Read a single record
            sql = 'UPDATE `Pets` SET name=%s WHERE owner=%s'
            cursor.execute(sql, (input[1],message.author.id))
    await client.send_message(message.channel,"Updating info...")
    connection.commit()
    x = "Changed name too: "+input[1]
async def pet_img(message):
    input = message.content.split(None,1)
    with connection.cursor() as cursor:
        # Read a single record
            sql = 'UPDATE `Pets` SET img=%s WHERE owner=%s'
            cursor.execute(sql, (input[1],message.author.id))
    await client.send_message(message.channel,"Updating info...")
    connection.commit()
    x = "Changed name too: "+input[1]
async def pet_img(message):
    input = message.content.split(None,1)
    with connection.cursor() as cursor:
        # Read a single record
            sql = 'UPDATE `Pets` SET img=%s WHERE owner=%s'
            cursor.execute(sql, (input[1],message.author.id))
    await client.send_message(message.channel,"Updating info...")
    connection.commit()
    x = "Changed name too: "+input[1]
async def pet_stat(message):
    try:
        with connection.cursor() as cursor:
                # Read a single record
                    sql = "SELECT `name` FROM `Pets` WHERE `owner`=%s"
                    cursor.execute(sql, (message.author.id))
                    result = cursor.fetchone()['name']
                    sql = "SELECT `hunger` FROM `Pets` WHERE `owner`=%s"
                    cursor.execute(sql, (message.author.id))
                    Hunger = cursor.fetchone()['hunger']
                    sql = "SELECT `happy` FROM `Pets` WHERE `owner`=%s"
                    cursor.execute(sql, (message.author.id))
                    Happy = cursor.fetchone()['happy']
                    sql = "SELECT `img` FROM `Pets` WHERE `owner`=%s"
                    cursor.execute(sql, (message.author.id))
                    img = cursor.fetchone()['img']
                    stats = 'Your pet details are:\n```fix\n' + 'Name: [' + result + ']\n' + 'Hunger levels: [' + str(Hunger) + ']\n' + 'Happiness: [' + str(Happy) + ']\n' + '```\n' + str(img)
                    await client.send_message(message.channel, stats)
    except TypeError:
        await client.send_message(message.channel,"You dont have a pet. get one by doing >pet-c with their name")
async def pet_cuddle(message):
    declass = message.content.split(None,1)
    try:
        await client.send_message(message.channel,"**CUDDLES!!**")
        with connection.cursor() as cursor:
            sql = "SELECT `happy` FROM `Pets` WHERE `owner`=%s"
            cursor.execute(sql, (message.author.id))
            happy = cursor.fetchone()['happy']
            if happy >= 100:
                await client.send_message(message.channel,"***Too much happiness***")
                return
            else:
                tot_hap = happy + 10
                sql = "UPDATE `Pets` SET happy =%s WHERE owner=%s"
                cursor.execute(sql, (tot_hap,message.author.id))
                await client.send_message(message.channel,"+10 Happiness\n+10 Coins")
        with connection.cursor() as cursor:
            sql = "SELECT `cuddle` FROM `Pets` WHERE `owner`=%s"
            cursor.execute(sql, (message.author.id))
            cuddle = cursor.fetchone()['cuddle']
            tot_cud = cuddle + 1
            sql = "UPDATE `Pets` SET cuddle =%s WHERE owner=%s"
            cursor.execute(sql, (tot_cud,message.author.id))
        connection.commit()
    except TypeError:
        await client.send_message(message.channel,"You dont have a pet. get one by doing >pet-c with their name")
async def pet_feed(message):
    try:
            await client.send_message(message.channel,"Feeding time!")
            with connection.cursor() as cursor:
                sql = "SELECT `hunger` FROM `Pets` WHERE `owner`=%s"
                cursor.execute(sql, (message.author.id))
                happy = cursor.fetchone()['hunger']
                if happy >= 100:
                    await client.send_message(message.channel,"*Too much food! you wont be charged*")
                else:
                    tot_food = happy + 3
                    sql = "UPDATE `Pets` SET hunger =%s WHERE owner=%s"
                    cursor.execute(sql, (tot_food,message.author.id))
                    await client.send_message(message.channel,"*You got +5 food!*")
            connection.commit()
    except TypeError:
        await client.send_message(message.channel,"You dont have a pet. get one by doing >pet-c with their name")
async def bank_check(message):
    declass = message.content.split(None,1)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `money` FROM `bankOfCerulean` WHERE `userId`=%s"
            cursor.execute(sql, (message.author.id))
            happy = cursor.fetchone()['money']
        await client.send_message(message.channel,happy)
    except TypeError:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `bankOfCerulean` (`userId`,`userName`,`money`,`extra`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (message.author.id, message.author.name,1000,'None'))
        await client.send_message(message.channel,"You didnt have an account with me. so i made you one! Have a free '1000' coins ^w^")
    connection.commit()
async def pet_minus_hung(message):
    with connection.cursor() as cursor:
        sql = "SELECT `hunger` FROM `Pets`"
        cursor.execute(sql)
        row = [item['hunger'] for item in cursor.fetchall()]
        await client.send_message(message.channel,row)
    coun = 1
    for item in row:
        item -= 2
        with connection.cursor() as cursor:
            sql = "UPDATE `Pets` SET hunger =%s WHERE ID=%s"
            cursor.execute(sql, (item,coun))
        coun += 1
    connection.commit()
async def pet_minus_happ(message):
    with connection.cursor() as cursor:
        sql = "SELECT `happy` FROM `Pets`"
        cursor.execute(sql)
        row = [item['happy'] for item in cursor.fetchall()]
        await client.send_message(message.channel,row)
    coun = 1
    for item in row:
        item -= 2
        with connection.cursor() as cursor:
            sql = "UPDATE `Pets` SET happy =%s WHERE ID=%s"
            cursor.execute(sql, (item,coun))
        coun += 1
    connection.commit()
#####################################################################################################################################################
async def cleverbot(message : str):
    """Ask a question to cleverbot"""
    question = message.content.split(None,1)
    print(question)
    try:
        print (message.channel)
        print (message.server)
    except UnicodeEncodeError:
        print('ENCODE ERROR, SKIPPING')
    else:
        answer = cb.ask(question[1])
        nice = ("```md\n")
        meme = ("\n```")
        code = ("[GH]: ")
        answer1 = ("(", answer, ")")
        answer = nice + code + answer + meme
        await client.send_message(message.channel, answer)
        print ("[Response] ", answer)
async def flip(message):
    x = random.randint(0,1)
    if x == 0:
        c = 'heads'
    if x == 1:
        c = 'tails'
    await client.send_message(message.channel,c)
async def midi(message):
    x = message.content.strip('>midi')
    x = x.lower()
    timer1 = datetime.utcnow()
    mid = x.split(None)
    MyMIDI = MIDIFile(1)
    track = 0
    time = 0
    MyMIDI.addTrackName(track,time,"85's text to midi")
    try:
        temp = int(mid[0])
        print(temp)
        MyMIDI.addTempo(track,time,temp)
        del mid[0]
        print(mid)
    except:
        MyMIDI.addTempo(track,time,120)
    track = 0
    channel = 0
    count = 0
    notes = {
    "a":57,
    "b":59,
    "c":60,
    "d":62,
    "e":64,
    "f":65,
    "g":67,
    "*":0,
    "a#":70,
    "c#":61,
    "d#":63,
    "f#":66,
    "g#":68
    }
    try:
        for note in mid:
            pitch = notes[note]
            time = count
            duration = 1
            volume = 100
            count = count + 1
            MyMIDI.addNote(track,channel,pitch,time, duration, volume)
    except KeyError:
        await client.send_message(message.channel,'Error: Key you have entered is not on my scale. please stick to the normal (Western) scale')
        return
    x = "midis/" + message.author.name +".mid"
    if not os.path.isfile(x):
        open(x, 'a')
    with open(x,"br+") as f:
        MyMIDI.writeFile(f)
    f.close()
    timer2 = datetime.utcnow()
    await client.send_file(message.channel,x)
    x = timer2 - timer1
    await client.send_message(message.channel,x)
async def eval_async(message):
    Strp = message.content.split(None, 1)
    resp = eval(Strp[1])
    if asyncio.iscoroutine(resp):
        resp = await resp
    else:
        await client.send_message(message.channel,resp)
async def eight_ball(message):
    question = message.content.strip('>8ball')
    prediction = random.randint(0, len(EIGHT_BALL_OPTIONS) - 1)
    await client.send_message(message.channel, '%s' % (EIGHT_BALL_OPTIONS[prediction]))
async def logo_image(message):
    prediction = random.randint(1, 4)
    filename = (prediction) + (".png")
    f = open(filename, "rb")
    await client.edit_profile(avatar=f.read())
async def changeavy_72(message):
    input = random.randint(1,9)
    inputx = 'A' + str(input)

    await client.send_message(discord.channel('216162726957809664'),input)
async def time_nick(message):
    time = str(datetime.now())
    await client.change_nickname(message.author,time)
async def youtube_search(message):
    try:
        timer1 = datetime.utcnow()
        question = message.content.split(None,1)
        query_string = urllib.parse.urlencode({"search_query": question[1]})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        await client.send_message(message.channel, "http://www.youtube.com/watch?v=" + search_results[0])
        timer2 = datetime.utcnow() - timer1
        time = str(timer2)
        nice = ("```fix\n")
        meme = ("\n```")
        timer3 = nice + time + meme
        await client.send_message(message.channel,timer3)
    except IndexError:
        await client.send_message(message.channel,'No results, Sorry')
async def rule34_search(message):
    nsfw_channels = ['198854364012609536','221869235326943233','190138968891850753','178147364022910976','217032187998896128','179420942374535168','179302255793668096','183796009585868800','213786282189520897','203049357535215616']
    if message.channel.id in nsfw_channels:
        question = message.content.split(None,1)
        try:
            with connection.cursor() as cursor:
                sql = "SELECT `word` FROM `r34_block` WHERE `word`=%s"
                cursor.execute(sql, (question[1]))
                result = cursor.fetchone()['word']
        except TypeError:
            lmao = ['Oh goddammit fine, have this',"F-fine then! Have this! It's not like I wanted to post it or anything..","From my database!","I see that dick out","whos been drawing dicks"]
            query_string = question[1].replace(" ","+")
            url = ("http://rule34.xxx/index.php?page=dapi&s=post&q=index&tags=" + query_string)
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    print(resp.status)
                    x=(message.author.id)
                    y=(message.author.name)
                    z=(message.server.name)
                    c=(message.channel.name)
                    g=resp.status
                    f = await resp.text()
            html_content = f
            images = []
            soup = BeautifulSoup(html_content,"html.parser")
            for link in soup.find_all('post'):
                io = (link.get('file_url'))
                images.append(io)
            number = len(images)
            if number <= 0:
                await client.send_message(message.channel,"No images found")
            else:
                number1 = len(lmao)
                X = random.randint(0,number1)
                Y = random.randint(0,10)
                L = random.randint(0,number)
                line = images[L]
                line = line[2:]
                lines = ("http://") + line
                await client.send_message(message.channel,lines)
                timer3 = 'Total images found: ' + str(number)
                await client.send_message(message.channel,timer3)
                ty = '```\nNSFW COMMAND: \nUSR: ' + x +' '+y + '\nSERVER: '+z+"\nCONTENT: " + lines +'\nHTTP RESPONSE: '+str(g)+'\n```'
                await client.send_message(globalLog,ty)
                if Y >= 7:
                    await client.send_message(message.channel,lmao[X])
                else:
                    return
        else:
            await client.send_message(message.channel,"Search query blacklisted.")
    else:
        await client.send_message(message.channel,"This is not a NSFW channel.")
async def acc(message):
    await client.send_message(message.channel,'Processing command...')
    x = "```fix\n|\n```"
    y = await client.send_message(message.channel,x)
    for x in (0,3):
        asyncio.sleep(0.8)
        x = "```fix\n/ \n```"
        await client.edit_message(y,x)
        asyncio.sleep(0.8)
        x = "```fix\n|\n```"
        await client.edit_message(y,x)
        asyncio.sleep(0.8)
        x = "```fix\n\ \n```"
        await client.edit_message(y,x)
        asyncio.sleep(0.8)
    await client.edit_message(y,'Done.')
async def news(message):
    extr = message.content.strip('>news')
    query = message.content.split(None, 1)
    url = ("http://feeds.bbci.co.uk/news/rss.xml?edition=uk")
    links = []
    d = feedparser.parse(url)
    for post in d.entries:
        io = (post.title + ": " + post.link + "")
        links.append(io)
    news = 'ETS GET ROIIIIIGHT INTO THA NEWZ\n'
    str = '1:\n[' + links[0] + ']\n'
    str1 = '2:\n[' + links[1] + ']\n'
    str2 = '3:\n[' + links[2] + ']\n'
    str3 = '4:\n[' + links[3] + ']\n'
    str4 = '5:\n[' + links[4] + ']\n'
    nice = '```xl\n'
    meme = '```\n'
    total = news + nice + str + str1 + str2 + str3 + str4 + meme
    await client.send_message(message.channel,total)
async def tag_create(message):
    query = message.clean_content.split(None, 2)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `name` FROM `Tags` WHERE `name`=%s"
            cursor.execute(sql, (query[1]))
            check = cursor.fetchone()['name']
    except TypeError:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `Tags` (`name`, `content`,`owner`) VALUES (%s, %s,%s)"
            cursor.execute(sql, (query[1], query[2],message.author.id))
        connection.commit()
        X = "A tag with name: " + query[1] + " Has been created! :metal:"
        await client.send_message(message.channel,X)
    else:
        X = "A tag with name: " + query[1] + " Already exists. Please pick another name"
        await client.send_message(message.channel,X)
async def debug():
    global debug
    if debug == True:
        debug = False
        print(debug)
    if debug == False:
        print(debug)
        debug = True
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Version: V', ver, ' OPlIOS')
    print('-----Justice Rains From Above----')
    channel_number = 0
    name = ("try >help")
    game = discord.Game(name=name)
    await client.change_status(game,idle=True)
    global counter_time
    counter_time = datetime.utcnow()
    global b_a
    global b_b
    global b_bs
    with open('Banned Words.txt') as banned_words:
        b_b = banned_words.read().split(';')

        print ('Blocked Words: ', b_b)
    with open('Admins.txt') as b_admin:
        b_a = b_admin.read().split(';')

        print ('Admins: ', b_a)
    with open('Blacklist.txt') as b_bs:
        b_bs = b_bs.read().split(';')

        print ('Blacklisted Servers: ', b_bs)
    usr_list = client.get_all_members()
    global globalLog
    globalLog = discord.utils.get(client.get_all_channels(), id='219209469714890754')
    global cLog
    cLog = discord.utils.get(client.get_all_channels(), id='219823507997982721')
    global spoopyChannel
    spoopyChannel = discord.utils.get(client.get_all_channels(), id='166384566846750720')

@client.event
async def on_message(message):
    input = message.content.split(None, 1)
    global b_bs
    global b_a
    global b_b
    try:
        if message.channel.id in b_bs:
            return
        if message.author == client.user:
            return
        if input[0] == (">join"):
            x = discord.utils.oauth_url(210695770217644032, permissions=None, server=None, redirect_uri=None)
            y = discord.utils.oauth_url(211994441106325504, permissions=None, server=None, redirect_uri=None)
            z = "**Invite links for both 72 and 85**\n72: "+x+"\n85: "+y
            await client.send_message(message.channel,z)
        if input[0] == ('>kitten'):
            cat = random.randint(100,300)
            kitten = 'https://placekitten.com/200/' + str(cat)
            await client.send_message(message.channel,kitten)
        if input[0] == ('>video'):
            x = 'https://appear.in/'
            y = random.randint(0,3000)
            v = "85bot"
            z = x +v+ str(y)
            await client.send_message(message.channel,z)
        if input[0] == ('>mal-g'):
            await mal(message)
        if input[0] == ('>scan-members'):
            return
        if input[0] == ('>enable-modlog'):
            x = message.author.roles
            coun = 0
            bC = discord.utils.get(message.author.roles, name='Bot Commander')
            if bC != None:
                await client.send_message(message.channel,'Role Found')
                with connection.cursor() as cursor:
                    sql = "INSERT INTO `modLogs` (`server`, `channel`) VALUES (%s, %s)"
                    x = message.server.name
                    y = message.channel.id
                    cursor.execute(sql, (x,y))
                connection.commit()
            else:
                await client.send_message(message.channel,"You do not have the role: Bot Commander. Please go get a role by that name and try again")
        if input[0] == ('>enable-nsfw'):
            x = message.author.roles
            coun = 0
            bC = discord.utils.get(message.author.roles, name='Bot Commander')
            if bC != None:
                await client.send_message(message.channel,'Role Found')
                with connection.cursor() as cursor:
                    sql = "INSERT INTO `modLogs` (`server`, `channel`) VALUES (%s, %s)"
                    x = message.server.name
                    y = message.channel.id
                    cursor.execute(sql, (x,y))
                connection.commit()
            else:
                await client.send_message(message.channel,"You do not have the role: Bot Commander. Please go get a role by that name and try again")        
        if input[0] == ('>pet-img'):
            await pet_img(message)
        if input[0] == ('>pet-feed'):
            await pet_feed(message)
        if input[0] == ('>avy'):
            await client.send_message(message.channel,message.author.avatar_url)
        if input[0] == ('>purge') and message.author.id in ['165568912564420608','190092287722651648']:
            limit1 = message.content.split(None, 2)
            limit2 = int(limit1[1])
            async for message in client.logs_from(message.channel, limit=limit2):#
                if limit1[2] == 'x':
                    await client.delete_message(message)
                if message.content.startswith(limit1[2]):
                    await client.delete_message(message)
        if input[0] == ('>say'):
            x = message.content.split(None,1)
            await client.send_message(message.channel,x[1])
        if input[0] == ('>flip'):
            await flip(message)
        if input[0] == ('>bank-s'):
            await bank_check(message)
        if input[0] == ('>test'):
            await fuck(message)

        if input[0] == ('>midi'):
            await midi(message)
        if input[0] == ('>midi-old'):
            x = "midis/" + message.author.name + ".mid"
            await client.send_file(message.channel,x)
        elif  input[0] == (';up'):
            await update_lists(message)
        elif  input[0] == ('>news'):
            await news(message)
        elif  input[0] == (';add') and message.author.id == "190092287722651648":
            query = message.content.split(None, 1)
            with connection.cursor() as cursor:
            # Create a new record
                sql = "INSERT INTO `BotMods` (`ID`) VALUES (%s)"
                cursor.execute(sql, (query[1]))
            connection.commit()
        elif  input[0] == ('lmao') and message.author.id == "190092287722651648":
            await client.send_message(message.channel, "Ceru! Stop saying that!")
        elif  input[0] == ('lmao') and message.author.id == "165554656380977152":
            await client.send_message(message.channel, "**Jade! Please stop saying lmao >,~,< your going to make me cry**")
        elif  input[0] == (';bl') and message.author.id in ["164129004998098945","190092287722651648"]:
            #await banned_word(message)
            declass = message.content.split(None, 1)
            with connection.cursor() as cursor:
                sql = "INSERT INTO `r34_block` (`word`) VALUES (%s)"
                cursor.execute(sql, (declass[1]))
            connection.commit()
            #await reset()

        elif  input[0] == (';bb') and message.author.id in b_a:
            Str = message.server.id
            splitMod = ';'
            Str2 = Str + splitMod
            with open("Blacklist.txt", "a") as myfile:
                myfile.write(Str2)

            print ("Added Blocked Word: ", Str[1])

        #-=-=-=-=-=-=-=-=-=-=-=-
        #Start of real commands
        #
        #
        #-=-=-=-=-=-=-=-=-=-=-=-
        if input[0] == ('>eval') and message.author.id == "190092287722651648":
            await eval_async(message)
        if input[0] == ('>pet-s'):
            print ('PET STAT')
            await pet_stat(message)
        if input[0] == ('>pet-rename'):
            await pet_re(message)
        if input[0] == ('>pet-c'):
            print ('PET CREATE')
            await pet_create(message)
        if input[0] == ('>emote'):
            x = client.get_all_emojis()
            emoji = []
            for y in x:
                emoji.append(y)
            print (y)
        if input[0] == ('>pet-cuddles'):
            print ('PET CUDDLES!')
            print (message.author)
            await pet_cuddle(message)
        if input[0] == ('>secret-1423'):
            await client.send_message(message.author,"aHR0cDovL2kuaW1ndXIuY29tL2tiMWhkN0QucG5n")
        elif  input[0] == ('>fp'):
            try:
                query = message.content.split(None, 1)
                images2 = []
                items = imgur.gallery(section='top', sort='time', page=0, window='day', show_viral=True)
                for item in items:
                    images2.append(item.link)
                number = int(query[1])
                await client.send_message(message.channel,images2[number])
            except IndexError:
                await client.send_message(message.channel,'Error: Number too high')
        elif  input[0] == ('>help'):
            helpmsg = await client.send_message(message.channel, helpmessage)
        elif  input[0] == ('>reset') and message.author.id == "190092287722651648":
            await reset()
        elif  input[0] == ('>r34'):
            await rule34_search(message)

        elif  input[0] == ('>retcon') and message.author.id == "190092287722651648":
            limit1 = message.content.split(None, 2)
            counter = (0)
            limit2 = int(limit1[1])
            async for message in client.logs_from(message.channel, limit=limit2):
                if message.author == client.user:
                    counter += 1
                    await client.delete_message(message)
        if  input[0] == ('>g'):
            #await client.send_message(message.channel, "Sorry, but google have rate limted the bot at this current time [Too many people like this command :/]")
            timer1 = datetime.utcnow()
            Strip2 = message.content.strip('>g ')
            Strip3 = Strip2.lower()
            if Strip3 in b_b:
                await client.send_message(message.channel, "Sorry, I cannot allow that. [Word in search has been blacklisted by a mod]")
            else:
                url = next(search(Strip2, tld='com', lang='en',safe=True, num=1, start=0, stop=2, pause=2.0))
                if 'rule34' in url:
                    await client.send_message(message.channel, "Sorry, I cannot allow that. [Word in search has been blacklisted by a mod]")
                elif 'porn' in url:
                    await client.send_message(message.channel, "Sorry, I cannot allow that. [Word in search has been blacklisted by a mod]")
                elif 'adult' in url:
                    await client.send_message(message.channel, "Sorry, I cannot allow that. [Word in search has been blacklisted by a mod]")
                elif url in b_b:
                    await client.send_message(message.channel, "Sorry, I cannot allow that. [Word in search has been blacklisted by a mod]")
                else:
                    await client.send_message(message.channel, url)
                    timer2 = datetime.utcnow() - timer1
                    time = str(timer2)
                    nice = ("```fix\n")
                    meme = ("\n```")
                    timer3 = nice + time + meme
                    await client.send_message(message.channel,timer3)
        elif  input[0] == ('>8ball'):
            await eight_ball(message)
        elif  input[0] == (">chat"):
            await cleverbot(message)
        elif  input[0] == ('>time'):
            print ('time command')
            global counter_time
            counter = datetime.utcnow() - counter_time
            await client.send_message(message.channel, "I have been online for: %s seconds" %(counter))
        if input[0] == ('>meme') and message.author.id == "190092287722651648":
            voice1 = discord.utils.get(message.server.channels,id='182269866496098313')
            player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=hqCbx5LQIlw')
            player.start()
            
        if input[0] == ('>te'):
            text = message.clean_content.split(None, 2)
            try:
                with connection.cursor() as cursor:
                    sql = "SELECT `owner` FROM `Tags` WHERE name=%s"
                    cursor.execute(sql, (text[1]))
                    check = cursor.fetchone()['owner']
                    if check == message.author.id:
                        with connection.cursor() as cursor:
                            sql = "UPDATE `Tags` SET content=%s WHERE name=%s"
                            cursor.execute(sql, (text[2],text[1]))
                        connection.commit()
                        await client.send_message(message.channel, "**Updated tag**")
                    else:
                        await client.send_message(message.channel, "**You dont own that tag**")
            except TypeError:
                await client.send_message(message.channel, "**You dont have any tags**")
        if input[0] == ('>td'):
            text = message.clean_content.split(None, 2)
            try:
                with connection.cursor() as cursor:
                    sql = "SELECT `owner` FROM `Tags` WHERE name=%s"
                    cursor.execute(sql, (text[1]))
                    check = cursor.fetchone()['owner']
                    if check == message.author.id:
                        with connection.cursor() as cursor:
                            sql = "DELETE FROM `Tags` WHERE name=%s"
                            cursor.execute(sql, (text[1]))
                        connection.commit()
                        await client.send_message(message.channel, "**Deleted tag**")
                    else:
                        await client.send_message(message.channel, "**You dont own that tag**")
            except TypeError:
                await client.send_message(message.channel, "**You dont have any tags**")

           
        if  input[0] == ('>tt'):
            query = message.content.split(None, 1)
            try:
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "SELECT `content` FROM `Tags` WHERE `name`=%s"
                    cursor.execute(sql, (query[1],))
                    result = cursor.fetchone()['content']
                    await client.send_message(message.channel, result)
            except TypeError:
                t = "There isnt a tag called: " + query[1]
                await client.send_message(message.channel,t)
        if input[0] == ('>ts'):
            try:
                with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                    sql = "SELECT `owner` FROM `Tags` WHERE `name`=%s"
                    cursor.execute(sql, (input[1]))
                    check = cursor.fetchone()['owner']
            except TypeError:
                x="there is no tag called: "+input[1]
                await client.send_message(message.channel,x)
            else:
                user = discord.utils.get(message.server.members, id=check)
                x = "The owner of that tag is: " + user.name
        if input[0] == ('>tl'):
            try:
                user = input[1]
            except IndexError:
                user = message.author.id
            with connection.cursor() as cursor:
                sql = "SELECT `name` FROM `Tags` WHERE owner=%s"
                cursor.execute(sql, (user))
                check = cursor.fetchall()
                xyz = len(check)
            list = []
            for x in check:
                list.append(x['name'])
            encode = ", ".join(list)
            encoded = "User owns these tags: \n**"+encode+"**"
            await client.send_message(message.channel,encoded)
        elif input[0] == ('>tc'):
            await tag_create(message)
        elif  input[0] == ('>changeavy'):
            await logo_image(message)
        elif message.author == 'Aradiabot#6115' or 'SHRUG' in message.content.lower():
            await client.send_message(message.channel, "https://i.imgur.com/kPkNrB1.gif")
        elif input[0] == ('>ping'):
            url = ("http://discordapp.com")
            time1 = datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    status = resp.status
                    reason = resp.reason
                    host = resp.host
            time2 = datetime.utcnow()
            if status == 200:
                y = ('We are good to go! :ok_hand:')
            else:
                y = ('ERROR')
            xyz = str(time2 - time1)
            x = y + '\n```fix\nCONNECTION STATS: \nSTATUS CODE: ' + str(status) + '\nREASON: '+ reason + '\nHOST: ' +host + '\n TIME TAKEN: '+ xyz+'\n```'
            await client.send_message(message.channel, x)
        elif input[0] == ('>ping-r34'):
            url = ("rule34.xxx")
            time1 = datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    status = resp.status
                    reason = resp.reason
                    host = resp.host
            time2 = datetime.utcnow()
            if status == 200:
                y = ('We are good to go! :ok_hand:')
            else:
                y = ('ERROR')
            xyz = str(time2 - time1)
            x = y + '\n```fix\nCONNECTION STATS: \nSTATUS CODE: ' + str(status) + '\nREASON: '+ reason + '\nHOST: ' +host + '\n TIME TAKEN: '+ xyz+'\n```'
            await client.send_message(message.channel, x)
        elif input[0] == ('>ping-c'):
            url = input[1]
            if validators.domain(input[1]):
                time1 = datetime.utcnow()
                url = 'http://' + url
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        status = resp.status
                        reason = resp.reason
                        host = resp.host
                time2 = datetime.utcnow()
                if status == 200:
                    y = ('We are good to go! :ok_hand:')
                else:
                    y = ('ERROR')
                xyz = str(time2 - time1)
                x = y + '\n```fix\nCONNECTION STATS: \nSTATUS CODE: ' + str(status) + '\nREASON: '+ reason + '\nHOST: ' +host + '\n TIME TAKEN: '+ xyz+'\n```'
                await client.send_message(message.channel, x)
            else:
                await client.send_message(message.channel, "Input is not a url.")
        elif  input[0] == ('>mercy'):
            await client.send_message(message.channel, 'https://66.media.tumblr.com/74b048f44f118738017f83b49f889d81/tumblr_o6zxbiOLZJ1qmfxrio4_500.gif')
        elif  input[0] == ('>mei'):
            await client.send_message(message.channel, 'https://67.media.tumblr.com/05d87ee3f275f3e4a347a66dc357df2d/tumblr_oa2ax5DagB1qgpem8o1_500.gif')
        elif  input[0] == ('>xefros'):
            await client.send_message(message.channel, 'http://66.media.tumblr.com/4c91d2176c852f24b5f70183d2122d8a/tumblr_o9vp76yvR51qfe7z2o1_500.png')
        elif  input[0] == ('>slenny'):
            await client.send_message(message.channel, "( ͡~ ͜ʖ ͡°)")
        elif  input[0] == ('>y'):
            await youtube_search(message)
        elif  input[0] == ('>tea'):
            await client.send_message(message.channel, "Please wait, making you a nice cup of green tea! ^w^")
            lol = ["~~dont drink 72's coffee. i hear is tainted~~","Why drink coffee when you can have a nice relaxing tea!","♓️🅰R🅰♍️🅱📧 made it for you","Made with love <3~"]
            ran = random.randint(0,3)
            x = "Here you go: :tea:, Enjoy!" + lol[ran]
            await client.send_message(message.author,x)
        elif  input[0] == ('>coffee'):
            await client.send_message(message.channel, "Dont try 72's coffee, tea will always be better")
        if input[0] == ('>pet-kill'):
            await client.send_message(message.channel, "Dont. You. Dare.")
        elif  input[0] == ('>fu'):
            await client.send_message(message.channel,"ᶠᶸᶜᵏ♥ᵧₒᵤ")
        if input[0] == ('>cid'):
            await client.send_message(message.channel,message.channel.id)
    except IndexError:
        pass



client.run("BOT_TOKEN", bot=True)
