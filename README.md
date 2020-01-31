# Python Markdown Ratings

This is an extension for [Python Markdown](https://python-markdown.github.io/)
that lets you add rating stars to your page.

# Usage

- Install the package:

```shell script
pip install markdown-ratings
```

- Add [FontAwesome css](https://fontawesome.com/) to your page.
- Add css to color checked stars:

```css
.star-checked {
    color: orange;
}
```

- Add the Markdown tag to your page:

```markdown
Something amazing with [rating:5]
```

The `rating` value goes from `0` to `5`.