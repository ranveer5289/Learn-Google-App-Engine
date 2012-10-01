import helloworld
from google.appengine.api import mail


obj = helloworld.helloworld()
mail_body = obj.parse_feed()
mail.send_mail(sender="ranveer.raghu@gmail.com",
                to="ranveer.raghu@gmail.com",
                subject="TVSeries Schedule",
                body=mail_body)
