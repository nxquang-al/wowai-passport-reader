from datetime import datetime

class Postprocessor:
	def __init__(self):
		return
	
	def __call__(self, info):
		for key in info.keys():
			if isinstance(info[key], str):
				info[key] = info[key].replace('<', '')
		idx = info['names'].find('  ')
		if idx != -1:
			info['names'] = info['names'][0:idx]
		
		try:
			info['date_of_birth'] = self.convert_datetime(info['date_of_birth'])
			info['expiration_date'] = self.convert_datetime(info['expiration_date'])
		except Exception:
			raise Exception("Invalid information")

		return info

	def convert_datetime(self, date):
		try:
			if len(date) != 6 or not date.isdigit():
				raise Exception("Invalid datetime")
			date = datetime.strptime(date, '%y%m%d')
			return date.strftime('%d-%m-%y')
		except Exception:
			return date