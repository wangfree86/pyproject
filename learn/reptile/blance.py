try:
    file=open('film_name.text','r+')
except Exception as e:
    print(e)
    response = input('do you want to create a new file:')
    if response=='y':
        file=open('film_name.text','w')
    else:
        pass
else:
    file.write('ssss')
    file.close()