# Testes do modelo Avaliacao (AR17).
# Executar a partir da raiz do projeto:
#   python -m unittest test_cases.test_avaliacao -v

import unittest
from datetime import date, datetime

from models.avaliacao import Avaliacao

PROCESSO = "Gestão de Mudanças (Change Management)"


def dados_validos(**alteracoes):
    """Dados no formato que o formulário já guardava (sem controles)."""
    dados = {
        "nome_avaliacao": "Avaliação 2026",
        "processo": PROCESSO,
        "data_inicial": date(2026, 1, 1),
        "data_final": date(2026, 6, 30),
        "objetivo": "Verificar a prontidão.",
        "escopo": "Área de TI.",
        "descricao_processo": "Mudanças passam por aprovação.",
    }
    dados.update(alteracoes)
    return dados


class TestCriacao(unittest.TestCase):
    def test_cria_com_todos_os_campos(self):
        a = Avaliacao(**dados_validos(controles_selecionados=("C-01", "C-02")))
        self.assertEqual(a.nome_avaliacao, "Avaliação 2026")
        self.assertEqual(a.processo, PROCESSO)
        self.assertEqual(a.data_inicial, date(2026, 1, 1))
        self.assertEqual(a.data_final, date(2026, 6, 30))
        self.assertEqual(a.objetivo, "Verificar a prontidão.")
        self.assertEqual(a.escopo, "Área de TI.")
        self.assertEqual(a.descricao_processo, "Mudanças passam por aprovação.")
        self.assertEqual(a.controles_selecionados, ("C-01", "C-02"))

    def test_opcionais_tem_padrao_vazio(self):
        a = Avaliacao(
            nome_avaliacao="X", processo=PROCESSO,
            data_inicial=date(2026, 1, 1), data_final=date(2026, 1, 2),
        )
        self.assertEqual(a.objetivo, "")
        self.assertEqual(a.escopo, "")
        self.assertEqual(a.descricao_processo, "")
        self.assertEqual(a.controles_selecionados, ())

    def test_datas_iguais_sao_permitidas(self):
        a = Avaliacao(**dados_validos(data_inicial=date(2026, 3, 3), data_final=date(2026, 3, 3)))
        self.assertEqual(a.data_inicial, a.data_final)

    def test_e_imutavel(self):
        a = Avaliacao(**dados_validos())
        with self.assertRaises(Exception):
            a.nome_avaliacao = "Outro"

    def test_controles_em_lista_viram_tupla(self):
        a = Avaliacao(**dados_validos(controles_selecionados=["C-01"]))
        self.assertEqual(a.controles_selecionados, ("C-01",))


class TestObrigatorios(unittest.TestCase):
    def test_nome_vazio_ou_so_espacos(self):
        for nome in ("", "   ", None):
            with self.subTest(nome=nome):
                with self.assertRaises(ValueError):
                    Avaliacao(**dados_validos(nome_avaliacao=nome))

    def test_processo_vazio(self):
        for processo in ("", "  ", None):
            with self.subTest(processo=processo):
                with self.assertRaises(ValueError):
                    Avaliacao(**dados_validos(processo=processo))

    def test_datas_ausentes(self):
        with self.assertRaises(ValueError):
            Avaliacao(**dados_validos(data_inicial=None))
        with self.assertRaises(ValueError):
            Avaliacao(**dados_validos(data_final=None))

    def test_campos_obrigatorios_sem_valor_padrao(self):
        with self.assertRaises(TypeError):
            Avaliacao(nome_avaliacao="X", processo=PROCESSO)


class TestTipos(unittest.TestCase):
    def test_data_inicial_posterior_a_final(self):
        with self.assertRaises(ValueError):
            Avaliacao(**dados_validos(data_inicial=date(2026, 7, 1), data_final=date(2026, 6, 30)))

    def test_datas_devem_ser_date_e_nao_texto_nem_datetime(self):
        for valor in ("2026-01-01", datetime(2026, 1, 1, 10, 0)):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Avaliacao(**dados_validos(data_inicial=valor))

    def test_textos_opcionais_devem_ser_str(self):
        for campo in ("objetivo", "escopo", "descricao_processo"):
            with self.subTest(campo=campo):
                with self.assertRaises(ValueError):
                    Avaliacao(**dados_validos(**{campo: 123}))

    def test_controles_invalidos(self):
        for valor in ("C-01", 5, ("C-01", ""), ("C-01", 3), ("  ",)):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Avaliacao(**dados_validos(controles_selecionados=valor))


class TestCompatibilidadeComFormulario(unittest.TestCase):
    CHAVES_ANTIGAS = {
        "nome_avaliacao", "processo", "data_inicial", "data_final",
        "objetivo", "escopo", "descricao_processo",
    }

    def test_dicionario_tem_chaves_do_formulario_mais_controles(self):
        d = Avaliacao(**dados_validos()).para_dicionario()
        self.assertEqual(set(d), self.CHAVES_ANTIGAS | {"controles_selecionados"})
        self.assertEqual(d["controles_selecionados"], [])

    def test_valores_do_formulario_sao_preservados_sem_alteracao(self):
        dados = dados_validos(objetivo="  texto com espaços  ", escopo="", descricao_processo="a\nb")
        d = Avaliacao(**dados).para_dicionario()
        for chave, valor in dados.items():
            self.assertEqual(d[chave], valor)

    def test_representa_dicionario_antigo_sem_controles(self):
        a = Avaliacao.de_dicionario(dados_validos())
        self.assertEqual(a.controles_selecionados, ())

    def test_ida_e_volta(self):
        original = Avaliacao(**dados_validos(controles_selecionados=("C-01",)))
        self.assertEqual(Avaliacao.de_dicionario(original.para_dicionario()), original)

    def test_de_dicionario_sem_campo_obrigatorio(self):
        dados = dados_validos()
        del dados["processo"]
        with self.assertRaises(KeyError):
            Avaliacao.de_dicionario(dados)


if __name__ == "__main__":
    unittest.main()
