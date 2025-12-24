from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "8540235886:AAGLHesJ7YFiN_Wyx-hlOB_YFRoMsGW6axs"
ADMIN_CHAT_ID = 239467720  # آیدی خودت

def user_message(update, context):
    user = update.message.from_user
    text = update.message.text

    msg = f"""
پیام جدید 📩

👤 نام: {user.first_name}
🆔 یوزرنیم: @{user.username}
🆔 آیدی: {user.id}

💬 پیام:
{text}
"""
    context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)

def admin_reply(update, context):
    if update.message.reply_to_message:
        replied = update.message.reply_to_message.text
        for line in replied.split("\n"):
            if "🆔 آیدی:" in line:
                user_id = int(line.split(":")[1].strip())
                context.bot.send_message(
                    chat_id=user_id,
                    text=update.message.text
                )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, user_message))
dp.add_handler(MessageHandler(Filters.text & Filters.reply, admin_reply))

updater.start_polling()
updater.idle()

