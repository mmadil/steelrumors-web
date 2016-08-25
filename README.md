steelrumors
==============================

This project contains further enhancements on top of [Building a Hacker News clone in Django][arocks-post] by [Arun Ravindran][github-source]

[arocks-post]: http://arunrocks.com/building-a-hacker-news-clone-in-django-part-1/
[github-source]:https://github.com/arocks/steel-rumors

### Stack

- Python 3
- Django 1.10
- Postgresql


## Installation

Minimum requirements: **pip, fabric3 & [postgres][install-postgres]**, setup is tested on Mac OSX only.

```
brew install postgres
[sudo] pip install fabric3
```

[install-postgres]: http://www.gotealeaf.com/blog/how-to-install-postgresql-on-a-mac

In your terminal, type or copy-paste the following:

    git clone git@github.com:mmadil/steelrumors-web.git; cd steelrumors-web; fab init

Go grab a cup of coffee until we bake your hot development machine.

Useful commands:

- `fab serve` - start [django server](http://localhost:8000/)

**NOTE:** Checkout `fabfile.py` for all the options available and what/how they do it.

## Feature and Requirements

- [x] User authentication via custom user model.
- [x] Users can manage their profile information.
- [x] Users can post links.
- [x] Users can vote links using AJAX.
- [ ] Add tests.
- [ ] Refactor.


## License

MIT License

Copyright (c) 2016 Mohammad Adil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
