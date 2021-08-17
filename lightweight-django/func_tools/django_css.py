def django_css(*args, **kwargs):
    return f"<h1 style='text-align:{kwargs.get('textAlign', '')};\
                        font-size: {kwargs.get('fontSize', '')};\
                        margin-top: {kwargs.get('marginTop', '')};\
                        color: {kwargs.get('color', '')};\
                        '>\
                {kwargs.get('text', '')}\
            </h1>"
