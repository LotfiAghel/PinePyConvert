import tokenize
import json
a=[]
mapp={0:""}
with tokenize.open('test.pine') as f:
    tokens = [i for i in tokenize.generate_tokens(f.readline)]
    #json.dumps(tokens)
    for token  in tokens:
        print(token)
        mapp[token.type]=token.string
        a.append({"type":token.type,
                  "line":token.start[0],
                   "cstart":token.start[1],
                   "cend":token.end[1],
                   "name":token.name,
                   "str":token.string})
print(a)
print(len(mapp))
print(mapp)
