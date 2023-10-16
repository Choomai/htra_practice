The last non-zero digit of a factorial can be found using the following recursive formula¹:

### Let D(n) be the last non-zero digit in n!. 

If the tens digit (or second last digit) of n is odd: 

`D(n) = 4 * D(floor(n/5)) * D(Unit digit of n)`

If the tens digit (or second last digit) of n is even:

`D(n) = 6 * D(floor(n/5)) * D(Unit digit of n)`

### For the numbers less than 10, we can easily find the last non-zero digit by first computing n!, then finding the last digit. 

- D(1) = 1
- D(2) = 2
- D(3) = 6
- D(4) = 4
- D(5) = 2
- D(6) = 2
- D(7) = 4
- D(8) = 2
- D(9) = 8

> D(1) to D(9) are assumed to be precomputed¹.

### For example, for n=27 (where the second last digit is even), we calculate:

```python
D(27) = 6 * D( 27 // 5 ) * D(7)

= 6 * D(5) * D(7)

= 6 * 2 * 4 = 48
```

The last non-zero digit is **8**¹.

This formula works because we are asked about the last non-zero digit, so we remove all factors of 5 and an equal number of factors of 2 from n!. After removing these factors, we can reduce the problem from n! to a smaller factorial calculation¹.

> Source: Conversation with Bing, 16/10/2023
>
> (1) Last non-zero digit of a factorial - GeeksforGeeks. https://www.geeksforgeeks.org/last-non-zero-digit-factorial/.
>
> (2) Last non Zero digit of a Factorial - Mathematics Stack Exchange. https://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial.
>
> (3) Last non-zero digit in factorial | Practice | GeeksforGeeks. https://practice.geeksforgeeks.org/problems/last-non-zero-digit-in-factorial5846/1.
>
> (4) Finding the last two non zero digits of a factorial - campusgate. https://www.campusgate.in/2013/10/finding-last-two-non-zero-digits-of.html.
>
> (5) undefined. http://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial.