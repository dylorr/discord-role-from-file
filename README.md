# Role Discord Members (by username) from File


### Bot Setup
1. Navigate to https://discord.com/developers/applications 
2. Create a new application
3. Navigate to the "Bot" tab
4. Make sure "Public Bot" is checked
5. Turn on "Server Members Intent" under "Priveleged Gateway Intents"
6. Navigate to "OAuth2" and the "URL Generator Tab"
7. Select "bot" from "Scopes", appropriate selections from "Bot Permissions" (Administrator may be overkill, but will get the job done)
8. Copy & Paste the generated URL at the bottom & select designated server - this is inviting the bot to the server


### Bot Setup in Server
1. Ensure you assign your bot a role within your server that is **higher** than the role you intend to assign to your list/file of users with the bot - meaning the bot's highest role should be greater than the role it is assigning - allowing for the bot to assign and edit roles of other users. This is important! You might need to make a new role or change permissions within the role in Discord to allow the bot to edit roles.

### Using this file
1. To get the server ID - aka guild id as referred to in the file - make sure you have Developer Mode turned on in Discord (Settings-->Advanced-->Developer Mode)
2. Find the designated server icon in the left side panel, right click and select 'Copy ID' from the tool tip. This should be inserted in line 20: ````guild = client.get_guild(ENTER SERVER ID HERE)````
3. Enter the role name you wish to assign to your list/file of users: ````role = discord.utils.get(guild.roles,name="ENTER ROLE NAME HERE")````
4. In order to connect the Bot you created in the first set of instructions - go back to https://discord.com/developers/applications, select your application and navigate to the "Bot" tab again
5. Under "Token", (just to be safe), hit "Regenerate" and "Copy" this token
6. Insert this token in line 41: ````client.run('PASTE TOKEN HERE')````

