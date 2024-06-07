# DRF Book API

![django](https://img.shields.io/badge/django-5.0.6-blue)
![DRF](https://img.shields.io/badge/DRF-3.15.1-blue)
![pillow](https://img.shields.io/badge/pillow-10.3.0-blue)

---

### This API allows the user to receive information about the list of books, each book separately and its picture.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setting all private data in .env in booksapi app:**

    ```bash
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_HOST=your_database_host
    DB_PORT=your_database_port
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

### Endpoints
- **List Books**: `GET api/v1/all-books/`
  - Retrieve a list of books.

- **Book Detail**: `GET api/v1/all-books/<int:pk>/`
  - Retrieve detailed information about a specific book.

- **Book Image**: `GET api/v1/image/<int:pk>/`
  - Retrieve the image of a specific book.

### Pagination
- The list of books endpoint supports pagination.

## Author

- Vladimir Petrov [@gumballton](https://github.com/Gumballton)