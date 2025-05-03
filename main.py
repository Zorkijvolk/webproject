from telegram.ext import Application, MessageHandler, filters, ConversationHandler, CommandHandler
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
import logging

BOT_TOKEN = ''
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

keyboard1 = [['/right'],
             ['/left']]
markup = ReplyKeyboardMarkup(keyboard1, one_time_keyboard=True)

keyboard2 = [['/enter_the_cafeteria'],
             ['/up'],
             ['/back']]
markup2 = ReplyKeyboardMarkup(keyboard2, one_time_keyboard=True)

keyboard3 = [['/right'],
             ['/up'],
             ['/back']]
markup3 = ReplyKeyboardMarkup(keyboard3, one_time_keyboard=True)

keyboard4 = [['/back']]
markup4 = ReplyKeyboardMarkup(keyboard4, one_time_keyboard=True)

remove_markup = ReplyKeyboardRemove()

keyboard5 = [['/forward'],
             ['/right'],
             ['/back']]
markup5 = ReplyKeyboardMarkup(keyboard5, one_time_keyboard=True)

keyboard6 = [['/sit'],
             ['/back']]
markup6 = ReplyKeyboardMarkup(keyboard6, one_time_keyboard=True)

keyboard7 = [['/take'],
             ['/dont_take'],
             ['/back']]
markup7 = ReplyKeyboardMarkup(keyboard7, one_time_keyboard=True)

keyboard8 = [['/forward'],
             ['/back']]
markup8 = ReplyKeyboardMarkup(keyboard8, one_time_keyboard=True)
keyboard9 = [['/left'],
             ['/back']]
markup9 = ReplyKeyboardMarkup(keyboard9, one_time_keyboard=True)


async def enter_the_cafeteria(update, context):
    global cur_stage, easter_egg1
    if cur_stage == 3:
        if easter_egg1:
            await update.message.reply_text('Ты зашел в столовую и не нашел ничего интересного', reply_markup=markup4)
        else:
            await update.message.reply_text('Ты зашел в столовую и нашел вилку! Взять её или нет?',
                                            reply_markup=markup7)
        cur_stage = 8
        return 8


async def back(update, context):
    global cur_stage
    if cur_stage == 10:
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        cur_stage = 2
        return 2
    elif cur_stage == 4:
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        cur_stage = 2
        return 2
    elif cur_stage == 5:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        cur_stage = 4
        return 4
    elif cur_stage == 2:
        await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
        cur_stage = 1
        return 1
    elif cur_stage == 6:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        cur_stage = 4
        return 4
    elif cur_stage == 7:
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        cur_stage = 6
        return 6
    elif cur_stage == 3:
        await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
        cur_stage = 1
        return 1
    elif cur_stage == 8:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        cur_stage = 3
        return 3
    elif cur_stage == 9:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        cur_stage = 3
        return 3
    elif cur_stage == 21:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?')
        cur_stage = 9
        return 9
    elif cur_stage == 22:
        await update.message.reply_text('Ты нашёл какой-то коридор. Вперед?')
        cur_stage = 21
        return 21
    elif cur_stage == 23:
        cur_stage = 22
        return 22


async def forward(update, context):
    global cur_stage
    if cur_stage == 4:
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        cur_stage = 6
        return 6


async def sit(update, context):
    global cur_stage, key
    if cur_stage == 6:
        if key:
            await update.message.reply_text('Ты зашел в актовый зал и сел на удобные сиденья', reply_markup=markup4)
        else:
            await update.message.reply_text('Ты зашел в актовый зал и между сидений нашел ключ. Взять его?',
                                            reply_markup=markup7)
        cur_stage = 7
        return 7


async def take(update, context):
    global cur_stage, key, easter_egg1
    if cur_stage == 7:
        key = 1
        await update.message.reply_text('Ты подобрал ключ. Интересно, может он что-то откроет?', reply_markup=markup4)
    if cur_stage == 8:
        easter_egg1 = 1
        await update.message.reply_text('Ты взял вилку. Может и пригодится!', reply_markup=markup4)


