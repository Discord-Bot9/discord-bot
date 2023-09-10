import discord
from discord.ext import commands

class Rolsüz(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command(name="rolsüz", help="Rolsüz olan kullanıcıları atar.")
    async def rolsüz(self, ctx):
        for member in ctx.guild.members:
            if not any(member.has_role(role) for role in ctx.guild.roles):
                await member.kick()

class Rolver(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command(name="rolver", help="Bir kullanıcıya rol verir.")
    async def rolver(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)

bot = commands.Bot(command_prefix="!")

bot.add_cog(Rolsüz(bot))
bot.add_cog(Rolver(bot))

bot.run("MTE0OTQ2NjM3MTk1MzAwMDQ1MA.G2IEqE.s4UdMbSzdr7djwlMS2cgZePW9HpKfaI416a5t4")