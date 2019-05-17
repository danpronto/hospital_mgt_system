__author__ = 'procoded'

from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import patDbase


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("MEDICAL RECORDS MANAGEMENT")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg = "powder blue")                # I might as well use "configure" and "background" for "fig" and "bg"


        Tops = Frame(root, bg = "Cadet Blue", bd = 20, pady =1, relief = RIDGE)
        Tops.pack(side = TOP)

        lblTitle = Label(Tops, font = ("arial", 44, "bold"), text = "MEDICAL RECORDS MANAGEMENT SYSTEM", bd = 5, bg = "Cadet Blue",
                 fg = "Cornsilk", justify = "center" )
        lblTitle.grid(row = 0, column = 0)


        LeftFrame = Frame(root, bd = 10, width =450, height = 570, padx = 2, relief = RIDGE, bg = "powder blue")
        LeftFrame.pack(side = LEFT)

        RightFrame = Frame(root, bd = 14, width =900, height = 550, padx = 20, relief = RIDGE, bg = "cadet blue")
        RightFrame.pack(side = RIGHT)



        Fullname = StringVar()
        Gender = StringVar()
        Phone = StringVar()
        DOB = StringVar()
        Mstatus = StringVar()
        PolID = StringVar()
        HInsurer = StringVar()
        ExDate = StringVar()
        Sname = StringVar()
        SAddy = StringVar()
        SPhone = StringVar()
        SRelate = StringVar()
        Famstory = StringVar()
        Medstory = StringVar()
        Medication = StringVar()
        Trestory = StringVar()
        patID = StringVar()
        Nationality = StringVar()
        Addy = StringVar()

