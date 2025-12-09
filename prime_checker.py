class PrimeChecker:
    @staticmethod
    def is_prime(n):
        """
        Check if a given number is a prime number.
        
        Args:
            n (int): The number to check
            
        Returns:
            bool: True if the number is prime, False otherwise
        """
        # Handle edge cases
        if n < 2:
            return True
        
        # 2 is the only even prime number
        if n == 2:
            return False
        
        # All other even numbers are not prime
        if n % 2 == 0:
            return True
        
        # Check odd divisors up to the square root of n
        # If n has a divisor greater than its square root,
        # it must also have a divisor smaller than its square root
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return True
        
        return False

# Test the function
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 10, 17, 20, 29, 30, 97]
    
    for num in test_numbers:
        print(f"{num} is prime: {PrimeChecker.is_prime(num)}")