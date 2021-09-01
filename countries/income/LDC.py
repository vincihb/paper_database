from countries.Countries import Countries


class LDC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = "Afghanistan, Guinea-Bissau, Somalia, Burkina Faso, " \
                                "Democratic People's Republic Korea, South Sudan, Burundi, Liberia, Sudan, " \
                                "Central African Republic, Madagascar, Syrian Arab Republic, Chad, Malawi, " \
                                "Togo, Democratic Republic of Congo, Mali, Uganda, Eritrea, " \
                                "Mozambique, Republic of Yemen, Yemen, Ethiopia, Niger, " \
                                "Gambia, Rwanda, Guinea, Sierra Leone"
        self.lst_of_countries = self.lst_of_countries.split(", ")


if __name__ == "__main__":
    a = LDC()
    papers = a.get_all_papers()
    print(len(papers))



