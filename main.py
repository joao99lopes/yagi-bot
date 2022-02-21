import discord
from discord.ext import commands, tasks
from itertools import cycle
from pomodoro import Pomodoro
import asyncio

client = commands.Bot(command_prefix='>')
status = cycle(['Sims2', 'Snake', 'PacMan', 'Fifa Street'])

local_pomodoro = Pomodoro()

@client.event
async def on_ready():
    change_status.start()
    channel = client.get_channel(786731799895343155)
    await channel.send('Buenos dias Matosinhos')
    print("Bot is ready.")


@client.event
async def on_member_join(member):
    channel = client.get_channel(786731799895343155)
    await channel.send(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    channel = client.get_channel(786731799895343155)
    await channel.send(f'{member} has left the server.')


@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def ping(ctx):
    await ctx.send(f'Ping é mas é o cacetinho! Já pediste isso {round(client.latency * 1000)} vezes')


@client.command()
async def pomodoro(ctx):
    args = ctx.message.content.split(' ', 2)
    if len(args) < 2:
        await ctx.send("Missing arguments\nTry one of this:\n" + local_pomodoro.get_help())
    else:
        cmd = args[1]
        if cmd not in ("start", "work-time", "rest-time", "round-limit", "help"):
            await ctx.send("Wrong arguments\nTry one of this:\n" + local_pomodoro.get_help())
        else:
            print(cmd,"\n")
            if cmd == "start":
                loop = asyncio.get_event_loop()
                loop.create_task(start(ctx))
            elif cmd == "help":
                await ctx.send(local_pomodoro.get_help())



async def start(ctx):
    local_pomodoro.set_is_running(True)
    is_working = True
    counter = local_pomodoro.get_number_of_rounds()

    while counter > 0:
        if is_working:
            t = local_pomodoro.get_work_time()*60
            await ctx.send("Pomodoro Round {}... START! :tomato:".format((int(local_pomodoro.get_number_of_rounds())-counter+1)))
        else:
            t = local_pomodoro.get_rest_time()*60
            await ctx.send("Pomodoro Round {}... REST! :tomato:".format(local_pomodoro.get_number_of_rounds()-counter+1))
            counter -=1
        while t > 0:
            if not (t > 5):
                msg = ":tomato:"*t
                await ctx.send(msg+"\n")
            await asyncio.sleep(1)
            t -= 1
        is_working = not is_working
    local_pomodoro.set_is_running(False)



client.run('OTQ0Njc3MzI5MzI4ODA3OTM3.YhFFUg.QtvBLxiiKuD59kcB4ANkyy5gd_w')
