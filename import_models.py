import pandas as pd
import numpy as np
import mysql.connector

def import_models():
    df = pd.read_excel("DVD_Films_List_for_Database_SJU.xlsx")
    conn = mysql.connector.connect(host='localhost', user='root', password='654321', database='chapinfilm')
    cursor = conn.cursor()
    for i,row in df.iterrows():
        print '-------', i, '-------------'
        print row
        title = row['Movie title'].replace("'", "\\'")
        alias = row['Also known as']
        if not pd.isnull(alias): alias = alias.replace("'", "\\'")
        year = row['Year']
        duration = row['Duration']
        durationMin = np.nan if pd.isnull(duration) else duration.split(' ')[0]
        version = row['Version']
        director = row['Director']
        if not pd.isnull(director): director = director.replace("'", "\\'")
        cast = row['Cast']
        if not pd.isnull(cast): cast = cast.replace("'", "\\'")
        casts = [] if pd.isnull(cast) else [s.strip() for s in cast.split(',')]
        award = row['Award']
        rating = row['rating']
        genre = row['Genre']
        genres = [] if pd.isnull(genre) else [s.strip().replace("'", "\\'") for s in genre.split(',')]
        medium = row['Medium']
        language = row['Language']
        languages = [] if pd.isnull(language) else [s.strip() for s in language.split(',')]
        closed_captions = row['Closed Captions']
        closed_captions_list = [] if pd.isnull(closed_captions) else [s.strip() for s in closed_captions.split(',')]

        add_film = ("insert into film (name, alias, version, year, duration, copies, medium, rating) "
                    "values('%s', %s, %s, %s, %s, %s, '%s', '%s')")
        data_film = (title, 
                     'NULL' if pd.isnull(alias) else "'"+alias+"'",
                     'NULL' if pd.isnull(version) else version, 
                     'NULL' if pd.isnull(year) else year,
                     'NULL' if pd.isnull(durationMin) else durationMin,
                     1,
                     medium,
                     'NULL' if pd.isnull(rating) else rating,
                     )
        sql = add_film%data_film
        print "sql:[" + sql + "]"
        cursor.execute(sql)
        filmid = cursor.lastrowid
        print 'inserted rowid', filmid

        #-- add language
        if len(languages) > 0 :
            add_lang = ("insert filmlanguage (film_id, language, category) "
                        "values(%s, '%s', '%s')")
            for lang in languages:
                data_lang = (filmid, lang, 'Languages' )
                sql = add_lang % data_lang
                cursor.execute(sql)

        if len(closed_captions_list) > 0 :
            add_lang = ("insert filmlanguage (film_id, language, category) "
                        "values(%s, '%s', '%s')")
            for lang in closed_captions_list:
                data_lang = (filmid, lang, 'ClosedCaptions' )
                sql = add_lang % data_lang
                cursor.execute(sql)

        #-- add award
        if not pd.isnull(award):
            add_award = "insert filmaward(film_id, award) values(%s, '%s')" %(filmid, award)
            cursor.execute(add_award)

        #-- add genre
        if len(genres) > 0:
            for g in genres:
                add_genre = "insert filmgenre(film_id, genre) values(%s, '%s')" %(filmid, g)
                cursor.execute(add_genre)

        #-- add staff
        add_staff = "insert filmstaff(film_id, role, name) values(%s, '%s', '%s')"
        if not pd.isnull(director):
            cursor.execute(add_staff%(filmid, 'Director', director))
        if len(casts) > 0:
            for c in casts:
                cursor.execute(add_staff%(filmid, 'Cast', c))

        conn.commit()

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    import_models()