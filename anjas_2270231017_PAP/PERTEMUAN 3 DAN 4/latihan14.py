data = "ini adalah string"
print(data)
print(type(data))
# 1. cara membuat string
'''
 1. dengan menggunakan single quote '...'
 2. dengan menggunakan double quote "..."
'''
data = 'Menggunakan single quote'
print(data)
data = "Menggunakan double quote"
print(data)
print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")
# 2. Menggunakan tanda \
# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')
# backlash
print("C:\\user\\Ucup")
# tab
print("ucup\t\t\t otong, semakin jauhan" )
# backspace
print("ucup \b otong, jadi deketan")
# newline
print("baris pertama.\n baris kedua.") # LF -> line feed -> unix, macos,
#linux
print(" baris pertama.\r baris kedua.") # CR -> carriage return ->commodore, acorn, lisp
print(" baris pertama.\r \n baris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows
# 3. String literal atau raw
# hati-hati
print('C:\new folder') # akan salah pathnya
# menggunakan raw string
print(r'C:\ new folder')
# multiline literal string

print("""Nama : UcupKelas : 3 SD""")
# multiline literal string dan RAW
print("""
Nama : Ucup
Kelas : 3 SD 
""")
# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD new normal 
Website : www.ucup.com/newID
""")