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
