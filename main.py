import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7586448163:AAE3tvRZWR3YKE3yavYpleM5gntWx2T6xVE"
CHAT_ID = "@pixhojeoficial"

logging.basicConfig(level=logging.INFO)

# Mensagens definidas
mensagem_publica = """
🚨 OPORTUNIDADE DE PIX LIBERADA

📢 Isso aqui não é curso, é acesso direto a um método validado por centenas de pessoas que já estão recebendo Pix.

💡 Você só precisa de 1 celular e ação.

🔗 Acesse agora: https://bit.ly/pixhojevip  
⚠️ Só até às 17h. Depois sai do ar.
"""

mensagem_privada = """
👀 Vejo que você está interessada em mudar de vida.

🎯 Se você está cansada de depender dos outros e quer fazer dinheiro com o que tem (seu celular), isso é pra você.

💸 O método do Pix está funcionando pra todo mundo que aplica com seriedade.

✅ Não é mágica. É execução. E você vai ter acesso a tudo por R$29.

👉 Liberado agora: https://bit.ly/pixhojevip  
"""

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Seja bem-vindo ao PixHoje! Aqui é onde começa sua virada financeira. Digite /pixhoje para ver a oportunidade de hoje.")

# Comando /pixhoje
async def pixhoje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text=mensagem_publica)
    await update.message.reply_text(mensagem_privada)

# Detecta palavras comuns e responde automaticamente
async def responder_automatico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    palavras_chave = ["oi", "ola", "olá", "bom dia", "boa tarde", "boa noite", "tudo bem", "e aí", "fala", "pix", "como", "ganhar", "quero", "funciona"]

    if any(p in texto for p in palavras_chave):
        await context.bot.send_message(chat_id=CHAT_ID, text=mensagem_publica)
        await update.message.reply_text(mensagem_privada)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pixhoje", pixhoje))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), responder_automatico))

if __name__ == "__main__":
    app.run_polling()
