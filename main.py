from asyncio.tasks import create_task, sleep
from typing import MutableSequence
import discord
from discord import role
from discord import client
from discord import activity
from discord import user
from discord import member
from discord import channel
from discord import guild
from discord import message
from discord import permissions
from discord import mentions
from discord import embeds
from discord.embeds import Embed
from discord.enums import DefaultAvatar
from discord.ext import commands
from PIL import Image
from io import BytesIO
from discord.ext.commands import context
from discord.ext.commands.errors import CommandNotFound
from discord.flags import Intents
import asyncio

bot = commands.Bot(command_prefix="_", Intents=Intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="BUO(Blox Universe Online)"))

@bot.event
async def on_member_join(member):
    salon = member.guild.get_channel(880837897639571597)
    await salon.send(f"**Bienvenue sur le server {member.mention}** :partying_face:\n \n")   

@bot.command()
async def botinfos(ctx):
    embd = discord.Embed(title=bot.user.name, description=f"**Bot crée par 𝕮𝖚𝖗𝖎𝖔𝖚𝖘#6555, commandes: **")
    embd.set_thumbnail(url=bot.user.avatar_url)
    await ctx.send(embed=embd)

@bot.command()
async def clear(ctx, number : int):
    msg = await ctx.channel.history(limit=number + 1).flatten()
    for clr in msg:
        await clr.delete()

@bot.command()
@commands.has_role("👑Devs👑")
async def pref(ctx, name):
    await ctx.message.delete()
    bot.command_prefix = name
    await ctx.send(f"**le prefix est maintenant  {bot.command_prefix}**")  

@bot.command()
async def verif(ctx):
    await ctx.message.delete()
    membre = ctx.guild.get_role(864488048753115156)
    await ctx.author.add_roles(membre)
    msg = await ctx.channel.history(limit = 1).flatten()
    for msgs in msg:
        await msgs.delete()

@bot.command()
@commands.has_role("Administrateur")
async def kick(ctx, user:discord.User, *reason):
    await ctx.message.delete()
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"**{user} a été kick pour la raison suivante: __{reason}__**")

@bot.command()
@commands.has_role("Chef Administrateur")
async def ban(ctx, user:discord.User, *reason):
    await ctx.message.delete()
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"**{user} a été ban pour la raison suivante: __{reason}__**")

@bot.command()
@commands.has_role("Animateur")
async def setevent(ctx, name, description):
    await ctx.message.delete()
    channel = await ctx.guild.create_text_channel(name="EVENT")
    await channel.send("@everyone event en cours")
    embd = discord.Embed(title=name)
    embd.set_thumbnail(url="https://emoji.gg/assets/emoji/3205-blob-stagevc.png")
    embd.add_field(name="description", value=description)
    await channel.send(embed=embd)

@bot.command()
@commands.has_role("Animateur")
async def delevent(ctx):
    await ctx.message.delete()
    chan = ctx.guild.channels
    for chans in chan:
        if chans.name == "event":
            await chans.delete()
            return
    await ctx.send("Il n'y a pas d'event en cours")

@bot.command()
@commands.has_role("Chef Administrateur")
async def send(ctx, text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command()
@commands.has_role("Chef Administrateur")
async def send2(ctx, text):
    await ctx.message.delete()
    await ctx.send(f"**{text}**")

@bot.command()
async def setsuggest(ctx, name):
    channel = ctx.guild.get_channel(864570389531197500)
    valide = ctx.guild.get_channel(881563703600873503)
    msg = await channel.send(f"Sugjestion de **{ctx.author.name}#{ctx.author.discriminator}:** \n \n **{name}**")

@bot.command()
async def tempmute(ctx, member : discord.Member, time : int):
    if time < 86400:
        role = ctx.guild.get_role(881955231963947009)
        await member.add_roles(role)
        await asyncio.sleep(time)
        await member.remove_roles(role)
    else:
        await ctx.send("**L'utilisateur ne peut'etre mute pendant plus de 48h**")
@bot.command()
async def mute(ctx, member : discord.member.Member):
    role = ctx.guild.get_role(881955231963947009)
    await member.add_roles(role)

@bot.command()
async def unmute(ctx, member : discord.Member):
    role = ctx.guild.get_role(881955231963947009)
    await member.remove_roles(role)

@bot.command()
async def channel(ctx, name):
    await ctx.guild.create_text_channel(name=name)

@bot.command()
async def vchannel(ctx, name):
    await ctx.guild.create_text_channel(name=name)

@bot.command()
async def maintenance(ctx):
    user = ctx.guild.members
    role = ctx.guild.get_role(884166257656614963)
    for users in user:
        await users.add_roles(role)

@bot.command()
async def unmaintenance(ctx):
    user = ctx.guild.user
    role = ctx.guild.get_roles(884166257656614963)
    for users in user:
        await users.remove_roles(role)

bot.run("ODY5MzM4MDAxNDMwNDIxNTI0.YP8wGw.zTpHLOxzT-ar8RvzKPM7w8FjuZM")