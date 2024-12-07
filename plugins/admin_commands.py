from telegram import Update
from telegram.ext import CallbackContext
import sqlite3

admin_id = 123456789  # Replace with your admin user ID

def save_channel_to_db(new_channel: str):
    """
    Save or update the subscription channel in the database.
    """
    try:
        conn = sqlite3.connect("bot_database.db")
        cursor = conn.cursor()
        cursor.execute("REPLACE INTO force_subscriptions (id, channel_username) VALUES (1, ?)", (new_channel,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error saving channel to DB: {e}")
        return False

def set_subscription_channel(update: Update, context: CallbackContext):
    # Check if the user is the admin
    if update.effective_user.id != admin_id:
        update.message.reply_text("You are not authorized to use this command.")
        return

    # Ensure the command has one argument (channel username)
    if len(context.args) != 1:
        update.message.reply_text("Usage: /setchannel <channel_username>")
        return

    new_channel = context.args[0]

    if save_channel_to_db(new_channel):
        update.message.reply_text(f"Subscription channel updated to: {new_channel}")
    else:
        update.message.reply_text("Failed to update the subscription channel.")
