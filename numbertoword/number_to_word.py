from decimal import Decimal
import math
from currencies import currencies

# Group Levels: 987,654,321.234
# 234 : Group Level -1
# 321 : Group Level 0
# 654 : Group Level 1
# 987 : Group Level 2
class NumberToWord:
    def get_decimal_value(self, decimal_part):
        result = ""
        if self.currency.part_precision != len(decimal_part):
            decimal_part_length = len(decimal_part)
            for i in range(0, self.currency.part_precision - decimal_part_length):
                decimal_part += "0"

            result = f"{decimal_part[0:self.currency.part_precision]}.{decimal_part[self.currency.part_precision:len(decimal_part)]}"

            result = str(round(Decimal(result)))
        else:
            result = decimal_part

        for i in range(0, self.currency.part_precision - len(result)):
            result += "0"

        return result

    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.english_prefix_text = ""
        self.english_suffix_text = "only."
        self.arabic_prefix_text = " فقط"
        self.arabic_suffix_text = "لا غير."

        splits = str(number).split(".")
        self.integer_value = int(splits[0])
        self.decimal_value = 0
        if len(splits) > 1:
            self.decimal_value = int(self.get_decimal_value(splits[1]))

    @staticmethod
    def to_word(number, currency_code, language):
        """
        Convert a numerical value to its word representation in either English or Arabic, 
        formatted with a specified currency.

        Parameters:
        number (float or int): The numerical value to be converted.
        currency_code (str): The code of the currency (e.g., 'USD', 'AED').
        language (str): The language in which the number should be converted ('English' or 'Arabic').

        Returns:
        str: A string representing the number in words with the specified currency 
             in the chosen language. Returns an error message if the language or 
             currency is undefined.

        Example:
        >>> NumberToWord.to_word(135.23, 'SYP', "Arabic")
        'فقط مائة و خمسة و ثلاثون ليرة سورية و ثلاثة و عشرون قرشاً لا غير.'

        Raises:
        TypeError: If the 'number' parameter is not an int or float.        
        """
        if not isinstance(number, (int, float)):
            raise TypeError("The 'number' parameter must be an int or float.")

        if language not in ["English","Arabic"]:
            return "Undefined Language!"

        currency = None 

        for cur in currencies:
            if cur.currency_code == currency_code:
                currency = cur
                break

        if not currency:
            return "Undefined Currency!"

        to_word = NumberToWord(number, currency)

        if language == "English":
            return to_word.convert_to_english()
        elif language == "Arabic":
            return to_word.convert_to_arabic()

    english_ones = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]

    english_tens = [
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]

    english_group = [
        "Hundred",
        "Thousand",
        "Million",
        "Billion",
        "Trillion",
        "Quadrillion",
        "Quintillion",
        "Sextillian",
        "Septillion",
        "Octillion",
        "Nonillion",
        "Decillion",
        "Undecillion",
        "Duodecillion",
        "Tredecillion",
        "Quattuordecillion",
        "Quindecillion",
        "Sexdecillion",
        "Septendecillion",
        "Octodecillion",
        "Novemdecillion",
        "Vigintillion",
        "Unvigintillion",
        "Duovigintillion",
        "10^72",
        "10^75",
        "10^78",
        "10^81",
        "10^84",
        "10^87",
        "Vigintinonillion",
        "10^93",
        "10^96",
        "Duotrigintillion",
        "Trestrigintillion",
    ]

    def process_group(self, group_number):
        tens = group_number % 100
        hundreds = int(group_number / 100)

        ret_val = ""

        if hundreds > 0:
            ret_val = f"{self.english_ones[hundreds]} {self.english_group[0]}"

        if tens > 0:
            if tens < 20:
                ret_val += " " if ret_val != "" else ""
                ret_val += self.english_ones[tens]
            else:
                ones = int(tens % 10)
                tens = int(tens / 10) - 2  # 20's offset

                ret_val += " " if ret_val != "" else ""
                ret_val += self.english_tens[tens]

                if ones > 0:
                    ret_val += " " if ret_val != "" else ""
                    ret_val += self.english_ones[ones]

        return ret_val

    def convert_to_english(self):
        temp_number = self.number

        if temp_number == 0:
            return "Zero"

        decimal_string = self.process_group(self.decimal_value)

        ret_val = ""

        group = 0

        if temp_number < 0:
            self.number = -1 * temp_number
            return self.convert_to_english()
        else:
            while temp_number >= 1:
                number_to_process = int(temp_number % 1000)
                temp_number = temp_number / 1000

                group_description = self.process_group(number_to_process)

                if group_description != "":
                    if group > 0:
                        ret_val = f"{self.english_group[group]} {ret_val}"

                    ret_val = f"{group_description} {ret_val}"

                group += 1

        formatted_number = ""
        formatted_number += f"{self.english_prefix_text} " if self.english_prefix_text != "" else ""
        formatted_number += ret_val if ret_val != "" else ""
        if ret_val != "":
            formatted_number += (
                self.currency.english_currency_name
                if self.integer_value == 1
                else self.currency.english_plural_currency_name
            )
        formatted_number += " and " if decimal_string != "" else ""
        formatted_number += decimal_string if decimal_string != "" else ""
        if decimal_string != "":
            formatted_number += " " + (
                self.currency.english_currency_part_name
                if self.decimal_value == 1
                else self.currency.english_plural_currency_part_name
            )
        formatted_number += f" {self.english_suffix_text}" if self.english_suffix_text != "" else ""

        return formatted_number

    arabic_ones = [
        "",
        "واحد",
        "اثنان",
        "ثلاثة",
        "أربعة",
        "خمسة",
        "ستة",
        "سبعة",
        "ثمانية",
        "تسعة",
        "عشرة",
        "أحد عشر",
        "اثنا عشر",
        "ثلاثة عشر",
        "أربعة عشر",
        "خمسة عشر",
        "ستة عشر",
        "سبعة عشر",
        "ثمانية عشر",
        "تسعة عشر",
    ]

    arabic_feminine_ones = [
        "",
        "إحدى",
        "اثنتان",
        "ثلاث",
        "أربع",
        "خمس",
        "ست",
        "سبع",
        "ثمان",
        "تسع",
        "عشر",
        "إحدى عشرة",
        "اثنتا عشرة",
        "ثلاث عشرة",
        "أربع عشرة",
        "خمس عشرة",
        "ست عشرة",
        "سبع عشرة",
        "ثماني عشرة",
        "تسع عشرة",
    ]

    arabic_tens = [
        "عشرون",
        "ثلاثون",
        "أربعون",
        "خمسون",
        "ستون",
        "سبعون",
        "ثمانون",
        "تسعون",
    ]

    arabic_hundreds = [
        "",
        "مائة",
        "مئتان",
        "ثلاثمائة",
        "أربعمائة",
        "خمسمائة",
        "ستمائة",
        "سبعمائة",
        "ثمانمائة",
        "تسعمائة",
    ]

    arabic_appended_twos = [
        "مئتا",
        "ألفا",
        "مليونا",
        "مليارا",
        "تريليونا",
        "كوادريليونا",
        "كوينتليونا",
        "سكستيليونا",
    ]

    arabic_twos = [
        "مئتان",
        "ألفان",
        "مليونان",
        "ملياران",
        "تريليونان",
        "كوادريليونان",
        "كوينتليونان",
        "سكستيليونان",
    ]

    arabic_group = [
        "مائة",
        "ألف",
        "مليون",
        "مليار",
        "تريليون",
        "كوادريليون",
        "كوينتليون",
        "سكستيليون",
    ]

    arabic_appended_group = [
        "",
        "ألفاً",
        "مليوناً",
        "ملياراً",
        "تريليوناً",
        "كوادريليوناً",
        "كوينتليوناً",
        "سكستيليوناً",
    ]

    arabic_plural_groups = [
        "",
        "آلاف",
        "ملايين",
        "مليارات",
        "تريليونات",
        "كوادريليونات",
        "كوينتليونات",
        "سكستيليونات",
    ]

    def get_digit_feminine_status(self, digit, group_level):
        if group_level == -1:  # if it is in the decimal part
            if self.currency.is_currency_part_name_feminine:
                return self.arabic_feminine_ones[digit]
            else:
                return self.arabic_ones[digit]
        else:
            if group_level == 0:
                if self.currency.is_currency_name_feminine:
                    return self.arabic_feminine_ones[digit]
                else:
                    return self.arabic_ones[digit]
            else:
                return self.arabic_ones[digit]

    def process_arabic_group(self, group_number, group_level, remaining_number):
        tens = group_number % 100
        hundreds = int(group_number / 100)

        ret_val = ""

        if hundreds > 0:
            if tens == 0 and hundreds == 2:  # حالة المضاف
                ret_val = self.arabic_appended_twos[0]
            else:  #  الحالة العادية
                ret_val = self.arabic_hundreds[hundreds]

        if tens > 0:
            if tens < 20:  # if we are processing under 20 numbers
                if (
                    tens == 2 and hundreds == 0 and group_level > 0
                ):  # This is special case for number 2 when it comes alone in the group
                    if (
                        self.integer_value == 2000
                        or self.integer_value == 2000000
                        or self.integer_value == 2000000000
                        or self.integer_value == 2000000000000
                        or self.integer_value == 2000000000000000
                        or self.integer_value == 2000000000000000000
                    ):  #  في حالة الاضافة
                        ret_val = self.arabic_appended_twos[group_level]
                    else:
                        ret_val = self.arabic_twos[group_level]
                else:  # General case
                    if ret_val != "":
                        ret_val += " و "

                    if tens == 1 and group_level > 0 and hundreds == 0:
                        ret_val += " "
                    else:
                        if (
                            (tens == 1 or tens == 2)
                            and (group_level == 0 or group_level == -1)
                            and hundreds == 0
                            and remaining_number == 0
                        ):
                            ret_val += ""  # Special case for 1 and 2 numbers like: ليرة سورية و ليرتان سوريتان
                        else:
                            # Get Feminine status for this digit
                            ret_val += self.get_digit_feminine_status(tens, group_level)
            else:
                ones = tens % 10
                tens = int(tens / 10) - 2  # 20's offset

                if ones > 0:
                    if ret_val != "":
                        ret_val += " و "

                    # Get Feminine status for this digit
                    ret_val += self.get_digit_feminine_status(ones, group_level)

                if ret_val != "":
                    ret_val += " و "

                ret_val += self.arabic_tens[tens]

        return ret_val

    def convert_to_arabic(self):
        temp_number = self.number

        if temp_number == 0:
            return "صفر"

        # Get Text for the decimal part
        decimal_string = self.process_arabic_group(self.decimal_value, -1, 0)

        ret_val = ""
        group = 0

        is_negative_number = False

        if temp_number < 0:
            is_negative_number = True
            temp_number = abs(temp_number)

        while temp_number >= 1:
            # seperate number into groups
            number_to_process = int(temp_number % 1000)

            temp_number = temp_number / 1000

            # convert group into its text
            group_description = self.process_arabic_group(number_to_process, group, math.floor(temp_number))

            if group_description != "":
                # here we add the new converted group to the previous concatenated text
                if group > 0:
                    if ret_val != "":
                        ret_val = f"و {ret_val}"

                    if number_to_process != 2:
                        if number_to_process % 100 != 1:
                            if number_to_process >= 3 and number_to_process <= 10:
                                # for numbers between 3 and 9 we use plural name
                                ret_val = f"{self.arabic_plural_groups[group]} {ret_val}"
                            else:
                                if ret_val != "":
                                    # use appending case
                                    ret_val = f"{self.arabic_appended_group[group]} {ret_val}"
                                else:
                                    ret_val = f"{self.arabic_group[group]} {ret_val}"  # use normal case
                        else:
                            ret_val = f"{self.arabic_group[group]} {ret_val}"

                ret_val = f"{group_description} {ret_val}"

            group += 1

        formatted_number = ""

        formatted_number += f"{self.arabic_prefix_text} " if self.arabic_prefix_text != "" else ""
        formatted_number += " ناقص " if is_negative_number else ""
        formatted_number += ret_val

        abs_integer_value = abs(self.integer_value)

        if abs_integer_value != 0:
            # here we add currency name depending on _intergerValue : 1 ,2 , 3--->10 , 11--->99
            remaining_100 = abs_integer_value % 100

            if remaining_100 == 0:
                formatted_number += self.currency.arabic_1_currency_name
            elif remaining_100 == 1:
                formatted_number += self.currency.arabic_1_currency_name
            elif remaining_100 == 2:
                if abs_integer_value == 2:
                    formatted_number += self.currency.arabic_2_currency_name
                else:
                    formatted_number += self.currency.arabic_1_currency_name
            elif remaining_100 >= 3 and remaining_100 <= 10:
                formatted_number += self.currency.arabic_3_10_currency_name
            elif remaining_100 >= 11 and remaining_100 <= 99:
                formatted_number += self.currency.arabic_11_99_currency_name

        formatted_number += " و " if self.decimal_value != 0 else ""
        formatted_number += decimal_string if self.decimal_value != 0 else ""

        if self.decimal_value != 0:
            # here we add currency part name depending on _intergerValue : 1 ,2 , 3--->10 , 11--->99
            formatted_number += " "

            remaining_100 = self.decimal_value % 100

            if remaining_100 == 0:
                formatted_number += self.currency.arabic_1_currency_part_name
            elif remaining_100 == 1:
                formatted_number += self.currency.arabic_1_currency_part_name
            elif remaining_100 == 2:
                formatted_number += self.currency.arabic_2_currency_part_name
            elif remaining_100 >= 3 and remaining_100 <= 10:
                formatted_number += self.currency.arabic_3_10_currency_part_name
            elif remaining_100 >= 11 and remaining_100 <= 99:
                formatted_number += self.currency.arabic_11_99_currency_part_name

        formatted_number += f" {self.arabic_suffix_text}" if self.arabic_suffix_text != "" else ""

        return formatted_number
