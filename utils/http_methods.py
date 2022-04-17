import requests
from logger import Logger

""" Список HTTP методов"""
class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod # это означает что мы теперь сможем вызывать этот метод в любом другом классе, поэтому и не передаем параметр self
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers = Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_responce(result)
        return result

    @staticmethod # это означает что мы теперь сможем вызывать этот метод в любом другом классе, поэтому и не передаем параметр self
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json = body, headers = Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_responce(result)
        return result

    @staticmethod # это означает что мы теперь сможем вызывать этот метод в любом другом классе, поэтому и не передаем параметр self
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json = body, headers = Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_responce(result)
        return result

    @staticmethod # это означает что мы теперь сможем вызывать этот метод в любом другом классе, поэтому и не передаем параметр self
    def delete(url,body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, json = body,headers = Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_responce(result)
        return result    