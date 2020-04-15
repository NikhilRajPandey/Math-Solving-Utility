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
    def convInFloat(cls,arrary):
        number = ''
        for num in arrary:
            number = number + str(num)
        number = float(number)
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
    def divide(cls,dividend,divisor,decimal_level=0):
        """
        This Function Will Return you reminder,quoitent in minimum processing
        Divisor and Dividend must be positive integer for that
        """
        if dividend < divisor:
            raise ValueError('Dividend is smaller than Divisor')
        if divisor == 0:
            raise ValueError('Divisor is smaller than 1')
        if divisor == 1:
            return [dividend,0]
        if divisor == dividend:
            return [1,0]
        cls.dividend = Calc.convInArray(dividend)
        cls.index = 0 # Index Starting from 1 because i have already added one element in current_processing
        quoitent = []
        reminder = []
        cls.current_processing = []
        cls.current_processing_num = 0
        # Suppose we have to divide 124 by 12 then first we make pairs.Current pair will store in this var
        cls.length_dividend = len(cls.dividend)
        start = True
        added_decimal = False
        while cls.index < cls.length_dividend:
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
            # print(cls.current_processing)
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
            if cls.index == cls.length_dividend:
                reminder = cls.current_processing.copy()
                if cls.convInNumber(reminder) != 0 and decimal_level != 0 and not added_decimal: # This means i have to also count decimal values
                    cls.length_dividend += decimal_level
                    quoitent.append('.')
                    for _ in range(decimal_level): cls.dividend.append(0)
                    added_decimal = True

        reminder = cls.convInNumber(reminder)
        if decimal_level != 0:
            quoitent = cls.convInFloat(quoitent)
        else:
            quoitent = cls.convInNumber(quoitent)

        return [quoitent,reminder]
        
    @classmethod
    def hcf(cls,numbers):
        numbers.sort()
        while len(numbers) != 1: # This will work when we have to find hcf of more than 2
            divide = Calc.divide(numbers[1],numbers[0]) # This Euclid's division algorithm
            answer = numbers[0]
            while divide[1] != 0:
                # print(True)
                answer = divide[1]
                divide = Calc.divide(numbers[0],divide[1])
            del numbers[0:1] 
            """ Removing two numbers and adding 1 hcf of both of them"""
            numbers[0] = answer
        return numbers[0]

    @classmethod
    def lcm(cls,numbers):
        all_number_product = 1
        for num in numbers:
            all_number_product = all_number_product * num
        # lcm(a1,a2,a...) * hcf(a1,a2,a...) = a1*a2*a...
        return cls.divide(all_number_product,cls.hcf(numbers))[0]

    @classmethod
    def isPrime(cls,number):
        if number <= 1: return False
        if number == 2 or number == 3: return True
        """
        All Prime Numbers can be represent in the form of 6n + 1 or 6n - 1 except 2 and 3 and numbers like 289,343 and 49 means square or cube of any prime no
        Source: https://www.quora.com/Why-do-prime-numbers-always-satisfy-the-6n+1-and-6n-1-conditions-Is-there-mathematical-logic-behind-it
        """
        if ((number + 1) % 6) == 0 or ((number - 1) % 6) == 0:
            return True
        return False

    @classmethod
    def is_perfect_square(cls,number):
        pass

    @classmethod
    def square_root(cls,number,decimal_level=0):
        """
        This Function will return you aproximate square root and 
        """
        # This method is not prime factorisation
        number_array = []
        counter_ = len(str(number))
        # Slicing the number four square root
        if counter_ % 2 == 0:
            while counter_ > 0:
                number_array.append(str(number)[(counter_-2):counter_])
                counter_ = counter_ - 2
        elif counter_ % 2 == 1:
            while counter_ > 0:
                if counter_ == 1:
                    number_array.append(str(number)[(counter_-1):counter_]) # I am adding number in number_arry from backward
                    counter_ = counter_ - 1
                else:
                    number_array.append(str(number)[(counter_-2):counter_])
                    counter_ = counter_ - 2
        # Main rooting Process here
        number_array = number_array[::-1] # Reversing the number array becuase ^^ line force me to do

        result_array = []
        calc_int = "" # Later i will convert this into integer
        index = 0
        reminder = 0 # By Default I am writing reminder 0 just a garbage value
        decimal_calculated = False
        leng_num_array = len(number_array)
        while index < leng_num_array:
            current_num = str(number_array[index])
            root_part = int(str(calc_int) + "1")

            while int(current_num) < root_part:
                result_array.append(0)
                if not(index + 1 <leng_num_array) and not decimal_calculated and decimal_level !=0:
                    result_array.append('.')
                    leng_num_array = leng_num_array + decimal_level
                    for _ in range(decimal_level): number_array.append("00")
                    decimal_calculated = True
                    index = index + 1
                if index + 1 < leng_num_array: # Like For numbers like 26
                    current_num += str(number_array[index+1])
                    index = index + 1
                    reminder = int(current_num)
                else: # For numbers like 100
                    break
                calc_int = str(calc_int) + '0'
                root_part = int(str(calc_int) + "1")

            current_num = int(current_num)
            # Root part and future root part are for avoid repetation of same calculations
            for num in range(1,10):
                str_num = str(num)
                calc_int = str(calc_int)
                future_root_part = ((int(calc_int + str_num) + 1) * (num + 1))
                if root_part <= current_num and future_root_part > current_num:
                    result_array.append(num)
                    calc_int += str_num # Calc int is like divisor
                    calc_int = int(calc_int) + num
                    reminder = current_num - root_part
                    if index + 1 < leng_num_array:
                        old_num = number_array[index+1]
                        number_array[index+1] = int(str(reminder) + str(old_num))
                    break
                root_part = future_root_part

            if not(index + 1 <leng_num_array) and reminder != 0 and not decimal_calculated and decimal_level !=0:
                result_array.append('.') # Adding Decimal Places
                leng_num_array = leng_num_array + decimal_level
                for _ in range(decimal_level): number_array.append("00")
                decimal_calculated = True
                old_num = number_array[index+1]
                number_array[index+1] = int(str(reminder) + str(old_num))
            index = index + 1

        if decimal_level != 0:
            return [cls.convInFloat(result_array),reminder]        
        return [cls.convInNumber(result_array),reminder]

    @classmethod
    def cube_root(cls,number): # Only for perfect cubes
        pass

    @classmethod
    def factors(cls,number):
        return_list = []
        # Cls.square_root_number function will return nearest square root Exp. sqrt(226) = 15
        print(cls.square_root(number))
        for num in range(1,number+1):
            # any number larget factor is smaller than sqrt(x) + 1
            if cls.divide(number,num)[1] == 0:
                return_list.append(num)
        return return_list
            
    @classmethod 
    def multiples(cls,number,no_of_multiple):
        return_list = []
        for num in range(1,no_of_multiple+1):
            return_list.append(number*num)
        return return_list

    @classmethod
    def isDecimal(cls,number):
        number_in_float = float(number)
        number = int(number)
        if number_in_float > number:
            return True
        return False


if __name__ == "__main__":
    # test_case = Calc.divide(12,0)
    # print(test_case)
    # test_case_2 = Calc.isPrime(289)
    # print(test_case_2)
    # print(Calc.isDecimal(4.56))
    # print(Calc.convInNumber(Calc.square_root(987)))
    # print(Calc.convInFloat(['1']))
    # print(Calc.hcf([21,6,9]))
    # print(Calc.hcf([16,8,24,28,18]))
    # print(Calc.multiples(5,6))
    # print(Calc.square_root(316))
    # print(Calc.factors(225))
    print(Calc.square_root(112,decimal_level=3))
    
