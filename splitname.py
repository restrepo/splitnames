import re
def split_names(s,exceptions=['GIL','LEW','LIZ','PAZ','REY','RIO','ROA','RUA','SUS','ZEA']):
    """
    Extract the parts of the full name `s` in the format ([] → optional):
    
    [SMALL_CONECTORS] FIRST_LAST_NAME [SMALL_CONECTORS] [SECOND_LAST_NAME] NAMES
    
    If len(s) < 4 → Foreign name assumed with single last name on it
    
    Add short last names to `exceptions` list if necessary
    
    Works with:
    ----
        s='LA ROTTA FORERO DANIEL ANDRES'
        s='MONTES RAMIREZ MARIA DEL CONSUELO'
        s='CALLEJAS POSADA RICARDO DE LA MERCED'
        s='DE LA CUESTA BENJUMEA MARIA DEL CARMEN'
        s='JARAMILLO OCAMPO NICOLAS CARLOS MARTI'
        s='RESTREPO QUINTERO DIEGO ALEJANDRO'
        s='RESTREPO ZEA JAIRO HUMBERTO'
        s='JIMENEZ DEL RIO MARLEN'        
        s='ROMANO ANTONIO ENEA'
        s='NARDI ENRICO'
    Fails with more than 2 last names:
    ----
        s='RANGEL MARTINEZ VILLAL ANDRES MAURICIO'
    """
    s=s.title()
    sl=re.sub('(\s\w{1,3})\s',r'\1-',s,re.UNICODE)
    sl=re.sub('(\s\w{1,3}\-\w{1,3})\s',r'\1-',sl,re.UNICODE)
    sl=re.sub('^(\w{1,3})\s',r'\1-' ,sl,re.UNICODE)
    #Clean exceptions
    #Extract short names list
    lst=[s for s in re.split( '(\w{1,3})\-',sl ) if len(s)>=1 and len(s)<=3 ]
    #intersection with exceptions list
    exc=[value for value in exceptions if value in lst]
    if exc:
        for e in exc:
            sl=sl.replace('{}-'.format(e),'{} '.format(e))
            
    #if sl.find('-')>-1:
    sll=[s.replace('-',' ') for s in sl.split()]
    if len(s.split())==2:
        sll=[s.split()[0]]+['']+[s.split()[1]]
    #
    d={'NOMBRE COMPLETO' : ' '.join(sll[2:]+sll[:2]),
     'PRIMER APELLIDO' : sll[0], 
     'SEGUNDO APELLIDO': sll[1], 
     'NOMBRES'         :' '.join(sll[2:]), 
     'INICIALES'       :' '.join( [i[0]+'.' for i in ' '.join(sll[2:]).split() ] )
    }
    return d
