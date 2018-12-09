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

# Wait 5 sec (mandatory)
sleep(5)

# Get all results
resultList = browser.find_element_by_class_name('results')
# Get all albums from results
albums = resultList.find_elements_by_tag_name('li')

# Iterate through all albums
for album in albums:
	# Make sure type is album
	if album.find_element_by_class_name('itemtype').text.find('ALBUM') != -1:
		# Get album name
		albumName = album.find_element_by_class_name('heading')
		# Check if it's our album
		if albumName.text.find(ALBUM) != -1:
			print("Album found..")
			# Get link of album and go into
			albumLink = album.find_element_by_link_text(albumName.text)
			albumLink.click()
			break

# Wait 5 sec (mandatory)
sleep(5)

# Get tracks table from results
trackTable = browser.find_element_by_id('track_table')
# Get all tracks
tracks = trackTable.find_elements_by_class_name('track_row_view')

# Iterate through all tracks
for track in tracks:
	# Get track name
	trackName = track.find_element_by_class_name('title')
	# Check if it's out track
	if trackName.text.find(TRACK) != -1:
		print("Track found..")
		# Play music :)
		playButton = track.find_element_by_class_name('play-col')
		playButton.click()
		print("Play music! :)")
		break

# Wait 10 sec
sleep(10)

# Exit browser
browser.close()
print("Exit")