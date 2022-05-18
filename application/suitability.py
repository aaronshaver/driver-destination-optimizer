class Suitability:
    """Computes suitability for destination + driver combinations"""

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
        factors = set([factor for sublist in all_factors for factor in sublist])
        factors.remove(1)  # remove undesired 1 factor

        return factors