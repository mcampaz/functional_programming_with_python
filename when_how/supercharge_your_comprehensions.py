Conditionals are important because they allow list comprehensions to filter out unwanted values, which would normally require a call to filter():

>>>
>>> sentence = 'the rocket came back from mars'
>>> vowels = [i for i in sentence if i in 'aeiou']
>>> vowels
['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']


If you need a more complex filter, then you can even move the conditional logic to a separate function:

>>>
>>> sentence = 'The rocket, who was named Ted, came back \
... from Mars because he missed his friends.'
>>> def is_consonant(letter):
...     vowels = 'aeiou'
...     return letter.isalpha() and letter.lower() not in vowels
>>> consonants = [i for i in sentence if is_consonant(i)]
['T', 'h', 'r', 'c', 'k', 't', 'w', 'h', 'w', 's', 'n', 'm', 'd', \
'T', 'd', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'M', 'r', 's', 'b', \
'c', 's', 'h', 'm', 's', 's', 'd', 'h', 's', 'f', 'r', 'n', 'd', 's']


For example, if you have a list of prices, then you may want to replace negative prices with 0 and leave the positive values unchanged:

>>>
>>> original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
>>> prices = [i if i > 0 else 0 for i in original_prices]
>>> prices
[1.25, 0, 10.22, 3.78, 0, 1.16]


If this seems overwhelming, then it may be helpful to view the conditional logic as its own function:

>>>
>>> def get_price(price):
...     return price if price > 0 else 0
>>> prices = [get_price(i) for i in original_prices]
>>> prices
[1.25, 0, 10.22, 3.78, 0, 1.16]


You can create a set comprehension by using curly braces instead of brackets:

>>> quote = "life, uh, finds a way"
>>> unique_vowels = {i for i in quote if i in 'aeiou'}
>>> unique_vowels
{'a', 'e', 'u', 'i'}


Dictionary comprehensions are similar, with the additional requirement of defining a key:

>>> squares = {i: i * i for i in range(10)}
>>> squares
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


The following example shows how this is possible, using get_weather_data() to generate fake weather data:

>>>
>>> import random
>>> def get_weather_data():
...     return random.randrange(90, 110)
>>> hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
>>> hot_temps
[107, 102, 109, 104, 107, 109, 108, 101, 104]