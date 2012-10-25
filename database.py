import imdb
import re

m = imdb.IMDb()
r = input("Enter the range to search for 0 - :")
i = 0
x = 2000000
genre_s = ""
director_s = ""
cast_s = ""
temp_string=u''
flag=1
files = open('/home/iamrock/Desktop/database.txt','w')
while i <= r :

    #try:

        movie = m.get_movie(`x`)
        genre_s =u""
        director_s =u""
        cast_s =u""
        
        title = movie.get('title')
        genre = movie.get('genre')
        director = movie.get('director')
        cast = movie.get('cast')
        year = movie.get('year')

        try:
            for j in genre:
                j = `j`
                j = j[j.find('_')+1:]
                j = j[0:j.find('_')]
                genre_s = genre_s + j
        
        except:
            genre_s='null'
            flag = 0

        print '<'
        print `x`


        
        print genre

        try:
            for j in director:
                j = `j`
                j = j[j.find('_')+1:]
                j = j[0:j.find('_')]
                director_s = director_s + `j`
        except:
            director_s = "null"
            flag = 0
            
        print director_s
        

        try :
            for j in cast:
                j = `j`
                j = j[j.find('_')+1:]
                j = j[0:j.find('_')]
                cast_s = cast_s + `j`
        except:
            cast_s = 'null'
            flag = 0
    
        print cast_s

        print year

        print '>'

        if flag:
                i = i + 1
                files.write('\n\n!#(')
                files.write(`x`)
                files.write(',"')
                files.write(genre_s)
                files.write('","')
                files.write(director_s)
                files.write('","')
                files.write(cast_s)
                files.write('",')
                files.write(`year`)
                files.write(');!!')
                print "no error this ones done well n good" + `i`
        else :
                print 'error : null values rejecting this id ...'
        x = x + 1
        flag = 1
files.close()
