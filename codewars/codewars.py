1、Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit
 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.
 persistence(4) => 0   # Because 4 is already a one-digit number.

#解答
from functools import reduce

def persistence(n):
    ret = 0
    while len(str(n)) > 1:
        ret = ret + 1
        n = reduce(lambda x,y:int(x)*int(y), str(n))

    return ret
	
2、Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"

#解答
def spin_words(sentence):
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)
	

3、将一个句子中的英文转换为对应的数值，非英文字符跳过。
eg：A/a : 1   B/b : 2 .....
AB : 1 2

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
	
//解释：join表示将列表中的字段连接为字符串。' '.join 表示用空格连接。''.join 表示无间隔连在一起。
	ord()表示将字母转换为对应的ASCII码值。
