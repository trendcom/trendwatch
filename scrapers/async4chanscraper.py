
import aiohttp
import asyncio
import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print ('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts))
        return result

    return timed



#'https://a.4cdn.org/board/threads.json

@timeit
async def get_threadnumbers(threadnumbers):
    url = 'https://a.4cdn.org/biz/threads.json'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
    for dict in data:
        for thread in dict['threads']:
            threadnumbers.append(thread['no'])

@timeit
async def get_threadcomments(thread_dict, threadnumber):
    strthreadnumber = str(threadnumber)
    url = 'https://a.4cdn.org/biz/thread/xxx.json'
    url = url.replace('xxx', strthreadnumber)
    async with aiohttp.ClientSession() as session:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()

            data = data['posts']
            comments = []
            for dict in data:

                try:
                    comment = dict['com']
                    comment = sanitize_comment(comment)
                    comments.append(comment)
                except KeyError:
                    pass
            thread_dict[strthreadnumber] = comments




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

@timeit
def main():
    threadnumbers = []
    thread_dict = {}
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_threadnumbers(threadnumbers))
    loop.run_until_complete(
        asyncio.gather(
            *(get_threadcomments(thread_dict, threadnumber) for threadnumber in threadnumbers)
        )
    )
    print(thread_dict)


if __name__ == "__main__":
    main()








