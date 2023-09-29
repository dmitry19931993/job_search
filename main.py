import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")
user = os.getenv("USER")

header = {
        "user-agent": user,
        "authorization": f"Bearer {api_key}",
    }

experience = ['noExperience', 'between1And3']
text = ['Python developer', 'Python', 'Django']
schedule = ['remote', None]
area = ["16", None]

def search_for_vacancies(header, experience, text, schedule, area):
    link = "https://api.hh.ru/vacancies"
    values = {
        "experience" : experience,
        "text" : text,
        "enable_snippets" : "true",
        "L_save_area" : "true",
        "order_by" : "publication_time",
        "per_page" : 100,
        "schedule" : schedule,
        "area" : area,
        "period" : 1,
    }
    my_req = requests.get(link, headers=header, data=values)
    date = json.loads(my_req.text)

    with open('my_test_1.json', 'w') as file:
        json.dump(date, file, indent=4)

def about_me(header):
    link = "https://api.hh.ru/me"
    my_req = requests.get(link, headers=header)
    date = json.loads(my_req.text)
    with open('my_test.json', 'w') as file:
        json.dump(date, file, indent=4)

def response_job(header, id):
    link = "https://api.hh.ru/negotiations"
    values = {
        "vacancy_id": id,
        "resume_id": "60dc6d88ff0bd5caf60039ed1f6f7553666675",
        "message": "Добрый день! Окончил курсы Skillbox  по профессии Python разработчик, в данный момент изучаю Django. Этот отклик был отправлен с помощью api.hh, с уважением Дмитрий",
    }
    my_req = requests.post(link, headers=header, data=values)
    print (my_req.status_code)

def main():
    while True:
        data_1 = search_for_vacancies(header=header, experience=experience[0], text=text[0], schedule=schedule[1],
                                      area=area[0])
        for job_req in data_1["items"]:
            response_job(header=header, id=job_req["id"])

        data_2 = search_for_vacancies(header=header, experience=experience[1], text=text[0], schedule=schedule[1],
                                      area=area[0])
        for job_req in data_2["items"]:
            response_job(header=header, id=job_req["id"])

        data_3 = search_for_vacancies(header=header, experience=experience[0], text=text[0], schedule=schedule[0],
                                      area=area[1])
        for job_req in data_3["items"]:
            response_job(header=header, id=job_req["id"])

        data_4 = search_for_vacancies(header=header, experience=experience[1], text=text[0], schedule=schedule[0],
                                      area=area[1])
        for job_req in data_4["items"]:
            response_job(header=header, id=job_req["id"])



if __name__ == "__main__":
    main()