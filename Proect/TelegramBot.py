import telebot
from telebot import types
import random
from datetime import datetime, timedelta
import time
import threading

bot = telebot.TeleBot('7640686137:AAFxTV_Y5xLY1ShdKyvgFWxG9iZh00eBwgY')

# Хранилище данных о розыгрышах
giveaways = {}
participants = {}


# Функция для автоматической проверки розыгрышей
def check_giveaways():
    while True:
        try:
            now = datetime.now()
            ended_giveaways = []

            # Проверяем все розыгрыши
            for giveaway_id, giveaway in list(giveaways.items()):
                if 'end_date' in giveaway and now >= giveaway['end_date']:
                    try:
                        # Проверяем минимальное количество участников
                        if len(giveaway['participants']) >= giveaway.get('min_participants', 1):
                            # Выбираем победителей
                            winners_count = min(giveaway['winners_count'], len(giveaway['participants']))
                            winners = random.sample(giveaway['participants'], winners_count)
                            giveaway['winners'] = [
                                f"@{bot.get_chat(user_id).username}" if bot.get_chat(
                                    user_id).username else f"user_{user_id}"
                                for user_id in winners
                            ]

                            # Формируем сообщение с победителями
                            winners_list = "\n".join([f"🎖 {winner}" for winner in giveaway['winners']])
                            result_message = (
                                f"🏆 **РЕЗУЛЬТАТЫ РОЗЫГРЫША** 🎉\n\n"
                                f"🎁 Приз: {giveaway['prize']}\n"
                                f"👑 Победители:\n{winners_list}\n\n"
                                f"Поздравляем победителей! 🎉"
                            )

                            # Отправляем результаты в каналы
                            for channel in giveaway['channels']:
                                try:
                                    bot.send_message(channel['id'], result_message, parse_mode="Markdown")
                                except Exception as e:
                                    print(f"Ошибка при отправке в канал {channel['title']}: {e}")

                            # Уведомляем администратора
                            try:
                                bot.send_message(
                                    giveaway['admin'],
                                    f"✅ Розыгрыш завершен! Победители:\n\n{winners_list}"
                                )
                            except Exception as e:
                                print(f"Ошибка при уведомлении администратора: {e}")
                        else:
                            # Уведомляем администратора о недостатке участников
                            try:
                                bot.send_message(
                                    giveaway['admin'],
                                    f"⚠️ Розыгрыш отменен! Недостаточно участников "
                                    f"(требуется: {giveaway['min_participants']}, "
                                    f"участвует: {len(giveaway['participants'])})."
                                )
                            except Exception as e:
                                print(f"Ошибка при уведомлении администратора: {e}")

                        # Помечаем розыгрыш для удаления
                        ended_giveaways.append(giveaway_id)
                    except Exception as e:
                        print(f"Ошибка при обработке розыгрыша {giveaway_id}: {e}")

            # Удаляем завершенные розыгрыши
            for giveaway_id in ended_giveaways:
                if giveaway_id in giveaways:
                    del giveaways[giveaway_id]

        except Exception as e:
            print(f"Ошибка в фоновой проверке розыгрышей: {e}")

        # Проверяем каждую минуту
        time.sleep(60)


# Запускаем фоновую проверку в отдельном потоке
threading.Thread(target=check_giveaways, daemon=True).start()


# Остальной код остается без изменений
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type in ['group', 'supergroup', 'channel']:
        bot.send_message(message.chat.id,
                         "🤖 Бот для розыгрышей активирован! Используйте /new_giveaway в личных сообщениях с ботом, чтобы создать новый розыгрыш.")
    else:
        # Обработка участия в розыгрыше через start
        if len(message.text.split()) > 1 and message.text.split()[1].startswith('giveaway_'):
            giveaway_id = int(message.text.split()[1].split('_')[1])
            participate_in_giveaway(message, giveaway_id)
            return

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎁 Создать розыгрыш")
        btn2 = types.KeyboardButton("📊 Мои розыгрыши")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "👋 Привет! Я бот для проведения розыгрышей в Telegram-каналах!",
                         reply_markup=markup)


def participate_in_giveaway(message, giveaway_id):
    try:
        if giveaway_id in giveaways:
            if message.from_user.id not in giveaways[giveaway_id]['participants']:
                giveaways[giveaway_id]['participants'].append(message.from_user.id)
                bot.send_message(message.chat.id, "✅ Вы успешно зарегистрированы в розыгрыше!")
            else:
                bot.send_message(message.chat.id, "ℹ️ Вы уже участвуете в этом розыгрыше.")
        else:
            bot.send_message(message.chat.id, "⚠️ Розыгрыш не найден или уже завершен.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка при регистрации: {e}")


@bot.message_handler(commands=['new_giveaway'])
def new_giveaway_command(message):
    if message.chat.type in ['group', 'supergroup', 'channel']:
        bot.send_message(message.chat.id,
                         "ℹ️ Чтобы создать новый розыгрыш, напишите мне в личные сообщения @your_bot_username")
    else:
        start_giveaway_creation(message)


