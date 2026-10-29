# Testes do modelo Controle (AR18).
# Executar a partir da raiz do projeto:
#   python -m unittest test_cases.test_controle -v

import dataclasses
import unittest

from models.controle import Controle

CAMPOS = (
    "identificador", "nome", "objetivo", "descricao", "responsavel",
    "frequencia", "evidencias_esperadas", "criterio_avaliacao", "criticidade",
)
CAMPOS_TEXTO = tuple(c for c in CAMPOS if c != "evidencias_esperadas")


def dados_validos(**alteracoes):
    dados = {
        "identificador": "CM-01",
        "nome": "Aprovação de mudanças",
        "objetivo": "Garantir que mudanças sejam autorizadas antes da implantação.",
        "descricao": "Toda mudança em produção exige aprovação registrada.",
        "responsavel": "Gerente de TI",
        "frequencia": "A cada mudança",
        "evidencias_esperadas": ["Ticket aprovado", "Registro de implantação"],
        "criterio_avaliacao": "100% das mudanças amostradas têm aprovação prévia.",
        "criticidade": "Alta",
    }
    dados.update(alteracoes)
    return dados


class TestCriacao(unittest.TestCase):
    def test_cria_controle_valido(self):
        c = Controle(**dados_validos())
        self.assertIsInstance(c, Controle)

    def test_possui_exatamente_os_nove_campos(self):
        nomes = tuple(f.name for f in dataclasses.fields(Controle))
        self.assertEqual(nomes, CAMPOS)
        self.assertEqual(len(nomes), 9)

    def test_campos_preservam_os_valores(self):
        dados = dados_validos()
        c = Controle(**dados)
        for campo in CAMPOS_TEXTO:
            with self.subTest(campo=campo):
                self.assertEqual(getattr(c, campo), dados[campo])
        self.assertEqual(c.evidencias_esperadas, ("Ticket aprovado", "Registro de implantação"))

    def test_textos_nao_sao_alterados(self):
        c = Controle(**dados_validos(nome="  Nome com espaços  "))
        self.assertEqual(c.nome, "  Nome com espaços  ")

    def test_evidencias_em_lista_ou_tupla_viram_tupla(self):
        for entrada in (["E1"], ("E1",)):
            with self.subTest(entrada=entrada):
                c = Controle(**dados_validos(evidencias_esperadas=entrada))
                self.assertEqual(c.evidencias_esperadas, ("E1",))

    def test_e_imutavel(self):
        c = Controle(**dados_validos())
        with self.assertRaises(dataclasses.FrozenInstanceError):
            c.nome = "Outro"

    def test_dois_controles_iguais_sao_iguais(self):
        self.assertEqual(Controle(**dados_validos()), Controle(**dados_validos()))


class TestObrigatorios(unittest.TestCase):
    def test_todos_os_campos_sao_obrigatorios_na_criacao(self):
        for campo in CAMPOS:
            with self.subTest(campo=campo):
                dados = dados_validos()
                del dados[campo]
                with self.assertRaises(TypeError):
                    Controle(**dados)

    def test_textos_vazios_ou_so_espacos(self):
        for campo in CAMPOS_TEXTO:
            for valor in ("", "   ", "\n\t"):
                with self.subTest(campo=campo, valor=valor):
                    with self.assertRaises(ValueError):
                        Controle(**dados_validos(**{campo: valor}))

    def test_evidencias_nao_pode_ser_vazia(self):
        for valor in ([], ()):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Controle(**dados_validos(evidencias_esperadas=valor))


