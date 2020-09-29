from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import time
import calendar
from tkcalendar import *



class pclander:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x500")
        self.root.title("Calendar Makes Fun")
        self.root.resizable(0,0)
        self.root.iconbitmap("cale.ico")

        Days=StringVar()
        Months=StringVar()
        Years=StringVar()

        


        #def__Hower_on_buttons_________________==========
        def on_enter1(e):
            But_Show_Calander['background']="black"
            But_Show_Calander['foreground']="cyan"
  
        def on_leave1(e):
            But_Show_Calander['background']="SystemButtonFace"
            But_Show_Calander['foreground']="SystemButtonText"

        def on_enter2(e):
            But_Birth_this_year['background']="black"
            But_Birth_this_year['foreground']="cyan"
  
        def on_leave2(e):
            But_Birth_this_year['background']="SystemButtonFace"
            But_Birth_this_year['foreground']="SystemButtonText"

        def on_enter3(e):
            But_Days_tills_alive['background']="black"
            But_Days_tills_alive['foreground']="cyan"
  
        def on_leave3(e):
            But_Days_tills_alive['background']="SystemButtonFace"
            But_Days_tills_alive['foreground']="SystemButtonText"
        
        def on_enter4(e):
            But_Clear['background']="black"
            But_Clear['foreground']="cyan"
  
        def on_leave4(e):
            But_Clear['background']="SystemButtonFace"
            But_Clear['foreground']="SystemButtonText"

        def on_enter5(e):
            But_Exit['background']="black"
            But_Exit['foreground']="cyan"
  
        def on_leave5(e):
            But_Exit['background']="SystemButtonFace"
            But_Exit['foreground']="SystemButtonText"

        def on_enter6(e):
            But_left_birthdays_days['background']="black"
            But_left_birthdays_days['foreground']="cyan"
  
        def on_leave6(e):
            But_left_birthdays_days['background']="SystemButtonFace"
            But_left_birthdays_days['foreground']="SystemButtonText"
        
        def on_enter7(e):
            But_Months_till_alive['background']="black"
            But_Months_till_alive['foreground']="cyan"
  
        def on_leave7(e):
            But_Months_till_alive['background']="SystemButtonFace"
            But_Months_till_alive['foreground']="SystemButtonText"

        def on_enter8(e):
            But_Years_old['background']="black"
            But_Years_old['foreground']="cyan"
  
        def on_leave8(e):
            But_Years_old['background']="SystemButtonFace"
            But_Years_old['foreground']="SystemButtonText"


        




        #def_on_buttons=========================
        def Exit():
            iExit=tkinter.messagebox.askyesnocancel("Information System","you want to exit system")
            if iExit ==True:
                 root.destroy()
                 return

        
        def Clear():
            TXT.delete("1.0",END)
            TXT.config(bg="white")
            

        def days_live():
            
            if Days.get()=="Day" or Months.get()=="Month" or Years.get()=="Year":
                tkinter.messagebox.askretrycancel("Information","Select your birthdate",icon="info")
            else:
                Clear()
                a=datetime.datetime.now()
                birth_date=datetime.date(int(Years.get()),int(Months.get()),int(Days.get()))
                todays_date=datetime.date(a.year,a.month,a.day)
                days_lives=todays_date-birth_date
                TXT.config(bg="black",fg="red")
                TXT.insert(END,"\t Let's Find Out How Many Day's You Are Alive From Your Birth ")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t So Your BirthDate Is = "+Years.get()+"-"+Months.get()+"-"+Days.get())
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t And Today's Date Is = ")
                TXT.insert(END,date.today())
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t The Day's You Have Lived Up Till Today Is = ")
                TXT.insert(END,days_lives.days)
                TXT.insert(END," days  ")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END," THATS SUPER IMPRESIVE   ")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END," The thing I want to say is  wake up now you have waisted so many days in your life  go and do somthing ")
                TXT.insert(END,"before you die work hard and make your life good")


        def show_calnder():
            if Years.get()=="Year":
                tkinter.messagebox.askretrycancel("Information","Select An year",icon="info")
            else:
                root=Toplevel(self.root)
                get_years=int(Years.get())
                cal_content=calendar.calendar(get_years)
                Lab_calander=Label(root,text=cal_content,font="Consolas 10 bold")
                Lab_calander.grid(row=0,column=0,padx=20)
                root.resizable(0,0)
            #TXT.insert(END,cal_content)
            #TXT.grid(row=4,column=1,padx=5)
            
        
        def search_date():
            if Days.get()=="Day" or Months.get()=="Month" or Years.get()=="Year":
                tkinter.messagebox.askretrycancel("Information","Select your Birth Date",icon="info")
            else:
                root1=Toplevel(self.root)
                get_years=int(Years.get())
                get_months=int(Months.get())
                get_days=int(Days.get())
                cal=Calendar(root1,selectmode='day',year=get_years,month=get_months,day=get_days)
                cal.pack(fill="both",expand=True)
                root1.resizable(0,0)

               

               
         

        def left_birthdays():
            a=datetime.datetime.now()
            todays_date=datetime.date(a.year,a.month,a.day)
            get_years=int(Years.get())
            get_months=int(Months.get())
            get_days=int(Days.get())
            select_date=datetime.date(get_years,get_months,get_days)
            if select_date < todays_date:
                tkinter.messagebox.askretrycancel("Error","Select the birthdate of this year",icon="error")     
            else:
                Clear()
                a=datetime.datetime.now()
                birth_date=datetime.date(int(Years.get()),int(Months.get()),int(Days.get()))
                todays_date=datetime.date(a.year,a.month,a.day)
                days_left_for_birthdays=birth_date-todays_date
                TXT.config(bg="black",fg="red")
                TXT.insert(END,"\t Let's Find Out How Many Day's are left for  Your Birth ")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t So Your BirthDate of this year Is = "+Years.get()+"-"+Months.get()+"-"+Days.get())
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t And Today's Date Is = ")
                TXT.insert(END,date.today())
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t The days left for your birthdays are = ")
                TXT.insert(END,days_left_for_birthdays.days)
                TXT.insert(END," days")


        def years_old():
            if Days.get()=="Day" or Months.get()=="Month" or Years.get()=="Year":
                tkinter.messagebox.askretrycancel("hello","Select days or Months or year")

            else:
                Clear()
                now=date.today()
                birth_date=datetime.date(int(Years.get()),int(Months.get()),int(Days.get()))
                rtls=relativedelta(now,birth_date)
                years_=rtls.years
                months_=rtls.months
                days_=rtls.days
                TXT.config(bg="black",fg="red")
                TXT.insert(END,"\t\t Let's Find Out What's Your Running Age Is ")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t So Your BirthDate Is = "+Years.get()+"-"+Months.get()+"-"+Days.get())
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t And Today's Date Is = ")
                TXT.insert(END,date.today())
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t Your Current Age Is =  ")
                TXT.insert(END,years_)
                TXT.insert(END," years old")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t Your Running Age Is = ")
                TXT.insert(END,years_)
                TXT.insert(END," years ")
                TXT.insert(END," ")
                TXT.insert(END,months_)
                TXT.insert(END," months ")
                TXT.insert(END,days_)
                TXT.insert(END," days   old")


        def months_left():
            if Days.get()=="Day" or Months.get()=="Month" or Years.get()=="Year":
                tkinter.messagebox.askretrycancel("Error","Select your birthdate")
            else:
                Clear()
                now=date.today()
                birth_date=datetime.date(int(Years.get()),int(Months.get()),int(Days.get()))
                rtls=relativedelta(now,birth_date)
                months_left_till=rtls.years*12+rtls.months
                TXT.config(bg="black",fg="red")
                TXT.insert(END,"\t\t Let's Find Out What's Your Running Age Is ")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t So Your BirthDate Is = "+Years.get()+"-"+Months.get()+"-"+Days.get())
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t And Today's Date Is = ")
                TXT.insert(END,date.today())
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END,"\t The Day's You Have Lived Up Till Today Is = ")
                TXT.insert(END,months_left_till)
                TXT.insert(END," Months  ")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END," THATS SUPER IMPRESIVE   ")
                TXT.insert(END,"\n")
                TXT.insert(END,"\n")
                TXT.insert(END," The thing I want to say is  wake up now you have waisted so many Months in your life  go and do somthing ")
                TXT.insert(END,"before you die work hard and make your life good")


            
                
            
            
            
        

    
       

        



        #frame on root

        Main_Frame=Frame(self.root,width=600,height=500,bg="red")
        Main_Frame.place(x=0,y=0)

        Frame_on_top=Frame(Main_Frame,width=600,height=100,bg="gray75",bd=4,relief=RIDGE)
        Frame_on_top.place(x=0,y=0)

        Frame_on_Middle=Frame(Main_Frame,width=600,height=300,bg="gray75",bd=4,relief=RIDGE)
        Frame_on_Middle.place(x=0,y=100)

        Frame_on_Bottom=Frame(Main_Frame,width=600,height=100,bg="gray75",bd=4,relief=RIDGE)
        Frame_on_Bottom.place(x=0,y=400)

        #frame on top
        lab_frame=LabelFrame(Frame_on_top,text="Select your birth date",font=('times new roman',11,'bold'),width=590,heigh=90)
        lab_frame.place(x=1,y=0)

        Day_list=list(range(1,32))
        Day_combo=Combobox(lab_frame,values=Day_list,font=('arial',10),width=15,state="readonly",textvariable=Days)
        Day_combo.set("Day")
        Day_combo.place(x=60,y=10)


        Month_list=list(range(1,13))
        Month_combo=Combobox(lab_frame,values=Month_list,font=('arial',10),width=15,state="readonly",textvariable=Months)
        Month_combo.set("Month")
        Month_combo.place(x=220,y=10)

        Year_list=list(range(1950,2050))
        year_combo=Combobox(lab_frame,values=Year_list,font=('arial',10),width=15,state="readonly",textvariable=Years)
        year_combo.set("Year")
        year_combo.place(x=380,y=10)


        #frame_on_middle==============================
        #textarea on frame
        TXT=Text(Frame_on_Middle, width=84,height=18,font=('arial',10,'bold'),bd=1,bg="gray95",relief=RIDGE,state="normal")
        TXT.grid(row=0,column=0)
        TXT.insert(END,"\t\t\t     ######******RULES******######")
        TXT.insert(END,"\n")
        TXT.insert(END,"\n")
        TXT.insert(END,"Select your birth date to find out your age ,the days you have lived up till now the months     you live up till now")
        TXT.insert(END,"\n")
        TXT.insert(END,"\n")
        TXT.insert(END,"left birthday days:- for that you have to select your this  year birth date")

        #frame_on_buttom==================================================
        But_Show_Calander=Button(Frame_on_Bottom,text="Calendar",width=13,height=1,relief=RIDGE,bd=3,font=("times new roman",11,"bold"),cursor="hand2",command=show_calnder)
        But_Show_Calander.place(x=20,y=10)
        But_Show_Calander.bind("<Enter>",on_enter1)
        But_Show_Calander.bind("<Leave>",on_leave1)

        But_Birth_this_year=Button(Frame_on_Bottom,text="Selected Date",width=13,height=1,relief=RIDGE,bd=3,font=("times new roman",11,"bold"),cursor="hand2",command=search_date)
        But_Birth_this_year.place(x=160,y=10)
        But_Birth_this_year.bind("<Enter>",on_enter2)
        But_Birth_this_year.bind("<Leave>",on_leave2)

        But_Days_tills_alive=Button(Frame_on_Bottom,text="Days you lived",width=13,height=1,relief=RIDGE,bd=3,font=("times new roman",11,"bold"),cursor="hand2",command=days_live)
        But_Days_tills_alive.place(x=300,y=10)
        But_Days_tills_alive.bind("<Enter>",on_enter3)
        But_Days_tills_alive.bind("<Leave>",on_leave3)

        But_Clear=Button(Frame_on_Bottom,text="Clear All",width=13,height=1,relief=RIDGE,bd=3,font=("times new roman",11,"bold"),command=Clear,cursor="hand2")
        But_Clear.place(x=440,y=10)
        But_Clear.bind("<Enter>",on_enter4)
        But_Clear.bind("<Leave>",on_leave4)

        But_Exit=Button(Frame_on_Bottom,text="Exit",width=13,height=1,relief=RIDGE,bd=3,font=("times new roman",11,"bold"),command=Exit,cursor="hand2")
        But_Exit.place(x=440,y=55)
        But_Exit.bind("<Enter>",on_enter5)
        But_Exit.bind("<Leave>",on_leave5)

        But_left_birthdays_days=Button(Frame_on_Bottom,text="left birthday Days",width=13,height=1,relief=RIDGE,bd=3,font=("times new roman",11,"bold"),cursor="hand2",command=left_birthdays)
        But_left_birthdays_days.place(x=20,y=55)
        But_left_birthdays_days.bind("<Enter>",on_enter6)
        But_left_birthdays_days.bind("<Leave>",on_leave6)

        But_Months_till_alive=Button(Frame_on_Bottom,text="Months you lived",width=13,height=1,relief=RIDGE,bd=3,font=("times new roman",11,"bold"),cursor="hand2",command=months_left)
        But_Months_till_alive.place(x=300,y=55)
        But_Months_till_alive.bind("<Enter>",on_enter7)
        But_Months_till_alive.bind("<Leave>",on_leave7)

        But_Years_old=Button(Frame_on_Bottom,text="Years old",width=13,height=1,relief=RIDGE,bd=3,font=("times new roman",11,"bold"),cursor="hand2",command=years_old)
        But_Years_old.place(x=160,y=55)
        But_Years_old.bind("<Enter>",on_enter8)
        But_Years_old.bind("<Leave>",on_leave8)

        

        







if __name__ == "__main__":
    root=Tk()
    app=pclander(root)
    root.mainloop()

    
