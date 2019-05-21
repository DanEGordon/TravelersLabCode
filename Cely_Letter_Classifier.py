#raw_doc references a letter as a continuous string (read straight from a text file), while doc references a letter where each word is an item in a list, having gone through the split command.

#import os
#os.chdir("Cely_Corpus_Test")
#raw = open("filename.txt", 'rU').read()

#file = open('results.txt','w')
#file.write(x)
#file.close



#Returns year letter was writen if it is at the top if the letter (still some problems)
def return_year(doc):
    startwords = ["Jhesu","Anno","Christus"]
    stopwords = ["Wellbelovyd","Ryght" ,'I','Riught']
    for x in doc:
        if x in startwords:
            k = doc.index(x)
            if doc[k+1] == "Jhesu":
                if doc[k+2][0] == "M" or "m" or "L" or "l" or '1':
                    return doc[k+2]

            else:
                if doc[k+1][0] == "M" or "m" or "L" or "l" or '1':
                    return doc[k+1]
        if x in stopwords:
            break

    return "none"






#Returns name of the sender if it is listed at the top of the letter
def Sender_first_pass(doc):
    common_starts = ["Anno","Jhesu","Wellbelovyd","Ryght",'Ryghte' ,'I','Riught',"Christus","Ther","Bedfelow", "Item"]
    if doc[0] not in common_starts:
        l = ""
        n = 0
        while doc[n] not in common_starts:
            l = l + " " + doc[n]
            n= n+1
        return l
    else:
        return "none"

# If letter has an address line, return it
def Address(doc):
    
    if "Addressed:" in doc:
        start = doc.index("Addressed:")
        after_ad = doc[start:]
        for x in after_ad:
            if x[-1] == '.':
                y = after_ad.index(x)
                break
            elif x == "dd" or x == "dd:":
                y = after_ad.index(x)
                break
        all_address = after_ad[:(y+1)]
        return " ".join(all_address)
    else:
        return "none"



#Search for a "writ at" statement using predetermined spellings of writ
def Sending_location(raw_doc):
    writ_spellings = ["Wreten",'Wrette','wrette','wrytte','Wrytte','wreten','wryttyn', 'Wryttyn',"Wrytten","wrytten",'wrettyn', 'Wrettyn','whryttyn','Whryttyn','wryt','Ryt' ,'ryt','Wryt',"writ","Writ", 'whryt','Whryt',"wryte","Wryte",'whrytten','Whrytten',"written","Written"]
    index_list = []
    doc = raw_doc.split()
    for x in doc:
        if x in writ_spellings:
            index_list = index_list + [doc.index(x)]
    rev_list = index_list[::-1]
    for x in rev_list:
        if doc[(x+1)] == "at":
            backhalf = doc[x:]
            for z in backhalf:
                if z[-1] == '.':
                    j = backhalf.index(z)
                    break
            sent_place = backhalf[:(j +1)]
            return " ".join(sent_place)

        elif doc[(x+1)] == "in":
            backhalf = doc[x:]
            for z in backhalf:
                if z[-1] == '.':
                    j = backhalf.index(z)
                    break
            sent_place = backhalf[:(j +1)]
            return " ".join(sent_place)

        else:
            return "none"


#Search for a "writ at" statement by first searching for words that begin with the letters "wr" and assuming they are spellings of writ.
def Sending_location_wide(raw_doc):
    doc = raw_doc.split()
    writ_spelling_search = []
    for x in doc:
        if x[0:2] == "wr" or x[0:2] == "Wr":
            if x not in writ_spelling_search:
                writ_spelling_search.append(x)

    index_list = []
    for x in doc:
        if x in writ_spelling_search:
            index_list = index_list + [doc.index(x)]
    rev_list = index_list[::-1]
    for x in rev_list:
        if doc[(x+1)] == "at":
            backhalf = doc[x:]
            for z in backhalf:
                if z[-1] == '.':
                    j = backhalf.index(z)
                    break
            sent_place = backhalf[:(j +1)]
            return " ".join(sent_place)

        elif doc[(x+1)] == "in":
            backhalf = doc[x:]
            for z in backhalf:
                if z[-1] == '.':
                    j = backhalf.index(z)
                    break
            sent_place = backhalf[:(j +1)]
            return " ".join(sent_place)

        else:
            return "none"



