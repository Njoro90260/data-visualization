from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts, hn_title, hn_comments = [], [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    # print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    # submission_dicts.append(submission_dict)
    hn_title.append(response_dict['title'])
    hn_comments.append(response_dict['descendants'])

def shorten_string(s, max_length=30):
    if len(s)> max_length:
        return s[:max_length].rstrip() + "..."
    return s

short_hn_title = [shorten_string(item) for item in hn_title]
# Make a visualization.
data = [{
    'type': 'bar',
    'x': short_hn_title,
    'y': hn_comments,
}]

my_layout = {
    'title': 'Top commented news on hacker news.',
    'xaxis': {
        'title': 'news title'
    },
    'yaxis': {
        'title': 'comments'
    }
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news_visualization.html')
# submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# for submission_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discussion link: {submission_dict['hn_link']}")
#     print(f"comments: {submission_dict['comments']}")