
"""
<span style="font-family:Papyrus; font-size:1.25em;">

**Json file sample:**

{"in_reply_to_status_id_str":"305159434462691328",<br>

- If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s ID.<br>

"in_reply_to_status_id":305159434462691328,<br>

- If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s ID.<br>

"coordinates":null,<br>

- Represents the geographic location of this Tweet as reported by the user or client application.<br>

"created_at":"Sat Feb 23 03:40:21 +0000 2013",<br>

- UTC time when this Tweet was created.<br>

"truncated":false,<br>

- Indicates whether the value of the text parameter was truncated.<br>

"in_reply_to_user_id_str":"2768501",<br>

- If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s author ID.<br>

"source":"<a href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\">Twitter for iPhone<\/a>",<br>

- Utility used to post the Tweet, as an HTML-formatted string.<br>

"retweet_count":0,<br>

- Number of times this Tweet has been retweeted.<br>

"retweeted":false,<br>

- Indicates whether this Tweet has been Retweeted by the authenticating user.<br>

"geo":null,<br>

- This deprecated attribute has its coordinates formatted as [lat, long], while all other Tweet geo is formatted as [long, lat].<br>

"in_reply_to_screen_name":"abcnews",<br>

- If the represented Tweet is a reply, this field will contain the screen name of the original Tweet’s author.<br>

"is_quote_status":false,<br>

- Indicates whether this is a Quoted Tweet.<br>

======================================================

"entities":{<br>

- Entities which have been parsed out of the text of the Tweet.<br>

"urls":[],<br>

- Represents URLs included in the text of a Tweet.<br>

"hashtags":[],<br>

- Represents hashtags which have been parsed out of the Tweet text.<br>

"user_mentions":[{"indices":[0,8],"screen_name":"abcnews","id_str":"2768501", "name":"ABC News","id":2768501}],<br>

- Represents other Twitter users mentioned in the text of the Tweet.<br>

"symbols":[]},<br>

- Represents symbols, i.e. $cashtags, included in the text of the Tweet.<br>

======================================================

"full_text":"@abcnews About bloody time. Adani only wants FIFO Indian workers for his Bowen basin mines.",<br>

- The "extended_tweet" object provides the "full_text" field that contains the complete, untruncated Tweet message when longer than 140 characters.<br>

"id_str":"305160140833816576",<br>

- The string representation of the unique identifier for this Tweet.<br>

"in_reply_to_user_id":2768501,<br>

-  If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s author ID.<br>

"display_text_range":[0,91],<br>

- Part of the extended Tweet object.  Contain the # of characters in the Tweet?<br>

"favorite_count":0,<br>

- Indicates approximately how many times this Tweet has been liked by Twitter users.<br>

"id":305160140833816576,<br>

- The integer representation of the unique identifier for this Tweet.<br>

"place":null,<br>

- When present, indicates that the tweet is associated (but not necessarily originating from) a Place.<br>

"contributors":null,<br>

- Can't find this field in the documentation.  Deprecated?<br>

"lang":"en",<br>

- When present, indicates a BCP 47 language identifier corresponding to the machine-detected language of the Tweet text, or und if no language could be detected.<br>

======================================================

"user":{<br>

- User object contains Twitter User account metadata that describes the Twitter User referenced.<br>

"utc_offset":36000,<br>

- Deprecated.<br>

"friends_count":1385,<br>

- The number of users this account is following (AKA their “followings”).<br>

"profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/698290934618787840\/SIpBKnWE_normal.jpg",<br>

- A HTTPS-based URL pointing to the user’s profile image.<br>

"listed_count":3,<br>

- The number of public lists that this user is a member of.<br>

"profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",<br>

- Deprecated.<br>

"default_profile_image":false,<br>

- When true, indicates that the user has not uploaded their own profile image and a default image is used instead.<br>

"favourites_count":533,<br>

- The number of Tweets this user has liked in the account’s lifetime.<br>

"description":"Train Driver extraordinaire, proud Union Leftie and Labor supporter.<br>

Cant stand the LNP and their regressive ideas. Mainly political but I do enjoy a laugh.",<br>

- The user-defined UTF-8 string describing their account.<br>

"created_at":"Tue Aug 21 23:23:52 +0000 2012",<br>

- The UTC datetime that the user account was created on Twitter.<br>

"is_translator":false,<br>

- Deprecated.<br>

"profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",<br>

- Deprecated.<br>

"protected":false,<br>

- When true, indicates that this user has chosen to protect their Tweets.<br>

"screen_name":"DazzDicko",<br>

- The screen name, handle, or alias that this user identifies themselves with. screen_names are unique but subject to change.<br>

"id_str":"772466924",<br>

- The string representation of the unique identifier for this User.<br>

"profile_link_color":"1DA1F2",<br>

- Deprecated.<br>

"is_translation_enabled":false,<br>

- Deprecated.<br>

"translator_type":"none",<br>

- Deprecated.<br>

"id":772466924,<br>

- The integer representation of the unique identifier for this User.<br>

"geo_enabled":true,<br>

- Deprecated.<br>

"profile_background_color":"C0DEED",<br>

- Deprecated.<br>

"lang":"en",<br>

- Deprecated.<br>

"has_extended_profile":false,<br>

- Deprecated.<br>

"profile_sidebar_border_color":"C0DEED",<br>

- Deprecated.<br>

"profile_text_color":"333333",<br>

- Deprecated.<br>

"verified":false,<br>

- When true, indicates that the user has a verified account.<br>

"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/698290934618787840\/SIpBKnWE_normal.jpg",<br>

- Deprecated.<br>

"time_zone":"Australia\/Brisbane",<br>

- Deprecated.<br>

"url":null,<br>

- A URL provided by the user in association with their profile.<br>

"contributors_enabled":false,<br>

- Deprecated.<br>

"profile_background_tile":false,<br>

- Deprecated.<br>

********************

"entities":{"description":{"urls":[]}},<br>

- Entities which have been parsed out of the text of the Tweet.<br>

********************

"statuses_count":5176,<br>

- The number of Tweets (including retweets) issued by the user. <br>

"follow_request_sent":false,<br>

- Deprecated.<br>

"followers_count":945,<br>

- The number of followers this account currently has.<br>

"profile_use_background_image":true,<br>

- Deprecated.<br>

"default_profile":true,<br>

- When true, indicates that the user has not altered the theme or background of their user profile.<br>

"following":false,<br>

- Deprecated.<br>

"name":"Daryl Dickson",<br>

- The name of the user, as they’ve defined it. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change.<br>

"location":"Far North Queensland",<br>

- The user-defined location for this account’s profile. Not necessarily a location, nor machine-parseable.<br>

"profile_sidebar_fill_color":"DDEEF6",<br>

- Deprecated.<br>

"notifications":false},<br>

- Deprecated.<br>

======================================================

"favorited":false}<br>

- Indicates whether this Tweet has been liked by the authenticating user.<br>

</span>
"""