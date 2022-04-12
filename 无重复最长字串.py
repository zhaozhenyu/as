class Solution(object):
    def reverse(self, x):
        x1=str(x)
        Negative = False
        if x1[0]=="-":
            print(x1,"原值")
            x1 = x1[1:]
            Negative=True
            print(x1,"去负操作",int(x1))
        x1 = x1[::-1]
        # 逆序
        if -2**31  <= int(x1)<= 2**31 - 1 :
            print(x1,"没有超过范围")
        else:
            return 0
        if x1[0]=="0" and len(x1)<=1:
            print("判断零操作")
            return 0
        print(x1,"x1",len(x1))
        Count=0
        for i in range(len(x1)):
            if x1[i] =="0" and x1[i:i+1]==0:
                print(x1[i], "if 循环" , "i equal",i)
                Count += 1
            print("Count",Count)
        x1=x1[Count:]
        if Negative==True:
            x1=int(x1)*-1
        print(x1, "去零操作")
        print(x1,"x1 cut")
        return  int(x1)
a=Solution()
print(a.reverse("123"),"返回值")