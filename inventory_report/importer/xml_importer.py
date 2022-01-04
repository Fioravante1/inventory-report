from inventory_report.importer.importer import Importer
from pathlib import Path
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        extensao = Path(path).suffix
        if ".xml" != extensao:
            raise ValueError('Arquivo inválido')
        else:
            return Inventory.read_file_xml(path)
