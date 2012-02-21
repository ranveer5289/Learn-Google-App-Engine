import feedparser

class helloworld():
        def parse_feed(self):
                feed_url = 'http://www.myepisodes.com/rss.php?feed=tomorrow&showignored=1&onlyunacquired=1&uid=ranveer5289&pwdmd5=90f2c9c53f66540e67349e0ab83d8cd0'

                rss_parsed = feedparser.parse(feed_url)

                episode_info = []

                for i in xrange(len(rss_parsed.entries)):
                        title =  rss_parsed.entries[i].title
                        title = title.replace('[','').replace(']','').strip()
                        episode_info.append(title)


                mail_body = "\n".join(episode_info)
                return mail_body
