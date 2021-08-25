# StreamMusic (Telegram bot project )
# Copyright (C) 2021  Sadew Jayasekara

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from StreamMusic.helpers.decorators import authorized_users_only
from StreamMusic.helpers.decorators import errors
from StreamMusic.services.callsmusic import client as USER
from StreamMusic.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>rước tiên, hãy thêm tôi làm quản trị viên của nhóm bạn</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "owomusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Tôi đã tham gia ở đây như bạn yêu cầu")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>người trợ giúp đã có trong cuộc trò chuyện của bạn</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 XẢY RA LỖI 🛑 \n User {user.first_name} không thể tham gia kênh của bạn có thể do đầy bộ nhớ! Đảm bảo rằng người dùng không bị cấm trong kênh."
            "\nnHoặc thêm thủ công @owomusic vào Nhóm của bạn và thử lại</b>",
        )
        return
    await message.reply_text(
        "<b>người trợ giúp người dùng đã tham gia cuộc trò chuyện của bạn</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Người dùng không thể rời khỏi nhóm của bạn! Có thể là lũ lụt."
            "\n\nHoặc kick tôi ra khỏi Nhóm của bạn theo cách thủ công</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Trợ lý Rời khỏi tất cả các cuộc trò chuyện")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Trợ lý rời đi ... Đã rời {left} nhóm. Failed: {failed} nhóm.")
            except:
                failed=failed+1
                await lol.edit(f"Trợ lý rời đi ... Đã rời {left} nhóm. Failed: {failed} nhóm.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Đã rời {left} nhóm. Failed {failed} nhóm.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Nhóm thậm chí còn chưa được liên kết")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Trước tiên hãy thêm tôi làm quản trị viên kênh của bạn</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "owomusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Tôi đã tham gia ở đây như bạn yêu cầu")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Người trợ giúp đã có trong kênh của bạn</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 XẢY RA LỖI 🛑 \n User {user.first_name} không thể tham gia kênh của bạn có thể do đầy bộ nhớ! Đảm bảo rằng người dùng không bị cấm trong kênh."
            "\nnHoặc thêm thủ công @owomusic vào Nhóm của bạn và thử lại</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your channel</b>",
    )
    
