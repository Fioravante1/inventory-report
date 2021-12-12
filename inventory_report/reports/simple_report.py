from datetime import date


class SimpleReport:
    def next_date(dict_list):
        today = date.today().strftime('%Y-%m-%d')
        return today

    def older_product(dict_list):
        date_list = []

        for current_date in dict_list:
            date_list.append(current_date["data_de_fabricacao"])

        return date_list

    def high_stock(dict_list):
        return dict_list

    def generate(dict_list):
        old_product = min(SimpleReport.older_product(dict_list))
        print(SimpleReport.next_date(dict_list), 'estou')
        first_line = (
            f"Data de fabricação mais antiga: {old_product}"
            )
        return first_line
