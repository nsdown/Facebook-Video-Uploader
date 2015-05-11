## this example uses sqlite
#Download sqlite browser app for dealing with your database here:
#http://sqlitebrowser.org/


#from peewee import *
import peewee


db = peewee.SqliteDatabase('VideoUploads.db')

class Video(peewee.Model):
    vid_url = peewee.CharField(max_length=4096)
    
    class Meta:
        database = db # This model uses the "people.db" database.

def addVideo(vid_url):
    vid = Video(vid_url=vid_url)
        vid.save()
            print "Added video", vid_url

def videoExists(vid_url):
    try:
    return Video.get(Video.vid_url == vid_url)
        except Video.DoesNotExist:
            return False

# Only create the tables if they do not exist.
db.create_tables([Video], safe=True)

