import os
from dotenv import load_dotenv
import requests


class Previsao:
    
    URL_BASE = "http://api.weatherapi.com/v1"
    
    def __init__(self):
        
        load_dotenv()
        
        self.__token = os.getenv('API_TOKEN')
        
        if not self.__token:
            raise ValueError("Token de API não encontrado. Verifique o arquivo .env.")

        
    def conexao(self, url, params):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            print("Consulta realizada com sucesso!")
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ou requisição: {e}")
            return None
        
        if response:
            return response.json()
        else:
            print("Erro ao obter dados. Nenhum dado foi retornado.")
            return None

    def validar_resposta(self, response):
            """Função para validar a resposta e tratar erro."""
            if response:
                try:
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.HTTPError as errh:
                    print(f"Erro HTTP: {errh}")
                except requests.exceptions.RequestException as e:
                    print(f"Erro de requisição: {e}")
            print("Erro ao obter dados. Nenhum dado foi retornado.")
            return None
    
    def consulta_previsao_atual(self, coordenadas, aqi):
        
        if aqi == None:
            aqi = "no"
    
        url = f"{self.URL_BASE}/current.json"
        
        params = {
            "key": self.__token,
            "q": coordenadas,
            "aqi": aqi
            }
        
        response = self.conexao(url=url, params=params)
        return self.validar_resposta(response)
    
    def consulta_previsao_historica_dia(self, coordenadas, dt):
        
    
        url = f"{self.URL_BASE}/history.json"
        
        params = {
            "key": self.__token,
            "q": coordenadas,
            "dt": dt
            }
        
        response = self.conexao(url=url, params=params)
        return self.validar_resposta(response)

