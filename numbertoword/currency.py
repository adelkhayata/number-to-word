class Currency:
    def __init__(
        self, currency_id, currency_code=None, currency_a_name=None, currency_e_name=None,
        is_currency_name_feminine=None, english_currency_name=None,
        english_plural_currency_name=None, arabic_1_currency_name=None, arabic_2_currency_name=None,
        arabic_3_10_currency_name=None, arabic_11_99_currency_name=None, part_precision=None,
        is_currency_part_name_feminine=None, english_currency_part_name=None, english_plural_currency_part_name=None,
        arabic_1_currency_part_name=None, arabic_2_currency_part_name=None, arabic_3_10_currency_part_name=None,
        arabic_11_99_currency_part_name=None
    ):
        self.currency_id = currency_id
        self.currency_code = currency_code
        self.currency_a_name = currency_a_name
        self.currency_e_name = currency_e_name
        self.is_currency_name_feminine = is_currency_name_feminine
        self.english_currency_name = english_currency_name
        self.english_plural_currency_name = english_plural_currency_name
        self.arabic_1_currency_name = arabic_1_currency_name
        self.arabic_2_currency_name = arabic_2_currency_name
        self.arabic_3_10_currency_name = arabic_3_10_currency_name
        self.arabic_11_99_currency_name = arabic_11_99_currency_name
        self.part_precision = part_precision
        self.is_currency_part_name_feminine = is_currency_part_name_feminine
        self.english_currency_part_name = english_currency_part_name
        self.english_plural_currency_part_name = english_plural_currency_part_name
        self.arabic_1_currency_part_name = arabic_1_currency_part_name
        self.arabic_2_currency_part_name = arabic_2_currency_part_name
        self.arabic_3_10_currency_part_name = arabic_3_10_currency_part_name
        self.arabic_11_99_currency_part_name = arabic_11_99_currency_part_name

    def __str__(self):
        return str(self.currency_e_name)
