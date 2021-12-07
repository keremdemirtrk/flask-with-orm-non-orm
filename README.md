# flask-with-orm-non-orm

# flask-with-orm-non-orm

# Uygulamayı kurmak ve kullanmak için aşağıdaki adımları yapmanız gerekmektedir. 2 farklı şekilde kurma imkanınız vardır, önerilen venv kullanarak kurulumudur.

# 1  - İstediğiniz bir dizine gelerek ister "mkdir homework" ile ya da elle "homework" isimli yeni bir klasör açınız.
# 2  - Terminal ile "cd homework" ile klasörün içerisine geliniz.
# 3  - "python3 -m venv venv" komutu ile venv kurarak ilerleyiniz. 
# 4  - "source venv/bin/activate" komutu ile venv'i aktif hale getiriniz. 
# 5  - Kodu bu klasörün içerisinde ya git clone ile ya da elle yükleyiniz.
# 6  - "pip install flask" komutu ile flask'ı yükleyiniz.
# 7  - "pip install Flask-Mail" ile flask-mail hizmetini kurunuz.
# 8  - "pip install flask-sqlalchemy" komutu ile SQLAlchemy'i kurunuz.
# 9  - "sqlite3 adresdata.db" komutu ile database'inizi kurmanız gerekmektedir. Çıkacak olan sqlite3 terminalinde önce ".tables" sonra ".exit" yapmanız gerekmektedir.
# 10 - "python3" ile python terminaline girerek, önce "from main import db"  sonra "db.create_all()" yaparak class'a göre db table'ını oluşturmanız gerekmektedir.

# Uygulama kurulumu bu kadardı. Şimdi değiştirmeniz ve eklemeniz gereken yerleri doğru bir şekilde ekledikten sonra uygulama çalışacak hale gelecektir. Aşağıdaki notları okuyunuz.

# 1 - main.py dosyası içerisindeki 12. satırı okuyunuz. => 4 tane /'dan sonra kodu indirdiğiniz yerin içerisinde olan DB path'i girilecektir.
# 2 - main.py dosyası içerisinde 98. satırı okuyunuz. => Tırnakların arasına E-mail adresinizi girmeniz gerekmektedir.
# 3 - main.py dosyası içerisinde 99. satırı okuyunuz. => Tırnakların arasına Password'unuzu girmeniz gerekmektedir.
# 4 - main.py dosyası içerisinde 109. satırı okuyunuz. => Tırnakların arasına Mail'i gönderecek E-mail adresini girmeniz gerekmektedir.
# 5 - main.py dosyası içerisinde 110. satırı okuyunuz. => Tırnakların arasına göndereceğiniz mail adresini girmeniz gerekmektedir.
# 6 - Mail'i yollamak istiyorsanız, gmail üzerinden gerekli güvenlik ayarını açmanız gerekmetedir. Vereceğim linkten ulaşabilirsiniz. https://www.google.com/settings/u/2/security/lesssecureapps
# 7 - Uygulamanın non-orm kısmının düzgün bir şekilde çalışması için uygulamayı run ettikten sonra main.py içerisindeki 50.satırı yorum satırından kaldırıp bir kere auto refresh olmasını bekleyiniz. Bu işlem process'i kırmaya gerek olmayan bir işlemdir.