#def Send_location_alt(raw_doc):
    #doc = raw_doc.split()
            
        




#return a value equal to the number of appearences of terms on the haste list
def count_haste(doc):
    haste_spellings = ['Haste',"haste","haste.","hast","Hast","hast."]
    counter = 0
    for x in doc :
        if x in haste_spellings:
            counter = counter+1
    return counter



#Returns list of form [a,b], a being total times any month is referenced in the letter, b being the number of different months mentioned
#Uses combination of predetermined spellings and letter pattern searches.  Can be expanded.
def count_month_refs(doc):
    mc = 0
    dif_mon = []
    for x in doc:
        Jan_spells = ["Jenever","Jennar"]
        if x[0:3] == "Jan" or x[0:3] == "jan" or x in Jan_spells or x[:-1] in Jan_spells:
            mc = mc + 1
            if 1 not in dif_mon:
                dif_mon = dif_mon + [1]

        Feb_spells = ['Feverell','Fewerell']
        if x[0:3] == "Feb" or x[0:3] == "feb" or x in Feb_spells or x[:-1] in Feb_spells:
            mc = mc + 1
            if 2 not in dif_mon:
                dif_mon = dif_mon + [2]

        March_spells = ["March","Marche","march","marche",'Marsche','marsche']
        if x in March_spells or x[:-1] in March_spells:
            mc = mc + 1
            if 3 not in dif_mon:
                dif_mon = dif_mon + [3]

        Apr_spells = ["Aperell",'Apperell']
        if x[0:3] == "apr" or x[0:3] == "Apr" or x in Apr_spells or x[:-1] in Apr_spells:
            mc = mc + 1
            if 4 not in dif_mon:
                dif_mon = dif_mon + [4]

        May_spells = ["May","Maye"]
        if x in May_spells or x[:-1] in May_spells:
            mc = mc + 1
            if 5 not in dif_mon:
                dif_mon = dif_mon + [5]

        June_spells = ["June","Jun","Juyn",'Joyn',"Juen"]     
        if x in June_spells or x[:-1] in June_spells:
            mc = mc + 1
            if 6 not in dif_mon:
                dif_mon = dif_mon + [6]

        July_spells = ["Jule","Juyll","Juylly","Jowlle","July"]
        if x in July_spells or x[:-1] in July_spells:
            mc = mc + 1
            if 7 not in dif_mon:
                dif_mon = dif_mon + [7]

        Aug_spells = ["August","Augwste","Ajust","aug",'Auguste','Aug']
        if x in Aug_spells or x[:-1] in Aug_spells:
            mc = mc + 1
            if 8 not in dif_mon:
                dif_mon = dif_mon + [8]
                
        if x[0:4] == "Sept" or x[0:4] == "sept":
            mc = mc + 1
            if 9 not in dif_mon:
                dif_mon = dif_mon + [9]
                
        if x[0:3] == "oct" or x[0:3] == "Oct":
            mc = mc + 1
            if 10 not in dif_mon:
                dif_mon = dif_mon + [10]
                
        if x[0:3] == "nov" or x[0:3] == "Nov":
            mc = mc + 1
            if 11 not in dif_mon:
                dif_mon = dif_mon + [11]

        Dec_spells = ["Desembyr","Decembyr","Desember","December"]
        if x in Dec_spells or x[:-1] in Dec_spells:
            mc = mc + 1
            if 12 not in dif_mon:
                dif_mon = dif_mon + [12]
    return [mc,len(dif_mon)]

    

