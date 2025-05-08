import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7586448163:AAE3tvRZWR3YKE3yavYpleM5gntWx2T6xVE"
CHAT_ID = "@pixhojeoficial"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Seja bem-vindo ao PixHoje!\n\n"
        "Use o comando /pixhoje para acessar a oportunidade atual de renda."
    )

async def pixhoje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🚨 ATENÇÃO: OPORTUNIDADE DE PIX LIBERADA\n\n"
        "🧠 1 método validado por centenas de pessoas que já estão recebendo Pix direto no celular.\n\n"
        "📲 Resultado real, fácil e direto, sem enrolação.\n\n"
        "💸 Não é curso, não é promessa: é acesso a uma fórmula já usada por milhares.\n\n"
        "👉 Veja o que você precisa fazer agora:  \n"
        "🔗 https://pay.kiwify.com.br/sScCeS7?afid=p7XcYlIg\n\n"
        "⚠️ Liberado só para quem clicar até às 17h de hoje."
    )
    await context.bot.send_message(chat_id=CHAT_ID, text=mensagem)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pixhoje", pixhoje))

if __name__ == "__main__":
    app.run_polling()
