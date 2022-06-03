class FederalAgeAmount:
    def __init__(self, age, income):
        self.__age = age
        self.__income = income
        self.__ageAmount = 0
        self.__maximumAmount = 7713
        self.__incomeThreshold = 38893
        self.__applicableRate = 0.15
        self.__maxIncome = 74960
        self.__remain = 0

    def determineAmount(self):
        if self.__age >= 65:
            if self.__income <= self.__incomeThreshold:
                self.__ageAmount = self.__maximumAmount
            elif self.__income >= self.__maxIncome:
                self.__ageAmount = 0
            else:
                self.__remain = self.__income - self.__incomeThreshold
                self.__remain = self.__remain * self.__applicableRate
                self.__ageAmount = self.__maximumAmount - self.__remain
        else:
            self.__ageAmount = 0
        return self.__ageAmount


class ONAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 5312
        self.__incomeThreshold = 39546
        self.__applicableRate = 0.15
        self.__maxIncome = 74960
        self.__remain = 0


class ABAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 5397
        self.__incomeThreshold = 40179
        self.__applicableRate = 0.15
        self.__maxIncome = 76159
        self.__remain = 0


class BCAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 4964
        self.__incomeThreshold = 36954
        self.__applicableRate = 0.15
        self.__maxIncome = 70048
        self.__remain = 0


class MBAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 3728
        self.__incomeThreshold = 27749
        self.__applicableRate = 0.15
        self.__maxIncome = 52602
        self.__remain = 0


class NBAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 5158
        self.__incomeThreshold = 38400
        self.__applicableRate = 0.15
        self.__maxIncome = 72787
        self.__remain = 0


class NLAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 6087
        self.__incomeThreshold = 33359
        self.__applicableRate = 0.15
        self.__maxIncome = 73939
        self.__remain = 0


class NSAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 8481
        self.__incomeThreshold = 25000
        self.__applicableRate = 0.06
        self.__maxIncome = 75000
        self.__remain = 0


class NTAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 7456
        self.__incomeThreshold = 38893
        self.__applicableRate = 0.15
        self.__maxIncome = 88600
        self.__remain = 0


class NUAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 10512
        self.__incomeThreshold = 38893
        self.__applicableRate = 0.15
        self.__maxIncome = 108973
        self.__remain = 0


class PEAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 3764
        self.__incomeThreshold = 28019
        self.__applicableRate = 0.15
        self.__maxIncome = 53112
        self.__remain = 0


class SKAgeAmount(FederalAgeAmount):
    def __init__(self, age, income):
        FederalAgeAmount.__init__(self, age, income)
        self.__ageAmount = 0
        self.__maximumAmount = 4942
        self.__incomeThreshold = 36794
        self.__applicableRate = 0.15
        self.__maxIncome = 69741
        self.__remain = 0
