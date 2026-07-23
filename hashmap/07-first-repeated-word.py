def first_repeated_word(sentence):
    words = sentence.lower().split()  
    seen = {}  
    
    for word in words:
        if word in seen:
            return word  
        seen[word] = 1   
    
    return None