#returns list of full dates referenced in the letter in the form "the (number designation) day of (month)" as in "3rd day of March"
def extract_dates(raw_doc): 
    doc = raw_doc.split()
    dates = []
    for x in doc:
        if x =='day':
            c = doc.index(x)
            if doc[c+1] == 'of' and (doc[c+2]).istitle() == True:
                dates.append (" ".join(doc[(c-2):(c+3)]))
            doc[c] = "stop"
                
                    
        elif x == 'daye':
            c = doc.index(x)
            if doc[c+1] == 'of' and (doc[c+2]).istitle() == True:
                dates.append (" ".join(doc[(c-2):(c+3)]))
            doc[c] = "stop"
            
    return dates
    


# if the letter mentions recieving a previous letter, return either the general text around
# that phrase or up to the date the afformentioned letter was sent
def rtest(doc):
    rlist = ["Resayvyd", 'ressayvyd','ressayved','resseyved','ressawyd' , 'reseyvyd','resavyd','resawyd' ,'ressavid','ressayvyd' ,'receyuyd' , 'received','resasayvd','resayvyd','ressayoyd','resseywyd']
    llist = ['lecter', 'letter', 'lettar','lettyr', 'lettyrs','lettyres','letters','lecters']
    for x in doc:
        if x in rlist:
            r_index = doc.index(x)
            post_r = doc[r_index: r_index+8]
            for y in post_r:
                if y in llist:
                    recieve_chunk = doc[(r_index-3):(r_index+15)]
                    if "day" in recieve_chunk:
                        of_ind = recieve_chunk.index("day")
                        return " ".join(recieve_chunk[:(of_ind+3)])
                    elif "daye" in recieve_chunk:
                        of_ind = recieve_chunk.index("daye")
                        return " ".join(recieve_chunk[:(of_ind+3)])
                    else:
                        return " ".join(recieve_chunk)

    return "none"



# finds words connected to sequences of events, in this case "tidings" and "understand"
# returns number of appearences in letter and a list of sentence chunks where the words show up
def event_words(doc):
    tidings_spells = ['tydynges', 'tydyngs', 'tydynges', 'tydyng', 'tydyngys', 'tidings',"tydynggys"]
    under_spells = ['understande', 'undyrstond', 'wndyrstone', 'wnderstond' ,'understand', 'understond', 'understonde', 'understond', 'undyrtsond', 'wndyrstonde', 'wnderstonde', 'wndyrstode', 'wndyrstones', 'wnderstonde']
    t_count = 0
    u_count = 0
    t_list = []
    u_list = []
    for x in doc:
        if x in tidings_spells:
            t_count = t_count + 1
            t_index = doc.index(x)
            t_list = t_list + [" ".join(doc[(t_index-4):(t_index+5)])]
            doc[t_index] = "extract"
        elif x in under_spells:
            u_count = u_count + 1
            u_index = doc.index(x)
            u_list = u_list + [" ".join(doc[(u_index-4):(u_index+5)])]
            doc[u_index] = "extract"

    return [t_count,u_count,t_list,u_list]
            



#a presentation of the information in IDLE. updated as new functions created.
def analyze_letter(raw_doc):
    doc = raw_doc.split()
    sent_year = return_year(doc)
    sender_name = Sender_first_pass(doc)
    address = Address(doc)
    Sent = Sending_location(raw_doc)
    Sent_wide = Sending_location_wide(raw_doc)
    haste = count_haste(doc)
    months = count_month_refs(doc)
    all_dates = extract_dates(raw_doc)
    response = rtest(doc)
    events = event_words(doc)

    print '-----'


    if sent_year != "none":
        print "Letter sent in the year " + sent_year

    if sender_name != "none":
        print "Sent by" + sender_name

    if address != "none":
        print address

    if Sent == "none":
        if Sent_wide != "none":
            print Sent_wide
    else:
        print Sent

    print "the term haste is referenced " + str(haste) + " time(s)"

    if months == 0:
        print "the names of months appear " + str(months[0]) + " time(s)"
    else:
        print "the names of months appear " + str(months[0]) + " time(s), with " + str(months[1]) + " different month(s) mentioned"
    

    if all_dates != []:
        x = 'The dates mentioned are '
        for y in all_dates:
            x=x+ (y + ", ")
        print x

    if response != 'none':
        print "Recieve statement: " + response

    if events[0] != 0:
        print "tidings appears " + str(events[0]) +" times in the following contexts: " + str(events[2])

    if events[1] != 0:
        print "understand appears " + str(events[1]) +" times in the following contexts: " + str(events[3])

