from datetime import datetime
class FormulariosDeRecurso():
    """
    Adaptador dos formulários de recurso para Web
    """
    FORMAT_12_HORAS = "%Y/%m/%d %I:%M %p"

    def __init__(self,repositorio):
        self.repositorio = repositorio

    def busca(self,form):
        tipo = None
        intervalos = []
        local,nome,id = (None,None,None)

        if self.repositorio.tipo_por_id(form["categoria"]):
            tipo = form["categoria"]

        try:
            dataInicial = datetime.strptime(form["initialDate"].upper().strip(),self.FORMAT_12_HORAS)
            dataFinal = datetime.strptime(form["finalDate"].upper().strip(),self.FORMAT_12_HORAS)
            intervalo = (dataInicial,dataFinal)
            intervalos.append(intervalo)
            print("Intervalo definido para busca")
        except:
            pass

        try:
            id = form["id"]
        except:
            pass

        try:
            local = form["local"]
        except:
            pass

        try:
            nome = form["nome"]
        except:
            pass

        return (id, nome, tipo, intervalos, local)
