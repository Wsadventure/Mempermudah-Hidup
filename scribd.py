import webbrowser
import re

url = input("Masukkan url scribdnya : ")

#awal kode ada di indeks 32 sampai ke indeks 

arr = url.split('/')

# print(f"{arr[4]}")

angka_link = arr[4]

link1 = "https://www.scribd.com/embeds/"
link2 = "/content?start_page=1&view_mode=scroll&access_key=key-fFexxf7r1bzEfWu3HKwf"
link = link1 + angka_link + link2

print(f"Page {link} akan dibuka pada browser di window lain")
webbrowser.open(link)


