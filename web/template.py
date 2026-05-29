"""Template rendering with XSS vulnerabilities."""


def render_welcome(username: str) -> str:
    """Render welcome message - XSS vulnerability."""
    # Direct string interpolation without escaping
    return f"<h1>Welcome, {username}!</h1>"


def render_comment(comment: str, author: str) -> str:
    """Render user comment - multiple XSS vectors."""
    # No input sanitization
    html = f"""
    <div class="comment">
        <p class="author">{author}</p>
        <p class="content">{comment}</p>
        <script>var userData = '{author}';</script>
    </div>
    """
    return html


def build_url(base: str, params: dict) -> str:
    """Build URL from parameters - open redirect."""
    # No validation of redirect URL
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base}?{query}"


def render_search_results(query: str, results: list) -> str:
    """Render search results - reflected XSS."""
    output = f"<h2>Results for: {query}</h2>\n<ul>"
    for item in results:
        output += f"<li>{item['title']}</li>"
    output += "</ul>"
    return output
