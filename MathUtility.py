class Frac:
    def __init__(self,numenator,denominator):
        pass
    def multiputive_inverse(self):
        pass
    def additive_inverse(self):
        pass
    def is_mixed_fraction(self):
        pass
    def convert_into_mix_fraction(self):
        pass

class Calc:
    # In any Function of this class numbers arg will always be a list
    @classmethod
    def convInNumber(cls,arrary): # Don't to be used by outside the class
        number = ''
        for num in arrary:
            number = number + str(num)
        number = int(number)
        return number
    
    @classmethod
    def convInArray(cls,number): # Don't to be used by outside the class
        array = []
        for num in str(number):
            array.append(int(num))
        return array   

    @classmethod
    def __increment_pair(cls):
        if cls.index >= cls.length_dividend:
            return False
        cls.current_processing.append(cls.dividend[cls.index])
        cls.current_processing_num = Calc.convInNumber(cls.current_processing)
        cls.index += 1
        return True

    @classmethod
    def divide(cls,dividend,divisor):
        """
        This Function Will Return you reminder,quoitent in minimum processing
        Divisor and Dividend must be positive integer for that
        """
        if dividend < divisor:
            raise ValueError('Dividend is smaller than Divisor')
        cls.dividend = Calc.convInArray(dividend)
        cls.index = 0 # Index Starting from 1 because i have already added one element in current_processing
        quoitent = []
        reminder = []
        cls.current_processing = []
        cls.current_processing_num = 0
        # Suppose we have to divide 124 by 12 then first we make pairs.Current pair will store in this var
        length_dividend = len(cls.dividend)
        cls.length_dividend = length_dividend
        start = True

        while cls.index < length_dividend:
            if start: # Start Divison
                start = False
                while cls.current_processing_num < divisor:
                    cls.__increment_pair()
            else:
                # Without this 122 / 12 (and other same kind) => quoitent = 1 and reminder = 2
                counter = 0
                while cls.current_processing_num < divisor:
                    if not cls.__increment_pair(): # Means I have reached maximum value
                        quoitent.append(0)
                        # Example of this 122/12. If i can't divide it then a divider value then i will just pass it to reminder and a 0 in quoitent
                        break
                    if counter == 0: # Means for first pair i don't have to put 0 in quoitent
                        counter = 1
                    else:
                        quoitent.append(0)
                
            # Just like we read the table for finding part of quoitent I am also doing same thing here down
            cls.current_processing_num = cls.convInNumber(cls.current_processing)
            current_value = divisor
            next_value = 0
            for qoit_part in range(1,10):
                next_value = divisor * (qoit_part + 1)
                if current_value <= cls.current_processing_num and next_value > cls.current_processing_num:
                    quoitent.append(qoit_part)
                    cls.current_processing_num = cls.current_processing_num - current_value
                    cls.current_processing = cls.convInArray(cls.current_processing_num).copy()
                    break
                else:
                    current_value = next_value
            
            # Adding Reminder Value Here
            if cls.index == length_dividend:
                reminder = cls.current_processing.copy()
            
        quoitent = cls.convInNumber(quoitent)
        reminder = cls.convInNumber(reminder)

        return [quoitent,reminder]
        
    @classmethod
    def hcf(cls,numbers):
        pass

    @classmethod
    def lcm(cls,numbers):
        pass

    @classmethod
    def isPrime(cls,numbers):
        pass

    @classmethod
    def is_perfect_square(cls,number):
        pass

    @classmethod
    def square_root(cls,number,decimal_level=2):
        pass

    @classmethod
    def cube_root(cls,number): # Only for perfect cubes
        pass

    @classmethod
    def factor(cls,number):
        pass

    @classmethod 
    def multiples(cls,number,no_of_multiple):
        pass


if __name__ == "__main__":
    test_case = Calc.divide(135,10)
    print(test_case)