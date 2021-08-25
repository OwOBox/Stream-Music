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
import asyncio
from StreamMusic.config import SUDO_USERS
from StreamMusic.config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from StreamMusic.services.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Xin chào, đây là dịch vụ trợ lý âm nhạc .\n\n ❗️ Rules:\n   - Không được phép trò chuyện\n   - Không được phép gửi thư rác \n\n 👉 **GỬI LIÊN KẾT MỜI NHÓM HOẶC TÊN NGƯỜI DÙNG NẾU NGƯỜI DÙNG KHÔNG THỂ THAM GIA NHÓM CỦA BẠN.**\n\n ⚠️ Tuyên bố từ chối trách nhiệm: Nếu bạn đang gửi tin nhắn ở đây, điều đó có nghĩa là quản trị viên sẽ nhìn thấy tin nhắn của bạn và tham gia trò chuyện\n    - Không thêm người dùng này vào các nhóm bí mật.\n   - Không chia sẻ thông tin cá nhân ở đây\n\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Đã bật Pmpermit")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Đã tắt Pmpermit")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Được chấp thuận cho PM do các tin nhắn gửi đi")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Được chấp thuận cho PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Đã bị loại bỏ đối với PM")
        return
    message.continue_propagation()
