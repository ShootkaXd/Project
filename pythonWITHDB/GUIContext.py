from tkinter import *
from tkinter import ttk
from DbContext import NotesDbContext

class GUIContext:
    def __init__(self, db_context: NotesDbContext) -> None:
        self.__db_context = db_context
        
        self.__root = Tk()
        self.__root.title('To-Do List')
        self.__root.geometry("400x250+500+300")

        self.__todos = Listbox(self.__root, height=10, selectmode='SINGLE')
        b1 = ttk.Button(self.__root, text='Add task', width=20, command=self.add_task)
        b2 = ttk.Button(self.__root, text='Delete', width=20, command=self.delete_task)
        b3 = ttk.Button(self.__root, text='Delete all', width=20, command=self.delete_all)

        l2 = ttk.Label(self.__root, text='Enter task title: ')
        self.__input = ttk.Entry(self.__root, width=21)

        self.__input.place(x=50, y=50)
        self.__todos.place(x=220, y=50)
        l2.place(x=50, y=50)
        b1.place(x=50, y=110)
        b2.place(x=50, y=140)
        b3.place(x=50, y=170)
        self.update_todos()
    
    def updatable(func):
        def wrapper(self):
            func(self)
            self.update_todos()
        return wrapper

    def update_todos(self) -> None:
        self.notes = self.__db_context.get_notes()

        self.__todos.delete(0, 'end')

        for i in self.notes:
            self.__todos.insert(int(i[0]), i[1])

    @updatable
    def add_task(self) -> None:
        text = self.__input.get()

        if (text):
            self.__db_context.post_note(text)
        self.__input.delete(0, 'end')

    @updatable
    def delete_task(self) -> None:
        self.__db_context.delete_note_by_value(
            self.__todos.get(self.__todos.curselection()[0])
        )

    @updatable
    def delete_all(self) -> None:
        self.__db_context.delete_all()

    def start_mainloop(self) -> None:
        self.__root.mainloop()