#returns what is printed in analyze_letter as one string
def analyze_letter_value(raw_doc):
    doc = raw_doc.split()
    sent_year = return_year(doc)
    sender_name = Sender_first_pass(doc)
    address = Address(doc)
    Sent = Sending_location(raw_doc)
    Sent_wide = Sending_location_wide(raw_doc)
    haste = count_haste(doc)
    months = count_month_refs(doc)
    all_dates = extract_dates(raw_doc)
    response = rtest(doc)
    events = event_words(doc)

    results_list = []

    results_list.append('-----')
  

    if sent_year != "none":
        results_list.append( "Letter sent in the year " + sent_year  )

    if sender_name != "none":
        results_list.append( "Sent by" + sender_name )

    if address != "none":
        results_list.append(address)

    if Sent == "none":
        if Sent_wide != "none":
            results_list.append(Sent_wide)
    else:
        results_list.append(Sent)

    results_list.append("the term haste is referenced " + str(haste) + " time(s)")

    if months == 0:
        results_list.append("the names of months appear " + str(months[0]) + " time(s)")
    else:
        results_list.append("the names of months appear " + str(months[0]) + " time(s), with " + str(months[1]) + " different month(s) mentioned")
    

    if all_dates != []:
        x = 'The dates mentioned are '
        for y in all_dates:
            x=x+ (y + ", ")
        results_list.append(x)

    if response != 'none':
        results_list.append("Recieve statement: " + response)

    if events[0] != 0:
        results_list.append("tidings appears " + str(events[0]) +" times in the following contexts: " + str(events[2]))

    if events[1] != 0:
        results_list.append( "understand appears " + str(events[1]) +" times in the following contexts: " + str(events[3]))


    final_results = ""
    for r in results_list:
        final_results = final_results + (str(r) + '\n' )


    return final_results
    



def cely_num():
    x=0
    nums = []
    while x <= 138:
        x = x+1
        nums.append(x)

    nums = nums + [143,144,145,146,147,148,149,150]
    return nums



def analyze_all(result_file):
    cn = cely_num()
    rf = open(result_file,'w')
    for c in cn:
        s = str(c)
        rf.write("\n" + s + '\n')
        cur_file = "Cely_" + s + ".txt"
        print cur_file
        raw = open(cur_file, 'rU').read()
        results = analyze_letter_value(raw)
        rf.write(results)


    rf.close()






def stats():
    cn = cely_num()
    haste_num = 0
    tyd_num = 0
    u_num = 0
    combo = 0
    for c in cn:
        s = str(c)
        cur_file = "Cely_" + s + ".txt"
        raw = open(cur_file, 'rU').read()
        k = raw.split()
        if count_haste(k) != 0:
            haste_num = haste_num + 1
        x = event_words(k)
        if x[0] > 0 :
            tyd_num = tyd_num + 1

        if x[1] > 0 :
            u_num = u_num + 1

        if x[0] > 0 and x[1] > 0:
            combo = combo+1
            

    
    print "haste: " + str(haste_num) +"/147"
    print "tidings: " + str(tyd_num) +"/147"
    print "understand: " + str(u_num) +"/147"
    print "combo: " + str(combo) +"/147"



    
        
