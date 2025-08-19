# ChuyenDeCongNghe

Đây là repo thực hành cá nhân môn Chuyên Đề Công Nghệ.

## Mô tả các thư mục chính

- **djangotutorial/**  
  Thực hành 8 tutorial parts theo tài liệu của django

- **models/**  
  Tạo 1 model đơn giản, thực hành viết queries quan hệ và một số complex queries, migration xuôi ngược, command tạo dữ liệu mẫu.

## Hướng dẫn chạy dự án

1. Cài đặt các thư viện cần thiết:

   ```
   pip install -r requirements.txt
   ```

2. Di chuyển vào thư mục dự án Django:

   ```
   cd djangotutorial
   ```

   or

   ```
   cd models
   ```

3. Chạy server phát triển:

   ```
   python manage.py runserver
   ```

4. Truy cập ứng dụng tại: [http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)

## Thực hành với models/

Trong thư mục **models/**, bạn có thể chạy các lệnh terminal sau:

1. Tạo migration từ model:

   ```
   python manage.py makemigrations
   ```

2. Áp dụng migration vào database:

   ```
   python manage.py migrate
   ```

3. Mở Django shell để thực hành query:

   ```
   python manage.py shell
   ```

4. Chạy custom management command để tạo dữ liệu mẫu:

   ```
   python manage.py seed
   ```

5. Xem database bằng SQLite CLI (nếu dùng SQLite):

   ```
   python manage.py dbshell
   ```

6. Tạo superuser để vào trang admin:
   ```
   python manage.py
   ```
