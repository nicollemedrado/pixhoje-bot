import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7586448163:AAE3tvRZWR3YKE3yavYpleM5gntWx2T6xVE"
CHAT_ID = "@pixhojeoficial"

logging.basicConfig(level=logging.INFO)

# Respostas para conversa 1:1 (privado)
respostas_saudacao = [
    "Oi linda! 👋 Tô aqui justamente pra te mostrar um jeito diferente de ganhar dinheiro com o que você já tem: seu celular.",
    "Bom dia! Já viu a galera recebendo Pix hoje cedo só por aplicar um método simples? Quer saber como?",
    "Seja bem-vinda! Você já ouviu falar no método que tá fazendo gente comum receber Pix todo dia?"
]

respostas_duvida = [
    "A pergunta é comum, mas te entendo. Olha o que a Giovanna Lima me mandou ontem após aplicar o método: recebeu R$100 no segundo dia!",
    "Funciona sim! Evelyn Silva aplicou e me mandou print de um Pix de R$250. O segredo é começar.",
    "A dúvida é normal, mas quem aplica de verdade, colhe. Caroline Santos começou na dúvida e hoje já bateu R$75 por dia."
]

respostas_acao = [
    "Perfeito. Mas vai com foco. 👉 https://bit.ly/pixhojevip\nDepois que acessar, volta aqui e me conta que eu te ajudo no passo 1.",
    "Aqui está o acesso que tá mudando vidas: https://bit.ly/pixhojevip\nComeça hoje e me chama se precisar de ajuda.",
    "Não perde tempo. Esse é o método: https://bit.ly/pixhojevip\nVocê só precisa aplicar e me contar o resultado depois."
]

respostas_neutra = [
    "Você não caiu aqui por acaso... posso te mostrar um caminho real de renda. Me manda uma dúvida e te explico.",
    "Tô aqui pra te mostrar como fazer Pix ainda hoje usando só seu celular. Me pergunta o que quiser.",
    "Se estiver com curiosidade, é só perguntar. Gosto de conversar com quem realmente quer mudar de vida."
]

# Mensagens públicas (iscas) sob comando
iscas_publicas = [
    "⚡️ Resultado de hoje: 3 Pix de R$100 recebidos com esse método simples. Não é curso, nem venda — é aplicação. Digite 'quero' no privado.",
    "👩‍🦰 “Fiz R$164 na minha primeira semana!” – Mensagem enviada por uma das seguidoras. Será que é você a próxima? 😏",
    "Hoje liberamos 20 acessos do método Pix. Ainda restam 3. Quem quiser entrar, me chama no privado com 'Pix'.",
    "🚨 ATENÇÃO: método atualizado liberado para quem quer fazer R$75 a R$250 no Pix sem vender nada. Use seu celular e foco. Digite /pixhoje."
]

# Detectar intenção
def detectar_intencao(texto):
    texto = texto.lower()
    if any(p in texto for p in ["oi", "ola", "olá", "bom dia", "boa tarde", "boa noite"]):
        return "saudacao"
    elif any(p in texto for p in ["funciona", "verdade", "real", "mentira", "confio"]):
        return "duvida"
    elif any(p in texto for p in ["quero", "link", "acesso", "comprar", "me manda", "como", "pix"]):
        return "acao"
    else:
        return "neutra"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Seja bem-vinda ao PixHoje!\nMe diga uma dúvida ou o que você busca, e eu te respondo como uma amiga que já descobriu o caminho. :)"
    )

# Resposta 1:1 automática
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

# Comando /isca para postar publicamente no canal
async def isca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = random.choice(iscas_publicas)
    await context.bot.send_message(chat_id=CHAT_ID, text=mensagem)

# Setup do bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("isca", isca))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), responder))

if __name__ == "__main__":
    app.run_polling()
