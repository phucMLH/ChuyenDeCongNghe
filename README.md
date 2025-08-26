# ChuyenDeCongNghe

Đây là repo thực hành cá nhân môn Chuyên Đề Công Nghệ.

## Hướng dẫn chạy dự án

1. Cài đặt các thư viện cần thiết:

   ```
   pip install -r requirements.txt
   ```

2. Di chuyển vào thư mục dự án Django:

   ```
   cd views
   ```

3. Chạy server phát triển:

   ```
   python manage.py runserver
   ```

4. Truy cập ứng dụng tại: [http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)

---

## Cấu trúc và các phần đã thực hiện

### 1. URL config

- File: `views/mysite/urls.py`, `views/polls/urls.py`
- Đã cấu hình các đường dẫn:
  - `/polls/articles/2003/`, `/polls/articles/<int:year>/`, ...
  - `/polls/now/`, `/polls/notfound/`, `/polls/forbidden/`, `/polls/created/`, `/polls/asyncnow/`
  - `/polls/about/`, `/polls/books/`, `/polls/asyncview/`, `/polls/template-example/`, `/polls/outside-template/`

### 2. View function

- File: `views/polls/views.py`
- Đã tạo các view function:
  - `special_case_2003`, `year_archive`, `month_archive`, `article_detail`
  - `current_datetime`, `not_found_view`, `permission_denied_view`, `created_view`, `async_current_datetime`
  - `example_template_view`, `example_outside_template_view`

### 3. Class-based view

- File: `views/polls/views.py`
- Đã tạo các class-based view:
  - `AboutView` (TemplateView, dùng template `about.html`)
  - `BookListView` (ListView, dùng template `polls/book_list.html`)
  - `AsyncView` (async class-based view)

### 4. Template

- Thư mục: `views/polls/templates/polls/`, `views/templates/`
- Đã tạo các file template:
  - `about.html` (cho AboutView)
  - `polls/book_list.html` (cho BookListView)
  - `polls/example.html` (cho example_template_view)
  - `example_outside.html` (template ngoài app, cho example_outside_template_view)

---

## Hướng dẫn kiểm tra từng phần

### URL config & View function

- Truy cập các đường dẫn như `/polls/now/`, `/polls/notfound/`, `/polls/articles/2003/` để kiểm tra các view function.

### Class-based view

- Truy cập `/polls/about/`, `/polls/books/`, `/polls/asyncview/` để kiểm tra các class-based view.

### Template

- Truy cập `/polls/template-example/` để kiểm tra template động.
- Truy cập `/polls/outside-template/` để kiểm tra template ngoài app.
