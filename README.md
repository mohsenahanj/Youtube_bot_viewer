# Youtube_bot_viewer
 Youtube robot python
![Static Badge](https://img.shields.io/badge/https%3A%2F%2Fcamo.githubusercontent.com%2F27ae9ff38ce84f28477dcd90f2329b1db70c83721c87d6f4a4234bf581553771%2F68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d79656c6c6f773f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e)

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

# کد تعداد بازدید
		
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




