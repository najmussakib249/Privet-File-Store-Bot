from pyrogram import filters
from pyrogram.types import Message
from pymongo import MongoClient
from config import MONGO_URL, ADMIN_ID, FORCE_SUB_CHANNEL

db = MongoClient(MONGO_URL)["FileStore"]
files = db.files

def register_handlers(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start(_, m: Message):
        await m.reply_text("Welcome to File Store Bot!")

    @app.on_message(filters.document | filters.video | filters.audio)
    async def save_file(_, m: Message):
        file_id = m.document.file_id if m.document else m.video.file_id if m.video else m.audio.file_id
        file_name = m.document.file_name if m.document else m.video.file_name if m.video else m.audio.file_name
        msg = await m.reply("Saving...")
        files.insert_one({"file_id": file_id, "file_name": file_name})
        await msg.edit(f"✅ Saved as: `{file_name}`")

    @app.on_message(filters.command("genlink") & filters.private)
    async def gen_link(_, m: Message):
        all_files = files.find()
        reply = ""
        for f in all_files:
            reply += f"• `{f['file_name']}` → `/get_{f['file_id']}`\n"
        await m.reply_text(reply or "No files yet.")

    @app.on_message(filters.command("batch"))
    async def batch(_, m: Message):
        await m.reply("📦 Batch feature coming soon!")

    @app.on_message(filters.command("custombatch"))
    async def custom_batch(_, m: Message):
        await m.reply("📦 Custom Batch feature coming soon!")

    @app.on_message(filters.command("autodelete"))
    async def auto_delete(_, m: Message):
        await m.reply("🗑 Auto delete feature coming soon!")

    @app.on_message(filters.command("mode"))
    async def mode(_, m: Message):
        await m.reply("⚙️ Current mode: Public")

    @app.on_message(filters.command("forcesub"))
    async def forcesub(_, m: Message):
        await m.reply(f"Join @{FORCE_SUB_CHANNEL} to use this bot.")
