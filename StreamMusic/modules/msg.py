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

import os
from StreamMusic.config import SOURCE_CODE
from StreamMusic.config import ASSISTANT_NAME
from StreamMusic.config import PROJECT_NAME
from StreamMusic.config import SUPPORT_GROUP
from StreamMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 Tôi là một bot nâng cao được tạo ra để chơi nhạc trong các cuộc trò chuyện thoại của các Nhóm & Kênh Telegram.\n\n✅ Gửi cho tôi /help để biết thêm thông tin."
      HELP_MSG = [
        ".",
f"""
**Này 👋 Chào mừng bạn trở lại {PROJECT_NAME}

⚪️ {PROJECT_NAME} có thể phát nhạc trong cuộc trò chuyện thoại của nhóm bạn cũng như các cuộc trò chuyện thoại trên kênh

⚪️ Tên trợ lý >> @{ASSISTANT_NAME}\n\nNhấp vào tiếp theo để xem hướng dẫn**
""",

f"""
**Setting up**

1) Đặt bot làm quản trị viên (Nhóm và trong kênh nếu sử dụng cplay)
2) Bắt đầu trò chuyện thoại
3) Thử /play [tên bài hát] lần đầu tiên bởi quản trị viên
*) Nếu userbot tham gia, hãy thưởng thức âm nhạc, Nếu không hãy thêm @{ASSISTANT_NAME} vào nhóm của bạn và thử lại

**Đối với kênh phát nhạc**
1) Đặt tôi làm quản trị viên kênh của bạn
2) Gửi /userbotjoinchannel trong nhóm được liên kết
3) Bây giờ gửi lệnh trong nhóm được liên kết

**Commands**

**=>> Song Playing 🎧**

- /play: Phát bài hát được yêu cầu
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /ytplay: Phát trực tiếp bài hát qua Youtube Music

**=>> Playback ⏯**

- /player: Mở menu Cài đặt của trình phát
- /skip: Bỏ qua bản nhạc hiện tại
- /pause: Tạm dừng bản nhạc
- /resume: Tiếp tục bản nhạc đã tạm dừng
- /end: Dừng phát lại phương tiện
- /current: Hiển thị bản nhạc đang phát hiện tại
- /playlist: Hiển thị danh sách phát

*Người chơi cmd và tất cả các cmd khác ngoại trừ /play, /current  và /playlist  chỉ dành cho quản trị viên của nhóm.
""",
        
f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
- /userbotleaveall - remove assistant from all chats
"""
      ]
