import tornado.ioloop
import tornado.web
import json
import random
import authentication as verify
import util
import database

#=
class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        info = ""
        self.render('login.html', info = info)

    def post(self, *args, **kwargs):
        # verify account and password
        account=self.get_argument('account')
        passwd=self.get_argument('passwd')
        auth = verify.auth(account, passwd)

        # if pass, continue to get cf based recommendation
        if(str(auth) == 'err1' or str(auth) == 'err2'):
            info = "Wrong Password or Account"
            return self.render('index.html', info = info)

        else:
            user = [account, passwd, str(auth)]
            print("Verification Passed", auth)

        # send unique id to get recommenation of content
        id = auth
        topic = 'id'
        msg = id
        print("Start sending ID to Kafka")
        util.kafkasend(topic, msg)

        # receive recommendation content and return to front end
        print("Set Consumer")
        consumer = util.setConsumer('cf_item')
        print("Start Receive Kafka")
        while True:
            reco = util.kafkareceive(consumer)
            if(reco != None):
                break

        # receive 5 recommendation items
        #items_cf = ["Kimi no Na wa.", "Fullmetal Alchemist: Brotherhood", "Gintama°", "Steins;Gate", "Hunter x Hunter (2011)"]
        item_cf = reco
        items_cf = util.buildhtml(item_cf)


        self.write("<h1>CF Recommendation</h1>")
        self.write(items_cf)
        return self.render("index.html", title="Recommentaion",user = user)

# Test Page Handler
class TestHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # Content Based Result
        recommendation = ['a','b','c','d','e']
        items = ""
        # Construct Items list
        for i in range(len(recommendation)):
            strbase = "<div onclick = 'get(this.id)' id = '%s'> %s </div>"%(recommendation[i], recommendation[i])
            items = items + '<tr>' + strbase +' </tr>'
        # srite back
        self.write(items)
        return self.render("test.html")

# Ajax Handler, to make content-based recommendation
class AjaxHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):

        # Get item name to make content based recommendation
        item = self.get_argument('item')
        print(item)

        # Get recommendation result from database
        data = database.get_similar_item(item)
        ##Test Data
        #data = list(random.sample(['1','2','3','4','5'], 5))

        # write back as a response to ajax
        names = util.buildhtml(data)
        print(names)
        self.write(names)



settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'debug':True
}

application = tornado.web.Application([
    (r"/index", MainHandler),(r"/test", TestHandler),(r"/ajax", AjaxHandler)
], **settings)


if __name__ == "__main__":
    application.listen(5050)
    tornado.ioloop.IOLoop.instance().start()
