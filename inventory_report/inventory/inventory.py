import xml.etree.ElementTree as Et
import csv
import json
from pathlib import Path
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        # https://qastack.com.br/programming/5899497/how-can-i-check-the-extension-of-a-file
        extensao = Path(path).suffix
        metodo_do_report = cls.report_method(report_type)
        arquivo_parsed = cls.read_file_method(extensao, path)
        return metodo_do_report.generate(arquivo_parsed)

    def report_method(report_type):
        if report_type == "completo":
            return CompleteReport
        else:
            return SimpleReport

    def read_file_method(extensao, path):
        if extensao == ".csv":
            return Inventory.read_file_csv(path)

        elif extensao == ".json":
            return Inventory.read_file_json(path)

        elif extensao == ".xml":
            return Inventory.read_file_xml(path)

    def read_file_csv(path):
        with open(path) as file:
            file_content = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(file_content)

    def read_file_json(path):
        with open(path, 'r') as file:
            file_content = json.load(file)
        return file_content

    def read_file_xml(path):
        dom = Et.parse(path)
        records = dom.findall("record")
        # filtro = "*"
        lista = []
        # https://www.youtube.com/watch?v=rFxXDO8-keg 
        # (importante para aprender xml parser!)
        for record in records:
            lista.append({
                "id": record.find("id").text,
                "nome_do_produto": record.find("nome_do_produto").text,
                "nome_da_empresa": record.find("nome_da_empresa").text,
                "data_de_fabricacao": record.find("data_de_fabricacao").text,
                "data_de_validade": record.find("data_de_validade").text,
                "numero_de_serie": record.find("numero_de_serie").text,
                "instrucoes_de_armazenamento": record.find(
                    "instrucoes_de_armazenamento").text
                })

        print(lista)
        return lista
