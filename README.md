# StaticScrape

![StaticScrape](https://img.shields.io/badge/version-0.2.1-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📌 Description
StaticScrape is a command-line tool designed to **clone the front end of any website** effortlessly. It retrieves the HTML structure while removing unnecessary scripts to create a clean static version of the webpage.

## 🚀 Features
- Extracts full HTML structure of a given website.
- Automatically removes unnecessary `<script>` tags.
- Uses **Playwright** to handle JavaScript rendering.
- Saves the cloned page as a static `.html` file.
- Simple CLI interface for easy usage.

## 🛠 Installation
You can install **StaticScrape** using pip:
```sh
pip install StaticScrape
```
After installation, ensure Playwright is set up for browser automation:
```sh
playwright install
```

## 📝 Usage
Run StaticScrape from the command line:
```sh
staticscrape
```

## 💡 Example
```sh
staticscrape
Enter URL: https://example.com
Enter output file name: my_clone
✅ Page saved as my_clone.html
```

## 🤝 Contributing
Feel free to contribute! If you find a bug or have a feature request, open an issue or submit a pull request.

## 📜 License
This project is licensed under the **MIT License**.

## 👤 Author
**Anurag Singh Bhandari**  
📧 anuuo3ups@gmail.com  

---

Happy Scraping! 🚀

