import discord


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.voice_states = True


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_voice_state_update(self, member, before, after):
        if str(member) == "mediumrare2299":
            if before.channel is None and after.channel is not None:
                print(f"{member.name} has joined {after.channel.name}")

                if member.dm_channel is None:
                    await member.create_dm()
                await member.dm_channel.send(
                    f"Remember to text Jenna about joining VC!"
                )


client = MyClient(intents=intents)
client.run("addyourapikeyhere")
