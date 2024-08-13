from django.shortcuts import render
# Create your views here.
def func1(request, num):
    res=num
    flag = False
    if num < 2:
        flag = True
    else:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
    
    if not flag:
        res = num
    else:
        res =""  
    
    return render(request, 'prime.html', {'res': res})


def func2(request,str1,str2):
    s1=str1.upper()
    s2=str2.upper()
    s11=[]
    s12=[]
    for i in s1:
        s11.append(i)
    for i in s2:
        s12.append(i)
    s11.sort()
    s12.sort()
    res=s11==s12
    d={'res':res}
    return render(request,'anagram.html',d)




def func3(request,num):
    res=num**2
    d={'res':res}
    return render(request,'square.html',d)


def func4(request,num):
    sum=0
    temp=num
    while num > 0:
        rem=num % 10
        sum=sum*10+rem
        num=num//10
    res=(temp==sum) 
    return render(request,'palin.html',{'res':res})

def func5(request,n1,n2):
    a=n1
    b=n2
    gcd=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i == 0:
            gcd = i
    return render(request,'gcd.html',{'r': gcd ,'n1':n1,'n2':n2})

