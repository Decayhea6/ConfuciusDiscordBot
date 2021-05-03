#ctrl-c to cancel
import os
import discord
from time import sleep
import json
client = discord.Client()

@client.event
async def on_ready():
    print('Currently vibing as {0.user}'.format(client))
    print("remember, you can kill me using ctrl-c")


@client.event
async def on_message(message):
    sep_words = message.content.split()
    if message.author == client.user:
        return
#this makes it so that confucious does not respond to himself


#random sentences
    elif "I need dating advice" in message.content or "the nasty nasty" in message.content:
        await message.channel.send('Good to meet girl in park. Better to park meat in girl.')
    elif "p0tat0" in message.content.split() or "p0tat0es" in message.content.split():
        await message.channel.send('Friends are like potatoes. If you eat them, they die. :(')
    elif  "I am a clown" in message.content:
        await message.channel.send('You are not just a clown, but the entire circus.')
    elif  "group of ravens" in message.content:
        await message.channel.send('An Unkindness')
    elif  "group of crows" in message.content:
        await message.channel.send('A Murder')
    elif  "drink and drive" in message.content:
        await message.channel.send('A man who drive like hell, bound to get there.')
    elif  "not solve world peace" in message.content:
        await message.channel.send('It is only when a mosquito lands on your testicles that you realize there is always a way to solve problems without violence.')
    elif "nurse" in message.content:
        await message.channel.send('Man who want pretty nurse, must be patient.')
    elif "time travel" in message.content:
        await message.channel.send('Time flies like an arrow. Fruit flies like banana.')
    elif "kiss" in message.content or "smooch" in message.content:
        await message.channel.send("Passionate kiss like spider web, soon lead to undoing of fly")
    elif "I hate my life" in message.content or "fuck fuck fuck" in message.content:
        await message.channel.send("Ok for shit to happen, will decompose.")
    elif "covid-19" in message.content or "don't wash hands" in message.content:
        await message.channel.send("Support bacteria - is only culture some people have")
    elif "butchered" in message.content or "butcher" in message.content:
        await message.channel.send("Butcher who back into meat grinder get a little behind in his orders")
    elif "peanut butter" in message.content or "I hope I don't have allergies" in message.content:
        await message.channel.send("Man with penis in peanut butter jar, fucking nuts")
    elif "kill me" in message.content:
        await message.channel.send("https://tenor.com/view/china-man-gun-gif-18153983")
    elif "when jackbox" in message.content:
        await message.channel.send("https://tenor.com/view/run-running-fast-basketball-court-sprint-gif-16667898")
    elif "what is a potato" in message.content:
        await message.channel.send("An erect South American herb (Solanum tuberosum) of the nightshade family widely cultivated for its edible starchy tuber. For the potato cult, see: shorturl.at/opDT1")
    elif "what is a chicken" in message.content:
        await message.channel.send("An animal that was created simply to cross roads.")
    elif "sussy" in message.content:
        await message.add_reaction("🥸")
    elif "sus" in sep_words:
        await message.add_reaction("😈")
    elif "minimalism" in message.content:
        await message.channel.send("Love people and use things, because the opposite never works.")
    elif "muffins" in message.content:
        await message.channel.send("So theres these muffins, baking in an oven. One muffin says, gee its hot in here!")
        await message.channel.send('The other muffin responds: "were both gonna die and no one will hear us scream."')
    elif "shit thats deep" in message.content:
        await message.channel.send("https://www.youtube.com/watch?v=L_jWHffIx5E")
    elif "switch" in message.content.split():
        await message.channel.send("clearly the Retro Video Game Console Player Handheld Gaming Portable Mini Arcade Videogames Electronic Machine Retrogame Play Vidio from alibaba express is superior in every way.")
#actual functions
#    elif "a" in sep_words

    elif ("+" in sep_words) or ("-" in sep_words) or ("/" in sep_words) or ("*" in sep_words) or ('^' in sep_words):
        symbols = 0
        result = None
        numbers = 0
        num1 = None
        num2 = None
        symbol = ""
        for word in sep_words:
            if num1 == None:
                try:
                    num1 = float(word)
                    numbers += 1
                except:
                    print(word + " is not a number XD")
            else:
                try:
                    num2 = float(word)
                    numbers += 1
                except:
                    print(word + " is not a number XD")
            if word in ["+", "-", "/", "*", "^"]:
                symbols += 1
                symbol = word
        if symbols == 1 and numbers == 2:
            if symbol == "+":
                result = num1 + num2
            elif symbol == "-":
                result = num1 - num2
            elif symbol == "/":
                result = num1 / num2
            elif symbol == "*":
                result = num1 * num2
            elif symbol == "^":
                result = num1 ** num2
            await message.channel.send(str(result))


#of course

    elif "Confucius" in message.content:
        await message.channel.send("https://tenor.com/view/what-the-hell-you-want-now-stare-what-do-you-want-what-do-you-need-gif-17590345")


client.run('Mzc5NzQ1NDUyNDM1NzAxNzYw.WgoPgw.W59O45lvlWcRHA-jrI0vifhM9l8')
