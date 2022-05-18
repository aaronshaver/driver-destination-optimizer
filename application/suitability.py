class Suitability:
    """Computes suitability for destination + driver combinations"""

    vowels = {'a', 'e', 'i', 'o', 'u'}
    VOWEL_MULTIPLIER = 1.5
    CONSONANT_MULTIPLIER = 1
    COMMON_FACTORS_MULTIPLIER = 1.5

    def get_factors(number):
        """
        -Returns all factors of a number except 1
        -Algorithm used is more efficient than naive solution: appends pairs of
        factors up to square root of source number for fewer iterations; this
        works because we will have seen higher factors before reaching the
        square root point by way of num // i
        """
        all_factors = []
        for i in range(1, int(number ** 0.5) + 1):
            if number % i == 0:
                all_factors.append([i, number // i])
        # list comprehension flattens list
        factors = set(
            [factor for sublist in all_factors for factor in sublist])
        factors.remove(1)  # remove undesired 1 factor

        return factors

    def get_vowel_count(name):
        """Returns integer of count of number of vowels in string"""
        return len([x for x in name if x.lower() in Suitability.vowels])

    def get_consonant_count(name):
        """Returns integer of count of number of vowels in string"""
        name_no_spaces = name.replace(' ', '')
        return len(
            [x for x in name_no_spaces if x.lower() not in Suitability.vowels]
        )

    def calculate_suitability(driver, destination):
        suitability = None

        if destination.is_even:
            suitability = driver.vowel_count * Suitability.VOWEL_MULTIPLIER
        else:
            suitability = driver.consonant_count * \
                Suitability.CONSONANT_MULTIPLIER

        if len(driver.factors.intersection(destination.factors)) > 0:
            suitability *= Suitability.COMMON_FACTORS_MULTIPLIER

        if not suitability:
            raise Exception(
                "Suitabilty score remained null after calculations")

        return suitability
