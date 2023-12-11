from requests import post

url = 'http://127.0.0.1:5001/predict'

json = {
    '' : ''
}

r = post(url, json=json)


print(r.status_code)