# Modelo de dados de uma avaliação de auditoria.
#
# Reúne em um só lugar as informações coletadas no formulário "Nova Auditoria".
# Este arquivo só descreve e valida os dados: não tem interface (Streamlit),
# banco de dados nem IA. Os nomes dos campos são os mesmos já usados em
# st.session_state["nova_auditoria"], para que o formulário continue compatível.

from dataclasses import dataclass
from datetime import date, datetime


@dataclass(frozen=True)
class Avaliacao:
    """Uma avaliação de auditoria preparatória.

    frozen=True deixa o objeto imutável: depois de criado, os valores não mudam
    por engano (para alterar algo, cria-se uma nova avaliação).

    Campos obrigatórios (as mesmas regras do formulário):
      - nome_avaliacao: texto não vazio (só espaços conta como vazio);
      - processo: texto não vazio;
      - data_inicial e data_final: datas; a inicial não pode ser posterior à
        final (datas iguais são permitidas).

    Campos opcionais (começam vazios):
      - objetivo, escopo e descricao_processo: textos livres;
      - controles_selecionados: veja a observação abaixo.
    """

    # Obrigatórios
    nome_avaliacao: str
    processo: str
    data_inicial: date
    data_final: date

    # Opcionais
    objetivo: str = ""
    escopo: str = ""
    descricao_processo: str = ""

    # Controles selecionados: ainda NÃO existe biblioteca nem seleção de
    # controles no projeto (item previsto para uma tarefa futura). Por isso o
    # modelo apenas reserva o espaço: uma tupla de identificadores (textos) de
    # controles, vazia por padrão. A tupla é imutável, combinando com
    # frozen=True. Quando a biblioteca existir, este tipo poderá ser revisto.
    controles_selecionados: tuple[str, ...] = ()

    def __post_init__(self):
        # Rede de segurança: o formulário já mostra mensagens específicas ao
        # usuário; aqui o modelo garante que nunca exista uma avaliação inválida.
        if not isinstance(self.nome_avaliacao, str) or not self.nome_avaliacao.strip():
            raise ValueError("O nome da avaliação é obrigatório.")
        if not isinstance(self.processo, str) or not self.processo.strip():
            raise ValueError("O processo avaliado é obrigatório.")

        for rotulo, valor in (
            ("data inicial", self.data_inicial),
            ("data final", self.data_final),
        ):
            # datetime é um tipo de date; recusamos para guardar só a data.
            if not isinstance(valor, date) or isinstance(valor, datetime):
                raise ValueError(f"A {rotulo} é obrigatória e deve ser uma data.")

        if self.data_inicial > self.data_final:
            raise ValueError("A data inicial não pode ser posterior à data final.")

        for rotulo, valor in (
            ("objetivo", self.objetivo),
            ("escopo", self.escopo),
            ("descricao_processo", self.descricao_processo),
        ):
            if not isinstance(valor, str):
                raise ValueError(f"O campo {rotulo} deve ser um texto.")

        # Aceita lista ou tupla na entrada, mas guarda sempre como tupla.
        if isinstance(self.controles_selecionados, str) or not hasattr(
            self.controles_selecionados, "__iter__"
        ):
            raise ValueError("Os controles selecionados devem ser uma sequência de textos.")
        controles = tuple(self.controles_selecionados)
        if not all(isinstance(c, str) and c.strip() for c in controles):
            raise ValueError("Cada controle selecionado deve ser um texto não vazio.")
        # Em dataclass imutável, usa-se object.__setattr__ para normalizar.
        object.__setattr__(self, "controles_selecionados", controles)

    def para_dicionario(self) -> dict:
        """Dicionário no formato guardado em st.session_state["nova_auditoria"].

        Tem as mesmas chaves que o formulário já usava, mais
        "controles_selecionados" (lista, vazia por enquanto).
        """
        return {
            "nome_avaliacao": self.nome_avaliacao,
            "processo": self.processo,
            "data_inicial": self.data_inicial,
            "data_final": self.data_final,
            "objetivo": self.objetivo,
            "escopo": self.escopo,
            "descricao_processo": self.descricao_processo,
            "controles_selecionados": list(self.controles_selecionados),
        }

    @classmethod
    def de_dicionario(cls, dados: dict) -> "Avaliacao":
        """Cria a avaliação a partir de um dicionário no formato do formulário.

        Aceita também o dicionário antigo, sem "controles_selecionados".
        """
        return cls(
            nome_avaliacao=dados["nome_avaliacao"],
            processo=dados["processo"],
            data_inicial=dados["data_inicial"],
            data_final=dados["data_final"],
            objetivo=dados.get("objetivo", ""),
            escopo=dados.get("escopo", ""),
            descricao_processo=dados.get("descricao_processo", ""),
            controles_selecionados=dados.get("controles_selecionados", ()),
        )
