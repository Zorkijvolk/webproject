from telegram.ext import Application, MessageHandler, filters, ConversationHandler, CommandHandler
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
import logging

BOT_TOKEN = '7223872652:AAEGTU0Ax5c4sPduTzBYfs0JsnrVS6L-Uzg'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

keyboard1 = [['/right'],
             ['/left']]
markup = ReplyKeyboardMarkup(keyboard1, one_time_keyboard=False)

keyboard2 = [['/enter_the_cafeteria'],
             ['/back']]
markup2 = ReplyKeyboardMarkup(keyboard2, one_time_keyboard=False)

keyboard3 = [['/right'],
             ['/up'],
             ['/back']]
markup3 = ReplyKeyboardMarkup(keyboard3, one_time_keyboard=False)

keyboard4 = [['/back']]
markup4 = ReplyKeyboardMarkup(keyboard4, one_time_keyboard=False)

remove_markup = ReplyKeyboardRemove()

keyboard5 = [['/forward'],
             ['/right'],
             ['/back']]
markup5 = ReplyKeyboardMarkup(keyboard5, one_time_keyboard=False)

keyboard6 = [['/sit'],
             ['/back']]
markup6 = ReplyKeyboardMarkup(keyboard6, one_time_keyboard=False)

keyboard7 = [['/take'],
             ['/dont_take'],
             ['/back']]
markup7 = ReplyKeyboardMarkup(keyboard7, one_time_keyboard=False)


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
    global cur_stage, key
    if cur_stage == 7:
        key = 1
        await update.message.reply_text('Ты подобрал ключ. Интересно, может он что-то откроет?', reply_markup=markup4)


async def dont_take(update, context):
    global cur_stage
    if cur_stage == 7:
        await update.message.reply_text('Ты не взял ключ.', reply_markup=markup4)


async def up(update, context):
    global cur_stage
    if cur_stage == 2:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?', reply_markup=markup5)
        cur_stage = 4
        return 4


async def right(update, context):
    global cur_stage, key
    if cur_stage == 0 or cur_stage == 1:
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
            if easter_egg:
                await update.message.reply_text('Поздравляю! Вы прошли игру! Собранно предметов: 1/1.'
                                                ' Если хотите, можете сыграть снова!')
            else:
                await update.message.reply_text('Поздравляю! Вы прошли игру! Собранно предметов: 0/1.'
                                                ' Рекомендуем поискать пасхалку!')
            return ConversationHandler.END
        else:
            await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт! \
        Ты этого не ожидал, надо искать ключ', reply_markup=markup4)
            cur_stage = 10
            return 10


async def left(update, context):
    global cur_stage
    if cur_stage == 0:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
        cur_stage = 3
        return 3


async def start(update, context):
    await update.message.reply_text("Ты пробрался в свою школу с одним заданием: прокрасться в кабинет информатики!"
                                    " Ты зашел через главный вход,"
                                    " потому что твои напарники предварительно отвлекли охранника и выключили камеры.")
    await update.message.reply_text('У тебя выбор: пойти направо или налево?', reply_markup=markup)
    return 1


async def first_response(update, context):
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
        ans = update.message.text
    if ans.lower() not in ['направо', 'налево']:
        await update.message.reply_text('У тебя выбор: пойти направо или налево?')
        return 1
    elif ans.lower() == 'направо':
        await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?')
        return 2
    await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
    return 3


async def second_response(update, context):
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
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
                                            " А нечего перед сном кушать, а то всякая чушь будет сниться!")
            if easter_egg:
                await update.message.reply_text('Поздравляю! Вы прошли игру! Собранно предметов: 1/1.'
                                                ' Если хотите, можете сыграть снова!')
            else:
                await update.message.reply_text('Поздравляю! Вы прошли игру! Собранно предметов: 0/1.'
                                                ' Рекомендуем поискать пасхалку!')
            return ConversationHandler.END
        else:
            await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт! \
Ты этого не ожидал, надо искать ключ')
            return 10
    elif ans == 'подняться':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?')
        return 4
    await update.message.reply_text('У тебя выбор: пойти направо или налево?')
    return 1


