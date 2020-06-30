#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

help_string = f'''
/help: To get this message

/mirror [download_url][magnet_link]: Start mirroring the link to google drive

/mirror unzip | unrar | untar [download_url][magnet_link] : starts mirroring and if downloaded file is any archive , extracts it to google drive

/mirror archive [download_url][magnet_link]: start mirroring and upload the archived (.tar) version of the download

/ytdl [youtube-dl supported link]:Reply To message Link To Mirror through youtube-dl 

/cancel (GID): Reply to the message by which the download was initiated and that download will be cancelled

/status: Shows a status of all the downloads

/stats: Show Stats of the machine the bot is hosted on

/ping: Test Ping 

'''

async def help_bot_message(client, message):
    await message.reply_text(help_string)


