from tkinter import *
from tkinter.messagebox import showinfo

from actions import AgendaActions


class AgendaView:

    def __init__(self):
        self._root = Tk()
        self._btn_new_contact = Button(self._root, text='New contact')
        self._btn_contact_list = Button(self._root, text='Contact list')
        self._btn_exit = Button(self._root, text='Exit')

        # load setup window
        self._window_setup()

    def _window_setup(self):
        # add settings frame
        self._root.title('Agenda')
        self._root.geometry('300x250')
        self._root.resizable(False, False)

        # settings widgets button _btn_new_contact
        self._btn_new_contact.grid(column=0, row=0, padx=10, pady=3)
        self._btn_new_contact['width'] = 30
        self._btn_new_contact['height'] = 4
        self._btn_new_contact['font'] = ("Verdana", "10", "italic", "bold")
        self._btn_new_contact['command'] = self._command_new_contact


        # settings widgets button _btn_contact_list
        self._btn_contact_list.grid(column=0, row=1, padx=10, pady=3)
        self._btn_contact_list['width'] = 30
        self._btn_contact_list['height'] = 4
        self._btn_contact_list['font'] = ("Verdana", "10", "italic", "bold")

        # settings widgets button _btn_exit
        self._btn_exit.grid(column=0, row=2, padx=10, pady=3)
        self._btn_exit['width'] = 30
        self._btn_exit['height'] = 4
        self._btn_exit['font'] = ("Verdana", 10, "italic", "bold")
        self._btn_exit['command'] = self._root.quit

    @staticmethod
    def _command_new_contact():
        agenda_new_contact_view = AgendaNewContactView()
        agenda_new_contact_view.run_view()


    def run_view(self):
        self._root.mainloop()


