class test(): # class(클래스) : 과자 틀, object(객체) : 과자 틀에 의해서 만들어진 과자
    def __init__(self,a,b=0): # 빈 그릇을 준비 (__init__이라는 메서드 만들기)
        # 여기서 self, a, b는 매개변수
        print("init {}, {}\n".format(a,b)) #init과 각각 a, b에 들어가는 무언가를 프린트
        self.a = a #self.속성에 값을 할당
        self.b = b #self.속성에 값을 할당
        self.c = 1 #self.속성에 값을 할당
    def print(self):
        print("a={}".format(self.a))
        print("b={}".format(self.b))
        print("c={}\n".format(self.c))

