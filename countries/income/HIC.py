from countries.Countries import Countries


class HIC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = "Andorra, Greece, Poland, Antigua and Barbuda, Greenland, Portugal, Aruba, " \
                                "Guam, Puerto Rico, Australia, Hong Kong, Qatar, Austria, " \
                                "Hungary, San Marino, Bahamas, Iceland, Saudi Arabia, Bahrain, " \
                                "Ireland, Seychelles, Barbados, Isle of Man, Singapore, Belgium, Israel, " \
                                "Sint Maarten, Bermuda, Italy, Slovak Republic, British Virgin Islands, " \
                                "Japan, Slovenia, Brunei Darussalam, South Korea, Republic of Korea, " \
                                "Spain, Canada, Kuwait, Saint Kitts and Nevis, Cayman Islands, Latvia, " \
                                "St. Martin, Channel Islands, Liechtenstein, Sweden, Chile, Lithuania, " \
                                "Switzerland, Croatia, Luxembourg, Taiwan, Curacao, Macao, Trinidad and Tobago, " \
                                "Cyprus, Malta, Turks and Caicos Islands, Czech Republic, Monaco, " \
                                "United Arab Emirates, Denmark, Nauru, United Kingdom, Estonia, " \
                                "Netherlands, United States, Faroe Islands, New Caledonia, Uruguay, " \
                                "Finland, New Zealand, Virgin Islands, France, Northern Mariana Islands, " \
                                "French Polynesia, Norway, Germany, Oman, Gibraltar, Palau"
        self.lst_of_countries = self.lst_of_countries.split(", ")


if __name__ == "__main__":
    a = HIC()
    papers = a.get_all_papers()
    print(len(papers))
    i = 0
    for paper in papers:
        if i == 20:
            break
        i = i + 1
        print(paper)


