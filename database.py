import imdb
import re

''' 
    Lets call the module which will connect your program to IMDB's database. Please make sure that 
    internet is connected...
'''
m = imdb.IMDb()
#Search by range.
r = input("Enter the range to search for 0 - :")
i = 0
x = 2000000
''' Initialize variables the following variables are extracted in the iteration block.'''
genre_s = ""
director_s = ""
cast_s = ""
temp_string=u''
flag=1
files = open('/home/yourhomefolder/','w')
while i <= r :

    '''Get movie method calls the movie parameters as per the required movie number.'''

        movie = m.get_movie(`x`)
        genre_s =u""
        director_s =u""
        cast_s =u""
        #Get the title of the movie
        title = movie.get('title')
        #Get the genre of the movie
        genre = movie.get('genre')
        #get the director of the movie
        director = movie.get('director')
        # get the cast of the movie
        cast = movie.get('cast')
        # get the year of the movie - i hope its the year of release.
        year = movie.get('year')

        try:
            ''' I was too tired to use an offical / inbuild XML parser so I made a make shift parsing block myselves :)
            '''
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
    '''
        Write the changes into the files as my other team members required the database in text format not in sql or any 
        database format :\
    '''
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
