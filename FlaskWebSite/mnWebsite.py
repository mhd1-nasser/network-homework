from flask import Flask, render_template, request,redirect,url_for
import os
app = Flask(__name__)

# تحديد مسار الصفحة الرئيسية
@app.route('/')
def login():
   # إذا كانت كلمة المرور خطأ أهر رسالة الكلمة خطأ
   try:
      message = request.args['messages']
      return render_template('login.html',message=message)
   except :
      # إذا كانت صحيحة قم بالتحويل للصفحة الرئيسية
      return render_template('login.html',message="")
      
# الصفحة الرئيسية
@app.route('/indix',methods = ['POST', 'GET'])
def main():
   # اقرء كلمة السر والمستخدم
   username = request.form["username"]
   password =request.form["login"]
   # تأكد من صحتهم إذا صح قم بالتوجيه لصفحة الأدمن
   if (username =='admin' and password=='admin'):
      return render_template("main.html",result = username)
   else:
      # إذا خطأ قم بإعادة التوجيه لصفحة الدخول مع إظهار رسالة خطأ في كلمة السر
      return redirect(url_for('login', messages="Wrong Password"))

# ابدأ الموقع
if __name__ == '__main__':
   app.run()