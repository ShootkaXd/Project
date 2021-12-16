from DbContext import NotesDbContext
from GUIContext import GUIContext

def main() -> None:
    db = NotesDbContext('db.db')

    ctx = GUIContext(db)

    ctx.start_mainloop()

if __name__ == "__main__":
    main()