class NLTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__newfoundland_tax = 0
        self.__tax_limit_1 = 38081
        self.__tax_limit_2 = self.__tax_limit_1 + 38080
        self.__tax_limit_3 = self.__tax_limit_2 + 59812
        self.__tax_limit_4 = self.__tax_limit_3 + 54390
        self.__tax_rate_level_1 = 0.087
        self.__tax_rate_level_2 = 0.145
        self.__tax_rate_level_3 = 0.158
        self.__tax_rate_level_4 = 0.173
        self.__tax_rate_level_5 = 0.183

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__newfoundland_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__newfoundland_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__newfoundland_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                      + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_4:
            self.__newfoundland_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                      + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                      + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_4:
            self.__newfoundland_tax = (self.__income - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                      + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                      + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                      + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__newfoundland_tax


class PETax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__princeEdward_tax = 0
        self.__tax_limit_1 = 31984
        self.__tax_limit_2 = self.__tax_limit_1 + 31985
        self.__tax_rate_level_1 = 0.098
        self.__tax_rate_level_2 = 0.138
        self.__tax_rate_level_3 = 0.167

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__princeEdward_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__princeEdward_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_2:
            self.__princeEdward_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                      + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1

        return self.__princeEdward_tax


class NSTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__novaScotia_tax = 0
        self.__tax_limit_1 = 29590
        self.__tax_limit_2 = self.__tax_limit_1 + 29590
        self.__tax_limit_3 = self.__tax_limit_2 + 33820
        self.__tax_limit_4 = self.__tax_limit_3 + 57000
        self.__tax_rate_level_1 = 0.0879
        self.__tax_rate_level_2 = 0.1495
        self.__tax_rate_level_3 = 0.1667
        self.__tax_rate_level_4 = 0.175
        self.__tax_rate_level_5 = 0.21

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__novaScotia_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__novaScotia_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                    + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__novaScotia_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                    + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                    + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_4:
            self.__novaScotia_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                    + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                    + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                    + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_4:
            self.__novaScotia_tax = (self.__income - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                    + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                    + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                    + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                    + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__novaScotia_tax


class NBTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__newBrunswick_tax = 0
        self.__tax_limit_1 = 43835
        self.__tax_limit_2 = self.__tax_limit_1 + 43836
        self.__tax_limit_3 = self.__tax_limit_2 + 54863
        self.__tax_limit_4 = self.__tax_limit_3 + 19849
        self.__tax_rate_level_1 = 0.0968
        self.__tax_rate_level_2 = 0.1482
        self.__tax_rate_level_3 = 0.1652
        self.__tax_rate_level_4 = 0.1784
        self.__tax_rate_level_5 = 0.203

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__newBrunswick_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__newBrunswick_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__newBrunswick_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                      + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_4:
            self.__newBrunswick_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                      + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                      + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_4:
            self.__newBrunswick_tax = (self.__income - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                      + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                      + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                      + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__newBrunswick_tax


class ONTax:
    def __init__(self, netIncome):
        self.__netIncome = netIncome
        self.__ontario_tax = 0
        self.__tax_limit_1 = 45142
        self.__tax_limit_2 = self.__tax_limit_1 + 45145
        self.__tax_limit_3 = self.__tax_limit_2 + 59713
        self.__tax_limit_4 = self.__tax_limit_3 + 70000
        self.__tax_rate_level_1 = 0.0505
        self.__tax_rate_level_2 = 0.0915
        self.__tax_rate_level_3 = 0.1116
        self.__tax_rate_level_4 = 0.1216
        self.__tax_rate_level_5 = 0.1316

    def calculate_tax(self):
        if self.__netIncome <= self.__tax_limit_1:
            self.__ontario_tax = self.__netIncome * self.__tax_rate_level_1
        elif self.__netIncome <= self.__tax_limit_2:
            self.__ontario_tax = (self.__netIncome - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__netIncome <= self.__tax_limit_3:
            self.__ontario_tax = (self.__netIncome - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__netIncome <= self.__tax_limit_4:
            self.__ontario_tax = (self.__netIncome - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                 + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__netIncome > self.__tax_limit_4:
            self.__ontario_tax = (self.__netIncome - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                 + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                 + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__ontario_tax


class MBTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__manitoba_tax = 0
        self.__tax_limit_1 = 33723
        self.__tax_limit_2 = self.__tax_limit_1 + 39162
        self.__tax_rate_level_1 = 0.108
        self.__tax_rate_level_2 = 0.1275
        self.__tax_rate_level_3 = 0.174

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__manitoba_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__manitoba_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                  + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_2:
            self.__manitoba_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                  + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                  + self.__tax_limit_1 * self.__tax_rate_level_1

        return self.__manitoba_tax


class SKTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__saskatchewan_tax = 0
        self.__tax_limit_1 = 45677
        self.__tax_limit_2 = self.__tax_limit_1 + 84829
        self.__tax_rate_level_1 = 0.105
        self.__tax_rate_level_2 = 0.125
        self.__tax_rate_level_3 = 0.145

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__saskatchewan_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__saskatchewan_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_2:
            self.__saskatchewan_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                      + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                      + self.__tax_limit_1 * self.__tax_rate_level_1

        return self.__saskatchewan_tax


class ABTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__alberta_tax = 0
        self.__tax_limit_1 = 131220
        self.__tax_limit_2 = self.__tax_limit_1 + 26244
        self.__tax_limit_3 = self.__tax_limit_2 + 52488
        self.__tax_limit_4 = self.__tax_limit_3 + 104976
        self.__tax_rate_level_1 = 0.10
        self.__tax_rate_level_2 = 0.12
        self.__tax_rate_level_3 = 0.13
        self.__tax_rate_level_4 = 0.14
        self.__tax_rate_level_5 = 0.15

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__alberta_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__alberta_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__alberta_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_4:
            self.__alberta_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                 + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_4:
            self.__alberta_tax = (self.__income - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                 + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                 + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__alberta_tax


class BCTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__britishColumbia_tax = 0
        self.__tax_limit_1 = 42184
        self.__tax_limit_2 = self.__tax_limit_1 + 42185
        self.__tax_limit_3 = self.__tax_limit_2 + 12497
        self.__tax_limit_4 = self.__tax_limit_3 + 20757
        self.__tax_limit_5 = self.__tax_limit_4 + 41860
        self.__tax_limit_6 = self.__tax_limit_5 + 62937
        self.__tax_rate_level_1 = 0.0506
        self.__tax_rate_level_2 = 0.077
        self.__tax_rate_level_3 = 0.105
        self.__tax_rate_level_4 = 0.1229
        self.__tax_rate_level_5 = 0.147
        self.__tax_rate_level_6 = 0.168
        self.__tax_rate_level_7 = 0.205

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__britishColumbia_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__britishColumbia_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                         + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__britishColumbia_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                         + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                         + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_4:
            self.__britishColumbia_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                         + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                         + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                         + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_5:
            self.__britishColumbia_tax = (self.__income - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                         + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                         + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                         + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                         + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_6:
            self.__britishColumbia_tax = (self.__income - self.__tax_limit_5) * self.__tax_rate_level_6 \
                                         + (self.__tax_limit_5 - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                         + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                         + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                         + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                         + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_6:
            self.__britishColumbia_tax = (self.__income - self.__tax_limit_6) * self.__tax_rate_level_7 \
                                         + (self.__tax_limit_6 - self.__tax_limit_5) * self.__tax_rate_level_6 \
                                         + (self.__tax_limit_5 - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                         + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                         + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                         + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                         + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__britishColumbia_tax


class YTTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__yukon_tax = 0
        self.__tax_limit_1 = 49020
        self.__tax_limit_2 = self.__tax_limit_1 + 49020
        self.__tax_limit_3 = self.__tax_limit_2 + 53938
        self.__tax_limit_4 = self.__tax_limit_3 + 348022
        self.__tax_rate_level_1 = 0.064
        self.__tax_rate_level_2 = 0.09
        self.__tax_rate_level_3 = 0.109
        self.__tax_rate_level_4 = 0.128
        self.__tax_rate_level_5 = 0.15

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__yukon_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__yukon_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                               + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__yukon_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                               + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                               + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_4:
            self.__yukon_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4 \
                               + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                               + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                               + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_4:
            self.__yukon_tax = (self.__income - self.__tax_limit_4) * self.__tax_rate_level_5 \
                               + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4 \
                               + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                               + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                               + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__yukon_tax


class NTTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__northwest_tax = 0
        self.__tax_limit_1 = 44396
        self.__tax_limit_2 = self.__tax_limit_1 + 44400
        self.__tax_limit_3 = self.__tax_limit_2 + 55566
        self.__tax_rate_level_1 = 0.059
        self.__tax_rate_level_2 = 0.086
        self.__tax_rate_level_3 = 0.122
        self.__tax_rate_level_4 = 0.1405

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__northwest_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__northwest_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                   + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__northwest_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                   + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                   + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_3:
            self.__northwest_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                   + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                   + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                   + self.__tax_limit_1 * self.__tax_rate_level_1

        return self.__northwest_tax


class NUTax:
    def __init__(self, netIncome):
        self.__income = netIncome
        self.__nunavut_tax = 0
        self.__tax_limit_1 = 46740
        self.__tax_limit_2 = self.__tax_limit_1 + 46740
        self.__tax_limit_3 = self.__tax_limit_2 + 58498
        self.__tax_rate_level_1 = 0.04
        self.__tax_rate_level_2 = 0.07
        self.__tax_rate_level_3 = 0.09
        self.__tax_rate_level_4 = 0.115

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__nunavut_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__nunavut_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__nunavut_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_3:
            self.__nunavut_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4 \
                                 + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__nunavut_tax
