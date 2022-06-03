class FederalBasicPersonalAmount:
    def __init__(self, income):
        self.__income = income
        self.__basicPersonalAmount = 0
        self.__baseAmount = 12421
        self.__incomeThreshold = 151987
        self.__divider = 64533
        self.__remain = 0
        self.__coefficient = 0
        self.__supplementAmount = 1387
        self.__applicableAmount = 0

    def determineAmount(self):
        if self.__income <= self.__incomeThreshold:
            self.__basicPersonalAmount = 13808
        else:
            self.__remain = self.__income - self.__incomeThreshold
            self.__coefficient = self.__remain / self.__divider
            self.__applicableAmount = self.__coefficient * self.__supplementAmount
            self.__remain = self.__supplementAmount - self.__applicableAmount
            if self.__remain <= 0:
                self.__remain = 0
            self.__basicPersonalAmount = self.__baseAmount + self.__remain
            if self.__basicPersonalAmount > 13808:
                self.__basicPersonalAmount = 13808
        return self.__basicPersonalAmount


class EmployeeInsurance:
    def __init__(self, EIAmount, province):
        self.__EIAmount = EIAmount
        self.__province = province
        self.__maxAmount = 889.54
        self.__maxQBAmount = 664.34
        self.__EIEnter = 0

    def defineMaxAmount(self):
        if self.__province == 'QB':
            if self.__EIAmount >= self.__maxQBAmount:
                self.__EIEnter = self.__maxQBAmount
            else:
                self.__EIEnter = self.__EIAmount
        else:
            if self.__EIAmount >= self.__maxAmount:
                self.__EIEnter = self.__maxAmount
            else:
                self.__EIEnter = self.__EIAmount
        return self.__EIEnter


class CPPContribution:
    def __init__(self, income, CPPAmount):
        self.__income = income
        self.__CPPAmount = CPPAmount
        self.__12MonthMaxCPPEarning = 61600
        self.__12MonthMaxCPPExemption = 3500
        self.__ActualCPPRate = 0.908257
        self.__RequiredBaseCPPRate = 0.0495
        self.__RequiredEnhancedCPPRate = 0.005
        self.__CPPPensionEarning = 0
        self.__EarningSubject = 0
        self.__CPPOverpayment = 0
        self.__Line30800 = 0
        self.__Line22215 = 0
        self.__Line44800 = 0
        self.__Line58240 = 0

    def calCPP(self):
        if self.__income >= self.__12MonthMaxCPPEarning:
            self.__CPPPensionEarning = self.__12MonthMaxCPPEarning
        else:
            self.__CPPPensionEarning = self.__income
        # Line 5
        self.__EarningSubject = self.__CPPPensionEarning - self.__12MonthMaxCPPExemption
        # Line 7
        ActualAmount = self.__CPPAmount * self.__ActualCPPRate
        # Line 8
        ActualEnhance = self.__CPPAmount - ActualAmount
        # Line 9
        RequiredBaseCPP = self.__EarningSubject * self.__RequiredBaseCPPRate
        # Line 10
        RequiredEnhanceCPP = self.__EarningSubject * self.__RequiredEnhancedCPPRate
        # Line 11
        TotalRequiredCPP = RequiredBaseCPP + RequiredEnhanceCPP
        # Line 14
        self.__CPPOverpayment = self.__CPPAmount - TotalRequiredCPP
        if ActualAmount <= RequiredBaseCPP:
            self.__Line30800 = ActualAmount
            self.__Line58240 = ActualAmount
        else:
            self.__Line30800 = RequiredBaseCPP
            self.__Line58240 = RequiredBaseCPP
        if ActualEnhance <= RequiredEnhanceCPP:
            self.__Line22215 = ActualEnhance
        else:
            self.__Line22215 = RequiredEnhanceCPP
        if self.__CPPOverpayment > 0:
            self.__Line44800 = self.__CPPOverpayment
        return self.__Line30800, self.__Line58240, self.__Line22215, self.__Line44800


class FederalTuitionCredit:
    def __init__(self, unusedAmount, tuitionFee, federalTax, deductionTotal):
        self.__unusedAmount = unusedAmount
        self.__tuitionFee = tuitionFee
        self.__federalTax = federalTax
        self.__deductionTotal = deductionTotal
        self.__credit = 0

    def calTuition(self):
        Line11 = self.__federalTax / 0.15
        Line13 = Line11 - self.__deductionTotal
        if Line13 <= self.__unusedAmount:
            self.__credit = Line13
        else:
            self.__credit = self.__unusedAmount
        return self.__credit


class CWB:
    def __init__(self, income, netIncome):
        self.__income = income
        self.__netIncome = netIncome
        self.__basicCWBAmount = 32244
        self.__CWBAmount = 0
        self.__baseAmount = 22944
        self.__maxBenefit = 1395

    def calCWB(self):
        if self.__netIncome < self.__basicCWBAmount:
            Line18 = self.__income - 3000
            Line20 = Line18 * 0.27
            if Line20 > self.__maxBenefit:
                Line22 = self.__maxBenefit
            else:
                Line22 = Line20
            Line25 = self.__netIncome - self.__baseAmount
            Line27 = Line25 * 0.15
            self.__CWBAmount = Line22 - Line27
        else:
            self.__CWBAmount = 0
        return self.__CWBAmount


