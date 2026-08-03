class A:
    verA = "Hello welcome to A class "
class B: 
    verB = "Hello welcome to B class "
class C(A,B):
    verC = "Hello welcome to C class "

ver1 = C()
print(ver1.verA, ver1.verB, ver1.verC)

