import env
from DiscordHooks import Hook, Embed, EmbedAuthor, Color
from datetime import datetime
import time

class Messages:
    def sendMessageAll(self, channel, message, description,  urltitle, url, color, author):

        embed = Embed(title=urltitle, url=url, description=description,
              timestamp=datetime.utcnow(), color=color, author=EmbedAuthor(name=author))

        Hook(hook_url=channel,
             username=env.Hook._BOTNAME,
             avatar_url=env.Hook._AVATAR,
             content=message,
             embeds=[embed]).execute()
        time.sleep(2)

    def sendSimple(self, channel, message):

        Hook(hook_url=channel,
             username=env.Hook._BOTNAME,
             avatar_url=env.Hook._AVATAR,
             content=message).execute()