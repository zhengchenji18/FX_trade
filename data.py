import requests

def get_data(date):
	date_str = date.strftime('%Y-%m-%d 00:00:00')
	req_str = f'http://localhost:5000/get_rates?date={date_str}'
	r = requests.get(req_str)

	if r.status_code == 200:
		return r.json()
	else:
		return []