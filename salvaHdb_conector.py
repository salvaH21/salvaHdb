import subprocess

class SalvaHdb:
    def __init__(self,basededatos):
        self.basededatos = basededatos
    def insert_file(self,coleccion,documento,contenido):
        self.operacion = "insert_file"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido
        comando = '"C:\\Users\\salva\\Documents\\GitHub2\\salvaHdb\\salvaHdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' "'+self.contenido+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            return("OK")
        else:
            return("KO")