import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Dogsite Example")

    # Create and pack the main label (big text)
    label1 = tk.Label(root, text="dog.example.com", font=("Arial", 24, "bold"))
    label1.pack(pady=(20, 10))

    # Create and pack the second label (smaller text)
    label2 = tk.Label(root, text="This is an example dogsite", font=("Arial", 16))
    label2.pack(pady=(0, 20))

    root.mainloop()

if __name__ == "__main__":
    main()
