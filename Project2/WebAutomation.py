from selenium import webdriver
from time import sleep

WEBSITE = "https://bandcamp.com"
ARTIST = "Maroon 5"
ALBUM = "Red Pill Blues"
TRACK = "Wait"

# Open Firefox browser
browser = webdriver.Firefox()
# Navigate to WEBSITE
browser.get(WEBSITE)

# Search ARTIST in search box
searchBox = browser.find_element_by_name("q")
searchBox.send_keys(ARTIST)
searchBox.submit()


#----

album_list = browser.find_element_by_class_name('result-items')
albums = album_list.find_elements_by_tag_name('li')

for album in albums:
	if album.find_element_by_class_name('itemtype').text.find('ALBUM') != -1:
		albumName = album.find_element_by_class_name('heading')
		print (albumName.text)
		if albumName.text.find('Best Of Lady Gaga') != -1:
			link = album.find_element_by_link_text(albumName.text)
			link.click()
			break


track_list = browser.find_element_by_id('track_table')
tracks = track_list.find_elements_by_class_name('track_row_view')

for track in tracks:
	trackName = track.find_element_by_class_name('title')
	print(trackName.find_element_by_tag_name('a').text)
	if trackName.text.find('Judas') != -1:
		playButton = track.find_element_by_class_name('play-col')
		playButton.click()
		break


sleep(10)

pauseButton = browser.find_element_by_class_name('playbutton')
pauseButton.click()
