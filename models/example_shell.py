from polls.models import Author, Book
a1 = Author.objects.create(name="Haruki Murakami", birth_year=1949)
a2 = Author.objects.create(name="J.K. Rowling", birth_year=1965)
b1 = Book.objects.create(title="Kafka on the Shore", published_year=2002, author=a1)
b2 = Book.objects.create(title="Norwegian Wood", published_year=1987, author=a1)
b3 = Book.objects.create(title="Harry Potter and the Goblet of Fire", published_year=2000, author=a2)

# Lấy tất cả các tác giả
Author.objects.all()

# Lấy tất cả các sách
Book.objects.all()

# Lấy sách của một tác giả cụ thể
Author.objects.get(name="Haruki Murakami").books.all()

# Lấy tác giả của một cuốn sách
Book.objects.get(title="Norwegian Wood").author

# Lọc sách xuất bản sau năm 1990
Book.objects.filter(published_year__gt=1990)

# Lọc tác giả có năm sinh trước 1960
Author.objects.filter(birth_year__lt=1960)

# Đếm số sách của một tác giả
a1.books.count()

# Lấy sách đầu tiên của một tác giả
a1.books.first()

# Lấy tất cả sách của J.K. Rowling
a2.books.all()

# Lấy tất cả sách có tiêu đề bắt đầu bằng "Harry"
Book.objects.filter(title__startswith="Harry")

# Xóa một cuốn sách
b2.delete()

# Cập nhật năm xuất bản của một cuốn sách
b1.published_year = 2003
b1.save()

# Lấy tất cả tác giả có ít nhất một cuốn sách xuất bản sau năm 1990
Author.objects.filter(books__published_year__gt=1990).distinct()


# Complex Queries Q
from django.db.models import Q

# Tác giả có tên bắt đầu bằng "J" hoặc sinh sau năm 1950
Author.objects.filter(Q(name__startswith="J") | Q(birth_year__gt=1950))

# Sách có tiêu đề chứa "Wood" và xuất bản trước năm 1990
Book.objects.filter(Q(title__icontains="wood") & Q(published_year__lt=1990))

# Sách không phải của "J.K. Rowling"
Book.objects.exclude(author__name="J.K. Rowling")

# Sách có tiêu đề chứa "Harry" hoặc xuất bản sau năm 2000
Book.objects.filter(Q(title__icontains="harry") | Q(published_year__gt=2000))

# Tác giả có ít nhất một cuốn sách xuất bản năm 2000 hoặc 2002
Author.objects.filter(books__published_year__in=[2000, 2002]).distinct()

# Sách của tác giả sinh trước 1960 và tiêu đề không chứa "Kafka"
Book.objects.filter(Q(author__birth_year__lt=1960) & ~Q(title__icontains="kafka"))

# Sách có tiêu đề chứa "Potter" hoặc tác giả sinh sau năm 1960
Book.objects.filter(Q(title__icontains="potter") | Q(author__birth_year__gt=1960))

# Tác giả không có sách nào xuất bản trước năm 1990
Author.objects.exclude(books__published_year__lt=1990)

# Sách của tác giả tên chứa "Rowling" và xuất bản từ năm 1995 đến 2005
Book.objects.filter(Q(author__name__icontains="rowling") & Q(published_year__gte=1995) & Q(published_year__lte=2005))