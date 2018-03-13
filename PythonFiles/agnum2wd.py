nw1={1:'One',2:'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six',\
     7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',11: 'Eleven',\
     12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',15: 'Fifteen',\
     16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
nw2={2:'Twenty',3:'Thirty',4:'Forty', 5:'Fifty',\
     6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
a=[]
def num(Number):
    if(1<= Number <=19):
        return nw1[Number]
    elif(Number>=20):
        return nw2[Number]
def size(x):
    length=len(str(x))
    for i in (0,length):
        while(x!=0):
            a.append(x%10)
            x=x/10
    print a
def words(x):
    length=len(str(x))
    if length==2:
        b=a[]
        print nw1[b]
def main():
    number = int(raw_input('Enter Number:'))
    size(number)
    words(number)
    '''ans = num(number)
    print ans'''
main()
