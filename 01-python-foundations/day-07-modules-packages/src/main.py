#import calculator

#result = calculator.add(10,20)

#print(result)

#from calculator import add,sub
#result = add(18,23)
#print(result)

#print(sub(23))

from calculator import add, multiply
from text_utils import clean_text, count_words


def main():
    print("Addition:", add(10, 20))
    print("Multiplication:", multiply(5, 4))

    text = "   Generative    AI is powerful.   "

    cleaned = clean_text(text)

    print("Cleaned text:", cleaned)
    print("Word count:", count_words(cleaned))


if __name__ == "__main__":
    main()