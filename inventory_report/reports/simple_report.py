from datetime import date


class SimpleReport():
    # posso sobreescrever
    @classmethod
    def generate(cls, dict_list):

        old_product = min(SimpleReport.older_product(dict_list))
        expiration_date = SimpleReport.closest_expiration_date(dict_list)
        enterprise_name = SimpleReport.high_stock(dict_list)
        one_line = (
            f"Data de fabricação mais antiga: {old_product}"
            )
        two_line = (
            f"Data de validade mais próxima: {expiration_date}"
        )
        three_line = (
            f"""Empresa com maior quantidade de produtos estocados: {
                enterprise_name["nome_da_empresa"]
                }"""
            )
        print(f"{one_line}\n{two_line}\n{three_line}\n", "estou aqui")
        return f"{one_line}\n{two_line}\n{three_line}\n"

    @staticmethod
    # Não posso sobreescrever (Não recebe cls - classe como parametro não é
    # necessário
    def count_enterprise(enterprise_name, dict_list):
        value = 0
        for enterprise in dict_list:
            if enterprise["nome_da_empresa"] == enterprise_name:
                value += 1

        return value

    @staticmethod
    def closest_expiration_date(dict_list):
        date_list = []
        today = date.today()
        for current_date in dict_list:
            date_list.append(
                date.fromisoformat(
                    current_date["data_de_validade"]
                                        )
                        )
        # https://stackoverflow.com/questions/32237862/find-the-closest-date-to-a-given-date
        date_validate = min(item for item in date_list if item > today)
        return date_validate

    @staticmethod
    def older_product(dict_list):
        date_list = []

        for current_date in dict_list:
            date_list.append(current_date["data_de_fabricacao"])

        return date_list

    @staticmethod
    def high_stock(dict_list):
        enterprises_stock_value = []
        # Não entendi porque não posso fazer um set direto no
        # enterprises_stock_value
        for enterprise in dict_list:
            stock_value = 0
            stock_value = SimpleReport.count_enterprise(
                enterprise["nome_da_empresa"], dict_list
                )
            enterprises_stock_value.append(
                {"nome_da_empresa": enterprise["nome_da_empresa"],
                    "valor_objetos_estocados": stock_value})
        # https://raccoon.ninja/pt/dev-pt/ordenar-lista-de-dicionarios-pelos-valores-das-chaves-python/
        ordenados = sorted(
            enterprises_stock_value, key=lambda k: k['valor_objetos_estocados']
            )
        return ordenados[len(ordenados) - 1]

    @staticmethod
    def get_all_enterprises(dict_list):
        # Consulta no repositório de leticia galvão:
        # Como inicialmente usei set(), por algum motivo a ordenação não batia
        # e como teste não cobra ordenação não passava!
        # Esse texto deve ser usado como feedback construtivo, ordenação ajuda,
        # por conta dessa diferença!
        # https://github.com/tryber/sd-010-b-inventory-report/pull/42/files#diff-1d75405432f767847d4d9acc877893c0a29992bad3d9b5b86b20dafec609a179R43
        enterprises = []
        for corporation in dict_list:
            if corporation["nome_da_empresa"] not in enterprises:
                enterprises.append(corporation["nome_da_empresa"])
        return enterprises
