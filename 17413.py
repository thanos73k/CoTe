s=(input())
check =False
word=''
result=''

for i in range(len(s)):

    if s[i] =='<':
        word+='<'
        check=True
    elif s[i] == '>':
        word += '>'
        result += word
        word = ''
        check = False

    elif check ==True:
        word +=s[i]

    elif check==False and s[i] ==' ':
        result += word
        result += ' '
        word=''

    elif check == False:
        word = s[i] + word

result +=word

print(result)