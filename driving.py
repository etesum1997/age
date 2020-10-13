driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
    print('抱歉喔只能回答有/沒有')
    raise SystemExit
    
age = input('請問你幾歲？')
age = int(age)
if driving == '有':
    if age >= 18:
        print('讚喔有考駕照')
    else:
        print('ㄏㄡˊ～～～你是不是偷開車')
if driving == '沒有':
    if age >= 18:
        print('廢廢還不會開車噗噗 可以去考駕照摟')
    else:
        print('正常發揮')
