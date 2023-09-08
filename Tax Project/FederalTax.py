class FederalIncomeTax:

    def __init__(self, income):
        self.__income = income
        self.__federal_tax = 0
        self.__tax_limit_1 = 49020
        self.__tax_limit_2 = 98040
        self.__tax_limit_3 = 151978
        self.__tax_limit_4 = 216511
        self.__tax_rate_level_1 = 0.15
        self.__tax_rate_level_2 = 0.205
        self.__tax_rate_level_3 = 0.26
        self.__tax_rate_level_4 = 0.29
        self.__tax_rate_level_5 = 0.33

    def calculate_tax(self):
        if self.__income <= self.__tax_limit_1:
            self.__federal_tax = self.__income * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_2:
            self.__federal_tax = (self.__income - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_3:
            self.__federal_tax = (self.__income - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2\
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income <= self.__tax_limit_4:
            self.__federal_tax = (self.__income - self.__tax_limit_3) * self.__tax_rate_level_4\
                                 + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        elif self.__income > self.__tax_limit_4:
            self.__federal_tax = (self.__income - self.__tax_limit_4) * self.__tax_rate_level_5 \
                                 + (self.__tax_limit_4 - self.__tax_limit_3) * self.__tax_rate_level_4\
                                 + (self.__tax_limit_3 - self.__tax_limit_2) * self.__tax_rate_level_3 \
                                 + (self.__tax_limit_2 - self.__tax_limit_1) * self.__tax_rate_level_2 \
                                 + self.__tax_limit_1 * self.__tax_rate_level_1
        return self.__federal_tax
