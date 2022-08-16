
from aiogram.utils import executor
from config import dp
import logging
from handlers import client,admin,callback,extra,fsm_ankets

client.register_handlers_client(dp)
admin.register_handler_admin(dp)
callback.register_handlers_callback(dp)
fsm_ankets.register_handlers_fsmanketa(dp)

extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)