name = input('Please Enter Your Name:- ')
age = int(input('Please Enter Your Age:- '))
# We can use these both type of statement.
# if age >18 and (name[0] =='a' or name[0] =='A'):
lower_name = name.lower()
if age > 18 and lower_name[0]== 'a':
    print('you are eligible to watch this movie. ')
else:
    print('Oh you are not eligible to watch this Movie. ')