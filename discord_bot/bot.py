import discord
from discord.ext import commands
from utils.website_api import get_website_roles, sync_roles_with_discord
from utils.discord_api import assign_role, remove_role
from config import BOT_TOKEN

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('Bot is ready')
    bot.loop.create_task(check_website_roles())  # Start periodic role synchronization

@bot.event
async def on_member_join(member):
    await sync_roles_with_discord(member)

@bot.command()
async def sync(ctx):
    await ctx.send("Syncing roles...")
    await sync_roles_with_discord(ctx.author)
    await ctx.send("Roles synced successfully!")

async def check_website_roles():
    while True:
        website_roles = get_website_roles()

        for guild in bot.guilds:
            for member in guild.members:
                await sync_roles_with_discord(member, website_roles)

        print("Website roles checked. Synchronization completed.")

        # Sleep for a week (adjust the interval as needed)
        await asyncio.sleep(7 * 24 * 60 * 60)

async def sync_roles_with_discord(member, website_roles=None):
    if website_roles is None:
        website_roles = get_website_roles()

    # Compare website roles with Discord server roles
    # Assign or remove roles based on the criteria

    # Example code: Assign a role
    role_id = website_roles.get(member.id)
    if role_id:
        role = member.guild.get_role(role_id)
        await assign_role(member, role)

    # Example code: Remove a role
    else:
        role_to_remove = None  # Specify the role to remove
        if role_to_remove:
            await remove_role(member, role_to_remove)

async def assign_role(member, role):
    await member.add_roles(role)
    print(f"Assigned role {role.name} to {member.name}")

async def remove_role(member, role):
    await member.remove_roles(role)
    print(f"Removed role {role.name} from {member.name}")

if __name__ == '__main__':
    bot.run(BOT_TOKEN)


if __name__ == '__main__':
    bot.run(BOT_TOKEN)