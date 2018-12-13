import re
import csv

def remove_cs(sentence):
	try:
		cs = re.search(r'\d+\/CS',sentence).group()
		sentence = sentence.replace(cs, '')
		return sentence
	except AttributeError:
		return sentence

def look_for_ct_dash(sentence):
	para = '()'
	try:
		ct_dash = re.search(r'\(.*?\)',sentence).group()
		get_ct = re.search(r'CT', ct_dash).group()
		if get_ct:
			ct_dash = ct_dash.replace('(','')
			ct_dash = ct_dash.replace(')','')
			sentence = sentence.replace(ct_dash, '')
			sentence = sentence.replace(para, '')
			num = ct_dash.replace('CT','')
			return [sentence,num,1,'each']
	except AttributeError:
		return sentence
		
def get_brand(sentence):
	name = re.search(r'[A-Za-z]*',sentence).group()
	return name
		
def get_oz(sentence):
	try:
		oz = re.search(r'\d+.?\d+?\s?oz',sentence[0]).group()
		sentence[0] = sentence[0].replace(oz, '')
		num = '({0})'.format(oz)
		sentence[0] = sentence[0] + num
		return sentence
	except AttributeError:
		return sentence

def stabilize(data):
	data = data.replace(' -', '')
	return [data, 1, 1, "each"]
		
def add_data(id, des, name, rest):
	unique_array.append(id)
	unique_array.append(des)
	unique_array.append(name)
	for item in rest:
		unique_array.append(item)
		
def search_csv():
	with open('data.csv', encoding='utf8') as f:  #use when can't decode
		x = csv.reader(f)
		with open('new.csv', 'w') as e:
			y = csv.writer(e)
			y.writerow(next(x, None))
			y.writerow(next(x, None))
			y.writerow(next(x, None))
			y.writerow(next(x, None))
			y.writerow(next(x, None))
			y.writerow(next(x, None))
			for line in x:
				if line != '':
					id = line[0]
					sentence = line[1]
					name = get_brand(sentence)
					rm = remove_cs(sentence)
					ex = look_for_ct_dash(rm)
					oun = get_oz(ex)
					if type(oun) == str:
						data = stabilize(oun)
						y.writerow([id, line[1], name, data[0],data[1],data[2],data[3]])
					if type(oun) == list:
						y.writerow([id, line[1], name, oun[0],oun[1],oun[2],oun[3]])
		
search_csv()
		