#===============================================functions===============================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("MEDICAL RECORDS MANAGEMENT", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearRec():
            self.txtpatID.delete(0,END)
            self.txtFullname.delete(0,END)
            self.txtDOB.delete(0,END)
            self.cboGender.set("")
            self.txtPhone.delete(0,END)
            self.cboMstatus.set("")
            self.txtAddy.delete(0,END)
            self.cboHInsurer.set("")
            self.txtPolID.delete(0,END)
            self.txtExDate.delete(0,END)
            self.cboNationality.set("")
            self.txtSname.delete(0,END)
            self.txtSAddy.delete(0,END)
            self.txtSPhone.delete(0,END)
            self.cboSRelate.set("")
            self.txtFamstory.delete(0,END)
            self.txtMedstory.delete(0,END)
            self.txtMedication.delete(0,END)
            self.txtTrestory.delete(0,END)

        def addRec():
            if (len(patID.get()) != 0):
                patDbase.addPatRec(patID.get(), Fullname.get(), DOB.get(), Gender.get(), Phone.get(), Mstatus.get(), Addy.get(), HInsurer.get(), PolID.get(), ExDate.get(), \
                    Nationality.get(), Sname.get(), SAddy.get(), SPhone.get(), SRelate.get(), Famstory.get(), Medstory.get(), Medication.get(), Trestory.get())
                patList.delete(0, END)
                patList.insert(END,(patID.get(), Fullname.get(), DOB.get(), Gender.get(), Phone.get(), Mstatus.get(), Addy.get(), HInsurer.get(), PolID.get(), \
                    ExDate.get(), Nationality.get(), Sname.get(), SAddy.get(), SPhone.get(), SRelate.get(), Famstory.get(), Medstory.get(), Medication.get(), Trestory.get()))

        def DisplayRec():
            patList.delete(0,END)
            for row in patDbase.viewPatRec():
                patList.insert(END, row, str(""))


        def globalRec(event):
            global sd
            searchPat = patList.curselection()[0]
            sd = patList.get(searchPat)

            self.txtpatID.delete(0,END)
            self.txtpatID.insert(END, sd[1])
            self.txtFullname.delete(0,END)
            self.txtFullname.insert(END, sd[2])
            self.txtDOB.delete(0,END)
            self.txtDOB.insert(END, sd[3])
            self.cboGender.delete(0,END)
            self.cboGender.insert(END, sd[4])
            self.txtPhone.delete(0,END)
            self.txtPhone.insert(END, sd[5])
            self.cboMstatus.delete(0,END)
            self.cboMstatus.insert(END, sd[6])
            self.txtAddy.delete(0,END)
            self.txtAddy.insert(END, sd[7])
            self.cboHInsurer.delete(0, END)
            self.cboHInsurer.insert(END, sd[8])
            self.txtPolID.delete(0,END)
            self.txtPolID.insert(END, sd[9])
            self.txtExDate.delete(0,END)
            self.txtExDate.insert(END, sd[10])
            self.cboNationality.delete(0,END)
            self.cboNationality.insert(END, sd[11])
            self.txtSname.delete(0,END)
            self.txtSname.insert(END, sd[12])
            self.txtSAddy.delete(0,END)
            self.txtSAddy.insert(END, sd[13])
            self.txtSPhone.delete(0,END)
            self.txtSPhone.insert(END, sd[14])
            self.cboSRelate.delete(0,END)
            self.cboSRelate.insert(END, sd[15])
            self.txtFamstory.delete(0,END)
            self.txtFamstory.insert(END, sd[16])
            self.txtMedstory.delete(0,END)
            self.txtMedstory.insert(END, sd[17])
            self.txtMedication.delete(0,END)
            self.txtMedication.insert(END, sd[18])
            self.txtTrestory.delete(0,END)
            self.txtTrestory.insert(END, sd[19])




        def deleteRec():
            if (len(patID.get() != 0)):
                patDbase.deletePatRec(sd[0])
            clearRec()
            DisplayRec()


        def serchDbase():
            patList.delete(0, END)
            for row in patDbase.searchData(patID.get(), Fullname.get(), DOB.get(), Gender.get(), Phone.get(), Mstatus.get(), Addy.get(), HInsurer.get(), PolID.get(), \
                    ExDate.get(), Nationality.get(), Sname.get(), SAddy.get(), SPhone.get(), SRelate.get(), Famstory.get(), Medstory.get(), Medication.get(), Trestory.get()):
                patList.insert(END, row, str(""))

        def update():
            if (len(patID.get() != 0)):
                patDbase.deletePatRec(sd(0))

            if (len(patID.get() != 0)):
                patDbase.addRec(patID.get(), Fullname.get(), DOB.get(), Gender.get(), Phone.get(), Mstatus.get(), Addy.get(), HInsurer.get(), PolID.get(), \
                    ExDate.get(), Nationality.get(), Sname.get(), SAddy.get(), SPhone.get(), SRelate.get(), Famstory.get(), Medstory.get(), Medication.get(), Trestory.get())
                patList.delete(0, END)
                patList.insert(END, (patID.get(), Fullname.get(), DOB.get(), Gender.get(), Phone.get(), Mstatus.get(), Addy.get(), HInsurer.get(), PolID.get(), \
                    ExDate.get(), Nationality.get(), Sname.get(), SAddy.get(), SPhone.get(), SRelate.get(), Famstory.get(), Medstory.get(), Medication.get(), Trestory.get()))

            #===============================================Widget===============================================================
        self.lblpatID = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Patient\'s ID No.:", padx = 2, bg = "powder blue")
        self.lblpatID.grid(row = 0, column = 0, sticky=W)
        self.txtpatID=  Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = patID ,width = 20)
        self.txtpatID.grid(row = 0, column = 1,pady = 3, padx = 20)

        self.lblFullname = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Fullname:", padx = 2, bg = "powder blue")
        self.lblFullname.grid(row = 1, column = 0, sticky=W)
        self.txtFullname = Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = Fullname,width = 20)
        self.txtFullname.grid(row = 1, column = 1,pady = 3, padx = 20)

        self.lblDOB = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Date of Birth:", padx = 2, bg = "powder blue")
        self.lblDOB.grid(row = 2, column = 0, sticky=W)
        self.txtDOB =  Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = DOB ,width = 20)
        self.txtDOB.grid(row = 2, column = 1,pady = 3, padx = 20)

        self.lblGender = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Gender:", padx = 2, bg = "powder blue")
        self.lblGender.grid(row = 3, column = 0, sticky=W)
        self.cboGender = ttk.Combobox(LeftFrame, textvariable = Gender, state = "readonly", font = ("arial", 12, "bold"), width = 18 )

        self.cboGender["value"] = ("", "Male", "Female")
        self.cboGender.current(0)
        self.cboGender.grid(row = 3, column = 1, pady = 3, padx = 20)

        self.lblPhone = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Phone No.:", padx = 2, bg = "powder blue")
        self.lblPhone.grid(row = 4, column = 0, sticky=W)
        self.txtPhone =  Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = Phone ,width = 20)
        self.txtPhone.grid(row = 4, column = 1,pady = 3, padx = 20)

        self.lblMstatus = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Marital Status:", padx = 2, bg = "powder blue")
        self.lblMstatus.grid(row = 5, column = 0, sticky=W)
        self.cboMstatus = ttk.Combobox(LeftFrame, textvariable = Mstatus, state = "readonly", font = ("arial", 12, "bold"), width = 18 )

        self.cboMstatus["value"] = ("", "Single", "Married", "Widowed", "Divorced")
        self.cboMstatus.current(0)
        self.cboMstatus.grid(row = 5, column = 1, pady = 3, padx = 20)

        self.lblAddy= Label(LeftFrame, font = ("arial", 12, "bold"), text = "Address:", padx = 2, bg = "powder blue")
        self.lblAddy.grid(row = 6, column = 0, sticky=W)
        self.txtAddy = Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = Addy,width = 20)
        self.txtAddy.grid(row = 6, column = 1,pady = 3, padx = 20)

        self.lblHInsurer = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Health Insurer:", padx = 2, bg = "powder blue")
        self.lblHInsurer.grid(row = 7, column = 0, sticky=W)
        self.cboHInsurer= ttk.Combobox(LeftFrame, textvariable = HInsurer, state = "readonly", font = ("arial", 12, "bold"), width = 18 )

        self.cboHInsurer["value"] = ("", "NHIS", "Second", "Third", "Fourth")
        self.cboHInsurer.current(0)
        self.cboHInsurer.grid(row = 7, column = 1, pady = 3, padx = 20)

        self.lblPolID = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Policy No.:", padx = 2, bg = "powder blue")
        self.lblPolID.grid(row = 8, column = 0, sticky=W)
        self.txtPolID= Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = PolID,width = 20)
        self.txtPolID.grid(row = 8, column = 1,pady = 3, padx = 20)

        self.lblExDate= Label(LeftFrame, font = ("arial", 12, "bold"), text = "Expiring Date:", padx = 2, bg = "powder blue")
        self.lblExDate.grid(row = 9, column = 0, sticky=W)
        self.txtExDate= Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = ExDate,width = 20)
        self.txtExDate.grid(row = 9, column = 1,pady = 3, padx = 20)

        self.lblNationality = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Nationality:", padx = 2, bg = "powder blue")
        self.lblNationality.grid(row = 10, column = 0, sticky=W)
        self.cboNationality = ttk.Combobox(LeftFrame, textvariable = Nationality, state = "readonly", font = ("arial", 12, "bold"), width = 18 )

        self.cboNationality ["value"] = ("","Afghan", "Albanian","Algerian","American",
                    "Andorran","Angolan","Antiguans","Argentinean","Armenian","Australian","Austrian","Azerbaijan",
                    "Bahamian","Bahraini","Bangladesh","Barbadian","Barbudans","Batswana","Belarusian","Belgian",
                    "Belizean","Beninese","Bhutanese","Bolivian","Bosnian","Brazilian","British","Bruneian",
                    "Bulgarian","Burkinabe","Burmese","Burundian","Cambodian","Cameroonian","Canadian","Cape Verde",
                    "Central African","Chadian","Chilean","Chinese","Colombian","Comoran","Congolese",
                    "Costa Rican","Croatian","Cuban","Cypriot","Czech","Danish","Djibouti","Dominican",
                    "Dominican","Dutch","Dutchman","Dutchwoman","East Timorese","Ecuadorean","Egyptian","Emirian","Equatorial Guinean",
                    "Eritrean","Estonian","Ethiopian","Fijian","Filipino","Finnish","French","Gabonese",
                    "Gambian","Georgian","German","Ghanaian","Greek","Grenadian","Guatemalan","Guinea-Bissauan",
                    "Guinean","Guyanese","Haitian","Herzegovinian","Honduran","Hungarian","I-Kiribati","Icelander",
                    "Indian","Indonesian""Iranian","Iraqi","Irish","Irish","Israeli","Italian",
                    "Ivorian","Jamaican","Japanese","Jordanian","Kazakhstani","Kenyan","Kittian/Nevisian","Kuwaiti",
                    "Kyrgyz","Laotian","Latvian","Lebanese","Liberian","Libyan","Liechtensteiner","Lithuanian",
                    "Luxembourger","Macedonian","Malagasy","Malawian","Malaysian","Maldivan","Malian","Maltese","Marshallese",
                    "Mauritanian","Mauritian","Mexican","Micronesian","Moldovan","Monacan","Mongolian","Moroccan",
                    "Mosotho","Motswana","Mozambican","Namibian","Nauruan","Nepalese","Netherlander","New Zealander",
                    "Ni-Vanuatu","Nicaraguan","Nigerian","Nigerien","North Korean","Northern Irish","Norwegian","Omani",
                    "Pakistani","Palauan","Panamanian","Papua New Guinean","Paraguayan","Peruvian","Polish","Portuguese",
                    "Qatari","Romanian","Russian","Rwandan","Saint Lucian","Salvadoran","Samoan","San Marinese",
                    "Sao Tomean","Saudi","Scottish","Senegalese","Serbian","Seychellois","Sierra Leonean","Singaporean",
                    "Slovakian","Slovenian","Solomon Islander","Somali","South African","South Korean","Spanish","Sri Lankan",
                    "Sudanese","Surinamer","Swazi","Swedish","Swiss","Syrian","Taiwanese","Tajik",
                    "Tanzanian","Thai","Togolese","Tongan","Trinidadian/Tobagonian","Tunisian",
                    "Turkish","Tuvaluan","Ugandan","Ukrainian","ruguayan","Uzbekistani","Venezuelan","Vietnamese",
                    "Welsh","Yemenite","Zambian","Zimbabwean")
        self.cboNationality.current(0)
        self.cboNationality.grid(row = 10, column = 1, pady = 3, padx = 20)

        self.lblSname = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Surety Name:", padx = 2, bg = "powder blue")
        self.lblSname.grid(row = 11, column = 0, sticky=W)
        self.txtSname = Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = Sname,width = 20)
        self.txtSname.grid(row = 11, column = 1,pady = 3, padx = 20)

        self.lblSAddy = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Surety Address:", padx = 2, bg = "powder blue")
        self.lblSAddy.grid(row = 12, column = 0, sticky=W)
        self.txtSAddy = Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = SAddy,width = 20)
        self.txtSAddy.grid(row = 12, column = 1,pady = 3, padx = 20)

        self.lblSPhone = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Surety Phone No.:", padx = 2, bg = "powder blue")
        self.lblSPhone.grid(row = 13, column = 0, sticky=W)
        self.txtSPhone = Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = SPhone,width = 20)
        self.txtSPhone.grid(row = 13, column = 1,pady = 3, padx = 20)

        self.lblSRelate= Label(LeftFrame, font = ("arial", 12, "bold"), text = "Relationship:", padx = 2, bg = "powder blue")
        self.lblSRelate.grid(row = 14, column = 0, sticky=W)
        self.cboSRelate = ttk.Combobox(LeftFrame, textvariable = SRelate, state = "readonly", font = ("arial", 12, "bold"), width = 18 )

        self.cboSRelate["value"] = ("", "Son", "Daughter","Uncle", "Aunt", "Husband", "Wife", "Son-in-Law", "Daughter-in-Law",
                                    "Step son", "Step daughter", "Father-in-Law", "Mother-in-Law", "Colleague", "Employer", "Others")
        self.cboSRelate.current(0)
        self.cboSRelate.grid(row = 14, column = 1, pady = 3, padx = 20)

        self.lblFamstory = Label(LeftFrame, font = ("arial", 12, "bold"), text = "F\\Medical History:", padx = 2, bg = "powder blue")
        self.lblFamstory.grid(row = 15, column = 0, sticky=W)
        self.txtFamstory=  Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = Famstory ,width = 20)
        self.txtFamstory.grid(row = 15, column = 1,pady = 3, padx = 20)

        self.lblMedstory = Label(LeftFrame, font = ("arial", 12, "bold"), text = "P\\Medical History:", padx = 2, bg = "powder blue")
        self.lblMedstory.grid(row = 16, column = 0, sticky=W)
        self.txtMedstory=  Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = Medstory ,width = 20)
        self.txtMedstory.grid(row = 16, column = 1,pady = 3, padx = 20)

        self.lblMedication = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Medication History:", padx = 2, bg = "powder blue")
        self.lblMedication.grid(row = 17, column = 0, sticky=W)
        self.txtMedication =  Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = Medication ,width = 20)
        self.txtMedication.grid(row = 17, column = 1,pady = 3, padx = 20)

        self.lblTrestory = Label(LeftFrame, font = ("arial", 12, "bold"), text = "Treatment History:", padx = 2, bg = "powder blue")
        self.lblTrestory.grid(row = 18, column = 0, sticky=W)
        self.txtTrestory=  Entry(LeftFrame, font = ("arial", 12, "bold"), textvariable = Trestory ,width = 20)
        self.txtTrestory.grid(row = 18, column = 1,pady = 3, padx = 20)