def start_giveaway_creation(message):
    try:
        msg = bot.send_message(message.chat.id,
                               "🎉 Давайте создадим новый розыгрыш!\n\n📝 Введите название приза (что вы разыгрываете):")
        bot.register_next_step_handler(msg, process_prize_name)
    except Exception as e:
        bot.reply_to(message, f"Ошибка при создании розыгрыша: {e}")


def process_prize_name(message):
    try:
        chat_id = message.chat.id
        giveaways[chat_id] = {
            'prize': message.text,
            'admin': message.from_user.id,
            'channels': [],
            'participants': [],
            'winners': []
        }

        msg = bot.send_message(chat_id, "🔢 Сколько участников должно быть для розыгрыша? (минимальное количество)")
        bot.register_next_step_handler(msg, process_min_participants)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")


def process_min_participants(message):
    try:
        chat_id = message.chat.id
        min_participants = int(message.text)

        if min_participants < 2:
            raise ValueError("Минимальное количество участников - 2")

        giveaways[chat_id]['min_participants'] = min_participants

        msg = bot.send_message(chat_id, "🏆 Сколько будет победителей?")
        bot.register_next_step_handler(msg, process_winners_count)
    except ValueError:
        msg = bot.send_message(chat_id,
                               "⚠️ Пожалуйста, введите корректное число (минимум 2). Сколько участников должно быть для розыгрыша?")
        bot.register_next_step_handler(msg, process_min_participants)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")


def process_winners_count(message):
    try:
        chat_id = message.chat.id
        winners_count = int(message.text)

        if winners_count < 1:
            raise ValueError("Должен быть хотя бы 1 победитель")

        giveaways[chat_id]['winners_count'] = winners_count

        msg = bot.send_message(chat_id,
                               "📅 Когда закончится розыгрыш? (введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ, например 31.12.2023 23:59)")
        bot.register_next_step_handler(msg, process_end_date)
    except ValueError:
        msg = bot.send_message(chat_id,
                               "⚠️ Пожалуйста, введите корректное число (минимум 1). Сколько будет победителей?")
        bot.register_next_step_handler(msg, process_winners_count)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")


def process_end_date(message):
    try:
        chat_id = message.chat.id
        end_date_str = message.text

        end_date = datetime.strptime(end_date_str, "%d.%m.%Y %H:%M")
        giveaways[chat_id]['end_date'] = end_date

        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("➕ Добавить канал", callback_data="add_channel")
        markup.add(btn)

        bot.send_message(chat_id, f"✅ Основные параметры розыгрыша установлены!\n\n"
                                  f"🎁 Приз: {giveaways[chat_id]['prize']}\n"
                                  f"👥 Минимум участников: {giveaways[chat_id]['min_participants']}\n"
                                  f"🏆 Победителей: {giveaways[chat_id]['winners_count']}\n"
                                  f"⏳ Окончание: {end_date_str}\n\n"
                                  f"Теперь добавьте каналы, где будет проводиться розыгрыш:",
                         reply_markup=markup)
    except ValueError:
        msg = bot.send_message(chat_id,
                               "⚠️ Неверный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ, например 31.12.2023 23:59")
        bot.register_next_step_handler(msg, process_end_date)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")


@bot.callback_query_handler(func=lambda call: call.data == "add_channel")
def add_channel_callback(call):
    try:
        msg = bot.send_message(call.message.chat.id,
                               "📢 Перешлите любое сообщение из канала, который вы хотите добавить (Обязательно добавьте бота в телеграмм канал и выдайте права администратора):")
        bot.register_next_step_handler(msg, process_channel_addition)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"⚠️ Ошибка: {e}")