class AgendaNewContactView:

    def __init__(self):
        self._root = Tk()
        self._pan_main = Frame(self._root)
        self._lbl_name = Label(self._pan_main, text='Name:')
        self._txt_name = Entry(self._pan_main)
        self._lbl_cell_phone = Label(self._pan_main, text='Cell phone:')
        self._txt_cell_phone = Entry(self._pan_main)
        self._lbl_email = Label(self._pan_main, text='Email:')
        self._txt_email = Entry(self._pan_main)
        self._lbl_zip_code = Label(self._pan_main, text='Zip code:')
        self._txt_zip_code = Entry(self._pan_main)
        self._lbl_street = Label(self._pan_main, text='Street:')
        self._txt_street = Entry(self._pan_main)
        self._lbl_neighborhood = Label(self._pan_main, text='Neighborhood:')
        self._txt_neighborhood = Entry(self._pan_main)
        self._lbl_city = Label(self._pan_main, text='City:')
        self._txt_city = Entry(self._pan_main)
        self._lbl_state = Label(self._pan_main, text='State:')
        self._txt_state = Entry(self._pan_main)
        self._btn_search_zip_code = Button(self._root, text='Search zip code')
        self._btn_save = Button(self._root, text='Save')
        self._btn_exit = Button(self._root, text='Exit')

        # load setup window
        self._window_setup()

    def _window_setup(self):
        # add settings frame
        self._root.title('Agenda - New contact')
        self._root.geometry('700x600')
        self._root.resizable(False, False)

        # settings container _pan_main
        self._pan_main['bd'] = 2
        self._pan_main['bg'] = 'lightgrey'
        self._pan_main.pack(pady=20, padx=20, fill="both", expand=True)

        # settings widgets label _lbl_name
        self._lbl_name.place(x=10, y=10)
        self._lbl_name['width'] = 16
        self._lbl_name['height'] = 2
        self._lbl_name['font'] = ("Verdana", 10)

        # settings widgets entry _txt_name
        self._txt_name.place(x=160, y=10)
        self._txt_name['width'] = 30
        self._txt_name['font'] = ("Verdana", 19)

        # settings widgets label _lbl_email
        self._lbl_email.place(x=10, y=60)
        self._lbl_email['width'] = 16
        self._lbl_email['height'] = 2
        self._lbl_email['font'] = ("Verdana", 10)

        # settings widgets entry _txt_email
        self._txt_email.place(x=160, y=60)
        self._txt_email['width'] = 30
        self._txt_email['font'] = ("Verdana", 19)

        # settings widgets label _lbl_cell_phone
        self._lbl_cell_phone.place(x=10, y=110)
        self._lbl_cell_phone['width'] = 16
        self._lbl_cell_phone['height'] = 2
        self._lbl_cell_phone['font'] = ("Verdana", 10)

        # settings widgets entry _txt_cell_phone
        self._txt_cell_phone.place(x=160, y=110)
        self._txt_cell_phone['width'] = 16
        self._txt_cell_phone['font'] = ("Verdana", 19)

        # settings widgets label _lbl_zip_code
        self._lbl_zip_code.place(x=10, y=160)
        self._lbl_zip_code['width'] = 16
        self._lbl_zip_code['height'] = 2
        self._lbl_zip_code['font'] = ("Verdana", 10)

        # settings widgets entry _txt_zip_code
        self._txt_zip_code.place(x=160, y=160)
        self._txt_zip_code['width'] = 16
        self._txt_zip_code['font'] = ("Verdana", 19)

        # settings widgets button _btn_search_zip_code
        self._btn_search_zip_code.place(x=460, y=180)
        self._btn_search_zip_code['width'] = 16
        self._btn_search_zip_code['height'] = 2
        self._btn_search_zip_code['font'] = ("Verdana", 10)
        self._btn_search_zip_code['command'] = self._command_search_zip_code


        # settings widgets label _lbl_street
        self._lbl_street.place(x=10, y=210)
        self._lbl_street['width'] = 16
        self._lbl_street['height'] = 2
        self._lbl_street['font'] = ("Verdana", 10)

        # settings widgets entry _txt_street
        self._txt_street.place(x=160, y=210)
        self._txt_street['width'] = 30
        self._txt_street['font'] = ("Verdana", 19)

        # settings widgets label _lbl_neighborhood
        self._lbl_neighborhood.place(x=10, y=260)
        self._lbl_neighborhood['width'] = 16
        self._lbl_neighborhood['height'] = 2
        self._lbl_neighborhood['font'] = ("Verdana", 10)

        # settings widgets entry _txt_neighborhood
        self._txt_neighborhood.place(x=160, y=260)
        self._txt_neighborhood['width'] = 30
        self._txt_neighborhood['font'] = ("Verdana", 19)

        # settings widgets label _lbl_city
        self._lbl_city.place(x=10, y=310)
        self._lbl_city['width'] = 16
        self._lbl_city['height'] = 2
        self._lbl_city['font'] = ("Verdana", 10)

        # settings widgets entry _txt_city
        self._txt_city.place(x=160, y=310)
        self._txt_city['width'] = 30
        self._txt_city['font'] = ("Verdana", 19)

        # settings widgets label _lbl_state
        self._lbl_state.place(x=10, y=360)
        self._lbl_state['width'] = 16
        self._lbl_state['height'] = 2
        self._lbl_state['font'] = ("Verdana", 10)

        # settings widgets entry _txt_state
        self._txt_state.place(x=160, y=360)
        self._txt_state['width'] = 30
        self._txt_state['font'] = ("Verdana", 19)

        # setting buttons
        self._btn_save.place(x=400, y=520)
        self._btn_save['width'] = 16
        self._btn_save['height'] = 2

        self._btn_exit.place(x=540, y=520)
        self._btn_exit['width'] = 16
        self._btn_exit['height'] = 2
        self._btn_exit['command'] = self._root.quit

    def _state_fields(self, state):
        self._txt_street.config(state = state)
        self._txt_neighborhood.config(state = state)
        self._txt_city.config(state = state)
        self._txt_state.config(state = state)


    def run_view(self):
        self._root.mainloop()

    def _command_search_zip_code(self):
        _zip_code_value = self._txt_zip_code.get()

        if _zip_code_value or len(_zip_code_value) == 8:
            data = AgendaActions.get_zip_code(zip_code=_zip_code_value)
            self._state_fields('normal')

            if data:
                self._txt_street.insert(0, data.get('logradouro'))
                self._txt_neighborhood.insert(0, data.get('bairro'))
                self._txt_city.insert(0, data.get('localidade'))
                self._txt_state.insert(0, data.get('estado'))
            else:
                showinfo("Info", "Zip code not found!")
        else:
            showinfo("Info", "The zip code field is empty")


if __name__ == '__main__':
    view = AgendaNewContactView()
    view.run_view()
