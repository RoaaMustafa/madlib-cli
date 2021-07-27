import re 

print("""
Welcome To  our fun game 
Lets have fun !!!
""")
 
# ////////////////////////////////////////////////////////////
def user_input():
    print (  """
    function that takes in a path to text file and returns a stripped string of the file’s contents.
    """)
    user_answer = []
    for i in range(len(list)):
        user_answer.append(input(f'Enter {list[i]}: '))

    # print(user_answer)
    return user_answer
# //////////////////////////////////////////////////
def read_template(file_path:str)->str:
    try:
     with open (file_path,'r') as file:
        content=file.read()
        return content.strip()
    except:
         raise FileNotFoundError(file_path)

#  //////////////////////////////////////////////// 
def parse_template(string):  

 actual_part=tuple(re.findall(r'{(.*?)}',string))
 actual_stripped=re.sub('{.*?}','{}',string)
 return actual_stripped,actual_part

#/////////////////////////////////////////////////


def merge(text:str,text_add:tuple):
    output_text=text.format(*text_add)
    with open('assets/output.txt','w') as file:
        file.write(output_text)
    return output_text

 # ////////////////////////////////////////
answer_from_user=[]

def Lets_start_game():
    read=read_template("assets/game_example_text.txt")
    text,value=parse_template(read)
    for i in value:
        input_user=input(f"Enter {i}:")
        answer_from_user.append(input_user)
    return merge(text,answer_from_user)
if __name__== "__main__":
 Lets_start_game()