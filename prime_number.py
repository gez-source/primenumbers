# Gerallt Franke
# Prime number generator.

from random import randrange

class Primality:
    
    def __init__(self):
        # Primes (including the number 2)
        self.primesLUT = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
                  101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,
                  211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,
                  317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,
                  439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,
                  569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,
                  677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,
                  821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,
                  947,953,967,971,977,983,991,997]


    def primeLUT(self, number):
        if number <= 1 or number == 4:
            return False
        # Check the lookup table.
        #if(number in primesLUT): 
        #    return True
        for prime in self.primesLUT:
            if number == prime:
                return True
            if number % prime == 0:
                return False
        return False
    
    def isPrime(self, number):    
        if number < 1000:
            # Use simple prime number lookup table test.
            return self.primeLUT(number)
        # Use the algorithm.
        return self.isBigPrime(number)
    
    @staticmethod
    def isBigPrime(number):
        i = 997
        while i < number:
            if number % i == 0:
                # A prime always has a remainder, it is only divisible by 1 and itself.
                return False 
            i += 1
        return True
    
def main():
    primality = Primality()
    # Test the code checking if it is correct using the lookup table.
    for n in range(0, 1000):
        if primality.isPrime(n) == True:
            assert primality.primeLUT(n) == True
            print(n)
    
    # Run the algorithm.
    for n in range(0, 1000):
        m = randrange(10 ** 6, 10 ** 7)
        #m = randrange(0, 100)
        if primality.isPrime(m) == True:
            print(m)
            #print(m, isPrime(m))
    
    
main()
