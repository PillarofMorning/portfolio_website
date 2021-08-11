from kivy.app import App
import datetime
from datetime import date, timedelta
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import dateutil.parser as dparser


# define our different screens
class FirstScreen(Screen):
    today = date.today()

    def expiration(self, till_expiration):
        return self.today + timedelta(days=till_expiration)

    def datestdtojd(self, stddate):
        fmt = '%Y-%m-%d'
        sdtdate = datetime.datetime.strptime(stddate, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        return (jdate)

    def callback(self, instance):
        name = self.ids.name_input.text
        self.ids.name_label.text = "todays date:\n " + str(self.today) + "  julian date: " + str(
            self.datestdtojd(str(self.today))) \
                                   + "\n\n70 days from now it will be:\n " + str(
            self.expiration(70)) + "  julian date: " + str(self.datestdtojd(str(self.expiration(70)))) \
                                   + "\n\n60 days from now it will be:\n " + str(
            self.expiration(60)) + "  julian date: " + str(self.datestdtojd(str(self.expiration(60)))) \
                                   + "\n\n55 days from now it will be:\n " + str(
            self.expiration(55)) + "  julian date: " + str(self.datestdtojd(str(self.expiration(55))))

        if name:
            self.ids.name_label.text = str(name) + " days from now it will be: " + "\n" + str(
                self.expiration(int(name))) + \
                                       " julian date: " + str(self.datestdtojd(str(self.expiration(int(name)))))
        else:
            self.ids.name_label.text = "please enter a valid expiration limit"




class SecondScreen(Screen):

    def datestdtojd(self, stddate):
        fmt = '%Y-%m-%d'
        sdtdate = datetime.datetime.strptime(stddate, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        return (jdate)

    def expiration(self, date):
        expirations = [55, 60, 70, 90]
        date = dparser.parse(str(date),fuzzy=True)
        cexpiration = [str(date + timedelta(days=expiration)).split(' ')[0]for expiration in expirations]
        return cexpiration

    def callback2(self, instance):
        name = self.ids.cde_input.text
        dates = self.expiration(name)
        self.ids.cde.text = "55 days: "  + dates[0] + "\n60 days: "+ dates[1] + "\n70 days: "+ dates[2] + "\n90 days: "+ dates[3]



class ThirdScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass

# designate KVY design file
root_widget = Builder.load_file('my.kv')


class MyApp(App):
    def build(self):
        return root_widget


MyApp().run()
