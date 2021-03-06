import threading

n=1000
offset=n//4

def thread_main(li, i):
    for idx in range(offset*i, offset*(i+1)):
        li[idx]*=2
    
li=[i for i in range(1,1001)]
threads=[]

#스레드를 생성
for i in range(4):
    th=threading.Thread(
        target=thread_main, args=(li,i))
    threads.append(th)

#멀티 스레딩
for th in threads:
    th.start()

#메인 스레드에서 나머지 스레드들이 모든 실행을 끝낼 떄 까지 기다린다.

for th in threads:
    th.join()

print(li)