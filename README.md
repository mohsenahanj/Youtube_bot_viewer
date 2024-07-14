# Youtube_bot_viewer
 Youtube robot python

# 🎥 Video View Bot

این ربات پایتونی به شما کمک می‌کند تا بازدیدهای ویدیوهای خود را افزایش دهید! فقط کافیست لینک ویدیو و تعداد بازدیدهای مورد نظر خود را وارد کنید و بقیه کارها را به ربات بسپارید.

## ویژگی‌ها
- 📈 افزایش بازدید ویدیوها
- 🔗 پشتیبانی از هر لینک ویدیویی
- ⚙️ تنظیم تعداد بازدیدها

## نحوه استفاده
ابتدا کد زیر را در پروژه خود قرار دهید:

```python
V_LINK = 'https://www.youtube.com/watch?v=PSsN6Y4Nqi8'
```

        ## کد تعداد بازدید
		
```python
class VideoViewBot:
    def __init__(self, link, views=50):
```

سپس مسیر chromedriver را به صورت زیر تنظیم کنید:

``` Python

EXECUTABLE = 'C:/Users/ahanj/Downloads/chromedriver_win32/chromedriver.exe'
```

نصب و راه‌اندازی
مخزن را کلون کنید:
```
git clone https://github.com/mohsenahanj/Youtube_bot_viewer.git
```

وابستگی‌ها را نصب کنید:
```python
pip install -r requirements.txt
```

##مشارکت
ما از مشارکت شما استقبال می‌کنیم! برای مشارکت، لطفاً یک فورک از مخزن ایجاد کرده و تغییرات خود را به صورت یک Pull Request ارسال کنید.

##مجوز
این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر، فایل LICENSE را مشاهده کنید.




