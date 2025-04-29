class Playlist:
    def __init__(self):
        self.songs = []

    def add_songs(self,title):
        self.songs.append(title)

    def __getitem__(self,index):
        return self.songs[index]
    
    def __setitem__(self,index,value):
        self.songs[index] = value
    
    def __len__(self):
        return len(self.songs)
    
playlist = Playlist()
playlist.add_songs("Song A")
playlist.add_songs("Song B")
print(playlist[0])
playlist[1] = "song X"
print(playlist[1])
print(len(playlist))
