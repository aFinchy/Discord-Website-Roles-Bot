import discord
from config import BOT_TOKEN

async def assign_role(member, role):
    try:
        await member.add_roles(role)
        print(f"Assigned role {role.name} to {member.name}")
    except discord.HTTPException as e:
        print(f"Failed to assign role {role.name} to {member.name}: {e}")

async def remove_role(member, role):
    try:
        await member.remove_roles(role)
        print(f"Removed role {role.name} from {member.name}")
    except discord.HTTPException as e:
        print(f"Failed to remove role {role.name} from {member.name}: {e}")

# Other functions for interacting with the Discord API can be added here
