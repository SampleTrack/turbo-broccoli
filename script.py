class Script:
    START_TXT = """
**Hello {}!** 👋

I am an Auto Motivational Post Bot. I manage channels to send daily motivation, riddles, and engagement posts.

**Commands:**
/start - Check if I'm alive
/help - How to use me
/about - Developer info
    """

    HELP_TXT = """
**⚙️ Admin Commands Only:**

`/setchannel [ID]` - Connect a channel
`/setfreq [Minutes]` - Interval between posts
`/enable_riddles [on/off]` - Toggle riddles
`/set_ad [Text/Link]` - Set footer ad for money
`/remove_ad` - Remove current ad
`/ban [ID]` - Ban a user
`/unban [ID]` - Unban a user
`/users` - Get user stats
    """

    ABOUT_TXT = """
**🤖 Bot:** Auto Motivational Sender
**📚 Library:** Pyrogram
**💾 Database:** MongoDB (Motor)
**📡 Host:** Render
    """
