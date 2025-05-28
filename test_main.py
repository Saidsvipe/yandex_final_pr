import requests

BASE_URL = "https://ffdedde3-fb04-41a6-b292-c05982b88375.serverhub.praktikum-services.ru"  

def test_create_order_and_get_by_track():
    # Создать заказ
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Пушкина, д.10",
        "metroStation": "Пушкинская",
        "phone": "+79161234567",
        "rentTime": 3,
        "deliveryDate": "2025-05-28",
        "color": ["black"],
        "comment": "Тестовый заказ"
    }
    create_resp = requests.post(f"{BASE_URL}/orders", json=order_data)
    assert create_resp.status_code == 201, f"Ошибка создания заказа: {create_resp.text}"

    track = create_resp.json().get("track")
    assert track is not None, "Номер трека не получен"

    # 2. Получить заказ по треку
    get_resp = requests.get(f"{BASE_URL}/orders/track", params={"t": track})
    assert get_resp.status_code == 200, f"Заказ по треку не найден: {get_resp.text}"

    print("Тест пройден: заказ создан и успешно получен по треку")

if __name__ == "__main__":
    test_create_order_and_get_by_track()