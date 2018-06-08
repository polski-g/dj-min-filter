Django .min. Filter
===

Template filter to insert .min just before .js/.css when in DEBUG mode.
Does **not** do any minification, for that, see django-compressor.


Quickstart
===

Install Django .min. Filter:

    pip install -e git+https://github.com/polski-g/dj-min-filter
    
Add it to your `INSTALLED_APPS`:
    
    INSTALLED_APPS = (
        ...
        'min_filter',
        ...
    )
    
    
Usage
===
In your templates,

    {% load min_filter %}
    ...
    {% static 'myresource-1.23.js'|min %}
