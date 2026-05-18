

cypher = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0','/', '@','#','$','!','?','(',')','-']


def crypt(string, position=10):
    
    new_string = ""
    
    for char in string:
        
        if char in cypher:
            i = cypher.index(char)
            if i + position <= len(cypher)-1:
                new_string = new_string + cypher[i + position]
            else:
                new_string = new_string + cypher[i - position]
        else:
            new_string = new_string + char
            
    return new_string
