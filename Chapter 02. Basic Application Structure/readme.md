# 1. Initialization
# 2. Routes and View Functions
###### [hello.py](hello.py)
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
        <h1>Hello World!</h1>
    """
```
![](images/02.00.png)

* Đoạn code dưới đây cũng cho ra kết quả tương tự như đoạn code ở trên:
###### [hello_01.py](hello_01.py)
```python
from flask import Flask
app = Flask(__name__)

def index():
    return """
        <h1>Hello World!</h1>
    """
    
app.add_url_rule("/", "index", index)
```
![](images/02.01.png)

<hr>

* Đoạn code dưới đây sẽ dựa vào tên của người dùng cung cấp trên url `localhost:5000/user/<name>` để trả về trang HTML chứa nội dụng **Hello, <name>!**.

###### [hello_02.py](hello_02.py)
```python
from flask import Flask
app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return """
        <h1>Hello, {}!</h1>
    """.format(name)
```
![](images/02.02.png)
# 3. A Complete Application
# 4. Development Web Server
* Giả sử cần chạy server trong file `hello.py`, thì tiến hành như sau:
```
export FLASK_APP=hello.py
flask run
```
* Flask mặc định server sẽ chạy tại địa chỉ `localhost:5000`.

