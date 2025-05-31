import requests

def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict/post"
    Input = { "raw_document": { "text": text_to_analyze } }
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json=Input, headers=Headers)
    response_data = response.text
    return response_data.json()
