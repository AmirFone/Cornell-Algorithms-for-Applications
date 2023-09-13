
def find_index(numbers, value):
    """
    Write a function that takes a list and a value, 
    and returns the index of the value in the list. 
    If the value is not in the list, return -1. 
    Do not use the built-in .index() method for this problem.
    """
    for i,num in enumerate(numbers):
        if num == value:
            return i
    else:
        return -1

def categorize_number(n):
    """
    Write a function that categorizes the given number as 'negative', 'zero', or 'positive'.
    """
    if n*-1==-n:
        return 'positive'
    elif n*-1==n:
        return 'negative'
    else:
        return 'zero'

def reverse_list(numbers):
    """
    Write a function that returns the reversed version of a list without using the built-in reverse method.
    """
    n,m=0,len(numbers)-1
    while n<m:
        numbers[n],numbers[m]=numbers[m],numbers[n]
        n+=1
        m-=1
    return numbers

def process_numbers(numbers):
    """
    Write a function that takes a list of numbers. 
    The function should iterate through the list and print each number until it encounters a negative number, 
    at which point it should break out of the loop. If it encounters a zero, it should skip that iteration using the continue statement.
    """
    for num in numbers:
        if num<0:
            break
        elif num==0:
            continue
        else:
            print(num)
    return

def string_lengths(strings):
    """
    Given a list of strings, write a function that returns a dictionary where the keys are the strings and the values are the lengths of those strings.
    """
    results={}
    for string in strings:
        results[string]=len(string)
    return results
def even_values_keys(data):
    """
    Given a dictionary, write a function that returns a list of keys whose values are even numbers.
    """
    results=[]
    for key in data:
        if data[key]%2==0:
            results.append(key)
    return results

def square_evens(numbers):
    """
    Given a list of numbers, use a list comprehension to return a list of squares of even numbers.
    """
    return [num**2 for num in numbers if num%2==0]

def long_strings(strings):
    """
    Given a list of strings, use a list comprehension to return a list of strings that have a length greater than 5.
    """
    return [string for string in strings if len(string)>5]

def convert_to_celsius(fahrenheit_temps):
    """
    Convert a list of temperatures from Fahrenheit to Celsius.
    
    Given a list of temperatures in Fahrenheit, convert each temperature to Celsius. 
    If the temperature is below freezing (32°F or 0°C), append the string "Freezing" 
    to the converted temperature. Otherwise, just return the converted temperature.
    
    Formula for Conversion:
    Celsius = (Fahrenheit - 32) / 1.8

    Example:
    Input: [32, 50, 100, 0, 20]
    Output: ['0.0°C Freezing', '10.0°C', '37.8°C', '-17.8°C Freezing', '-6.7°C Freezing']
    """
    results=[]
    for temp in fahrenheit_temps:
        celsius=(temp-32)/1.8
        if celsius<0:
            results.append(f'{celsius}°C Freezing')
        else:
            results.append(f'{celsius}°C')
    return results



