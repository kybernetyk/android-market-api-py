# Python Android Market Library

This is a Python port of the [Android Market API Java Project](http://code.google.com/p/android-market-api/)


## Requirements
* [Python 2.5+](http://www.python.org)
* [Protocol Buffers](http://code.google.com/p/protobuf/)

## Install:
Linux:

1. aptitude install libprotobuf-dev
2. wget http://protobuf.googlecode.com/files/protobuf-2.4.1.tar.bz2 && tar -jxf protobuf-2.4.1.tar.bz2
1. cd protobuf-2.4.1/python/
4. sudo python setup.py build
5. If no errors in step 4: sudo python setup.py install

Mac OS:

1. Install homebrew: http://mxcl.github.com/homebrew/
2. brew install protobuf
3. curl -o protobuf-2.4.1.tar.bz2 http://protobuf.googlecode.com/files/protobuf-2.4.1.tar.bz2 && tar -jxf protobuf-2.4.1.tar.bz2
4. sudo python setup.py build
5. If no errors in step 4: sudo python setup.py install

## Usage

Begin by starting a new session and entering your google credentials.

    session = MarketSession()
    session.login("user@gmail.com", "password")
    
Search for "bankdroid" on the market and print the first result

    results = session.searchApp("bankdroid")
    app = results[0]
    pprint(app)

which prints:

    {'apptype': 1L,
     'creator': u'Nullbyte',
     'creatorid': u'Nullbyte',
     'id': u'-4924482311466714951',
     'packagename': u'com.liato.bankdroid',
     'rating': u'4.526643598615917',
     'ratingscount': 1445L,
     'title': u'Bankdroid',
     'version': u'1.6.3',
     'versioncode': 102L,
     'extendedinfo': {'category': u'Finance',
                      'contactemail': u'android@nullbyte.eu',
                      'contactwebsite': u'http://github.com/liato/android-bankdroid',
                      'downloadscount': 0L,
                      'downloadscounttext': u'10,000-50,000',
                      'installsize': 1323486L,
                      'packagename': u'com.liato.bankdroid',
                      'screenshotscount': 2L
    ...
    }

Print the last two comments for the app

    results = session.getComments(app["id"])
    pprint(results[:2])
    
and you get:

    [{'authorid': u'02028671193556683049',
      'authorname': u'Vincent',
      'creationtime': 1299254796868L,
      'rating': 5L,
      'text': u'Changed my (everyday) life!'},
     {'authorid': u'15970848302407799024',
      'authorname': u'primetomas',
      'creationtime': 1299101108485L,
      'rating': 5L,
      'text': u'This is awesome. Keep up the good work!'}]
    
Download and save the first screenshot to disk:

    data = session.getImage(app["id"])
    f = open("screenshot.png", "wb")
    f.write(data)
    f.close()

Download and save the app icon to disk:

    data = session.getImage(app["id"], imagetype=market_proto.GetImageRequest.ICON)
    f = open("icon.png", "wb")
    f.write(data)
    f.close()
    
Get all the categories and subcategories:

    results = session.getCategories()
    pprint(results)
    
Prints:

    [{'apptype': 1L,
      'subcategories': [{'apptype': 1L,
                         'subtitle': u'Pandora Radio, Google Maps, Gmail',
                         'title': u'All applications'},
                        {'apptype': 1L,
                         'categoryid': u'BOOKS_AND_REFERENCE',
                         'subtitle': u'Google Sky Map, Dictionary.com, Bible',
                         'title': u'Books & Reference'},
                         ...],
      'title': u'APPLICATION'},
    ...
    ]


Check out [examples.py](blob/master/examples.py) for working examples.

## License

MIT