#===============================================Listbox and Scrollbar==============================================================================================================

        scrollbar =Scrollbar(RightFrame)
        scrollbar.grid(row = 1, column = 8, columnspan = 2, sticky = "ns")

        patList = Listbox(RightFrame, width =95, height = 20, bg = "white", bd = 10, font = ("arial", 12, "bold"), yscrollcommand = scrollbar.set)
        patList.bind("<<ListboxSelect>>", globalRec )
        patList.grid(row = 1,column = 0, columnspan = 8)

        self.lblLabel = Label(RightFrame, font = ("arial", 18, "bold"), pady = 0, bg = "Cadet blue", text = "PATIENTS RECORD:")
        self.lblLabel.grid(row = 0, column = 0, columnspan = 7)
        scrollbar.config(command = patList.yview)

#------------------------------------------------------------Buttons-----------------------------------------------------------------------

        self.btnAdd = Button(RightFrame, padx = 16, pady = 1, bd = 7, fg = "black", font = ("arial", 16, "bold"), width =4,text = "Add New",
                  bg = "Powder blue", command = addRec)
        self.btnAdd.grid(row = 2,column = 0)

        self.btnDisplay= Button(RightFrame, padx = 16, pady = 1, bd = 7, fg = "black", font = ("arial", 16, "bold"), width =4,text = "Display",
                    bg = "Powder blue", command = DisplayRec)
        self.btnDisplay.grid(row = 2,column = 1)

        self.btnClear= Button(RightFrame, padx = 16, pady = 1, bd = 7, fg = "black", font = ("arial", 16, "bold"), width =4,
                  text = "Clear", bg = "Powder blue", command = clearRec)
        self.btnClear.grid(row = 2,column = 2)

        self.btnDelete = Button(RightFrame, padx = 16, pady = 1, bd = 7, fg = "black", font = ("arial", 16, "bold"), width =4,
                text = "Delete", bg = "Powder blue", command = deleteRec)
        self.btnDelete.grid(row = 2,column = 3)

        self.btnSearch= Button(RightFrame, padx = 16, pady = 1, bd = 7, fg = "black", font = ("arial", 16, "bold"), width =4,text = "Search",
                  bg = "Powder blue", command = serchDbase)
        self.btnSearch.grid(row = 2,column = 4)

        self.btnUpdate= Button(RightFrame, padx = 16, pady = 1, bd = 7, fg = "black", font = ("arial", 16, "bold"), width =4,text = "Update",
                    bg = "Powder blue", command = update)
        self.btnUpdate.grid(row = 2,column = 5)

        #self.btnPrint= Button(RightFrame, padx = 16, pady = 1, bd = 7, fg = "black", font = ("arial", 16, "bold"), width =4,
            #      text = "Print", bg = "Powder blue")
        #self.btnPrint.grid(row = 2,column = 6)

        self.btnExit= Button(RightFrame, padx = 16, pady = 1, bd = 7, fg = "black", font = ("arial", 16, "bold"), width =4,
                  text = "Exit", bg = "Powder blue", command = iExit)
        self.btnExit.grid(row = 2,column = 6)






if __name__ == "__main__":              #it is important to close the system with this four lines of codes
    root = Tk()
    application = Hospital(root)
    root.mainloop()