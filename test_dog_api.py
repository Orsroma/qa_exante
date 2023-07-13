import pytest
import requests


class TestDog:

    def test_response_status(self, response_status):

        # Тест проверяет текст успешности ответа сервера для запроса произвольно выбранного изображения собаки

        if response_status.lower() == 'success':
            assert f'Response status: {response_status}'
        elif response_status != 'success':
            assert False, f'Response status: {response_status}'
        else:
            assert False, 'Something wrong'

    def test_response_status_code(self, response_status_code):

        # Тест проверяет код успешности ответа сервера для запроса произвольно выбранного изображения собаки

        if response_status_code == 200:
            assert f'Response status code: {response_status_code}'
        elif response_status_code != 200:
            assert False, f'Response status code: {response_status_code}'
        else:
            assert False, 'Something wrong'

    def test_breed_in_list(self, response_breeds_list):

        # Тест проверяет успешность нахождения породы собаки например поиск МОПСА в списке всех пород

        if 'pug' in response_breeds_list['message']:
            assert 'pug in response_breeds_list'
        elif 'pug' not in response_breeds_list['message']:
            assert False, 'pug not in response_breeds_list'
        else:
            assert False, 'Something wrong'

    def test_response_status_breed(self, response_status_breed):

        # Тест проверяет успешность ответа сервера для запроса заданной породы собаки

        if 'success' in response_status_breed:
            assert f'Response status breed: {response_status_breed}'
        elif 'success' not in response_status_breed:
            assert False, f'Response status breed: {response_status_breed}'
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('breed', ["pug", "borzoi", "boxer", "pitbullf"])
    def test_given_breed_in_list(self, response_breeds_list, breed):

        # Тест проверяет успешность нахождения определенной породы собаки в списке всех пород

        if breed in response_breeds_list['message']:
            assert f'{breed} in response_breeds_list'

        else:
            assert False, 'Something wrong'

    def test_breeds_list_size(self):
        # Тест проверяет, что размер списка всех пород собак соответствует ожидаемому значению.

        response = requests.get('https://dog.ceo/api/breeds/list/all')
        response_breeds_list = response.json()

        expected_breeds_count = 98
        actual_breeds_count = len(response_breeds_list['message'])
        assert actual_breeds_count == expected_breeds_count, f'Expected {expected_breeds_count} breeds, but got {actual_breeds_count}'
