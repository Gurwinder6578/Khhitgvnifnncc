from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

# --- CONFIGURATION ---
API_ID = 33846755
API_HASH = "6bdfa52e67bc011d04333a420134c90f"
BOT_TOKEN = "8525195990:AAGxzR4aNtfnQ0x1F4WvPJYy-pETh3upelg"

app = Client("anime_roll_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- CAPTION TEMPLATE ---
# The <blockquote> tag creates the blue vertical line (quote style)
# ✈ and ➲ are decorative symbols to match your style
CAPTION_TEXT = (
    "<b>ANIME ROLL</b>\n\n"
    "<blockquote>✈ POWERED BY : @Dub_Anime_ZZ       ❞</blockquote>\n\n"
    "<blockquote>➲ JOIN HERE  : @ABANIMEOFFICIAL   ❞</blockquote>"
)

@app.on_message((filters.private | filters.channel) & (filters.video | filters.document))
async def auto_caption(client, message: Message):
    # Security check: Don't reply to our own messages to avoid infinite loops
    if message.from_user and message.from_user.is_self:
        return
        
    # If the file is generic media, ensure it has video attributes or treat as file
    caption = CAPTION_TEXT
    
    try:
        # We use copy() to "forward again" with a brand new caption
        await message.copy(
            chat_id=message.chat.id,
            caption=caption,
            parse_mode=ParseMode.HTML
        )
    except Exception as e:
        print(f"Error copying message: {e}")

if __name__ == "__main__":
    print("Bot Started...")
    app.run()
