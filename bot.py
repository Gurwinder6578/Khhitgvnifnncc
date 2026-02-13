import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pyrogram import Client, filters
from pyrogram.enums import ParseMode

# ---------------- HEALTH CHECK (Stays the same) ----------------
class HealthCheck(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_server():
    # Force Port 8000
    port = 8000
    HTTPServer(("0.0.0.0", port), HealthCheck).serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# ---------------- BOT CONFIG ----------------
API_ID = 33846755
API_HASH = "6bdfa52e67bc011d04333a420134c90f"
BOT_TOKEN = "8525195990:AAGxzR4aNtfnQ0x1F4WvPJYy-pETh3upelg"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ---------------- CAPTION (MARKDOWN V2 STYLE) ----------------
# We use ">" for the Blue Quote Box
# We use "*" for Bold
# We use "||" for Spoilers (Optional, removed here for simplicity)
CAPTION = (
    "*ANIME ROLL*\n\n"
    ">✈ POWERED BY : @Dub\\_Anime\\_ZZ       ❞\n\n"
    ">➲ JOIN HERE  : @ABANIMEOFFICIAL   ❞"
)

# ---------------- BOT LOGIC ----------------

@app.on_message(filters.video | filters.document)
async def add_caption(client, message):
    try:
        if message.chat.type.name == "CHANNEL":
            await message.edit_caption(
                caption=CAPTION,
                parse_mode=ParseMode.MARKDOWN  # <--- Changed to MARKDOWN
            )
        
        elif message.chat.type.name == "PRIVATE":
            await message.copy(
                chat_id=message.chat.id,
                caption=CAPTION,
                parse_mode=ParseMode.MARKDOWN  # <--- Changed to MARKDOWN
            )
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Bot Started...")
    app.run()
    
