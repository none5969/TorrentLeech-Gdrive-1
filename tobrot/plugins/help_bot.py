#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

async def help_bot_message(client, message):
    await message.reply_text("""Available Commands : \n\n /help: to print this help \n\n /mirror: Reply To Message Link If You Want To Mirror Link Into Gdrive \n\n /ytdl: Reply To Message Link If You Want To Download YT Video To Upload To Telegram \n\n /mirrorup: Reply To Message Link If You Want To Mirror Link And Upload To This Group\n\n /tmirror: Reply To Any File If You Want To Mirror From Telegram And Upload To Gdrive \n\n /stats: Show Stats of the machine the bot is hosted on \n\n Add-ons: *archive | *unzip | *unrar | *untar""")



