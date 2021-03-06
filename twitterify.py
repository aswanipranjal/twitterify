import string

limit = 140 #character limit
separator = "..." 

punctuation_list = list(string.punctuation)

def twitterify(string):
    list_of_strings = []
    if len(string) <= limit:
        list_of_strings.append(string)
    
    else:
        i = limit - len(separator)
        while(True):
            if string[i] == " " and string[i-1] not in punctuation_list: #so that ellipses don't follow punctuation 
                break
            else:
                i -= 1

        list_of_strings.append(string[:i+1] + separator)

        remaining = separator + string[i+1:]

        if len(remaining) > limit:
            list_of_strings += twitterify(remaining)
        else:
            list_of_strings.append(remaining)

    return list_of_strings

#example
string = """Contrary to popular belief, Lorem Ipsum is not simply random text. 
            It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. 
            Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 
            Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical 
            literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de 
            Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. 
            This book is a treatise on the theory of ethics, very popular during the Renaissance. 
            The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32. 
            The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 
            1.10.32 and 1.10.33 from \"de Finibus Bonorum et Malorum\" by Cicero are also reproduced in their exact original
            form, accompanied by English versions from the 1914 translation by H. Rackham."""

answer = twitterify(string)

for i in answer:
    print(len(i), i)
