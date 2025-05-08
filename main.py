import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

TOKEN = "7586448163:AAE3tvRZWR3YKE3yavYpleM5gntWx2T6xVE"

logging.basicConfig(level=logging.INFO)

# Respostas personalizadas
respostas_saudacao = [
    "Oi! 👋 Seja bem-vinda. Já sabe da oportunidade Pix de hoje?",
    "Olá! Pronta para começar sua renda pelo celular ainda hoje?",
    "Bem-vinda! Quer saber como outras pessoas estão recebendo Pix agora?"
]

respostas_duvida = [
    "Sim, é real! Esse método já ajudou centenas de pessoas a fazerem seus primeiros R$100 pelo Pix.",
    "Funciona sim! Não é mágica, é estratégia testada e validada por muita gente.",
    "Muita gente me pergunta isso. A resposta é simples: quem aplica, recebe. 😉"
]

respostas_acao = [
    "Perfeito! Acesse agora o método liberado e siga os passos: https://bit.ly/pixhojevip",
    "Você está no ponto certo pra começar. Aqui está o link: https://bit.ly/pixhojevip",
    "Clique aqui e comece hoje mesmo sua virada financeira: https://bit.ly/pixhojevip"
]

respostas_neutra = [
    "Estou aqui pra te mostrar como fazer Pix ainda hoje usando só seu celular.",
    "Você não caiu aqui por acaso... posso te mostrar um caminho real de renda.",
    "Se estiver com dúvidas ou curiosidade, me chama com uma pergunta. Estou aqui pra te ajudar!"
]

# Detectar intenção da mensagem
def detectar_intencao(texto):
    texto = texto.lower()
    if any(p in texto for p in ["oi", "ola", "olá", "bom dia", "boa tarde", "boa noite"]):
        return "saudacao"
    elif any(p in texto for p in ["funciona", "verdade", "real", "mentira", "confio"]):
        return "duvida"
    elif any(p in texto for p in ["quero", "link", "acesso", "comprar", "me manda"]):
        return "acao"
    else:
        return "neutra"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Seja bem-vinda ao PixHoje! Me diga uma dúvida ou o que você busca, e eu te respondo como uma amiga que já descobriu o caminho. :)")

# Resposta inteligente no privado
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intencao = detectar_intencao(update.message.text)
    if intencao == "saudacao":
        resposta = random.choice(respostas_saudacao)
    elif intencao == "duvida":
        resposta = random.choice(respostas_duvida)
    elif intencao == "acao":
        resposta = random.choice(respostas_acao)
    else:
        resposta = random.choice(respostas_neutra)

    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), responder))

if __name__ == "__main__":
    app.run_polling()
