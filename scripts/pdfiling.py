file_ = """<!DOCTYPE html>
<html lang ="pt-br>
<head>

	<meta charset="UTF-8"/>
	<style>

.header {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

h1 {
  font-size: 27px;
  text-align: center;
  font-family: Arial;
}

h2 {
  font-size: 33px;
  text-align: center;
  display: inline-block;
  font-family: Arial;
}

h3 {
  font-size: 27px;
  text-align: center;
  display: inline;
  font-family: Arial;
}

h4 {
  font-size: 27px;
  text-align: center;
  display: inline;
  font-family: Arial;
}

h5 {
  font-size: 27px;
  text-align: center;
  font-family: Arial;
}



.one{
	
	margin: 0 auto;
	display: flex;
	justify-content: center;
    padding: 10px;
}

.two{
	margin: 0 auto;
	display: flex;
	justify-content: center;
    padding: 10px;
}

.three{
	margin: 0 auto;
	display: flex;
	justify-content: center;
    padding: 10px;
}

.table{
	display: block;
	margin-left: auto;
	margin-right: auto;
	width: 1000px;
	height: 600px;

}

.graph{
	display: block;
	margin-left: auto;
	margin-right: auto;
	width: 1400px;
	height: 500px;
}
	
	</style>
	

</head>

<body>
<div id="interface">
			<div>
				<img src="file:///D:/jose/Estatística/images/Cap.png" width="900" height="467" class = "header"/>
				<h1 >RELATÓRIO ESTATÍSTICOS DE CURSOS E RECURSOS UTILIZADOS<br><br><{data}><br><br><br><br><br><br><br><br><br><br><br><br></h1>
			</div>
			<div class = "one">
				<h2>Treinamentos realizados-Fundamentos de Impressão I - 3D Finder </h2>
				<img src="file:///D:/jose/Estatística/images/finder.PNG" class = "finder"/><br><br><br>
				<img src="file:///D:/jose/Estatística/images/Treinamento Semipresencial  - Fundamentos de Impressão 3D_table.png" class = "table"/>
				<img src="file:///D:/jose/Estatística/images/Treinamento Semipresencial  - Fundamentos de Impressão 3D.png" class = "graph"/>

			</div>
			<div class = "two">
				<h3>Treinamentos realizados-Fundamentos de impressao 3D II - Zmorph</h3> 
				<img src="file:///D:/jose/Estatística/images/zmorph.PNG" class = "zmorph"/>
				<tabela>
				<grafico>
			</div>
			<div class = "three">
				<h4>Treinamentos realizados-Gravadora e Cortado Laser</h4> 
				<img src="file:///D:/jose/Estatística/images/cortadora.PNG" class = "laser"/>
				<tabela>
				<grafico>
			</div >
			<div>
				<h5>RESERVAS DE TODOS EQUIPAMENTOS (EM HORAS)<br><{data}></h5>
				
				<tabela>
				<grafico>
			</div>
		</div>
</body>
</html>
"""


if __name__ == "__main__":
    import pdfkit
    options = {'enable-local-file-access': True,
               'encoding': 'UTF-8',
                           'page-size': 'A4',
                           'orientation': 'landscape',
               'dpi': 400}
    pdfkit.from_string(file_, 'filename.pdf', options=options)
