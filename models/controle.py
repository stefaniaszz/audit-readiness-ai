# Modelo de dados de um controle avaliável (AR18).
#
# Descreve UM controle que o sistema poderá avaliar. Este arquivo só descreve
# e valida os dados: não há interface (Streamlit), banco de dados, biblioteca
# de controles nem IA. Segue o mesmo padrão de models/avaliacao.py.

from dataclasses import dataclass


@dataclass(frozen=True)
class Controle:
    """Um controle avaliável.

    frozen=True deixa o objeto imutável: para mudar algo, cria-se outro controle.

    Todos os nove campos são obrigatórios (o cartão da AR18 diz que cada
    controle "deverá possuir" todos eles) e não têm valor padrão.
    Textos não podem ser vazios (só espaços conta como vazio).

    Decisão sobre frequência e criticidade: os requisitos do projeto ainda não
    definem escalas (por exemplo, "Alta/Média/Baixa" ou "Mensal/Anual"). Por
    isso os dois campos são texto livre não vazio, sem lista fechada de valores.
    Quando a escala for definida, a validação poderá ser restringida.
    """

    identificador: str  # identifica unicamente o controle (ex.: "CM-01")
    nome: str
    objetivo: str  # finalidade do controle
    descricao: str  # detalhamento do controle
    responsavel: str  # pessoa ou função responsável
    frequencia: str  # periodicidade de execução ou aplicação
    # Evidências que demonstram a execução ou a efetividade do controle.
    # Tupla (imutável) de textos; precisa ter ao menos uma evidência.
    evidencias_esperadas: tuple[str, ...]
    criterio_avaliacao: str  # regra ou parâmetro usado para avaliar
    criticidade: str  # nível de criticidade atribuído

    def __post_init__(self):
        for rotulo, valor in (
            ("identificador", self.identificador),
            ("nome", self.nome),
            ("objetivo", self.objetivo),
            ("descricao", self.descricao),
            ("responsavel", self.responsavel),
            ("frequencia", self.frequencia),
            ("criterio_avaliacao", self.criterio_avaliacao),
            ("criticidade", self.criticidade),
        ):
            if not isinstance(valor, str) or not valor.strip():
                raise ValueError(f"O campo {rotulo} é obrigatório e deve ser um texto não vazio.")

        # Aceita SOMENTE list ou tuple na entrada, mas guarda sempre como tupla.
        # Qualquer outro tipo é recusado: texto e bytes (senão cada letra ou byte
        # viraria uma evidência), dicionário e conjunto (não têm ordem de
        # evidências garantida e um dicionário só contribuiria com as chaves),
        # números, None etc.
        if not isinstance(self.evidencias_esperadas, (list, tuple)):
            raise ValueError("As evidências esperadas devem ser uma lista ou uma tupla de textos.")
        evidencias = tuple(self.evidencias_esperadas)
        if not evidencias:
            raise ValueError("Informe ao menos uma evidência esperada.")
        if not all(isinstance(e, str) and e.strip() for e in evidencias):
            raise ValueError("Cada evidência esperada deve ser um texto não vazio.")
        # Em dataclass imutável, usa-se object.__setattr__ para normalizar.
        object.__setattr__(self, "evidencias_esperadas", evidencias)

    def para_dicionario(self) -> dict:
        """Dicionário com os nove campos (evidências como lista)."""
        return {
            "identificador": self.identificador,
            "nome": self.nome,
            "objetivo": self.objetivo,
            "descricao": self.descricao,
            "responsavel": self.responsavel,
            "frequencia": self.frequencia,
            "evidencias_esperadas": list(self.evidencias_esperadas),
            "criterio_avaliacao": self.criterio_avaliacao,
            "criticidade": self.criticidade,
        }

    @classmethod
    def de_dicionario(cls, dados: dict) -> "Controle":
        """Cria o controle a partir de um dicionário no formato de para_dicionario().

        Falta de chave gera KeyError; valor inválido gera ValueError.
        """
        return cls(
            identificador=dados["identificador"],
            nome=dados["nome"],
            objetivo=dados["objetivo"],
            descricao=dados["descricao"],
            responsavel=dados["responsavel"],
            frequencia=dados["frequencia"],
            evidencias_esperadas=dados["evidencias_esperadas"],
            criterio_avaliacao=dados["criterio_avaliacao"],
            criticidade=dados["criticidade"],
        )
