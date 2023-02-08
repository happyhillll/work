import pandas as pd
import requests
import json
import pprint
import time
from tqdm import tqdm

def request(question:str):
    data = json.dumps(obj = {"debug" : 1, "sources" : [question]})
    res = requests.request("POST", "http://convai-irqa-dev.ncsoft.com:32401/api/v1.0/nano_faq/faq_manager/nano", headers={
            'Content-Type': 'application/json'
        }, data = data)
    respond = res.json()
    tags = ""
    if not respond.get("answer"):
        answer = None
        tags = None
    else:
        t_list = respond.get("answer").get("tags")
        for r in t_list:
            tags += r + "/"
        answer = respond.get("answer").get("body")
        tags = tags[:-1]
    return question, answer, tags
if __name__ == "__main__":
    a = pd.read_excel("nano chatbot_(시연용) Test 명세서.xlsx", sheet_name="01_기본 질문")
    questions = a["Question"]
    answers = []
    tags = []
    for i, q in tqdm(enumerate(questions)):
        _, a, tag = request(q)
        print(q, a, tag)
        time.sleep(0.01)
        answers.append(a)
        tags.append(tag)
    data = {'Questions': questions,
    'answers': answers,
    'tags': tags}
    df = pd.DataFrame(data)
    df.to_excel("qs_l.xlsx", sheet_name = 'Sheet1', 
            header = True, 
            index = True, 
            index_label = "id", 
            freeze_panes = (2, 0))
