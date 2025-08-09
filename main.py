import discord
from discord.ext import commands
import os

# Configuração do Bot (apenas o token via variável de ambiente)
TOKEN = os.environ['TOKEN']  # Obrigatório no Railway

# IDs dos Canais (hardcoded conforme solicitado)
WELCOME_CHANNEL_ID = 1403597123362095174  # Canal de boas-vindas
RULES_CHANNEL_ID = 1403596753927934164    # Canal de regras

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="o canal #boas-vindas"
    ))

@bot.event
async def on_member_join(member):
    try:
        # Obter os canais pelos IDs fixos
        welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)
        rules_channel = bot.get_channel(RULES_CHANNEL_ID)
        
        embed = discord.Embed(
            title=f"🎉 Bem-vindo(a) {member.name}!",
            description=f"Leia as regras em {rules_channel.mention}",
            color=0x5865F2  # Roxo do Discord
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(
            name="📌 Não esqueça:",
            value="1. Verificar seu e-mail\n2. Ler as regras\n3. Explorar os canais",
            inline=False
        )
        
        await welcome_channel.send(embed=embed)
        
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem: {e}")

if __name__ == "__main__":
    bot.run(TOKEN)