async def dont_take(update, context):
    global cur_stage
    if cur_stage == 7:
        await update.message.reply_text('Ты не взял ключ.', reply_markup=markup4)
    elif cur_stage == 8:
        await update.message.reply_text('Ты не подобрал вилку. Зачем она в пустой школе?', reply_markup=markup4)


async def up(update, context):
    global cur_stage
    if cur_stage == 2:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        cur_stage = 4
        return 4
    elif cur_stage == 3:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно??',
                                        reply_markup=markup9)
        cur_stage = 9
        return 9


async def right(update, context):
    global cur_stage, key
    if cur_stage == 1:
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        cur_stage = 2
        return 2
    elif cur_stage == 4:
        await update.message.reply_text('Ты пришел к концу коридора, но ничего не нашел')
        cur_stage = 5
        return 5
    elif cur_stage == 2:
        if key:
            await update.message.reply_text("Ты достал ключ и... открыл кабинет информатики!"
                                            " Ты зашел в кабинет и включил компьютер,"
                                            " вставил флешку и... включилось видео смешных котов?!"
                                            " Вдруг зазвенел будильник и ты проснулся!"
                                            " А нечего перед сном кушать, а то всякая чушь будет сниться!",
                                            reply_markup=remove_markup)
            if easter_egg1 + easter_egg2 + easter_egg3 == 3:
                await update.message.reply_text('Поздравляю! Вы прошли игру! Собранно предметов: 3/3.'
                                                ' Если хотите, можете сыграть снова!')
            else:
                await update.message.reply_text(f'Поздравляю! Вы прошли игру! Собранно предметов:'
                                                f' {easter_egg1 + easter_egg2 + easter_egg3}/3.'
                                                ' Рекомендуем поискать пасхалки!')
            return ConversationHandler.END
        else:
            await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт! \
        Ты этого не ожидал, надо искать ключ', reply_markup=markup4)
            cur_stage = 10
            return 10


async def left(update, context):
    global cur_stage
    if cur_stage == 1:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                        reply_markup=markup2)
        cur_stage = 3
        return 3
    elif cur_stage == 9:
        await update.message.reply_text('Ты нашёл какой-то коридор. Вперед?', reply_markup=markup8)
        cur_stage = 21
        return 21


async def start(update, context):
    global cur_stage
    await update.message.reply_text("Ты пробрался в свою школу с одним заданием: прокрасться в кабинет информатики!"
                                    " Ты зашел через главный вход,"
                                    " потому что твои напарники предварительно отвлекли охранника и выключили камеры.")
    await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
    cur_stage = 1
    return 1


async def response_1(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['направо', 'налево']:
        await update.message.reply_text('У тебя выбор: пойти направо или налево?')
        return 1
    elif ans.lower() == 'направо':
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
        cur_stage = 2
        return 2
    await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?',
                                    reply_markup=markup2)
    cur_stage = 3
    return 3


