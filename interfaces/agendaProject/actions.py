import requests

class AgendaActions:
    @staticmethod
    def get_zip_code(zip_code: str):
        api_url = f'https://viacep.com.br/ws/{zip_code}/json/'
        response = requests.get(api_url)
        data = response.json()
        if 'erro' in data:
            return None

        return data