import webbrowser

raw_input(('\n' * 50) + 'Folders')
print

"""
TODO:
    [ ] Remotely create/edit/remove bookmarks
    [x] by implementing Class system
    [ ] Implement GUI Interface
    [ ] Save bookmarks to / Find bookmarks from text files
    [ ] Parse through browser-generated HTML File to automate adding bookmarks
"""

class Folder:
        
        def __init__(self, bookmarks):
                self.length = len(bookmarks)
                self.bookmarks = bookmarks
                
                entries = range(0, self.length)
                
                for i in entries:
                        entries[i] = bookmarks[i]
                
                self.entries = entries
                
        def without(self, delete):
                replace = []

                for i in self.bookmarks:
                        if i.name != delete:
                                replace.append(i)

                return Folder(replace)

        def add(self, bookmark):
                self.entries.append(bookmark)

class Bookmark:
        def __init__(self, name, url):
                marks = {}
                
                self.name = name
                self.url = marks[name] = url

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Add bookmarks
#-------------------------------------------------------------------------------

x1 = Bookmark( 'Facebook', 'https://www.facebook.com/' )
x2 = Bookmark( 'YouTube', 'https://www.youtube.com/' )
x3 = Bookmark( 'Netflix', 'http://www.netflix.com/WiHome' )

# Create blank folders, print out names of folders
#-------------------------------------------------------------------------------

folders = {}                                                 # {'NAME', 'VALUE'}

for i in range(0,9):
        folders[i] = None

folders[0] = Folder( [x1, x2, x3] )

for i in folders:
        print i

# 
#-------------------------------------------------------------------------------

x = input("\nOpen Folder: ")
folder = folders[x]

# 
#-------------------------------------------------------------------------------

print '\nFolder #' + str(x) + '\n'

# Main loop
#-------------------------------------------------------------------------------

done = False
done2 = False
select = ''

while done == False:

        print "Select operation\n\n" + "0) Add entry\n" + "1) Remove entry\n" + "2) Open entry\n" + "3) End program\n"
        operation = input("Operation: ")

        done2 = False
        
        if operation == 0:
                while done2 == False:
                        
                        print

                        count = 0
                        for bookmark in folder.entries:
                                print str(count) + ') ' + bookmark.name + ': ' + bookmark.url
                                count = count + 1
                        mark = count

                        print str(mark) + ") Back"
                        
                        label = raw_input('\nEntry Label: ')

                        if label == str(mark):
                                done2 = True
                                continue
                        
                        url = raw_input('\nEntry URL: ')
                        
                        if url.startswith('https://') | url.startswith('http://'):
                                folder.add(Bookmark(label, url))
                                done = False
                                done2 = False
                                select = ""
        
        elif operation == 1:
                while select.isdigit() == False & (select != 'all') & done2 == False:

                        print ""

                        count = 0
                        for bookmark in folder.entries:
                                print str(count) + ') ' + bookmark.name + ': ' + bookmark.url
                                count = count + 1
                        mark = count

                        print str(mark) + ") Back"
                        
                        select = raw_input('\nRemove Entry: ')

                        if select.isdigit() == True & (select != mark) & (select != 'all'):
                                done2 = True
                        if select == mark:
                                done2 = True
                                continue
        
                if (int(select) < count) & (int(select) >= 0):
                        folder = folder.without(folder.entries[int(select)].name)
                        for bookmark in folder.entries:
                                print bookmark
                        done = False
                        done2 = False
                        select = ""
        
                if select == 'all':
                        folder = {}
                        done2 = True
                        break
        elif operation == 2:
                while select.isdigit() == False & (select != 'all') & done2 == False:

                        print

                        count = 0
                        for bookmark in folder.entries:
                                print str(count) + ') ' + bookmark.name + ': ' + bookmark.url
                                count = count + 1
                        mark = count
                        
                        print str(mark) + ") Back"
                        
                        select = raw_input('\nOpen Entry: ')

                        if select.isdigit() == True & (select != mark) & (select != 'all'):
                                if(int(select) != count):
                                        done2 = True
                                else:
                                        done2 = True
                        if select == mark:
                                done2 = True
                                continue
        
                if (int(select) < count) & (int(select) >= 0):
                        print (folder.entries[int(select)].url)
                        webbrowser.open_new(folder.entries[int(select)].url)
                        done = False
                        done2 = False
                        select = ""
        
                if select == 'all':
                        for entry in folder.entries:
                                webbrowser.open_new(entry.url)
                        done2 = True
                        break
        else:
                break
