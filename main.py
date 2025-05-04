from telegram.ext import Application, MessageHandler, filters, ConversationHandler, CommandHandler
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
import logging
from data import db_session
from data.help_table import HelpTable


BOT_TOKEN = ''
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

keyboard1 = [['/right'],
             ['/left'],
             ['/stop']]
markup = ReplyKeyboardMarkup(keyboard1, one_time_keyboard=True)

keyboard2 = [['/enter_the_cafeteria'],
             ['/up'],
             ['/back'],
             ['/stop']]
markup2 = ReplyKeyboardMarkup(keyboard2, one_time_keyboard=True)

keyboard3 = [['/right'],
             ['/up'],
             ['/back'],
             ['/stop']]
markup3 = ReplyKeyboardMarkup(keyboard3, one_time_keyboard=True)

keyboard4 = [['/back'],
             ['/stop']]
markup4 = ReplyKeyboardMarkup(keyboard4, one_time_keyboard=True)

remove_markup = ReplyKeyboardRemove()

keyboard5 = [['/forward'],
             ['/right'],
             ['/back'],
             ['/stop']]
markup5 = ReplyKeyboardMarkup(keyboard5, one_time_keyboard=True)

keyboard6 = [['/sit'],
             ['/back'],
             ['/stop']]
markup6 = ReplyKeyboardMarkup(keyboard6, one_time_keyboard=True)

keyboard7 = [['/take'],
             ['/dont_take'],
             ['/stop']]
markup7 = ReplyKeyboardMarkup(keyboard7, one_time_keyboard=True)

keyboard8 = [['/forward'],
             ['/back'],
             ['/stop']]
markup8 = ReplyKeyboardMarkup(keyboard8, one_time_keyboard=True)
keyboard9 = [['/left'],
             ['/back'],
             ['/stop']]
markup9 = ReplyKeyboardMarkup(keyboard9, one_time_keyboard=True)


