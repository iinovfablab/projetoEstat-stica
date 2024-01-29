file_ = """<!DOCTYPE html>
<html lang ="pt-br">
<head>

	<meta charset="UTF-16"/>
	<link rel="stylesheet" href="D:/jose/Estatística/teste.css">

</head>
	<body style="background-color: gray; margin: 0;">
			<div class="page">
				<div class="horizontalCenterColumn">
					<img src="D:/jose/Estatística/images/Cap.png" width="820" height="467" class = "header"/>
					<h1 >RELATÓRIO ESTATÍSTICOS DE CURSOS E RECURSOS UTILIZADOS</h1>
				</div>
			</div>

			<div class="page">
				<div class="horizontalCenterColumn">
					<div class="horizontalCenterRowTitle">
						<h2>Treinamentos realizados-Fundamentos de Impressão I - 3D Finder </h2>
						<img src="D:/jose/Estatística/images/finder.PNG" class="icon"/>
					</div>
						<img src="D:/jose/Estatística/images/Treinamento Semipresencial  - Fundamentos de Impressão 3D_table.png" class = "table"/>
				</div>
			</div>

			<div class="page" >
				<div class="horizontalCenterColumn">
					<img src="D:/jose/Estatística/images/Treinamento Semipresencial  - Fundamentos de Impressão 3D.png" width="1100px" height="650px"/>
				</div>
			</div>
			<div class="page">
				<div class="horizontalCenterColumn">
					<div class="horizontalCenterRowTitle">
						<h3>Treinamentos realizados-Fundamentos de impressao 3D II - Zmorph</h3> 
						<img src="D:/jose/Estatística/images/zmorph.PNG" class = "zmorph"/>
					</div>
					<tabela>
					<grafico>
				</div>
			</div>

			<div class="page">
				<div class="horizontalCenterColumn">
					<div class="horizontalCenterRowTitle">
						<h4>Treinamentos realizados-Gravadora e Cortado Laser</h4> 
						<img src="D:/jose/Estatística/images/cortadora.PNG" class = "laser"/>
					</div>
					<tabela>
					<grafico>
				</div>
			</div >

			<div class="page">
				<div class="horizontalCenterColumn">
					<div class="horizontalCenterRowTitle">
						<h5>RESERVAS DE TODOS EQUIPAMENTOS (EM HORAS)
							<br>
							<{data}>
						</h5>
					</div>
					
					<tabela>
					<grafico>
				</div>
			</div>

</body>
</html>
"""


if __name__ == "__main__":
	
    import pdfkit
	

    options = {'enable-local-file-access': None,
               'encoding': 'UTF-16',
                           'page-size': 'A4',
                           'orientation': 'landscape',
               			   'dpi': 600,
                        }
    pdfkit.from_file("D:/jose/Estatística/teste.html", 'filename2.pdf', options=options)
	
	

"""
import os
import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtGui import *
import os



def html_to_pdf(html, pdf):
	os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--foo-arg=foo-value --bar-arg=bar-value"
	app = QtWidgets.QApplication(sys.argv)
	page = QtWebEngineWidgets.QWebEnginePage()
	

	def handle_print_finished(filename, status):
		print("finished", filename, status)
		QtWidgets.QApplication.quit()

	def handle_load_finished(status):
		if status:
			page.printToPdf(pdf)

		else:
			print("Failed")
			QtWidgets.QApplication.quit()

	page.pdfPrintingFinished.connect(handle_print_finished)
	page.loadFinished.connect(handle_load_finished)
	page.load(QtCore.QUrl.fromLocalFile(html))
	app.exec_()


if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join("D:\jose\Estatística", "teste.html")
    print(filename)

    html_to_pdf(filename, "test.pdf")
"""