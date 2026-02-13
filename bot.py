import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pyrogram import Client, filters
from pyrogram.enums import ParseMode

# ---------------- HEALTH CHECK (Your Working Version) ----------------
class HealthCheck(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_server():
    # Uses the port Koyeb assigns, or 8000 if testing locally
    port = int(os.environ.get("PORT", 8000))
    HTTPServer(("0.0.0.0", port), HealthCheck).serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# ---------------- BOT CONFIG ----------------
API_ID = 33846755
API_HASH = "6bdfa52e67bc011d04333a420134c90f"
BOT_TOKEN = "8525195990:AAGxzR4aNtfnQ0x1F4WvPJYy-pETh3upelg"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ---------------- CAPTION (HTML STYLE) ----------------
# <b> = Bold
# <blockquote> = The Blue Quote Line
CAPTION = (
    "<b>ANIME ROLL</b>\n\n"
    "<blockquote>✈ POWERED BY : @Dub_Anime_ZZ       ❞</blockquote>\n\n"
    "<blockquote>➲ JOIN HERE  : @ABANIMEOFFICIAL   ❞</blockquote>"
)

# ---------------- BOT LOGIC ----------------

@app.on_message(filters.video | filters.document)
async def add_caption(client, message):
    try:
        # If in a Channel (Admin), EDIT the caption
        if message.chat.type.name == "CHANNEL":
            await message.edit_caption(
                caption=CAPTION,
                parse_mode=ParseMode.HTML  # <--- MUST BE HTML
            )
        
        # If in Private (Forwarding), COPY it back
        elif message.chat.type.name == "PRIVATE":
            await message.copy(
                chat_id=message.chat.id,
                caption=CAPTION,
                parse_mode=ParseMode.HTML  # <--- MUST BE HTML
            )
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("Bot Started...")
    app.run()
    
