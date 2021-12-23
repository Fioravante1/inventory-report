from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dict_list):
        report = super().generate(dict_list)
        all_corporates = super().get_all_enterprises(dict_list)
        # stock_corporates = []
        res = ""
        for corporation in all_corporates:
            stock_qtd = super().count_enterprise(corporation, dict_list)
            res += f"- {corporation}: {stock_qtd}\n"

        print(report + "\n" + "Produtos estocados por empresa: \n" + res)

        return report + "\n\n" + "Produtos estocados por empresa: \n" + res
