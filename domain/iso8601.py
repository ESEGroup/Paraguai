from datetime import datetime

isoformat = "%Y-%m-%dT%H:%M:%SZ"
def from_iso(string):
    return datetime.strptime(string, isoformat)

def to_iso(dt):
    return dt.strftime(isoformat)
