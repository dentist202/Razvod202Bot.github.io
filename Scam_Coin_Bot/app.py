from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters
from credentials import BOT_TOKEN, BOT_USERNAME
import json

async def launch_web_ui(update: Update, callback: CallbackContext):
    # display our web-app!
    kb = [
        [KeyboardButton(
            "Show me my Web-App!",
           web_app=WebAppInfo("https://dentist202.github.io/Razvod202Bot.github.io/Scam_Coin_Bot/") # obviously, set yours here.
        )]
    ]
    await update.message.reply_text("Let's do this...", reply_markup=ReplyKeyboardMarkup(kb))


if __name__ == '__main__':

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', launch_web_ui))


    async def web_app_data(update: Update, context: CallbackContext):
        data = json.loads(update.message.web_app_data.data)
        await update.message.reply_text("Your data was:")
        for result in data:
            await update.message.reply_text(f"{result['name']}: {result['value']}")

    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))

    print(f"Your bot is listening! Navigate to http://t.me/{BOT_USERNAME} to interact with it!")
    application.run_polling()