import math
class ComplexNumber:
    
    def __init__(self,real=0,imaginary=0):
        
        if (type(real) not in [int, float]) and (type(imaginary) not in [int, float]):
            raise ValueError("Invalid value for real and imaginary part")
        else:
            if type(real) not in [int, float]:
                raise ValueError("Invalid value for real part")
            elif type(imaginary) not in [int, float]:
                raise ValueError("Invalid value for imaginary part")
            else:
                self.real_part=real
                self.imaginary_part=imaginary
        
    def __str__(self):
        if self.imaginary_part >= 0:
            return "{}+{}i".format(self.real_part,self.imaginary_part)
        else:
            return "{}{}i".format(self.real_part,self.imaginary_part)
        
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
     
        
    def __add__(self,other):
        return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
    
    def __sub__(self,other):
        return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
    
    def __mul__(self,other):
        return ComplexNumber((self.real_part*other.real_part)-(self.imaginary_part*other.imaginary_part),(self.real_part*other.imaginary_part)+(self.imaginary_part*other.real_part))  
    
    def __truediv__(self,other):
        a,b,c,d=self.real_part,self.imaginary_part,other.real_part,other.imaginary_part
        real_1=(((a*c)+(b*d))/((math.pow(c,2))+(math.pow(d,2))))
        imaginary_1=(((b*c)-(a*d))/((math.pow(c,2))+(math.pow(d,2))))
        return ComplexNumber(real_1,imaginary_1)
    
    def __abs__(self):
        absolute=round(math.sqrt(math.pow(self.real_part,2)+math.pow(self.imaginary_part,2)),3)
        return absolute
    
    def __eq__(self,other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part
        
        

"""

Your ComplexNumber class should represent the complex numbers.
Real and imaginary parts should be either integers or floats.

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> one_plus_two_i.real_part
1
>>> one_plus_two_i.imaginary_part
2

>>> from complex_number import ComplexNumber
>>> one = ComplexNumber(1)
>>> one.real_part
1
>>> one.imaginary_part
0

>>> from complex_number import ComplexNumber
>>> zero = ComplexNumber()
>>> zero.real_part
0
>>> zero.imaginary_part
0

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber("1", 2)
ValueError: Invalid value for real part

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,"2")
ValueError: Invalid value for imaginary part

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber("1","2")
ValueError: Invalid value for real and imaginary part

Task 2: Print

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> print(one_plus_two_i)
1+2i
Task 3: Conjugate

Your ComplexNumber class should contain conjugate method that return conjugate of the complex_number

Example for conjugate:
Conjugate for complex number 1 + 2i is 1 - 2i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> one_minus_two_i = one_plus_two_i.conjugate()
>>> print(one_plus_two_i)
1+2i
>>> print(one_minus_two_i)
1-2i
Task 4: Addition

When adding complex number instances using + operator it should return a complex number object

Example for addition:
1 + 2i + 2 + 3i = 3 + 5i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> three_plus_four_i = ComplexNumber(3,4)
>>> four_plus_six_i = one_plus_two_i + three_plus_four_i
>>> print(four_plus_six_i)
4+6i
Task 5: Subtraction

When subtracting complex number instance using - operator it should return a complex number object.

Example for Subtraction
2 + 2i - 1 + 1i = 1 + 1i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> three_plus_four_i = ComplexNumber(3,4)
>>> two_plus_two_i = three_plus_four_i - one_plus_two_i
>>> print(two_plus_two_i)
2+2i
Task 6: Multiplication

When multiplying complex number instances using * operator, it should return multiplication of complex number instances
Example for Multiplication
1+2i * 3+4i = -5+10i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> three_plus_four_i = ComplexNumber(3,4)
>>> minus_five_plus_ten_i = one_plus_two_i * three_plus_four_i
>>> print(minus_five_plus_ten_i)
-5+10i
Task 7: Division

When dividing two complex number instances using / operator, it should return a complex number object.

Example for Division
1+2i / 3+4i = -0.44+0.08i

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> three_plus_four_i = ComplexNumber(3,4)
>>> point_four_four_plus_point_zero_eight_i = one_plus_two_i / three_plus_four_i
>>> print(point_four_four_plus_point_zero_eight_i)
0.44+0.8i
>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> zero = ComplexNumber()
>>> one_plus_two_i / zero
ZeroDivisionError: division by zero
Task 8: Absolute

Your ComplexNumber class should return absolute of the complex number

Example for Absolute
absolute of 1+2i is 2.236 ( sqrt(1 ^2 + 2 ^2) )

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> one_plus_two_i = ComplexNumber(1,2)
>>> absolute_value = abs(one_plus_two_i)
>>> absolute_value
2.236

Task 9: Equality

When comparing complex number instances using ==, it should return True when instances are equal otherwise return False

Your code is expected to behave as below

>>> from complex_number import ComplexNumber
>>> Complex(1,2) == ComplexNumber(1,2)
True
>>> Complex(2,1) == ComplexNumber(1,2)
False




"""