class TestTiposEValoresInvalidos(unittest.TestCase):
    def test_textos_com_tipo_errado(self):
        for campo in CAMPOS_TEXTO:
            for valor in (None, 123, 1.5, ["texto"], b"texto"):
                with self.subTest(campo=campo, valor=valor):
                    with self.assertRaises(ValueError):
                        Controle(**dados_validos(**{campo: valor}))

    def test_evidencias_com_tipo_errado(self):
        for valor in (None, "Ticket aprovado", b"abc", 5, 1.5, True, {"a": 1}.get):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Controle(**dados_validos(evidencias_esperadas=valor))

    def test_evidencias_rejeita_dicionario(self):
        for valor in ({"Ticket aprovado": 1}, {"Ticket aprovado": "Ticket aprovado"}, {}):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Controle(**dados_validos(evidencias_esperadas=valor))

    def test_evidencias_rejeita_conjuntos(self):
        for valor in ({"Ticket aprovado"}, frozenset({"Ticket aprovado"}), set()):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Controle(**dados_validos(evidencias_esperadas=valor))

    def test_evidencias_rejeita_outros_iteraveis(self):
        # Só list e tuple são aceitos: geradores, ranges, etc. são recusados.
        for valor in (iter(["E1"]), (e for e in ["E1"]), range(3), bytearray(b"abc")):
            with self.subTest(valor=type(valor).__name__):
                with self.assertRaises(ValueError):
                    Controle(**dados_validos(evidencias_esperadas=valor))

    def test_evidencias_item_com_espacos_e_quebras_de_linha_e_vazio(self):
        with self.assertRaises(ValueError):
            Controle(**dados_validos(evidencias_esperadas=["Ok", " \n\t "]))

    def test_evidencias_com_item_invalido(self):
        for valor in (["Ok", ""], ["Ok", "  "], ["Ok", 3], ["Ok", None], [["aninhada"]]):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Controle(**dados_validos(evidencias_esperadas=valor))

    def test_nao_ha_lista_fechada_de_criticidade_ou_frequencia(self):
        # Decisão documentada: sem escalas definidas nos requisitos, qualquer
        # texto não vazio é aceito.
        c = Controle(**dados_validos(criticidade="Nível 7", frequencia="Quinzenal"))
        self.assertEqual(c.criticidade, "Nível 7")
        self.assertEqual(c.frequencia, "Quinzenal")


class TestDicionario(unittest.TestCase):
    def test_para_dicionario_tem_as_nove_chaves(self):
        d = Controle(**dados_validos()).para_dicionario()
        self.assertEqual(tuple(d), CAMPOS)

    def test_para_dicionario_valores_e_evidencias_em_lista(self):
        dados = dados_validos()
        d = Controle(**dados).para_dicionario()
        for campo in CAMPOS_TEXTO:
            self.assertEqual(d[campo], dados[campo])
        self.assertIsInstance(d["evidencias_esperadas"], list)
        self.assertEqual(d["evidencias_esperadas"], dados["evidencias_esperadas"])

    def test_de_dicionario_reconstroi(self):
        dados = dados_validos()
        c = Controle.de_dicionario(dados)
        self.assertEqual(c, Controle(**dados))
        self.assertEqual(c.evidencias_esperadas, ("Ticket aprovado", "Registro de implantação"))

    def test_de_dicionario_sem_chave(self):
        for campo in CAMPOS:
            with self.subTest(campo=campo):
                dados = dados_validos()
                del dados[campo]
                with self.assertRaises(KeyError):
                    Controle.de_dicionario(dados)

    def test_de_dicionario_valor_invalido(self):
        with self.assertRaises(ValueError):
            Controle.de_dicionario(dados_validos(nome=""))
        with self.assertRaises(ValueError):
            Controle.de_dicionario(dados_validos(evidencias_esperadas=[]))

    def test_ida_e_volta_preserva_os_dados(self):
        original = Controle(**dados_validos())
        d = original.para_dicionario()
        self.assertEqual(Controle.de_dicionario(d), original)
        self.assertEqual(Controle.de_dicionario(d).para_dicionario(), d)

    def test_alterar_dicionario_nao_altera_o_controle(self):
        c = Controle(**dados_validos())
        d = c.para_dicionario()
        d["evidencias_esperadas"].append("Extra")
        d["nome"] = "Outro"
        self.assertEqual(c.evidencias_esperadas, ("Ticket aprovado", "Registro de implantação"))
        self.assertEqual(c.nome, "Aprovação de mudanças")


if __name__ == "__main__":
    unittest.main()
