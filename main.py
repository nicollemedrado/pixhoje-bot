import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7586448163:AAE3tvRZWR3YKE3yavYpleM5gntWx2T6xVE"
CHAT_ID = "@pixhojeoficial"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Seja bem-vindo ao PixHoje! Use o comando /pixhoje para receber a oportunidade do dia.")

async def pixhoje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """💸 OPORTUNIDADE PIX DO DIA

Esse método está sendo liberado para poucos usuários e pode fazer cair Pix ainda hoje.

📲 Acesse agora: https://pay.kiwify.com.br/sScCeS7?afid=p7XcYlIg

⚠️ Liberado somente até às 17h. Entre agora e veja como funciona."""
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pixhoje", pixhoje))

if __name__ == "__main__":
    app.run_polling()
