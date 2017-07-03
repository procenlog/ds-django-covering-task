from datetime import date

def copyright_context_processor(request):
    dict = {'start_year' : 2015,
            'end_year' : date.today().year }
    return dict