import requests
def data():
    r=requests.get("https://drive.google.com/open?id=1s14HqKZcZkEArah1MDy8kpG9JFeC4YfGxBCEgnELXQk")
    data=r.text.split("content")[9].split("><")[0]
    return (data[2:-1])