async def enter_the_cafeteria(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    if context.user_data['cur_stage'] == 3:
        if context.user_data['easter_egg1']:
            await update.message.reply_text('Ты зашел в столовую и не нашел ничего интересного', reply_markup=markup4)
        else:
            await update.message.reply_text('Ты зашел в столовую и нашел вилку! Взять её или нет?',
                                            reply_markup=markup7)
        context.user_data['cur_stage'] = 8
        return 8


async def back(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    elif context.user_data['cur_stage'] == 10:
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        context.user_data['cur_stage'] = 2
        return 2
    elif context.user_data['cur_stage'] == 4:
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        context.user_data['cur_stage'] = 2
        return 2
    elif context.user_data['cur_stage'] == 5:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        context.user_data['cur_stage'] = 4
        return 4
    elif context.user_data['cur_stage'] == 2:
        await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
        context.user_data['cur_stage'] = 1
        return 1
    elif context.user_data['cur_stage'] == 6:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        context.user_data['cur_stage'] = 4
        return 4
    elif context.user_data['cur_stage'] == 7:
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        context.user_data['cur_stage'] = 6
        return 6
    elif context.user_data['cur_stage'] == 3:
        await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
        context.user_data['cur_stage'] = 1
        return 1
    elif context.user_data['cur_stage'] == 8:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        context.user_data['cur_stage'] = 3
        return 3
    elif context.user_data['cur_stage'] == 9:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        context.user_data['cur_stage'] = 3
        return 3
    elif context.user_data['cur_stage'] == 21:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?',
                                        reply_markup=markup9)
        context.user_data['cur_stage'] = 9
        return 9
    elif context.user_data['cur_stage'] == 22:
        await update.message.reply_text('Ты нашел какой-то коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 21
        return 21
    elif context.user_data['cur_stage'] == 23:
        await update.message.reply_text('Ты идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 22
        return 22
    elif context.user_data['cur_stage'] == 24:
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 23
        return 23
    elif context.user_data['cur_stage'] == 25:
        await update.message.reply_text('Ты опять идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 24
        return 24
    elif context.user_data['cur_stage'] == 26:
        await update.message.reply_text('Ты снова идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 25
        return 25
    elif context.user_data['cur_stage'] == 27:
        await update.message.reply_text('Ты продолжаешь идти по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 26
        return 26
    elif context.user_data['cur_stage'] == 28:
        await update.message.reply_text('Ты не заканчиваешь идти по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 27
        return 27
    elif context.user_data['cur_stage'] == 29:
        await update.message.reply_text('Не может же этот коридор быть бесконечным. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 28
        return 28
    elif context.user_data['cur_stage'] == 30:
        await update.message.reply_text('Вдали виден конец коридора. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 29
        return 29
    elif context.user_data['cur_stage'] == 11:
        await update.message.reply_text('Ты пришел в длинный коридор. Пойти вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 5
        return 5
    elif context.user_data['cur_stage'] == 12:
        await update.message.reply_text('Ты прошел немного дальше по коридору и пока не видишь ничего интересного.'
                                        ' Пойти вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 11
        return 11
    elif context.user_data['cur_stage'] == 13:
        await update.message.reply_text('Ты прошел еще дальше. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 12
        return 12
    elif context.user_data['cur_stage'] == 14:
        await update.message.reply_text('Ты прошел подальше. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 13
        return 13
    elif context.user_data['cur_stage'] == 15:
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 14
        return 14
    elif context.user_data['cur_stage'] == 16:
        await update.message.reply_text('Это очень длинный коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 15
        return 15
    elif context.user_data['cur_stage'] == 17:
        await update.message.reply_text('Это оооооооочень длинный коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 16
        return 16
    elif context.user_data['cur_stage'] == 18:
        await update.message.reply_text('Конца коридора еще не видно. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 17
        return 17
    elif context.user_data['cur_stage'] == 19:
        await update.message.reply_text('Тебе не надоело? Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 18
        return 18
    elif context.user_data['cur_stage'] == 20:
        await update.message.reply_text('Опять вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 19
        return 19


async def forward(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    elif context.user_data['cur_stage'] == 4:
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        context.user_data['cur_stage'] = 6
        return 6
    elif context.user_data['cur_stage'] == 21:
        await update.message.reply_text('Ты идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 22
        return 22
    elif context.user_data['cur_stage'] == 22:
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 23
        return 23
    elif context.user_data['cur_stage'] == 23:
        await update.message.reply_text('Ты опять идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 24
        return 24
    elif context.user_data['cur_stage'] == 24:
        await update.message.reply_text('Ты снова идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 25
        return 25
    elif context.user_data['cur_stage'] == 25:
        await update.message.reply_text('Ты продолжаешь идти по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 26
        return 26
    elif context.user_data['cur_stage'] == 26:
        await update.message.reply_text('Ты не заканчиваешь идти по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 27
        return 27
    elif context.user_data['cur_stage'] == 27:
        await update.message.reply_text('Не может же этот коридор быть бесконечным. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 28
        return 28
    elif context.user_data['cur_stage'] == 28:
        await update.message.reply_text('Вдали виден конец коридора. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 29
        return 29
    elif context.user_data['cur_stage'] == 29:
        if context.user_data['easter_egg3']:
            await update.message.reply_text('Здесь нет ничего интересного', reply_markup=markup4)
            context.user_data['cur_stage'] = 30
            return 30
        else:
            context.user_data['easter_egg3'] = 1
            await update.message.reply_text('Ты нашел на полу ластик. И зачем он?')
            await update.message.reply_text('Ты вернулся к развилке')
            await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?',
                                            reply_markup=markup9)
            context.user_data['cur_stage'] = 9
            return 9
    elif context.user_data['cur_stage'] == 5:
        await update.message.reply_text('Ты прошел немного дальше по коридору и пока не видишь ничего интересного.'
                                        ' Пойти вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 11
        return 11
    elif context.user_data['cur_stage'] == 11:
        await update.message.reply_text('Ты прошел еще дальше. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 12
        return 12
    elif context.user_data['cur_stage'] == 12:
        await update.message.reply_text('Ты прошел подальше. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 13
        return 13
    elif context.user_data['cur_stage'] == 13:
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 14
        return 14
    elif context.user_data['cur_stage'] == 14:
        await update.message.reply_text('Это очень длинный коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 15
        return 15
    elif context.user_data['cur_stage'] == 15:
        await update.message.reply_text('Это оооооооочень длинный коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 16
        return 16
    elif context.user_data['cur_stage'] == 16:
        await update.message.reply_text('Конца коридора еще не видно. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 17
        return 17
    elif context.user_data['cur_stage'] == 17:
        await update.message.reply_text('Тебе не надоело? Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 18
        return 18
    elif context.user_data['cur_stage'] == 18:
        await update.message.reply_text('Опять вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 19
        return 19
    elif context.user_data['cur_stage'] == 19:
        if context.user_data['easter_egg2']:
            await update.message.reply_text('Ты уже был здесь. Ничего интересного не осталось', reply_markup=markup4)
            context.user_data['cur_stage'] = 20
            return 20
        else:
            context.user_data['easter_egg2'] = 1
            await update.message.reply_text('Все же это было не зря. Ты нашел линейку. Смешно, правда?')
            await update.message.reply_text('Ты вернулся к развилке.')
            await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
            context.user_data['cur_stage'] = 4
            return 4


async def sit(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    if context.user_data['cur_stage'] == 6:
        if context.user_data['key']:
            await update.message.reply_text('Ты зашел в актовый зал и сел на удобные сиденья', reply_markup=markup4)
        else:
            await update.message.reply_text('Ты зашел в актовый зал и между сидений нашел ключ. Взять его?',
                                            reply_markup=markup7)
        context.user_data['cur_stage'] = 7
        return 7


async def take(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    if context.user_data['cur_stage'] == 7:
        context.user_data['key'] = 1
        await update.message.reply_text('Ты подобрал ключ. Интересно, может он что-то откроет?',)
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        context.user_data['cur_stage'] = 6
        return 6
    if context.user_data['cur_stage'] == 8:
        context.user_data['easter_egg1'] = 1
        await update.message.reply_text('Ты взял вилку. Может и пригодится!')
        await update.message.reply_text(
            'Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?', reply_markup=markup2)
        context.user_data['cur_stage'] = 3
        return 3


async def dont_take(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    elif context.user_data['cur_stage'] == 7:
        await update.message.reply_text('Ты не взял ключ.')
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        context.user_data['cur_stage'] = 6
        return 6
    elif context.user_data['cur_stage'] == 8:
        await update.message.reply_text('Ты не подобрал вилку. Зачем она в пустой школе?')
        await update.message.reply_text(
            'Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?', reply_markup=markup2)
        context.user_data['cur_stage'] = 3
        return 3


async def up(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    elif context.user_data['cur_stage'] == 2:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        context.user_data['cur_stage'] = 4
        return 4
    elif context.user_data['cur_stage'] == 3:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?',
                                        reply_markup=markup9)
        context.user_data['cur_stage'] = 9
        return 9


async def right(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    elif context.user_data['cur_stage'] == 1:
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        context.user_data['cur_stage'] = 2
        return 2
    elif context.user_data['cur_stage'] == 4:
        await update.message.reply_text('Ты пришел в длинный коридор. Пойти вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 5
        return 5
    elif context.user_data['cur_stage'] == 2:
        if context.user_data['key']:
            await update.message.reply_text("Ты достал ключ и... открыл кабинет информатики!"
                                            " Ты зашел в кабинет и включил компьютер,"
                                            " вставил флешку и... включилось видео смешных котов?!"
                                            " Вдруг зазвенел будильник и ты проснулся!"
                                            " А нечего перед сном кушать, а то всякая чушь будет сниться!",
                                            reply_markup=remove_markup)
            score = (context.user_data["easter_egg1"] + context.user_data["easter_egg2"] +
                     context.user_data["easter_egg3"])
            if score == 3:
                await update.message.reply_text('Поздравляю! Вы прошли игру! Собранно предметов: 3/3.'
                                                ' Если хотите, можете сыграть снова!')
            else:
                await update.message.reply_text(f'Поздравляю! Вы прошли игру! Собранно предметов: {score}/3.'
                                                f' Рекомендуем поискать пасхалки!')
            return ConversationHandler.END
        else:
            await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт!'
                                            ' Ты этого не ожидал, надо искать ключ', reply_markup=markup4)
            context.user_data['cur_stage'] = 10
            return 10


async def left(update, context):
    if 'cur_stage' not in context.user_data or context.user_data['cur_stage'] == 0:
        return ConversationHandler.END
    elif context.user_data['cur_stage'] == 1:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        context.user_data['cur_stage'] = 3
        return 3
    elif context.user_data['cur_stage'] == 9:
        await update.message.reply_text('Ты нашёл какой-то коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 21
        return 21


async def start(update, context):
    await update.message.reply_text('При выходе из игры ваш прогресс не сохранится')
    await update.message.reply_text("Ты пробрался в свою школу с одним заданием: прокрасться в кабинет информатики!"
                                    " Ты зашел через главный вход,"
                                    " потому что твои напарники предварительно отвлекли охранника и выключили камеры.")
    await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
    context.user_data['key'] = 0
    context.user_data['cur_stage'] = 1
    context.user_data['easter_egg1'] = 0
    context.user_data['easter_egg2'] = 0
    context.user_data['easter_egg3'] = 0
    return 1


async def response_1(update, context):
    ans = update.message.text.lower()
    if ans not in ['направо', 'налево']:
        await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
        return 1
    elif ans == 'направо':
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        context.user_data['cur_stage'] = 2
        return 2
    await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                    reply_markup=markup2)
    context.user_data['cur_stage'] = 3
    return 3


async def response_2(update, context):
    ans = update.message.text.lower()
    if ans not in ['правее', 'подняться', 'обратно']:
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        return 2
    elif ans == 'правее':
        if context.user_data['key']:
            await update.message.reply_text("Ты достал ключ и... открыл кабинет информатики!"
                                            " Ты зашел в кабинет и включил компьютер,"
                                            " вставил флешку и... включилось видео смешных котов?!"
                                            " Вдруг зазвенел будильник и ты проснулся!"
                                            " А нечего перед сном кушать, а то всякая чушь будет сниться!",
                                            reply_markup=remove_markup)
            score = (context.user_data["easter_egg1"] + context.user_data["easter_egg2"] +
                     context.user_data["easter_egg3"])
            if score == 3:
                await update.message.reply_text('Поздравляю! Вы прошли игру! Собранно предметов: 3/3.'
                                                ' Если хотите, можете сыграть снова!')
            else:
                await update.message.reply_text(f'Поздравляю! Вы прошли игру! Собранно предметов: {score}/3.'
                                                f' Рекомендуем поискать пасхалки!')
            return ConversationHandler.END
        else:
            await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт! '
                                            'Ты этого не ожидал, надо искать ключ', reply_markup=markup4)
            context.user_data['cur_stage'] = 10
            return 10
    elif ans == 'подняться':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        context.user_data['cur_stage'] = 4
        return 4
    await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
    context.user_data['cur_stage'] = 1
    return 1


async def response_3(update, context):
    ans = update.message.text.lower()
    if ans not in ['подняться', 'зайти', 'обратно']:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        return 3
    elif ans == 'подняться':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?',
                                        reply_markup=markup9)
        context.user_data['cur_stage'] = 9
        return 9
    elif ans == 'зайти':
        if context.user_data['easter_egg1']:
            await update.message.reply_text('Ты зашел в столовую и не нашел ничего интересного', reply_markup=markup4)
        else:
            await update.message.reply_text('Ты зашел в столовую и нашел вилку! Взять её или нет?',
                                            reply_markup=markup7)
        context.user_data['cur_stage'] = 8
        return 8
    await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
    context.user_data['cur_stage'] = 1
    return 1


async def response_4(update, context):
    ans = update.message.text.lower()
    if ans not in ['направо', 'вперед', 'обратно']:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        context.user_data['cur_stage'] = 4
        return 4
    elif ans == 'направо':
        await update.message.reply_text('Ты пришел в длинный коридор. Пойти вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 5
        return 5
    elif ans == 'вперед':
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        context.user_data['cur_stage'] = 6
        return 6
    await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
    context.user_data['cur_stage'] = 2
    return 2


async def response_5(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты пришел в длинный коридор. Пойти вперед?', reply_markup=markup8)
        return 5
    if ans == 'обратно':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        context.user_data['cur_stage'] = 4
        return 4
    await update.message.reply_text('Ты прошел немного дальше по коридору и пока не видишь ничего интересного.'
                                    ' Пойти вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 11
    return 11


async def response_6(update, context):
    ans = update.message.text.lower()
    if ans not in ['посидеть', 'обратно']:
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        return 6
    elif ans == 'посидеть':
        if context.user_data['key']:
            await update.message.reply_text('Ты зашел в актовый зал и сел на удобные сиденья', reply_markup=markup4)
        else:
            await update.message.reply_text('Ты зашел в актовый зал и между сидений нашел ключ. Взять его?',
                                            reply_markup=markup7)
        context.user_data['cur_stage'] = 7
        return 7
    await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
    context.user_data['cur_stage'] = 4
    return 4


async def response_7(update, context):
    ans = update.message.text.lower()
    if context.user_data['key']:
        if ans != 'обратно':
            await update.message.reply_text('Ты зашел в актовый зал и сел на удобные сиденья', reply_markup=markup4)
            return 7
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        context.user_data['cur_stage'] = 6
        return 6
    else:
        if ans not in ['взять', 'нет']:
            await update.message.reply_text('Ты зашел в актовый зал и между сидений нашел ключ. Взять его?',
                                            reply_markup=markup7)
            return 7
        elif ans == 'взять':
            context.user_data['key'] = 1
            await update.message.reply_text('Ты подобрал ключ. Интересно, может он что-то откроет?')
        elif ans == 'нет':
            await update.message.reply_text('Ты не взял ключ.')
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        context.user_data['cur_stage'] = 6
        return 6


async def response_8(update, context):
    ans = update.message.text.lower()
    if context.user_data['easter_egg1']:
        if ans != 'обратно':
            await update.message.reply_text('Ты зашел в столовую и не нашел ничего интересного', reply_markup=markup4)
            return 8
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        context.user_data['cur_stage'] = 3
        return 3
    else:
        if ans not in ['взять', 'нет']:
            await update.message.reply_text('Ты зашел в столовую и нашел вилку! Взять её или нет?',
                                            reply_markup=markup7)
            return 8
        elif ans == 'взять':
            context.user_data['easter_egg1'] = 1
            await update.message.reply_text('Ты взял вилку. Может и пригодится!')
        elif ans == 'нет':
            await update.message.reply_text('Ты не подобрал вилку. Зачем она в пустой школе?')
        await update.message.reply_text(
            'Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?', reply_markup=markup2)
        context.user_data['cur_stage'] = 3
        return 3


async def response_9(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'налево']:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?',
                                        reply_markup=markup9)
        return 9
    elif ans == 'обратно':
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        context.user_data['cur_stage'] = 3
        return 3
    await update.message.reply_text('Ты нашел какой-то коридор. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 21
    return 21


async def response_10(update, context):
    ans = update.message.text.lower()
    if ans != 'обратно':
        await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт! '
                                        'Ты этого не ожидал, надо искать ключ', reply_markup=markup4)
        return 10
    await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
    context.user_data['cur_stage'] = 2
    return 2


async def response_11(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты прошел немного дальше по коридору и пока не видишь ничего интересного.'
                                        ' Пойти вперед?', reply_markup=markup8)
        return 11
    if ans == 'обратно':
        await update.message.reply_text('Ты пришел в длинный коридор. Пойти вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 5
        return 5
    await update.message.reply_text('Ты прошел еще дальше. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 12
    return 12


async def response_12(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты прошел еще дальше. Вперед?', reply_markup=markup8)
        return 12
    if ans == 'обратно':
        await update.message.reply_text('Ты прошел немного дальше по коридору и пока не видишь ничего интересного.'
                                        ' Пойти вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 11
        return 11
    await update.message.reply_text('Ты прошел подальше. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 13
    return 13


async def response_13(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты прошел подальше. Вперед?', reply_markup=markup8)
        return 13
    if ans == 'обратно':
        await update.message.reply_text('Ты прошел еще дальше. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 12
        return 12
    await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 14
    return 14


async def response_14(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
        return 14
    if ans == 'обратно':
        await update.message.reply_text('Ты прошел подальше. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 13
        return 13
    await update.message.reply_text('Это очень длинный коридор. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 15
    return 15


async def response_15(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Это очень длинный коридор. Вперед?', reply_markup=markup8)
        return 15
    if ans == 'обратно':
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 14
        return 14
    await update.message.reply_text('Это оооооооочень длинный коридор. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 16
    return 16


async def response_16(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Это оооооооочень длинный коридор. Вперед?', reply_markup=markup8)
        return 16
    if ans == 'обратно':
        await update.message.reply_text('Это очень длинный коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 15
        return 15
    await update.message.reply_text('Конца коридора еще не видно. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 17
    return 17


async def response_17(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Конца коридора еще не видно. Вперед?', reply_markup=markup8)
        return 17
    if ans == 'обратно':
        await update.message.reply_text('Это оооооооочень длинный коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 16
        return 16
    await update.message.reply_text('Тебе не надоело? Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 18
    return 18


async def response_18(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Тебе не надоело? Вперед?', reply_markup=markup8)
        return 18
    if ans == 'обратно':
        await update.message.reply_text('Конца коридора еще не видно. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 17
        return 17
    await update.message.reply_text('Опять вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 19
    return 19


async def response_19(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Опять вперед?', reply_markup=markup8)
        return 19
    if ans == 'обратно':
        await update.message.reply_text('Тебе не надоело? Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 18
        return 18
    if context.user_data['easter_egg2']:
        await update.message.reply_text('Ты уже был здесь. Ничего интересного не осталось', reply_markup=markup4)
        context.user_data['cur_stage'] = 20
        return 20
    else:
        context.user_data['easter_egg2'] = 1
        await update.message.reply_text('Все же это было не зря. Ты нашел линейку. Смешно, правда?')
        await update.message.reply_text('Ты вернулся к развилке.')
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        context.user_data['cur_stage'] = 4
        return 4


async def response_20(update, context):
    ans = update.message.text.lower()
    if ans != 'обратно':
        await update.message.reply_text('Ты уже был здесь. Ничего интересного не осталось', reply_markup=markup4)
        return 20
    await update.message.reply_text('Опять вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 19
    return 19


async def response_21(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты нашел какой-то коридор. Вперед?', reply_markup=markup8)
        return 21
    if ans == 'обратно':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?',
                                        reply_markup=markup9)
        context.user_data['cur_stage'] = 9
        return 9
    await update.message.reply_text('Ты идешь по коридору. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 22
    return 22


async def response_22(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты идешь по коридору. Вперед?', reply_markup=markup8)
        return 22
    if ans == 'обратно':
        await update.message.reply_text('Ты нашел какой-то коридор. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 21
        return 21
    await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 23
    return 23


async def response_23(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
        return 23
    if ans == 'обратно':
        await update.message.reply_text('Ты идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 22
        return 22
    await update.message.reply_text('Ты опять идешь по коридору. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 24
    return 24


async def response_24(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты опять идешь по коридору. Вперед?', reply_markup=markup8)
        return 24
    if ans == 'обратно':
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 23
        return 23
    await update.message.reply_text('Ты снова идешь по коридору. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 25
    return 25


async def response_25(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты снова идешь по коридору. Вперед?', reply_markup=markup8)
        return 25
    if ans == 'обратно':
        await update.message.reply_text('Ты опять идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 24
        return 24
    await update.message.reply_text('Ты продолжаешь идти по коридору. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 26
    return 26


async def response_26(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты продолжаешь идти по коридору. Вперед?', reply_markup=markup8)
        return 26
    if ans == 'обратно':
        await update.message.reply_text('Ты снова идешь по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 25
        return 25
    await update.message.reply_text('Ты не заканчиваешь идти по коридору. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 27
    return 27


async def response_27(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты не заканчиваешь идти по коридору. Вперед?', reply_markup=markup8)
        return 27
    if ans == 'обратно':
        await update.message.reply_text('Ты продолжаешь идти по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 26
        return 26
    await update.message.reply_text('Не может же этот коридор быть бесконечным. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 28
    return 28


async def response_28(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Не может же этот коридор быть бесконечным. Вперед?', reply_markup=markup8)
        return 28
    if ans == 'обратно':
        await update.message.reply_text('Ты не заканчиваешь идти по коридору. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 27
        return 27
    await update.message.reply_text('Вдали виден конец коридора. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 29
    return 29


async def response_29(update, context):
    ans = update.message.text.lower()
    if ans not in ['обратно', 'вперед']:
        await update.message.reply_text('Вдали виден конец коридора. Ввперед?', reply_markup=markup8)
        return 29
    if ans == 'обратно':
        await update.message.reply_text('Не может же этот коридор быть бесконечным. Вперед?', reply_markup=markup8)
        context.user_data['cur_stage'] = 28
        return 28
    if context.user_data['easter_egg3']:
        await update.message.reply_text('Здесь нет ничего интересного', reply_markup=markup4)
        context.user_data['cur_stage'] = 30
        return 30
    else:
        context.user_data['easter_egg3'] = 1
        await update.message.reply_text('Ты нашел на полу ластик. И зачем он?')
        await update.message.reply_text('Ты вернулся к развилке')
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?',
                                        reply_markup=markup9)
        context.user_data['cur_stage'] = 9
        return 9


async def response_30(update, context):
    ans = update.message.text.lower()
    if ans != 'обратно':
        await update.message.reply_text('Здесь нет ничего интересного', reply_markup=markup4)
        return 30
    await update.message.reply_text('Вдали виден конец коридора. Вперед?', reply_markup=markup8)
    context.user_data['cur_stage'] = 29
    return 29


async def stop(update, context):
    await update.message.reply_text("Возвращайтесь снова! (Ваш прогресс не сохранился)",
                                    reply_markup=ReplyKeyboardRemove())
    context.user_data['key'] = 0
    context.user_data['cur_stage'] = 0
    context.user_data['easter_egg1'] = 0
    context.user_data['easter_egg2'] = 0
    context.user_data['easter_egg3'] = 0
    return ConversationHandler.END


async def help_func(update, context):
    await update.message.reply_text(db_session.create_session().query(HelpTable).filter(HelpTable.id == 1)[0].text)


def main():
    db_session.global_init("db/bot_db.sqlite")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("help", help_func))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), CommandHandler('right', right), CommandHandler('left', left),
                      CommandHandler('back', back), CommandHandler('up', up), CommandHandler('forward', forward),
                      CommandHandler('take', take), CommandHandler('dont_take', dont_take), CommandHandler('sit', sit),
                      CommandHandler('enter_the_cafeteria', enter_the_cafeteria)],

        states={

            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_1)],

            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_2)],

            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_3)],

            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_4)],

            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_5)],

            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_6)],

            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_7)],

            8: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_8)],

            9: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_9)],

            10: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_10)],

            11: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_11)],

            12: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_12)],

            13: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_13)],

            14: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_14)],

            15: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_15)],

            16: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_16)],

            17: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_17)],

            18: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_18)],

            19: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_19)],

            20: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_20)],

            21: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_21)],

            22: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_22)],

            23: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_23)],

            24: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_24)],

            25: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_25)],

            26: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_26)],

            27: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_27)],

            28: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_28)],

            29: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_29)],

            30: [MessageHandler(filters.TEXT & ~filters.COMMAND, response_30)]

        },

        fallbacks=[CommandHandler('stop', stop), CommandHandler('right', right), CommandHandler('left', left),
                   CommandHandler('back', back), CommandHandler('up', up), CommandHandler('forward', forward),
                   CommandHandler('take', take), CommandHandler('dont_take', dont_take), CommandHandler('sit', sit),
                   CommandHandler('enter_the_cafeteria', enter_the_cafeteria)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
