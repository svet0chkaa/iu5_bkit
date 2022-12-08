import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

#log (вводит текущее состояние в терминале, что что-то делает)
logging.basicConfig(level=logging.INFO) #логируем информацию

#init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#prices (список доступных цен на наши продукты)
PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=500*100) #сумму указываем в копейках (а в боте будут рубли)


#buy (генерирует и отправляет пользователю инвойс платежа)
@dp.message_handler(commands=['buy']) #@декоратор сообщение обработчик
async def buy(message: types.Message): #ассинхронная функция (выполнаяется параллелльно с другими) 
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':   #split - берет сторку и разделяет на подстроки
        await bot.send_message(message.chat.id, "Тестовый платеж!")  #await - ожидать, пока не напишется TEST

    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://фотообои.рф/upload/iblock/1b3/bs7385.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False, #True будет тогда, когда способ оплаты зависит от выбранного способа доставки
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


# pre checkout (обработка и утверждение платежа перед тем, как пользователь его совершит) (надо дать ответ в течение 10 сек, иначе платеж отменится)
@dp.pre_checkout_query_handler(lambda query: True) #для отправки запроса на предоплату, lambda query - проверяем, что пришел положительный ответ
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True) #ok=True - не должно быть ошибок


# successful payment (обработка успешно проведенного платежа)
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT) #выполняется, если платеж прошел
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():   #итерируется по словарю 
        print(f"{k} = {v}")
 
    await bot.send_message(message.chat.id,
                           f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")


#run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False) #так как работаем с финансами, надо обработать каждое сообщение с серверов тг, поэтому аргумент в значении False