from random import choice
from string import punctuation
from time import sleep
from tkinter import *

def read_file():
    f = open("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\hangman_words.txt", "r")
    textt = f.read().lower()
    n = [i for i in textt.split() if i not in (punctuation , "the", 'or' , 'and' , 'that', 'where', 'who', 'on', 'to', 'betweem')]
    return n

class hangman(object):
    def __init__(self, win: Tk):
        self.sttt = ""

        self.coun_mistake = 1
        self.win = win
        self.win.geometry("%dx%d+%d+%d" % (600, 350, 100, 100))
        self.word = choice(read_file())
        print(self.word)
        self.countt = len(self.word)
        self.str_ = ["_" for _ in range(self.countt)]
        self.l1= Label(self.win, text= " ".join(self.str_), font= "tahoma 18 normal")
        self.l1.place(x = 20, y = 10)

        self.a = Button(self.win, text = 'a', font= "tahoma 14 normal", width= 2, command= self.click_a)
        self.a.place(x = 10, y = 100)

        self.b= Button(self.win, text = 'b', font= "tahoma 14 normal", width= 2, command= self.click_b)
        self.b.place(x = 50, y = 100)

        self.c= Button(self.win, text = 'c', font= "tahoma 14 normal", width= 2, command = self.click_c)
        self.c.place(x = 90, y = 100)

        self.d= Button(self.win, text = 'd', font= "tahoma 14 normal", width= 2, command = self.click_d)
        self.d.place(x = 130, y = 100)

        self.e= Button(self.win, text = 'e', font= "tahoma 14 normal", width= 2, command = self.click_e)
        self.e.place(x = 170, y = 100)

        self.f= Button(self.win, text = 'f', font= "tahoma 14 normal", width= 2, command = self.click_f)
        self.f.place(x = 210, y = 100)

        self.g= Button(self.win, text = 'g', font= "tahoma 14 normal", width= 2, command = self.click_g)
        self.g.place(x = 250, y = 100)

        self.h= Button(self.win, text = 'h', font= "tahoma 14 normal", width= 2, command = self.click_h)
        self.h.place(x = 290, y = 100)

        self.i= Button(self.win, text = 'i', font= "tahoma 14 normal", width= 2, command = self.click_i)
        self.i.place(x = 10, y = 150)

        self.j= Button(self.win, text = 'j', font= "tahoma 14 normal", width= 2, command = self.click_j)
        self.j.place(x = 50, y = 150)

        self.k= Button(self.win, text = 'k', font= "tahoma 14 normal", width= 2, command = self.click_k)
        self.k.place(x = 90, y = 150)

        self.l= Button(self.win, text = 'l', font= "tahoma 14 normal", width= 2, command = self.click_l)
        self.l.place(x = 130, y = 150)
 
        self.m= Button(self.win, text = 'm', font= "tahoma 14 normal", width= 2, command = self.click_m)
        self.m.place(x = 170, y = 150)

        self.n= Button(self.win, text = 'n', font= "tahoma 14 normal", width= 2, command = self.click_n)
        self.n.place(x = 210, y = 150)

        self.o= Button(self.win, text = 'o', font= "tahoma 14 normal", width= 2, command = self.click_o)
        self.o.place(x = 250, y = 150)
 
        self.p= Button(self.win, text = 'p', font= "tahoma 14 normal", width= 2, command = self.click_p)
        self.p.place(x = 290, y = 150)

        self.q= Button(self.win, text = 'q', font= "tahoma 14 normal", width= 2, command = self.click_q)
        self.q.place(x = 10, y = 200)

        self.r= Button(self.win, text = 'r', font= "tahoma 14 normal", width= 2, command = self.click_r)
        self.r.place(x = 50, y = 200)
 
        self.s= Button(self.win, text = 's', font= "tahoma 14 normal", width= 2, command = self.click_s)
        self.s.place(x = 90, y = 200)

        self.t= Button(self.win, text = 't', font= "tahoma 14 normal", width= 2, command = self.click_t)
        self.t.place(x = 130, y = 200)

        self.u= Button(self.win, text = 'u', font= "tahoma 14 normal", width= 2, command = self.click_u)
        self.u.place(x = 170, y = 200)

        self.v= Button(self.win, text = 'v', font= "tahoma 14 normal", width= 2, command = self.click_v)
        self.v.place(x = 210, y = 200)

        self.w= Button(self.win, text = 'w', font= "tahoma 14 normal", width= 2, command = self.click_w)
        self.w.place(x = 250, y = 200)

        self.x= Button(self.win, text = 'x', font= "tahoma 14 normal", width= 2, command = self.click_x)
        self.x.place(x = 290, y = 200)

        self.y= Button(self.win, text = 'y', font= "tahoma 14 normal", width= 2, command = self.click_y)
        self.y.place(x = 130, y = 250)

        self.z= Button(self.win, text = 'z', font= "tahoma 14 normal", width= 2, command = self.click_z)
        self.z.place(x = 170, y = 250)

    def click(self, name):
        if name not in self.sttt:
            self.sttt += name
            if name in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == name:
                        self.str_[i] = f" {name} "
                print("".join(i.strip() for i in self.str_) == self.word)
                if "".join(i.strip() for i in self.str_) == self.word:
                    self.ex_page("you win, congratulation!")
                self.ll= Label(self.win, text= "  ".join(self.str_), font= "tahoma 18 normal")
                self.ll.place(x = 20, y = 10)

            else:
                if self.coun_mistake == 1:
                    self.l2 = Label(self.win, text= "_______________", font= "tahoma 14 bold")
                    self.l2.place(x = 380, y = 200)
                    self.coun_mistake += 1
                elif self.coun_mistake == 2:
                    self.l3 = Label(self.win, text = "|\n|\n|\n|\n|", font= "tahoma 14 bold")
                    self.l3.place(x = 550, y = 100)
                    self.coun_mistake += 1
                elif self.coun_mistake == 3:
                    self.l4 = Label(self.win, text= "_________", font= "tahoma 14 bold")
                    self.l4.place(x = 450, y = 80)
                    self.coun_mistake += 1
                elif self.coun_mistake == 4:
                    self.l5 = Label(self.win, text = "|\nO\n/|\\\n/\\", font= "tahoma 14 bold")
                    self.l5.place(x = 440, y = 110)
                    self.a['state'] = DISABLED
                    self.b['state'] = DISABLED
                    self.c['state'] = DISABLED
                    self.d['state'] = DISABLED
                    self.e['state'] = DISABLED
                    self.f['state'] = DISABLED
                    self.g['state'] = DISABLED
                    self.h['state'] = DISABLED
                    self.i['state'] = DISABLED
                    self.j['state'] = DISABLED
                    self.k['state'] = DISABLED
                    self.l['state'] = DISABLED
                    self.m['state'] = DISABLED
                    self.n['state'] = DISABLED
                    self.o['state'] = DISABLED
                    self.p['state'] = DISABLED
                    self.q['state'] = DISABLED
                    self.r['state'] = DISABLED
                    self.s['state'] = DISABLED
                    self.t['state'] = DISABLED
                    self.u['state'] = DISABLED
                    self.v['state'] = DISABLED
                    self.w['state'] = DISABLED
                    self.x['state'] = DISABLED
                    self.y['state'] = DISABLED
                    self.z['state'] = DISABLED
                    sleep(.01)
                    self.ex_page("you are fail the word is {}".format(self.word.upper()))


    def ex_page(self, text):
        self.wi = Tk()
        Label(self.wi, text= text, font="tahoma 14 normal").pack()
        Button(self.wi, text= "ok", command= self.dic, font="tahoma 14 normal").pack()
    
    def dic(self):
        self.wi.destroy()
        self.win.destroy()
        

    def click_a(self):
        self.click("a")

    def click_b(self):
        self.click("b")        

    def click_c(self):
        self.click("c")  


    def click_d(self):
        self.click("d")  


    def click_e(self):
        self.click("e")  


    def click_f(self):
        self.click("f")  


    def click_g(self):
        self.click("g")  


    def click_h(self):
        self.click("h")  


    def click_i(self):
        self.click("i")  


    def click_j(self):
        self.click("j")  


    def click_k(self):
        self.click("k")  

    def click_l(self):
        self.click("l")  


    def click_m(self):
        self.click("m")  


    def click_n(self):
        self.click("n")  


    def click_o(self):
        self.click("o")  


    def click_p(self):
        self.click("p")  


    def click_q(self):
        self.click("q")  


    def click_r(self):
        self.click("r")  


    def click_s(self):
        self.click("s")  


    def click_t(self):
        self.click("t")  

    def click_u(self):
        self.click("u")  


    def click_v(self):
        self.click("v")  


    def click_w(self):
        self.click("w")  


    def click_x(self):
        self.click("x")  


    def click_y(self):
        self.click("y")  


    def click_z(self):
        self.click("z")  

w = Tk()
hangman(w)
w.mainloop()