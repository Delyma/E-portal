class EvenChecker:
    @staticmethod
    def is_even(n):
        """
        Check if a given number is even.

        Args:
            n (int): The number to check

        Returns:
            bool: True if the number is even, False otherwise
        """
        return n % 2 == 0

# Test the function
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 10, 17, 20, 29, 30, 97]
    for num in test_numbers:
        print(f"{num} is even: {EvenChecker.is_even(num)}")
