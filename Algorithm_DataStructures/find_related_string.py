def find_related_words(repository,word):
    n = len(word)
    if n < 3:
        return []
    result = [x for x in repository if x[:n].lower() == word.lower()]
    if len(result)>3:
        return result[:3]
    return result

result = find_related_words(["hello","hellow","hellowo","hellowor","helloworl"],"hell")
print(result)
