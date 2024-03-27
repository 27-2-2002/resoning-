# 1. Eliminate implication
# 2. Move negation inward (Demorgan Law)
# 3. Remove double-not.
# 4. Standardize variable scope.
# 5. The prenex form (obtained by moving all quantifiers to the left of the formula.)
# 6. Skolemization for existential quantifiers.
# 7. Eliminate universal quantifiers.
# 8. Convert to conjunctive normal form
# 9. Turn conjunctions into clauses in a set, and rename variables so that no clause shares the same variable name.
# 10.Rename variables in clauses so that each clause has a unique variable name.
# ~ = not , V = and , ∧ = or , ∀ , ∃
# Section : S4
# Student : Alaa Mohsen Farag - 20211015
# Student : Hajer Galal Anwer - 20210404

print("∀x [ ∀y Body(y) =⇒ Head(x,y) ] =⇒ [ ∃y Head(y,x) ]")

def Step1(e):
    TheArray = e.split(" ")
    for i in range(len(TheArray)):
        if(TheArray[i] == "=⇒"):
            TheArray[i] = "V"
            if(TheArray[i-1] == "]"):
                TheArray.insert(TheArray.index("["), "~")
            else:
                TheArray.insert(i-1,"~")
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

def Step2(e):
    TheArray = e.split(" ")
    for i in range(len(TheArray)):
        if(TheArray[i] == "~"):
            if(TheArray[i+1] == "["):
                TheArray.insert(TheArray.index("]") + 2, "~")
                TheArray.remove('~')
                TheArray.insert(i + 1, "~")
                if(TheArray[TheArray.index("]")+1] == "V"):
                    TheArray[TheArray.index("]") + 1] = '∧'
                elif(TheArray[TheArray.index("]")+1] == "∧"):
                    TheArray[TheArray.index("]") + 1] = 'V'
                break
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

def Step3(e):
    TheArray = e.split(" ")
    for i in range(len(TheArray)):
        if(TheArray[i] == "~"):
            TheArray.remove("~")
            if (TheArray[i+1] == "~"):
                TheArray.remove("~")
            elif(TheArray[i+2] == "~"):
                TheArray.remove("~")
            elif(TheArray[i+3] == "~"):
                TheArray.remove("~")
            break
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

def Step4(e):
    TheArray = e.split(" ")
    indexs = []
    for i in range(len(TheArray)):
       if(TheArray[i]._contains("∀") or TheArray[i].contains_("∃")):
           indexs.append(i)
    indexs.append(len(TheArray))
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

def Step5(e):
    TheArray = e.split(" ")
    for i in range(len(TheArray)):
        if(TheArray[i]._contains_("∃")):
            TheArray.remove(TheArray[i])
            for j in range(i , len(TheArray)):
                newtext1 = TheArray[j].replace("x", "No", 1).replace("y", "No", 1)
                TheArray[j] = newtext1
            break
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

def Step6(e):
    TheArray = e.split(" ")
    exx = ""
    for i in range(len(TheArray)):
        if (TheArray[i]._contains("∀") or TheArray[i].contains_("∃")):
            exx += TheArray[i] + " "
    arrayA = [item for item in TheArray if '∀' not in item]
    arrayE = [item for item in arrayA if '∃' not in item]
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

def Step7(e):
    TheArray = e.split(" ")
    TheArray = [element for element in TheArray if "∀" not in element]
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

def Step8(e):
    TheArray = e.split(" ")
    i = 0
    while i < len(TheArray):
        if(TheArray[i] == "∧"):
            if(TheArray[i+1] == "[" or TheArray[i+2] == "["):
                TheArray[i] = "V"
        i += 1
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

def Step9(e):
    TheArray = e.split(" ")
    TheArray = [element for element in TheArray if "[" not in element]
    TheArray = [element for element in TheArray if "]" not in element]
    TheArray = [element for element in TheArray if "∧" not in element]
    TheArray = [element for element in TheArray if "V" not in element]
    ex = "{ "
    for i in range(len(TheArray)):
        ex += TheArray[i] + " ,"
    ex[:-2]
    ex += " }"
    return ex

def Step10(e):
    TheArray = e.split(" ")
    i = 0 
    while i < len(TheArray):
        if(TheArray[i]._contains_("x")):
            new = TheArray[i].replace("x","par1",1)
            TheArray[i] = new

        if(TheArray[i]._contains_("y")):
            new = TheArray[i].replace("y","par2",1)
            TheArray[i] = new
        
        if(TheArray[i]._contains_("z")):
            new = TheArray[i].replace("z","par3",1)
            TheArray[i] = new
        
        if(TheArray[i]._contains_("w")):
            new = TheArray[i].replace("w","par4",1)
            TheArray[i] = new
        i += 1
    ex = "" 
    for i in range(len(TheArray)):
        ex += TheArray[i] + " "
    return ex[:-1]

print(Step10(Step9((Step8(Step7(Step6(Step5(Step4(Step3(Step2(Step1("∀x [ ∀y Body(y) =⇒ Head(x,y) ] =⇒ [ ∃y Head(y,x) ]"))))))))))))
