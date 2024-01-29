

import os
from datetime import datetime
import win32com.client as win32




if __name__ == '__main__':
	of = os.path.abspath('.').split('\\')[:-1]
	p = '\\'.join(of)
	outlook = win32.Dispatch('outlook.application')
	mail = outlook.CreateItem(0)
	mail.To = "josefilho@unisanta.br"
	mail.Subject = 'Relatório INOVFABLAB' + \
		datetime.now().strftime('%#d %b %Y %H:%M')

	with open(p+'\\teste.html', 'r', encoding='utf-8') as ht:
		html = ht.read() 
	print(html)
	only_png = list(filter(lambda x: x.endswith('.png'), os.listdir(p+'\\images')))
	for o in only_png:
		mail.Attachments.Add(p+'\\images\\'+o)

	mail.HTMLBody = html
	mail.Send()