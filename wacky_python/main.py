db: dict[int,str] = {'0':'Bob', '1':'Alice'}

user_selection: int = 3

if user := db.get(user_selection):
    print(user)
else:
    print('User not found')


# There is same example but without walrus operator
user_selection: int = 3
user: str | None = db.get(user_selection)
if user is not None:
    print(user)
else:
    print('User not found')

# Another example of using walrus operator
def analyse_text(text: str) -> dict[str,str|float|list[str]]:
    return {'words' : (words := text.split()),
            'word_count' : (word_count := len(words)),
            'average_word_length' : (sum(len(word) for word in words) / word_count)}

print(analyse_text('Hello world'))
