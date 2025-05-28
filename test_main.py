# Инкин Максим, 30-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import logging
from configuration import URL_SERVICE, CREATE_ORDER
from data import order_body

# Настройка логирования
logging.basicConfig(
    filename='/var/www/backend/logs/error.log',
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def test_create_order_and_get_by_track():
    try:
        # Шаг 1: создать заказ
        create_resp = requests.post(URL_SERVICE + CREATE_ORDER, json=order_body)
        assert create_resp.status_code == 201, f"Ошибка создания заказа: {create_resp.text}"

        track = create_resp.json().get("track")
        assert track, "Трек заказа не получен"

        # Шаг 2: получить заказ по треку
        get_resp = requests.get(f"{URL_SERVICE}/api/v1/orders/track", params={"t": track})
        assert get_resp.status_code == 200, f"Ошибка получения заказа по треку: {get_resp.text}"

        print("Тест пройден: заказ успешно создан и найден по треку")

    except AssertionError as ae:
        logging.error(ae)
        raise
    except Exception as e:
        logging.exception("Неожиданная ошибка в автотесте")
        raise
