import discord
from discord.ext import commands
import os

prefix = '!'

bot = commands.Bot(command_prefix= prefix)

ban_msg = ['fuck, да']

bot.remove_command("help")

#Скрипт "Модерация чата"
@bot.event
async def on_message(msg):
    for i in ban_msg:
        if i in msg.content:
            await bot.delete_message(msg)

    await bot.process_commands(msg)

#Скрипт "Автороли"
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name= 'Легионер')
    await member.add_roles(role)

#Скрипт "Начало лаботы"
@bot.event 
async def on_ready():
    print ("Ready to work!")

#Команда !h
@bot.command(pass_context= True)
async def h(ctx):
    emb = discord.Embed(title= 'Info about command', collor= 0x2472bf)
    emb.add_field(name= '{}help'.format(prefix), value= 'Shows this embed')
    emb.add_field(name= '{}status'.format(prefix), value= 'Shows Bot status')
    emb.add_field(name= '{}mute'.format(prefix), value= 'Ограничивает сообщения: !mute @Seraf')
    await ctx.send(embed= emb)

#Команда !moder
@bot.command(pass_context= True)
async def moder(ctx):
    emb = discord.Embed(title= 'Список для модераторов', collor= 0x324325)
    emb.add_field(name= '{}helpm'.format(prefix), value= 'Показывает этот список')
    emb.add_field(name= '{}mute'.format(prefix), value= 'Огарничивает сообщения: !mute @Seraf')
    await ctx.send(embed= emb)

#Команда !status
@bot.command(pass_context= True)
async def st(ctx):
    await ctx.send('On')

#Команда !mute
@bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name= "mute")
    await member.add_roles(mute_role)

#Команда !ban
@bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def ban(ctx, user: discord.Member):
    await member.ban(user)




token = os.environ.get('BOT_TOKEN')