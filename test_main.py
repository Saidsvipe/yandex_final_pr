# Инкин Максим, 30-я когорта — Финальный проект. Инженер по тестированию плюс

import logging
from data import order_body
from sender_stand_request import create_order, get_order_by_track

# Настройка логирования
logging.basicConfig(
    filename='/var/www/backend/logs/error.log',
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def test_create_order_and_get_by_track():
    try:
        # Создать заказ
        create_resp = create_order(order_body)
        assert create_resp.status_code == 201, f"Ошибка создания заказа: {create_resp.text}"

        track = create_resp.json().get("track")
        assert track, "Трек заказа не получен"

        # Получить заказ по треку
        get_resp = get_order_by_track(track)
        assert get_resp.status_code == 200, f"Ошибка получения заказа по треку: {get_resp.text}"

    except AssertionError as ae:
        logging.error(ae)
        raise
    except Exception as e:
        logging.exception("Неожиданная ошибка в автотесте")
        raise