import socket
import os
import Questions
from _thread import *

ServerSideSocket = socket.socket()
# عنوان السيرفر
host = '127.0.0.1'
# بورت الاستماع
port = 3000
# عدد الاتصالات التي تم اجراؤها
ThreadCount = 0
try:
    # محاولة فتح سوكت
    ServerSideSocket.bind((host, port))
except socket.error as e:
    # خطأ أثناء محاولة الاستماع للسوكت
    print(str(e))
    # في حال الاتصال اطبع أن السوكت تستمتع وتنتظر اتصالا
print('Socket is listening..')
# عدد الاتصالات المسموحة في نفس الوقت 
ServerSideSocket.listen(5)
# تابع الإرسال والاستقبال والذي يقوم بجلب الاسئلة وحساب عدد الاجابات الصحيحة
def multi_threaded_client(connection):
    # ارسل للمستخدم عبارة قم بادخل السمك
    connection.send(str.encode('Server is working: Please Enter Your Name:'))
    # قم بانتظار جواب المستخدم
    name =connection.recv(2048)
    # قم بارسال رسالة التعليمات باختيار الجواب الصحيح
    connection.send(str.encode((' Welcome '+name.decode('utf-8')+' select the correct answer a or b Or c or d, Press Enter to start')))
    # قم بتعريف متحول من كلاس الاسئلة 
    qlist =  Questions.QuestionsList.question
    # يشير الى رقم السؤال الحالي
    counter = 0
    # العلامة التي قام الطالب بتحصيلها
    mark = 0
    # قم بالمرور على جميع الاسئلة بالتتالي
    while counter< len(qlist):
        # ارسل السؤال للمستخدم
        connection.send(str.encode(qlist[counter].question))
        # انتظر الجواب
        data = connection.recv(2048)
        # قم بتخزين جواب المستخدم
        qlist[counter].userAnswer = data.decode('utf-8')
        if not data:
            break
        # إذا كان الجواب صحيحا قم بزيادة عدد الاجوبة الصحيحة
        if qlist[counter].userAnswer == qlist[counter].answer:
            mark = mark+1
        # انتقل للسؤال التالي
        counter = counter+1
    counter =0
    correctanswers =""
    while counter< len(qlist):
        correctanswers = correctanswers +"\ncorrect answer: "+ qlist[counter].answer+" your answer is: "+qlist[counter].userAnswer
        counter =counter+1
    # اطبع علامة الطالب الكلية بعد انتهاء الحلقة
    correctanswers =correctanswers+('\nyour mark is: '+str(mark) +"/"+str(counter))
    connection.sendall(str.encode(correctanswers))
    # أغلق الاتصال
    connection.close()
    
# الاستماع حتى يأتي اتصال جديد وفي حال جاء اتصال قم بتحويله لبورت جديد واطرح الاسئلة عليه
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()


