from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler


buttons = ReplyKeyboardMarkup([["🇺🇿 O'zbek", '🇷🇺 Русский']], resize_keyboard=True)
service_button = ReplyKeyboardMarkup([["Kochmas mulk", 'avto servis']], resize_keyboard=True)

#service_button = ReplyKeyboardMarkup([['Tanirofka'], ['Shumka', 'Elektrik'], ['Moy almashtirish']])

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_html('<b>Assalom alekum, {}</b>\n \n Bizning xizmatlarimizga xush kelibsiz biz da tamirlash va kochmas mulk xizmatlari mavjud'.format(update.message.from_user.first_name), reply_markup=buttons)
    return 1

def uzb(update, context):
    # update.message.reply_text(
    #     'ozbek tili🇺🇿', #reply_markup=buttons,
    #     #reply_markup=ReplyKeyboardRemove(),
    # )
     
    # keyboard = [
    #     [
    #         InlineKeyboardButton("Kochmas mulk", callback_data='4'),
    #         InlineKeyboardButton("avto servis", callback_data='6')
    #     ]
    # ]
    # update.message.reply_text('Bizning xizmatlarimiz', reply_markup = InlineKeyboardMarkup(keyboard))
    
    update.message.reply_text('Qaysi xizmatimizdan foydalanmoqchisiz',
                              reply_markup=service_button)
    
    return 2  



def rus(update, context):
    update.message.reply_text(
        'Русский язык🇷🇺', #reply_markup=buttons 
        reply_markup=ReplyKeyboardRemove()
    )


def avtoservice(update, context):
    query = update.callback_query
    query.message.delete()
    query.message.reply_html('avto service', reply_markup = InlineKeyboardMarkup(service_button))
    service_button = [
        [
            InlineKeyboardButton("Kochmas mulk", callback_data='4'),
            InlineKeyboardButton("avto servis", callback_data='6')
        ]
    ]


def main():
    updater = Updater('911583993:AAHDt-JO2mqItxJzseiIyddRsynOwPAPT30', use_context=True)

    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1:[
            MessageHandler(Filters.regex("^(🇺🇿 O'zbek)$"), uzb), 
            MessageHandler(Filters.regex('^(🇷🇺 Русский)$'), rus)
           ],
        2:[
            MessageHandler(Filters.regex("^(Kochmas mulk)$"), uzb), 
            MessageHandler(Filters.regex('^(avto servis$'), rus)
          ]
    },
    fallbacks=[MessageHandler(Filters.text, start)]
    )
    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CallbackQueryHandler(avtoservice))
    updater.start_polling()
    updater.idle()
    
if __name__ == 'main':
    main()