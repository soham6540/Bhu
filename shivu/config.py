class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7147738922"
    sudo_users = "7147738922", "6574393060"
    GROUP_ID = -1002029788751
    TOKEN = "7197840791:AAHR-OqWB2L3cuhPxClWCHOFKi1ndaigTjg"
    mongo_url = "mongodb+srv://DaxxMusic6:TeamDaxx1@cluster0.ln5y16q.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "-1002192923367"
    UPDATE_CHAT = "-1002194284395"
    BOT_USERNAME = "@godess_soulland_bot"
    CHARA_CHANNEL_ID = "-1002163390646"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
