#!/usr/bin/env python3
import ast, asyncio, datetime, discord, discord.utils, linecache, sys
from discord.ext import commands

async def failrespond():
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename,lineno,f.f_globals)
        return '`ERROR on line:` {}\n`Code:` ```python\n{}\n````Exception:` {}'.format(lineno,line.strip(),exc_obj)

async def conv2dict(convinput):
    return ast.literal_eval(convinput)

class General():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def emb(self,ctx,*,kwargs):
        await self.bot.say("self: {0}\nctx: {1}\nkwargs: {2}".format(self,ctx,kwargs))
        for key, value in kwargs:
            await self.bot.say("{0} = {1}".format(key, value))
        return

    @emb.error
    async def emb_error(self, error, ctw):
        await self.bot.say("{0} | {1}".format(error,ctw))
        return

    @commands.command(pass_context=True)
    async def test(self,ctx,*,txtinput):
        txtconv = await conv2dict("{{{0}}}".format(txtinput))
        if 'title' not in txtconv or 'text' not in txtconv or 'color' not in txtconv:
            await self.bot.say("You're missing a parameter, dumbass.")
        else:
            try:
                        #title is not the top line, but the one below it.                 #title color                     #title link to                #text under title
                        # url can happen after colour
                embed = discord.Embed(title=txtconv['title'], colour=discord.Colour(txtconv['color']), url=" ", description=txtconv['text'], \
                                  timestamp=datetime.datetime.utcfromtimestamp(1497651933))
                                  # ^ timestamp at the VERY bottom.
                            #Very bottom image, above signature.
                #embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
                                #thumbnail in top right.
                embed.set_thumbnail(url=ctx.message.author.avatar_url[:-10])
                             #title at top       #make it a link               #grab icon
                #embed.set_author(name="author name", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
                             #very bottom, signature #icon at bottom, squared.
                #embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
                            #Emoji with text tied to it (under)
                #embed.add_field(name="🤔", value="some of these properties have certain limits...")
                #embed.add_field(name="😱", value="try exceeding some of them!")
                #embed.add_field(name="🙄", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
                            #Kinda like tables
                #embed.add_field(name="<:thonkang:219069250692841473>", value="these last two", inline=True)
                #embed.add_field(name="<:thonkang:219069250692841473>", value="are inline fields", inline=True)
                await self.bot.say(embed=embed)
            except:
                await self.bot.say(await failrespond())
        return

def setup(bot):
    bot.add_cog(General(bot))