def process_channel_addition(message):
    try:
        chat_id = message.chat.id
        giveaway = giveaways.get(chat_id)

        if not giveaway:
            raise ValueError("Розыгрыш не найден")

        if message.forward_from_chat and message.forward_from_chat.type == "channel":
            channel_id = message.forward_from_chat.id
            channel_title = message.forward_from_chat.title
        elif message.text.startswith("@"):
            channel_id = message.text[1:]
            channel_title = message.text
        else:
            raise ValueError("Неверный формат канала")

        try:
            chat_member = bot.get_chat_member(channel_id if isinstance(channel_id, int) else f"@{channel_id}",
                                              bot.get_me().id)
            if chat_member.status not in ["administrator", "creator"]:
                raise ValueError("Бот не является администратором канала")
        except:
            raise ValueError("Бот не является администратором канала или канал не найден")

        giveaway['channels'].append({
            'id': channel_id,
            'title': channel_title
        })

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("➕ Добавить еще канал", callback_data="add_channel")
        btn2 = types.InlineKeyboardButton("✅ Завершить настройку", callback_data="finish_setup")
        markup.add(btn1, btn2)

        channels_list = "\n".join([f"📢 {ch['title']}" for ch in giveaway['channels']])

        bot.send_message(chat_id, f"✅ Канал добавлен!\n\nСписок каналов:\n{channels_list}", reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка: {e}\nПопробуйте еще раз.")
        start_giveaway_creation(message)


@bot.callback_query_handler(func=lambda call: call.data == "finish_setup")
def finish_setup_callback(call):
    try:
        chat_id = call.message.chat.id
        giveaway = giveaways.get(chat_id)

        if not giveaway or not giveaway.get('channels'):
            bot.send_message(chat_id, "⚠️ Вы не добавили ни одного канала. Розыгрыш не может быть создан.")
            return

        giveaway_post = f"🎉 **РОЗЫГРЫШ** 🎁\n\n" \
                        f"🏆 Приз: {giveaway['prize']}\n" \
                        f"👑 Победителей: {giveaway['winners_count']}\n" \
                        f"⏳ Завершается: {giveaway['end_date'].strftime('%d.%m.%Y %H:%M')}\n\n" \
                        f"Для участия нажмите кнопку ниже!"

        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🎁 Участвовать",
                                         url=f"https://t.me/{bot.get_me().username}?start=giveaway_{chat_id}")
        markup.add(btn)

        for channel in giveaway['channels']:
            try:
                bot.send_message(channel['id'], giveaway_post, reply_markup=markup, parse_mode="Markdown")
            except Exception as e:
                bot.send_message(chat_id, f"⚠️ Не удалось опубликовать в канале {channel['title']}: {e}")

        bot.send_message(chat_id,
                         "✅ Розыгрыш успешно запущен в выбранных каналах! Я сообщу вам, когда придет время выбирать победителей.")
    except Exception as e:
        bot.send_message(chat_id, f"⚠️ Ошибка при завершении настройки: {e}")


@bot.message_handler(func=lambda message: message.text == "🎁 Создать розыгрыш")
def create_giveaway(message):
    start_giveaway_creation(message)


@bot.message_handler(func=lambda message: message.text == "📊 Мои розыгрыши")
def my_giveaways(message):
    try:
        user_giveaways = []
        for giveaway_id, giveaway in giveaways.items():
            if giveaway['admin'] == message.from_user.id:
                channels = ", ".join([ch['title'] for ch in giveaway['channels']])
                user_giveaways.append(
                    f"🎁 {giveaway['prize']}\n"
                    f"📢 Каналы: {channels}\n"
                    f"👥 Участников: {len(giveaway['participants'])}\n"
                    f"⏳ Завершается: {giveaway['end_date'].strftime('%d.%m.%Y %H:%M')}\n"
                    f"🔗 Ссылка: https://t.me/{bot.get_me().username}?start=giveaway_{giveaway_id}\n"
                )

        if user_giveaways:
            bot.send_message(message.chat.id, "📊 Ваши активные розыгрыши:\n\n" + "\n\n".join(user_giveaways))
        else:
            bot.send_message(message.chat.id, "ℹ️ У вас нет активных розыгрышей.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка при получении списка розыгрышей: {e}")


@bot.message_handler(commands=['draw_winners'])
def draw_winners(message):
    try:
        chat_id = message.chat.id
        giveaway = giveaways.get(chat_id)

        if not giveaway:
            bot.send_message(chat_id, "⚠️ Активный розыгрыш не найден.")
            return

        if datetime.now() < giveaway['end_date']:
            bot.send_message(chat_id,
                             f"⚠️ Розыгрыш еще не закончился. Окончание: {giveaway['end_date'].strftime('%d.%m.%Y %H:%M')}")
            return

        if len(giveaway['participants']) < giveaway['min_participants']:
            bot.send_message(chat_id,
                             f"⚠️ Недостаточно участников для розыгрыша (требуется: {giveaway['min_participants']}, участвует: {len(giveaway['participants'])}). Розыгрыш отменен.")
            return

        winners = random.sample(giveaway['participants'], min(giveaway['winners_count'], len(giveaway['participants'])))
        giveaway['winners'] = [
            f"@{bot.get_chat(user_id).username}" if bot.get_chat(user_id).username else f"user_{user_id}" for user_id in
            winners]

        winners_list = "\n".join([f"🎖 {winner}" for winner in giveaway['winners']])

        result_message = f"🏆 **РЕЗУЛЬТАТЫ РОЗЫГРЫША** 🎉\n\n" \
                         f"🎁 Приз: {giveaway['prize']}\n" \
                         f"👑 Победители:\n{winners_list}\n\n" \
                         f"Поздравляем победителей! 🎉"

        for channel in giveaway['channels']:
            try:
                bot.send_message(channel['id'], result_message, parse_mode="Markdown")
            except Exception as e:
                bot.send_message(chat_id, f"⚠️ Не удалось отправить результаты в канал {channel['title']}: {e}")

        bot.send_message(chat_id, f"✅ Победители розыгрыша выбраны и опубликованы в каналах!\n\n{winners_list}")
    except Exception as e:
        bot.send_message(chat_id, f"⚠️ Ошибка при выборе победителей: {e}")


# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)