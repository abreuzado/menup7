import telebot 
import firebase_admin 
from firebase_admin import credentials, firestore 

cred = credentials.Certificate("firebase.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

db = firestore.client()
bot = telebot.TeleBot('7144651940:AAGA_ejGvtKdeskJToWLZoToz3aXLXsyfdA')

link = 'https://www.akaili777.com/#/?akaili777_Code=GFNXJQ'

test = ''

# CPA
@bot.message_handler(commands=['cpa'])
def cpa(message):

    valor = 25
    deps = 10
    if test == '':
      codigo = 'GFNXJQ'
    else:
      codigo = test

    text = f'''
    CPA 🇨🇳
    
    👥️️ Depositantes: {deps}
    💰️ Valor: R$ {valor}.00
    🧾 Codigo: {codigo}


    (Após o pagamento, envie o comprovante para @prates777 e espere.))
    PIX: GUPRIX@GMAIL.COM 
    '''
  
    bot.send_message(message.chat.id, text, )
  
# CADASTRO
@bot.message_handler(commands=['cadastrar'])
def cadatrar(message):
   markup = telebot.types.InlineKeyboardMarkup()
   markup.add(telebot.types.InlineKeyboardButton("Concluído", callback_data="concluido"))
   bot.reply_to(message, text=f'''
   Faça o cadastro na plataforma chinesa abaixo 👇
   
   [Plataforma China]({link})''', parse_mode='Markdown', reply_markup=markup)

# CODIGO INDICAÇÃO 
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "concluido":
      bot.send_message(call.message.chat.id, text="Cadastro concluído!\n Digite o seu codigo de indicação")
    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        user_id = message.from_user.id
        codigo = message.text
        doc_ref = db.collection('users').document(str(user_id))
        doc_ref.set({
            'codigo': codigo
        })
        test = codigo
        bot.send_message(message.chat.id, text="Perfeito, continue no /cpa")
  
# START
@bot.message_handler(commands=['start'])
def start(message):
   bot.reply_to(message, text='''
   METODO CPA 🇨🇳
   
   Boa tarde, sou um robô e irei te ajudar a partir de agora! 
   Repita os passos abaixo:
   
   1. Use o comando "/cadastrar" e abra sua conta.
   
   2. Use o comando "/cpa" digite a quantidade de depositantes.
   
   3. faça o pagamento pelo QrCode ou Link.
   
   4. Aguarde o pagamento ser aprovado( espere a mensagem (pagamento concluído).
   
   5. Use o comando "/dashboard" para verificar seu Menu CPA.
   
   6. Seja feliz.''')
   
bot.polling(none_stop=True)  
