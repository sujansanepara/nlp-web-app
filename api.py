import requests
import os
from dotenv import load_dotenv

load_dotenv()

def sentiment_analysis(text):
        url = 'https://api.api-ninjas.com/v1/' + 'sentiment?text={}'.format(text)
        response = requests.get(url, headers={'X-Api-Key': os.getenv("API_KEY")})
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "msg": response.text}

    
# for Code Test
# print(sentiment_analysis("I am so happy!"))