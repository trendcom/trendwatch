from scrapers.JSONscraper import fetch_data


# https://github.com/4chan/4chan-API API for JSON to 4chan


# fetches every threadnumber in the board /biz/
# TODO specify how many pages of the board to fetch threadnumbers from
def get_threadnumbers():

    thread_catalog = fetch_data('https://a.4cdn.org/biz/threads.json')
    threadnumbers = []

    for dict in thread_catalog:
        for thread in dict['threads']:
            threadnumbers.append(thread['no'])

    return threadnumbers[1:]


# gets the JSON data from the thread with that threadnumber
def get_thread(thread_number):
    thread_number = str(thread_number)
    preamble = "https://a.4cdn.org/biz/thread/xxx.json"
    preamble = preamble.replace('xxx',thread_number)
    thread = fetch_data(preamble)
    return thread

# gets the posts from the thread with that threadnumber
def get_posts(thread_number):
    thread_data = get_thread(thread_number)
    posts = thread_data['posts']
    return posts
# gets the comments from the thread with that threadnumber, a bunch of strings in a list.
def get_thread_comments(thread_number):
    posts = get_posts(thread_number)
    thread_comments = []
    for post in posts:
        try:
            comment = post['com']
            comment = sanitize_comment(comment)
            thread_comments.append(comment)
        except KeyError:
            pass


    return thread_comments

# sanitizes comments, helperfunction not really needed.
def sanitize_comment(comment):

    if comment.startswith('<a href'):
        quotelink_end = comment.find('<br>')
        comment = comment[quotelink_end+4:]
    comment = comment.replace('<span class="quote">','')
    comment = comment.replace('</span>','')
    comment = comment.replace('&gt;','>')
    comment = comment.replace('&#039;',"'")
    comment = comment.replace('&quot;','"')
    comment = comment.replace('<br>',' ')
    return comment


# gets ALL comments from every thread on the /biz/ board, and puts them in a list.
def get_all_comments():
    thread_numbers = get_threadnumbers()
    comments = []

    for thread_ID in thread_numbers:
        comments.extend(get_thread_comments(thread_ID))

    return comments

# TODO move over functions relating to comments over to a new file
# sees how many times a specific substring is mentioned for a list of comments.
def mentions(comment_list, substring):   # substring needs to be surrounded with whitespace for python to match it as a word.

    mentions = 0

    for comment in comment_list:
        comment = comment.lower()
        if substring in comment:
            mentions+=1


    return mentions


















