def make_readable(seconds):
    make_readable = lambda x : x if len(x) == 2 else '0' + x
    
    hours = make_readable(str(seconds // (60*60)))
    seconds = seconds % (60*60)
    minutes = make_readable(str(seconds // 60))
    seconds = make_readable(str(seconds % 60))
    
    return f"{hours}:{minutes}:{seconds}"