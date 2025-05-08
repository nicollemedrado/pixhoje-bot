import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7586448163:AAE3tvRZWR3YKE3yavYpleM5gntWx2T6xVE"
CHAT_ID = "@pixhojeoficial"

logging.basicConfig(level=logging.INFO)

etapas_conversa = {
    0: "Olá! Seja muito bem-vindo(a) ao PixHoje 💬\nVocê caiu aqui por acaso ou tá buscando uma virada de chave na vida?",
    1: "Perfeito, essa curiosidade já é o primeiro passo.\nO PixHoje não é curso, nem promessa mágica. É um método simples que mostra como fazer R$75 a R$250 direto no Pix com o celular.\nVocê se sente preso(a) na rotina às vezes?",
    2: "Eu te entendo. Sabe o que é mais louco? Quem mais se transforma com esse método são justamente os que entram com medo.\nO medo mostra que você se importa. E quem aplica, vê acontecer.",
    3: "Sei o que você tá pensando: 'E se for só mais um link qualquer?'\nMas é por isso que eu tô conversando com você. Porque aqui, a venda é a última parte. Primeiro vem o propósito.",
    4: "E sim: você tem 7 dias de garantia. Não curtiu? Pede o estorno e o valor volta. Mas vou te dizer: menos de 1% pede. E sabe o motivo? Quem aplica, colhe. Simples assim.",
    5: "Você não deve se interessar só pelo Pix. Mas porque você já tentou tanto e ainda não recebeu o que merece.\nEsse método é pequeno no valor, mas grande na transformação — se você fizer com propósito.",
    6: "Agora sim... você está pronto(a).\n👉 https://bit.ly/pixhojevip\nDepois que acessar, volta aqui e me diz 'entrei'. Quero acompanhar de perto. 💸"
}

interacoes = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    interacoes[user_id] = 0
    await update.message.reply_text(etapas_conversa[0])

async def conversa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in interacoes:
        interacoes[user_id] = 0

    etapa = interacoes[user_id]
    resposta = etapas_conversa.get(etapa, etapas_conversa[6])
    await update.message.reply_text(resposta)

    if etapa < 6:
        interacoes[user_id] += 1
    else:
        interacoes[user_id] = 0

iscas = [
    "⚡️ Hoje já foram 3 Pix de R$100 pra quem aplicou o método. Você pode ser o próximo(a). Manda 'quero' pra saber como.",
    "🚨 Método atualizado liberado: sem vender, sem seguidores, só usando o celular e foco. Digita 'como funciona'.",
    "👀 Já viu alguém receber Pix e pensou: 'por que não eu?' — talvez essa seja sua chance. Pergunta aqui."
]

async def isca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(iscas)
    await context.bot.send_message(chat_id=CHAT_ID, text=msg)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("isca", isca))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), conversa))

if __name__ == "__main__":
    app.run_polling()
