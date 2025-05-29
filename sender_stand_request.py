import requests
from configuration import URL_SERVICE, CREATE_ORDER, GET_ORDER
def create_order(order_body):
    return requests.post(URL_SERVICE + CREATE_ORDER, json=order_body)
def get_order_by_track(track):
    return requests.get(URL_SERVICE + GET_ORDER, params={"t": track})
