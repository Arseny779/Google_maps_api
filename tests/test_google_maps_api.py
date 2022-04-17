from requests import Response
from utils.api import Google_maps_api
from utils.checking import Checking
import json



"""Создание , изменение и удаление новой локации"""

class Test_create_place():


    def test_create_new_place(self):
        
        print('Метод POST')
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        Checking.check_json_value(result_post, 'status', 'OK')

        print('Метод GET POST')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('Метод PUT')
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('Метод GET PUT')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print('Метод DELETE')
        result_get: Response = Google_maps_api.delete_new_place(place_id)
        
        print('Метод GET DELETE')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        