class LIFTCredit:
    def __init__(self, income, netIncome):
        self.__income = income
        self.__netIncome = netIncome
        self.__credit = 0
        self.__maxCredit = 850
        self.__incomeThreshold = 30000

    def calCredit(self):
        Line5 = self.__income * 0.0505
        if Line5 > self.__maxCredit:
            self.__credit = self.__maxCredit
        else:
            self.__credit = Line5
        Line17 = self.__netIncome - self.__incomeThreshold
        if Line17 <= 0:
            Line17 = 0
        Line19 = Line17 * 0.1
        self.__credit = self.__credit - Line19
        if self.__credit < 0:
            self.__credit = 0
        return self.__credit


class OntarioHealthPremium:
    def __init__(self, netIncome):
        self.__netIncome = netIncome
        self.__OHP = 0

    def calOHP(self):
        if self.__netIncome < 20000:
            self.__OHP = 0
        elif self.__netIncome < 25000:
            self.__OHP = (self.__netIncome - 20000) * 0.06
        elif self.__netIncome < 36000:
            self.__OHP = 300
        elif self.__netIncome < 38500:
            self.__OHP = (self.__netIncome - 36000) * 0.06 + 300
        elif self.__netIncome < 48000:
            self.__OHP = 450
        elif self.__netIncome < 48600:
            self.__OHP = (self.__netIncome - 48000) * 0.25 + 450
        elif self.__netIncome < 72000:
            self.__OHP = 600
        elif self.__netIncome < 72600:
            self.__OHP = (self.__netIncome - 72000) * 0.25 + 600
        elif self.__netIncome < 200000:
            self.__OHP = 750
        elif self.__netIncome < 200600:
            self.__OHP = (self.__netIncome - 200000) * 0.25 + 750
        else:
            self.__OHP = 900
        return self.__OHP


class DonationsAndGifts:
    def __init__(self, netIncome, charities, government, universities, unitedNation):
        self.__netIncome = netIncome
        self.__charities = charities
        self.__government = government
        self.__universities = universities
        self.__unitedNation = unitedNation
        self.__incomeThreshold = 216511
        self.__Line34900 = 0

    def calDonationAndGift(self):
        totalDonation = self.__charities + self.__government + self.__universities + self.__unitedNation
        totalDonationLimit = self.__netIncome * 0.75
        if totalDonation <= totalDonationLimit:
            allowableDonation = totalDonation
        else:
            allowableDonation = totalDonationLimit
        if allowableDonation <= 200:
            Line13 = allowableDonation
        else:
            Line13 = 200
        Line14 = allowableDonation - Line13
        Line19 = self.__netIncome - self.__incomeThreshold
        if Line19 < 0:
            Line19 = 0
        if Line14 <= Line19:
            Line20F = Line14
        else:
            Line20F = Line19
        Line20 = Line20F * 0.33
        Line21 = (Line14 - Line20F) * 0.29
        Line22 = Line13 * 0.15
        self.__Line34900 = Line20 + Line21 + Line22
        return self.__Line34900, Line13, Line14


class NLLITCredit:
    def __init__(self, netIncome):
        self.__netIncome = netIncome
        self.__basicReduction = 862
        self.__baseAmount = 20619
        self.__applicableRate = 0.16

    def cal(self):
        Line94 = self.__netIncome - self.__baseAmount
        Line96 = Line94 * self.__applicableRate
        Line97 = self.__basicReduction - Line96
        if Line97 < 0:
            Line97 = 0
        return Line97


class PELICredit:
    def __init__(self, netIncome, age):
        self.__netIncome = netIncome
        self.__age = age
        self.__basicReduction = 350
        self.__baseAmount = 19000
        self.__applicableRate = 0.05
        self.__ageAmount = 250

    def cal(self):
        if self.__age < 65:
            ageReduction = self.__ageAmount
        else:
            ageReduction = 0
        Line83 = self.__basicReduction + ageReduction
        Line86 = self.__netIncome - self.__baseAmount
        if Line86 < 0:
            Line86 = 0
        Line88 = Line86 * self.__applicableRate
        Line89 = Line83 - Line88
        return Line89


class NSLICredit(NLLITCredit):
    def __init__(self, netIncome):
        NLLITCredit.__init__(self, netIncome)
        self.__basicReduction = 300
        self.__baseAmount = 15000
        self.__applicableRate = 0.05


class NBLICredit(NLLITCredit):
    def __init__(self, netIncome):
        NLLITCredit.__init__(self, netIncome)
        self.__basicReduction = 684
        self.__baseAmount = 17840
        self.__applicableRate = 0.03


class CBTaxCredit(NLLITCredit):
    def __init__(self, netIncome):
        NLLITCredit.__init__(self, netIncome)
        self.__basicReduction = 481
        self.__baseAmount = 21418
        self.__applicableRate = 0.0356
