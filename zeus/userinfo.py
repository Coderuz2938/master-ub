from telethon import events
import zeus.client
from telethon.tl.functions.users import GetFullUserRequest
from os import remove

client = zeus.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.userinfo'))
async def userinfo(event):
    await event.delete()
    try:
        getinformation = await event.get_reply_message()
        targetid = getinformation.sender_id
        targetdetails = await client(GetFullUserRequest(targetid))
        messagelocation = event.to_id
        client.parse_mode = "html"
        userimage = await client.download_profile_photo(f"@{targetdetails.users[0].username}")
        await client.send_file(messagelocation, userimage, caption=f"๐ค NickName: {targetdetails.users[0].first_name}\n๐ค Familyasi: {targetdetails.users[0].last_name}\n๐ Username: @{targetdetails.users[0].username}\n๐ User ID: {targetdetails.users[0].id}\nโ๏ธ Tel nomeri: {targetdetails.users[0].phone}\n๐ User Link: <a href='tg://user?id={targetid}'>Profile</a>\n๐ Bio: {targetdetails.full_user.about}\n๐ Data Center ID: {targetdetails.users[0].photo.dc_id}\n๐ค Bot: {targetdetails.users[0].bot}\n๐ฅ oสปzaro guruhlar: {targetdetails.full_user.common_chats_count}\n๐ซ Blocklangan: {targetdetails.full_user.blocked}\n\n")
        remove(userimage)
    except:
        pass