async def response_2(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['правее', 'подняться', 'обратно']:
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?')
        return 2
    elif ans == 'правее':
        if key:
            await update.message.reply_text("Ты достал ключ и... открыл кабинет информатики!"
                                            " Ты зашел в кабинет и включил компьютер,"
                                            " вставил флешку и... включилось видео смешных котов?!"
                                            " Вдруг зазвенел будильник и ты проснулся!"
                                            " А нечего перед сном кушать, а то всякая чушь будет сниться!",
                                            reply_markup=remove_markup)
            if easter_egg1 + easter_egg2 + easter_egg3 == 3:
                await update.message.reply_text('Поздравляю! Вы прошли игру! Собранно предметов: 3/3.'
                                                ' Если хотите, можете сыграть снова!')
            else:
                await update.message.reply_text(f'Поздравляю! Вы прошли игру! Собранно предметов:'
                                                f' {easter_egg1 + easter_egg2 + easter_egg3}/3.'
                                                ' Рекомендуем поискать пасхалки!')
            return ConversationHandler.END
        else:
            await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт! \
Ты этого не ожидал, надо искать ключ', reply_markup=markup4)
            cur_stage = 10
            return 10
    elif ans == 'подняться':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        cur_stage = 4
        return 4
    await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
    cur_stage = 1
    return 1


async def response_3(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['подняться', 'зайти', 'обратно']:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
        return 3
    elif ans == 'подняться':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?')
        cur_stage = 9
        return 9
    elif ans == 'зайти':
        if easter_egg1:
            await update.message.reply_text('Ты зашел в столовую и не нашел ничего интересного', reply_markup=markup4)
        else:
            await update.message.reply_text('Ты зашел в столовую и нашел вилку! Взять её или нет?',
                                            reply_markup=markup7)
        cur_stage = 8
        return 8
    await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
    cur_stage = 1
    return 1


async def response_4(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['направо', 'вперед', 'обратно']:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        cur_stage = 4
        return 4
    elif ans == 'направо':
        await update.message.reply_text('Ты пришел в длинный коридор. Пойти вперед?', reply_markup=markup4)
        cur_stage = 5
        return 5
    elif ans == 'вперед':
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?', reply_markup=markup6)
        cur_stage = 6
        return 6
    await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?', reply_markup=markup3)
    cur_stage = 2
    return 2


async def response_5(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты пришел в длинный коридор. Пойти вперед?')
        return 5
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        cur_stage = 4
        return 4
    await update.message.reply_text('Ты прошел немного дальше по коридору и пока не видишь ничего интересного.'
                                    ' Пойти вперед?', reply_markup=markup8)
    cur_stage = 11
    return 11


async def response_6(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['посидеть', 'обратно']:
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?')
        return 6
    elif ans == 'посидеть':
        if key:
            await update.message.reply_text('Ты зашел в актовый зал и сел на удобные сиденья')
        else:
            await update.message.reply_text('Ты зашел в актовый зал и между сидений нашел ключ. Взять его?')
        cur_stage = 7
        return 7
    await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?')
    cur_stage = 4
    return 4


async def response_7(update, context):
    global cur_stage
    global key
    ans = update.message.text
    if key:
        if ans.lower() != 'обратно':
            await update.message.reply_text('Ты зашел в актовый зал и сел на удобные сиденья')
            return 7
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?')
        cur_stage = 6
        return 6
    else:
        if ans.lower() not in ['взять', 'нет']:
            await update.message.reply_text('Ты зашел в актовый зал и между сидений нашел ключ. Взять его?')
            return 7
        elif ans.lower() == 'взять':
            key = 1
            await update.message.reply_text('Ты подобрал ключ. Интересно, может он что-то откроет?')
        elif ans.lower() == 'нет':
            await update.message.reply_text('Ты не взял ключ.')
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?')
        cur_stage = 6
        return 6


async def response_8(update, context):
    global cur_stage
    global easter_egg1
    ans = update.message.text
    if easter_egg1:
        if ans != 'обратно':
            await update.message.reply_text('Ты зашел в столовую и не нашел ничего интересного')
            return 8
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
        cur_stage = 3
        return 3
    else:
        if ans.lower() not in ['взять', 'нет']:
            await update.message.reply_text('Ты зашел в столовую и нашел вилку! Взять её или нет?')
        elif ans.lower() == 'взять':
            easter_egg1 = 1
            await update.message.reply_text('Ты взял вилку. Может и пригодится!')
        elif ans.lower() == 'нет':
            await update.message.reply_text('Ты не подобрал вилку. Зачем она в пустой школе?')
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
        cur_stage = 3
        return 3


# Здесь изменена реплика

# БЫЛО: Ты пришел на 2 этаж. Пойти вперед или налево?

# СТАЛО: Ты пришел на 2 этаж. Пойти налево или вернуться обратно?


async def response_9(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'налево']:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти налево или вернуться обратно?')
        return 9
    elif ans.lower() == 'обратно':
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
        cur_stage = 3
        return 3
    await update.message.reply_text('Ты нашел какой-то коридор. Вперед?')
    cur_stage = 21
    return 21


async def response_10(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() != 'обратно':
        await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт! \
Ты этого не ожидал, надо искать ключ')
        return 10
    await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?')
    cur_stage = 2
    return 2


async def response_11(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты прошел немного дальше по коридору и пока не видишь ничего интересного.'
                                        ' Пойти вперед?')
        return 11
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты пришел в длинный коридор. Пойти вперед?')
        cur_stage = 5
        return 5
    await update.message.reply_text('Ты прошел еще дальше. Вперед?')
    cur_stage = 12
    return 12


async def response_12(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты прошел еще дальше. Вперед?')
        return 12
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты прошел немного дальше по коридору и пока не видишь ничего интересного.'
                                        ' Пойти вперед?')
        cur_stage = 11
        return 11
    await update.message.reply_text('Ты прошел подальше. Вперед?')
    cur_stage = 13
    return 13


async def response_13(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты прошел подальше. Вперед?')
        return 13
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты прошел еще дальше. Вперед?')
        cur_stage = 12
        return 12
    await update.message.reply_text('Ты все еще идешь по коридору. Дальше?')
    cur_stage = 14
    return 14


async def response_14(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты все еще идешь по коридору. Дальше?')
        return 14
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты прошел подальше. Вперед?')
        cur_stage = 13
        return 13
    await update.message.reply_text('Это очень длинный коридор. Дальше?')
    cur_stage = 15
    return 15


async def response_15(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Это очень длинный коридор. Дальше?')
        return 15
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты все еще идешь по коридору. Дальше?')
        cur_stage = 14
        return 14
    await update.message.reply_text('Это оооооооочень длинный коридор. Вперед?')
    cur_stage = 16
    return 16


async def response_16(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Это оооооооочень длинный коридор. Вперед?')
        return 16
    if ans.lower() == 'обратно':
        await update.message.reply_text('Это очень длинный коридор. Дальше?')
        cur_stage = 15
        return 15
    await update.message.reply_text('Конца коридора еще не видно. Вперед?')
    cur_stage = 17
    return 17


async def response_17(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Конца коридора еще не видно. Вперед?')
        return 17
    if ans.lower() == 'обратно':
        await update.message.reply_text('Это оооооооочень длинный коридор. Вперед?')
        cur_stage = 16
        return 16
    await update.message.reply_text('Тебе не надоело? Вперед?')
    cur_stage = 18
    return 18


async def response_18(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Тебе не надоело? Вперед?')
        return 18
    if ans.lower() == 'обратно':
        await update.message.reply_text('Конца коридора еще не видно. Вперед?')
        cur_stage = 17
        return 17
    await update.message.reply_text('Опять вперед?')
    cur_stage = 19
    return 19


async def response_19(update, context):
    global cur_stage
    global easter_egg2
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Опять вперед?')
        return 19
    if ans.lower() == 'обратно':
        await update.message.reply_text('Тебе не надоело? Вперед?')
        cur_stage = 18
        return 18
    if easter_egg2:
        await update.message.reply_text('Ты уже был здесь. Ничего интересного не осталось')
        cur_stage = 20
        return 20
    else:
        easter_egg2 = 1
        await update.message.reply_text('Все же это было не зря. Ты нашел линейку. Смешно, правда?')
        await update.message.reply_text('Ты вернулся к развилке.')
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?')
        cur_stage = 4
        return 4


async def response_20(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() != 'обратно':
        await update.message.reply_text('Ты уже был здесь. Ничего интересного не осталось')
        return 20
    await update.message.reply_text('Опять вперед?')
    cur_stage = 19
    return 19


async def response_21(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты нашел какой-то коридор. Вперед?')
        return 21
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или налево?')
        cur_stage = 9
        return 9
    await update.message.reply_text('Ты идешь по коридору. Вперед?')
    cur_stage = 22
    return 22


async def response_22(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты идешь по коридору. Вперед?')
        return 22
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты нашел какой-то коридор. Вперед?')
        cur_stage = 21
        return 21
    await update.message.reply_text('Ты все еще идешь по коридору. Вперед?')
    cur_stage = 23
    return 23


async def response_23(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?')
        return 23
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты идешь по коридору. Вперед?')
        cur_stage = 22
        return 22
    await update.message.reply_text('Ты опять идешь по коридору. Вперед?')
    cur_stage = 24
    return 24


async def response_24(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты опять идешь по коридору. Вперед?')
        return 24
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты все еще идешь по коридору. Вперед?')
        cur_stage = 23
        return 23
    await update.message.reply_text('Ты снова идешь по коридору. Вперед?')
    cur_stage = 25
    return 25


async def response_25(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты снова идешь по коридору. Вперед?')
        return 25
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты опять идешь по коридору. Вперед?')
        cur_stage = 24
        return 24
    await update.message.reply_text('Ты продолжаешь идти по коридору. Вперед?')
    cur_stage = 26
    return 26


async def response_26(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты продолжаешь идти по коридору. Вперед?')
        return 26
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты снова идешь по коридору. Вперед?')
        cur_stage = 25
        return 25
    await update.message.reply_text('Ты не зананчиваешь идти по коридору. Вперед?')
    cur_stage = 27
    return 27


async def response_27(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Ты не зананчиваешь идти по коридору. Вперед?')
        return 27
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты продолжаешь идти по коридору. Вперед?')
        cur_stage = 26
        return 26
    await update.message.reply_text('Не может же этот коридор быть бесконечным. Вперед?')
    cur_stage = 28
    return 28


async def response_28(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Не может же этот коридор быть бесконечным. Вперед?')
        return 28
    if ans.lower() == 'обратно':
        await update.message.reply_text('Ты не зананчиваешь идти по коридору. Вперед?')
        cur_stage = 27
        return 27
    await update.message.reply_text('Вдали виден конец коридора. Вперед?')
    cur_stage = 29
    return 29


async def response_29(update, context):
    global cur_stage
    global easter_egg3
    ans = update.message.text
    if ans.lower() not in ['обратно', 'вперед']:
        await update.message.reply_text('Вдали виден конец коридора. Ввперед?')
        return 29
    if ans.lower() == 'обратно':
        await update.message.reply_text('Не может же этот коридор быть бесконечным. Вперед?')
        cur_stage = 28
        return 28
    if easter_egg3:
        await update.message.reply_text('Здесь нет ничего интересного', reply_markup=markup4)
        cur_stage = 30
        return 30
    else:
        easter_egg3 = 1
        await update.message.reply_text('Ты нашел на полу ластик. И зачем он?')
        await update.message.reply_text('Ты вернулся к развилке')
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или налево?')
        cur_stage = 9
        return 9


async def response_30(update, context):
    global cur_stage
    ans = update.message.text
    if ans.lower() != 'обратно':
        await update.message.reply_text('Здесь нет ничего интересного')
        return 30
    await update.message.reply_text('Вдали виден конец коридора. Вперед?')
    cur_stage = 29
    return 29


async def stop(update, context):
    global cur_stage
    global key, easter_egg1, easter_egg2, easter_egg3
    await update.message.reply_text("Возвращайтесь снова! (Ваш прогресс не сохранился)",
                                    reply_markup=ReplyKeyboardRemove())
    key = 0
    easter_egg1 = 0
    easter_egg2 = 0
    easter_egg3 = 0
    cur_stage = 0
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()
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
    key = 0
    cur_stage = 0
    easter_egg1 = 0
    easter_egg2 = 0
    easter_egg3 = 0
    main()
