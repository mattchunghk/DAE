import json
from sseclient import SSEClient as EventSource

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
with open('new_pages.csv', 'a') as f:
    for event in EventSource(url):
        if event.event == 'message':
            try:
                content = json.loads(event.data)
            except ValueError:
                pass
            else:
                if content['type'] == "edit":
                    print(content['title'], content['comment'])
