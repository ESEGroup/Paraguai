from difflib import SequenceMatcher
from itertools import product
from domain import RepositorioRecurso, Recurso, TipoRecurso, IntervaloDeTempo, Agendamento

class RepositorioRecursoEmMemoria(RepositorioRecurso):
    def __init__(self):
        listaTipos = [(0,"Sala"),(1,"Projetor"),(2,"Microscópio")]
        self.listaTipoRecurso = [TipoRecurso(id = identificador, nome = recurso) for (identificador,recurso) in listaTipos ]
        self.recursos = []
        # Mudar depois
        self.mockar_recursos()

    def mockar_recursos(self):
        recursos_iniciais = [("Sala H-201",0,"Fundão,CT,Bloco H"),
                             ("Sala H-204",0,"Fundão,CT,Bloco H"),
                             ("Projetor AB-Z",1,"Fundão,CT,Sala D-201"),
                             ("Projetor AB-X",1,"Fundão,CCMN,Sala F-102"),
                             ("Microscópio XYZ",2,"Fundão,CCMN,Sala F201")]
        qtd_recursos = len(self.recursos)
        for index,(nome,tipo,local) in enumerate(recursos_iniciais):
            id = qtd_recursos + index + 1
            novoRecurso = Recurso(nome, self.tipo_por_id(tipo), local)
            novoRecurso.id = id
            self.recursos.append(novoRecurso)


        ag = []
        natal = IntervaloDeTempo('2016-12-24 00:00','2016-12-26 00:00')
        agNatal = Agendamento(natal)
        ag.append(agNatal)
        recursoComAgendamento = Recurso("Projetor Natalino",self.tipo_por_id(1),"Fundão,CCMN,Sala D-201",ag)
        id = len(self.recursos) + 1
        recursoComAgendamento.id = id
        self.recursos.append(recursoComAgendamento)

    def criarOuSalvar(self, recurso):
        if recurso.id:
            recursoAlterado = self.obter(recurso.id)
            if recursoAlterado:
                self.recursos[recursoAlterado.id - 1] = recurso
            return recurso
        return self.criar(recurso)

    def criar(self, recurso):
        recurso.id = len(self.recursos) + 1
        self.recursos.append(recurso)
        return recurso

    def remover(self, RecursoID):
        try:
            del self.recursos[RecursoID - 1]
            return True
        except:
            return False

    def obter(self, identificador):
        print("BUSCA POR ID -> ",identificador)
        try:
            return self.recursos[int(identificador)-1]
        except:
            return None

    def buscar(self, recursoFiltro):
        if recursoFiltro.id:
            return self.obter(recursoFiltro.id)

        iter_recursos = iter(self.recursos)
        # Filtro por tipo
        print("Filtrando recursos com o tipo:", recursoFiltro.tipo.id)
        iter_recursos = (
                        r
                        for r
                        in iter_recursos
                        if r.tipo == recursoFiltro.tipo
                        )
        # Busca por nome
        if recursoFiltro.nome:
            iter_recursos = (
                             r
                             for r
                             in iter_recursos
                             if SequenceMatcher(None, r.nome, recursoFiltro.nome).ratio() > 0.5
                             )
        # Filtro por localização
        if recursoFiltro.localizacao:
            print("Filtro por local -> ", recursoFiltro.localizacao)
            iter_recursos = (
                             r
                             for r
                             in iter_recursos
                             #if SequenceMatcher(None, r.localizacao.split(','), recursoFiltro.localizacao.split(',')).ratio() > 0.51
                             if self.proximidade(r.localizacao, recursoFiltro.localizacao) > 0.6
                            )

        # Filtro por disponibilidade de agendamento
        if recursoFiltro.agendamentos:
            print("Filtro por agendamento -> ", len(recursoFiltro.agendamentos), " agendamentos desejados" )
            iter_recursos = (r for r in iter_recursos
                # Pega apenas os recursos cujo número de agendamentos sobrepostos seja 0
                if
                    [x for (x,y) in product(recursoFiltro.agendamentos,r.agendamentos) if not x.intervalo.intercede(y.intervalo)]
                or not r.agendamentos
                )

        return list(iter_recursos)

    def proximidade(self,lugar1,lugar2):
        l1 = lugar1.split(',')
        l2 = lugar2.split(',')
        taxa = 1
        for index,lugar in enumerate(l2):
            if len(l1) == index:
                break
            taxa = taxa * SequenceMatcher(None, lugar.strip(), l1[index].strip()).ratio()
        return taxa

    def todos(self):
        return self.recursos

    def metadados(self):
        return { "tipos" : self.listaTipoRecurso }

    def tipo_por_id(self,id):
        for tipo in self.listaTipoRecurso:
            if str(tipo.id) == str(id):
                return tipo
        print("TipoRecurso não existente ->", id)
        return None

