'''
* @author: Mirza-Younus-Baig
 * @date: 13/01/2019
 '''
#Reverse of a string
#The same string will be used for palindrome check.

string = input('Enter the string. ')

print("The reverse of the string is ", ''.join(list(reversed(string))))

if string == string[::-1]:
         print('Palindrome')
else:
         print('Not a  palindrome')
