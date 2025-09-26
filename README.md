# 🛠️ Static Site Generator in Python

A lightweight and modular **Static Site Generator (SSG)** built in Python from scratch. Converts Markdown files into fully-structured, clean HTML pages — with support for inline and block-level elements, asset management, and more. No frameworks, no fluff — just Python and good design.

---

## 🚀 Features

✅ **Markdown to HTML conversion**  
Seamlessly parses `.md` files into clean, semantic HTML.

✅ **Inline element handling**  
Supports bold, italic, inline code, links, and more.

✅ **Block-level support**  
Handles headings, paragraphs, lists, blockquotes, and code blocks with proper HTML structure.

✅ **Object-Oriented Architecture**  
Clean, modular codebase using OOP principles and recursion — easy to extend and maintain.

✅ **Static Asset Management**  
Automatically copies static assets like CSS, images, and JavaScript to the output folder.

✅ **Fully Functional Website Generator**  
Generates a ready-to-deploy static website from your Markdown content and assets.

---

## 🧪 How It Works

1. **Parses Markdown**: Reads and processes `.md` files using custom parsing logic.
2. **Generates HTML**: Converts each file into valid HTML with support for inline and block elements.
3. **Copies Assets**: Moves CSS, images, and other static files to the output directory.
4. **Builds Website**: Outputs a complete folder with all HTML pages and assets ready to be hosted.

---

## Example

### Convert this Markdown:
```
# Hello World

This is a **bold** word and *italic* word.

Visit [Google](https://google.com).
```

### To HTML:
```
<h1>Hello World</h1>
<p>This is a <strong>bold</strong> word and <em>italic</em> word.</p>
<p>Visit <a href="https://google.com">Google</a>.</p>
```

## 🧱 Built With

- Python 3
- Markdown parsing (custom logic — no external libraries)
- Clean OOP and recursion patterns