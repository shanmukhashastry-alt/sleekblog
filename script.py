# Create a comprehensive HTML/CSS/JavaScript blog template structure
# First, let's create the HTML structure

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleek Blog - Modern & Simple</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h2>SleekBlog</h2>
            </div>
            <ul class="nav-menu">
                <li class="nav-item">
                    <a href="#home" class="nav-link">Home</a>
                </li>
                <li class="nav-item">
                    <a href="#about" class="nav-link">About</a>
                </li>
                <li class="nav-item">
                    <a href="#blog" class="nav-link">Blog</a>
                </li>
                <li class="nav-item">
                    <a href="#contact" class="nav-link">Contact</a>
                </li>
            </ul>
            <div class="nav-toggle" id="mobile-menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero-container">
            <div class="hero-content">
                <h1 class="hero-title">Welcome to My Blog</h1>
                <p class="hero-subtitle">Sharing thoughts, ideas, and stories in a clean, modern design</p>
                <a href="#blog" class="cta-button">Read Latest Posts</a>
            </div>
        </div>
    </section>

    <!-- Featured Posts -->
    <section class="featured-posts" id="blog">
        <div class="container">
            <h2 class="section-title">Featured Posts</h2>
            <div class="posts-grid">
                <article class="post-card">
                    <div class="post-image">
                        <img src="https://via.placeholder.com/400x250/667eea/ffffff?text=Blog+Post+1" alt="Post 1">
                    </div>
                    <div class="post-content">
                        <div class="post-meta">
                            <span class="post-date">Jan 15, 2025</span>
                            <span class="post-category">Technology</span>
                        </div>
                        <h3 class="post-title">The Future of Web Design</h3>
                        <p class="post-excerpt">Exploring the latest trends and technologies shaping the future of web design and user experience.</p>
                        <a href="#" class="read-more">Read More</a>
                    </div>
                </article>

                <article class="post-card">
                    <div class="post-image">
                        <img src="https://via.placeholder.com/400x250/764ba2/ffffff?text=Blog+Post+2" alt="Post 2">
                    </div>
                    <div class="post-content">
                        <div class="post-meta">
                            <span class="post-date">Jan 12, 2025</span>
                            <span class="post-category">Lifestyle</span>
                        </div>
                        <h3 class="post-title">Minimalism in Daily Life</h3>
                        <p class="post-excerpt">How adopting minimalist principles can lead to a more focused and fulfilling lifestyle.</p>
                        <a href="#" class="read-more">Read More</a>
                    </div>
                </article>

                <article class="post-card">
                    <div class="post-image">
                        <img src="https://via.placeholder.com/400x250/f093fb/ffffff?text=Blog+Post+3" alt="Post 3">
                    </div>
                    <div class="post-content">
                        <div class="post-meta">
                            <span class="post-date">Jan 10, 2025</span>
                            <span class="post-category">Design</span>
                        </div>
                        <h3 class="post-title">Color Theory in Modern Design</h3>
                        <p class="post-excerpt">Understanding how colors influence user perception and emotional response in digital design.</p>
                        <a href="#" class="read-more">Read More</a>
                    </div>
                </article>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about" id="about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2 class="section-title">About Me</h2>
                    <p>I'm a passionate writer and designer focused on creating meaningful content and beautiful experiences. This blog is where I share my thoughts on technology, design, and life.</p>
                    <p>Join me on this journey as we explore the intersection of creativity and functionality in our digital world.</p>
                </div>
                <div class="about-image">
                    <img src="https://via.placeholder.com/300x300/4facfe/ffffff?text=About+Me" alt="About Me">
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact" id="contact">
        <div class="container">
            <h2 class="section-title">Get In Touch</h2>
            <div class="contact-content">
                <div class="contact-info">
                    <h3>Let's Connect</h3>
                    <p>Have a question or want to collaborate? I'd love to hear from you.</p>
                    <div class="contact-item">
                        <i class="fas fa-envelope"></i>
                        <span>hello@sleekblog.com</span>
                    </div>
                    <div class="social-links">
                        <a href="#" class="social-link"><i class="fab fa-twitter"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-linkedin"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                <form class="contact-form">
                    <div class="form-group">
                        <input type="text" placeholder="Your Name" required>
                    </div>
                    <div class="form-group">
                        <input type="email" placeholder="Your Email" required>
                    </div>
                    <div class="form-group">
                        <textarea placeholder="Your Message" rows="5" required></textarea>
                    </div>
                    <button type="submit" class="submit-btn">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo">
                    <h3>SleekBlog</h3>
                </div>
                <div class="footer-links">
                    <a href="#home">Home</a>
                    <a href="#about">About</a>
                    <a href="#blog">Blog</a>
                    <a href="#contact">Contact</a>
                </div>
                <div class="footer-social">
                    <a href="#" class="social-link"><i class="fab fa-twitter"></i></a>
                    <a href="#" class="social-link"><i class="fab fa-linkedin"></i></a>
                    <a href="#" class="social-link"><i class="fab fa-github"></i></a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 SleekBlog. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

print("HTML structure created successfully!")
print("Length of HTML content:", len(html_content))