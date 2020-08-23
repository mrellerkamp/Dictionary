import urllib2
import json
import sqlite3
import sqlite3 as lite 


prompt = int(raw_input('To view words, press 1. To add a word, press 2: '))
while prompt <= 2:
    if prompt == 1:
        con = lite.connect('dictionary.db')
        cur = con.cursor()
        
        def get_dictionary():
            cur.execute("SELECT * FROM words ORDER BY word ASC")
            table = cur.fetchall()
            for tple in table:
                print 
                print tple[1] + ': ' +  tple[2]
                
            con.commit()
            
            con.close()
        
        get_dictionary()
        
    elif prompt == 2: 
        
        conn = sqlite3.connect('dictionary.db')
        c = conn.cursor()
        
        base_url = 'https://api.dictionaryapi.dev/api/v1/entries/en/'
        word = raw_input('Enter word: ')
        
        request_url = base_url + word
        
        
        hdr = { 'User-Agent' : 'dictionary bot' }
        req = urllib2.Request(request_url, headers=hdr)
        r = urllib2.urlopen(req)
        
        data = r.read()
        
        obj = json.loads(data)
        
        meaning = obj.pop()['meaning']
        
        
        keys = meaning.keys()
        definitions = [meaning[key] for key in keys]
        definitions = [d for sublist in definitions for d in sublist]
        
        for index, d in enumerate(definitions):
            print str(index + 1) + '. ' + d['definition']
            
        num = int(raw_input('Select a number: '))
        
        while num > len(definitions):
            print 'That is not a valid input.'
            num = int(raw_input('Select a number: '))
        
        chosen_definition = definitions[num - 1]['definition']
        print 'This word has been added to the list.'
        
        c.execute("INSERT INTO words VALUES (NULL,?,?)", (word, chosen_definition))
        
        conn.commit()
        
        conn.close()
    else:
        print 'Try again.'
        
            
        #prompt = int(raw_input('To view words, press 1. To add a word, press 2: '))
    

    
    prompt = int(raw_input('To view words, press 1. To add a word, press 2: '))
        



    
