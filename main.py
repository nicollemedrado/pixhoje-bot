import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7586448163:AAE3tvRZWR3YKE3yavYpleM5gntWx2T6xVE"
CHAT_ID = "@pixhojeoficial"

logging.basicConfig(level=logging.INFO)

respostas_saudacao = [
    "Olá! Seja muito bem-vindo(a) ao PixHoje 👋\nVocê tá aqui por um motivo... quer saber o que vai mudar a sua vida hoje?",
    "Oi! Bem-vindo(a). Tô aqui pra te mostrar um caminho novo com o celular que você já tem nas mãos.",
    "Seja bem-vindo(a)! Já ouviu falar do método que tá fazendo Pix cair pra gente comum todos os dias?"
]

respostas_duvida = [
    "É normal desconfiar... mas sabe quem não recebeu Pix? Quem nunca tentou. 😉",
    "A dúvida é o que separa quem fica parado de quem muda de vida.",
    "Funciona sim! E eu só te mostro porque já vi acontecer com várias pessoas que começaram sem acreditar também."
]

respostas_interesse = [
    "Adoro quando alguém quer saber mais. Isso já mostra atitude.",
    "Quer saber mais? Só me promete que se eu te mostrar, você vai aplicar, combinado?",
    "Tá pronto(a) pra realmente fazer diferente dessa vez?"
]

mensagem_link = "Então agora sim... você está pronto(a).\n👉 https://bit.ly/pixhojevip\nDepois de acessar, me chama aqui com seu print, quero acompanhar de perto."

iscas_publicas = [
    "⚡️ Hoje já foram 3 Pix de R$100 pra quem aplicou o método. Você pode ser o próximo(a). Manda 'quero' pra saber como.",
    "🚨 Método atualizado liberado: sem vender, sem seguidores, só usando o celular e foco. Digita 'como funciona'.",
    "👀 Já viu alguém receber Pix e pensou: 'por que não eu?' — talvez essa seja sua chance. Pergunta aqui."
]

interacoes_usuario = {}

def detectar_intencao(texto):
    texto = texto.lower()
    if any(p in texto for p in ["oi", "ola", "olá", "bom dia", "boa tarde", "boa noite"]):
        return "saudacao"
    elif any(p in texto for p in ["funciona", "verdade", "real", "mentira", "confio"]):
        return "duvida"
    elif any(p in texto for p in ["quero", "link", "acesso", "comprar", "como", "pix"]):
        return "interesse"
    else:
        return "neutra"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Seja bem-vindo(a) ao PixHoje! Vamos conversar... me diz o que você está buscando aqui?")

async def isca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(iscas_publicas)
    await context.bot.send_message(chat_id=CHAT_ID, text=msg)

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    texto = update.message.text
    intencao = detectar_intencao(texto)

    if user_id not in interacoes_usuario:
        interacoes_usuario[user_id] = 0

    if intencao == "saudacao":
        resposta = random.choice(respostas_saudacao)
    elif intencao == "duvida":
        resposta = random.choice(respostas_duvida)
    elif intencao == "interesse":
        resposta = random.choice(respostas_interesse)
    else:
        resposta = "Me manda sua dúvida ou o que você gostaria de alcançar ainda esse mês. Tô aqui pra conversar com você."

    await update.message.reply_text(resposta)

    interacoes_usuario[user_id] += 1
    if interacoes_usuario[user_id] >= 3:
        await update.message.reply_text(mensagem_link)
        interacoes_usuario[user_id] = 0

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("isca", isca))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), responder))

if __name__ == "__main__":
    app.run_polling()