async def third_response(update, context):
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
        ans = update.message.text
    if ans.lower() not in ['подняться', 'зайти', 'обратно']:
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
        return 3
    elif ans == 'подняться':
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед?')
        return 9
    elif ans == 'зайти':
        if easter_egg:
            await update.message.reply_text('Ты зашел в столовую и не нашел ничего интересного')
        else:
            await update.message.reply_text('Ты зашел в столовую и нашел вилку! Взять её или нет?')
        return 8
    await update.message.reply_text('У тебя выбор: пойти направо или налево?')
    return 1


async def fourth_response(update, context):
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
        ans = update.message.text
    if ans.lower() not in ['направо', 'вперед', 'обратно']:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?')
        return 4
    elif ans == 'направо':
        await update.message.reply_text('Ты пришел к концу коридора, но ничего не нашел')
        return 5
    elif ans == 'вперед':
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?')
        return 6
    await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?')
    return 2


async def fifth_response(update, context):
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
        ans = update.message.text
    if ans.lower() != 'обратно':
        await update.message.reply_text('Ты пришел к концу коридора, но ничего не нашел')
        return 5
    await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?')
    return 4


async def sixth_response(update, context):
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
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
        return 7
    await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед или направо?')
    return 4


async def seventh_response(update, context):
    global key
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
        ans = update.message.text
    if key:
        if ans.lower() != 'обратно':
            await update.message.reply_text('Ты зашел в актовый зал и сел на удобные сиденья')
            return 7
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?')
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
        return 6


async def eighth_response(update, context):
    global easter_egg
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
        ans = update.message.text
    if easter_egg:
        if ans != 'обратно':
            await update.message.reply_text('Ты зашел в столовую и не нашел ничего интересного')
            return 8
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
        return 3
    else:
        if ans.lower() not in ['взять', 'нет']:
            await update.message.reply_text('Ты зашел в столовую и нашел вилку! Взять её или нет?')
        elif ans.lower() == 'взять':
            easter_egg = 1
            await update.message.reply_text('Ты взял вилку. Может и пригодится!')
        elif ans.lower() == 'нет':
            await update.message.reply_text('Ты не подобрал вилку. Зачем она в пустой школе?')
        await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
        return 3


async def ninth_response(update, context):
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
        ans = update.message.text
    if ans.lower() not in ['вперед', 'обратно']:
        await update.message.reply_text('Ты пришел на 2 этаж. Пойти вперед?')
        return 9
    elif ans == 'вперед':
        await update.message.reply_text('Tы пришел к большому актовому залу, почти как в театре:'
                                        ' посидеть в нем или вернуться обратно?')
        return 6
    await update.message.reply_text('Ты пришел к лестнице и столовой. Зайти в столовую или подняться на 2 этаж?')
    return 3


async def tenth_response(update, context):
    global last_ans
    if last_ans:
        ans = last_ans
        last_ans = None
    else:
        ans = update.message.text
    if ans.lower() != 'обратно':
        await update.message.reply_text('Ураа! Ты нашел кабинет информатики!... Но вот проблема! Он закрыт! \
Ты этого не ожидал, надо искать ключ')
        return 10
    await update.message.reply_text('Tы пришел к лестнице: пойти правее или подняться?')
    return 2


async def stop(update, context):
    global key, easter_egg
    await update.message.reply_text("Возвращайтесь снова! (Ваш прогресс не сохранился) ")
    key = 0
    easter_egg = 0
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    #    application.add_handler(CommandHandler("right", right))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), CommandHandler('right', right), CommandHandler('left', left),
                      CommandHandler('back', back), CommandHandler('up', up), CommandHandler('forward', forward),
                      CommandHandler('take', take), CommandHandler('dont_take', dont_take), CommandHandler('sit', sit)],

        states={

            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],

            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_response)],

            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, third_response)],

            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, fourth_response)],

            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, fifth_response)],

            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, sixth_response)],

            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, seventh_response)],

            8: [MessageHandler(filters.TEXT & ~filters.COMMAND, eighth_response)],

            9: [MessageHandler(filters.TEXT & ~filters.COMMAND, ninth_response)],

            10: [MessageHandler(filters.TEXT & ~filters.COMMAND, tenth_response)]
        },

        fallbacks=[CommandHandler('stop', stop), CommandHandler('right', right), CommandHandler('left', left),
                   CommandHandler('back', back), CommandHandler('up', up), CommandHandler('forward', forward),
                   CommandHandler('take', take), CommandHandler('dont_take', dont_take), CommandHandler('sit', sit)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    key = 0
    last_ans = None
    cur_stage = 0
    easter_egg = 0
    main()
