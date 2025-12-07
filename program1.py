from collections import deque

def program_stack():
    # Menggunakan deque untuk efisiensi PopLeft dan AppendLeft
    stack = deque()
    
    while True:
        print("\n--- Menu Program Stack ---")
        print("a) Append (Masukkan dari kanan/ujung atas)")
        print("b) AppendLeft (Masukkan dari kiri/ujung bawah)")
        print("c) Pop (Keluarkan dari kanan/ujung atas)")
        print("d) PopLeft (Keluarkan dari kiri/ujung bawah)")
        print("e) Clear (Kosongkan Stack)")
        print("f) Keluar")
        print(f"Stack saat ini: {list(stack)}")
        
        pilihan = input("Masukkan pilihan (a/b/c/d/e/f): ").lower()
        
        if pilihan == 'a':
            nilai = input("Masukkan nilai untuk Append: ")
            stack.append(nilai)
            print(f"Nilai '{nilai}' ditambahkan.")
            
        elif pilihan == 'b':
            nilai = input("Masukkan nilai untuk AppendLeft: ")
            stack.appendleft(nilai)
            print(f"Nilai '{nilai}' ditambahkan dari kiri.")
            
        elif pilihan == 'c':
            if stack:
                nilai_pop = stack.pop()
                print(f"Nilai '{nilai_pop}' dikeluarkan (Pop).")
            else:
                print("Stack kosong, tidak bisa Pop.")
                
        elif pilihan == 'd':
            if stack:
                nilai_popleft = stack.popleft()
                print(f"Nilai '{nilai_popleft}' dikeluarkan (PopLeft).")
            else:
                print("Stack kosong, tidak bisa PopLeft.")
                
        elif pilihan == 'e':
            stack.clear()
            print("Stack telah dikosongkan (Clear).")
            
        elif pilihan == 'f':
            print("Program Stack selesai.")
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

program_stack()