import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

TOKEN = "7586448163:AAE3tvRZWR3YKE3yavYpleM5gntWx2T6xVE"

logging.basicConfig(level=logging.INFO)

# Roteiro motivacional baseado em gatilhos emocionais
respostas = {
    "motivo_start": {
        "text": "Você já pensou em desistir de tudo, mas mesmo assim continua tentando?\nIsso já te torna mais forte do que imagina.\nQuer ver onde essa força pode te levar?",
        "buttons": [("Sim, me mostra", "motivo_mostra"), ("Tenho medo de me decepcionar de novo", "motivo_medo")]
    },
    "motivo_mostra": {
        "text": "O PixHoje é mais do que um método. É um lembrete de que você ainda tem controle.\nVocê vai aprender como transformar R$29 em liberdade usando só seu celular.",
        "buttons": [("Mas e se não funcionar?", "motivo_duvida"), ("Quero entrar", "motivo_quero")]
    },
    "motivo_medo": {
        "text": "O medo é só um sinal de que você tá saindo da zona de conforto.\nA zona onde nada muda.\nSe você chegou até aqui, não é por acaso.",
        "buttons": [("O que é esse método?", "motivo_mostra"), ("Quero arriscar", "motivo_quero")]
    },
    "motivo_duvida": {
        "text": "Nada na vida é garantia. Mas aqui você tem 7 dias pra testar.\nE se não gostar, seu dinheiro volta. Simples assim.",
        "buttons": [("Ok, quero tentar", "motivo_quero"), ("Isso faz sentido", "motivo_mostra")]
    },
    "motivo_quero": {
        "text": "Se você sentiu algo lendo isso, siga seu instinto.\n👉 https://bit.ly/pixhojevip\nA mudança começa quando a coragem fala mais alto. 💥",
        "buttons": []
    }
}

# Início do fluxo motivacional com /motivar
async def motivacional(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = respostas["motivo_start"]
    keyboard = [[InlineKeyboardButton(text, callback_data=callback)] for text, callback in data["buttons"]]
    await update.message.reply_text(data["text"], reply_markup=InlineKeyboardMarkup(keyboard))

# Controle da navegação por botões
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data
    data = respostas.get(key, respostas["motivo_start"])
    keyboard = [[InlineKeyboardButton(text, callback_data=callback)] for text, callback in data["buttons"]]
    await query.message.reply_text(data["text"], reply_markup=InlineKeyboardMarkup(keyboard) if keyboard else None)

# Configuração do bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("motivar", motivacional))
app.add_handler(CallbackQueryHandler(button))

if __name__ == "__main__":
    app.run_polling()
