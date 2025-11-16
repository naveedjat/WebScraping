# 🌐 Web Scraping

In this project I will dive deep into  **web scraping with Python**. where I will be exploring foundational libraries like `requests` and `BeautifulSoup`, as well as advanced libraries and frameworks like `Selenium` and `Scrapy`. Along the way, I will learn the  key methods and concepts that will make the scraping websites easier and more faster.

---

## 📚 Libraries Covered

- **Requests**: For making HTTP requests and handling responses.  
- **BeautifulSoup**: For parsing and navigating HTML content.  
- **Selenium**: For automating browsers, handling dynamic content, and interacting with JavaScript-heavy sites.  
- **Scrapy**: A powerful framework for large-scale web scraping with asynchronous support and built-in project management.

---

## 🔍 Key Concepts and Methods Learned

### 1️⃣ Requests Library
- **HTTP Methods**: `GET` for retrieving web pages.  
- **Status Codes**:  
  - `200` → Success  
  - `404` → Not Found  
  - `403` → Forbidden  
  - `500` → Server Error  
- **Response Attributes**:  
  - `response.content` → Raw binary content  
  - `response.text` → Decoded text content  
  - `response.headers` → Metadata about the response  
  - `response.cookies` → Cookies sent by the server  
  - `response.elapsed` → Time taken for the server to respond  

---

### 2️⃣ BeautifulSoup Library
- **HTML Parsing**: Use `html.parser` to parse HTML content.  
- **Objects in BeautifulSoup**:  
  - **Tags** → Represents HTML tags like `<p>` or `<a>`  
  - **NavigableString** → Text content inside tags  
  - **Comment** → HTML comments  
  - **ResultSet** → Collection of matching elements (e.g., all paragraphs)  
- **Key Methods**:  
  - `find_all()` → Find all matching elements based on tags or attributes  
  - `prettify()` → Format HTML for readability  
  - `.text` → Extract text inside a tag  
  - `find()` → Retrieve the first matching element  

---

### 3️⃣ Selenium Library
- **Browser Automation**: Open pages, click buttons, scroll, fill forms.  
- **Dynamic Content Handling**: Works with JavaScript-rendered sites.  
- **Key Methods**:  
  - `driver.get(url)` → Open a webpage  
  - `driver.find_element_by_*()` → Locate elements  
  - `driver.click()` → Click buttons or links  
  - `driver.quit()` → Close the browser  

---

### 4️⃣ Scrapy Framework
- **Purpose**: Efficiently scrape large datasets and multiple pages asynchronously.  
- **Features**:  
  - Manages requests, retries, and rate limits  
  - Organizes scraping projects with spiders  
  - Handles pipelines for storing and cleaning data  

---
