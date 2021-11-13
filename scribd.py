import webbrowser

angka_link = input("Masukkan angka yang ada di link Scribdnya : ")
link1 = "https://www.scribd.com/embeds/"
link2 = "/content?start_page=1&view_mode=scroll&access_key=key-fFexxf7r1bzEfWu3HKwf"
link = link1 + angka_link + link2

print(f"Page {link} akan dibuka pada browser di window lain")
webbrowser.open(link)
