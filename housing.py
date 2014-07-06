


from fred.fred import Fred
import reportlab
from reportlab import platypus
import matplotlib
from pprint import pprint

from datetime import datetime


def str2dt(s): return datetime.strptime(s, '%Y-%m-%d')




#fredob = Fred()

def fred_demo():
    try:
        cat = Fred().category(category_id=125)
        rels = Fred().releases('dates', limit=10)
        ser = Fred().release('series', release_id=51)
        search = Fred().series('search', search_text="money stock")
        srcs = Fred().sources()
        src = Fred().source(source_id=51)
    finally: globals().update(locals())


def use_fred():
    try:
        if 0:
            search = Fred().series('search', search_text="money stock")
            t1 = [ob.title for ob in search.seriess.series]
            # One of the nice things about Z Williams api code is the
            # transparent conversion between dot/dict notation.
            t2 = [ob.title for ob in search['seriess']['series']]
            
            search = Fred().series('search', search_text="housing")   #1000
            search = Fred().series('search', search_text="house price") #300
            search = Fred().series('search', search_text="house price denver") #
            search = Fred().series('search', search_text="denver") # 93

            search = Fred().series('search', search_text="home price index") #314
            search = Fred().series('search', search_text="home price index chicago") #
            t3 = [ob.title for ob in search.seriess.series]
        sid = 'DNXRSA'  # denver housing 
        rel = Fred().series('release', series_id=sid) #
        obs = Fred().series('observations', series_id=sid) #
        x = [ob for ob in obs.observations.observation]
    finally: globals().update(locals())



def city_data(sid):
    try:
        obs = Fred().series('observations', series_id=sid) #
        obs = obs.observations.observation
        dat = [(str2dt(ob.date), float(ob.value)) for ob in obs]
        return dat
    finally: globals().update(locals())


class housing(object):
    def __init__(self):
        self.cityd = dict(
            denver = city_data('DNXRSA'),
            chicago = city_data('CHXRSA'),
            miami = city_data('MIXRSA'),
        )

    def city(self, name):
        return self.cityd[name]

hd = housing()
cd = hd.city('denver')
cc = hd.city('chicago')
cm = hd.city('miami')




from cStringIO import StringIO

#matplotlib.use('Agg')
#matplotlib.use('macosx')
from matplotlib import figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

try:
    from plt_graphic import plot_as_string
except:
    def plot_as_string(canvas, fmt):
        img_file = StringIO()
        canvas.print_figure(img_file, format=fmt)
        return img_file.getvalue()





def fig_test(interactive=True):
    try:
        if interactive:
            import matplotlib.pyplot as plt
            fig = plt.figure()
        else:
            fig = figure.Figure(figsize=(3,3), dpi=120)
            canvas = FigureCanvasAgg(fig)
        ax = fig.add_subplot(111)
        ax.plot(range(3))

        
        x = [dt.toordinal() for (dt,p) in cd]
        m = min(x)
        x = [n-m for n in x]
        y = [p for (dt,p) in cd]
        ax.plot(x,y)


        if interactive:
            plt.show()
        else:
            fig_string1 = plot_as_string(canvas, 'svg')
            fig_string2 = plot_as_string(canvas, 'png')
    finally: globals().update(locals())


pylogo = '~/python-logo.py'
def reportlab_test(): 
    try:
        pass
    finally: globals().update(locals())


def f():
    try:
        pass
    finally: globals().update(locals())



# C-r C-o x    == insert register x without auto crap.
def f():
    try:
        pass
    finally: globals().update(locals())

# yoo


