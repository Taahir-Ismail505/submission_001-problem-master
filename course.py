

def create_outline():
    """
    TODO: implement your code here
    """#STEP 1
    '''
    puts all topics in  the a tuple and prints them ...in no..specific order
    '''
    Topics = set(["Introduction to Python","Tools of the Trade",
    "How to make decisions","How to repeat code",
    "How to structure data","Functions","Modules"])
    newTopic = list(Topics)
    newTopic.sort()    
    print("Course Topics:")
    for newTopic in newTopic:
        print("* " + newTopic)
    ###############################################################################    
    TopList  =list(Topics)#STEP 2
    '''
    creates a dict. for problems 1 to 3 and joins it with the the course topics 
    '''
    TopList.sort()
    TopicsL={"Problem 1":1,
            "Problem 2":2,
            "Problem 3":3 }
    TopicsL=list(TopicsL)
    
    print("Problems:")
    for TopList in TopList :
        print("* "+TopList +" : "+ (", ").join(TopicsL))
    ###############################################################################
    print("Student Progress:")#STEP 3
    '''
    puts all tuples into a list then prints all lists that goes through the loop
    '''
    Name1= ("Nyari" ,"Introduction to Python" ,"Problem 2 ", "[STARTED]")
    Name2= ("Adam" , " How to make decisions" ,"Problem 1 ", "[GRADED]")
    Name3 = ("Tom" ,"Tools of the Trade" , "Problem 3" ,"[COMPLETED]")
    My_NameList=[Name1,Name2,Name3] 
    x= 1
    for student, module, problem, status in My_NameList:
        print(str(x) + '. ', end='')
        print(f'{student} - {module} - {problem} {status}')
        x += 1
    
if __name__ == "__main__":
    create_outline()
