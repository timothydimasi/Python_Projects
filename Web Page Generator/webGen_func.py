import webbrowser

import webGen_gui
import webGen_main


def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo



if __name__ == "__main__":
    pass