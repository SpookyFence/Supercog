# -*- coding: utf-8 -*-
import discord
import os
import random
from discord.ext import commands
from .utils import checks
from cogs.utils.dataIO import dataIO

class supercog:
    def __init__(self, bot):
        self.bot = bot
        self.filename = 'data/gay/gay.json'
        self.gay = dataIO.load_json(self.filename)            

    async def save_gays(self):
            dataIO.save_json(self.filename, self.gay)
        
    @commands.command(pass_context=True)
    async def truth(self, context, user : discord.Member):
        '''Reveals the truth of the universe 👀
	(100% accurate)
	'''
        server = context.message.server
        author = context.message.author
        if user.id == '208268769452097537' or user.id == '411296631112073216' :#Silver
            message = (user.mention + " is as straight as an arrow")
        elif user.id == '146776905956327425':#ruler
            message = (user.mention + " 는 게이입니다.")
        elif user.id == '163670747787689994':#bingbong
            bingbong = random.randint(0, 1)
            if bingbong == 0:
                message = (user.mention + " hab gae")
            elif bingbong == 1:
                message = (user.mention + " is so gae his mum turnd gae")
        elif user.id == '190519714529673216':#electro
            message = (user.mention + " sucks both regular and spotted dick")
        elif user.id == '90881082802581504':#z
            message = (user.mention + " is not gay because he is a scary murderbot and will kill me otherwise :(")
        elif user.id == '155530711326130176':#inrix
            message = (user.mention + " is gay for Big Mac")
        elif user.id == '262146238852497411':#rosa
            message = (user.mention + " is a pink fox. that is all")
        elif user.id == '136220914911019009':#nifl
            message = (user.mention + " is so gay he turned zach bi") 
        elif user.id == '131447879876345857': #lycan
            message = (user.mention + " is gay. literally.") 
        elif user.id == '145728974604075008' or user.id == '145777576420442112': #vinnie
            message = (user.mention + " was born gay and thinks cuddles are nice.")
        elif user.id == '80318518901342208': #officialy
            message = (user.mention + " is so gay he leaked nudes")
        elif user.id == '244232045528743946': #Zacharais
            message = (user.mention + " is gay and built a gay tank with a gay skull on it")
        #======================================================================
        #Servers
        elif server.id == '279855495035092993':#gaem central
            message = (user.mention + " hab gae")
        else:
            message = (user.mention + " is gay")
        await self.bot.say(message)

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def thot(self, *, user : discord.Member):
        """Detects how much of a thot a user is."""
        state = random.getstate()
        random.seed(user.id)
        thotLevel = random.randint(0, 30)
        max = 30
        thot = "[{}".format("█ " * thotLevel)
        notthot = "{}]".format("▯" * (max-thotLevel))
        random.setstate(state)
        if thotLevel == 30:
            await self.bot.say("detecting thot level: " + thot+ notthot)
            await self.bot.say("MAXIMUM THOT DETECTED. BEGONE! BEGONE!")
        elif thotLevel == 0:
            await self.bot.say("detecting thot level: " + thot + notthot)
            await self.bot.say("What a nice young man you are, not a thot at all")
        else:
            await self.bot.say("detecting thot level: " + thot + notthot)

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ree(self):
        "FetishBot 9001: certified REEE master"
        dong = "R{}!".format("E" * random.randint(10, 50))
        await self.bot.say(dong)

    @commands.command()
    async def tree(self):
        "FetishBot 9001: uncertified tree surgeon"
        length = ("""
.
                .#.
             .###.
         .#%##%.
      .%##%###.
   .##%###%##.
.#%###%##%##.
                #
                #
          """)      
        await self.bot.say(length)

    @commands.command()
    async def poet(self):
        "FetishBot 9001: certified Robert Burns impersonator"
        dong = "Oh the pelican, How smoothly doth he crest, a Wind God!"
        await self.bot.say(dong)
    @commands.command()
    async def jester(message, after):
        "FetishBot9001: certified jester fan"
        if str(after.status) == "online":
            jester=("@Sir Inrix | <3#6950 fix jester or riot")
        self.bot.say(jester)
        


def setup(bot):
    bot.add_cog(supercog(bot))

